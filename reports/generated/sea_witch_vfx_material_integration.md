# Sea-witch material and VFX integration

Status: offline material/VFX audit passed. Live League rendering is not yet verified.

## Required model contract

The production SKN must expose exactly these material-routed submeshes:

- `WitchBody`
- `CoralArmor`
- `PowPow`
- `Fishbones`
- `Zapper`
- `Recall`

The production texture outputs must exist at:

- `assets/characters/jinx/skins/skin65/jinx_skin65_seawitch_body_tx_cm.tex`
- `assets/characters/jinx/skins/skin65/jinx_skin65_seawitch_armor_tx_cm.tex`
- `assets/characters/jinx/skins/skin65/jinx_skin65_seawitch_weapon_tx_cm.tex`
- `assets/characters/jinx/skins/skin65/jinx_skin65_seawitch_recall_tx_cm.tex`

Ritobin resolves those paths to `0x64f95bcb8dd8c990`, `0x2489c105d2f3a54e`,
`0x595c3a5442cd34ca`, and `0x1fc0564f1f8fb66f`, respectively.

## Material behavior

`patch_abyssal_bins.py` removes the active Ocean Song `Material: link` from
`SkinMeshProperties` and replaces the old Body/Hair/Skirt/Weapon/WeaponVFX routes
with texture-only routes for the six production submeshes. These routes use the
standard opaque SkinMesh path. The custom `Recall` submesh remains hidden by
default. Ocean Song's four alpha-blended static material definitions remain in the
BIN as unreferenced data and cannot affect the champion mesh.

JinxMine routes the new `ShellFamiliars` submesh explicitly to
`assets/characters/jinxmine/skins/skin65/jinxmine_skin65_tx_cm.tex` (ritobin hash
`0x502c280e70de722e`) through the standard opaque SkinMesh path, with self
illumination `0.25` and brush alpha override `1.0`. The route contains no custom
material link and assumes the production model audit confirms zero retained Ocean
Song vertices.

## VFX behavior

All 117 Skin65 renderable systems are covered across the Jinx skin BIN and linked
multi-skin BIN. The patch changes 2,977 `ValueColor` vectors to the selected
black-violet/coral/seafoam palette. It also validates all ten JinxMine/Chomper
resolver keys against concrete VFX definitions in the linked BIN.

Particle-card TEX files are deliberately not recompressed or recolored. The audit
requires every card to retain its source bytes, byte size, TEX header, BC format,
dimensions, mip payload, and alpha. Theme color comes from the BIN tint curves.
This is the square-artifact safeguard.

## Build integration

The 3.0.0 `build.ps1` pipeline constructs the model and opaque atlases first,
then calls `build_abyssal_vfx_assets.py` and `patch_abyssal_bins.py`. This order
keeps the authored missile assets while copying its native skeleton and validates
the required material contract before packaging.

## Offline evidence

- `sea_witch_vfx_material_audit.json`: opaque routes, palette distribution, full
  VFX corpus accounting, and Chomper resolver coverage.
- `sea_witch_vfx_asset_audit.json`: 360 dependencies, 319 byte-identical
  particle-card TEX files, native TEX header/size checks, and output-derived
  contact-sheet metadata.
- `sea_witch_vfx_contact_sheet.png`: decoded from
  packaged TEX outputs; it does not synthesize recolors or simulate BIN tinting.
- Jinx, JinxMine, and linked multi-skin patched text compile with ritobin. Jinx
  round-trips with zero active material links in `SkinMeshProperties`; JinxMine
  round-trips with the explicit opaque `ShellFamiliars` route intact.

## Required live smoke test

Before release, inspect spawn/idle/recall, both Q weapon states and basic attacks,
W cast/missile/hit, all E mine states and explosion, and R missile/explosion. Reject
the build for any translucent champion surface, full-card square, missing particle,
stock cyan/gold spell family, unresolved Chomper state, or Recall mesh visible
outside its intended state.
