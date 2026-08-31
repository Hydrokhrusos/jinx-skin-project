import argparse
import json
import os
import struct
import sys


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True)
    parser.add_argument("--addon-root", required=True)
    parser.add_argument("--target-skin", type=int, default=65)
    parser.add_argument("--skins", default="13,37,51,60,62,65")
    parser.add_argument("--report", required=True)
    argv = sys.argv[sys.argv.index("--") + 1 :] if "--" in sys.argv else sys.argv[1:]
    return parser.parse_args(argv)


def main():
    args = parse_args()
    sys.path.insert(0, os.path.abspath(args.addon_root))
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from Aventurine.io.import_skl import read_skl
    import build_model

    root = os.path.abspath(args.root)
    skins = [int(value) for value in args.skins.split(",")]
    skeletons = {}
    models = {}
    for skin in skins:
        folder = os.path.join(root, f"assets/characters/jinx/skins/skin{skin}")
        stem = os.path.join(folder, f"jinx_skin{skin}")
        joints, influence_map = read_skl(stem + ".skl")
        skn = build_model.parse_skn(stem + ".skn")
        skeletons[skin] = (joints, influence_map)
        models[skin] = skn

    target_joints, _ = skeletons[args.target_skin]
    target_names = {joint.name for joint in target_joints}
    rows = []
    for skin in skins:
        joints, influence_map = skeletons[skin]
        skn = models[skin]
        weighted_names = set()
        for vertex in skn["vertices"]:
            local_indices = struct.unpack_from("<4B", vertex, 12)
            weights = struct.unpack_from("<4f", vertex, 16)
            for local_index, weight in zip(local_indices, weights):
                if weight <= 1e-7:
                    continue
                joint_index = influence_map[local_index] if influence_map else local_index
                weighted_names.add(joints[joint_index].name)
        missing = sorted(weighted_names - target_names)
        rows.append(
            {
                "skin": skin,
                "joints": len(joints),
                "vertices": len(skn["vertices"]),
                "triangles": len(skn["indices"]) // 3,
                "submeshes": [item["name"] for item in skn["submeshes"]],
                "weighted_joints": len(weighted_names),
                "weighted_joints_present_in_target": len(weighted_names & target_names),
                "missing_weighted_joints": missing,
                "direct_retarget_coverage": round(
                    len(weighted_names & target_names) / max(1, len(weighted_names)), 6
                ),
            }
        )
    payload = {"target_skin": args.target_skin, "target_joints": len(target_joints), "models": rows}
    os.makedirs(os.path.dirname(os.path.abspath(args.report)), exist_ok=True)
    with open(args.report, "w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2)
        handle.write("\n")
    for row in rows:
        print(
            f"SKIN={row['skin']} VERTICES={row['vertices']} SUBMESHES={len(row['submeshes'])} "
            f"RETARGET={row['direct_retarget_coverage']:.3f} MISSING={len(row['missing_weighted_joints'])}"
        )


if __name__ == "__main__":
    main()
