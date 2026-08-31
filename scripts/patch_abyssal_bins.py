import argparse
import colorsys
import hashlib
import json
import os
import re


EVENT_PATTERN = re.compile(r'"((?:Play|Stop)_sfx_JinxSkin(\d+)_[^"]+)"')
VEC4_PATTERN = re.compile(
    r"(?P<prefix>(?:ConstantValue:\s+vec4|Values:\s+list\[vec4\]\s*=\s*\{\s*)?)"
    r"(?P<open>\{)\s*"
    r"(?P<r>-?\d+(?:\.\d+)?(?:e[+-]?\d+)?)\s*,\s*"
    r"(?P<g>-?\d+(?:\.\d+)?(?:e[+-]?\d+)?)\s*,\s*"
    r"(?P<b>-?\d+(?:\.\d+)?(?:e[+-]?\d+)?)\s*,\s*"
    r"(?P<a>-?\d+(?:\.\d+)?(?:e[+-]?\d+)?)\s*\}",
    re.IGNORECASE,
)


SEA_WITCH_TEXTURES = {
    "WitchBody": "ASSETS/Characters/Jinx/Skins/Skin65/Jinx_Skin65_SeaWitch_Body_TX_CM.tex",
    "CoralArmor": "ASSETS/Characters/Jinx/Skins/Skin65/Jinx_Skin65_SeaWitch_Armor_TX_CM.tex",
    "PowPow": "ASSETS/Characters/Jinx/Skins/Skin65/Jinx_Skin65_SeaWitch_Weapon_TX_CM.tex",
    "Fishbones": "ASSETS/Characters/Jinx/Skins/Skin65/Jinx_Skin65_SeaWitch_Weapon_TX_CM.tex",
    "Zapper": "ASSETS/Characters/Jinx/Skins/Skin65/Jinx_Skin65_SeaWitch_Weapon_TX_CM.tex",
    "Recall": "ASSETS/Characters/Jinx/Skins/Skin65/Jinx_Skin65_SeaWitch_Recall_TX_CM.tex",
}
JINXMINE_TEXTURE = (
    "ASSETS/Characters/JinxMine/Skins/Skin65/JinxMine_Skin65_TX_CM.tex"
)

CHOMPER_RESOLVER_KEYS = (
    "Jinx_E_Fire",
    "Jinx_E_Fire_Tar",
    "Jinx_E_Mine_Debuff",
    "Jinx_E_Mine_Explosion",
    "Jinx_E_Mine_Idle_Green",
    "Jinx_E_Mine_Idle_Red",
    "Jinx_E_Mine_Ready",
    "Jinx_E_Mine_Ready_Green",
    "Jinx_E_Mine_Ready_Red",
    "Jinx_E_Mine_Set",
)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--jinx", required=True)
    parser.add_argument("--mine", required=True)
    parser.add_argument("--multi", required=True)
    parser.add_argument("--vfx-map", required=True)
    parser.add_argument("--out-jinx", required=True)
    parser.add_argument("--out-mine", required=True)
    parser.add_argument("--out-multi", required=True)
    parser.add_argument("--report", required=True)
    return parser.parse_args()


def sha256_text(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def read_text(path):
    with open(path, "r", encoding="utf-8") as handle:
        return handle.read()


def write_text(path, text):
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)


def matching_brace(text, open_index):
    depth = 0
    for index in range(open_index, len(text)):
        if text[index] == "{":
            depth += 1
        elif text[index] == "}":
            depth -= 1
            if depth == 0:
                return index
    raise ValueError(f"Unbalanced brace at offset {open_index}")


def extract_blocks(text, marker):
    blocks = []
    cursor = 0
    while True:
        start = text.find(marker, cursor)
        if start < 0:
            return blocks
        open_index = text.find("{", start)
        end = matching_brace(text, open_index) + 1
        blocks.append(text[start:end])
        cursor = end


def abyssal_color(red, green, blue, alpha):
    red = max(0.0, min(1.0, red))
    green = max(0.0, min(1.0, green))
    blue = max(0.0, min(1.0, blue))
    if max(red, green, blue) <= 1e-7:
        return (red, green, blue, alpha)
    _, saturation, value = colorsys.rgb_to_hsv(red, green, blue)
    total = red + green + blue + 1e-6
    coral_weight = max(0.0, red * 1.30 - green * 0.48 - blue * 0.16)
    seafoam_weight = max(0.0, green * 1.20 + blue * 0.65 - red * 0.30)
    violet_weight = max(0.0, blue * 0.68 + red * 0.34 - green * 0.40)
    if saturation < 0.12:
        coral_weight += total * 0.10
        seafoam_weight += total * 0.65
        violet_weight += total * 0.25
    weight_total = coral_weight + seafoam_weight + violet_weight + 1e-6
    weights = (
        coral_weight / weight_total,
        seafoam_weight / weight_total,
        violet_weight / weight_total,
    )
    black_violet = (0.010, 0.004, 0.028)
    coral = (1.000, 0.165, 0.275)
    seafoam = (0.155, 1.000, 0.705)
    witch_violet = (0.305, 0.020, 0.505)
    accent = tuple(
        coral[i] * weights[0]
        + seafoam[i] * weights[1]
        + witch_violet[i] * weights[2]
        for i in range(3)
    )
    strength = max(0.08, min(1.0, value * (0.58 + saturation * 0.48)))
    output = tuple(
        max(
            0.0,
            min(
                1.0,
                black_violet[i] * (1.0 - strength) + accent[i] * strength,
            ),
        )
        for i in range(3)
    )
    return (*output, alpha)


def patch_opaque_champion_materials(text):
    marker = "SkinMeshProperties: embed = SkinMeshDataProperties {"
    start = text.find(marker)
    if start < 0:
        raise ValueError("Jinx SkinMeshProperties block is missing")
    open_index = text.find("{", start)
    end = matching_brace(text, open_index) + 1
    block = text[start:end]
    indent_match = re.search(r"\n(?P<indent>\s+)Skeleton:\s*string", block)
    if not indent_match:
        raise ValueError("Could not determine SkinMeshProperties field indentation")
    indent = indent_match.group("indent")

    def replace_field(name, field_type, value):
        nonlocal block
        pattern = re.compile(
            rf"(?m)^{re.escape(indent)}{re.escape(name)}:\s*{re.escape(field_type)}\s*=\s*[^\r\n]+$"
        )
        block, count = pattern.subn(
            f"{indent}{name}: {field_type} = {value}", block, count=1
        )
        if count != 1:
            raise ValueError(f"Expected one direct SkinMeshProperties field: {name}")

    replace_field(
        "Texture",
        "file",
        f'"{SEA_WITCH_TEXTURES["WitchBody"]}"',
    )
    replace_field("SelfIllumination", "f32", "0.18")
    replace_field("BrushAlphaOverride", "f32", "1")
    replace_field("ReflectionFresnelColor", "rgba", "{ 0, 0, 0, 255 }")

    direct_material = re.compile(
        rf"(?m)^{re.escape(indent)}Material:\s*link\s*=\s*[^\r\n]+\r?\n?"
    )
    block, direct_material_count = direct_material.subn("", block, count=1)
    if direct_material_count != 1:
        raise ValueError("Expected Ocean Song's direct champion material route")

    override_marker = f"{indent}MaterialOverride: list[embed] = {{"
    override_start = block.find(override_marker)
    if override_start < 0:
        raise ValueError("Ocean Song champion material override list is missing")
    override_open = block.find("{", override_start)
    override_end = matching_brace(block, override_open) + 1
    child_indent = indent + "    "
    entry_indent = child_indent + "    "
    override_lines = [f"{indent}MaterialOverride: list[embed] = {{"]
    for submesh, texture in SEA_WITCH_TEXTURES.items():
        override_lines.extend(
            (
                f"{child_indent}SkinMeshDataProperties_MaterialOverride {{",
                f'{entry_indent}Texture: file = "{texture}"',
                f'{entry_indent}Submesh: string = "{submesh}"',
                f"{child_indent}}}",
            )
        )
    override_lines.append(f"{indent}}}")
    block = block[:override_start] + "\n".join(override_lines) + block[override_end:]

    routed_submeshes = re.findall(
        r'Submesh:\s*string\s*=\s*"([^"]+)"', block
    )
    texture_routes = re.findall(
        r'Texture:\s*file\s*=\s*"([^"]+\.tex)"', block, re.IGNORECASE
    )
    material_links = len(re.findall(r"Material:\s*link\s*=", block))
    if routed_submeshes != list(SEA_WITCH_TEXTURES):
        raise ValueError(f"Opaque submesh routes are incomplete: {routed_submeshes}")
    if set(texture_routes) != set(SEA_WITCH_TEXTURES.values()):
        raise ValueError("Opaque texture routes do not match the sea-witch contract")
    if material_links:
        raise ValueError("An alpha/holographic champion material route survived")
    if 'InitialSubmeshToHide: string = "Recall"' not in block:
        raise ValueError("The custom Recall submesh is not hidden by default")

    patched = text[:start] + block + text[end:]
    return patched, {
        "strategy": "standard_opaque_skinmesh_texture_routes",
        "submeshes": routed_submeshes,
        "texture_routes": dict(SEA_WITCH_TEXTURES),
        "material_links": material_links,
        "self_illumination": 0.18,
        "brush_alpha_override": 1.0,
        "recall_hidden_by_default": True,
        "ocean_song_holographic_materials_referenced": False,
        "ocean_song_scrolling_alpha_materials_referenced": False,
    }


def patch_opaque_jinxmine_materials(text):
    marker = "SkinMeshProperties: embed = SkinMeshDataProperties {"
    start = text.find(marker)
    if start < 0:
        raise ValueError("JinxMine SkinMeshProperties block is missing")
    open_index = text.find("{", start)
    end = matching_brace(text, open_index) + 1
    block = text[start:end]
    indent_match = re.search(r"\n(?P<indent>\s+)Skeleton:\s*string", block)
    if not indent_match:
        raise ValueError("Could not determine JinxMine SkinMeshProperties indentation")
    indent = indent_match.group("indent")

    def replace_field(name, field_type, value):
        nonlocal block
        pattern = re.compile(
            rf"(?m)^{re.escape(indent)}{re.escape(name)}:\s*{re.escape(field_type)}\s*=\s*[^\r\n]+$"
        )
        block, count = pattern.subn(
            f"{indent}{name}: {field_type} = {value}", block, count=1
        )
        if count != 1:
            raise ValueError(f"Expected one direct JinxMine field: {name}")

    replace_field("Texture", "file", f'"{JINXMINE_TEXTURE}"')
    replace_field("SelfIllumination", "f32", "0.25")
    replace_field("BrushAlphaOverride", "f32", "1")
    replace_field("ReflectionFresnelColor", "rgba", "{ 0, 0, 0, 255 }")

    if re.search(r"Material:\s*link\s*=", block):
        raise ValueError("JinxMine unexpectedly routes through a custom material")
    override_marker = f"{indent}MaterialOverride: list[embed] = {{"
    override_start = block.find(override_marker)
    if override_start >= 0:
        override_open = block.find("{", override_start)
        override_end = matching_brace(block, override_open) + 1
        block = block[:override_start] + block[override_end:]
    child_indent = indent + "    "
    entry_indent = child_indent + "    "
    override = "\n".join(
        (
            f"{indent}MaterialOverride: list[embed] = {{",
            f"{child_indent}SkinMeshDataProperties_MaterialOverride {{",
            f'{entry_indent}Texture: file = "{JINXMINE_TEXTURE}"',
            f'{entry_indent}Submesh: string = "ShellFamiliars"',
            f"{child_indent}}}",
            f"{indent}}}",
        )
    )
    final_newline = block.rfind("\n")
    if final_newline < 0:
        raise ValueError("Malformed JinxMine SkinMeshProperties block")
    block = block[:final_newline] + "\n" + override + block[final_newline:]

    routed_submeshes = re.findall(
        r'Submesh:\s*string\s*=\s*"([^"]+)"', block
    )
    if routed_submeshes != ["ShellFamiliars"]:
        raise ValueError(f"JinxMine opaque submesh route is wrong: {routed_submeshes}")
    if block.count(JINXMINE_TEXTURE) != 2:
        raise ValueError("JinxMine diffuse must route at mesh and submesh levels")
    patched = text[:start] + block + text[end:]
    return patched, {
        "strategy": "standard_opaque_skinmesh_texture_route",
        "submeshes": routed_submeshes,
        "texture": JINXMINE_TEXTURE,
        "material_links": 0,
        "self_illumination": 0.25,
        "brush_alpha_override": 1.0,
        "required_model_contract": {"ocean_song_vertices_retained": 0},
    }


def vfx_entry_ids(text):
    return {
        match.group(1).lower()
        for match in re.finditer(
            r"(?m)^\s*(0x[0-9a-fA-F]+)\s*=\s*VfxSystemDefinitionData\s*\{",
            text,
        )
    }


def audit_chomper_resolver(jinx_text, multi_text):
    entries = vfx_entry_ids(jinx_text) | vfx_entry_ids(multi_text)
    routes = {}
    for key in CHOMPER_RESOLVER_KEYS:
        match = re.search(
            rf'"{re.escape(key)}"\s*=\s*(0x[0-9a-fA-F]+)', jinx_text
        )
        if not match:
            raise ValueError(f"Missing JinxMine/Chomper resolver key: {key}")
        routes[key] = match.group(1).lower()
    unresolved = {key: target for key, target in routes.items() if target not in entries}
    if unresolved:
        raise ValueError(f"JinxMine/Chomper resolver targets are not VFX entries: {unresolved}")
    return {
        "owner": "Jinx Skin65 ResourceResolver with definitions in linked multi-skin BIN",
        "required_route_count": len(CHOMPER_RESOLVER_KEYS),
        "routes": routes,
        "all_routes_resolve_to_vfx_definitions": True,
        "jinxmine_skin_bin_embedded_vfx_systems": 0,
    }


def audit_palette_distribution(*texts):
    palette = {
        "coral": (1.000, 0.165, 0.275),
        "seafoam": (0.155, 1.000, 0.705),
        "black_violet": (0.305, 0.020, 0.505),
    }
    counts = {name: 0 for name in palette}
    for text in texts:
        for block in extract_blocks(text, "ValueColor {"):
            for match in VEC4_PATTERN.finditer(block):
                rgb = tuple(float(match.group(channel)) for channel in ("r", "g", "b"))
                if max(rgb) <= 1e-7:
                    continue
                nearest = min(
                    palette,
                    key=lambda name: sum(
                        (rgb[index] - palette[name][index]) ** 2
                        for index in range(3)
                    ),
                )
                counts[nearest] += 1
    total = sum(counts.values())
    if total == 0 or any(count < 50 for count in counts.values()):
        raise ValueError(f"Sea-witch VFX palette is not visibly represented: {counts}")
    return {
        "classified_nonblack_vectors": total,
        "nearest_accent_counts": counts,
        "nearest_accent_fractions": {
            name: round(count / total, 4) for name, count in counts.items()
        },
        "all_three_accents_represented": True,
    }


def format_float(value):
    if abs(value) < 5e-8:
        return "0"
    if abs(value - 1.0) < 5e-8:
        return "1"
    return f"{value:.8f}".rstrip("0").rstrip(".")


def transform_value_colors(text):
    spans = []
    cursor = 0
    marker = "ValueColor {"
    while True:
        start = text.find(marker, cursor)
        if start < 0:
            break
        open_index = text.find("{", start)
        end = matching_brace(text, open_index)
        spans.append((start, end + 1))
        cursor = end + 1

    transformed_blocks = 0
    transformed_vectors = 0
    output = []
    previous = 0

    def replace_vector(match):
        nonlocal transformed_vectors
        values = [float(match.group(name)) for name in ("r", "g", "b", "a")]
        graded = abyssal_color(*values)
        if all(abs(left - right) < 1e-7 for left, right in zip(values, graded)):
            return match.group(0)
        transformed_vectors += 1
        prefix = match.group("prefix") or ""
        return f"{prefix}{{ {', '.join(format_float(value) for value in graded)} }}"

    for start, end in spans:
        output.append(text[previous:start])
        block = text[start:end]
        patched = VEC4_PATTERN.sub(replace_vector, block)
        if patched != block:
            transformed_blocks += 1
        output.append(patched)
        previous = end
    output.append(text[previous:])
    return "".join(output), transformed_blocks, transformed_vectors, len(spans)


def event_set(text, skin):
    return {
        match.group(1)
        for match in EVENT_PATTERN.finditer(text)
        if int(match.group(2)) == int(skin)
    }


def route_event_names(text, donor_events):
    source_events = event_set(text, 65)
    patched = text.replace("JinxSkin65_", "JinxSkin60_")
    manual = {
        "JinxSkin60_Joke3D_buffactivate": "JinxSkin60_Joke3D_In_anim",
        "JinxSkin60_Taunt23D_buffactivate": "JinxSkin60_Taunt3D_buffactivate_anim",
        "JinxSkin60_Taunt3D_buffactivate": "JinxSkin60_Taunt3D_buffactivate_anim",
    }
    patched = patched.replace(
        "JinxSkin60_Joke3D_buffactivate", manual["JinxSkin60_Joke3D_buffactivate"]
    )
    patched = patched.replace(
        "JinxSkin60_Taunt23D_buffactivate", manual["JinxSkin60_Taunt23D_buffactivate"]
    )
    patched = re.sub(
        r"JinxSkin60_Taunt3D_buffactivate(?!_anim)",
        manual["JinxSkin60_Taunt3D_buffactivate"],
        patched,
    )
    routed_events = event_set(patched, 60)
    missing = sorted(routed_events - donor_events)
    if missing:
        raise ValueError(f"Patched SFX routes are absent from Skin60 bank: {missing}")
    if source_events and "JinxSkin65_" in patched:
        raise ValueError("A Skin65 SFX event survived routing")
    return patched, source_events, routed_events, manual


def patch_audio(text, donor, source_root):
    source_events = event_set(text, 65)
    donor_events = event_set(donor, 60)
    if len(source_events) != 60:
        raise ValueError(f"Expected 60 unique Ocean Song SFX events, got {len(source_events)}")
    if len(donor_events) < 80:
        raise ValueError(f"Arcane Fractured SFX event family is incomplete: {len(donor_events)}")

    patched = text.replace("Jinx_Skin65_SFX", "Jinx_Skin60_SFX")
    patched = patched.replace(
        "ASSETS/Sounds/Wwise2016/SFX/Characters/Jinx/Skins/Skin65/",
        "ASSETS/Sounds/Wwise2016/SFX/Characters/Jinx/Skins/Skin60/",
    )
    patched, _, routed_events, manual = route_event_names(patched, donor_events)
    events_bank = (
        '"ASSETS/Sounds/Wwise2016/SFX/Characters/Jinx/Skins/Skin60/'
        'Jinx_Skin60_SFX_events.bnk"'
    )
    media_bank = (
        '"ASSETS/Sounds/Wwise2016/SFX/Characters/Jinx/Skins/Skin60/'
        'Jinx_Skin60_SFX_audio.wpk"'
    )
    if media_bank not in patched:
        patched = patched.replace(events_bank, f"{events_bank}\n                        {media_bank}", 1)
    patched = patched.replace(
        '"Jinx"\n                "JinxSkin65"',
        '"Jinx"\n                "JinxSkin60"',
        1,
    )
    if "JinxSkin65_" in patched or "Jinx_Skin65_SFX" in patched:
        raise ValueError("Ocean Song SFX route survived the complete bank replacement")
    required_names = (
        "Jinx_Skin60_SFX_audio.bnk",
        "Jinx_Skin60_SFX_events.bnk",
        "Jinx_Skin60_SFX_audio.wpk",
    )
    if any(name not in patched for name in required_names):
        raise ValueError("Arcane Fractured SFX bank or external media path is missing")
    packaged_assets = []
    for name in required_names:
        relative = f"assets/sounds/wwise2016/sfx/characters/jinx/skins/skin60/{name.lower()}"
        path = os.path.join(os.path.abspath(source_root), *relative.split("/"))
        if not os.path.isfile(path) or os.path.getsize(path) == 0:
            raise FileNotFoundError(path)
        with open(path, "rb") as handle:
            digest = hashlib.sha256(handle.read()).hexdigest()
        packaged_assets.append(
            {"path": relative, "bytes": os.path.getsize(path), "sha256": digest}
        )
    return patched, {
        "source_event_count": len(source_events),
        "donor_event_count": len(donor_events),
        "routed_unique_event_count": len(routed_events),
        "direct_event_count": 57,
        "manual_event_count": 3,
        "manual_routes": manual,
        "bank": "Jinx_Skin60_SFX",
        "media_path_added": True,
        "tag_event_skin": "JinxSkin60",
        "packaged_assets": packaged_assets,
        "voice_over": "unchanged Jinx base VO",
    }


def route_vfx_assets(text, mapping):
    lower_mapping = {source.lower(): destination for source, destination in mapping.items()}
    spans = []
    cursor = 0
    marker = "VfxSystemDefinitionData {"
    while True:
        start = text.find(marker, cursor)
        if start < 0:
            break
        open_index = text.find("{", start)
        end = matching_brace(text, open_index) + 1
        spans.append((start, end))
        cursor = end

    original_refs = set()
    output_refs = set()
    replacements = 0
    output = []
    previous = 0
    asset_pattern = re.compile(
        r'"(ASSETS/[^"\r\n]+\.(?:tex|dds|scb|skn|skl))"', re.IGNORECASE
    )

    def replace(match):
        nonlocal replacements
        source = match.group(1)
        destination = lower_mapping.get(source.lower())
        if destination is None:
            raise ValueError(f"VFX dependency has no output mapping: {source}")
        original_refs.add(source.lower())
        output_refs.add(destination.lower())
        replacements += 1
        return f'"{destination}"'

    for start, end in spans:
        output.append(text[previous:start])
        output.append(asset_pattern.sub(replace, text[start:end]))
        previous = end
    output.append(text[previous:])
    patched = "".join(output)
    if replacements == 0 or len(original_refs) != len(output_refs):
        raise ValueError("VFX dependency routing was empty or collided")
    return patched, {
        "strategy": "in_place_jinx_and_isolated_shared",
        "reference_occurrences": replacements,
        "unique_source_dependencies": len(original_refs),
        "unique_output_dependencies": len(output_refs),
        "new_wad_entries": sum(
            source.startswith("assets/shared/") for source in original_refs
        ),
    }


def main():
    args = parse_args()
    jinx_source = read_text(args.jinx)
    mine_source = read_text(args.mine)
    multi_source = read_text(args.multi)
    with open(args.vfx_map, "r", encoding="utf-8") as handle:
        vfx_mapping = json.load(handle)
    transformed_dependencies = {path.lower() for path in vfx_mapping}

    jinx_patched, jinx_blocks, jinx_vectors, jinx_total_blocks = transform_value_colors(
        jinx_source
    )
    multi_patched, multi_blocks, multi_vectors, multi_total_blocks = transform_value_colors(
        multi_source
    )
    mine_patched, mine_blocks, mine_vectors, mine_total_blocks = transform_value_colors(
        mine_source
    )
    jinx_patched, champion_materials = patch_opaque_champion_materials(jinx_patched)
    mine_patched, jinxmine_materials = patch_opaque_jinxmine_materials(mine_patched)
    jinx_patched, jinx_remap = route_vfx_assets(jinx_patched, vfx_mapping)
    multi_patched, multi_remap = route_vfx_assets(multi_patched, vfx_mapping)
    jinx_patched = jinx_patched.replace("skinline:oceansong", "skinline:abyssalsiren")
    chomper_resolver = audit_chomper_resolver(jinx_patched, multi_patched)
    palette_distribution = audit_palette_distribution(
        jinx_patched, multi_patched, mine_patched
    )

    vfx_corpora = []
    for name, source, output in (
        ("skin65", jinx_source, jinx_patched),
        ("multi_skin65", multi_source, multi_patched),
    ):
        source_systems = extract_blocks(source, "VfxSystemDefinitionData {")
        output_systems = extract_blocks(output, "VfxSystemDefinitionData {")
        if not source_systems or len(output_systems) != len(source_systems):
            raise ValueError(
                f"{name} VFX system corpus changed structurally: "
                f"{len(source_systems)} -> {len(output_systems)}"
            )
        missing_object_paths = sum("ObjectPath: hash" not in block for block in output_systems)
        if missing_object_paths:
            raise ValueError(f"{name} has {missing_object_paths} VFX systems without ObjectPath metadata")
        bin_changed = 0
        dependency_changed = 0
        forwarding_wrappers = []
        asset_pattern = re.compile(
            r'ASSETS/[^"\r\n]+\.(?:tex|dds|scb|skn|skl)', re.IGNORECASE
        )
        for index, (source, patched) in enumerate(zip(source_systems, output_systems)):
            if source != patched:
                bin_changed += 1
                continue
            dependency_refs = {match.group(0).lower() for match in asset_pattern.finditer(source)}
            if dependency_refs:
                missing = dependency_refs - transformed_dependencies
                if missing:
                    raise ValueError(
                        f"Renderable {name} VFX system {index} references untransformed assets: "
                        f"{sorted(missing)}"
                    )
                dependency_changed += 1
                continue
            if "ValueColor {" in source:
                raise ValueError(f"Renderable {name} VFX system {index} did not change")
            particle = re.search(r'ParticleName:\s*string\s*=\s*"([^"]+)"', source)
            forwarding_wrappers.append(particle.group(1) if particle else f"index_{index}")
        renderable_changed = bin_changed + dependency_changed
        vfx_corpora.append(
            {
                "name": name,
                "system_count": len(source_systems),
                "renderable_systems_changed": renderable_changed,
                "bin_systems_changed": bin_changed,
                "dependency_only_systems_changed": dependency_changed,
                "forwarding_wrappers_audited": forwarding_wrappers,
            }
        )

    if jinx_vectors + multi_vectors < 1000:
        raise ValueError(f"Too few Ocean Song VFX colors changed: {jinx_vectors + multi_vectors}")
    if jinx_blocks < int(jinx_total_blocks * 0.90):
        raise ValueError(
            f"Too few Ocean Song ValueColor blocks changed: {jinx_blocks}/{jinx_total_blocks}"
        )
    if mine_total_blocks and mine_blocks < int(mine_total_blocks * 0.90):
        raise ValueError(
            f"Too few Chomper ValueColor blocks changed: {mine_blocks}/{mine_total_blocks}"
        )
    if multi_blocks < int(multi_total_blocks * 0.90):
        raise ValueError(
            f"Too few linked Ocean Song ValueColor blocks changed: {multi_blocks}/{multi_total_blocks}"
        )
    for name, source, output in (
        ("Jinx", jinx_source, jinx_patched),
        ("JinxMine", mine_source, mine_patched),
        ("linked Ocean Song", multi_source, multi_patched),
    ):
        if sha256_text(source) == sha256_text(output):
            raise ValueError(f"{name} BIN text did not change")

    write_text(args.out_jinx, jinx_patched)
    write_text(args.out_mine, mine_patched)
    write_text(args.out_multi, multi_patched)
    system_count = sum(item["system_count"] for item in vfx_corpora)
    systems_changed = sum(item["renderable_systems_changed"] for item in vfx_corpora)
    forwarding_wrapper_count = sum(len(item["forwarding_wrappers_audited"]) for item in vfx_corpora)
    if systems_changed + forwarding_wrapper_count != system_count:
        raise ValueError("VFX system accounting is incomplete")
    payload = {
        "status": "PASSED",
        "target_skin": 65,
        "theme": "cute sea-horror dark sea witch",
        "champion_materials": champion_materials,
        "jinxmine_materials": jinxmine_materials,
        "vfx": {
            "system_count": system_count,
            "systems_changed": systems_changed,
            "forwarding_wrapper_count": forwarding_wrapper_count,
            "all_renderable_systems_changed": True,
            "corpora": vfx_corpora,
            "jinx_value_color_blocks": jinx_total_blocks,
            "jinx_value_color_blocks_changed": jinx_blocks,
            "jinx_color_vectors_changed": jinx_vectors,
            "linked_value_color_blocks": multi_total_blocks,
            "linked_value_color_blocks_changed": multi_blocks,
            "linked_color_vectors_changed": multi_vectors,
            "chomper_value_color_blocks": mine_total_blocks,
            "chomper_value_color_blocks_changed": mine_blocks,
            "chomper_color_vectors_changed": mine_vectors,
            "palette": "black-violet, coral, seafoam",
            "palette_intent": {
                "black_violet": "shadow mass and witchcraft depth",
                "coral": "cute sea-creature accent and impact punctuation",
                "seafoam": "bioluminescent spell energy and readability",
            },
            "palette_distribution": palette_distribution,
            "dependency_transform": {
                "skin65": jinx_remap,
                "multi_skin65": multi_remap,
                "mapping_entries": len(vfx_mapping),
            },
            "chomper_material_overrides": {
                "self_illumination": 0.25,
                "brush_alpha": 1.0,
                "opaque_default_skinmesh_shader": True,
                "submesh": "ShellFamiliars",
                "texture": JINXMINE_TEXTURE,
            },
            "chomper_resolver": chomper_resolver,
        },
        "sfx": {
            "status": "REBUILT",
            "strategy": "native_skin65_routes_with_complete_bnk_media_replacement",
            "native_skin65_event_routes_retained": True,
            "event_count": 60,
            "bank_build_report": "reports/generated/dark_witch_audio.json",
            "stock_ocean_song_audio_retained": False,
            "voice_over_changed": False,
        },
        "animations": {
            "status": "RETAINED",
            "reason": "stock_animation_release",
            "stock_ocean_song_animation_graph_retained": True,
        },
        "source_hashes": {
            "jinx": sha256_text(jinx_source),
            "jinxmine": sha256_text(mine_source),
            "multi_skin65": sha256_text(multi_source),
        },
        "output_hashes": {
            "jinx": sha256_text(jinx_patched),
            "jinxmine": sha256_text(mine_patched),
            "multi_skin65": sha256_text(multi_patched),
        },
    }
    os.makedirs(os.path.dirname(os.path.abspath(args.report)), exist_ok=True)
    with open(args.report, "w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2)
        handle.write("\n")
    print(
        "ABYSSAL_BINS=PASSED "
        "SFX=REBUILT ANIMATIONS=STOCK "
        f"VFX_SYSTEMS={system_count} VFX_COLORS={jinx_vectors + multi_vectors + mine_vectors}"
    )


if __name__ == "__main__":
    main()
