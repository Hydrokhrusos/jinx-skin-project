import argparse
import json
import os
import struct
import sys

from mathutils import Matrix


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--jinx-root", required=True)
    parser.add_argument("--nami-root", required=True)
    parser.add_argument("--morgana-root", required=True)
    parser.add_argument("--addon-root", required=True)
    parser.add_argument("--report", required=True)
    argv = sys.argv[sys.argv.index("--") + 1 :] if "--" in sys.argv else sys.argv[1:]
    return parser.parse_args(argv)


def parse_skn(path):
    data = open(path, "rb").read()
    offset = 0

    def take(fmt):
        nonlocal offset
        size = struct.calcsize(fmt)
        values = struct.unpack_from(fmt, data, offset)
        offset += size
        return values[0] if len(values) == 1 else values

    if take("<I") != 0x00112233:
        raise ValueError(f"Unexpected SKN signature: {path}")
    major, minor = take("<HH")
    submeshes = []
    for _ in range(take("<I")):
        name = data[offset : offset + 64].split(b"\0", 1)[0].decode("ascii")
        offset += 64
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
    offset += 4
    index_count, vertex_count, vertex_size, vertex_type = take("<IIII")
    offset += 40
    indices = list(take(f"<{index_count}H"))
    vertices = [
        data[offset + index * vertex_size : offset + (index + 1) * vertex_size]
        for index in range(vertex_count)
    ]
    return {
        "version": [major, minor],
        "vertex_size": vertex_size,
        "vertex_type": vertex_type,
        "submeshes": submeshes,
        "indices": indices,
        "vertices": vertices,
    }


def rounded(values):
    return [round(float(value), 5) for value in values]


def inspect_tex(path):
    with open(path, "rb") as handle:
        header = handle.read(12)
    if len(header) < 12 or header[:4] != b"TEX\0":
        return {"format": "unsupported"}
    width, height = struct.unpack_from("<HH", header, 4)
    format_code = header[9]
    return {
        "width": width,
        "height": height,
        "format_code": f"0x{format_code:02x}",
        "format": {0x0A: "BC1", 0x0C: "BC3"}.get(format_code, "other"),
    }


def global_joint_matrices(joints):
    matrices = [None] * len(joints)

    def calculate(index):
        if matrices[index] is not None:
            return matrices[index]
        joint = joints[index]
        local = (
            Matrix.Translation(joint.raw_trans)
            @ joint.raw_rot.to_matrix().to_4x4()
            @ Matrix.Diagonal((*joint.raw_scale, 1.0))
        )
        matrices[index] = (
            calculate(joint.parent) @ local if joint.parent >= 0 else local
        )
        return matrices[index]

    for joint_index in range(len(joints)):
        calculate(joint_index)
    return matrices


def inspect_model(
    champion,
    skin,
    root,
    target_joints,
    target_names,
    target_influence_names,
    target_globals,
    read_skl,
):
    skin_name = str(skin)
    skin_number = int(skin_name)
    folder = os.path.join(root, f"assets/characters/{champion}/skins/skin{skin_name}")
    stem = os.path.join(folder, f"{champion}_skin{skin_name}")
    joints, influences = read_skl(stem + ".skl")
    joint_by_name = {joint.name: index for index, joint in enumerate(joints)}
    target_by_name = {joint.name: index for index, joint in enumerate(target_joints)}
    donor_globals = global_joint_matrices(joints)
    skn = parse_skn(stem + ".skn")
    texture_files = sorted(
        name for name in os.listdir(folder) if name.lower().endswith(".tex")
    )
    texture_layouts = {
        name: inspect_tex(os.path.join(folder, name)) for name in texture_files
    }
    submesh_rows = []
    model_weighted = set()

    for submesh in skn["submeshes"]:
        start = submesh["vertex_start"]
        stop = start + submesh["vertex_count"]
        positions = []
        uvs = []
        weighted = {}
        dominant = {}
        for vertex in skn["vertices"][start:stop]:
            positions.append(struct.unpack_from("<3f", vertex, 0))
            local_indices = struct.unpack_from("<4B", vertex, 12)
            weights = struct.unpack_from("<4f", vertex, 16)
            uvs.append(struct.unpack_from("<2f", vertex, 44))
            dominant_slot = max(range(4), key=lambda index: weights[index])
            for slot, (local_index, weight) in enumerate(zip(local_indices, weights)):
                if weight <= 1e-7:
                    continue
                joint_index = influences[local_index] if influences else local_index
                joint_name = joints[joint_index].name
                model_weighted.add(joint_name)
                weighted[joint_name] = weighted.get(joint_name, 0.0) + weight
                if slot == dominant_slot:
                    dominant[joint_name] = dominant.get(joint_name, 0) + 1
        weighted_names = set(weighted)
        missing = sorted(weighted_names - target_names)
        missing_influences = sorted(weighted_names - target_influence_names)
        influence_fallbacks = {}
        for joint_name in missing_influences:
            if joint_name not in target_by_name:
                influence_fallbacks[joint_name] = None
                continue
            target_index = target_by_name[joint_name]
            while (
                target_index >= 0
                and target_joints[target_index].name not in target_influence_names
            ):
                target_index = target_joints[target_index].parent
            influence_fallbacks[joint_name] = (
                target_joints[target_index].name if target_index >= 0 else None
            )
        bind_deltas = []
        for joint_name in sorted(weighted_names & target_names):
            donor_matrix = donor_globals[joint_by_name[joint_name]]
            target_matrix = target_globals[target_by_name[joint_name]]
            donor_translation, donor_rotation, donor_scale = donor_matrix.decompose()
            target_translation, target_rotation, target_scale = target_matrix.decompose()
            translation_vector = donor_translation - target_translation
            rotation_angle = target_rotation.rotation_difference(donor_rotation).angle
            rotation_angle = min(rotation_angle, abs(6.283185307179586 - rotation_angle))
            bind_deltas.append(
                {
                    "name": joint_name,
                    "translation": (donor_translation - target_translation).length,
                    "translation_vector": [float(value) for value in translation_vector],
                    "rotation_degrees": rotation_angle * 57.29577951308232,
                    "scale": max(
                        abs(float(donor_scale[index] - target_scale[index]))
                        for index in range(3)
                    ),
                }
            )
        bind_deltas.sort(
            key=lambda row: max(row["translation"], row["rotation_degrees"], row["scale"]),
            reverse=True,
        )
        minimum = [min(value[index] for value in positions) for index in range(3)]
        maximum = [max(value[index] for value in positions) for index in range(3)]
        uv_minimum = [min(value[index] for value in uvs) for index in range(2)]
        uv_maximum = [max(value[index] for value in uvs) for index in range(2)]
        submesh_rows.append(
            {
                "name": submesh["name"],
                "vertices": submesh["vertex_count"],
                "triangles": submesh["index_count"] // 3,
                "bounds_min": rounded(minimum),
                "bounds_max": rounded(maximum),
                "uv_min": rounded(uv_minimum),
                "uv_max": rounded(uv_maximum),
                "weighted_joints": len(weighted_names),
                "target_joint_coverage": round(
                    len(weighted_names & target_names) / max(1, len(weighted_names)), 6
                ),
                "missing_target_joints": missing,
                "target_influence_coverage": round(
                    len(weighted_names & target_influence_names)
                    / max(1, len(weighted_names)),
                    6,
                ),
                "missing_target_influences": missing_influences,
                "influence_fallbacks": influence_fallbacks,
                "bind_pose_delta_max": {
                    "translation": round(
                        max((row["translation"] for row in bind_deltas), default=0.0), 6
                    ),
                    "rotation_degrees": round(
                        max(
                            (row["rotation_degrees"] for row in bind_deltas), default=0.0
                        ),
                        6,
                    ),
                    "scale": round(
                        max((row["scale"] for row in bind_deltas), default=0.0), 6
                    ),
                },
                "largest_bind_pose_deltas": [
                    {
                        "name": row["name"],
                        "translation": round(row["translation"], 6),
                        "translation_vector": rounded(row["translation_vector"]),
                        "rotation_degrees": round(row["rotation_degrees"], 6),
                        "scale": round(row["scale"], 6),
                    }
                    for row in bind_deltas[:12]
                    if max(row["translation"], row["rotation_degrees"], row["scale"])
                    > 1e-6
                ],
                "top_weighted_joints": [
                    {"name": name, "weight": round(weight, 4)}
                    for name, weight in sorted(
                        weighted.items(), key=lambda item: item[1], reverse=True
                    )[:16]
                ],
                "top_dominant_joints": [
                    {"name": name, "vertices": count}
                    for name, count in sorted(
                        dominant.items(), key=lambda item: item[1], reverse=True
                    )[:16]
                ],
            }
        )

    return {
        "champion": champion,
        "skin": skin_number,
        "joints": len(joints),
        "vertices": len(skn["vertices"]),
        "triangles": len(skn["indices"]) // 3,
        "texture_files": texture_files,
        "texture_layouts": texture_layouts,
        "target_joint_coverage": round(
            len(model_weighted & target_names) / max(1, len(model_weighted)), 6
        ),
        "missing_target_joints": sorted(model_weighted - target_names),
        "submeshes": submesh_rows,
    }


def main():
    args = parse_args()
    sys.path.insert(0, os.path.abspath(args.addon_root))
    from Aventurine.io.import_skl import read_skl

    target_stem = os.path.join(
        args.jinx_root, "assets/characters/jinx/skins/skin65/jinx_skin65"
    )
    target_joints, target_influences = read_skl(target_stem + ".skl")
    target_names = {joint.name for joint in target_joints}
    target_influence_names = {
        target_joints[index].name for index in target_influences
    }
    target_globals = global_joint_matrices(target_joints)
    models = []
    for skin in (13, 20, 37, 38, 40, 51, 60, 62, 65):
        models.append(
            inspect_model(
                "jinx",
                skin,
                args.jinx_root,
                target_joints,
                target_names,
                target_influence_names,
                target_globals,
                read_skl,
            )
        )
    for skin in ("07", "32", "51"):
        models.append(
            inspect_model(
                "nami",
                skin,
                args.nami_root,
                target_joints,
                target_names,
                target_influence_names,
                target_globals,
                read_skl,
            )
        )
    models.append(
        inspect_model(
            "morgana",
            "26",
            args.morgana_root,
            target_joints,
            target_names,
            target_influence_names,
            target_globals,
            read_skl,
        )
    )
    payload = {
        "status": "PASSED",
        "target": {
            "champion": "jinx",
            "skin": 65,
            "joints": len(target_joints),
            "influences": len(target_influences),
            "influence_names": sorted(target_influence_names),
        },
        "models": models,
    }
    os.makedirs(os.path.dirname(os.path.abspath(args.report)), exist_ok=True)
    with open(args.report, "w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2)
        handle.write("\n")
    print(f"SOURCE_COMPONENT_AUDIT=PASSED MODELS={len(models)}")


if __name__ == "__main__":
    main()
