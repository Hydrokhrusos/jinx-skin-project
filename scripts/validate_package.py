import argparse
import hashlib
import json
import os


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--config", required=True)
    parser.add_argument("--source-content", required=True)
    parser.add_argument("--extracted-content", required=True)
    parser.add_argument("--info", required=True)
    parser.add_argument("--routing", required=True)
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
    config = json.load(open(args.config, "r", encoding="utf-8"))
    if config["version"] != "1.0.6":
        raise ValueError("Package config is not semantic version 1.0.6")
    if [layer["name"] for layer in config["layers"]] != ["base"]:
        raise ValueError("Expected exactly one base package layer")

    source_files = collect(args.source_content)
    extracted_files = collect(args.extracted_content)
    auxiliary_files = {}
    for auxiliary in ("readme.md", "license", "license.md", "license.txt"):
        if auxiliary in extracted_files:
            auxiliary_files[auxiliary] = extracted_files.pop(auxiliary)
    if set(auxiliary_files) != {"readme.md"}:
        raise ValueError(f"Unexpected package metadata files: {sorted(auxiliary_files)}")
    source_readme = os.path.join(os.path.dirname(os.path.abspath(args.config)), "README.md")
    if auxiliary_files["readme.md"]["sha256"] != sha256_file(source_readme):
        raise ValueError("Extracted package README does not match the project README")
    if source_files != extracted_files:
        missing = sorted(set(source_files) - set(extracted_files))
        extra = sorted(set(extracted_files) - set(source_files))
        mismatched = sorted(
            path
            for path in set(source_files) & set(extracted_files)
            if source_files[path] != extracted_files[path]
        )
        raise ValueError(
            f"Extracted package mismatch; missing={missing}, extra={extra}, mismatched={mismatched}"
        )
    if len(source_files) != 11:
        raise ValueError(f"Expected 11 package files, found {len(source_files)}")

    info = open(args.info, "r", encoding="utf-8-sig").read()
    required_info = (
        "ocean-song-jinx-weapon-upscale",
        "Version: 1.0.6",
        "base (priority: 0)",
    )
    missing_info = [value for value in required_info if value not in info]
    if missing_info:
        raise ValueError(f"league-mod info validation failed: {missing_info}")

    routing = open(args.routing, "r", encoding="utf-8-sig").read()
    required_routing = (
        "ROUTED_WADS=jinx.wad.client",
        "WAD=jinx.wad.client OVERRIDES=11",
    )
    missing_routing = [value for value in required_routing if value not in routing]
    if missing_routing:
        raise ValueError(f"LTK ModpkgContent routing validation failed: {missing_routing}")
    routed_paths = {
        line.rsplit(" ", 1)[0].replace("\\", "/").lower()
        for line in routing.splitlines()
        if (line.startswith("assets/") or line.startswith("data/")) and " " in line
    }
    expected_routed_paths = {
        path.split("/", 2)[2]
        for path in source_files
        if path.startswith("base/jinx.wad.client/")
    }
    if routed_paths != expected_routed_paths:
        raise ValueError(
            "LTK ModpkgContent exposed the wrong override paths; "
            f"missing={sorted(expected_routed_paths - routed_paths)}, "
            f"extra={sorted(routed_paths - expected_routed_paths)}"
        )

    report = {
        "status": "PASSED",
        "name": config["name"],
        "version": config["version"],
        "package": {
            "path": os.path.abspath(args.package),
            "size": os.path.getsize(args.package),
            "sha256": sha256_file(args.package),
        },
        "layer": "base",
        "file_count": len(source_files),
        "auxiliary_files": auxiliary_files,
        "files": source_files,
        "checks": {
            "league_mod_info": "PASSED",
            "semantic_version": "PASSED",
            "layer_metadata": "PASSED",
            "extracted_file_allowlist": "PASSED",
            "extracted_payload_checksums": "PASSED",
            "ltk_modpkg_0_9_1_wad_index": "PASSED",
            "ltk_modpkg_content_routing": "PASSED",
        },
    }
    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as handle:
        json.dump(report, handle, indent=2)
        handle.write("\n")
    print(
        "PACKAGE_VALIDATION=PASSED "
        f"FILES={len(source_files)} SHA256={report['package']['sha256']}"
    )


if __name__ == "__main__":
    main()
