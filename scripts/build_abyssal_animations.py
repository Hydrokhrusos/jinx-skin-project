import argparse
import bisect
import hashlib
import json
import math
import os
import sys


EXPECTED_GROUPS = {
    "assets/characters/jinx/skins/base/animations": 61,
    "assets/characters/jinx/skins/skin65/animations": 2,
    "assets/characters/jinxmine/skins/skin65/animations": 6,
}


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-root", required=True)
    parser.add_argument("--out-root", required=True)
    parser.add_argument("--addon-root", required=True)
    parser.add_argument("--report", required=True)
    argv = sys.argv[sys.argv.index("--") + 1 :] if "--" in sys.argv else sys.argv[1:]
    return parser.parse_args(argv)


def sha256_file(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def elf_hash(value):
    result = 0
    for character in value.lower():
        result = (result << 4) + ord(character)
        high = result & 0xF0000000
        if high:
            result ^= high >> 24
        result &= ~high
    return result & 0xFFFFFFFF


def interpolate_component(track, frame, attribute, default):
    keyed = sorted(
        (key, getattr(pose, attribute))
        for key, pose in track.poses.items()
        if getattr(pose, attribute) is not None
    )
    if not keyed:
        return default.copy()
    frames = [item[0] for item in keyed]
    index = bisect.bisect_left(frames, frame)
    if index < len(keyed) and keyed[index][0] == frame:
        return keyed[index][1].copy()
    if index == 0:
        return keyed[0][1].copy()
    if index == len(keyed):
        return keyed[-1][1].copy()
    left_frame, left = keyed[index - 1]
    right_frame, right = keyed[index]
    factor = (frame - left_frame) / (right_frame - left_frame)
    if attribute == "rotation":
        return left.slerp(right, factor)
    return left.lerp(right, factor)


def densify(anm, pose_type, vector_type, quaternion_type):
    zero = vector_type((0.0, 0.0, 0.0))
    one = vector_type((1.0, 1.0, 1.0))
    identity = quaternion_type((1.0, 0.0, 0.0, 0.0))
    for track in anm.tracks:
        poses = {}
        for frame in range(anm.frame_count):
            pose = pose_type()
            pose.translation = interpolate_component(track, frame, "translation", zero)
            pose.scale = interpolate_component(track, frame, "scale", one)
            pose.rotation = interpolate_component(track, frame, "rotation", identity)
            poses[frame] = pose
        track.poses = poses


def animation_style(filename):
    name = filename.lower()
    if any(token in name for token in ("attack", "spell", "crit")):
        return "recoil", math.radians(2.8)
    if any(token in name for token in ("run", "haste", "respawn")):
        return "surge", math.radians(2.0)
    if any(token in name for token in ("idle", "channel")):
        return "sway", math.radians(2.3)
    if any(token in name for token in ("dance", "laugh", "joke", "taunt", "recall")):
        return "performance", math.radians(3.4)
    if any(token in name for token in ("death", "stunned")):
        return "fall", math.radians(1.6)
    return "abyssal_motion", math.radians(1.9)


def select_tracks(anm):
    tracks = {track.joint_hash: track for track in anm.tracks}
    preferred = [
        "Spine3",
        "Spine2",
        "Head",
        "Pelvis",
        "Root",
        "Minigun",
        "Rocket_Launcher",
        "Weapon",
        "Body",
    ]
    selected = [tracks[elf_hash(name)] for name in preferred if elf_hash(name) in tracks][:3]
    if not selected:
        selected = sorted(anm.tracks, key=lambda track: track.joint_hash)[:2]
    if not selected:
        raise ValueError("Animation contains no tracks")
    return selected


def mutate_animation(anm, filename, pose_type, vector_type, quaternion_type):
    densify(anm, pose_type, vector_type, quaternion_type)
    selected = select_tracks(anm)
    style, amplitude = animation_style(filename)
    axes = (
        vector_type((0.0, 0.0, 1.0)),
        vector_type((1.0, 0.0, 0.0)),
        vector_type((0.0, 1.0, 0.0)),
    )
    for track_index, track in enumerate(selected):
        axis = axes[track_index % len(axes)]
        phase_offset = track_index * 0.83
        for frame in range(anm.frame_count):
            progress = frame / max(1, anm.frame_count - 1)
            wave = math.sin(progress * math.tau + phase_offset)
            angle = amplitude * (0.32 + wave * 0.68) * (1.0 - track_index * 0.16)
            if abs(angle) < math.radians(0.18):
                angle = math.copysign(math.radians(0.18), angle if angle else 1.0)
            delta = quaternion_type(axis, angle)
            pose = track.poses[frame]
            pose.rotation = (pose.rotation @ delta).normalized()
    return style, [f"0x{track.joint_hash:08x}" for track in selected]


def normalized_path(path):
    return path.replace("\\", "/").lower()


def main():
    args = parse_args()
    sys.path.insert(0, os.path.abspath(args.addon_root))
    from mathutils import Quaternion, Vector
    from Aventurine.io.export_anm import write_anm_from_data
    from Aventurine.io.import_anm import ANMPose, read_anm

    source_root = os.path.abspath(args.source_root)
    output_root = os.path.abspath(args.out_root)
    rows = []
    group_counts = {group: 0 for group in EXPECTED_GROUPS}

    for directory, _, filenames in os.walk(source_root):
        for filename in sorted(filenames):
            if not filename.lower().endswith(".anm"):
                continue
            source = os.path.join(directory, filename)
            relative = normalized_path(os.path.relpath(source, source_root))
            group = next(
                (candidate for candidate in EXPECTED_GROUPS if relative.startswith(candidate + "/")),
                None,
            )
            if group is None:
                continue
            group_counts[group] += 1
            output = os.path.join(output_root, *relative.split("/"))
            os.makedirs(os.path.dirname(output), exist_ok=True)

            animation = read_anm(source)
            source_frames = animation.frame_count
            source_tracks = len(animation.tracks)
            source_fps = animation.fps
            style, changed_tracks = mutate_animation(
                animation, filename, ANMPose, Vector, Quaternion
            )
            write_anm_from_data(output, animation, fps=source_fps)
            roundtrip = read_anm(output)
            if roundtrip.frame_count != source_frames:
                raise ValueError(f"Frame count changed for {relative}")
            if len(roundtrip.tracks) != source_tracks:
                raise ValueError(f"Track count changed for {relative}")
            if abs(roundtrip.fps - source_fps) > 0.001:
                raise ValueError(f"FPS changed for {relative}")
            source_hash = sha256_file(source)
            output_hash = sha256_file(output)
            if source_hash == output_hash:
                raise ValueError(f"Animation did not change: {relative}")
            rows.append(
                {
                    "path": relative,
                    "style": style,
                    "frames": source_frames,
                    "tracks": source_tracks,
                    "fps": round(source_fps, 6),
                    "changed_tracks": changed_tracks,
                    "source_sha256": source_hash,
                    "output_sha256": output_hash,
                }
            )

    if group_counts != EXPECTED_GROUPS:
        raise ValueError(f"Animation corpus changed: expected {EXPECTED_GROUPS}, got {group_counts}")
    if len(rows) != 69:
        raise ValueError(f"Expected 69 rewritten animations, got {len(rows)}")

    payload = {
        "status": "PASSED",
        "variant": "Encore Animation Edition",
        "animation_count": len(rows),
        "groups": group_counts,
        "source_hashes_all_differ": True,
        "frame_track_fps_invariants": True,
        "animations": rows,
    }
    os.makedirs(os.path.dirname(os.path.abspath(args.report)), exist_ok=True)
    with open(args.report, "w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2)
        handle.write("\n")
    print(
        f"ABYSSAL_ANIMATIONS=PASSED FILES={len(rows)} "
        f"FRAMES={sum(item['frames'] for item in rows)}"
    )


if __name__ == "__main__":
    try:
        main()
    except Exception:
        import traceback

        traceback.print_exc()
        sys.exit(1)
