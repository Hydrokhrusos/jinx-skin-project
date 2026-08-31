import argparse
import hashlib
import json
import os
import struct
import sys
import tempfile

import bpy
import numpy as np


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


def uv_fields(height, width):
    y, x = np.mgrid[0:height, 0:width].astype(np.float32)
    u = x / max(1, width - 1)
    v = y / max(1, height - 1)
    return u, v


def authored_pattern(height, width, role):
    u, v = uv_fields(height, width)
    black_violet = np.array((0.012, 0.004, 0.030), dtype=np.float32)
    deep_plum = np.array((0.115, 0.018, 0.180), dtype=np.float32)
    coral = np.array((0.920, 0.095, 0.250), dtype=np.float32)
    bone = np.array((0.720, 0.665, 0.580), dtype=np.float32)
    seafoam = np.array((0.070, 0.860, 0.620), dtype=np.float32)
    base_noise = (
        0.42
        + 0.20 * np.sin(u * 17.0 + np.sin(v * 9.0) * 2.6)
        + 0.15 * np.sin(v * 25.0 - u * 7.0)
        + 0.08 * np.cos((u + v) * 39.0)
    )
    vein_distance = np.abs(
        np.sin(u * 13.0 + np.sin(v * 8.0) * 2.4)
        * np.cos(v * 11.0 - np.sin(u * 7.0))
    )
    veins = np.clip((0.105 - vein_distance) / 0.105, 0.0, 1.0) ** 1.7
    scales = np.clip(
        (np.cos(u * 46.0) * np.cos(v * 39.0) - 0.55) / 0.45,
        0.0,
        1.0,
    )
    rings = np.clip(
        (np.cos(np.sqrt((u - 0.5) ** 2 + (v - 0.5) ** 2) * 110.0) - 0.40)
        / 0.60,
        0.0,
        1.0,
    )
    rgb = black_violet + deep_plum * np.clip(base_noise[..., None] * 0.52, 0.0, 0.55)
    if role == "armor":
        rgb += coral * veins[..., None] * 0.72
        rgb += seafoam * scales[..., None] * 0.48
        rgb += bone * rings[..., None] * 0.08
    elif role == "recall":
        sigils = np.clip(
            (np.cos((u - 0.5) * 86.0) * np.cos((v - 0.5) * 86.0) - 0.66)
            / 0.34,
            0.0,
            1.0,
        )
        rgb += seafoam * (rings * 0.62 + sigils * 0.42)[..., None]
        rgb += coral * veins[..., None] * 0.38
    elif role == "missile":
        rgb += bone * (0.07 + rings * 0.18)[..., None]
        rgb += coral * veins[..., None] * 0.58
        rgb += seafoam * scales[..., None] * 0.34
    else:
        raise ValueError(role)
    alpha = np.full((height, width, 1), 255, dtype=np.uint8)
    return np.concatenate(
        (np.clip(np.rint(rgb * 255.0), 0, 255).astype(np.uint8), alpha), axis=2
    )


def grade_body(rgba):
    rgb = rgba[..., :3].astype(np.float32) / 255.0
    maximum = rgb.max(axis=2, keepdims=True)
    minimum = rgb.min(axis=2, keepdims=True)
    luminance = (
        rgb[..., 0:1] * 0.2126 + rgb[..., 1:2] * 0.7152 + rgb[..., 2:3] * 0.0722
    )
    saturation = (maximum - minimum) / np.maximum(maximum, 1e-5)
    skin = np.clip((rgb[..., 0:1] - rgb[..., 2:3] * 0.86) * 3.2, 0.0, 1.0)
    skin *= np.clip((luminance - 0.18) * 2.4, 0.0, 1.0)
    blue = np.clip((rgb[..., 2:3] - rgb[..., 0:1] * 0.55) * 2.5, 0.0, 1.0)
    warm = np.clip((rgb[..., 0:1] - rgb[..., 1:2] * 0.72) * 2.6, 0.0, 1.0)
    neutral = np.clip(1.0 - saturation * 1.8, 0.0, 1.0)
    dark = np.clip(1.0 - luminance * 1.75, 0.0, 1.0)
    palette = mix_palette(
        [skin + 0.02, blue + 0.03, warm + 0.02, neutral * 0.55 + dark + 0.05],
        [
            (0.72, 0.58, 0.72),
            (0.025, 0.145, 0.265),
            (0.90, 0.075, 0.235),
            (0.035, 0.008, 0.075),
        ],
    )
    shade = np.clip(0.24 + luminance * 0.93, 0.10, 1.05)
    detail = (rgb - luminance) * 0.16
    target = np.clip(palette * shade + detail, 0.0, 1.0)
    u, v = uv_fields(rgba.shape[0], rgba.shape[1])
    glow = np.clip(
        (np.cos(u * 61.0 + np.sin(v * 23.0)) * np.cos(v * 49.0) - 0.76) / 0.24,
        0.0,
        1.0,
    )[..., None]
    non_skin = 1.0 - np.clip(skin * 1.3, 0.0, 1.0)
    target = target * (1.0 - glow * non_skin * 0.30) + np.array(
        (0.06, 0.88, 0.64), dtype=np.float32
    ) * glow * non_skin * 0.30
    alpha = np.full((*rgba.shape[:2], 1), 255, dtype=np.uint8)
    return np.concatenate(
        (np.clip(np.rint(target * 255.0), 0, 255).astype(np.uint8), alpha), axis=2
    )


def grade_weapon(rgba, mine=False):
    rgb = rgba[..., :3].astype(np.float32) / 255.0
    maximum = rgb.max(axis=2, keepdims=True)
    minimum = rgb.min(axis=2, keepdims=True)
    luminance = (
        rgb[..., 0:1] * 0.2126 + rgb[..., 1:2] * 0.7152 + rgb[..., 2:3] * 0.0722
    )
    saturation = (maximum - minimum) / np.maximum(maximum, 1e-5)
    warm = np.clip((rgb[..., 0:1] - rgb[..., 2:3] * 0.72) * 2.1, 0.0, 1.0)
    green = np.clip((rgb[..., 1:2] + rgb[..., 2:3] * 0.45 - rgb[..., 0:1]) * 1.9, 0.0, 1.0)
    pale = np.clip(luminance * (1.0 - saturation * 0.72), 0.0, 1.0)
    dark = np.clip(1.0 - luminance * 1.55, 0.0, 1.0)
    palette = mix_palette(
        [warm + 0.03, green + 0.03, pale + 0.06, dark + 0.08],
        [
            (0.92, 0.095, 0.235),
            (0.065, 0.88, 0.62),
            (0.70, 0.63, 0.52) if not mine else (0.24, 0.30, 0.31),
            (0.022, 0.005, 0.060),
        ],
    )
    shade = (
        np.clip(0.13 + luminance * 0.72, 0.07, 0.78)
        if mine
        else np.clip(0.19 + luminance * 1.02, 0.09, 1.08)
    )
    u, v = uv_fields(rgba.shape[0], rgba.shape[1])
    coral_ridges = np.clip(
        (np.cos(u * 45.0 + np.sin(v * 19.0) * 3.0) - 0.65) / 0.35,
        0.0,
        1.0,
    )[..., None]
    target = np.clip(palette * shade, 0.0, 1.0)
    target = target * (1.0 - coral_ridges * 0.22) + np.array(
        (0.96, 0.12, 0.30), dtype=np.float32
    ) * coral_ridges * 0.22
    alpha = np.full((*rgba.shape[:2], 1), 255, dtype=np.uint8)
    return np.concatenate(
        (np.clip(np.rint(target * 255.0), 0, 255).astype(np.uint8), alpha), axis=2
    )


def save_preview(rgba, path):
    height, width = rgba.shape[:2]
    image = bpy.data.images.new(os.path.basename(path), width=width, height=height, alpha=True)
    pixels = np.flipud(rgba).astype(np.float32).reshape(-1) / 255.0
    image.pixels.foreach_set(pixels)
    image.filepath_raw = os.path.abspath(path)
    image.file_format = "PNG"
    image.save()
    bpy.data.images.remove(image)


def image_metrics(rgba):
    rgb = rgba[..., :3].astype(np.float32)
    horizontal = np.abs(rgb[:, 1:] - rgb[:, :-1]).mean()
    vertical = np.abs(rgb[1:] - rgb[:-1]).mean()
    quantized = (rgba[..., :3] // 16).reshape(-1, 3)
    unique = len(np.unique(quantized, axis=0))
    return {
        "rgb_standard_deviation": round(float(rgb.std()), 4),
        "mean_neighbor_contrast": round(float((horizontal + vertical) * 0.5), 4),
        "quantized_unique_colors": unique,
        "opaque_pixels": int((rgba[..., 3] == 255).sum()),
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
            result = authored_pattern(rgba.shape[0], rgba.shape[1], role)
        else:
            raise ValueError(role)
        metrics = image_metrics(result)
        total_pixels = result.shape[0] * result.shape[1]
        if metrics["opaque_pixels"] != total_pixels:
            raise ValueError(f"Non-opaque pixels in {role} atlas")
        if metrics["rgb_standard_deviation"] < 18.0:
            raise ValueError(f"Atlas is too flat: {role}")
        if metrics["mean_neighbor_contrast"] < 0.55:
            raise ValueError(f"Atlas lacks local detail: {role}")
        if metrics["quantized_unique_colors"] < 12:
            raise ValueError(f"Atlas has too few colors: {role}")
        changed_pixels = int(np.any(result[..., :3] != rgba[..., :3], axis=2).sum())
        if changed_pixels < total_pixels * 0.95:
            raise ValueError(f"Too few changed pixels in {role}: {changed_pixels}/{total_pixels}")
        mip_levels = encode_tex_with_texconv(
            result, output, header, args.texconv, dither=True
        )
        layout = validate_tex_layout(output)
        decoded = load_tex(output, tex_to_dds_bytes)
        decoded_metrics = image_metrics(decoded)
        if decoded_metrics["opaque_pixels"] != total_pixels:
            raise ValueError(f"Compression introduced alpha in {role}")
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
                "preview": preview,
            }
        )

    payload = {
        "status": "PASSED",
        "version": "3.0.0",
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
