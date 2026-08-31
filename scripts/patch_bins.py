import argparse
import hashlib
import json
import os
import re


SKINS = range(65, 74)
INITIAL_HIDE_FIELDS = (
    "InitialSubmeshToHide",
    "InitialSubmeshShadowsToHide",
    "InitialSubmeshMouseOversToHide",
)
HASHED_INITIAL_HIDE_FIELDS = ("0x80b7f78f", "0xf4ba5c9e", "0x382825a9")
Q_TRANSITION_FILES = {
    "minigun_spell1_weapon_gunonly.anm": {
        "event": "ShowFishbonesDuringRiotHandoff",
        "show": ("Fishbones",),
    },
    "launcher_spell1_weapon.anm": {
        "event": "ShowPowPowDuringRiotHandoff",
        "show": ("PowPow", "WeaponVFX", "Weapon03"),
    },
}


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-dir", required=True)
    parser.add_argument("--out-dir", required=True)
    parser.add_argument("--report", required=True)
    return parser.parse_args()


def sha256_text(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def canonical_clip_key(key):
    if key.startswith("0x"):
        return key
    value = key.strip('"').lower().encode("utf-8")
    result = 0x811C9DC5
    for byte in value:
        result = ((result ^ byte) * 0x01000193) & 0xFFFFFFFF
    return f"0x{result:08x}"


def replace_once(text, old, new, label):
    count = text.count(old)
    if count != 1:
        raise ValueError(f"Expected one {label}, found {count}")
    return text.replace(old, new, 1)


def patch_initial_visibility(text, skin):
    replacements = 0
    for field in INITIAL_HIDE_FIELDS:
        old = f'{field}: string = "Recall"'
        if old in text:
            text = replace_once(
                text,
                old,
                f'{field}: string = "Recall Fishbones"',
                f"{field} in skin{skin}",
            )
            replacements += 1
    for field in HASHED_INITIAL_HIDE_FIELDS:
        old = f'{field}: string = "Recall"'
        if old in text:
            text = replace_once(
                text,
                old,
                f'{field}: string = "Recall Fishbones"',
                f"{field} in skin{skin}",
            )
            replacements += 1
    if replacements != 3:
        raise ValueError(f"Expected three initial-hide fields in skin{skin}, patched {replacements}")
    return text


def patch_material_override(text, skin):
    semantic = re.compile(
        r'(?P<indent>[ \t]*)SkinMeshDataProperties_MaterialOverride \{\n'
        r'(?P=indent)    Material: link = (?P<material>[^\n]+)\n'
        r'(?P=indent)    Submesh: string = "Weapon"\n'
        r'(?P=indent)\}'
    )
    hashed = re.compile(
        r'(?P<indent>[ \t]*)0x8b7a4394 \{\n'
        r'(?P=indent)    0xd2e4d060: link = (?P<material>[^\n]+)\n'
        r'(?P=indent)    0xaad7612c: string = "Weapon"\n'
        r'(?P=indent)\}'
    )
    matches = list(semantic.finditer(text)) + list(hashed.finditer(text))
    if len(matches) != 1:
        raise ValueError(f"Expected one Weapon material override in skin{skin}, found {len(matches)}")
    match = matches[0]
    indent = match.group("indent")
    material = match.group("material")
    if match.re is semantic:
        entry_type, material_field, submesh_field = (
            "SkinMeshDataProperties_MaterialOverride",
            "Material",
            "Submesh",
        )
    else:
        entry_type, material_field, submesh_field = (
            "0x8b7a4394",
            "0xd2e4d060",
            "0xaad7612c",
        )
    replacement = (
        f'{indent}{entry_type} {{\n'
        f'{indent}    {material_field}: link = {material}\n'
        f'{indent}    {submesh_field}: string = "PowPow"\n'
        f'{indent}}}\n'
        f'{indent}{entry_type} {{\n'
        f'{indent}    {material_field}: link = {material}\n'
        f'{indent}    {submesh_field}: string = "Fishbones"\n'
        f'{indent}}}'
    )
    return text[: match.start()] + replacement + text[match.end() :], material


def visibility_event_lines(name, show, hide, indent):
    item = indent + "    "
    lines = [
        f'{indent}"{name}" = SubmeshVisibilityEventData {{',
    ]
    if show:
        lines.append(f"{item}mShowSubmeshList: list[hash] = {{")
        lines.extend(f'{item}    "{submesh}"' for submesh in show)
        lines.append(f"{item}}}")
    if hide:
        lines.append(f"{item}mHideSubmeshList: list[hash] = {{")
        lines.extend(f'{item}    "{submesh}"' for submesh in hide)
        lines.append(f"{item}}}")
    lines.append(f"{indent}}}")
    return lines


def closing_brace(text, opening):
    depth = 0
    for index in range(opening, len(text)):
        if text[index] == "{":
            depth += 1
        elif text[index] == "}":
            depth -= 1
            if depth == 0:
                return index
    raise ValueError("Unterminated BIN text block")


def atomic_clips(text):
    pattern = re.compile(
        r'^(?P<indent>[ \t]+)(?P<key>"[^"]+"|0x[0-9a-f]{8}) = AtomicClipData \{',
        re.MULTILINE,
    )
    clips = []
    for match in pattern.finditer(text):
        opening = text.find("{", match.start())
        end = closing_brace(text, opening) + 1
        block = text[match.start() : end]
        path_match = re.search(r"mAnimationFilePath: file = (?P<path>[^\n]+)", block)
        if path_match is None:
            continue
        clips.append(
            {
                "start": match.start(),
                "end": end,
                "key": match.group("key"),
                "indent": match.group("indent"),
                "path": path_match.group("path").strip().strip('"'),
                "block": block,
            }
        )
    return clips


def add_visibility_event(block, event_name, show, hide, clip_key):
    if event_name in block:
        raise ValueError(f"Visibility event already exists in {clip_key}: {event_name}")
    lines = block.splitlines()
    map_index = next(
        (index for index, line in enumerate(lines) if "mEventDataMap: map[hash,pointer]" in line),
        None,
    )
    if map_index is None:
        tick_index = next(
            (index for index, line in enumerate(lines) if "mTickDuration:" in line),
            None,
        )
        if tick_index is None:
            raise ValueError(f"Animation clip has no event-map insertion point: {clip_key}")
        property_indent = lines[tick_index][: len(lines[tick_index]) - len(lines[tick_index].lstrip())]
        event_indent = property_indent + "    "
        event_map = [f"{property_indent}mEventDataMap: map[hash,pointer] = {{"]
        event_map.extend(visibility_event_lines(event_name, show, hide, event_indent))
        event_map.append(f"{property_indent}}}")
        lines[tick_index:tick_index] = event_map
        return "\n".join(lines)

    map_indent = lines[map_index][: len(lines[map_index]) - len(lines[map_index].lstrip())]
    depth = 0
    map_end = None
    for index in range(map_index, len(lines)):
        depth += lines[index].count("{")
        depth -= lines[index].count("}")
        if depth == 0:
            map_end = index
            break
    if map_end is None:
        raise ValueError(f"Animation event map is unterminated: {clip_key}")
    lines[map_end:map_end] = visibility_event_lines(
        event_name,
        show,
        hide,
        map_indent + "    ",
    )
    return "\n".join(lines)


def riot_weapon_family(animation_path):
    name = os.path.basename(animation_path).lower()
    if name in Q_TRANSITION_FILES or name in {
        "minigun_spell1_weapon2.anm",
        "launcher_spell1_weapon2.anm",
    }:
        return None
    if "minigun" in name:
        return "minigun"
    if "rlauncher" in name or name in {
        "jinx_emote_enter_rocket.anm",
        "jinx_emote_exit_rocket.anm",
    }:
        return "rlauncher"
    return None


def patch_riot_animation_families(text):
    patches = []
    family_clips = []
    transition_clips = []
    for clip in atomic_clips(text):
        basename = os.path.basename(clip["path"]).lower()
        transition = Q_TRANSITION_FILES.get(basename)
        if transition is not None:
            patched = add_visibility_event(
                clip["block"],
                transition["event"],
                transition["show"],
                (),
                clip["key"],
            )
            patches.append((clip["start"], clip["end"], patched))
            transition_clips.append(
                {
                    "clip_key": canonical_clip_key(clip["key"]),
                    "clip": basename,
                    "show": list(transition["show"]),
                }
            )
            continue

        family = riot_weapon_family(clip["path"])
        if family is None:
            continue
        if family == "minigun":
            event_name = "RiotMinigunFamilyVisibility"
            show = ("PowPow", "WeaponVFX", "Weapon03")
            hide = ("Fishbones",)
        else:
            event_name = "RiotRlauncherFamilyVisibility"
            show = ("Fishbones",)
            hide = ("PowPow", "WeaponVFX", "Weapon03")
        patched = add_visibility_event(
            clip["block"],
            event_name,
            show,
            hide,
            clip["key"],
        )
        patches.append((clip["start"], clip["end"], patched))
        family_clips.append(
            {
                "family": family,
                "clip_key": canonical_clip_key(clip["key"]),
                "clip": basename,
                "show": list(show),
                "hide": list(hide),
            }
        )

    for start, end, replacement in sorted(patches, reverse=True):
        text = text[:start] + replacement + text[end:]
    if len(transition_clips) != 2:
        raise ValueError(f"Expected two Riot Q handoff clips, found {len(transition_clips)}")
    family_counts = {
        family: sum(clip["family"] == family for clip in family_clips)
        for family in ("minigun", "rlauncher")
    }
    if family_counts["minigun"] < 20 or family_counts["rlauncher"] < 20:
        raise ValueError(f"Incomplete Riot weapon-family coverage: {family_counts}")
    return text, family_clips, transition_clips, family_counts


def write_text(path, text):
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)


def main():
    args = parse_args()
    report = {"status": "PASSED", "version": "1.0.6", "skins": [], "graph": {}}
    for skin in SKINS:
        source_path = os.path.join(args.source_dir, f"skin{skin}.py")
        output_path = os.path.join(args.out_dir, f"skin{skin}.py")
        source = open(source_path, "r", encoding="utf-8").read()
        patched = patch_initial_visibility(source, skin)
        patched, material = patch_material_override(patched, skin)
        if (
            patched.count('string = "Fishbones"') != 1
            or patched.count('string = "PowPow"') != 1
            or patched.count('string = "Recall Fishbones"') != 3
        ):
            raise ValueError(f"Weapon submesh patch missing in skin{skin}")
        write_text(output_path, patched)
        report["skins"].append(
            {
                "skin": skin,
                "source_sha256": sha256_text(source),
                "output_sha256": sha256_text(patched),
                "weapon_material": material,
                "initially_hidden": "Recall Fishbones",
                "material_submeshes": ["PowPow", "Fishbones"],
            }
        )

    graph_source_path = os.path.join(args.source_dir, "animations_skin65.py")
    graph_output_path = os.path.join(args.out_dir, "animations_skin65.py")
    graph_source = open(graph_source_path, "r", encoding="utf-8").read()
    graph_patched, family_clips, transition_clips, family_counts = patch_riot_animation_families(
        graph_source
    )
    added_events = len(family_clips) + len(transition_clips)
    if graph_patched.count("SubmeshVisibilityEventData") != graph_source.count(
        "SubmeshVisibilityEventData"
    ) + added_events:
        raise ValueError(f"Expected exactly {added_events} weapon-family visibility events")
    write_text(graph_output_path, graph_patched)
    report["graph"] = {
        "source_sha256": sha256_text(graph_source),
        "output_sha256": sha256_text(graph_patched),
        "source": "Riot persistent Minigun and Rlauncher animation families",
        "selection": "the game-selected Riot animation family is the persistent weapon-state signal",
        "transitions": transition_clips,
        "families": family_clips,
        "family_counts": family_counts,
        "state_events": len(family_clips),
        "handoff_events": len(transition_clips),
        "buffbone_state_events": 0,
    }
    os.makedirs(os.path.dirname(os.path.abspath(args.report)), exist_ok=True)
    with open(args.report, "w", encoding="utf-8") as handle:
        json.dump(report, handle, indent=2)
        handle.write("\n")
    print(
        "BIN_PATCH=PASSED SKINS=9 "
        f"MINIGUN_FAMILY_CLIPS={family_counts['minigun']} "
        f"RLAUNCHER_FAMILY_CLIPS={family_counts['rlauncher']} "
        "Q_HANDOFF_CLIPS=2 SOURCE=RiotAnimationFamilies"
    )


if __name__ == "__main__":
    main()
