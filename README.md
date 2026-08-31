# Abyssal Siren Jinx

Version 3.0.0

Abyssal Siren Jinx is a development baseline for a complete model, texture, VFX, and SFX replacement for Ocean Song Jinx (skin 65). The installable package is `dist/abyssal-siren-jinx_3.0.0.modpkg`.

Version 3.0.0 replaces the 2.x asset direction with a new cute-horror sea-witch design. The champion no longer uses Ocean Song's character geometry: Jinx's anatomy, face, and hair begin with the compatible skin-51 foundation; Pow-Pow and Fishbones begin with skin-62 weapon cores; and extensive authored coral, shell, crown, armor, and relic geometry creates the final silhouette. Bespoke opaque atlases replace the previous translucent and holographic material treatment.

The final material pass preserves the donor atlases' face, cloth, trim, hair, metal, and relic detail through source-aware grading instead of covering them with procedural overlays. Authored geometry uses dedicated coral, aged-bone, abyssal-violet, and seafoam texture regions with separate value ranges and guarded UV gutters. Generated TEX files are round-tripped through the production decoder and rejected if mip ordering, alpha, top-level imagery, color-family coverage, or material separation changes during BC compression.

## Replaced assets

- The champion model and materials, including explicit WitchBody, CoralArmor, Pow-Pow, Fishbones, Zapper, and recall submeshes.
- Chompers and the ultimate missile, each with a dedicated model and opaque texture treatment.
- All 117 routed VFX systems, rethemed through 2,977 audited color vectors in a black-violet, coral, and seafoam palette.
- All 60 skin-65 SFX events and all 63 referenced media files, rebuilt from dark-witch donor material. Voice-over is not changed.

The 319 working Riot particle-card textures are preserved byte-for-byte. Their alpha masks, compression, mipmaps, and inactive texels are part of how League renders the effects; changing those bitmaps caused the square artifacts in earlier builds. The VFX systems, colors, material routing, models, and effect meshes are still rethemed around those known-good cards.

Stock Ocean Song animations are retained in 3.0.0. The custom model is bound to the native 106-joint skin-65 skeleton and is checked in stock minigun-idle, rocket-idle, Zapper, and recall poses.

## Known issues

- The ultimate (R) cast has minor visual bugs that still need correction.

See [references/sources.md](references/sources.md) for component and audio provenance.

## Install

1. Remove or disable every earlier Abyssal Siren package, including the Encore and 2.x builds.
2. Add `abyssal-siren-jinx_3.0.0.modpkg` to LTK Manager.
3. Disable other mods that replace Ocean Song Jinx or `Jinx.wad.client`.
4. Enable this package, patch the game, and select Ocean Song Jinx without a chroma for the first test.

The authored BIN replacement targets skin 65. Ocean Song chromas share some base assets and are not the validation target for this release.

## Build and validation

Run:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/build.ps1
```

The build reads authoritative assets from the installed League WAD, constructs the hybrid models and opaque textures, patches VFX and audio routing, creates the package, extracts it again, rebuilds and extracts an LTK overlay, and checks hashes, native joint order, vertex weights, TEX payloads, Wwise Vorbis media, event coverage, and routed resources. It also renders the exact exported SKN, SKL, TEX, and stock animation data for visual inspection; those renders are not mockups.

Offline validation and exported-model renders cannot prove that the current League client will play every asset correctly. Before treating the release as live-validated, run a Practice Tool smoke test covering movement, basic attacks in both Q forms, W, E placement and trigger, R flight and impact, passive, recall, death, and audio at normal game volume.
