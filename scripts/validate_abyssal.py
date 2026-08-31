import argparse
import hashlib
import json
import os
import re
import struct

from tex_layout import validate_tex_layout


SEMVER = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")
VERSION = "3.0.0"
CHAMPION_SUBMESHES = (
    "WitchBody",
    "CoralArmor",
    "PowPow",
    "Fishbones",
    "Zapper",
    "Recall",
)
CHOMPER_SUBMESHES = ("ShellFamiliars",)
MISSILE_SUBMESHES = ("LeviathanBolt",)
TEXTURE_ROUTES = {
    "body": "assets/characters/jinx/skins/skin65/jinx_skin65_seawitch_body_tx_cm.tex",
    "armor": "assets/characters/jinx/skins/skin65/jinx_skin65_seawitch_armor_tx_cm.tex",
    "weapon": "assets/characters/jinx/skins/skin65/jinx_skin65_seawitch_weapon_tx_cm.tex",
    "recall": "assets/characters/jinx/skins/skin65/jinx_skin65_seawitch_recall_tx_cm.tex",
    "mine": "assets/characters/jinxmine/skins/skin65/jinxmine_skin65_tx_cm.tex",
    "missile": "assets/characters/jinx/skins/skin65/particles/jinx_skin65_r_mis_globefish.tex",
}
NEW_TEXTURE_ROUTES = {
    TEXTURE_ROUTES[role] for role in ("body", "armor", "weapon", "recall")
}
AUDIO_FILES = {
    "audio": "assets/sounds/wwise2016/sfx/characters/jinx/skins/skin65/jinx_skin65_sfx_audio.bnk",
    "events": "assets/sounds/wwise2016/sfx/characters/jinx/skins/skin65/jinx_skin65_sfx_events.bnk",
}
CORE_FILES = {
    "assets/characters/jinx/skins/skin65/jinx_skin65.skn",
    "assets/characters/jinx/skins/skin65/jinx_skin65.skl",
    "assets/characters/jinx/skins/skin65/particles/jinx_skin65_r_mis_globefish_01_1.skn",
    "assets/characters/jinx/skins/skin65/particles/jinx_skin65_r_mis_globefish_01_1.skl",
    "assets/characters/jinxmine/skins/skin65/jinxmine_skin65.skn",
    "assets/characters/jinxmine/skins/skin65/jinxmine_skin65.skl",
    "data/characters/jinx/skins/skin65.bin",
    "data/characters/jinx/jinx_multi_skins_skin65_skins_skin66_skins_skin67_skins_skin68_skins_skin69_skins_skin70_skins_skin71_skins_skin72_skins_skin73.bin",
    "data/characters/jinxmine/skins/skin65.bin",
}


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", required=True)
    parser.add_argument("--package", required=True)
    parser.add_argument("--package-extract", required=True)
    parser.add_argument("--overlay", required=True)
    parser.add_argument("--stock-wad", required=True)
    parser.add_argument("--overlay-wad", required=True)
    parser.add_argument("--out", required=True)
    return parser.parse_args()


def sha256_file(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def normalized(path):
    return path.replace("\\", "/").lower()


def collect_files(root):
    result = {}
    for directory, _, filenames in os.walk(root):
        for filename in filenames:
            path = os.path.join(directory, filename)
            result[normalized(os.path.relpath(path, root))] = {
                "size": os.path.getsize(path),
                "sha256": sha256_file(path),
                "absolute_path": os.path.abspath(path),
            }
    return result


def load_json(path):
    with open(path, "r", encoding="utf-8-sig") as handle:
        return json.load(handle)


def overlay_routes(path):
    routes = set()
    with open(path, "r", encoding="utf-8-sig") as handle:
        for raw_line in handle:
            line = raw_line.strip()
            if not line.startswith("BUILT_WAD="):
                continue
            route = normalized(line.removeprefix("BUILT_WAD="))
            marker = "/overlay/"
            if marker not in route:
                raise ValueError(f"Overlay route lacks overlay root: {line}")
            routes.add(route.split(marker, 1)[1])
    if not routes:
        raise ValueError(f"Overlay route report is empty: {path}")
    return routes


def wad_chunk_inventory(path):
    with open(path, "rb") as handle:
        header = handle.read(272)
    if len(header) < 272 or header[:2] != b"RW" or header[2] != 3:
        raise ValueError(f"Invalid WAD v3 header: {path}")
    count = struct.unpack_from("<i", header, 268)[0]
    if count <= 0:
        raise ValueError(f"Invalid WAD chunk count {count}: {path}")
    with open(path, "rb") as handle:
        handle.seek(272)
        toc = handle.read(count * 32)
    if len(toc) != count * 32:
        raise ValueError(f"Truncated WAD chunk table: {path}")
    hashes = {struct.unpack_from("<Q", toc, index * 32)[0] for index in range(count)}
    if len(hashes) != count:
        raise ValueError(f"Duplicate WAD chunk hashes: {path}")
    return count, hashes


def skn_submeshes(path):
    data = open(path, "rb").read()
    if len(data) < 12 or struct.unpack_from("<I", data, 0)[0] != 0x00112233:
        raise ValueError(f"Invalid SKN signature: {path}")
    major, minor, count = struct.unpack_from("<HHI", data, 4)
    if major != 4 or count <= 0:
        raise ValueError(f"Unexpected SKN layout {major}.{minor} with {count} submeshes: {path}")
    offset = 12
    names = []
    for _ in range(count):
        if offset + 80 > len(data):
            raise ValueError(f"Truncated SKN submesh table: {path}")
        names.append(data[offset : offset + 64].split(b"\0", 1)[0].decode("ascii"))
        offset += 80
    return tuple(names)


def require_report_version(name, report):
    if report.get("version", report.get("project_version")) != VERSION:
        raise ValueError(f"{name} report is not version {VERSION}")


def require_hash(path, expected, label):
    actual = sha256_file(path)
    if actual != expected:
        raise ValueError(f"{label} hash mismatch: expected={expected} actual={actual}")


def require_render(item, label):
    path = item.get("path")
    if not path or not os.path.isfile(path):
        raise FileNotFoundError(f"Missing {label} render: {path}")
    require_hash(path, item.get("sha256"), f"{label} render")


def validate_payload(project_root, package_extract, overlay_extract, expected):
    stage_root = os.path.join(
        project_root, "variants", "base", "content", "base", "Jinx.wad.client"
    )
    package_root = os.path.join(package_extract, "base", "jinx.wad.client")
    stage = collect_files(stage_root)
    package = collect_files(package_root)
    overlay = collect_files(overlay_extract)
    for name, inventory in (("stage", stage), ("package", package)):
        if set(inventory) != expected:
            raise ValueError(
                f"{name} allowlist mismatch: missing={sorted(expected - set(inventory))} "
                f"extra={sorted(set(inventory) - expected)}"
            )
    if not expected.issubset(overlay):
        raise ValueError(f"Overlay is missing expected files: {sorted(expected - set(overlay))}")
    tex_count = 0
    for path in sorted(expected):
        hashes = {stage[path]["sha256"], package[path]["sha256"], overlay[path]["sha256"]}
        if len(hashes) != 1:
            raise ValueError(f"Content/package/overlay hash mismatch for {path}")
        if path.endswith(".tex"):
            tex_count += 1
            layouts = [
                validate_tex_layout(stage[path]["absolute_path"]),
                validate_tex_layout(package[path]["absolute_path"]),
                validate_tex_layout(overlay[path]["absolute_path"]),
            ]
            if len({(item["format_code"], item["bytes"]) for item in layouts}) != 1:
                raise ValueError(f"TEX layout mismatch for {path}")
    return {
        "status": "PASSED",
        "files": len(expected),
        "overlay_files_inspected": len(overlay),
        "content_package_overlay_hashes_match": True,
        "tex_layouts_validated": tex_count,
    }


def main():
    args = parse_args()
    project_root = os.path.abspath(args.project_root)
    reports_root = os.path.join(project_root, "reports", "generated")
    models = load_json(os.path.join(reports_root, "abyssal_models.json"))
    textures = load_json(os.path.join(reports_root, "abyssal_textures.json"))
    vfx_assets = load_json(os.path.join(reports_root, "abyssal_vfx_assets.json"))
    bins = load_json(os.path.join(reports_root, "abyssal_bins.json"))
    visual = load_json(os.path.join(reports_root, "abyssal_visual_qa.json"))
    audio = load_json(os.path.join(reports_root, "dark_witch_audio.json"))

    for name, report in (
        ("models", models),
        ("textures", textures),
        ("vfx_assets", vfx_assets),
        ("bins", bins),
        ("visual", visual),
        ("audio", audio),
    ):
        if report.get("status") != "PASSED":
            raise ValueError(f"{name} report did not pass")
        if name in {"models", "textures", "visual", "audio"}:
            require_report_version(name, report)

    stage_root = os.path.join(
        project_root, "variants", "base", "content", "base", "Jinx.wad.client"
    )
    champion = models["champion"]
    chompers = models["chompers"]
    missile = models["ultimate_missile"]
    invariants = models["invariants"]
    required_model_invariants = {
        "ocean_song_champion_geometry_retained": False,
        "ocean_song_chompers_geometry_retained": False,
        "ocean_song_missile_geometry_retained": False,
        "native_champion_skeleton_byte_identical": True,
        "native_chompers_skeleton_byte_identical": True,
        "joint_order_unchanged": True,
        "new_skeleton_joints_added": 0,
        "uint16_indices_valid": True,
    }
    for key, expected in required_model_invariants.items():
        if invariants.get(key) != expected:
            raise ValueError(f"Model invariant failed: {key}={invariants.get(key)!r}")
    for label, model in (
        ("champion", champion),
        ("chompers", chompers),
        ("ultimate missile", missile),
    ):
        if model.get("target_ocean_song_vertices_retained") != 0:
            raise ValueError(f"{label} retains Ocean Song geometry")

    reported_submeshes = tuple(item["name"] for item in champion["submeshes"])
    if reported_submeshes != CHAMPION_SUBMESHES:
        raise ValueError(f"Champion report submeshes drifted: {reported_submeshes}")
    model_paths = {
        "champion": "assets/characters/jinx/skins/skin65/jinx_skin65.skn",
        "chompers": "assets/characters/jinxmine/skins/skin65/jinxmine_skin65.skn",
        "ultimate missile": "assets/characters/jinx/skins/skin65/particles/jinx_skin65_r_mis_globefish_01_1.skn",
    }
    expected_submeshes = {
        "champion": CHAMPION_SUBMESHES,
        "chompers": CHOMPER_SUBMESHES,
        "ultimate missile": MISSILE_SUBMESHES,
    }
    model_reports = {
        "champion": champion,
        "chompers": chompers,
        "ultimate missile": missile,
    }
    for label, relative in model_paths.items():
        path = os.path.join(stage_root, *relative.split("/"))
        if skn_submeshes(path) != expected_submeshes[label]:
            raise ValueError(f"Unexpected {label} SKN submeshes: {skn_submeshes(path)}")
        require_hash(path, model_reports[label]["sha256"], f"{label} SKN")

    for label, model, relative in (
        (
            "champion",
            champion,
            "assets/characters/jinx/skins/skin65/jinx_skin65.skl",
        ),
        (
            "chompers",
            chompers,
            "assets/characters/jinxmine/skins/skin65/jinxmine_skin65.skl",
        ),
    ):
        if model["skeleton_sha256"] != model["target_skeleton_sha256"]:
            raise ValueError(f"{label} native skin65 skeleton bytes changed")
        require_hash(
            os.path.join(stage_root, *relative.split("/")),
            model["target_skeleton_sha256"],
            f"{label} native skin65 skeleton",
        )

    if not textures.get("opaque_material_atlases") or len(textures.get("textures", [])) != 6:
        raise ValueError("Expected exactly six opaque sea-witch atlases")
    texture_by_role = {item["role"]: item for item in textures["textures"]}
    if set(texture_by_role) != set(TEXTURE_ROUTES):
        raise ValueError(f"Texture role inventory drifted: {sorted(texture_by_role)}")
    for role, expected_path in TEXTURE_ROUTES.items():
        item = texture_by_role[role]
        if normalized(item["output"]) != expected_path:
            raise ValueError(f"{role} texture route drifted: {item['output']}")
        if item["source_sha256"] == item["output_sha256"]:
            raise ValueError(f"{role} texture is unchanged from its source")
        if item["changed_pixels"] < item["total_pixels"] * 0.95:
            raise ValueError(f"{role} texture change is not substantial")
        if item["decoded_metrics"]["opaque_pixels"] != item["total_pixels"]:
            raise ValueError(f"{role} texture is not fully opaque after compression")
        require_hash(
            os.path.join(stage_root, *expected_path.split("/")),
            item["output_sha256"],
            f"{role} texture",
        )

    champion_materials = bins.get("champion_materials", {})
    expected_material_routes = {
        "WitchBody": TEXTURE_ROUTES["body"],
        "CoralArmor": TEXTURE_ROUTES["armor"],
        "PowPow": TEXTURE_ROUTES["weapon"],
        "Fishbones": TEXTURE_ROUTES["weapon"],
        "Zapper": TEXTURE_ROUTES["weapon"],
        "Recall": TEXTURE_ROUTES["recall"],
    }
    actual_material_routes = {
        name: normalized(path)
        for name, path in champion_materials.get("texture_routes", {}).items()
    }
    if tuple(champion_materials.get("submeshes", [])) != CHAMPION_SUBMESHES:
        raise ValueError("Champion opaque material submesh inventory drifted")
    if actual_material_routes != expected_material_routes:
        raise ValueError(f"Champion texture routes drifted: {actual_material_routes}")
    if (
        champion_materials.get("strategy") != "standard_opaque_skinmesh_texture_routes"
        or champion_materials.get("material_links") != 0
        or champion_materials.get("brush_alpha_override") != 1.0
        or not champion_materials.get("recall_hidden_by_default")
        or champion_materials.get("ocean_song_holographic_materials_referenced")
        or champion_materials.get("ocean_song_scrolling_alpha_materials_referenced")
    ):
        raise ValueError("Champion material routing is not opaque and square-safe")
    mine_materials = bins.get("jinxmine_materials", {})
    if (
        tuple(mine_materials.get("submeshes", [])) != CHOMPER_SUBMESHES
        or normalized(mine_materials.get("texture", "")) != TEXTURE_ROUTES["mine"]
        or mine_materials.get("material_links") != 0
        or mine_materials.get("brush_alpha_override") != 1.0
        or mine_materials.get("required_model_contract", {}).get(
            "ocean_song_vertices_retained"
        )
        != 0
    ):
        raise ValueError("Chompers material route is not the opaque ShellFamiliars route")

    if not vfx_assets.get("all_dependencies_routed"):
        raise ValueError("Not every VFX dependency was routed")
    if not vfx_assets.get("square_safe_texture_recolor"):
        raise ValueError("Particle-card background preservation failed")
    if vfx_assets.get("vfx_systems") != 117:
        raise ValueError("Expected exactly 117 Ocean Song-slot VFX systems")
    if vfx_assets.get("particle_card_textures_audited") != 319:
        raise ValueError("Expected 319 byte-preserved particle-card TEX assets")
    for key in (
        "particle_textures_byte_identical",
        "particle_texture_sizes_preserved",
        "particle_texture_headers_preserved",
    ):
        if not vfx_assets.get(key):
            raise ValueError(f"Particle-card preservation failed: {key}")
    if vfx_assets.get("unique_dependencies", 0) < 300:
        raise ValueError("VFX dependency corpus is incomplete")
    shared_dependencies = sum(
        normalized(item.get("source", "")).startswith("assets/shared/")
        for item in vfx_assets.get("assets", [])
    )
    if shared_dependencies != 14 or vfx_assets.get("isolated_shared_dependencies") != 14:
        raise ValueError("Shared VFX dependency isolation inventory drifted")
    if vfx_assets.get("new_wad_entries") != shared_dependencies:
        raise ValueError("Only isolated shared VFX dependencies may add WAD chunks")
    for asset in vfx_assets.get("assets", []):
        source = normalized(asset.get("source", ""))
        destination = normalized(asset.get("destination", ""))
        if source.startswith("assets/shared/") and "/abyssal/vfx/" not in destination:
            raise ValueError(f"Shared VFX dependency was not isolated: {source}")
        if not source.startswith("assets/shared/") and source != destination:
            raise ValueError(f"Jinx-local VFX dependency was not replaced in place: {source}")
        if "inactive_pixels" in asset and asset["inactive_pixels"] != asset["inactive_pixels_preserved"]:
            raise ValueError(f"VFX card background changed: {source}")
    particle_cards = [
        item for item in vfx_assets.get("assets", []) if item.get("particle_card_preserved")
    ]
    if len(particle_cards) != 319 or any(
        item["source_sha256"] != item["output_sha256"]
        or not item.get("byte_size_preserved")
        or not item.get("tex_header_preserved")
        for item in particle_cards
    ):
        raise ValueError("A particle-card TEX changed bytes, size, or native header")
    packaged_vfx_skeletons = [
        item for item in vfx_assets.get("assets", []) if item.get("extension") == ".skl"
    ]
    if not packaged_vfx_skeletons or any(
        item.get("status") != "preserved"
        or item["source_sha256"] != item["output_sha256"]
        for item in packaged_vfx_skeletons
    ):
        raise ValueError("A packaged skin65 VFX skeleton changed bytes")

    vfx = bins["vfx"]
    if vfx_assets.get("vfx_systems") != vfx.get("system_count"):
        raise ValueError("VFX asset and BIN system inventories disagree")
    if (
        vfx.get("system_count") != 117
        or vfx.get("systems_changed", 0) + vfx.get("forwarding_wrapper_count", 0) != 117
        or not vfx.get("all_renderable_systems_changed")
    ):
        raise ValueError("Not every renderable VFX system was recolored or audited")
    color_vectors = sum(
        vfx.get(key, 0)
        for key in (
            "jinx_color_vectors_changed",
            "linked_color_vectors_changed",
            "chomper_color_vectors_changed",
        )
    )
    if color_vectors != 2977:
        raise ValueError(f"Expected 2,977 recolored ValueColor vectors, found {color_vectors}")
    palette = vfx.get("palette_distribution", {})
    if palette.get("classified_nonblack_vectors") != 2977 or not palette.get(
        "all_three_accents_represented"
    ):
        raise ValueError("VFX black-violet/coral/seafoam palette coverage drifted")
    resolver = vfx.get("chomper_resolver", {})
    if (
        resolver.get("required_route_count") != 10
        or len(resolver.get("routes", {})) != 10
        or not resolver.get("all_routes_resolve_to_vfx_definitions")
    ):
        raise ValueError("Chompers VFX resolver does not cover all ten routes")
    animation_scope = bins.get("animations", {})
    if (
        animation_scope.get("status") != "RETAINED"
        or not animation_scope.get("stock_ocean_song_animation_graph_retained")
    ):
        raise ValueError("Stock-animation release unexpectedly patches the animation graph")

    target_audio = audio.get("target", {})
    expected_audio_counts = {
        "event_count": 60,
        "play_event_count": 48,
        "stop_event_count": 12,
        "media_count": 63,
        "sound_object_count": 103,
    }
    for key, expected in expected_audio_counts.items():
        if target_audio.get(key) != expected:
            raise ValueError(f"Audio {key} drifted: {target_audio.get(key)}")
    if target_audio.get("skin_slot") != 65:
        raise ValueError("Dark-witch audio is not routed to skin65")
    coverage = audio.get("coverage", {})
    for key in (
        "all_sfx_bank_media_replaced",
        "all_60_sfx_events_route_only_to_replaced_media",
        "native_wwise_vorbis_plugin_preserved",
        "every_replacement_decodes_with_vgmstream",
    ):
        if not coverage.get(key):
            raise ValueError(f"Dark-witch audio coverage failed: {key}")
    if (
        coverage.get("unique_replaced_media") != 63
        or coverage.get("patched_sound_objects") != 103
        or coverage.get("non_target_sfx_media_remaining") != 0
        or coverage.get("voice_over_changed") is not False
    ):
        raise ValueError("Dark-witch audio replacement inventory drifted")
    if (
        len(audio.get("event_routes", {})) != 60
        or len(audio.get("changed_media", [])) != 63
        or len(audio.get("decoded_replacements", [])) != 63
    ):
        raise ValueError("Dark-witch audio report cardinalities drifted")
    if any(
        item.get("wem_format", {}).get("format_tag") != "0xffff"
        or item.get("decoded_validation", {}).get("decoder_identified") != "Custom Vorbis"
        for item in audio["decoded_replacements"]
    ):
        raise ValueError("One or more replacement WEMs are not decodable Wwise Vorbis")
    if sum(audio.get("donor_usage", {}).values()) != 63:
        raise ValueError("Dark-witch donor mapping does not cover all 63 media")
    for bank, relative in AUDIO_FILES.items():
        require_hash(
            os.path.join(stage_root, *relative.split("/")),
            audio["banks"][bank]["output_sha256"],
            f"dark-witch {bank} bank",
        )

    visual_champion = visual["champion"]
    if (
        tuple(visual_champion.get("submeshes", [])) != CHAMPION_SUBMESHES
        or visual_champion.get("model_sha256") != champion["sha256"]
    ):
        raise ValueError("Visual QA did not render the exported champion SKN")
    if set(visual_champion.get("rest_views", {})) != {
        "front",
        "front_three_quarter",
        "left",
        "right",
        "back",
    }:
        raise ValueError("Five-angle champion visual QA is incomplete")
    for name, item in visual_champion["rest_views"].items():
        require_render(item, f"champion {name}")
    require_render(visual_champion["face_closeup"], "champion face/crown closeup")
    require_render(visual_champion["weapon_closeup"], "coral relic weapon closeup")
    expected_poses = {
        "stock_minigun_idle",
        "stock_rocket_idle",
        "stock_zapper_spell2",
        "stock_recall",
    }
    if set(visual_champion.get("stock_animation_poses", {})) != expected_poses:
        raise ValueError("Stock-animation pose QA inventory is incomplete")
    for name, item in visual_champion["stock_animation_poses"].items():
        if item.get("packaged"):
            raise ValueError(f"QA-only stock animation was packaged: {name}")
        require_render(item, name)
    if (
        tuple(visual["chompers"].get("submeshes", [])) != CHOMPER_SUBMESHES
        or visual["chompers"].get("model_sha256") != chompers["sha256"]
    ):
        raise ValueError("Visual QA did not render the exported ShellFamiliars SKN")
    if (
        tuple(visual["ultimate_missile"].get("submeshes", [])) != MISSILE_SUBMESHES
        or visual["ultimate_missile"].get("model_sha256") != missile["sha256"]
    ):
        raise ValueError("Visual QA did not render the exported LeviathanBolt SKN")
    require_render(visual["chompers"]["rest"], "ShellFamiliars rest")
    require_render(
        visual["chompers"]["manual_deformation_test"], "ShellFamiliars deformation"
    )
    if not visual["chompers"]["manual_deformation_test"].get(
        "manual_pose_not_packaged"
    ):
        raise ValueError("Chompers QA pose was not marked as test-only")
    require_render(visual["ultimate_missile"]["rest"], "LeviathanBolt rest")
    require_render(visual["contact_sheet"], "model contact sheet")
    if visual.get("live_game_test_completed"):
        raise ValueError("Offline validator cannot certify a live-game test")

    texture_paths = {normalized(item["output"]) for item in textures["textures"]}
    vfx_paths = {normalized(item["destination"]) for item in vfx_assets["assets"]}
    expected_files = CORE_FILES | texture_paths | vfx_paths | set(AUDIO_FILES.values())
    if any("/animations/" in path or path.endswith(".anm") for path in expected_files):
        raise ValueError("Stock-animation release unexpectedly contains animation assets")
    if not set(AUDIO_FILES.values()).issubset(expected_files):
        raise ValueError("Dark-witch SFX banks are missing from the package allowlist")

    config = load_json(os.path.join(project_root, "variants", "base", "mod.config.json"))
    if not SEMVER.fullmatch(config.get("version", "")) or config["version"] != VERSION:
        raise ValueError(f"Base config does not use semantic version {VERSION}")
    payload_result = validate_payload(
        project_root,
        os.path.abspath(args.package_extract),
        os.path.abspath(args.overlay),
        expected_files,
    )
    if not os.path.isfile(args.package):
        raise FileNotFoundError(args.package)

    stock_chunks, stock_hashes = wad_chunk_inventory(args.stock_wad)
    overlay_chunks, overlay_hashes = wad_chunk_inventory(args.overlay_wad)
    expected_new_chunks = vfx_assets["new_wad_entries"] + len(NEW_TEXTURE_ROUTES)
    if overlay_chunks != stock_chunks + expected_new_chunks:
        raise ValueError(
            f"Overlay WAD chunk count changed: stock={stock_chunks} "
            f"expected_new={expected_new_chunks} overlay={overlay_chunks}"
        )
    if stock_hashes - overlay_hashes:
        raise ValueError("Overlay WAD dropped stock chunk hashes")
    if len(overlay_hashes - stock_hashes) != expected_new_chunks:
        raise ValueError("Overlay WAD new chunk inventory drifted")

    routes = overlay_routes(os.path.join(reports_root, "abyssal_base_overlay.txt"))
    if routes != {"data/final/champions/jinx.wad.client"}:
        raise ValueError(f"Package escaped Jinx WAD routing: {sorted(routes)}")
    manual_review_path = os.path.join(
        reports_root, "abyssal_manual_visual_review.md"
    )
    if not os.path.isfile(manual_review_path):
        raise FileNotFoundError("The exported-overlay renders have not received manual review")

    payload = {
        "status": "PASSED",
        "version": VERSION,
        "target": "Ocean Song Jinx skin 65",
        "scope": "complete model, texture, VFX, and SFX replacement; stock animations retained",
        "live_game_smoke_test": "REQUIRED",
        "wad_mount_safety": {
            "status": "PASSED",
            "strategy": "in_place_jinx_and_isolated_shared",
            "stock_chunks": stock_chunks,
            "overlay_chunks": overlay_chunks,
            "new_chunks": expected_new_chunks,
            "stock_chunk_hashes_preserved": True,
        },
        "overlay_routing": {
            "status": "PASSED",
            "routes": sorted(routes),
            "unrelated_champion_wads_rebuilt": 0,
        },
        "package": {
            **payload_result,
            "path": os.path.abspath(args.package),
            "sha256": sha256_file(args.package),
            "animations_included": 0,
            "sound_assets_included": len(AUDIO_FILES),
        },
        "acceptance": {
            "zero_ocean_song_gameplay_geometry_retained": True,
            "native_skin65_skeletons_byte_identical": True,
            "champion_submeshes": list(CHAMPION_SUBMESHES),
            "chompers_submeshes": list(CHOMPER_SUBMESHES),
            "missile_submeshes": list(MISSILE_SUBMESHES),
            "six_opaque_texture_and_material_routes": True,
            "vfx_systems_rethemed": 117,
            "vfx_valuecolor_vectors_recolored": 2977,
            "particle_card_textures_byte_preserved": 319,
            "sfx_events_replaced": 60,
            "sfx_media_replaced": 63,
            "sfx_sound_objects_patched": 103,
            "wwise_vorbis_plugin": "0x00040001",
            "voice_over_retained": True,
            "animations_omitted_by_request": True,
            "exported_model_visual_qa": True,
            "manual_visual_review_completed": True,
            "manual_visual_review_report": {
                "path": os.path.abspath(manual_review_path),
                "sha256": sha256_file(manual_review_path),
            },
            "ltk_package_extract_validation": True,
            "ltk_overlay_validation": True,
            "bc1_bc3_tex_payload_layouts_validated": True,
        },
    }
    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2)
        handle.write("\n")
    print(
        "ABYSSAL_VALIDATION=PASSED "
        f"FILES={payload_result['files']} TEX={payload_result['tex_layouts_validated']} "
        f"VFX=117/2977 AUDIO=60/63/103 WAD_CHUNKS={stock_chunks}+{expected_new_chunks}"
    )


if __name__ == "__main__":
    main()
