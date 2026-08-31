import argparse
import glob
import json
import os
import sys
from collections import Counter


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--skn", required=True)
    parser.add_argument("--skl", required=True)
    parser.add_argument("--addon-root", required=True)
    parser.add_argument("--animations")
    parser.add_argument("--out", required=True)
    return parser.parse_args(sys.argv[sys.argv.index("--") + 1 :])


def elf_hash(text):
    value = 0
    for byte in text.lower().encode("utf-8"):
        value = (value << 4) + byte
        high = value & 0xF0000000
        if high:
            value ^= high >> 24
        value &= ~high
    return value & 0xFFFFFFFF


def vec(values):
    return [round(float(value), 6) for value in values]


def xyz(value):
    return (value.x, value.y, value.z)


def main():
    args = parse_args()
    sys.path.insert(0, os.path.abspath(args.addon_root))

    from Aventurine.io.import_skl import read_skl
    from Aventurine.io.import_skn import read_skn
    from Aventurine.io.import_anm import read_anm

    indices, vertices, submeshes = read_skn(args.skn)
    joints, influences = read_skl(args.skl)

    bone_names = [joint.name for joint in joints]
    influence_map = influences or list(range(len(joints)))
    submesh_rows = []
    for submesh in submeshes:
        subset = vertices[
            submesh.vertex_start : submesh.vertex_start + submesh.vertex_count
        ]
        positions = [xyz(vertex.position) for vertex in subset]
        mins = [min(position[i] for position in positions) for i in range(3)]
        maxs = [max(position[i] for position in positions) for i in range(3)]
        weighted = Counter()
        rigid = Counter()
        for vertex in subset:
            active = []
            for local_idx, weight in zip(vertex.influences, vertex.weights):
                if weight <= 0:
                    continue
                joint_idx = influence_map[local_idx]
                name = bone_names[joint_idx]
                weighted[name] += float(weight)
                active.append((name, float(weight)))
            if active:
                rigid[max(active, key=lambda item: item[1])[0]] += 1

        submesh_rows.append(
            {
                "name": submesh.name,
                "elf_hash": f"0x{elf_hash(submesh.name):08x}",
                "vertex_start": submesh.vertex_start,
                "vertex_count": submesh.vertex_count,
                "index_start": submesh.index_start,
                "index_count": submesh.index_count,
                "bounds_min": vec(mins),
                "bounds_max": vec(maxs),
                "weighted_bones": [
                    {"name": name, "weight": round(weight, 4)}
                    for name, weight in weighted.most_common(12)
                ],
                "dominant_bones": [
                    {"name": name, "vertices": count}
                    for name, count in rigid.most_common(12)
                ],
            }
        )

    joint_rows = []
    for index, joint in enumerate(joints):
        joint_rows.append(
            {
                "index": index,
                "name": joint.name,
                "elf_hash": f"0x{elf_hash(joint.name):08x}",
                "parent_index": joint.parent,
                "parent_name": (
                    joints[joint.parent].name if joint.parent >= 0 else None
                ),
                "translation": vec(joint.raw_trans),
                "rotation_wxyz": vec(joint.raw_rot),
                "scale": vec(joint.raw_scale),
            }
        )

    joint_by_hash = {elf_hash(joint.name): joint.name for joint in joints}
    animation_rows = []
    if args.animations:
        for animation_path in sorted(
            glob.glob(os.path.join(args.animations, "**", "*.anm"), recursive=True)
        ):
            animation = read_anm(animation_path)
            track_rows = []
            for track in animation.tracks:
                name = joint_by_hash.get(track.joint_hash)
                if name is None:
                    continue
                if not (
                    "minigun" in name.lower()
                    or "rocket_launcher" in name.lower()
                    or name in {"L_Hand", "R_Hand"}
                ):
                    continue

                track_row = {
                    "joint": name,
                    "joint_hash": f"0x{track.joint_hash:08x}",
                    "keyed_frames": sorted(track.poses),
                }
                for property_name in ("translation", "scale"):
                    values = [
                        getattr(pose, property_name)
                        for pose in track.poses.values()
                        if getattr(pose, property_name) is not None
                    ]
                    if values:
                        components = [tuple(value) for value in values]
                        track_row[property_name] = {
                            "min": vec(
                                min(value[i] for value in components)
                                for i in range(3)
                            ),
                            "max": vec(
                                max(value[i] for value in components)
                                for i in range(3)
                            ),
                        }
                track_rows.append(track_row)

            animation_rows.append(
                {
                    "path": os.path.relpath(animation_path, args.animations).replace(
                        os.sep, "/"
                    ),
                    "fps": round(animation.fps, 6),
                    "duration": round(animation.duration, 6),
                    "frame_count": animation.frame_count,
                    "track_count": len(animation.tracks),
                    "weapon_tracks": track_rows,
                }
            )

    result = {
        "source_skn": os.path.abspath(args.skn),
        "source_skl": os.path.abspath(args.skl),
        "vertices": len(vertices),
        "indices": len(indices),
        "submesh_count": len(submeshes),
        "joint_count": len(joints),
        "influence_count": len(influence_map),
        "submeshes": submesh_rows,
        "joints": joint_rows,
        "animations": animation_rows,
    }
    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2)
        handle.write("\n")

    print(
        f"ASSET_AUDIT=PASSED VERTICES={len(vertices)} "
        f"SUBMESHES={len(submeshes)} JOINTS={len(joints)}"
    )


if __name__ == "__main__":
    main()
