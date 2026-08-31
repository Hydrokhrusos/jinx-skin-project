import struct


def tex_block_size(format_code):
    if format_code == 0x0A:
        return 8
    if format_code == 0x0C:
        return 16
    raise ValueError(f"Unsupported TEX format code 0x{format_code:02x}")


def expected_tex_payload_size(width, height, format_code):
    block_size = tex_block_size(format_code)
    total = 0
    while True:
        total += max(1, (width + 3) // 4) * max(1, (height + 3) // 4) * block_size
        if width == 1 and height == 1:
            return total
        width = max(1, width // 2)
        height = max(1, height // 2)


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
