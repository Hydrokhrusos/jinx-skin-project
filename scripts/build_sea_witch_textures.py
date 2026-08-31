import argparse
import hashlib
import json
import os
import struct
import sys
import tempfile

import bpy
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from project_version import VERSION
from sea_witch_materials import MATERIAL_TILES


TEXTURE_SPECS = (
    (
        "assets/characters/jinx/skins/skin51/jinx_skin51_main_tx_cm.tex",
        "assets/characters/jinx/skins/skin65/jinx_skin65_seawitch_body_tx_cm.tex",
        "body",
    ),
    (
        "assets/characters/jinx/skins/skin62/jinx_skin62_tx_cm.tex",
        "assets/characters/jinx/skins/skin65/jinx_skin65_seawitch_armor_tx_cm.tex",
        "armor",
    ),
    (
        "assets/characters/jinx/skins/skin62/jinx_skin62_weapon_tx_cm.tex",
        "assets/characters/jinx/skins/skin65/jinx_skin65_seawitch_weapon_tx_cm.tex",
        "weapon",
    ),
    (
        "assets/characters/jinx/skins/skin62/jinx_skin62_recall_tx_cm.tex",
        "assets/characters/jinx/skins/skin65/jinx_skin65_seawitch_recall_tx_cm.tex",
        "recall",
    ),
    (
        "assets/characters/jinxmine/skins/skin62/jinxmine_skin62_tx_cm.tex",
        "assets/characters/jinxmine/skins/skin65/jinxmine_skin65_tx_cm.tex",
        "mine",
    ),
    (
        "assets/characters/jinx/skins/skin65/particles/jinx_skin65_r_mis_globefish.tex",
        "assets/characters/jinx/skins/skin65/particles/jinx_skin65_r_mis_globefish.tex",
        "missile",
    ),
)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-root", required=True)
    parser.add_argument("--out-root", required=True)
    parser.add_argument("--addon-root", required=True)
    parser.add_argument("--texconv", required=True)
    parser.add_argument("--preview-dir", required=True)
    parser.add_argument("--report", required=True)
    argv = sys.argv[sys.argv.index("--") + 1 :] if "--" in sys.argv else sys.argv[1:]
    return parser.parse_args(argv)


def sha256_file(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def source_header(path):
    with open(path, "rb") as handle:
        data = handle.read(12)
    if len(data) != 12 or data[:4] != b"TEX\0":
        raise ValueError(f"Invalid TEX header: {path}")
    width, height, version, texture_format, flags, texture_type = struct.unpack(
        "<HHBBBB", data[4:]
    )
    if texture_format not in {0x0A, 0x0C}:
        raise ValueError(f"Unsupported source TEX format: 0x{texture_format:02x}")
    return {
        "width": width,
        "height": height,
        "version": version,
        "format": texture_format,
        "flags": flags,
        "type": texture_type,
    }


def load_tex(path, tex_to_dds_bytes):
    descriptor, temporary = tempfile.mkstemp(suffix=".dds")
    os.close(descriptor)
    try:
        with open(temporary, "wb") as handle:
            handle.write(tex_to_dds_bytes(os.path.abspath(path)))
        image = bpy.data.images.load(temporary, check_existing=False)
        image.colorspace_settings.name = "Non-Color"
        width, height = map(int, image.size)
        pixels = np.empty(width * height * 4, dtype=np.float32)
        image.pixels.foreach_get(pixels)
        rgba = np.flipud(
            np.clip(np.rint(pixels.reshape(height, width, 4) * 255.0), 0, 255).astype(
                np.uint8
            )
        ).copy()
        bpy.data.images.remove(image)
        return rgba
    finally:
        if os.path.exists(temporary):
            os.remove(temporary)


def mix_palette(weights, colors):
    total = np.maximum(sum(weights), 1e-6)
    result = np.zeros((*weights[0].shape[:2], 3), dtype=np.float32)
    for weight, color in zip(weights, colors):
        result += (weight / total) * np.asarray(color, dtype=np.float32)
    return result


def smoothstep(edge0, edge1, value):
    amount = np.clip((value - edge0) / max(edge1 - edge0, 1e-6), 0.0, 1.0)
    return amount * amount * (3.0 - 2.0 * amount)


def uv_fields(height, width):
    y, x = np.mgrid[0:height, 0:width].astype(np.float32)
    u = x / max(1, width - 1)
    v = 1.0 - y / max(1, height - 1)
    return u, v


def opaque_rgba(rgb):
    alpha = np.full((*rgb.shape[:2], 1), 255, dtype=np.uint8)
    return np.concatenate(
        (np.clip(np.rint(rgb * 255.0), 0, 255).astype(np.uint8), alpha), axis=2
    )


def palette_ramp(weights, shadows, highlights, luminance, low=0.025, high=0.92):
    shadow = mix_palette(weights, shadows)
    highlight = mix_palette(weights, highlights)
    amount = smoothstep(low, high, luminance) ** 0.88
    return shadow * (1.0 - amount) + highlight * amount


def material_pattern(height, width, material, role):
    u, v = uv_fields(height, width)
    math_tau = np.pi * 2.0
    grain = np.sin(u * 19.7 + v * 7.1) * np.sin(v * 16.3 - u * 5.7)
    broad = 0.5 + 0.5 * np.cos(math_tau * (u * 2.0 + 0.10 * np.sin(v * math_tau)))
    growth = 0.5 + 0.5 * np.cos(math_tau * (v * 3.0 + 0.08 * np.sin(u * math_tau)))

    palettes = {
        "coral": ((0.105, 0.016, 0.050), (0.880, 0.255, 0.300)),
        "bone": ((0.105, 0.085, 0.105), (0.790, 0.690, 0.515)),
        "abyssal": ((0.008, 0.012, 0.040), (0.245, 0.155, 0.390)),
        "seafoam": ((0.008, 0.090, 0.105), (0.210, 0.900, 0.665)),
    }
    shadow, highlight = (np.asarray(color, dtype=np.float32) for color in palettes[material])
    if material == "coral":
        amount = 0.32 + broad * 0.32 + (1.0 - v) * 0.22 + grain * 0.055
        amount *= 1.0 - smoothstep(0.72, 1.0, v) * 0.42
    elif material == "bone":
        amount = 0.40 + broad * 0.17 + growth * 0.24 + grain * 0.045
        seam = smoothstep(0.82, 1.0, np.abs(u - 0.5) * 2.0)
        amount *= 1.0 - seam * 0.20
    elif material == "abyssal":
        amount = 0.22 + broad * 0.20 + growth * 0.12 + (1.0 - v) * 0.18 + grain * 0.035
    elif material == "seafoam":
        center = np.sin(np.pi * u) * np.sin(np.pi * v)
        amount = 0.30 + center * 0.47 + broad * 0.13 + grain * 0.035
    else:
        raise ValueError(material)

    if role == "recall" and material == "seafoam":
        amount = np.clip(amount * 1.13 + 0.05, 0.0, 1.0)
    elif role == "missile" and material == "bone":
        amount = np.clip(amount * 1.08, 0.0, 1.0)
    amount = np.clip(amount, 0.0, 1.0)[..., None]
    rgb = shadow * (1.0 - amount) + highlight * amount
    return np.clip(rgb, 0.0, 1.0)


def material_pixel_region(height, width, material):
    u0, v0, u1, v1 = MATERIAL_TILES[material]
    x0 = int(round(u0 * width))
    x1 = int(round(u1 * width))
    # Aventurine's TEX-to-DDS path presents DDS rows in the same vertical
    # direction used by exported SKN UVs; flipping V here swaps material tiles.
    y0 = int(round(v0 * height))
    y1 = int(round(v1 * height))
    return y0, y1, x0, x1


def authored_atlas(height, width, role):
    rgb = np.zeros((height, width, 3), dtype=np.float32)
    for material in MATERIAL_TILES:
        y0, y1, x0, x1 = material_pixel_region(height, width, material)
        rgb[y0:y1, x0:x1] = material_pattern(
            y1 - y0, x1 - x0, material, role
        )
    return opaque_rgba(rgb)


def grade_body(rgba):
    rgb = rgba[..., :3].astype(np.float32) / 255.0
    red = rgb[..., 0:1]
    green = rgb[..., 1:2]
    blue = rgb[..., 2:3]
    maximum = rgb.max(axis=2, keepdims=True)
    minimum = rgb.min(axis=2, keepdims=True)
    luminance = red * 0.2126 + green * 0.7152 + blue * 0.0722
    saturation = (maximum - minimum) / np.maximum(maximum, 1e-5)
    bright = smoothstep(0.16, 0.68, luminance)
    dark = 1.0 - smoothstep(0.03, 0.55, luminance)

    teal = np.clip((green + blue - red * 1.42 - 0.04) * 2.4, 0.0, 1.0)
    gold = np.clip((red * 0.72 + green * 0.72 - blue * 1.30 - 0.06) * 2.5, 0.0, 1.0)
    pale = np.clip(1.0 - saturation * 1.85, 0.0, 1.0) * bright
    coral = np.clip((red - green * 1.18 - 0.015) * 2.7, 0.0, 1.0) * saturation
    skin = np.clip(
        (red * 0.78 + green * 0.30 - blue * 0.54 - 0.035) * 2.0,
        0.0,
        1.0,
    )
    skin *= bright * np.clip(1.18 - saturation, 0.0, 1.0)
    violet = np.clip((red + blue * 0.72 - green * 1.38) * 1.5, 0.0, 1.0)
    abyssal = dark + np.clip(0.42 - saturation, 0.0, 0.42) * 0.55

    weights = [
        skin + 0.018,
        teal + 0.012,
        gold + 0.010,
        pale + 0.012,
        coral + 0.010,
        violet + 0.018,
        abyssal + 0.025,
    ]
    shadows = [
        (0.205, 0.105, 0.205),
        (0.005, 0.070, 0.095),
        (0.105, 0.065, 0.045),
        (0.105, 0.105, 0.155),
        (0.125, 0.012, 0.055),
        (0.040, 0.012, 0.075),
        (0.006, 0.004, 0.024),
    ]
    highlights = [
        (0.835, 0.665, 0.745),
        (0.105, 0.785, 0.610),
        (0.745, 0.570, 0.325),
        (0.700, 0.665, 0.730),
        (0.875, 0.190, 0.315),
        (0.390, 0.145, 0.515),
        (0.105, 0.035, 0.155),
    ]
    target = palette_ramp(weights, shadows, highlights, luminance)
    source_detail = (rgb - luminance) * 0.055
    return opaque_rgba(np.clip(target + source_detail, 0.0, 1.0))


def grade_weapon(rgba, mine=False):
    rgb = rgba[..., :3].astype(np.float32) / 255.0
    red = rgb[..., 0:1]
    green = rgb[..., 1:2]
    blue = rgb[..., 2:3]
    maximum = rgb.max(axis=2, keepdims=True)
    minimum = rgb.min(axis=2, keepdims=True)
    luminance = red * 0.2126 + green * 0.7152 + blue * 0.0722
    saturation = (maximum - minimum) / np.maximum(maximum, 1e-5)
    bright = smoothstep(0.15, 0.66, luminance)
    dark = 1.0 - smoothstep(0.025, 0.52, luminance)

    coral = np.clip((red - green * 1.34 - 0.01) * 3.1, 0.0, 1.0) * saturation
    seafoam = np.clip(
        (green * 0.58 + blue * 0.88 - red * 0.90 - 0.055) * 2.2,
        0.0,
        1.0,
    ) * (0.35 + saturation)
    brass = np.clip(
        (red * 0.66 + green * 0.70 - blue * 1.18 - 0.04) * 2.3,
        0.0,
        1.0,
    )
    silver = np.clip(1.0 - saturation * 1.65, 0.0, 1.0) * bright
    violet = np.clip((blue + red * 0.32 - green * 0.88) * 1.65, 0.0, 1.0)
    abyssal = dark + np.clip(0.36 - saturation, 0.0, 0.36) * 0.45

    weights = [
        coral + 0.010,
        seafoam + 0.012,
        brass + 0.016,
        silver + 0.012,
        violet + 0.012,
        abyssal + 0.028,
    ]
    shadows = [
        (0.120, 0.012, 0.045),
        (0.005, 0.070, 0.085),
        (0.105, 0.065, 0.032),
        (0.105, 0.105, 0.125),
        (0.025, 0.018, 0.080),
        (0.005, 0.004, 0.022),
    ]
    highlights = [
        (0.915, 0.175, 0.285),
        (0.105, 0.865, 0.635),
        (0.790, 0.610, 0.330),
        (0.730, 0.700, 0.665),
        (0.285, 0.185, 0.475),
        (0.095, 0.030, 0.135),
    ]
    high = 1.05 if mine else 0.92
    target = palette_ramp(weights, shadows, highlights, luminance, high=high)
    if mine:
        target *= 0.84
    source_detail = (rgb - luminance) * 0.045
    return opaque_rgba(np.clip(target + source_detail, 0.0, 1.0))


def save_preview(rgba, path):
    height, width = rgba.shape[:2]
    image = bpy.data.images.new(os.path.basename(path), width=width, height=height, alpha=True)
    pixels = np.flipud(rgba).astype(np.float32).reshape(-1) / 255.0
    image.pixels.foreach_set(pixels)
    image.filepath_raw = os.path.abspath(path)
    image.file_format = "PNG"
    image.save()
    bpy.data.images.remove(image)


def color_family_metrics(rgb):
    red = rgb[..., 0]
    green = rgb[..., 1]
    blue = rgb[..., 2]
    maximum = rgb.max(axis=2)
    minimum = rgb.min(axis=2)
    luminance = red * 0.2126 + green * 0.7152 + blue * 0.0722
    saturation = (maximum - minimum) / np.maximum(maximum, 1.0)
    masks = {
        "coral": (red > green * 1.35) & (red > blue * 1.12) & (red > 48.0),
        "seafoam": (green > red * 1.28) & (green > blue * 0.86) & (green > 48.0),
        "bone": (
            (red > green * 1.01)
            & (green > blue * 1.10)
            & (luminance > 62.0)
            & (saturation < 0.72)
        ),
        "violet": (blue > green * 1.16) & (red > green * 0.92) & (blue > 34.0),
        "neutral_light": (saturation < 0.16) & (luminance > 72.0),
    }
    return {
        name: round(float(mask.mean()), 6)
        for name, mask in masks.items()
    }


def material_region_metrics(rgba):
    rgb = rgba[..., :3].astype(np.float32)
    rows = {}
    means = []
    for material in MATERIAL_TILES:
        y0, y1, x0, x1 = material_pixel_region(
            rgba.shape[0], rgba.shape[1], material
        )
        mean = rgb[y0:y1, x0:x1].mean(axis=(0, 1))
        means.append(mean)
        rows[material] = {
            "mean_rgb": [round(float(value), 3) for value in mean],
            "mean_luminance": round(
                float(mean[0] * 0.2126 + mean[1] * 0.7152 + mean[2] * 0.0722),
                3,
            ),
        }
    distances = [
        float(np.linalg.norm(means[first] - means[second]))
        for first in range(len(means))
        for second in range(first + 1, len(means))
    ]
    return {
        "regions": rows,
        "minimum_mean_rgb_distance": round(min(distances), 3),
    }


def image_metrics(rgba, authored_materials=False):
    rgb = rgba[..., :3].astype(np.float32)
    horizontal = np.abs(rgb[:, 1:] - rgb[:, :-1]).mean()
    vertical = np.abs(rgb[1:] - rgb[:-1]).mean()
    quantized = (rgba[..., :3] // 16).reshape(-1, 3)
    unique = len(np.unique(quantized, axis=0))
    luminance = (
        rgb[..., 0] * 0.2126 + rgb[..., 1] * 0.7152 + rgb[..., 2] * 0.0722
    )
    low, median, high = np.percentile(luminance, (5.0, 50.0, 95.0))
    families = color_family_metrics(rgb)
    result = {
        "rgb_standard_deviation": round(float(rgb.std()), 4),
        "mean_neighbor_contrast": round(float((horizontal + vertical) * 0.5), 4),
        "quantized_unique_colors": unique,
        "opaque_pixels": int((rgba[..., 3] == 255).sum()),
        "luminance_percentiles": {
            "p05": round(float(low), 3),
            "p50": round(float(median), 3),
            "p95": round(float(high), 3),
        },
        "luminance_span_p05_p95": round(float(high - low), 3),
        "color_family_fractions": families,
        "color_families_above_one_percent": sum(
            fraction >= 0.01 for fraction in families.values()
        ),
    }
    if authored_materials:
        result["material_separation"] = material_region_metrics(rgba)
    return result


def validate_image_metrics(role, stage, metrics, total_pixels, authored_materials):
    label = f"{stage} {role} atlas"
    if metrics["opaque_pixels"] != total_pixels:
        raise ValueError(f"{label} contains non-opaque pixels")
    if metrics["rgb_standard_deviation"] < 18.0:
        raise ValueError(f"{label} is too flat")
    if metrics["mean_neighbor_contrast"] < 0.18:
        raise ValueError(f"{label} lacks local detail")
    if metrics["quantized_unique_colors"] < 24:
        raise ValueError(f"{label} has too few colors")
    if metrics["luminance_span_p05_p95"] < 48.0:
        raise ValueError(f"{label} lacks a readable value hierarchy")
    if metrics["color_families_above_one_percent"] < 3:
        raise ValueError(f"{label} lacks material color separation")
    if authored_materials and (
        metrics["material_separation"]["minimum_mean_rgb_distance"] < 48.0
    ):
        raise ValueError(f"{label} material tiles are not distinct")


def compression_metrics(authored, decoded):
    if decoded.shape != authored.shape:
        raise ValueError(
            f"Decoded TEX dimensions changed: expected {authored.shape}, got {decoded.shape}"
        )
    rgb_error = np.abs(
        decoded[..., :3].astype(np.float32) - authored[..., :3].astype(np.float32)
    )
    alpha_mismatches = int((decoded[..., 3] != authored[..., 3]).sum())
    return {
        "mean_absolute_rgb_error": round(float(rgb_error.mean()), 4),
        "p95_absolute_rgb_error": round(float(np.percentile(rgb_error, 95.0)), 4),
        "alpha_mismatches": alpha_mismatches,
    }


def main():
    args = parse_args()
    sys.path.insert(0, os.path.abspath(args.addon_root))
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from Aventurine.utils.texture_manager import tex_to_dds_bytes
    from encode_tex import encode_tex_with_texconv
    from tex_layout import validate_tex_layout

    source_root = os.path.abspath(args.source_root)
    output_root = os.path.abspath(args.out_root)
    preview_root = os.path.abspath(args.preview_dir)
    os.makedirs(preview_root, exist_ok=True)
    rows = []
    for source_relative, output_relative, role in TEXTURE_SPECS:
        source = os.path.join(source_root, *source_relative.split("/"))
        output = os.path.join(output_root, *output_relative.split("/"))
        if not os.path.isfile(source):
            raise FileNotFoundError(source)
        header = source_header(source)
        rgba = load_tex(source, tex_to_dds_bytes)
        if role == "body":
            result = grade_body(rgba)
        elif role == "weapon":
            result = grade_weapon(rgba)
        elif role == "mine":
            result = grade_weapon(rgba, mine=True)
        elif role in {"armor", "recall", "missile"}:
            result = authored_atlas(rgba.shape[0], rgba.shape[1], role)
        else:
            raise ValueError(role)
        uses_authored_materials = role in {"armor", "recall", "missile"}
        metrics = image_metrics(result, authored_materials=uses_authored_materials)
        total_pixels = result.shape[0] * result.shape[1]
        validate_image_metrics(
            role, "Authored", metrics, total_pixels, uses_authored_materials
        )
        changed_pixels = int(np.any(result[..., :3] != rgba[..., :3], axis=2).sum())
        if changed_pixels < total_pixels * 0.95:
            raise ValueError(f"Too few changed pixels in {role}: {changed_pixels}/{total_pixels}")
        mip_levels = encode_tex_with_texconv(
            result, output, header, args.texconv, dither=True
        )
        layout = validate_tex_layout(output)
        decoded = load_tex(output, tex_to_dds_bytes)
        decoded_metrics = image_metrics(
            decoded, authored_materials=uses_authored_materials
        )
        validate_image_metrics(
            role, "Decoded", decoded_metrics, total_pixels, uses_authored_materials
        )
        compression = compression_metrics(result, decoded)
        if compression["alpha_mismatches"]:
            raise ValueError(f"Compression changed alpha in {role}")
        if compression["mean_absolute_rgb_error"] > 16.0:
            raise ValueError(f"Compression corrupted the top mip in {role}")
        if compression["p95_absolute_rgb_error"] > 48.0:
            raise ValueError(f"Compression lost excessive color detail in {role}")
        preview = os.path.join(preview_root, f"sea_witch_{role}_atlas.png")
        save_preview(decoded, preview)
        rows.append(
            {
                "role": role,
                "source": source_relative,
                "output": output_relative,
                "source_sha256": sha256_file(source),
                "output_sha256": sha256_file(output),
                "changed_pixels": changed_pixels,
                "total_pixels": total_pixels,
                "mip_levels": mip_levels,
                "layout": layout,
                "authored_metrics": metrics,
                "decoded_metrics": decoded_metrics,
                "compression_metrics": compression,
                "preview": preview,
            }
        )

    payload = {
        "status": "PASSED",
        "version": VERSION,
        "theme": "black-violet sea witch, coral pink relics, seafoam bioluminescence, aged bone",
        "opaque_material_atlases": True,
        "textures": rows,
    }
    os.makedirs(os.path.dirname(os.path.abspath(args.report)), exist_ok=True)
    with open(args.report, "w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2)
        handle.write("\n")
    print(
        f"SEA_WITCH_TEXTURES=PASSED COUNT={len(rows)} "
        f"CHANGED_PIXELS={sum(row['changed_pixels'] for row in rows)}"
    )


if __name__ == "__main__":
    try:
        main()
    except Exception:
        import traceback

        traceback.print_exc()
        sys.exit(1)
