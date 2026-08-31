# Abyssal Siren Jinx 3.0.1 manual visual review

Reviewed on 2026-08-31 from the exact SKN, SKL, and TEX files extracted from the reconstructed LTK overlay under `build/abyssal/validation/overlay`.

## Accepted checks

- The front, three-quarter, left, right, and back renders show a substantially new silhouette: coral crown, open rib armor, shell mantle, long Jinx hair anchors, and two oversized coral-relic weapons. It does not read as the Ocean Song model with small deformations.
- The face and crown close-up keeps Jinx recognizable and the face unobstructed. Source-aware grading preserves facial features, hair strands, cloth panels, pale trim, and small accessories instead of flattening them under a single procedural color.
- `WitchBody`, `CoralArmor`, `PowPow`, `Fishbones`, and `Zapper` are visibly distinct. The authored armor separates coral pink, aged bone, abyssal violet, and seafoam into intentional UV regions, while the donor weapon atlas retains its engraved metal, coral, and sea-glass detail. `Recall` is hidden in normal renders and appears in the stock recall pose only.
- The decoded production TEX files match the authored top-level images without mip tiles, stripes, alpha corruption, transparent holograms, stretched full-model projections, or untextured squares. The texture build also checks value range, local detail, color-family coverage, and material-tile separation after BC compression.
- The stock minigun idle, rocket idle, spell-2 Zapper pose, and recall pose show intact shoulders, elbows, wrists, and hands. No obvious native-arm collapse or detached weapon was observed.
- The Chompers shell familiar retains the donor shell's panel and trim detail. The authored leviathan missile separates its dark body, aged-bone head, coral horns, and seafoam spines. The manual Chompers jaw pose separates cleanly without tearing.
- The VFX atlas contact sheet contains shaped grayscale/color masks rather than placeholder solid squares. The build audit confirms all 319 stock particle-card TEX files are preserved byte-for-byte while color behavior is changed in the 117 VFX systems.

## Reviewed images

- `build/abyssal/qa/model/sea_witch_model_contact_sheet.png`
- `build/abyssal/qa/model/model_face_crown_closeup.png`
- `build/abyssal/qa/model/model_coral_relic_weapons_closeup.png`
- `build/abyssal/qa/model/model_stock_minigun_idle_f017.png`
- `build/abyssal/qa/model/model_stock_rocket_idle_f018.png`
- `build/abyssal/qa/model/model_stock_zapper_spell2_f022.png`
- `build/abyssal/qa/model/model_stock_recall_f162.png`
- `build/abyssal/qa/model/model_chompers_manual_jaw_test.png`
- `build/abyssal/qa/model/model_leviathan_missile_three_quarter.png`
- `reports/generated/sea_witch_vfx_contact_sheet.png`

## Remaining live check

Offline rendering cannot prove League's live material, VFX timing, audio mix, or gameplay state transitions. A Practice Tool smoke test remains required for Q weapon switching, attacks, W, E, R, recall, death, dance/taunt/joke, and audible SFX levels.
