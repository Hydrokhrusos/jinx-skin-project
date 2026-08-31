import argparse
import glob
import json
import os
import sys

import bpy


class Reporter:
    def report(self, levels, message):
        print(f"AVENTURINE_{'/'.join(sorted(levels))}={message}")


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--skl", required=True)
    parser.add_argument("--animations", required=True)
    parser.add_argument("--addon-root", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--pattern", default="*.anm")
    return parser.parse_args(sys.argv[sys.argv.index("--") + 1 :])


def rounded(vector):
    return [round(float(value), 6) for value in vector]


def distance(a, b):
    return round(float((a - b).length), 6)


def main():
    args = parse_args()
    sys.path.insert(0, os.path.abspath(args.addon_root))

    from Aventurine.io import import_anm
    from Aventurine.io.import_skl import create_armature, read_skl

    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)

    joints, _ = read_skl(args.skl)
    armature = create_armature(joints, name="OceanSongJinx", bone_orient="NATIVE")
    armature.select_set(True)
    bpy.context.view_layer.objects.active = armature

    hand_names = ("L_Hand", "R_Hand")
    handle_names = (
        "Minigun_Handle_Front",
        "Minigun_Handle_Back",
        "Rocket_Launcher_Handle",
    )
    rows = []
    paths = sorted(
        glob.glob(
            os.path.join(args.animations, "**", args.pattern), recursive=True
        )
    )
    for animation_path in paths:
        previous_actions = set(bpy.data.actions)
        status = import_anm.load(
            Reporter(),
            bpy.context,
            animation_path,
            create_new_action=True,
            adapt_to_edits=False,
        )
        if status != {"FINISHED"}:
            raise RuntimeError(f"Could not import {animation_path}: {status}")

        animation = import_anm.read_anm(animation_path)
        frames = sorted({0, max(0, animation.frame_count // 2), max(0, animation.frame_count - 1)})
        samples = []
        for frame in frames:
            bpy.context.scene.frame_set(frame)
            bpy.context.view_layer.update()
            positions = {
                name: armature.pose.bones[name].matrix.translation.copy()
                for name in hand_names + handle_names
            }
            distances = {
                f"{hand}->{handle}": distance(positions[hand], positions[handle])
                for hand in hand_names
                for handle in handle_names
            }
            samples.append(
                {
                    "frame": frame,
                    "positions": {
                        name: rounded(position)
                        for name, position in positions.items()
                    },
                    "distances": distances,
                }
            )

        rows.append(
            {
                "path": os.path.relpath(animation_path, args.animations).replace(
                    os.sep, "/"
                ),
                "frame_count": animation.frame_count,
                "samples": samples,
            }
        )

        armature.animation_data_clear()
        for action in set(bpy.data.actions) - previous_actions:
            bpy.data.actions.remove(action)

    result = {
        "source_skl": os.path.abspath(args.skl),
        "animation_root": os.path.abspath(args.animations),
        "animations": rows,
    }
    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2)
        handle.write("\n")

    print(f"GRIP_AUDIT=PASSED ANIMATIONS={len(rows)}")


if __name__ == "__main__":
    main()
