import argparse
import hashlib
import json
import math
import os
import struct
import sys

from mathutils import Matrix, Vector


WEAPON_SUBMESH = "Weapon"
POWPOW_SUBMESH = "PowPow"
FISHBONES_SUBMESH = "Fishbones"
POWPOW_AUX_SUBMESHES = {"WeaponVFX", "Weapon03"}
POWPOW_CHAIN_SUBMESH = "Weapon03"


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--skn", required=True)
    parser.add_argument("--skl", required=True)
    parser.add_argument("--addon-root", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--report", required=True)
    parser.add_argument("--scale", type=float, default=1.5)
    argv = sys.argv[sys.argv.index("--") + 1 :] if "--" in sys.argv else sys.argv[1:]
    return parser.parse_args(argv)


def sha256_bytes(value):
    return hashlib.sha256(value).hexdigest()


def rounded(values):
    return [round(float(value), 6) for value in values]


def parse_skn(path):
    data = open(path, "rb").read()
    offset = 0

    def take(fmt):
        nonlocal offset
        size = struct.calcsize(fmt)
        values = struct.unpack_from(fmt, data, offset)
        offset += size
        return values[0] if len(values) == 1 else values

    magic = take("<I")
    if magic != 0x00112233:
        raise ValueError("Unexpected SKN signature")
    major, minor = take("<HH")
    if major < 4:
        raise ValueError(f"Expected SKN v4+, got {major}.{minor}")

    submeshes = []
    for _ in range(take("<I")):
        raw_name = data[offset : offset + 64]
        offset += 64
        name = raw_name.split(b"\0", 1)[0].decode("ascii")
        vertex_start, vertex_count, index_start, index_count = take("<IIII")
        submeshes.append(
            {
                "name": name,
                "vertex_start": vertex_start,
                "vertex_count": vertex_count,
                "index_start": index_start,
                "index_count": index_count,
            }
        )

    flags = data[offset : offset + 4]
    offset += 4
    index_count, vertex_count, vertex_size, vertex_type = take("<IIII")
    original_bounds = data[offset : offset + 40]
    offset += 40
    indices = list(take(f"<{index_count}H"))
    vertices = [
        bytearray(data[offset + i * vertex_size : offset + (i + 1) * vertex_size])
        for i in range(vertex_count)
    ]
    offset += vertex_count * vertex_size
    trailing_data = data[offset:]
    if vertex_size < 52:
        raise ValueError(f"Unsupported vertex size: {vertex_size}")

    return {
        "magic": magic,
        "major": major,
        "minor": minor,
        "flags": flags,
        "vertex_size": vertex_size,
        "vertex_type": vertex_type,
        "original_bounds": original_bounds,
        "submeshes": submeshes,
        "indices": indices,
        "vertices": vertices,
        "trailing_data": trailing_data,
        "source_bytes": data,
    }


def global_joint_matrices(joints):
    matrices = [None] * len(joints)

    def calculate(index):
        if matrices[index] is not None:
            return matrices[index]
        joint = joints[index]
        local = (
            Matrix.Translation(Vector(joint.raw_trans))
            @ joint.raw_rot.to_matrix().to_4x4()
            @ Matrix.Diagonal((*Vector(joint.raw_scale), 1.0))
        )
        matrices[index] = calculate(joint.parent) @ local if joint.parent >= 0 else local
        return matrices[index]

    for joint_index in range(len(joints)):
        calculate(joint_index)
    return matrices


def descendants(joints, root_index):
    result = {root_index}
    changed = True
    while changed:
        changed = False
        for index, joint in enumerate(joints):
            if joint.parent in result and index not in result:
                result.add(index)
                changed = True
    return result


def vertex_position(vertex):
    return Vector(struct.unpack_from("<3f", vertex, 0))


def vertex_normal(vertex):
    return Vector(struct.unpack_from("<3f", vertex, 32))


def set_position(vertex, value):
    struct.pack_into("<3f", vertex, 0, *value)


def set_normal(vertex, value):
    struct.pack_into("<3f", vertex, 32, *value)


def vertex_family_scores(vertex, influence_map, powpow_joints, fishbones_joints):
    local_influences = struct.unpack_from("<4B", vertex, 12)
    weights = struct.unpack_from("<4f", vertex, 16)
    scores = {POWPOW_SUBMESH: 0.0, FISHBONES_SUBMESH: 0.0}
    for local_index, weight in zip(local_influences, weights):
        if weight <= 0:
            continue
        joint_index = influence_map[local_index] if influence_map else local_index
        if joint_index in powpow_joints:
            scores[POWPOW_SUBMESH] += float(weight)
        if joint_index in fishbones_joints:
            scores[FISHBONES_SUBMESH] += float(weight)
    return scores


def split_weapon(skn, submesh, influence_map, powpow_joints, fishbones_joints):
    family_triangles = {POWPOW_SUBMESH: [], FISHBONES_SUBMESH: []}
    ambiguous = []
    mixed_weight_triangles = 0
    start = submesh["index_start"]
    stop = start + submesh["index_count"]
    source_indices = skn["indices"][start:stop]
    for triangle_offset in range(0, len(source_indices), 3):
        triangle = source_indices[triangle_offset : triangle_offset + 3]
        total = {POWPOW_SUBMESH: 0.0, FISHBONES_SUBMESH: 0.0}
        for vertex_index in triangle:
            scores = vertex_family_scores(
                skn["vertices"][vertex_index],
                influence_map,
                powpow_joints,
                fishbones_joints,
            )
            for family in total:
                total[family] += scores[family]
        if total[POWPOW_SUBMESH] > 0 and total[FISHBONES_SUBMESH] > 0:
            mixed_weight_triangles += 1
        difference = total[POWPOW_SUBMESH] - total[FISHBONES_SUBMESH]
        if abs(difference) <= 1e-6:
            ambiguous.append(
                {
                    "triangle": triangle_offset // 3,
                    "indices": triangle,
                    "scores": total,
                }
            )
            continue
        family = POWPOW_SUBMESH if difference > 0 else FISHBONES_SUBMESH
        family_triangles[family].append(triangle)

    if ambiguous:
        raise ValueError(f"Could not classify {len(ambiguous)} weapon triangles")
    if not all(family_triangles.values()):
        raise ValueError("Weapon split did not produce both PowPow and Fishbones")
    return family_triangles, mixed_weight_triangles


def make_warps(scale, rocket_handle, minigun_back, minigun_front):
    axis_vector = minigun_front - minigun_back
    axis_length = axis_vector.length
    if axis_length <= 1e-6:
        raise ValueError("Minigun handle anchors overlap")
    axis = axis_vector.normalized()

    def fishbones(position, normal):
        return rocket_handle + scale * (position - rocket_handle), normal

    def powpow(position, normal):
        relative = position - minigun_back
        axial_distance = relative.dot(axis)
        radial = relative - axis * axial_distance
        if axial_distance < 0:
            new_position = minigun_back + scale * relative
            new_normal = normal
        elif axial_distance > axis_length:
            new_position = minigun_front + scale * (position - minigun_front)
            new_normal = normal
        else:
            new_position = minigun_back + axis * axial_distance + radial * scale
            axial_normal = axis * normal.dot(axis)
            radial_normal = normal - axial_normal
            new_normal = axial_normal + radial_normal / scale
            if new_normal.length > 1e-8:
                new_normal.normalize()
        return new_position, new_normal

    return powpow, fishbones, axis_length


def bounds(vertices):
    positions = [vertex_position(vertex) for vertex in vertices]
    minimum = Vector(tuple(min(position[i] for position in positions) for i in range(3)))
    maximum = Vector(tuple(max(position[i] for position in positions) for i in range(3)))
    center = (minimum + maximum) * 0.5
    radius = max((position - center).length for position in positions)
    return minimum, maximum, center, radius


def family_bounds(vertices, indices):
    positions = [vertex_position(vertices[index]) for index in sorted(set(indices))]
    minimum = Vector(tuple(min(position[i] for position in positions) for i in range(3)))
    maximum = Vector(tuple(max(position[i] for position in positions) for i in range(3)))
    return {
        "min": rounded(minimum),
        "max": rounded(maximum),
        "extent": rounded(maximum - minimum),
    }


def encode_name(name):
    encoded = name.encode("ascii")
    if len(encoded) > 63:
        raise ValueError(f"Submesh name too long: {name}")
    return encoded + b"\0" * (64 - len(encoded))


def write_skn(path, skn, submeshes, indices, vertices):
    minimum, maximum, center, radius = bounds(vertices)
    chunks = [
        struct.pack("<IHHI", skn["magic"], skn["major"], skn["minor"], len(submeshes))
    ]
    for submesh in submeshes:
        chunks.append(encode_name(submesh["name"]))
        chunks.append(
            struct.pack(
                "<IIII",
                submesh["vertex_start"],
                submesh["vertex_count"],
                submesh["index_start"],
                submesh["index_count"],
            )
        )
    chunks.extend(
        [
            skn["flags"],
            struct.pack(
                "<IIII",
                len(indices),
                len(vertices),
                skn["vertex_size"],
                skn["vertex_type"],
            ),
            struct.pack("<3f3f3ff", *minimum, *maximum, *center, radius),
            struct.pack(f"<{len(indices)}H", *indices),
            b"".join(bytes(vertex) for vertex in vertices),
            skn["trailing_data"],
        ]
    )
    output = b"".join(chunks)
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with open(path, "wb") as handle:
        handle.write(output)
    return output


def main():
    args = parse_args()
    if not 1.0 < args.scale <= 2.0:
        raise ValueError("Scale must be greater than 1.0 and no more than 2.0")

    sys.path.insert(0, os.path.abspath(args.addon_root))
    from Aventurine.io.import_skl import read_skl

    skn = parse_skn(args.skn)
    joints, influence_map = read_skl(args.skl)
    joint_names = {joint.name: index for index, joint in enumerate(joints)}
    required = {
        "Rocket_Launcher",
        "Rocket_Launcher_Handle",
        "Minigun",
        "Minigun_Handle_Back",
        "Minigun_Handle_Front",
    }
    missing = sorted(required - joint_names.keys())
    if missing:
        raise ValueError(f"Missing required joints: {missing}")

    matrices = global_joint_matrices(joints)
    rocket_handle = matrices[joint_names["Rocket_Launcher_Handle"]].to_translation()
    minigun_back = matrices[joint_names["Minigun_Handle_Back"]].to_translation()
    minigun_front = matrices[joint_names["Minigun_Handle_Front"]].to_translation()
    powpow_joints = descendants(joints, joint_names["Minigun"])
    fishbones_joints = descendants(joints, joint_names["Rocket_Launcher"])
    overlap = powpow_joints & fishbones_joints
    if overlap:
        raise ValueError(f"Weapon skeleton families overlap: {sorted(overlap)}")

    auxiliary_components = {}
    for name in sorted(POWPOW_AUX_SUBMESHES):
        submesh = next((item for item in skn["submeshes"] if item["name"] == name), None)
        if submesh is None:
            raise ValueError(f"Missing Pow-Pow auxiliary submesh: {name}")
        indices = range(submesh["vertex_start"], submesh["vertex_start"] + submesh["vertex_count"])
        scores = [
            vertex_family_scores(skn["vertices"][index], influence_map, powpow_joints, fishbones_joints)
            for index in indices
        ]
        powpow_vertices = sum(score[POWPOW_SUBMESH] > 0 for score in scores)
        fishbones_vertices = sum(score[FISHBONES_SUBMESH] > 0 for score in scores)
        if powpow_vertices != submesh["vertex_count"] or fishbones_vertices != 0:
            raise ValueError(f"Pow-Pow auxiliary submesh has wrong weapon weights: {name}")
        auxiliary_components[name] = {
            "role": "chain" if name == POWPOW_CHAIN_SUBMESH else "vfx",
            "vertex_count": submesh["vertex_count"],
            "vertices_weighted_to_minigun": powpow_vertices,
            "vertices_weighted_to_rocket_launcher": fishbones_vertices,
        }

    weapon = next(
        (submesh for submesh in skn["submeshes"] if submesh["name"] == WEAPON_SUBMESH),
        None,
    )
    if weapon is None:
        raise ValueError(f"Missing {WEAPON_SUBMESH} submesh")
    split_triangles, mixed_triangles = split_weapon(
        skn, weapon, influence_map, powpow_joints, fishbones_joints
    )
    warp_powpow, warp_fishbones, handle_span = make_warps(
        args.scale, rocket_handle, minigun_back, minigun_front
    )

    source_family_indices = {
        family: [index for triangle in triangles for index in triangle]
        for family, triangles in split_triangles.items()
    }
    source_bounds = {
        family: family_bounds(skn["vertices"], indices)
        for family, indices in source_family_indices.items()
    }

    output_vertices = []
    output_indices = []
    output_submeshes = []
    tail_hash_pairs = []

    def append_part(name, source_vertex_indices, source_triangles, warp=None):
        vertex_start = len(output_vertices)
        index_start = len(output_indices)
        ordered_sources = sorted(set(source_vertex_indices))
        remap = {source: vertex_start + offset for offset, source in enumerate(ordered_sources)}
        for source_index in ordered_sources:
            original = skn["vertices"][source_index]
            vertex = bytearray(original)
            if warp is not None:
                position, normal = warp(vertex_position(vertex), vertex_normal(vertex))
                set_position(vertex, position)
                set_normal(vertex, normal)
            tail_hash_pairs.append(
                {
                    "source": source_index,
                    "source_tail": sha256_bytes(bytes(original[12:32] + original[44:])),
                    "output_tail": sha256_bytes(bytes(vertex[12:32] + vertex[44:])),
                }
            )
            output_vertices.append(vertex)
        for triangle in source_triangles:
            output_indices.extend(remap[index] for index in triangle)
        part = {
            "name": name,
            "vertex_start": vertex_start,
            "vertex_count": len(ordered_sources),
            "index_start": index_start,
            "index_count": len(source_triangles) * 3,
        }
        output_submeshes.append(part)
        return part

    for submesh in skn["submeshes"]:
        if submesh["name"] == WEAPON_SUBMESH:
            for family, warp in (
                (POWPOW_SUBMESH, warp_powpow),
                (FISHBONES_SUBMESH, warp_fishbones),
            ):
                triangles = split_triangles[family]
                append_part(
                    family,
                    [index for triangle in triangles for index in triangle],
                    triangles,
                    warp,
                )
            continue

        start = submesh["vertex_start"]
        source_vertex_indices = list(range(start, start + submesh["vertex_count"]))
        index_start = submesh["index_start"]
        raw_indices = skn["indices"][index_start : index_start + submesh["index_count"]]
        triangles = [raw_indices[offset : offset + 3] for offset in range(0, len(raw_indices), 3)]
        warp = warp_powpow if submesh["name"] in POWPOW_AUX_SUBMESHES else None
        append_part(submesh["name"], source_vertex_indices, triangles, warp)

    if len(output_vertices) >= 65536 or max(output_indices) >= 65536:
        raise ValueError("Result exceeds SKN uint16 vertex index limit")
    if any(item["source_tail"] != item["output_tail"] for item in tail_hash_pairs):
        raise ValueError("A skin-weight, influence, UV, or extension field changed")

    output_bytes = write_skn(
        args.out, skn, output_submeshes, output_indices, output_vertices
    )
    output_by_name = {submesh["name"]: submesh for submesh in output_submeshes}
    output_family_indices = {}
    for family in (POWPOW_SUBMESH, FISHBONES_SUBMESH):
        part = output_by_name[family]
        output_family_indices[family] = list(
            range(part["vertex_start"], part["vertex_start"] + part["vertex_count"])
        )
    # Include Pow-Pow's two auxiliary material sections in its geometric bounds.
    for auxiliary in POWPOW_AUX_SUBMESHES:
        submesh = output_by_name[auxiliary]
        output_family_indices[POWPOW_SUBMESH].extend(
            range(submesh["vertex_start"], submesh["vertex_start"] + submesh["vertex_count"])
        )

    pow_back_after, _ = warp_powpow(minigun_back.copy(), Vector((0, 0, 1)))
    pow_front_after, _ = warp_powpow(minigun_front.copy(), Vector((0, 0, 1)))
    fish_handle_after, _ = warp_fishbones(rocket_handle.copy(), Vector((0, 0, 1)))
    report = {
        "status": "PASSED",
        "version": "1.0.6",
        "scale": args.scale,
        "source": {
            "path": os.path.abspath(args.skn),
            "sha256": sha256_bytes(skn["source_bytes"]),
            "vertices": len(skn["vertices"]),
            "indices": len(skn["indices"]),
            "submeshes": [item["name"] for item in skn["submeshes"]],
            "submesh_layout": skn["submeshes"],
        },
        "output": {
            "path": os.path.abspath(args.out),
            "sha256": sha256_bytes(output_bytes),
            "vertices": len(output_vertices),
            "indices": len(output_indices),
            "submeshes": output_submeshes,
        },
        "weapon_split": {
            "triangle_counts": {
                family: len(triangles) for family, triangles in split_triangles.items()
            },
            "mixed_weight_triangles": mixed_triangles,
            "ambiguous_triangles": 0,
        },
        "powpow_linked_components": auxiliary_components,
        "grip_anchors": {
            "rocket_handle": rounded(rocket_handle),
            "minigun_handle_back": rounded(minigun_back),
            "minigun_handle_front": rounded(minigun_front),
            "minigun_handle_span": round(handle_span, 6),
            "maximum_anchor_displacement": round(
                max(
                    (fish_handle_after - rocket_handle).length,
                    (pow_back_after - minigun_back).length,
                    (pow_front_after - minigun_front).length,
                ),
                9,
            ),
        },
        "source_weapon_bounds": source_bounds,
        "output_weapon_bounds": {
            family: family_bounds(output_vertices, indices)
            for family, indices in output_family_indices.items()
        },
        "invariants": {
            "native_skeleton_unchanged": True,
            "native_weapon_submesh_split_by_rig_family": True,
            "skin_weights_influences_uvs_preserved": True,
            "uint16_indices_valid": True,
        },
    }
    os.makedirs(os.path.dirname(os.path.abspath(args.report)), exist_ok=True)
    with open(args.report, "w", encoding="utf-8") as handle:
        json.dump(report, handle, indent=2)
        handle.write("\n")
    print(
        "MODEL_BUILD=PASSED "
        f"SCALE={args.scale:.2f} VERTICES={len(output_vertices)} "
        f"SUBMESHES={len(output_submeshes)} GRIP_DELTA={report['grip_anchors']['maximum_anchor_displacement']}"
    )


if __name__ == "__main__":
    main()
