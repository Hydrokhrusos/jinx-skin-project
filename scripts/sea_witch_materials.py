MATERIAL_TILES = {
    "coral": (0.0, 0.0, 0.5, 0.5),
    "bone": (0.5, 0.0, 1.0, 0.5),
    "abyssal": (0.0, 0.5, 0.5, 1.0),
    "seafoam": (0.5, 0.5, 1.0, 1.0),
}

# Keep synthetic UVs away from tile boundaries so BC compression and mipmaps
# cannot bleed an adjacent material onto narrow horns and ribbons.
UV_GUTTER = 0.018


def material_uv_region(material):
    if material not in MATERIAL_TILES:
        raise ValueError(f"Unknown sea-witch material: {material}")
    u0, v0, u1, v1 = MATERIAL_TILES[material]
    return (
        u0 + UV_GUTTER,
        v0 + UV_GUTTER,
        u1 - UV_GUTTER,
        v1 - UV_GUTTER,
    )


def remap_material_uvs(uvs, material):
    u0, v0, u1, v1 = material_uv_region(material)
    return [
        (u0 + float(u) * (u1 - u0), v0 + float(v) * (v1 - v0))
        for u, v in uvs
    ]
