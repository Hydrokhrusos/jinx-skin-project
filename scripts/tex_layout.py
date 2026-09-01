import struct


def tex_block_size(format_code):
    if format_code == 0x0A:
        return 8
    if format_code == 0x0C:
        return 16
    raise ValueError(f"Unsupported TEX format code 0x{format_code:02x}")


def tex_mip_level_sizes(width, height, format_code):
    block_size = tex_block_size(format_code)
    sizes = []
    while True:
        sizes.append(
            max(1, (width + 3) // 4)
            * max(1, (height + 3) // 4)
            * block_size
        )
        if width == 1 and height == 1:
            return sizes
        width = max(1, width // 2)
        height = max(1, height // 2)


def expected_tex_payload_size(width, height, format_code):
    return sum(tex_mip_level_sizes(width, height, format_code))


def dds_payload_to_tex_payload(payload, width, height, format_code):
    """Convert standard largest-first DDS mips to Riot's smallest-first order."""
    sizes = tex_mip_level_sizes(width, height, format_code)
    if len(payload) != sum(sizes):
        raise ValueError(
            f"DDS mip payload mismatch: expected {sum(sizes)}, got {len(payload)}"
        )
    levels = []
    offset = 0
    for size in sizes:
        levels.append(payload[offset : offset + size])
        offset += size
    return b"".join(reversed(levels))


def validate_tex_layout(path):
    with open(path, "rb") as handle:
        data = handle.read()
    if len(data) < 12 or data[:4] != b"TEX\0":
        raise ValueError(f"Invalid TEX header: {path}")
    width, height = struct.unpack_from("<HH", data, 4)
    format_code = data[9]
    expected_size = 12 + expected_tex_payload_size(width, height, format_code)
    if len(data) != expected_size:
        raise ValueError(
            f"Invalid TEX payload size for format 0x{format_code:02x}: "
            f"expected {expected_size}, got {len(data)} ({path})"
        )
    return {
        "width": width,
        "height": height,
        "format_code": format_code,
        "format": "BC1" if format_code == 0x0A else "BC3",
        "bytes": len(data),
    }
