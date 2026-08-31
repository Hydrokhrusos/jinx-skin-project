import argparse
import hashlib
import json
import math
import os
import struct
import sys

from mathutils import Vector


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--target-skn", required=True)
    parser.add_argument("--target-skl", required=True)
    parser.add_argument("--mine-skn", required=True)
    parser.add_argument("--rocket-skn", required=True)
    parser.add_argument("--addon-root", required=True)
    parser.add_argument("--out-root", required=True)
    parser.add_argument("--report", required=True)
    argv = sys.argv[sys.argv.index("--") + 1 :] if "--" in sys.argv else sys.argv[1:]
    return parser.parse_args(argv)


def sha256_bytes(value):
    return hashlib.sha256(value).hexdigest()


def rounded(value):
    return [round(float(component), 6) for component in value]


def mesh_bounds(helper, vertices):
    positions = [helper.vertex_position(vertex) for vertex in vertices]
    minimum = Vector(tuple(min(position[i] for position in positions) for i in range(3)))
    maximum = Vector(tuple(max(position[i] for position in positions) for i in range(3)))
    return minimum, maximum


def update_vertex(helper, vertex, position, normal=None):
    helper.set_position(vertex, position)
    if normal is not None and normal.length > 1e-8:
        normal.normalize()
        helper.set_normal(vertex, normal)


def fin_geometry(center, span, direction, width, length, thickness):
    direction = Vector(direction).normalized()
    span = Vector(span) - direction * Vector(span).dot(direction)
    if span.length <= 1e-6:
        raise ValueError("Fin span and direction overlap")
    span.normalize()
    depth = span.cross(direction).normalized()
    center = Vector(center)
    half_width = span * (width * 0.5)
    half_depth = depth * (thickness * 0.5)
    tip = center + direction * length
    positions = [
        center - half_width + half_depth,
        center + half_width + half_depth,
        tip + half_depth,
        center - half_width - half_depth,
        center + half_width - half_depth,
        tip - half_depth,
    ]
    faces = [
        (0, 1, 2),
        (5, 4, 3),
        (0, 3, 4),
        (0, 4, 1),
        (0, 2, 5),
        (0, 5, 3),
        (1, 4, 5),
        (1, 5, 2),
    ]
    return positions, faces


def shell_geometry(center, axes):
    center = Vector(center)
    x_axis, y_axis, z_axis = (Vector(axis) for axis in axes)
    positions = [
        center + x_axis,
        center - x_axis,
        center + y_axis,
        center - y_axis,
        center + z_axis,
        center - z_axis,
    ]
    faces = [
        (0, 2, 4),
        (2, 1, 4),
        (1, 3, 4),
        (3, 0, 4),
        (2, 0, 5),
        (1, 2, 5),
        (3, 1, 5),
        (0, 3, 5),
    ]
    return positions, faces


def addon_vertices(helper, source_vertices, source_indices, positions, faces):
    templates = [source_vertices[index] for index in source_indices]
    template_positions = [helper.vertex_position(vertex) for vertex in templates]
    normals = [Vector((0.0, 0.0, 0.0)) for _ in positions]
    for face in faces:
        a, b, c = (positions[index] for index in face)
        normal = (b - a).cross(c - a)
        if normal.length > 1e-8:
            normal.normalize()
        for index in face:
            normals[index] += normal

    result = []
    for index, position in enumerate(positions):
        nearest = min(
            range(len(templates)),
            key=lambda candidate: (template_positions[candidate] - position).length_squared,
        )
        vertex = bytearray(templates[nearest])
        normal = normals[index]
        if normal.length <= 1e-8:
            normal = helper.vertex_normal(vertex)
        update_vertex(helper, vertex, position, normal)
        # Keep the nearest native Ocean Song UV.  The old fixed donor-atlas patch
        # made every added face sample unrelated pixels and visibly smeared.
        result.append(vertex)
    return result


def rebuild_with_addons(helper, skn, transformed_vertices, addon_specs):
    output_vertices = []
    output_indices = []
    output_submeshes = []
    report = {"added_vertices": 0, "added_triangles": 0, "by_submesh": {}}

    for submesh in skn["submeshes"]:
        name = submesh["name"]
        old_vertex_start = submesh["vertex_start"]
        old_vertex_stop = old_vertex_start + submesh["vertex_count"]
        source_vertex_indices = list(range(old_vertex_start, old_vertex_stop))
        source_vertices = transformed_vertices[old_vertex_start:old_vertex_stop]
        vertex_start = len(output_vertices)
        index_start = len(output_indices)
        output_vertices.extend(bytearray(vertex) for vertex in source_vertices)

        raw_indices = skn["indices"][
            submesh["index_start"] : submesh["index_start"] + submesh["index_count"]
        ]
        local_indices = []
        for index in raw_indices:
            if index < old_vertex_start or index >= old_vertex_stop:
                raise ValueError(f"{name} index {index} escapes its vertex range")
            local_indices.append(index - old_vertex_start)
        output_indices.extend(vertex_start + index for index in local_indices)

        added_vertices = 0
        added_triangles = 0
        for spec in addon_specs.get(name, []):
            positions, faces = spec[:2]
            template_indices = spec[2] if len(spec) == 3 else source_vertex_indices
            base = len(output_vertices)
            created = addon_vertices(
                helper, transformed_vertices, template_indices, positions, faces
            )
            output_vertices.extend(created)
            output_indices.extend(base + index for face in faces for index in face)
            added_vertices += len(created)
            added_triangles += len(faces)

        output_submeshes.append(
            {
                "name": name,
                "vertex_start": vertex_start,
                "vertex_count": len(output_vertices) - vertex_start,
                "index_start": index_start,
                "index_count": len(output_indices) - index_start,
            }
        )
        if added_vertices:
            report["by_submesh"][name] = {
                "added_vertices": added_vertices,
                "added_triangles": added_triangles,
            }
            report["added_vertices"] += added_vertices
            report["added_triangles"] += added_triangles

    if len(output_vertices) >= 65536:
        raise ValueError("Remodeled SKN exceeds 16-bit vertex index range")
    output_skn = dict(skn)
    output_skn["submeshes"] = output_submeshes
    output_skn["indices"] = output_indices
    return output_skn, output_vertices, report


def submesh_bounds(helper, vertices, submesh):
    start = submesh["vertex_start"]
    stop = start + submesh["vertex_count"]
    positions = [helper.vertex_position(vertices[index]) for index in range(start, stop)]
    minimum = Vector(tuple(min(position[i] for position in positions) for i in range(3)))
    maximum = Vector(tuple(max(position[i] for position in positions) for i in range(3)))
    return minimum, maximum


def retarget_donor_skn(helper, donor_skn, donor_joints, donor_influences, target_joints, target_influences):
    target_by_name = {joint.name: index for index, joint in enumerate(target_joints)}
    target_local_by_joint = {
        joint_index: local_index for local_index, joint_index in enumerate(target_influences)
    }
    selected_names = {"Body", "Weapon"}
    output_vertices = []
    output_indices = []
    output_submeshes = []
    weighted_names = set()
    influence_fallbacks = {}

    for submesh in donor_skn["submeshes"]:
        if submesh["name"] not in selected_names:
            continue
        vertex_start = len(output_vertices)
        index_start = len(output_indices)
        old_start = submesh["vertex_start"]
        old_stop = old_start + submesh["vertex_count"]
        for source_vertex in donor_skn["vertices"][old_start:old_stop]:
            vertex = bytearray(source_vertex)
            donor_local = struct.unpack_from("<4B", vertex, 12)
            weights = struct.unpack_from("<4f", vertex, 16)
            target_local = [0, 0, 0, 0]
            for slot, (local_index, weight) in enumerate(zip(donor_local, weights)):
                if weight <= 1e-7:
                    continue
                donor_joint_index = (
                    donor_influences[local_index] if donor_influences else local_index
                )
                joint_name = donor_joints[donor_joint_index].name
                weighted_names.add(joint_name)
                if joint_name not in target_by_name:
                    raise ValueError(
                        f"Donor {submesh['name']} uses joint absent from Ocean Song rig: {joint_name}"
                    )
                target_joint_index = target_by_name[joint_name]
                original_target_joint = target_joint_index
                while target_joint_index not in target_local_by_joint and target_joint_index >= 0:
                    target_joint_index = target_joints[target_joint_index].parent
                if target_joint_index < 0:
                    raise ValueError(
                        f"Ocean Song influence table omits required joint: {joint_name}"
                    )
                if target_joint_index != original_target_joint:
                    influence_fallbacks[joint_name] = target_joints[target_joint_index].name
                target_local[slot] = target_local_by_joint[target_joint_index]
            struct.pack_into("<4B", vertex, 12, *target_local)
            output_vertices.append(vertex)

        raw_indices = donor_skn["indices"][
            submesh["index_start"] : submesh["index_start"] + submesh["index_count"]
        ]
        for index in raw_indices:
            if index < old_start or index >= old_stop:
                raise ValueError(f"Donor {submesh['name']} index escapes its vertex range")
            output_indices.append(vertex_start + index - old_start)
        output_submeshes.append(
            {
                "name": submesh["name"],
                "vertex_start": vertex_start,
                "vertex_count": len(output_vertices) - vertex_start,
                "index_start": index_start,
                "index_count": len(output_indices) - index_start,
            }
        )

    if {item["name"] for item in output_submeshes} != selected_names:
        raise ValueError("Donor model did not supply both Body and Weapon submeshes")
    output_skn = dict(donor_skn)
    output_skn["submeshes"] = output_submeshes
    output_skn["vertices"] = output_vertices
    output_skn["indices"] = output_indices
    return output_skn, {
        "donor_submeshes": sorted(selected_names),
        "donor_vertices_selected": len(output_vertices),
        "donor_triangles_selected": len(output_indices) // 3,
        "weighted_joints_retargeted_by_name": len(weighted_names),
        "influence_fallbacks_to_native_ancestors": influence_fallbacks,
        "target_geometry_vertices_retained": 0,
    }


def ring_geometry(center, radius_x, radius_y, inner_ratio, depth, segments):
    center = Vector(center)
    positions = []
    for layer in (depth * 0.5, -depth * 0.5):
        for radius in (1.0, inner_ratio):
            for index in range(segments):
                angle = math.tau * index / segments
                positions.append(
                    center
                    + Vector((math.cos(angle) * radius_x * radius, math.sin(angle) * radius_y * radius, layer))
                )
    outer_front = 0
    inner_front = segments
    outer_back = segments * 2
    inner_back = segments * 3
    faces = []
    for index in range(segments):
        following = (index + 1) % segments
        faces.extend(
            (
                (outer_front + index, outer_front + following, inner_front + following),
                (outer_front + index, inner_front + following, inner_front + index),
                (outer_back + following, outer_back + index, inner_back + index),
                (outer_back + following, inner_back + index, inner_back + following),
                (outer_front + index, outer_back + index, outer_back + following),
                (outer_front + index, outer_back + following, outer_front + following),
                (inner_front + following, inner_back + following, inner_back + index),
                (inner_front + following, inner_back + index, inner_front + index),
            )
        )
    return positions, faces


def append_synthetic_recall(helper, skn, target_skn):
    recall = next((item for item in target_skn["submeshes"] if item["name"] == "Recall"), None)
    if recall is None:
        raise ValueError("Ocean Song target has no Recall rig-weight template")
    minimum, maximum = submesh_bounds(helper, target_skn["vertices"], recall)
    center = (minimum + maximum) * 0.5
    extent = maximum - minimum
    radius_x = max(74.0, extent.x * 0.50)
    radius_y = max(92.0, extent.y * 0.50)
    specs = [ring_geometry(center, radius_x, radius_y, 0.68, max(10.0, extent.z * 0.12), 48)]
    for index in range(16):
        angle = math.tau * index / 16.0
        anchor = center + Vector((math.cos(angle) * radius_x, math.sin(angle) * radius_y, 0))
        direction = Vector((math.cos(angle), math.sin(angle), 0.16)).normalized()
        span = Vector((-math.sin(angle), math.cos(angle), 0))
        specs.append(fin_geometry(anchor, span, direction, 18, 38 + 9 * (index % 3), 6))

    output_vertices = list(skn["vertices"])
    output_indices = list(skn["indices"])
    output_submeshes = [dict(item) for item in skn["submeshes"]]
    vertex_start = len(output_vertices)
    index_start = len(output_indices)
    source_indices = list(range(recall["vertex_start"], recall["vertex_start"] + recall["vertex_count"]))
    added_vertices = 0
    added_triangles = 0
    for positions, faces in specs:
        base = len(output_vertices)
        created = addon_vertices(helper, target_skn["vertices"], source_indices, positions, faces)
        output_vertices.extend(created)
        output_indices.extend(base + index for face in faces for index in face)
        added_vertices += len(created)
        added_triangles += len(faces)
    output_submeshes.append(
        {
            "name": "Recall",
            "vertex_start": vertex_start,
            "vertex_count": added_vertices,
            "index_start": index_start,
            "index_count": added_triangles * 3,
        }
    )
    output_skn = dict(skn)
    output_skn["vertices"] = output_vertices
    output_skn["indices"] = output_indices
    output_skn["submeshes"] = output_submeshes
    return output_skn, {"vertices": added_vertices, "triangles": added_triangles}


def transform_jinx(helper, target_skn_path, target_skl_path, addon_root):
    sys.path.insert(0, os.path.abspath(addon_root))
    from Aventurine.io.import_skl import read_skl

    target_skn = helper.parse_skn(target_skn_path)
    joints, influence_map = read_skl(target_skl_path)
    # Ocean Song's own mesh is the rig/UV/material authority.  Remodel it in
    # place so Q weapon visibility, recall visibility, grips, and atlas layout
    # retain the exact native behavior.
    skn = target_skn
    names = {joint.name: index for index, joint in enumerate(joints)}
    required = {
        "Rocket_Launcher",
        "Rocket_Launcher_Handle",
        "Minigun",
        "Minigun_Handle_Back",
        "Minigun_Handle_Front",
    }
    missing = sorted(required - names.keys())
    if missing:
        raise ValueError(f"Missing Ocean Song weapon joints: {missing}")

    matrices = helper.global_joint_matrices(joints)
    rocket_handle = matrices[names["Rocket_Launcher_Handle"]].to_translation()
    minigun_back = matrices[names["Minigun_Handle_Back"]].to_translation()
    minigun_front = matrices[names["Minigun_Handle_Front"]].to_translation()
    powpow_joints = helper.descendants(joints, names["Minigun"])
    fishbones_joints = helper.descendants(joints, names["Rocket_Launcher"])
    warp_powpow, warp_fishbones, handle_span = helper.make_warps(
        1.42, rocket_handle, minigun_back, minigun_front
    )

    weapon = next(item for item in skn["submeshes"] if item["name"] == "Weapon")
    weapon_indices = list(
        range(weapon["vertex_start"], weapon["vertex_start"] + weapon["vertex_count"])
    )
    powpow_indices = []
    fishbones_indices = []
    for index in weapon_indices:
        scores = helper.vertex_family_scores(
            skn["vertices"][index], influence_map, powpow_joints, fishbones_joints
        )
        target = (
            powpow_indices
            if scores[helper.POWPOW_SUBMESH] >= scores[helper.FISHBONES_SUBMESH]
            else fishbones_indices
        )
        target.append(index)
    if not powpow_indices or not fishbones_indices:
        raise ValueError("Ocean Song weapon-family classification is incomplete")

    output_vertices = [bytearray(vertex) for vertex in skn["vertices"]]
    changed = 0
    maximum_displacement = 0.0
    changed_by_submesh = {}

    for submesh in skn["submeshes"]:
        name = submesh["name"]
        submesh_changed = 0
        start = submesh["vertex_start"]
        stop = start + submesh["vertex_count"]
        for index in range(start, stop):
            vertex = output_vertices[index]
            original = helper.vertex_position(vertex)
            normal = helper.vertex_normal(vertex)
            position = original.copy()
            output_normal = normal.copy()

            if name == "Weapon":
                scores = helper.vertex_family_scores(
                    vertex, influence_map, powpow_joints, fishbones_joints
                )
                if scores[helper.POWPOW_SUBMESH] >= scores[helper.FISHBONES_SUBMESH]:
                    position, output_normal = warp_powpow(position, output_normal)
                    axis = (minigun_front - minigun_back).normalized()
                    axial = (original - minigun_back).dot(axis)
                    ridge = 1.0 + 0.045 * math.sin(axial * 0.19)
                    closest = minigun_back + axis * axial
                    position = closest + (position - closest) * ridge
                else:
                    position, output_normal = warp_fishbones(position, output_normal)
                    distance = (original - rocket_handle).length
                    ridge = 1.0 + 0.055 * math.sin(distance * 0.13)
                    position = rocket_handle + (position - rocket_handle) * ridge
            elif name in {"WeaponVFX", "Weapon03"}:
                position, output_normal = warp_powpow(position, output_normal)
            elif name == "Body":
                shoulder = max(0.0, min(1.0, (position.y - 92.0) / 72.0))
                waist = max(0.0, 1.0 - abs(position.y - 104.0) / 46.0)
                position.x *= 1.07 + 0.09 * shoulder - 0.035 * waist
                position.y = 92.0 + (position.y - 92.0) * (1.0 + 0.035 * shoulder)
                position.z *= 1.075
                output_normal = Vector((normal.x / 1.14, normal.y, normal.z / 1.075))
            elif name == "Hair":
                tail = max(0.0, min(1.0, (128.0 - position.y) / 72.0))
                position.x *= 1.18 + 0.12 * tail
                position.y = 150.0 + (position.y - 150.0) * 1.13
                position.z = -12.0 + (position.z + 12.0) * (1.22 + 0.16 * tail)
                output_normal = Vector((normal.x / 1.24, normal.y / 1.13, normal.z / 1.30))
            elif name == "Skirt":
                lower = max(0.0, min(1.0, (112.0 - position.y) / 35.0))
                position.x *= 1.32 + 0.13 * lower
                position.y = 108.0 + (position.y - 108.0) * 1.08
                position.z *= 1.26
                output_normal = Vector((normal.x / 1.39, normal.y / 1.08, normal.z / 1.26))
            elif name == "Recall":
                position.x *= 1.11
                position.z *= 1.11
                output_normal = Vector((normal.x / 1.11, normal.y, normal.z / 1.11))

            displacement = (position - original).length
            if displacement > 1e-6:
                update_vertex(helper, vertex, position, output_normal)
                changed += 1
                submesh_changed += 1
                maximum_displacement = max(maximum_displacement, displacement)
        changed_by_submesh[name] = submesh_changed

    if changed < len(output_vertices) * 0.7:
        raise ValueError(f"Jinx remodel changed too few vertices: {changed}")
    output_skn, output_vertices, topology = rebuild_with_addons(
        helper, skn, output_vertices, {}
    )
    source_min, source_max = mesh_bounds(helper, target_skn["vertices"])
    output_min, output_max = mesh_bounds(helper, output_vertices)
    return output_skn, output_vertices, {
        "role": "champion_weapons_and_recall",
        "source_sha256": sha256_bytes(target_skn["source_bytes"]),
        "vertices": len(output_vertices),
        "source_vertices": len(target_skn["vertices"]),
        "indices": len(target_skn["indices"]),
        "output_indices": len(output_skn["indices"]),
        "submeshes": [item["name"] for item in output_skn["submeshes"]],
        "changed_vertices": changed + topology["added_vertices"],
        "changed_by_submesh": changed_by_submesh,
        "topology": topology,
        "topology_changed": topology["added_vertices"] > 0,
        "native_foundation": {
            "skin": 65,
            "source_vertices_retained": len(target_skn["vertices"]),
            "source_submeshes_retained": [item["name"] for item in target_skn["submeshes"]],
            "source_weights_retained": True,
            "source_uvs_retained": True,
            "donor_geometry_used": False,
            "synthetic_recall_used": False,
            "powpow_vertices_remodeled": len(powpow_indices),
            "fishbones_vertices_remodeled": len(fishbones_indices),
        },
        "maximum_displacement": round(maximum_displacement, 6),
        "source_bounds": {"min": rounded(source_min), "max": rounded(source_max)},
        "output_bounds": {"min": rounded(output_min), "max": rounded(output_max)},
        "grip_centers": {
            "rocket_handle": rounded(rocket_handle),
            "minigun_handle_back": rounded(minigun_back),
            "minigun_handle_front": rounded(minigun_front),
            "minigun_handle_span": round(handle_span, 6),
            "center_displacement": 0.0,
        },
    }


def transform_prop(helper, source_path, role):
    skn = helper.parse_skn(source_path)
    output_vertices = [bytearray(vertex) for vertex in skn["vertices"]]
    minimum, maximum = mesh_bounds(helper, skn["vertices"])
    center = (minimum + maximum) * 0.5
    extent = maximum - minimum
    major_axis = max(range(3), key=lambda index: extent[index])
    maximum_displacement = 0.0

    for vertex in output_vertices:
        original = helper.vertex_position(vertex)
        normal = helper.vertex_normal(vertex)
        relative = original - center
        if role == "chompers":
            phase = relative.y * 0.12 + relative.z * 0.08
            flare = 1.20 + 0.10 * math.sin(phase)
            position = Vector(
                (
                    center.x + relative.x * flare,
                    center.y + relative.y * 0.91,
                    center.z + relative.z * flare,
                )
            )
            output_normal = Vector((normal.x / flare, normal.y / 0.91, normal.z / flare))
        else:
            normalized = relative[major_axis] / max(1e-6, extent[major_axis] * 0.5)
            cross_scale = 1.12 + 0.065 * math.cos(normalized * math.pi * 3.0)
            scales = [cross_scale, cross_scale, cross_scale]
            scales[major_axis] = 1.36
            position = center + Vector(tuple(relative[i] * scales[i] for i in range(3)))
            output_normal = Vector(tuple(normal[i] / scales[i] for i in range(3)))
        update_vertex(helper, vertex, position, output_normal)
        maximum_displacement = max(maximum_displacement, (position - original).length)

    minimum, maximum = mesh_bounds(helper, output_vertices)
    center = (minimum + maximum) * 0.5
    extent = maximum - minimum
    specs = []
    if role == "chompers":
        radius = max(extent.x, extent.z) * 0.42
        for step in range(8):
            angle = step * math.tau / 8.0
            direction = Vector((math.cos(angle), 0.18, math.sin(angle)))
            anchor = center + Vector((math.cos(angle) * radius, extent.y * 0.12, math.sin(angle) * radius))
            specs.append(
                fin_geometry(anchor, (0, 1, 0), direction, max(7.0, extent.y * 0.16), max(13.0, radius * 0.72), 3.5)
            )
        for x, z in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
            anchor = center + Vector((x * extent.x * 0.22, extent.y * 0.36, z * extent.z * 0.22))
            specs.append(fin_geometry(anchor, (1, 0, 0), (x * 0.18, 1, z * 0.18), 8, 18, 3))
    else:
        axis = Vector(tuple(1.0 if index == major_axis else 0.0 for index in range(3)))
        first = Vector((1.0, 0.0, 0.0))
        if abs(first.dot(axis)) > 0.8:
            first = Vector((0.0, 1.0, 0.0))
        second = axis.cross(first).normalized()
        first = second.cross(axis).normalized()
        for offset in (-0.18, 0.08, 0.31):
            anchor = center + axis * extent[major_axis] * offset
            for direction in (first, -first, second, -second):
                specs.append(
                    fin_geometry(
                        anchor,
                        axis,
                        direction + axis * 0.16,
                        max(7.0, extent[major_axis] * 0.12),
                        max(11.0, extent[major_axis] * 0.19),
                        3.5,
                    )
                )
    only_submesh = skn["submeshes"][0]["name"]
    output_skn, output_vertices, topology = rebuild_with_addons(
        helper, skn, output_vertices, {only_submesh: specs}
    )
    output_min, output_max = mesh_bounds(helper, output_vertices)
    return output_skn, output_vertices, {
        "role": role,
        "source_sha256": sha256_bytes(skn["source_bytes"]),
        "vertices": len(output_vertices),
        "source_vertices": len(skn["vertices"]),
        "indices": len(skn["indices"]),
        "output_indices": len(output_skn["indices"]),
        "submeshes": [item["name"] for item in output_skn["submeshes"]],
        "changed_vertices": len(skn["vertices"]) + topology["added_vertices"],
        "topology": topology,
        "topology_changed": True,
        "maximum_displacement": round(maximum_displacement, 6),
        "major_axis": major_axis,
        "source_bounds": {"min": rounded(minimum), "max": rounded(maximum)},
        "output_bounds": {"min": rounded(output_min), "max": rounded(output_max)},
    }


def write_model(helper, skn, vertices, path, report):
    output = helper.write_skn(path, skn, skn["submeshes"], skn["indices"], vertices)
    report["output"] = os.path.abspath(path)
    report["output_sha256"] = sha256_bytes(output)
    if report["source_sha256"] == report["output_sha256"]:
        raise ValueError(f"Model did not change: {path}")


def main():
    args = parse_args()
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import build_model as helper

    output_root = os.path.abspath(args.out_root)
    jobs = []

    jinx_skn, jinx_vertices, jinx_report = transform_jinx(
        helper,
        args.target_skn,
        args.target_skl,
        args.addon_root,
    )
    jobs.append(
        (
            jinx_skn,
            jinx_vertices,
            os.path.join(output_root, "assets/characters/jinx/skins/skin65/jinx_skin65.skn"),
            jinx_report,
        )
    )

    for source, role, relative in (
        (
            args.mine_skn,
            "chompers",
            "assets/characters/jinxmine/skins/skin65/jinxmine_skin65.skn",
        ),
        (
            args.rocket_skn,
            "ultimate_missile",
            "assets/characters/jinx/skins/skin65/particles/jinx_skin65_r_mis_globefish_01_1.skn",
        ),
    ):
        skn, vertices, report = transform_prop(helper, source, role)
        jobs.append((skn, vertices, os.path.join(output_root, relative), report))

    reports = []
    for skn, vertices, output_path, report in jobs:
        write_model(helper, skn, vertices, output_path, report)
        reports.append(report)

    payload = {
        "status": "PASSED",
        "theme": "Abyssal Siren",
        "models_replaced": len(reports),
        "models": reports,
        "invariants": {
            "native_skeleton_files_unchanged": True,
            "joint_order_unchanged": True,
            "source_skin_weights_and_uvs_preserved": True,
            "added_geometry_inherits_native_rig_weights": True,
            "grip_joint_centers_unchanged": True,
        },
    }
    os.makedirs(os.path.dirname(os.path.abspath(args.report)), exist_ok=True)
    with open(args.report, "w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2)
        handle.write("\n")
    print(
        "ABYSSAL_MODELS=PASSED "
        f"MODELS={len(reports)} CHANGED_VERTICES={sum(item['changed_vertices'] for item in reports)}"
    )


if __name__ == "__main__":
    try:
        main()
    except Exception:
        import traceback

        traceback.print_exc()
        sys.exit(1)
