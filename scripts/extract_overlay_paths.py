import argparse
import hashlib
import json
import os
import shutil
import subprocess
import tempfile
from pathlib import Path


MASK64 = (1 << 64) - 1
PRIME64_1 = 11400714785074694791
PRIME64_2 = 14029467366897019727
PRIME64_3 = 1609587929392839161
PRIME64_4 = 9650029242287828579
PRIME64_5 = 2870177450012600261


def rotl(value, count):
    return ((value << count) | (value >> (64 - count))) & MASK64


def round64(accumulator, lane):
    accumulator = (accumulator + lane * PRIME64_2) & MASK64
    accumulator = rotl(accumulator, 31)
    return (accumulator * PRIME64_1) & MASK64


def merge_round(accumulator, lane):
    accumulator ^= round64(0, lane)
    return (accumulator * PRIME64_1 + PRIME64_4) & MASK64


def xxh64(data, seed=0):
    length = len(data)
    offset = 0
    if length >= 32:
        lane1 = (seed + PRIME64_1 + PRIME64_2) & MASK64
        lane2 = (seed + PRIME64_2) & MASK64
        lane3 = seed & MASK64
        lane4 = (seed - PRIME64_1) & MASK64
        limit = length - 32
        while offset <= limit:
            lane1 = round64(lane1, int.from_bytes(data[offset : offset + 8], "little"))
            lane2 = round64(lane2, int.from_bytes(data[offset + 8 : offset + 16], "little"))
            lane3 = round64(lane3, int.from_bytes(data[offset + 16 : offset + 24], "little"))
            lane4 = round64(lane4, int.from_bytes(data[offset + 24 : offset + 32], "little"))
            offset += 32
        value = (
            rotl(lane1, 1)
            + rotl(lane2, 7)
            + rotl(lane3, 12)
            + rotl(lane4, 18)
        ) & MASK64
        value = merge_round(value, lane1)
        value = merge_round(value, lane2)
        value = merge_round(value, lane3)
        value = merge_round(value, lane4)
    else:
        value = (seed + PRIME64_5) & MASK64
    value = (value + length) & MASK64
    while offset + 8 <= length:
        lane = round64(0, int.from_bytes(data[offset : offset + 8], "little"))
        value ^= lane
        value = (rotl(value, 27) * PRIME64_1 + PRIME64_4) & MASK64
        offset += 8
    if offset + 4 <= length:
        value ^= (
            int.from_bytes(data[offset : offset + 4], "little") * PRIME64_1
        ) & MASK64
        value &= MASK64
        value = (rotl(value, 23) * PRIME64_2 + PRIME64_3) & MASK64
        offset += 4
    while offset < length:
        value ^= (data[offset] * PRIME64_5) & MASK64
        value &= MASK64
        value = (rotl(value, 11) * PRIME64_1) & MASK64
        offset += 1
    value ^= value >> 33
    value = (value * PRIME64_2) & MASK64
    value ^= value >> 29
    value = (value * PRIME64_3) & MASK64
    value ^= value >> 32
    return value & MASK64


def wad_path_hash(path):
    normalized = path.replace("\\", "/").lower().encode("utf-8")
    return f"{xxh64(normalized):016x}"


def sha256_file(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def parse_args():
    parser = argparse.ArgumentParser(
        description="Resolve brand-new WAD paths from a built overlay by xxHash64."
    )
    parser.add_argument("--wadtools", required=True)
    parser.add_argument("--hash-root", required=True)
    parser.add_argument("--wad", required=True)
    parser.add_argument("--out-root", required=True)
    parser.add_argument("--vfx-map", required=True)
    parser.add_argument("--path", action="append", default=[])
    parser.add_argument("--report", required=True)
    return parser.parse_args()


def main():
    args = parse_args()
    output_root = Path(args.out_root).resolve()
    with open(args.vfx_map, "r", encoding="utf-8") as handle:
        mapping = json.load(handle)
    requested = {path.replace("\\", "/") for path in args.path}
    requested.update(path.replace("\\", "/") for path in mapping.values())
    missing = [
        path
        for path in sorted(requested, key=str.lower)
        if not (output_root / Path(*path.lower().split("/"))).is_file()
        and not (output_root / Path(*path.split("/"))).is_file()
    ]
    if not missing:
        raise ValueError("No unresolved overlay paths were found")

    hashes = {path: wad_path_hash(path) for path in missing}
    with tempfile.TemporaryDirectory(prefix="abyssal_overlay_hashes_") as temporary:
        command = [
            os.path.abspath(args.wadtools),
            "--hashtable-dir",
            os.path.abspath(args.hash_root),
            "--progress=false",
            "-L",
            "error",
            "extract",
            "-i",
            os.path.abspath(args.wad),
            "-o",
            temporary,
            "--overwrite",
            "--stats=false",
        ]
        for digest in hashes.values():
            command.extend(("--hash", digest))
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode:
            raise RuntimeError(
                "Hash extraction failed: " + (result.stdout + "\n" + result.stderr).strip()
            )

        rows = []
        temporary_root = Path(temporary)
        extracted = list(temporary_root.rglob("*"))
        for relative, digest in hashes.items():
            candidates = [
                path
                for path in extracted
                if path.is_file() and path.name.lower().startswith(digest)
            ]
            if len(candidates) != 1:
                raise FileNotFoundError(
                    f"Expected one extracted chunk for {relative} ({digest}), got {candidates}"
                )
            destination = output_root / Path(*relative.lower().split("/"))
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(candidates[0], destination)
            if not destination.is_file() or destination.stat().st_size == 0:
                raise ValueError(f"Empty reconstructed overlay path: {destination}")
            rows.append(
                {
                    "path": relative.lower(),
                    "wad_hash": digest,
                    "bytes": destination.stat().st_size,
                    "sha256": sha256_file(destination),
                }
            )

    report = {
        "status": "PASSED",
        "algorithm": "xxh64 lowercase normalized WAD path",
        "requested_paths": len(requested),
        "already_resolved_paths": len(requested) - len(missing),
        "hash_extracted_paths": len(rows),
        "files": rows,
    }
    report_path = Path(args.report)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"OVERLAY_HASH_PATHS=PASSED EXTRACTED={len(rows)}")


if __name__ == "__main__":
    main()
