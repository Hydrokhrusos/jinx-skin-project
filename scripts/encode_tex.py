import argparse
import hashlib
import json
import os
import subprocess
import struct
import sys
import tempfile

import numpy as np

from tex_layout import expected_tex_payload_size, validate_tex_layout


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--report", required=True)
    argv = sys.argv[sys.argv.index("--") + 1 :] if "--" in sys.argv else sys.argv[1:]
    return parser.parse_args(argv)


def sha256_file(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def rgb565(rgb):
    rgb = rgb.astype(np.uint16)
    return ((rgb[:, 0] >> 3) << 11) | ((rgb[:, 1] >> 2) << 5) | (rgb[:, 2] >> 3)


def expand565(values):
    values = values.astype(np.uint16)
    red = (values >> 11) & 31
    green = (values >> 5) & 63
    blue = values & 31
    return np.stack(
        (
            (red << 3) | (red >> 2),
            (green << 2) | (green >> 4),
            (blue << 3) | (blue >> 2),
        ),
        axis=1,
    ).astype(np.int16)


def _rgba_blocks(rgba):
    height, width = rgba.shape[:2]
    padded_width = (width + 3) & ~3
    padded_height = (height + 3) & ~3
    if padded_width != width or padded_height != height:
        padded = np.zeros((padded_height, padded_width, 4), dtype=np.uint8)
        padded[:height, :width] = rgba
        padded[height:, :width] = rgba[-1:, :, :]
        padded[:, width:] = padded[:, width - 1 : width]
        rgba = padded

    return (
        rgba.reshape(padded_height // 4, 4, padded_width // 4, 4, 4)
        .transpose(0, 2, 1, 3, 4)
        .reshape(-1, 16, 4)
    )


def encode_bc1(rgba, force_opaque=False):
    blocks = _rgba_blocks(rgba)
    output = bytearray()
    for start in range(0, len(blocks), 32768):
        block = blocks[start : start + 32768]
        rgb = block[:, :, :3].astype(np.int16)
        alpha = block[:, :, 3]
        transparent = (
            np.zeros(len(block), dtype=bool)
            if force_opaque
            else np.any(alpha < 128, axis=1)
        )
        opaque_mask = (
            np.ones_like(alpha, dtype=bool) if force_opaque else alpha >= 128
        )
        luminance = rgb[:, :, 0] * 54 + rgb[:, :, 1] * 183 + rgb[:, :, 2] * 19
        minimum_luma = np.where(opaque_mask, luminance, 1 << 30)
        maximum_luma = np.where(opaque_mask, luminance, -1)
        minimum_index = np.argmin(minimum_luma, axis=1)
        maximum_index = np.argmax(maximum_luma, axis=1)
        rows = np.arange(len(block))
        minimum_rgb = rgb[rows, minimum_index].astype(np.uint8)
        maximum_rgb = rgb[rows, maximum_index].astype(np.uint8)
        all_transparent = ~np.any(opaque_mask, axis=1)
        minimum_rgb[all_transparent] = 0
        maximum_rgb[all_transparent] = 0

        minimum_565 = rgb565(minimum_rgb)
        maximum_565 = rgb565(maximum_rgb)
        color0 = np.where(transparent, minimum_565, maximum_565).astype(np.uint16)
        color1 = np.where(transparent, maximum_565, minimum_565).astype(np.uint16)
        equal_opaque = (~transparent) & (color0 <= color1)
        increment = equal_opaque & (color0 < 0xFFFF)
        decrement = equal_opaque & ~increment
        color0[increment] += 1
        color1[decrement] -= 1

        first = expand565(color0)
        second = expand565(color1)
        palette = np.empty((len(block), 4, 3), dtype=np.int16)
        palette[:, 0] = first
        palette[:, 1] = second
        opaque_rows = ~transparent
        palette[opaque_rows, 2] = (2 * first[opaque_rows] + second[opaque_rows]) // 3
        palette[opaque_rows, 3] = (first[opaque_rows] + 2 * second[opaque_rows]) // 3
        palette[transparent, 2] = (first[transparent] + second[transparent]) // 2
        palette[transparent, 3] = 0

        delta = (rgb[:, :, None, :] - palette[:, None, :, :]).astype(np.int32)
        distance = np.sum(delta * delta, axis=3, dtype=np.int32)
        indices = np.argmin(distance, axis=2).astype(np.uint32)
        indices[(transparent[:, None]) & (~opaque_mask)] = 3
        packed_indices = np.zeros(len(block), dtype=np.uint32)
        for pixel in range(16):
            packed_indices |= indices[:, pixel] << (2 * pixel)

        records = np.empty(
            len(block),
            dtype=np.dtype([("c0", "<u2"), ("c1", "<u2"), ("indices", "<u4")]),
        )
        records["c0"] = color0
        records["c1"] = color1
        records["indices"] = packed_indices
        output.extend(records.tobytes())
    return bytes(output)


def encode_bc3(rgba):
    blocks = _rgba_blocks(rgba)
    color_blocks = encode_bc1(rgba, force_opaque=True)
    output = bytearray()
    color_offset = 0
    for start in range(0, len(blocks), 32768):
        block = blocks[start : start + 32768]
        alpha = block[:, :, 3].astype(np.uint16)
        alpha0 = alpha.max(axis=1)
        alpha1 = alpha.min(axis=1)
        palette = np.empty((len(block), 8), dtype=np.uint16)
        palette[:, 0] = alpha0
        palette[:, 1] = alpha1
        eight_alpha = alpha0 > alpha1
        for index in range(1, 7):
            palette[eight_alpha, index + 1] = (
                (7 - index) * alpha0[eight_alpha]
                + index * alpha1[eight_alpha]
                + 3
            ) // 7
        six_alpha = ~eight_alpha
        for index in range(1, 5):
            palette[six_alpha, index + 1] = (
                (5 - index) * alpha0[six_alpha]
                + index * alpha1[six_alpha]
                + 2
            ) // 5
        palette[six_alpha, 6] = 0
        palette[six_alpha, 7] = 255

        distance = np.abs(
            alpha[:, :, None].astype(np.int16)
            - palette[:, None, :].astype(np.int16)
        )
        indices = np.argmin(distance, axis=2).astype(np.uint64)
        packed = np.zeros(len(block), dtype=np.uint64)
        for pixel in range(16):
            packed |= indices[:, pixel] << (3 * pixel)

        for row in range(len(block)):
            output.append(int(alpha0[row]))
            output.append(int(alpha1[row]))
            output.extend(int(packed[row]).to_bytes(6, "little"))
            output.extend(color_blocks[color_offset : color_offset + 8])
            color_offset += 8
    return bytes(output)


def downsample(image):
    height, width = image.shape[:2]
    if width == 1 and height == 1:
        return image
    if width > 1 and height > 1:
        trimmed = image[: height - height % 2, : width - width % 2]
        return (
            trimmed.reshape(trimmed.shape[0] // 2, 2, trimmed.shape[1] // 2, 2, 4)
            .mean(axis=(1, 3))
            .round()
            .astype(np.uint8)
        )
    if width > 1:
        return image[:, : width - width % 2].reshape(height, width // 2, 2, 4).mean(axis=2).round().astype(np.uint8)
    return image[: height - height % 2].reshape(height // 2, 2, width, 4).mean(axis=1).round().astype(np.uint8)


def write_tga(rgba, path):
    height, width = rgba.shape[:2]
    header = struct.pack(
        "<BBBHHBHHHHBB",
        0,
        0,
        2,
        0,
        0,
        0,
        0,
        0,
        width,
        height,
        32,
        0x28,
    )
    with open(path, "wb") as handle:
        handle.write(header)
        handle.write(rgba[..., [2, 1, 0, 3]].tobytes())


def encode_tex_with_texconv(rgba, path, header, texconv, dither=True):
    height, width = rgba.shape[:2]
    if width != header["width"] or height != header["height"]:
        raise ValueError("TEX dimensions changed before DirectXTex compression")
    fourcc = b"DXT1" if header["format"] == 0x0A else b"DXT5"
    dxgi_format = "BC1_UNORM" if header["format"] == 0x0A else "BC3_UNORM"
    with tempfile.TemporaryDirectory(prefix="abyssal_texconv_") as temporary:
        source = os.path.join(temporary, "input.tga")
        output_dds = os.path.join(temporary, "input.dds")
        write_tga(rgba, source)
        command = [
            os.path.abspath(texconv),
            "-nologo",
            "-y",
            "-dx9",
            "-f",
            dxgi_format,
            "-m",
            "0",
            "-if",
            "FANT",
            "-sepalpha",
            "--tga-zero-alpha",
            "-o",
            temporary,
            source,
        ]
        if dither:
            command[command.index("-sepalpha"):command.index("-sepalpha")] = ["-bc", "d"]
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode or not os.path.isfile(output_dds):
            raise RuntimeError(
                "DirectXTex compression failed: "
                + (result.stdout + "\n" + result.stderr).strip()
            )
        with open(output_dds, "rb") as handle:
            dds = handle.read()
    if len(dds) < 128 or dds[:4] != b"DDS " or dds[84:88] != fourcc:
        raise ValueError(f"Unexpected DirectXTex DDS layout for {path}")
    payload = dds[128:]
    expected = expected_tex_payload_size(width, height, header["format"])
    if len(payload) != expected:
        raise ValueError(
            f"DirectXTex mip payload mismatch: expected {expected}, got {len(payload)}"
        )
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with open(path, "wb") as handle:
        handle.write(b"TEX\0")
        handle.write(
            struct.pack(
                "<HHBBBB",
                width,
                height,
                header["version"],
                header["format"],
                header["flags"],
                header["type"],
            )
        )
        handle.write(payload)
    validate_tex_layout(path)
    levels = 1
    while width > 1 or height > 1:
        width = max(1, width // 2)
        height = max(1, height // 2)
        levels += 1
    return levels


def main():
    args = parse_args()
    import bpy

    image = bpy.data.images.load(os.path.abspath(args.image), check_existing=False)
    image.colorspace_settings.name = "Non-Color"
    width, height = map(int, image.size)
    if width != height or width & (width - 1):
        raise ValueError("TEX input must be a square power-of-two image")
    pixels = np.empty(width * height * 4, dtype=np.float32)
    image.pixels.foreach_get(pixels)
    # Blender exposes image rows bottom-up; TEX/DDS blocks are stored top-down.
    rgba = np.flipud(
        np.clip(np.rint(pixels.reshape(height, width, 4) * 255.0), 0, 255).astype(np.uint8)
    ).copy()
    levels = []
    current = rgba
    while True:
        levels.append({"width": current.shape[1], "height": current.shape[0], "data": encode_bc1(current)})
        if current.shape[:2] == (1, 1):
            break
        current = downsample(current)

    output_path = os.path.abspath(args.out)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "wb") as handle:
        handle.write(b"TEX\0")
        handle.write(struct.pack("<HHBBBB", width, height, 1, 0x0A, 0, 1))
        for level in levels:
            handle.write(level["data"])
    validate_tex_layout(output_path)
    report = {
        "status": "PASSED",
        "source": os.path.abspath(args.image),
        "source_sha256": sha256_file(args.image),
        "output": output_path,
        "output_sha256": sha256_file(output_path),
        "width": width,
        "height": height,
        "format": "BC1",
        "mip_levels": len(levels),
        "mips": [
            {"width": level["width"], "height": level["height"], "bytes": len(level["data"])}
            for level in levels
        ],
        "size": os.path.getsize(output_path),
    }
    report_path = os.path.abspath(args.report)
    os.makedirs(os.path.dirname(report_path), exist_ok=True)
    with open(report_path, "w", encoding="utf-8") as handle:
        json.dump(report, handle, indent=2)
        handle.write("\n")
    print(
        f"TEX_ENCODE=PASSED SIZE={width}x{height} MIPS={len(levels)} "
        f"SHA256={report['output_sha256']}"
    )


if __name__ == "__main__":
    main()
