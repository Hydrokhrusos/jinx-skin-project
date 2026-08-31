import argparse
import hashlib
import json
import math
import os
import re
import shutil
import struct
import sys
import tempfile

import bpy
import numpy as np


ASSET_PATTERN = re.compile(
    r'"(ASSETS/[^"\r\n]+\.(?:tex|dds|scb|skn|skl))"', re.IGNORECASE
)
TECHNICAL_TOKENS = (
    "mask",
    "noise",
    "erod",
    "distort",
    "alpha",
    "normal",
    "mult",
    "gradient",
    "ramp",
    "hold",
)
VFX_MESH_DIFFUSE_BASENAMES = {
    "jinx_skin65_r_mis_globefish.tex",
}


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--bin", action="append", required=True)
    parser.add_argument("--source-root", required=True)
    parser.add_argument("--generated-root", required=True)
    parser.add_argument("--out-root", required=True)
    parser.add_argument("--addon-root", required=True)
    parser.add_argument("--texconv", required=True)
    parser.add_argument("--map-out", required=True)
    parser.add_argument("--report", required=True)
    parser.add_argument("--preview-dir", required=True)
    argv = sys.argv[sys.argv.index("--") + 1 :] if "--" in sys.argv else sys.argv[1:]
    return parser.parse_args(argv)


def sha256_file(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


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
            f"Expected BC1/BC3 VFX texture, got format 0x{texture_format:02x}: {path}"
        )
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
            handle.write(tex_to_dds_bytes(path))
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


def abyssal_grade(rgba, filename):
    rgb = rgba[..., :3].astype(np.float32) / 255.0
    alpha = rgba[..., 3:4]
    maximum = rgb.max(axis=2, keepdims=True)
    luminance = (
        rgb[..., 0:1] * 0.2126 + rgb[..., 1:2] * 0.7152 + rgb[..., 2:3] * 0.0722
    )
    if any(token in filename.lower() for token in TECHNICAL_TOKENS):
        return rgba.copy()
    energy = np.clip(maximum * 0.78 + luminance * 0.22, 0.0, 1.0)
    total = rgb.sum(axis=2, keepdims=True) + 1e-5
    saturation = (maximum - rgb.min(axis=2, keepdims=True)) / np.maximum(maximum, 1e-5)
    coral_weight = np.maximum(0.0, rgb[..., 0:1] * 1.30 - rgb[..., 1:2] * 0.48 - rgb[..., 2:3] * 0.16)
    seafoam_weight = np.maximum(0.0, rgb[..., 1:2] * 1.20 + rgb[..., 2:3] * 0.65 - rgb[..., 0:1] * 0.30)
    violet_weight = np.maximum(0.0, rgb[..., 2:3] * 0.68 + rgb[..., 0:1] * 0.34 - rgb[..., 1:2] * 0.40)
    desaturated = saturation < 0.12
    coral_weight += np.where(desaturated, total * 0.10, 0.0)
    seafoam_weight += np.where(desaturated, total * 0.65, 0.0)
    violet_weight += np.where(desaturated, total * 0.25, 0.0)
    weight_total = coral_weight + seafoam_weight + violet_weight + 1e-5
    coral = np.array([1.000, 0.165, 0.275], dtype=np.float32)
    seafoam = np.array([0.155, 1.000, 0.705], dtype=np.float32)
    witch_violet = np.array([0.305, 0.020, 0.505], dtype=np.float32)
    black_violet = np.array([0.010, 0.004, 0.028], dtype=np.float32)
    accent = (
        coral * (coral_weight / weight_total)
        + seafoam * (seafoam_weight / weight_total)
        + witch_violet * (violet_weight / weight_total)
    )
    strength = np.clip(energy * (0.58 + saturation * 0.48), 0.08, 1.0)
    target = black_violet * (1.0 - strength) + accent * strength
    result = np.clip(np.rint(target * 255.0), 0, 255).astype(np.uint8)
    # Particle cards depend on exact black/near-black texels remaining inactive.
    # Recolor only authored energy; never turn the empty card background blue.
    inactive = np.max(rgba[..., :3], axis=2) <= 3
    result[inactive] = rgba[..., :3][inactive]
    return np.concatenate((result, alpha), axis=2)


def transform_scb(source, output):
    data = bytearray(open(source, "rb").read())
    if data[:8] != b"r3d2Mesh":
        raise ValueError(f"Invalid SCB signature: {source}")
    major, minor = struct.unpack_from("<HH", data, 8)
    vertex_count, _, _ = struct.unpack_from("<III", data, 140)
    vertex_offset = 176 + (4 if (major, minor) == (3, 2) else 0)
    positions = [struct.unpack_from("<3f", data, vertex_offset + index * 12) for index in range(vertex_count)]
    if not positions:
        raise ValueError(f"SCB has no vertices: {source}")
    center = tuple(sum(position[axis] for position in positions) / len(positions) for axis in range(3))
    output_positions = []
    for index, position in enumerate(positions):
        relative = [position[axis] - center[axis] for axis in range(3)]
        phase = index * 0.173 + relative[1] * 0.021
        transformed = (
            center[0] + relative[0] * 1.13 + math.sin(phase) * relative[2] * 0.045,
            center[1] + relative[1] * 0.91,
            center[2] + relative[2] * 1.18 + math.cos(phase) * relative[0] * 0.035,
        )
        output_positions.append(transformed)
        struct.pack_into("<3f", data, vertex_offset + index * 12, *transformed)
    minimum = tuple(min(position[axis] for position in output_positions) for axis in range(3))
    maximum = tuple(max(position[axis] for position in output_positions) for axis in range(3))
    struct.pack_into("<6f", data, 152, *(minimum + maximum))
    os.makedirs(os.path.dirname(output), exist_ok=True)
    with open(output, "wb") as handle:
        handle.write(data)
    return vertex_count


def grade_rgb565(value):
    red = ((value >> 11) & 0x1F) / 31.0
    green = ((value >> 5) & 0x3F) / 63.0
    blue = (value & 0x1F) / 31.0
    energy = max(red, green, blue)
    total = red + green + blue + 1e-5
    maximum = max(red, green, blue)
    minimum = min(red, green, blue)
    saturation = (maximum - minimum) / max(maximum, 1e-5)
    coral_weight = max(0.0, red * 1.30 - green * 0.48 - blue * 0.16)
    seafoam_weight = max(0.0, green * 1.20 + blue * 0.65 - red * 0.30)
    violet_weight = max(0.0, blue * 0.68 + red * 0.34 - green * 0.40)
    if saturation < 0.12:
        coral_weight += total * 0.10
        seafoam_weight += total * 0.65
        violet_weight += total * 0.25
    weight_total = coral_weight + seafoam_weight + violet_weight + 1e-5
    black_violet = (0.010, 0.004, 0.028)
    coral = (1.000, 0.165, 0.275)
    seafoam = (0.155, 1.000, 0.705)
    witch_violet = (0.305, 0.020, 0.505)
    accent = tuple(
        coral[index] * coral_weight / weight_total
        + seafoam[index] * seafoam_weight / weight_total
        + witch_violet[index] * violet_weight / weight_total
        for index in range(3)
    )
    strength = min(1.0, max(0.08, energy * (0.58 + saturation * 0.48)))
    target = tuple(
        min(
            1.0,
            max(
                0.0,
                black_violet[index] * (1.0 - strength)
                + accent[index] * strength,
            ),
        )
        for index in range(3)
    )
    return (
        int(round(target[0] * 31.0)) << 11
        | int(round(target[1] * 63.0)) << 5
        | int(round(target[2] * 31.0))
    )


def remap_bc1_selectors(selector_bits, four_color):
    output = 0
    for index in range(16):
        selector = (selector_bits >> (index * 2)) & 0x3
        if four_color:
            selector = (1, 0, 3, 2)[selector]
        elif selector < 2:
            selector = 1 - selector
        output |= selector << (index * 2)
    return output


def transform_dds(source, output):
    data = bytearray(open(source, "rb").read())
    if len(data) < 128 or data[:4] != b"DDS ":
        raise ValueError(f"Invalid DDS header: {source}")
    fourcc = bytes(data[84:88])
    if fourcc not in {b"DXT1", b"DXT5"}:
        raise ValueError(f"Unsupported VFX DDS format {fourcc!r}: {source}")
    block_size = 8 if fourcc == b"DXT1" else 16
    payload_size = len(data) - 128
    if payload_size <= 0 or payload_size % block_size:
        raise ValueError(f"Invalid {fourcc.decode()} payload size: {source}")
    block_count = payload_size // block_size
    for index in range(block_count):
        block_offset = 128 + index * block_size
        color_offset = block_offset if fourcc == b"DXT1" else block_offset + 8
        color0, color1, selectors = struct.unpack_from("<HHI", data, color_offset)
        output0 = grade_rgb565(color0)
        output1 = grade_rgb565(color1)
        swapped = False
        if fourcc == b"DXT1":
            four_color = color0 > color1
            if output0 == output1:
                if four_color:
                    output0 = min(0xFFFF, output0 + 1) if output0 < 0xFFFF else output0
                    output1 = max(0, output1 - 1) if output0 == output1 else output1
                else:
                    output1 = min(0xFFFF, output1 + 1) if output1 < 0xFFFF else output1
                    output0 = max(0, output0 - 1) if output0 == output1 else output0
            if (four_color and output0 <= output1) or (not four_color and output0 > output1):
                output0, output1 = output1, output0
                swapped = True
            if swapped:
                selectors = remap_bc1_selectors(selectors, four_color)
        struct.pack_into("<HHI", data, color_offset, output0, output1, selectors)
    os.makedirs(os.path.dirname(output), exist_ok=True)
    with open(output, "wb") as handle:
        handle.write(data)
    return {"format": fourcc.decode("ascii"), "changed_blocks": block_count}


def in_place_destination(source_ref):
    normalized = source_ref.replace("\\", "/")
    if normalized.lower().startswith("assets/shared/"):
        digest = hashlib.sha1(normalized.lower().encode("utf-8")).hexdigest()[:10]
        basename = re.sub(r"[^a-z0-9_.-]+", "_", os.path.basename(normalized).lower())
        relative = f"assets/characters/jinx/skins/skin65/abyssal/vfx/{digest}_{basename}"
        reference = "ASSETS/Characters/Jinx/Skins/Skin65/Abyssal/VFX/" + f"{digest}_{basename}"
        return relative, reference
    return normalized.lower(), normalized


def resize_nearest(image, height, width):
    y = np.linspace(0, image.shape[0] - 1, height).astype(np.int32)
    x = np.linspace(0, image.shape[1] - 1, width).astype(np.int32)
    return image[y][:, x]


def write_preview(candidates, output):
    selected = []
    used = set()
    categories = ("_q_", "_w_", "_e_", "_r_", "idle", "recall", "passive", "dance")
    for category in categories:
        match = next(
            ((path, image) for path, image in candidates if category in path.lower() and path not in used),
            None,
        )
        if match:
            selected.append(match)
            used.add(match[0])
    for item in candidates:
        if len(selected) >= 8:
            break
        if item[0] not in used:
            selected.append(item)
            used.add(item[0])
    if not selected:
        raise ValueError("No VFX textures available for preview")
    tile = 192
    canvas = np.zeros((tile * 2, tile * 4, 4), dtype=np.uint8)
    canvas[..., 3] = 255
    for index, (_, rgba) in enumerate(selected[:8]):
        row, column = divmod(index, 4)
        thumbnail = resize_nearest(rgba, tile, tile)
        alpha = thumbnail[..., 3:4].astype(np.float32) / 255.0
        checker = np.full((tile, tile, 3), 14, dtype=np.float32)
        composed = thumbnail[..., :3].astype(np.float32) * alpha + checker * (1.0 - alpha)
        canvas[row * tile : (row + 1) * tile, column * tile : (column + 1) * tile, :3] = np.clip(
            composed, 0, 255
        ).astype(np.uint8)
    os.makedirs(os.path.dirname(output), exist_ok=True)
    image = bpy.data.images.new("Abyssal_VFX_Contact_Sheet", width=canvas.shape[1], height=canvas.shape[0], alpha=True)
    image.pixels.foreach_set(np.flipud(canvas).astype(np.float32).reshape(-1) / 255.0)
    image.filepath_raw = output
    image.file_format = "PNG"
    image.save()
    bpy.data.images.remove(image)
    return [path for path, _ in selected[:8]]


def main():
    args = parse_args()
    sys.path.insert(0, os.path.abspath(args.addon_root))
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from Aventurine.utils.texture_manager import tex_to_dds_bytes
    from encode_tex import encode_tex_with_texconv, validate_tex_layout

    bin_reports = []
    unique_refs = {}
    for path in args.bin:
        text = open(path, "r", encoding="utf-8").read()
        blocks = extract_blocks(text, "VfxSystemDefinitionData {")
        systems = []
        for block in blocks:
            refs = sorted({match.group(1) for match in ASSET_PATTERN.finditer(block)}, key=str.lower)
            for ref in refs:
                unique_refs.setdefault(ref.lower(), ref)
            particle = re.search(r'ParticleName:\s*string\s*=\s*"([^"]+)"', block)
            object_path = re.search(r"ObjectPath:\s*hash\s*=\s*([^\r\n]+)", block)
            systems.append(
                {
                    "particle": particle.group(1) if particle else "<unnamed>",
                    "object_path": object_path.group(1).strip() if object_path else "<missing>",
                    "asset_references": len(refs),
                    "value_colors": block.count("ValueColor {"),
                }
            )
        if not systems or any(item["object_path"] == "<missing>" for item in systems):
            raise ValueError(f"Incomplete VFX system metadata in {path}")
        bin_reports.append({"path": os.path.abspath(path), "system_count": len(systems), "systems": systems})

    source_root = os.path.abspath(args.source_root)
    generated_root = os.path.abspath(args.generated_root)
    out_root = os.path.abspath(args.out_root)
    mapping = {}
    rows = []
    preview_candidates = []
    for source_ref in sorted(unique_refs.values(), key=str.lower):
        normalized = source_ref.replace("\\", "/").lower()
        source = os.path.join(source_root, *normalized.split("/"))
        generated = os.path.join(generated_root, *normalized.split("/"))
        if not os.path.isfile(source):
            raise FileNotFoundError(f"VFX dependency was not extracted: {source_ref}")
        build_input = generated if os.path.isfile(generated) else source
        destination_relative, destination_ref = in_place_destination(source_ref)
        output = os.path.join(out_root, *destination_relative.split("/"))
        extension = os.path.splitext(normalized)[1]
        details = {}
        same_generated_output = os.path.abspath(build_input) == os.path.abspath(output)
        mesh_diffuse_texture = (
            extension == ".tex"
            and os.path.basename(normalized) in VFX_MESH_DIFFUSE_BASENAMES
        )
        particle_texture = (
            extension == ".tex"
            and "/particles/" in normalized
            and not mesh_diffuse_texture
        )
        technical = particle_texture or mesh_diffuse_texture or extension in {".dds", ".skl"} or any(
            token in os.path.basename(normalized) for token in TECHNICAL_TOKENS
        )
        intended_transform = extension == ".scb" or (
            extension == ".tex" and not technical
        ) or extension == ".skn"
        if same_generated_output:
            details = {"reused_generated_output": True}
            if not os.path.isfile(output):
                raise FileNotFoundError(f"Generated VFX dependency disappeared: {output}")
            if particle_texture:
                validate_tex_layout(output)
                preview_candidates.append(
                    (destination_relative, load_tex(output, tex_to_dds_bytes))
                )
        elif extension == ".tex":
            header = source_header(build_input)
            if technical:
                os.makedirs(os.path.dirname(output), exist_ok=True)
                shutil.copy2(build_input, output)
                validate_tex_layout(output)
                details = {
                    "width": header["width"],
                    "height": header["height"],
                    "format": "BC1" if header["format"] == 0x0A else "BC3",
                    "changed_pixels": 0,
                    "technical_input_preserved": True,
                    "particle_card_preserved": particle_texture,
                    "vfx_mesh_diffuse_preserved": mesh_diffuse_texture,
                    "byte_size_preserved": os.path.getsize(build_input)
                    == os.path.getsize(output),
                    "tex_header_preserved": source_header(build_input)
                    == source_header(output),
                }
                if particle_texture:
                    preview_candidates.append(
                        (destination_relative, load_tex(output, tex_to_dds_bytes))
                    )
            else:
                rgba = load_tex(build_input, tex_to_dds_bytes)
                graded = abyssal_grade(rgba, os.path.basename(normalized))
                changed_pixels = int(np.any(graded[..., :3] != rgba[..., :3], axis=2).sum())
                inactive = np.max(rgba[..., :3], axis=2) <= 3
                inactive_preserved = int(
                    np.all(graded[..., :3][inactive] == rgba[..., :3][inactive], axis=1).sum()
                )
                if inactive_preserved != int(inactive.sum()):
                    raise ValueError(f"VFX card background changed: {source_ref}")
                if changed_pixels == 0 and int(inactive.sum()) == rgba.shape[0] * rgba.shape[1]:
                    os.makedirs(os.path.dirname(output), exist_ok=True)
                    shutil.copy2(build_input, output)
                    validate_tex_layout(output)
                    intended_transform = False
                    details = {
                        "width": int(rgba.shape[1]),
                        "height": int(rgba.shape[0]),
                        "format": "BC1" if header["format"] == 0x0A else "BC3",
                        "changed_pixels": 0,
                        "inactive_pixels": int(inactive.sum()),
                        "inactive_pixels_preserved": inactive_preserved,
                        "compressed_inactive_threshold": 4,
                        "compressed_inactive_pixels_above_threshold": 0,
                        "technical_input_preserved": True,
                        "all_inactive_card_preserved": True,
                    }
                else:
                    if changed_pixels == 0:
                        raise ValueError(f"VFX texture did not change: {source_ref}")
                    mip_levels = encode_tex_with_texconv(
                        graded, output, header, args.texconv, dither=False
                    )
                    encoded = load_tex(output, tex_to_dds_bytes)
                    compressed_inactive = np.max(encoded[..., :3][inactive], axis=1)
                    compressed_inactive_above_threshold = int(
                        (compressed_inactive > 4).sum()
                    )
                    if compressed_inactive_above_threshold:
                        raise ValueError(
                            f"Compressed VFX card background became active: {source_ref} "
                            f"({compressed_inactive_above_threshold} pixels)"
                        )
                    details = {
                        "width": int(rgba.shape[1]),
                        "height": int(rgba.shape[0]),
                        "format": "BC1" if header["format"] == 0x0A else "BC3",
                        "changed_pixels": changed_pixels,
                        "inactive_pixels": int(inactive.sum()),
                        "inactive_pixels_preserved": inactive_preserved,
                        "compressed_inactive_threshold": 4,
                        "compressed_inactive_pixels_above_threshold": compressed_inactive_above_threshold,
                        "technical_input_preserved": False,
                        "mip_levels": mip_levels,
                        "encoder": "Microsoft DirectXTex texconv 2026.5.8",
                    }
                    preview_candidates.append((destination_relative, encoded))
        elif extension == ".scb":
            details = {"changed_vertices": transform_scb(build_input, output)}
        elif extension == ".dds":
            os.makedirs(os.path.dirname(output), exist_ok=True)
            shutil.copy2(build_input, output)
            details = {"passthrough": True, "technical_input_preserved": True}
        else:
            os.makedirs(os.path.dirname(output), exist_ok=True)
            shutil.copy2(build_input, output)
            details = {"passthrough": True}
        source_hash = sha256_file(source)
        output_hash = sha256_file(output)
        if technical and source_hash == output_hash:
            details.setdefault("technical_input_preserved", True)
        if intended_transform and source_hash == output_hash:
            raise ValueError(f"Visible VFX dependency did not change: {source_ref}")
        transform_status = "transformed" if source_hash != output_hash else "preserved"
        mapping[source_ref] = destination_ref
        rows.append(
            {
                "source": source_ref,
                "destination": destination_relative,
                "destination_reference": destination_ref,
                "extension": extension,
                "source_sha256": source_hash,
                "output_sha256": output_hash,
                "status": transform_status,
                **details,
            }
        )

    os.makedirs(os.path.dirname(os.path.abspath(args.map_out)), exist_ok=True)
    with open(args.map_out, "w", encoding="utf-8") as handle:
        json.dump(mapping, handle, indent=2)
        handle.write("\n")
    preview = os.path.abspath(os.path.join(args.preview_dir, "vfx_contact_sheet.png"))
    preview_assets = write_preview(preview_candidates, preview)
    extension_counts = {}
    for row in rows:
        extension_counts[row["extension"]] = extension_counts.get(row["extension"], 0) + 1
    isolated_shared = sum(
        item["source"].replace("\\", "/").lower().startswith("assets/shared/")
        for item in rows
    )
    particle_card_rows = [item for item in rows if item.get("particle_card_preserved")]
    if not particle_card_rows:
        raise ValueError("No particle-card TEX dependencies were audited")
    if not all(
        item["status"] == "preserved"
        and item.get("byte_size_preserved")
        and item.get("tex_header_preserved")
        for item in particle_card_rows
    ):
        raise ValueError("A particle-card TEX changed bytes, size, or native header")
    payload = {
        "status": "PASSED",
        "theme": "cute sea-horror dark sea witch",
        "palette": "black-violet, coral, seafoam",
        "source_bins": bin_reports,
        "vfx_systems": sum(item["system_count"] for item in bin_reports),
        "unique_dependencies": len(rows),
        "dependency_strategy": "in_place_jinx_and_isolated_shared",
        "all_dependencies_routed": len(mapping) == len(rows),
        "transformed_dependencies": sum(item["status"] == "transformed" for item in rows),
        "preserved_dependencies": sum(item["status"] == "preserved" for item in rows),
        "square_safe_texture_recolor": all(
            item.get("inactive_pixels") == item.get("inactive_pixels_preserved")
            and item.get("compressed_inactive_pixels_above_threshold", 0) == 0
            for item in rows
            if item["extension"] == ".tex" and "inactive_pixels" in item
        ),
        "technical_masks_and_noise_preserved": all(
            item["status"] == "preserved"
            for item in rows
            if item.get("technical_input_preserved")
        ),
        "particle_textures_byte_identical": all(
            item["status"] == "preserved"
            for item in particle_card_rows
        ),
        "particle_texture_sizes_preserved": all(
            item.get("byte_size_preserved", False) for item in particle_card_rows
        ),
        "particle_texture_headers_preserved": all(
            item.get("tex_header_preserved", False) for item in particle_card_rows
        ),
        "particle_card_textures_audited": len(particle_card_rows),
        "in_place_dependencies": len(rows) - isolated_shared,
        "isolated_shared_dependencies": isolated_shared,
        "new_wad_entries": isolated_shared,
        "extension_counts": extension_counts,
        "assets": rows,
        "preview": {
            "path": preview,
            "sha256": sha256_file(preview),
            "assets": preview_assets,
            "source": "decoded packaged TEX outputs; no synthetic preview recolor",
        },
    }
    os.makedirs(os.path.dirname(os.path.abspath(args.report)), exist_ok=True)
    with open(args.report, "w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2)
        handle.write("\n")
    print(
        f"ABYSSAL_VFX_ASSETS=PASSED SYSTEMS={payload['vfx_systems']} "
        f"DEPENDENCIES={len(rows)} TRANSFORMED={payload['transformed_dependencies']} "
        f"TEX={extension_counts.get('.tex', 0)} "
        f"SCB={extension_counts.get('.scb', 0)}"
    )


if __name__ == "__main__":
    try:
        main()
    except Exception:
        import traceback

        traceback.print_exc()
        sys.exit(1)
