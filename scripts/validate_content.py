import argparse
import hashlib
import json
import os
import re
import struct


EXPECTED_SUBMESHES = (
    "Body",
    "Hair",
    "Skirt",
    "PowPow",
    "Fishbones",
    "WeaponVFX",
    "Weapon03",
    "Recall",
)
EXPECTED_RELATIVE_FILES = {
    "assets/characters/jinx/skins/skin65/jinx_skin65.skn",
    "data/characters/jinx/animations/skin65.bin",
    *{f"data/characters/jinx/skins/skin{skin}.bin" for skin in range(65, 74)},
}


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--content-wad", required=True)
    parser.add_argument("--roundtrip-dir", required=True)
    parser.add_argument("--model-report", required=True)
    parser.add_argument("--bin-report", required=True)
    parser.add_argument("--out", required=True)
    return parser.parse_args()


def sha256_file(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


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
        raise ValueError("Invalid SKN signature")
    major, minor = take("<HH")
    if major != 4:
        raise ValueError(f"Expected SKN 4.x, got {major}.{minor}")
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
    return {
        "major": major,
        "minor": minor,
        "vertex_size": vertex_size,
        "vertex_type": vertex_type,
        "vertex_count": vertex_count,
        "index_count": index_count,
        "submeshes": submeshes,
        "indices": indices,
    }


def validate_mesh(path, model_report):
    mesh = parse_skn(path)
    names = tuple(item["name"] for item in mesh["submeshes"])
    if names != EXPECTED_SUBMESHES:
        raise ValueError(f"Unexpected split submesh layout: {names}")
    if "Weapon" in names:
        raise ValueError("Combined Weapon submesh remains")
    if not model_report["invariants"]["native_weapon_submesh_split_by_rig_family"]:
        raise ValueError("Weapon split invariant failed")
    if mesh["vertex_count"] != model_report["output"]["vertices"]:
        raise ValueError("Mesh vertex count does not match build report")
    if mesh["index_count"] != model_report["output"]["indices"]:
        raise ValueError("Mesh index count does not match build report")
    if model_report["source"]["sha256"] == model_report["output"]["sha256"]:
        raise ValueError("Output mesh is identical to the unscaled Riot source")
    if model_report["grip_anchors"]["maximum_anchor_displacement"] != 0:
        raise ValueError("Grip anchors moved")
    if model_report["weapon_split"]["ambiguous_triangles"] != 0:
        raise ValueError("Weapon classification contains ambiguous triangles")
    if model_report["weapon_split"]["mixed_weight_triangles"] != 0:
        raise ValueError("Weapon classification contains mixed-family triangles")
    if model_report["scale"] != 1.6:
        raise ValueError("Unexpected weapon scale")

    chain = model_report["powpow_linked_components"].get("Weapon03")
    if chain is None or chain.get("role") != "chain":
        raise ValueError("Pow-Pow chain component is not identified")
    if chain["vertices_weighted_to_minigun"] != chain["vertex_count"]:
        raise ValueError("Pow-Pow chain is not fully linked to Riot's Minigun joints")
    if chain["vertices_weighted_to_rocket_launcher"] != 0:
        raise ValueError("Pow-Pow chain is linked to Fishbones")

    for submesh in mesh["submeshes"]:
        start = submesh["index_start"]
        stop = start + submesh["index_count"]
        minimum = submesh["vertex_start"]
        maximum = minimum + submesh["vertex_count"]
        for index in mesh["indices"][start:stop]:
            if not minimum <= index < maximum:
                raise ValueError(f"Out-of-range index in {submesh['name']}: {index}")
    if max(mesh["indices"]) >= 65536:
        raise ValueError("Mesh exceeds uint16 index limit")
    return mesh


def read_text(path):
    return open(path, "r", encoding="utf-8").read()


def extract_block(text, key, type_hash="0x5bd9a1e6"):
    marker = f"{key} = {type_hash} {{"
    start = text.find(marker)
    if start < 0:
        raise ValueError(f"Animation graph block is missing: {key}")
    opening = text.find("{", start)
    depth = 0
    for index in range(opening, len(text)):
        if text[index] == "{":
            depth += 1
        elif text[index] == "}":
            depth -= 1
            if depth == 0:
                return text[start : index + 1]
    raise ValueError(f"Animation graph block is unterminated: {key}")


def extract_visibility_events(clip_block):
    events = []
    marker = " = 0xbcf56e70 {"
    cursor = 0
    while True:
        marker_index = clip_block.find(marker, cursor)
        if marker_index < 0:
            break
        start = clip_block.rfind("\n", 0, marker_index) + 1
        opening = clip_block.find("{", marker_index)
        depth = 0
        for index in range(opening, len(clip_block)):
            if clip_block[index] == "{":
                depth += 1
            elif clip_block[index] == "}":
                depth -= 1
                if depth == 0:
                    events.append(clip_block[start : index + 1])
                    cursor = index + 1
                    break
        else:
            raise ValueError("Visibility event block is unterminated")
    return events


def visibility_hashes(event, list_field):
    list_marker = f"{list_field}: list[hash] = {{"
    list_start = event.find(list_marker)
    if list_start < 0:
        return set()
    list_end = event.find("}", list_start)
    hashes = set(re.findall(r"0x[0-9a-f]{8}", event[list_start:list_end]))
    hashes.discard(list_field)
    return hashes


def require_visibility_event(events, expected_show, expected_hide, label):
    matches = []
    for event in events:
        show = visibility_hashes(event, "0x6d4d42d0")
        hide = visibility_hashes(event, "0xbb41a45b")
        if show == set(expected_show) and hide == set(expected_hide):
            matches.append(event)
    if len(matches) != 1:
        raise ValueError(
            f"Expected one {label} visibility event with show={sorted(expected_show)} "
            f"hide={sorted(expected_hide)}, found {len(matches)}"
        )


def validate_roundtrips(directory, bin_report):
    skin_results = []
    for skin in range(65, 74):
        path = os.path.join(directory, f"skin{skin}.py")
        text = read_text(path)
        if text.count('string = "Recall Fishbones"') != 3:
            raise ValueError(f"skin{skin}: initial Fishbones visibility patch missing")
        if text.count('string = "PowPow"') != 1:
            raise ValueError(f"skin{skin}: PowPow material override missing")
        if text.count('string = "Fishbones"') != 1:
            raise ValueError(f"skin{skin}: Fishbones material override missing")
        if 'string = "Weapon"' in text:
            raise ValueError(f"skin{skin}: combined Weapon material override remains")
        if text.count("0x6e5ceb16") != 1:
            raise ValueError(f"skin{skin}: shared Ocean Song animation graph link missing")
        skin_results.append({"skin": skin, "sha256": sha256_file(path)})

    graph_path = os.path.join(directory, "animations_skin65.py")
    graph = read_text(graph_path)
    graph_report = bin_report["graph"]
    if graph_report["family_counts"] != {"minigun": 21, "rlauncher": 21}:
        raise ValueError(f"Unexpected Riot family coverage: {graph_report['family_counts']}")

    to_fishbones = extract_block(graph, "0xadc1b4e7")
    to_powpow = extract_block(graph, "0x0fd7fa17")
    fishbones_events = extract_visibility_events(to_fishbones)
    powpow_events = extract_visibility_events(to_powpow)
    if len(fishbones_events) != 1 or len(powpow_events) != 1:
        raise ValueError("Riot Q handoff clips do not each contain exactly one visibility event")
    require_visibility_event(
        fishbones_events,
        {"0x6f827b46"},
        set(),
        "Fishbones Q handoff",
    )
    require_visibility_event(
        powpow_events,
        {"0xae091905", "0xf3d47b63", "0xed500a70"},
        set(),
        "Pow-Pow Q handoff",
    )

    family_results = []
    for clip in graph_report["families"]:
        block = extract_block(graph, clip["clip_key"])
        events = extract_visibility_events(block)
        if len(events) != 1:
            raise ValueError(
                f"{clip['clip_key']} ({clip['clip']}): expected exactly one family visibility event, "
                f"found {len(events)}"
            )
        if clip["family"] == "minigun":
            expected_show = {"0xae091905", "0xf3d47b63", "0xed500a70"}
            expected_hide = {"0x6f827b46"}
        elif clip["family"] == "rlauncher":
            expected_show = {"0x6f827b46"}
            expected_hide = {"0xae091905", "0xf3d47b63", "0xed500a70"}
        else:
            raise ValueError(f"Unknown Riot animation family: {clip['family']}")
        require_visibility_event(
            events,
            expected_show,
            expected_hide,
            f"{clip['family']} family {clip['clip_key']}",
        )
        family_results.append(
            {
                "family": clip["family"],
                "clip_key": clip["clip_key"],
                "clip": clip["clip"],
            }
        )

    for key in ("0x622bd465", "0x2ec639bb", "0x1d39abef", "0x5316001f"):
        if "0xbcf56e70" in extract_block(graph, key):
            raise ValueError(f"Visibility event incorrectly attached to non-state clip {key}")

    return skin_results, {
        "sha256": sha256_file(graph_path),
        "source": "Riot persistent Minigun and Rlauncher animation families",
        "selection": "game-selected Riot family",
        "to_fishbones_clip_key": "0xadc1b4e7",
        "to_fishbones_clip": "minigun_spell1_weapon_gunonly.anm",
        "to_powpow_clip_key": "0x0fd7fa17",
        "to_powpow_clip": "launcher_spell1_weapon.anm",
        "q_handoff_visibility_events": 2,
        "state_visibility_events": len(family_results),
        "family_counts": graph_report["family_counts"],
        "family_clips": family_results,
        "buffbone_state_events": 0,
        "powpow_hidden_with_chain": ["PowPow", "WeaponVFX", "Weapon03"],
    }


def collect_content_files(root):
    files = {}
    for directory, _, names in os.walk(root):
        for name in names:
            path = os.path.join(directory, name)
            relative = os.path.relpath(path, root).replace(os.sep, "/")
            files[relative] = {
                "size": os.path.getsize(path),
                "sha256": sha256_file(path),
            }
    return files


def main():
    args = parse_args()
    model_report = json.load(open(args.model_report, "r", encoding="utf-8"))
    bin_report = json.load(open(args.bin_report, "r", encoding="utf-8"))
    if model_report.get("status") != "PASSED" or bin_report.get("status") != "PASSED":
        raise ValueError("An upstream build report did not pass")

    files = collect_content_files(args.content_wad)
    if set(files) != EXPECTED_RELATIVE_FILES:
        missing = sorted(EXPECTED_RELATIVE_FILES - set(files))
        extra = sorted(set(files) - EXPECTED_RELATIVE_FILES)
        raise ValueError(f"Content allowlist mismatch; missing={missing}, extra={extra}")
    mesh_path = os.path.join(
        args.content_wad,
        "assets",
        "characters",
        "jinx",
        "skins",
        "skin65",
        "jinx_skin65.skn",
    )
    mesh = validate_mesh(mesh_path, model_report)
    skin_roundtrips, graph_roundtrip = validate_roundtrips(args.roundtrip_dir, bin_report)

    report = {
        "status": "PASSED",
        "version": "1.0.6",
        "target": "Jinx.wad.client",
        "source_skin": 65,
        "content_file_count": len(files),
        "content_files": files,
        "mesh": {
            "version": f"{mesh['major']}.{mesh['minor']}",
            "vertices": mesh["vertex_count"],
            "indices": mesh["index_count"],
            "submeshes": [item["name"] for item in mesh["submeshes"]],
            "weapon_scale": model_report["scale"],
            "maximum_grip_anchor_displacement": model_report["grip_anchors"][
                "maximum_anchor_displacement"
            ],
        },
        "bin_roundtrip": {
            "skins": skin_roundtrips,
            "animation_graph": graph_roundtrip,
        },
        "checks": {
            "content_allowlist": "PASSED",
            "skn_structure": "PASSED",
            "weapon_submesh_split": "PASSED",
            "weapon_family_classification": "PASSED",
            "powpow_chain_rig_linkage": "PASSED",
            "grip_anchors": "PASSED",
            "skin_bins_roundtrip": "PASSED",
            "riot_q_handoff_visibility_roundtrip": "PASSED",
            "riot_persistent_family_visibility_roundtrip": "PASSED",
            "no_buffbone_state_visibility_events": "PASSED",
        },
    }
    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as handle:
        json.dump(report, handle, indent=2)
        handle.write("\n")
    print(
        "CONTENT_VALIDATION=PASSED "
        f"FILES={len(files)} SKINS={len(skin_roundtrips)} "
        f"VERTICES={mesh['vertex_count']} RIOT_FAMILY_CLIPS={len(graph_roundtrip['family_clips'])} "
        "RIOT_Q_HANDOFF_CLIPS=2"
    )


if __name__ == "__main__":
    main()
