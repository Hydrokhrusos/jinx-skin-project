import argparse
import hashlib
import json
import os
import shutil
import struct
import sys
import tempfile

import bpy
import numpy as np


TEXTURES = (
    (
        "assets/characters/jinx/skins/skin65/jinx_skin65_tx_cm.tex",
        "assets/characters/jinx/skins/skin65/jinx_skin65_tx_cm.tex",
        "champion_diffuse",
    ),
    (
        "assets/characters/jinx/skins/skin65/jinx_skin65_body_mask_tx_cm.tex",
        "assets/characters/jinx/skins/skin65/jinx_skin65_body_mask_tx_cm.tex",
        "preserved_shader_input",
    ),
    ("assets/characters/jinx/skins/skin65/jinx_skin65_iridescent_tx_cm.tex", "assets/characters/jinx/skins/skin65/jinx_skin65_iridescent_tx_cm.tex", "preserved_shader_input"),
    ("assets/characters/jinx/skins/skin65/jinx_skin65_matcap_tx_cm.tex", "assets/characters/jinx/skins/skin65/jinx_skin65_matcap_tx_cm.tex", "preserved_shader_input"),
    ("assets/characters/jinx/skins/skin65/jinx_skin65_scrollingwater_tx_cm.tex", "assets/characters/jinx/skins/skin65/jinx_skin65_scrollingwater_tx_cm.tex", "preserved_shader_input"),
    ("assets/characters/jinx/skins/skin65/jinx_skin65_scrollingwater2_tx_cm.tex", "assets/characters/jinx/skins/skin65/jinx_skin65_scrollingwater2_tx_cm.tex", "preserved_shader_input"),
    (
        "assets/characters/jinx/skins/skin65/jinx_skin65_weapon_tx_cm.tex",
        "assets/characters/jinx/skins/skin65/jinx_skin65_weapon_tx_cm.tex",
        "weapons_diffuse",
    ),
    ("assets/characters/jinx/skins/skin65/jinx_skin65_weapon_mask_tx_cm.tex", "assets/characters/jinx/skins/skin65/jinx_skin65_weapon_mask_tx_cm.tex", "preserved_shader_input"),
    ("assets/characters/jinx/skins/skin65/jinx_skin65_weaponvfx_mask_tx_cm.tex", "assets/characters/jinx/skins/skin65/jinx_skin65_weaponvfx_mask_tx_cm.tex", "preserved_shader_input"),
    ("assets/characters/jinx/skins/skin65/jinx_skin65_skirt_tx_cm.tex", "assets/characters/jinx/skins/skin65/jinx_skin65_skirt_tx_cm.tex", "skirt"),
    ("assets/characters/jinx/skins/skin65/jinx_skin65_skirt_mask_tx_cm.tex", "assets/characters/jinx/skins/skin65/jinx_skin65_skirt_mask_tx_cm.tex", "preserved_shader_input"),
    ("assets/characters/jinx/skins/skin65/jinx_skin65_star_tx_cm.tex", "assets/characters/jinx/skins/skin65/jinx_skin65_star_tx_cm.tex", "preserved_shader_input"),
    (
        "assets/characters/jinxmine/skins/skin65/jinxmine_skin65_tx_cm.tex",
        "assets/characters/jinxmine/skins/skin65/jinxmine_skin65_tx_cm.tex",
        "chompers",
    ),
    (
        "assets/characters/jinx/skins/skin65/particles/jinx_skin65_r_mis_globefish.tex",
        "assets/characters/jinx/skins/skin65/particles/jinx_skin65_r_mis_globefish.tex",
        "ultimate_missile",
    ),
)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-root", required=True)
    parser.add_argument("--out-root", required=True)
    parser.add_argument("--addon-root", required=True)
    parser.add_argument("--texconv", required=True)
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
        raise ValueError(
            f"Expected BC1/BC3 source texture, got format 0x{texture_format:02x}: {path}"
        )
    return {
        "width": width,
        "height": height,
        "version": version,
        "format": texture_format,
        "flags": flags,
        "type": texture_type,
    }


def abyssal_grade(rgba, role):
    rgb = rgba[..., :3].astype(np.float32) / 255.0
    alpha = rgba[..., 3:4]
    palette = {
        "champion_diffuse": (0.035, 0.26, 0.46),
        "weapons_diffuse": (0.15, 0.22, 0.62),
        "skirt": (0.25, 0.10, 0.55),
        "chompers": (0.015, 0.44, 0.36),
        "ultimate_missile": (0.24, 0.08, 0.62),
    }
    if role not in palette:
        raise ValueError(f"No abyssal diffuse palette for role: {role}")
    base = np.array(palette[role], dtype=np.float32)
    # A nearly solid authored material is intentional here.  The native Ocean
    # Song diffuse contains dense horizontal water bands that became zebra-like
    # under a dark remap; retain only a quiet 6% of that detail.  Native alpha,
    # matcap, masks, iridescence, and scrolling-water inputs remain untouched.
    target = base * 0.94 + rgb * 0.06

    result = np.clip(np.rint(target * 255.0), 0, 255).astype(np.uint8)
    return np.concatenate((result, alpha), axis=2)


def main():
    args = parse_args()
    sys.path.insert(0, os.path.abspath(args.addon_root))
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from Aventurine.utils.texture_manager import tex_to_dds_bytes
    from encode_tex import encode_tex_with_texconv, validate_tex_layout

    rows = []
    for source_relative, output_relative, role in TEXTURES:
        source = os.path.join(os.path.abspath(args.source_root), source_relative)
        output = os.path.join(os.path.abspath(args.out_root), output_relative)
        if not os.path.isfile(source):
            raise FileNotFoundError(source)
        header = source_header(source)

        if role == "preserved_shader_input":
            os.makedirs(os.path.dirname(output), exist_ok=True)
            shutil.copy2(source, output)
            row = {
                "path": output_relative,
                "source_path": source_relative,
                "role": role,
                "status": "preserved",
                "format": "BC1" if header["format"] == 0x0A else "BC3",
                "width": header["width"],
                "height": header["height"],
                "source_sha256": sha256_file(source),
                "output_sha256": sha256_file(output),
                "changed_pixels": 0,
                "total_pixels": header["width"] * header["height"],
                "layout": validate_tex_layout(output),
            }
            rows.append(row)
            continue

        descriptor, temporary_dds = tempfile.mkstemp(suffix=".dds")
        os.close(descriptor)
        try:
            with open(temporary_dds, "wb") as handle:
                handle.write(tex_to_dds_bytes(source))
            image = bpy.data.images.load(temporary_dds, check_existing=False)
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
        finally:
            if os.path.exists(temporary_dds):
                os.remove(temporary_dds)

        if (width, height) != (header["width"], header["height"]):
            raise ValueError(f"Decoded texture dimensions changed: {source}")
        graded = abyssal_grade(rgba, role)
        changed_pixels = int(np.any(graded[..., :3] != rgba[..., :3], axis=2).sum())
        if changed_pixels < width * height * 0.95:
            raise ValueError(f"Too few pixels changed in {output_relative}: {changed_pixels}")
        mip_levels = encode_tex_with_texconv(graded, output, header, args.texconv)
        decoded_output_bytes = len(tex_to_dds_bytes(output))
        row = {
            "path": output_relative,
            "source_path": source_relative,
            "role": role,
            "status": "recolored",
            "format": "BC1" if header["format"] == 0x0A else "BC3",
            "width": width,
            "height": height,
            "source_sha256": sha256_file(source),
            "output_sha256": sha256_file(output),
            "changed_pixels": changed_pixels,
            "total_pixels": width * height,
            "mip_levels": mip_levels,
            "encoder": "Microsoft DirectXTex texconv 2026.5.8",
            "decoded_output_bytes": decoded_output_bytes,
        }
        if row["source_sha256"] == row["output_sha256"]:
            raise ValueError(f"Texture did not change: {output_relative}")
        rows.append(row)

    payload = {
        "status": "PASSED",
        "theme": "abyssal navy, bioluminescent teal, ultraviolet",
        "textures_packaged": len(rows),
        "textures_recolored": sum(item["status"] == "recolored" for item in rows),
        "shader_inputs_preserved": sum(item["status"] == "preserved" for item in rows),
        "native_ocean_song_uv_atlases_used": True,
        "textures": rows,
    }
    os.makedirs(os.path.dirname(os.path.abspath(args.report)), exist_ok=True)
    with open(args.report, "w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2)
        handle.write("\n")
    print(
        f"ABYSSAL_TEXTURES=PASSED RECOLORED={payload['textures_recolored']} "
        f"PRESERVED={payload['shader_inputs_preserved']} "
        f"PIXELS={sum(item['changed_pixels'] for item in rows)}"
    )


if __name__ == "__main__":
    try:
        main()
    except Exception:
        import traceback

        traceback.print_exc()
        sys.exit(1)
