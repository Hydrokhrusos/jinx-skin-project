import argparse
import json
import os
import sys


def rounded(values):
    return [round(float(value), 5) for value in values]


def scale_summary(track):
    keyed = {
        int(frame): rounded(pose.scale)
        for frame, pose in track.poses.items()
        if pose.scale is not None
    }
    if not keyed:
        return None
    frames = sorted(keyed)
    return {
        "first": {"frame": frames[0], "value": keyed[frames[0]]},
        "last": {"frame": frames[-1], "value": keyed[frames[-1]]},
        "unique": sorted({tuple(value) for value in keyed.values()}),
    }


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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--addon-root", required=True)
    parser.add_argument("--skl", required=True)
    parser.add_argument("--anm", action="append", required=True)
    parser.add_argument("--summary", action="store_true")
    args = parser.parse_args(sys.argv[sys.argv.index("--") + 1 :])

    sys.path.insert(0, os.path.abspath(args.addon_root))
    from Aventurine.io.import_anm import read_anm
    from Aventurine.io.import_skl import read_skl
    from Aventurine.utils.binary_utils import Hash

    joints, _ = read_skl(args.skl)
    by_name = {joint.name: index for index, joint in enumerate(joints)}
    weapon_indices = descendants(joints, by_name["Minigun"]) | descendants(
        joints, by_name["Rocket_Launcher"]
    )
    names_by_hash = {Hash.elf(joints[index].name): joints[index].name for index in weapon_indices}

    result = {}
    for path in args.anm:
        anm = read_anm(path)
        if args.summary:
            root_tracks = {}
            for track in anm.tracks:
                name = names_by_hash.get(track.joint_hash)
                if name not in {"Minigun", "Rocket_Launcher"}:
                    continue
                root_tracks[name] = scale_summary(track)
            result[os.path.basename(path)] = {
                "frame_count": anm.frame_count,
                "fps": anm.fps,
                "weapon_root_scales": root_tracks,
            }
            continue
        tracks = {}
        for track in anm.tracks:
            name = names_by_hash.get(track.joint_hash)
            if name is None:
                continue
            frames = {}
            for frame, pose in sorted(track.poses.items()):
                frames[str(frame)] = {
                    "translation": rounded(pose.translation) if pose.translation is not None else None,
                    "scale": rounded(pose.scale) if pose.scale is not None else None,
                }
            tracks[name] = frames
        result[os.path.basename(path)] = {
            "frame_count": anm.frame_count,
            "fps": anm.fps,
            "weapon_tracks": tracks,
        }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
