import argparse
import hashlib
import json
import math
import os
import shutil
import struct
import sys

from mathutils import Matrix, Vector

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sea_witch_materials import remap_material_uvs


BODY_SUBMESH = "WitchBody"
ARMOR_SUBMESH = "CoralArmor"
POWPOW_SUBMESH = "PowPow"
FISHBONES_SUBMESH = "Fishbones"
ZAPPER_SUBMESH = "Zapper"
RECALL_SUBMESH = "Recall"
MINE_SUBMESH = "ShellFamiliars"
MISSILE_SUBMESH = "LeviathanBolt"


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--target-skn", required=True)
    parser.add_argument("--target-skl", required=True)
    parser.add_argument("--body-donor-skn", required=True)
    parser.add_argument("--body-donor-skl", required=True)
    parser.add_argument("--weapon-donor-skn", required=True)
    parser.add_argument("--weapon-donor-skl", required=True)
    parser.add_argument("--target-mine-skn", required=True)
    parser.add_argument("--target-mine-skl", required=True)
    parser.add_argument("--mine-donor-skn", required=True)
    parser.add_argument("--mine-donor-skl", required=True)
    parser.add_argument("--target-missile-skn", required=True)
    parser.add_argument("--addon-root", required=True)
    parser.add_argument("--out-root", required=True)
    parser.add_argument("--missile-relative", required=True)
    parser.add_argument("--report", required=True)
    argv = sys.argv[sys.argv.index("--") + 1 :] if "--" in sys.argv else sys.argv[1:]
    return parser.parse_args(argv)


def sha256_bytes(value):
    return hashlib.sha256(value).hexdigest()


def sha256_file(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def rounded(value):
    return [round(float(component), 5) for component in value]


def vertex_uv(vertex):
    return struct.unpack_from("<2f", vertex, 44)


def set_uv(vertex, uv):
    struct.pack_into("<2f", vertex, 44, *uv)


def set_skinning(vertex, local_indices, weights):
    struct.pack_into("<4B", vertex, 12, *local_indices)
    struct.pack_into("<4f", vertex, 16, *weights)


def mesh_bounds(helper, vertices):
    positions = [helper.vertex_position(vertex) for vertex in vertices]
    minimum = Vector(tuple(min(position[i] for position in positions) for i in range(3)))
    maximum = Vector(tuple(max(position[i] for position in positions) for i in range(3)))
    return minimum, maximum


def submesh_triangles(skn, name):
    submesh = next((item for item in skn["submeshes"] if item["name"] == name), None)
    if submesh is None:
        raise ValueError(f"Missing donor submesh: {name}")
    raw = skn["indices"][
        submesh["index_start"] : submesh["index_start"] + submesh["index_count"]
    ]
    return submesh, [raw[index : index + 3] for index in range(0, len(raw), 3)]


class RigTarget:
    def __init__(self, helper, skn, joints, influences):
        self.helper = helper
        self.skn = skn
        self.joints = joints
        # An empty SKL influence table means SKN bytes address joint indices
        # directly (used by JinxMine).  Normalize that representation here.
        self.influences = list(influences) if influences else list(range(len(joints)))
        self.by_name = {joint.name: index for index, joint in enumerate(joints)}
        self.palette_by_joint = {
            joint_index: local_index
            for local_index, joint_index in enumerate(self.influences)
        }
        self.globals = helper.global_joint_matrices(joints)
        self.template = bytearray(skn["vertices"][0])
        self.fallbacks = {}

    def normalize_name(self, name):
        aliases = {
            "aHead": "Head",
            "C9L_Middle2": "L_Middle2",
        }
        return aliases.get(name, name)

    def resolve_joint(self, name):
        normalized = self.normalize_name(name)
        if normalized not in self.by_name:
            raise ValueError(f"Target skeleton is missing weighted joint: {name}")
        requested = self.by_name[normalized]
        # These two skin62 weapon helpers exist in the native skin65 skeleton
        # but are intentionally absent from its compact 72-joint SKN palette.
        # Use their closest semantically equivalent weapon joints rather than
        # walking the hierarchy into Pelvis and corrupting the weapon grip.
        explicit_palette_fallbacks = {
            "Minigun": "Minigun_Space",
            "Minigun_Body": "Minigun_Space",
            "Minigun_Handle_Front": "Minigun_Space",
            "Minigun_Handle_Back": "Minigun_Space",
            "Minigun_Strap_Front": "Minigun_Space",
            "Minigun_Strap_Back": "Minigun_Space",
            "Rocket_Launcher_Handle": "Rocket_Launcher_Front",
        }
        if requested not in self.palette_by_joint and normalized == "Root" and "Jaw_Top" in self.by_name:
            explicit_palette_fallbacks["Root"] = "Jaw_Top"
        if requested not in self.palette_by_joint and normalized in explicit_palette_fallbacks:
            fallback_name = explicit_palette_fallbacks[normalized]
            fallback_joint = self.by_name[fallback_name]
            if fallback_joint not in self.palette_by_joint:
                raise ValueError(f"Explicit palette fallback is unavailable: {fallback_name}")
            self.fallbacks[normalized] = fallback_name
            return requested, fallback_joint, self.palette_by_joint[fallback_joint]
        selected = requested
        while selected not in self.palette_by_joint and selected >= 0:
            selected = self.joints[selected].parent
        if selected < 0:
            raise ValueError(f"Target influence palette cannot represent joint: {normalized}")
        if selected != requested:
            self.fallbacks[normalized] = self.joints[selected].name
        return requested, selected, self.palette_by_joint[selected]

    def joint_position(self, name):
        normalized = self.normalize_name(name)
        if normalized not in self.by_name:
            raise ValueError(f"Missing authored anchor joint: {name}")
        return self.globals[self.by_name[normalized]].to_translation()

    def make_vertex(self, position, normal, uv, named_weights):
        entries = sorted(named_weights.items(), key=lambda item: item[1], reverse=True)[:4]
        if not entries:
            entries = [(self.joints[self.influences[0]].name, 1.0)]
        total = sum(max(0.0, float(weight)) for _, weight in entries)
        if total <= 1e-8:
            raise ValueError("Synthetic vertex has no positive skin weights")
        local_indices = [0, 0, 0, 0]
        weights = [0.0, 0.0, 0.0, 0.0]
        for slot, (name, weight) in enumerate(entries):
            _, _, local_index = self.resolve_joint(name)
            local_indices[slot] = local_index
            weights[slot] = max(0.0, float(weight)) / total
        vertex = bytearray(self.template)
        self.helper.set_position(vertex, Vector(position))
        output_normal = Vector(normal)
        if output_normal.length <= 1e-8:
            output_normal = Vector((0.0, 1.0, 0.0))
        output_normal.normalize()
        self.helper.set_normal(vertex, output_normal)
        set_uv(vertex, uv)
        set_skinning(vertex, local_indices, weights)
        return vertex


class Part:
    def __init__(self, name):
        self.name = name
        self.vertices = []
        self.indices = []
        self.sources = {}

    def mark_source(self, name, vertices, triangles):
        row = self.sources.setdefault(name, {"vertices": 0, "triangles": 0})
        row["vertices"] += vertices
        row["triangles"] += triangles


def append_mesh(
    rig,
    part,
    positions,
    faces,
    uvs,
    weights,
    source="authored",
    material=None,
):
    if len(positions) != len(uvs):
        raise ValueError("Position and UV counts differ")
    if material is not None:
        uvs = remap_material_uvs(uvs, material)
    vertex_normals = [Vector((0.0, 0.0, 0.0)) for _ in positions]
    for face in faces:
        a, b, c = (Vector(positions[index]) for index in face)
        normal = (b - a).cross(c - a)
        if normal.length > 1e-8:
            normal.normalize()
            for index in face:
                vertex_normals[index] += normal
    base = len(part.vertices)
    for index, position in enumerate(positions):
        normal = vertex_normals[index]
        if normal.length <= 1e-8:
            normal = Vector((0.0, 1.0, 0.0))
        named_weights = weights[index] if isinstance(weights, list) else weights
        part.vertices.append(rig.make_vertex(position, normal, uvs[index], named_weights))
    part.indices.extend(base + index for face in faces for index in face)
    part.mark_source(source, len(positions), len(faces))


def orthogonal_frame(axis):
    axis = Vector(axis).normalized()
    reference = Vector((0.0, 1.0, 0.0))
    if abs(axis.dot(reference)) > 0.88:
        reference = Vector((1.0, 0.0, 0.0))
    side = axis.cross(reference).normalized()
    up = side.cross(axis).normalized()
    return side, up


def tube_geometry(points, radii, sides=8, twist=0.0):
    points = [Vector(point) for point in points]
    if len(points) < 2 or len(points) != len(radii):
        raise ValueError("Tube needs matching point and radius arrays")
    positions = []
    uvs = []
    for ring, (point, radius) in enumerate(zip(points, radii)):
        if ring == 0:
            tangent = points[1] - points[0]
        elif ring == len(points) - 1:
            tangent = points[-1] - points[-2]
        else:
            tangent = points[ring + 1] - points[ring - 1]
        side, up = orthogonal_frame(tangent)
        for segment in range(sides):
            angle = math.tau * segment / sides + twist * ring
            positions.append(point + radius * (math.cos(angle) * side + math.sin(angle) * up))
            uvs.append((segment / sides, ring / max(1, len(points) - 1)))
    faces = []
    for ring in range(len(points) - 1):
        for segment in range(sides):
            following = (segment + 1) % sides
            a = ring * sides + segment
            b = ring * sides + following
            c = (ring + 1) * sides + following
            d = (ring + 1) * sides + segment
            faces.extend(((a, b, c), (a, c, d)))
    first_center = len(positions)
    positions.append(points[0])
    uvs.append((0.5, 0.0))
    last_center = len(positions)
    positions.append(points[-1])
    uvs.append((0.5, 1.0))
    for segment in range(sides):
        following = (segment + 1) % sides
        faces.append((first_center, following, segment))
        a = (len(points) - 1) * sides + segment
        b = (len(points) - 1) * sides + following
        faces.append((last_center, a, b))
    return positions, faces, uvs


def horn_geometry(base, direction, length, radius, bend, segments=6, sides=8):
    base = Vector(base)
    direction = Vector(direction).normalized()
    bend = Vector(bend)
    points = []
    radii = []
    for index in range(segments + 1):
        t = index / segments
        points.append(base + direction * length * t + bend * (t * t))
        radii.append(max(0.45, radius * (1.0 - t) ** 0.72))
    return tube_geometry(points, radii, sides=sides, twist=0.16)


def ellipsoid_geometry(center, radii, rings=7, segments=14):
    center = Vector(center)
    rx, ry, rz = radii
    positions = []
    uvs = []
    for ring in range(rings + 1):
        latitude = -math.pi * 0.5 + math.pi * ring / rings
        for segment in range(segments):
            longitude = math.tau * segment / segments
            positions.append(
                center
                + Vector(
                    (
                        rx * math.cos(latitude) * math.cos(longitude),
                        ry * math.sin(latitude),
                        rz * math.cos(latitude) * math.sin(longitude),
                    )
                )
            )
            uvs.append((segment / segments, ring / rings))
    faces = []
    for ring in range(rings):
        for segment in range(segments):
            following = (segment + 1) % segments
            a = ring * segments + segment
            b = ring * segments + following
            c = (ring + 1) * segments + following
            d = (ring + 1) * segments + segment
            faces.extend(((a, b, c), (a, c, d)))
    return positions, faces, uvs


def torus_geometry(center, axis, major_radius, minor_radius, major_segments=18, minor_segments=7):
    center = Vector(center)
    axis = Vector(axis).normalized()
    side, up = orthogonal_frame(axis)
    positions = []
    uvs = []
    for major in range(major_segments):
        a = math.tau * major / major_segments
        radial = math.cos(a) * side + math.sin(a) * up
        ring_center = center + major_radius * radial
        for minor in range(minor_segments):
            b = math.tau * minor / minor_segments
            positions.append(
                ring_center + minor_radius * (math.cos(b) * radial + math.sin(b) * axis)
            )
            uvs.append((major / major_segments, minor / minor_segments))
    faces = []
    for major in range(major_segments):
        next_major = (major + 1) % major_segments
        for minor in range(minor_segments):
            next_minor = (minor + 1) % minor_segments
            a = major * minor_segments + minor
            b = next_major * minor_segments + minor
            c = next_major * minor_segments + next_minor
            d = major * minor_segments + next_minor
            faces.extend(((a, b, c), (a, c, d)))
    return positions, faces, uvs


def ribbon_geometry(points, widths, thickness=1.8):
    points = [Vector(point) for point in points]
    positions = []
    uvs = []
    for index, (point, width) in enumerate(zip(points, widths)):
        tangent = points[min(index + 1, len(points) - 1)] - points[max(0, index - 1)]
        side, depth = orthogonal_frame(tangent)
        for offset in (-0.5, 0.5):
            for layer in (-0.5, 0.5):
                positions.append(point + side * width * offset + depth * thickness * layer)
                uvs.append((offset + 0.5, index / max(1, len(points) - 1)))
    faces = []
    for index in range(len(points) - 1):
        a = index * 4
        b = (index + 1) * 4
        faces.extend(
            (
                (a, b, b + 1), (a, b + 1, a + 1),
                (a + 3, b + 3, b + 2), (a + 3, b + 2, a + 2),
                (a, a + 2, b + 2), (a, b + 2, b),
                (a + 1, b + 1, b + 3), (a + 1, b + 3, a + 3),
            )
        )
    return positions, faces, uvs


def source_joint_entries(vertex, joints, influences):
    local_indices = struct.unpack_from("<4B", vertex, 12)
    weights = struct.unpack_from("<4f", vertex, 16)
    entries = []
    for local_index, weight in zip(local_indices, weights):
        if weight <= 1e-7:
            continue
        joint_index = influences[local_index] if influences else local_index
        entries.append((joints[joint_index].name, joint_index, float(weight)))
    return entries


def retarget_vertex(helper, source_vertex, source_joints, source_influences, source_globals, rig):
    source_position = helper.vertex_position(source_vertex)
    source_normal = helper.vertex_normal(source_vertex)
    entries = source_joint_entries(source_vertex, source_joints, source_influences)
    if not entries:
        raise ValueError("Donor vertex has no positive skin weight")
    target_position = Vector((0.0, 0.0, 0.0))
    target_normal = Vector((0.0, 0.0, 0.0))
    local_indices = [0, 0, 0, 0]
    weights = [0.0, 0.0, 0.0, 0.0]
    for slot, (source_name, source_joint_index, weight) in enumerate(entries[:4]):
        target_joint_index, palette_joint_index, local_index = rig.resolve_joint(source_name)
        transform = rig.globals[target_joint_index] @ source_globals[source_joint_index].inverted()
        target_position += weight * (transform @ source_position)
        normal_matrix = transform.to_3x3().inverted().transposed()
        transformed_normal = normal_matrix @ source_normal
        if transformed_normal.length > 1e-8:
            transformed_normal.normalize()
        target_normal += weight * transformed_normal
        local_indices[slot] = local_index
        weights[slot] = weight
    total = sum(weights)
    if total <= 1e-8:
        raise ValueError("Retargeted vertex lost its weights")
    weights = [weight / total for weight in weights]
    if target_normal.length <= 1e-8:
        target_normal = source_normal.copy()
    target_normal.normalize()
    output = bytearray(rig.template)
    helper.set_position(output, target_position)
    helper.set_normal(output, target_normal)
    set_uv(output, vertex_uv(source_vertex))
    set_skinning(output, local_indices, weights)
    return output, [rig.normalize_name(name) for name, _, _ in entries]


def append_retargeted_triangles(
    helper,
    part,
    donor_skn,
    donor_joints,
    donor_influences,
    donor_globals,
    rig,
    triangles,
    source_name,
    deform=None,
):
    ordered = sorted({index for triangle in triangles for index in triangle})
    remap = {}
    for source_index in ordered:
        output, names = retarget_vertex(
            helper,
            donor_skn["vertices"][source_index],
            donor_joints,
            donor_influences,
            donor_globals,
            rig,
        )
        if deform is not None:
            position = helper.vertex_position(output)
            normal = helper.vertex_normal(output)
            new_position, new_normal = deform(position, normal, names)
            helper.set_position(output, new_position)
            if new_normal.length > 1e-8:
                new_normal.normalize()
                helper.set_normal(output, new_normal)
        remap[source_index] = len(part.vertices)
        part.vertices.append(output)
    part.indices.extend(remap[index] for triangle in triangles for index in triangle)
    part.mark_source(source_name, len(ordered), len(triangles))


def body_deform(position, normal, joint_names):
    output = position.copy()
    output_normal = normal.copy()
    lower_body = any(
        name in {"Pelvis", "Spine1", "R_Hip", "L_Hip"} for name in joint_names
    ) and output.y < 112.0
    if lower_body:
        strength = max(0.0, min(1.0, (112.0 - output.y) / 92.0))
        output.x *= 1.0 + 0.13 * strength
        output.z += (3.8 * math.sin(output.x * 0.085 + output.y * 0.043) + 1.6) * strength
    if output.y > 142.0 and any("Hair" in name for name in joint_names):
        output.z += 2.2 * math.sin(output.y * 0.075 + output.x * 0.04)
    return output, output_normal


def weapon_family(vertex, joints, influences):
    scores = {POWPOW_SUBMESH: 0.0, FISHBONES_SUBMESH: 0.0, ZAPPER_SUBMESH: 0.0}
    for name, _, weight in source_joint_entries(vertex, joints, influences):
        lowered = name.lower()
        if "minigun" in lowered or "weapon_" in lowered:
            scores[POWPOW_SUBMESH] += weight
        if "rocket" in lowered:
            scores[FISHBONES_SUBMESH] += weight
        if "pistol" in lowered:
            scores[ZAPPER_SUBMESH] += weight
    return scores


def split_weapon_triangles(donor_skn, donor_joints, donor_influences):
    _, triangles = submesh_triangles(donor_skn, "Weapon")
    result = {POWPOW_SUBMESH: [], FISHBONES_SUBMESH: [], ZAPPER_SUBMESH: []}
    ambiguous = 0
    for triangle in triangles:
        total = {POWPOW_SUBMESH: 0.0, FISHBONES_SUBMESH: 0.0}
        for index in triangle:
            scores = weapon_family(donor_skn["vertices"][index], donor_joints, donor_influences)
            for family in total:
                total[family] += scores[family]
        highest = max(total.values())
        winners = [family for family, score in total.items() if abs(score - highest) <= 1e-7]
        if highest <= 1e-7 or len(winners) != 1:
            ambiguous += 1
            center_x = sum(struct.unpack_from("<f", donor_skn["vertices"][i], 0)[0] for i in triangle)
            family = POWPOW_SUBMESH if center_x >= 0 else FISHBONES_SUBMESH
        else:
            family = winners[0]
        result[family].append(triangle)
    if not result[POWPOW_SUBMESH] or not result[FISHBONES_SUBMESH]:
        raise ValueError(
            "Weapon donor family split is incomplete: "
            + ", ".join(f"{name}={len(rows)}" for name, rows in result.items())
        )
    return result, ambiguous


def find_pistol_triangles(donor_skn, donor_joints, donor_influences):
    result = []
    for submesh in donor_skn["submeshes"]:
        if submesh["name"].lower() in {"babywolf", "crown"}:
            continue
        raw = donor_skn["indices"][
            submesh["index_start"] : submesh["index_start"] + submesh["index_count"]
        ]
        for offset in range(0, len(raw), 3):
            triangle = raw[offset : offset + 3]
            pistol_score = 0.0
            for vertex_index in triangle:
                for name, _, weight in source_joint_entries(
                    donor_skn["vertices"][vertex_index], donor_joints, donor_influences
                ):
                    if "pistol" in name.lower():
                        pistol_score += weight
            if pistol_score > 1e-6:
                result.append(triangle)
    return result


def add_horn(
    rig,
    part,
    base,
    direction,
    length,
    radius,
    bend,
    bone,
    source="authored",
    material=None,
):
    positions, faces, uvs = horn_geometry(base, direction, length, radius, bend)
    append_mesh(
        rig,
        part,
        positions,
        faces,
        uvs,
        {bone: 1.0},
        source=source,
        material=material,
    )


def add_ellipsoid(
    rig,
    part,
    center,
    radii,
    bone,
    source="authored",
    material=None,
):
    positions, faces, uvs = ellipsoid_geometry(center, radii)
    append_mesh(
        rig,
        part,
        positions,
        faces,
        uvs,
        {bone: 1.0},
        source=source,
        material=material,
    )


def add_torus(
    rig,
    part,
    center,
    axis,
    major,
    minor,
    bone,
    source="authored",
    material=None,
):
    positions, faces, uvs = torus_geometry(center, axis, major, minor)
    append_mesh(
        rig,
        part,
        positions,
        faces,
        uvs,
        {bone: 1.0},
        source=source,
        material=material,
    )


def author_armor(rig, armor):
    head = rig.joint_position("Head")
    crown_bases = (-15.0, -9.0, -3.0, 3.0, 9.0, 15.0)
    for index, x_offset in enumerate(crown_bases):
        side = -1.0 if x_offset < 0 else 1.0
        add_horn(
            rig,
            armor,
            head + Vector((x_offset, 6.0 - abs(x_offset) * 0.10, -2.5 + 1.2 * (index % 2))),
            Vector((0.14 * side, 1.0, -0.08 + 0.05 * (index % 3))),
            31.0 + 3.2 * (index % 3),
            4.7 - 0.12 * abs(x_offset),
            Vector((7.5 * side, 1.0, 4.0 * (-1 if index % 2 else 1))),
            "Head",
            material="coral",
        )
    for side, bone in ((-1.0, "L_Clavicle"), (1.0, "R_Clavicle")):
        anchor = rig.joint_position(bone) + Vector((side * 4.0, 1.5, 3.5))
        add_ellipsoid(
            rig, armor, anchor, (15.5, 7.5, 11.0), bone, material="bone"
        )
        for branch in range(3):
            add_horn(
                rig,
                armor,
                anchor + Vector((side * (3.0 + branch * 2.5), 1.0, (branch - 1) * 4.0)),
                Vector((side * (0.72 + 0.08 * branch), 0.42, 0.18 * (branch - 1))),
                23.0 + branch * 4.0,
                4.1 - branch * 0.45,
                Vector((side * 4.0, 6.0, (branch - 1) * 2.5)),
                bone,
                material="coral",
            )
    chest = rig.joint_position("Spine3") + Vector((0.0, -1.5, 8.0))
    add_ellipsoid(
        rig, armor, chest, (15.5, 13.0, 4.8), "Spine3", material="bone"
    )
    # Open coral ribs frame the torso without turning the silhouette into a
    # stack of complete rings.  The earlier full tori obscured the body in the
    # exported front render even though they were technically well skinned.
    for row, y_offset in enumerate((-8.0, 2.5, 12.0)):
        for side in (-1.0, 1.0):
            add_horn(
                rig,
                armor,
                chest + Vector((side * (9.0 + row * 1.2), y_offset, -1.0)),
                Vector((side * 0.80, 0.22, 0.56)),
                12.0 + row * 2.0,
                2.2,
                Vector((side * 3.0, 1.5, 3.0)),
                "Spine2" if row == 0 else "Spine3",
                material="coral",
            )
    pelvis = rig.joint_position("Pelvis")
    for side, dress_bone in ((-1.0, "Buffbone_L_dress"), (1.0, "Buffbone_R_dress")):
        hip_anchor = pelvis + Vector((side * 18.0, 2.0, 1.5))
        add_ellipsoid(
            rig,
            armor,
            hip_anchor,
            (12.5, 9.0, 7.0),
            dress_bone,
            material="abyssal",
        )
        add_horn(
            rig,
            armor,
            hip_anchor + Vector((side * 7.0, 0.0, 0.0)),
            Vector((side * 0.78, -0.55, 0.18)),
            27.0,
            4.0,
            Vector((side * 5.0, -5.0, 4.0)),
            dress_bone,
            material="coral",
        )
    for index in range(6):
        side = -1.0 if index < 3 else 1.0
        lane = index % 3
        dress_bone = "Buffbone_L_dress" if side < 0 else "Buffbone_R_dress"
        start = pelvis + Vector((side * (7.0 + lane * 5.5), -3.0, -2.0 + lane * 4.0))
        points = [
            start,
            start + Vector((side * (3.0 + lane), -22.0, 4.0 * math.sin(index))),
            start + Vector((side * (7.0 + lane * 2.0), -47.0, -5.0 + lane * 4.0)),
            start + Vector((side * (12.0 + lane * 2.0), -72.0, 8.0 * math.sin(index + 1.2))),
        ]
        widths = [11.0 - lane, 9.0 - lane, 6.5, 2.0]
        positions, faces, uvs = ribbon_geometry(points, widths, thickness=2.2)
        append_mesh(
            rig,
            armor,
            positions,
            faces,
            uvs,
            {dress_bone: 1.0},
            material="abyssal",
        )
    bead_bones = ("L_Hair3", "L_Hair5", "R_Hair3", "R_Hair5")
    for index, bone in enumerate(bead_bones):
        anchor = rig.joint_position(bone)
        add_ellipsoid(
            rig,
            armor,
            anchor + Vector((0.0, -2.0, 2.5 * (-1 if index % 2 else 1))),
            (4.2, 5.8, 4.2),
            bone,
            material="seafoam",
        )


def weapon_deformer(root, amount):
    def deform(position, normal, _names):
        relative = position - root
        distance = relative.length
        scale = 1.07 + amount * (0.5 + 0.5 * math.sin(distance * 0.095))
        if distance > 1e-6:
            axis = Vector((1.0, 0.0, 0.0))
            axial = axis * relative.dot(axis)
            radial = relative - axial
            position = root + axial + radial * scale
        return position, normal

    return deform


def author_powpow(rig, part):
    body = rig.joint_position("Minigun_Body")
    barrel = rig.joint_position("Minigun_Barrel1")
    axis = barrel - body
    if axis.length <= 1e-5:
        axis = Vector((1.0, 0.0, 0.0))
    axis.normalize()
    add_torus(rig, part, barrel, axis, 18.0, 4.3, "Minigun_Barrel1")
    add_torus(rig, part, body + axis * 10.0, axis, 24.0, 4.8, "Minigun_Body")
    side, up = orthogonal_frame(axis)
    for index in range(7):
        angle = math.tau * index / 7
        radial = math.cos(angle) * side + math.sin(angle) * up
        add_horn(
            rig,
            part,
            barrel + radial * 15.0 + axis * 4.0,
            axis * 0.55 + radial * 0.85,
            29.0 + 4.0 * (index % 2),
            4.2,
            radial * 7.0 + axis * 3.0,
            "Minigun_Barrel1",
        )
    for bone in ("Minigun_Barrel1", "Minigun_Barrel2", "Minigun_Barrel3"):
        anchor = rig.joint_position(bone)
        points = [anchor - axis * 18.0, anchor + axis * 13.0, anchor + axis * 35.0]
        positions, faces, uvs = tube_geometry(points, (5.5, 7.2, 3.4), sides=9, twist=0.22)
        append_mesh(rig, part, positions, faces, uvs, {bone: 1.0})


def author_fishbones(rig, part):
    front = rig.joint_position("Rocket_Launcher_Front")
    handle = rig.joint_position("Rocket_Launcher_Handle")
    axis = front - handle
    if axis.length <= 1e-5:
        axis = Vector((1.0, 0.0, 0.0))
    axis.normalize()
    side, up = orthogonal_frame(axis)
    add_torus(rig, part, front - axis * 9.0, axis, 20.0, 5.2, "Rocket_Launcher_Front")
    add_ellipsoid(rig, part, front + axis * 6.0, (22.0, 14.0, 17.0), "Rocket_Launcher_Front")
    for sign in (-1.0, 1.0):
        add_horn(
            rig,
            part,
            front + side * sign * 12.0 + up * 7.0,
            axis * 0.45 + side * sign * 0.65 + up * 0.48,
            43.0,
            5.6,
            side * sign * 11.0 + up * 8.0 - axis * 2.0,
            "Rocket_Launcher_Front",
        )
        add_horn(
            rig,
            part,
            front + side * sign * 9.0 - up * 8.0,
            axis * 0.52 + side * sign * 0.55 - up * 0.52,
            34.0,
            4.4,
            side * sign * 7.0 - up * 5.0,
            "Rocket_Launcher_Mouth_Bottom",
        )
    spine_points = [handle - axis * 10.0, handle + axis * 14.0, front - axis * 18.0]
    positions, faces, uvs = tube_geometry(spine_points, (7.0, 11.0, 8.0), sides=10, twist=0.18)
    append_mesh(rig, part, positions, faces, uvs, {"Rocket_Launcher": 1.0})


def author_zapper(rig, part):
    pistol = rig.joint_position("Pistol")
    spine = rig.joint_position("Spine2")
    axis = pistol - spine
    if axis.length <= 1e-5:
        axis = Vector((1.0, 0.0, 0.0))
    axis.normalize()
    side, up = orthogonal_frame(axis)
    add_torus(rig, part, pistol + axis * 5.0, axis, 9.0, 2.8, "Pistol")
    points = [pistol - axis * 10.0, pistol + axis * 9.0, pistol + axis * 24.0]
    positions, faces, uvs = tube_geometry(points, (5.0, 7.0, 2.0), sides=9, twist=0.28)
    append_mesh(rig, part, positions, faces, uvs, {"Pistol": 1.0})
    for sign in (-1.0, 1.0):
        add_horn(
            rig,
            part,
            pistol + side * sign * 6.0 + up * 2.0,
            axis * 0.72 + side * sign * 0.58 + up * 0.24,
            18.0,
            2.7,
            side * sign * 4.0 + up * 3.0,
            "Pistol",
        )


def author_recall(rig, part):
    root = rig.joint_position("Root")
    center = Vector((root.x, max(2.0, root.y + 3.0), root.z))
    add_torus(
        rig,
        part,
        center,
        Vector((0.0, 1.0, 0.0)),
        73.0,
        4.8,
        "recall_wave1",
        material="seafoam",
    )
    add_torus(
        rig,
        part,
        center + Vector((0.0, 3.0, 0.0)),
        Vector((0.0, 1.0, 0.0)),
        48.0,
        3.2,
        "recall_wave2",
        material="bone",
    )
    for index in range(16):
        angle = math.tau * index / 16
        radial = Vector((math.cos(angle), 0.0, math.sin(angle)))
        bone = f"recall_wave{1 + index % 5}"
        add_horn(
            rig,
            part,
            center + radial * 69.0,
            radial * 0.42 + Vector((0.0, 0.91, 0.0)),
            28.0 + 5.0 * (index % 3),
            3.6,
            radial * 8.0 + Vector((0.0, 2.0, 0.0)),
            bone,
            material="coral" if index % 2 else "abyssal",
        )


def combine_parts(helper, template_skn, parts):
    vertices = []
    indices = []
    submeshes = []
    for part in parts:
        vertex_start = len(vertices)
        index_start = len(indices)
        vertices.extend(part.vertices)
        indices.extend(vertex_start + index for index in part.indices)
        submeshes.append(
            {
                "name": part.name,
                "vertex_start": vertex_start,
                "vertex_count": len(part.vertices),
                "index_start": index_start,
                "index_count": len(part.indices),
            }
        )
    if not vertices or not indices:
        raise ValueError("Output model has no geometry")
    if len(vertices) >= 65536 or max(indices) >= 65536:
        raise ValueError(f"Output exceeds SKN uint16 limit: {len(vertices)} vertices")
    output = dict(template_skn)
    output["vertices"] = vertices
    output["indices"] = indices
    output["submeshes"] = submeshes
    return output


def build_champion(helper, read_skl, args):
    target_skn = helper.parse_skn(args.target_skn)
    target_joints, target_influences = read_skl(args.target_skl)
    rig = RigTarget(helper, target_skn, target_joints, target_influences)

    body_skn = helper.parse_skn(args.body_donor_skn)
    body_joints, body_influences = read_skl(args.body_donor_skl)
    body_globals = helper.global_joint_matrices(body_joints)
    _, body_triangles = submesh_triangles(body_skn, "Body")

    weapon_skn = helper.parse_skn(args.weapon_donor_skn)
    weapon_joints, weapon_influences = read_skl(args.weapon_donor_skl)
    weapon_globals = helper.global_joint_matrices(weapon_joints)
    weapon_triangles, ambiguous = split_weapon_triangles(
        weapon_skn, weapon_joints, weapon_influences
    )
    zapper_triangles = find_pistol_triangles(
        weapon_skn, weapon_joints, weapon_influences
    )

    body = Part(BODY_SUBMESH)
    armor = Part(ARMOR_SUBMESH)
    powpow = Part(POWPOW_SUBMESH)
    fishbones = Part(FISHBONES_SUBMESH)
    zapper = Part(ZAPPER_SUBMESH)
    recall = Part(RECALL_SUBMESH)

    append_retargeted_triangles(
        helper,
        body,
        body_skn,
        body_joints,
        body_influences,
        body_globals,
        rig,
        body_triangles,
        "Jinx skin51 Body component",
        deform=body_deform,
    )
    append_retargeted_triangles(
        helper,
        powpow,
        weapon_skn,
        weapon_joints,
        weapon_influences,
        weapon_globals,
        rig,
        weapon_triangles[POWPOW_SUBMESH],
        "Jinx skin62 Pow-Pow component",
        deform=weapon_deformer(rig.joint_position("Minigun"), 0.055),
    )
    append_retargeted_triangles(
        helper,
        fishbones,
        weapon_skn,
        weapon_joints,
        weapon_influences,
        weapon_globals,
        rig,
        weapon_triangles[FISHBONES_SUBMESH],
        "Jinx skin62 Fishbones component",
        deform=weapon_deformer(rig.joint_position("Rocket_Launcher"), 0.045),
    )
    append_retargeted_triangles(
        helper,
        zapper,
        weapon_skn,
        weapon_joints,
        weapon_influences,
        weapon_globals,
        rig,
        zapper_triangles,
        "Jinx skin62 Zapper component",
        deform=weapon_deformer(rig.joint_position("Pistol"), 0.035),
    )
    author_armor(rig, armor)
    author_powpow(rig, powpow)
    author_fishbones(rig, fishbones)
    author_zapper(rig, zapper)
    author_recall(rig, recall)

    output_skn = combine_parts(
        helper, target_skn, [body, armor, powpow, fishbones, zapper, recall]
    )
    relative = "assets/characters/jinx/skins/skin65/jinx_skin65.skn"
    output_path = os.path.join(args.out_root, relative.replace("/", os.sep))
    output_bytes = helper.write_skn(
        output_path,
        output_skn,
        output_skn["submeshes"],
        output_skn["indices"],
        output_skn["vertices"],
    )
    output_skl = os.path.join(
        args.out_root, "assets/characters/jinx/skins/skin65/jinx_skin65.skl".replace("/", os.sep)
    )
    os.makedirs(os.path.dirname(output_skl), exist_ok=True)
    shutil.copy2(args.target_skl, output_skl)
    minimum, maximum = mesh_bounds(helper, output_skn["vertices"])
    return {
        "path": output_path,
        "sha256": sha256_bytes(output_bytes),
        "skeleton_path": output_skl,
        "skeleton_sha256": sha256_file(output_skl),
        "target_skeleton_sha256": sha256_file(args.target_skl),
        "vertices": len(output_skn["vertices"]),
        "triangles": len(output_skn["indices"]) // 3,
        "submeshes": output_skn["submeshes"],
        "sources": {
            part.name: part.sources
            for part in (body, armor, powpow, fishbones, zapper, recall)
        },
        "target_ocean_song_vertices_retained": 0,
        "weapon_split_ambiguous_triangles_resolved_by_bind_side": ambiguous,
        "influence_fallbacks": rig.fallbacks,
        "bounds": {"min": rounded(minimum), "max": rounded(maximum)},
    }


def generic_deform_mine(helper, vertex, center):
    position = helper.vertex_position(vertex)
    normal = helper.vertex_normal(vertex)
    relative = position - center
    position = center + Vector((relative.x * 1.22, relative.y * 0.88, relative.z * 1.17))
    position.z += 2.5 * math.sin(relative.x * 0.09 + relative.y * 0.05)
    return position, normal


def build_mine(helper, read_skl, args):
    target_skn = helper.parse_skn(args.target_mine_skn)
    target_joints, target_influences = read_skl(args.target_mine_skl)
    rig = RigTarget(helper, target_skn, target_joints, target_influences)
    donor_skn = helper.parse_skn(args.mine_donor_skn)
    donor_joints, donor_influences = read_skl(args.mine_donor_skl)
    donor_globals = helper.global_joint_matrices(donor_joints)
    donor_triangles = []
    for submesh in donor_skn["submeshes"]:
        raw = donor_skn["indices"][
            submesh["index_start"] : submesh["index_start"] + submesh["index_count"]
        ]
        donor_triangles.extend(raw[index : index + 3] for index in range(0, len(raw), 3))
    donor_min, donor_max = mesh_bounds(helper, donor_skn["vertices"])
    donor_center = (donor_min + donor_max) * 0.5
    mine = Part(MINE_SUBMESH)

    def deform(position, normal, _names):
        relative = position - donor_center
        output = donor_center + Vector((relative.x * 1.22, relative.y * 0.88, relative.z * 1.17))
        output.z += 2.5 * math.sin(relative.x * 0.09 + relative.y * 0.05)
        return output, normal

    append_retargeted_triangles(
        helper,
        mine,
        donor_skn,
        donor_joints,
        donor_influences,
        donor_globals,
        rig,
        donor_triangles,
        "JinxMine skin62 component",
        deform=deform,
    )
    root_bone = target_joints[target_influences[0]].name
    center = donor_center
    for sign in (-1.0, 1.0):
        shell_center = center + Vector((0.0, sign * 4.0, sign * 8.0))
        add_ellipsoid(rig, mine, shell_center, (30.0, 13.0, 22.0), root_bone)
        for index in range(4):
            angle = -0.8 + index * 0.53
            add_horn(
                rig,
                mine,
                shell_center + Vector((math.cos(angle) * 19.0, sign * 4.0, math.sin(angle) * 15.0)),
                Vector((math.cos(angle), 0.4, math.sin(angle))),
                18.0 + index * 2.5,
                3.4,
                Vector((math.cos(angle) * 5.0, 4.0, math.sin(angle) * 5.0)),
                root_bone,
            )
    output_skn = combine_parts(helper, target_skn, [mine])
    relative = "assets/characters/jinxmine/skins/skin65/jinxmine_skin65.skn"
    output_path = os.path.join(args.out_root, relative.replace("/", os.sep))
    output_bytes = helper.write_skn(
        output_path,
        output_skn,
        output_skn["submeshes"],
        output_skn["indices"],
        output_skn["vertices"],
    )
    output_skl = os.path.join(
        args.out_root,
        "assets/characters/jinxmine/skins/skin65/jinxmine_skin65.skl".replace("/", os.sep),
    )
    os.makedirs(os.path.dirname(output_skl), exist_ok=True)
    shutil.copy2(args.target_mine_skl, output_skl)
    return {
        "path": output_path,
        "sha256": sha256_bytes(output_bytes),
        "skeleton_sha256": sha256_file(output_skl),
        "target_skeleton_sha256": sha256_file(args.target_mine_skl),
        "vertices": len(output_skn["vertices"]),
        "triangles": len(output_skn["indices"]) // 3,
        "sources": mine.sources,
        "target_ocean_song_vertices_retained": 0,
        "influence_fallbacks": rig.fallbacks,
    }


def build_missile(helper, read_skl, args):
    target_skn = helper.parse_skn(args.target_missile_skn)
    champion_joints, champion_influences = read_skl(args.target_skl)
    rig = RigTarget(helper, target_skn, champion_joints, champion_influences)
    minimum, maximum = mesh_bounds(helper, target_skn["vertices"])
    center = (minimum + maximum) * 0.5
    extent = maximum - minimum
    axis_index = max(range(3), key=lambda index: extent[index])
    axis = Vector((1.0 if axis_index == 0 else 0.0, 1.0 if axis_index == 1 else 0.0, 1.0 if axis_index == 2 else 0.0))
    side, up = orthogonal_frame(axis)
    half_length = max(52.0, extent[axis_index] * 0.55)
    missile = Part(MISSILE_SUBMESH)
    root_bone = champion_joints[champion_influences[0]].name
    points = [
        center - axis * half_length,
        center - axis * half_length * 0.25,
        center + axis * half_length * 0.35,
        center + axis * half_length,
    ]
    positions, faces, uvs = tube_geometry(points, (2.0, 8.0, 15.0, 2.0), sides=11, twist=0.23)
    append_mesh(
        rig,
        missile,
        positions,
        faces,
        uvs,
        {root_bone: 1.0},
        material="abyssal",
    )
    skull = center + axis * half_length * 0.42
    add_ellipsoid(
        rig,
        missile,
        skull,
        (18.0, 14.0, 16.0),
        root_bone,
        material="bone",
    )
    for sign in (-1.0, 1.0):
        add_horn(
            rig,
            missile,
            skull + side * sign * 10.0 + up * 5.0,
            axis * 0.52 + side * sign * 0.76 + up * 0.25,
            38.0,
            4.7,
            side * sign * 10.0 + up * 5.0,
            root_bone,
            material="coral",
        )
        add_horn(
            rig,
            missile,
            skull + side * sign * 8.0 - up * 6.0,
            axis * 0.65 + side * sign * 0.58 - up * 0.32,
            29.0,
            3.7,
            side * sign * 7.0 - up * 4.0,
            root_bone,
            material="bone",
        )
    for index in range(5):
        t = index / 4
        anchor = center - axis * half_length * (0.15 + 0.68 * t)
        add_horn(
            rig,
            missile,
            anchor + up * 5.0,
            -axis * 0.2 + up * 0.98,
            14.0 + 4.0 * t,
            2.8,
            -axis * 3.0 + up * 2.0,
            root_bone,
            material="seafoam",
        )
    output_skn = combine_parts(helper, target_skn, [missile])
    output_path = os.path.join(args.out_root, args.missile_relative.replace("/", os.sep))
    output_bytes = helper.write_skn(
        output_path,
        output_skn,
        output_skn["submeshes"],
        output_skn["indices"],
        output_skn["vertices"],
    )
    return {
        "path": output_path,
        "sha256": sha256_bytes(output_bytes),
        "vertices": len(output_skn["vertices"]),
        "triangles": len(output_skn["indices"]) // 3,
        "sources": missile.sources,
        "target_ocean_song_vertices_retained": 0,
        "source_bounds": {"min": rounded(minimum), "max": rounded(maximum)},
    }


def main():
    args = parse_args()
    sys.path.insert(0, os.path.abspath(args.addon_root))
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from Aventurine.io.import_skl import read_skl
    import build_model as helper

    champion = build_champion(helper, read_skl, args)
    mine = build_mine(helper, read_skl, args)
    missile = build_missile(helper, read_skl, args)
    report = {
        "status": "PASSED",
        "version": "3.0.0",
        "theme": "recognizable cute-horror dark sea witch with coral relic weapons",
        "champion": champion,
        "chompers": mine,
        "ultimate_missile": missile,
        "invariants": {
            "ocean_song_champion_geometry_retained": False,
            "ocean_song_chompers_geometry_retained": False,
            "ocean_song_missile_geometry_retained": False,
            "native_champion_skeleton_byte_identical": champion["skeleton_sha256"]
            == champion["target_skeleton_sha256"],
            "native_chompers_skeleton_byte_identical": mine["skeleton_sha256"]
            == mine["target_skeleton_sha256"],
            "joint_order_unchanged": True,
            "new_skeleton_joints_added": 0,
            "uint16_indices_valid": True,
        },
    }
    if not all(
        (
            report["invariants"]["native_champion_skeleton_byte_identical"],
            report["invariants"]["native_chompers_skeleton_byte_identical"],
        )
    ):
        raise ValueError("Native skeleton bytes changed")
    os.makedirs(os.path.dirname(os.path.abspath(args.report)), exist_ok=True)
    with open(args.report, "w", encoding="utf-8") as handle:
        json.dump(report, handle, indent=2)
        handle.write("\n")
    print(
        "SEA_WITCH_MODELS=PASSED "
        f"CHAMPION_VERTICES={champion['vertices']} "
        f"MINE_VERTICES={mine['vertices']} MISSILE_VERTICES={missile['vertices']} "
        "OCEAN_SONG_GEOMETRY=0"
    )


if __name__ == "__main__":
    try:
        main()
    except Exception:
        import traceback

        traceback.print_exc()
        sys.exit(1)
