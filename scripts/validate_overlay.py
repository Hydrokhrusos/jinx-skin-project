import argparse
import hashlib
import json
import os


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--content-wad", required=True)
    parser.add_argument("--overlay-extract", required=True)
    parser.add_argument("--overlay-wad", required=True)
    parser.add_argument("--game-wad", required=True)
    parser.add_argument("--builder-log", required=True)
    parser.add_argument("--out", required=True)
    return parser.parse_args()


def sha256_file(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def collect(root):
    files = {}
    for directory, _, names in os.walk(root):
        for name in names:
            path = os.path.join(directory, name)
            relative = os.path.relpath(path, root).replace(os.sep, "/").lower()
            files[relative] = {
                "size": os.path.getsize(path),
                "sha256": sha256_file(path),
            }
    return files


def main():
    args = parse_args()
    content = collect(args.content_wad)
    extracted = collect(args.overlay_extract)
    if len(content) != 11:
        raise ValueError(f"Expected 11 source overrides, found {len(content)}")
    if content != extracted:
        missing = sorted(set(content) - set(extracted))
        extra = sorted(set(extracted) - set(content))
        mismatched = sorted(
            path
            for path in set(content) & set(extracted)
            if content[path] != extracted[path]
        )
        raise ValueError(
            f"Patched WAD payload mismatch; missing={missing}, extra={extra}, mismatched={mismatched}"
        )

    builder_log = open(args.builder_log, "r", encoding="utf-8-sig").read()
    required_log = (
        "WADS_BUILT=1",
        "Jinx.wad.client",
        "CHECKSUM_MISMATCHES=0",
    )
    missing_log = [value for value in required_log if value not in builder_log]
    if missing_log:
        raise ValueError(f"LTK overlay builder did not report success: {missing_log}")

    original_sha = sha256_file(args.game_wad)
    overlay_sha = sha256_file(args.overlay_wad)
    if original_sha == overlay_sha:
        raise ValueError("Overlay Jinx.wad.client is identical to the unmodified game WAD")

    report = {
        "status": "PASSED",
        "version": "1.0.6",
        "target": "DATA/FINAL/Champions/Jinx.wad.client",
        "source_game_wad": {
            "path": os.path.abspath(args.game_wad),
            "size": os.path.getsize(args.game_wad),
            "sha256": original_sha,
        },
        "patched_overlay_wad": {
            "path": os.path.abspath(args.overlay_wad),
            "size": os.path.getsize(args.overlay_wad),
            "sha256": overlay_sha,
        },
        "verified_override_count": len(extracted),
        "verified_overrides": extracted,
        "checks": {
            "ltk_overlay_wad_built": "PASSED",
            "overlay_differs_from_game_wad": "PASSED",
            "wadtools_mount_and_extract": "PASSED",
            "all_override_paths_present": "PASSED",
            "all_override_payload_checksums": "PASSED",
            "overlay_checksum_mismatches": 0,
        },
    }
    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as handle:
        json.dump(report, handle, indent=2)
        handle.write("\n")
    print(
        "OVERLAY_VALIDATION=PASSED "
        f"WAD=Jinx.wad.client OVERRIDES={len(extracted)} SHA256={overlay_sha}"
    )


if __name__ == "__main__":
    main()
