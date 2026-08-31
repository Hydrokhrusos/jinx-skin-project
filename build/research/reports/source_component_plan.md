# Abyssal Siren Jinx source and component audit

Date: 2026-08-31  
Target: Ocean Song Jinx slot 65 runtime, using the native skin65 skeleton and animations  
Production submesh contract: `WitchBody`, `CoralArmor`, `PowPow`, `Fishbones`, `Recall`  
Geometry constraint: retain no Ocean Song skin65 vertices; skin65 remains only the runtime skeleton, influence, animation, and visibility authority.

## Recommended final construction

The strongest original hybrid is:

| Output | Primary source geometry | Secondary source geometry | Required original work |
|---|---|---|---|
| `WitchBody` | Cafe Cuties Jinx skin51 face, anatomy, hands, legs, and rigged hair foundations | T1 Jinx skin62 selected hair islands and 486-vertex `Crown`; the head-area hat component from Bewitching Nami skin32 | Delete every maid/food identifier; rebuild an asymmetric short sea-witch coat, split overskirt, hood/hat transition, kelp braids, and a coral-themed Pistol/Zapper. Pack all retained islands into the new body atlas. |
| `CoralArmor` | Selected Coven Nami skin51 `Armor` plates | Small horn/collar/wing-tip shards from Coven Morgana skin26 | Recut, rescale, simplify, and manually reweight into a crown, high carapace collar, one asymmetric shoulder fin, forearm cuff, and hip plates. It must not retain Nami's tail silhouette or Morgana's wing silhouette. |
| `PowPow` | T1 Jinx skin62 minigun inner chassis, drum, handles, and animation-bearing barrel cores | Coven Nami armor/staff fragments as shell motifs | Replace the T1 outer shell with a nautilus-drum and branching coral barrel cage. Keep the grip and rotating bones exact. Do not include the skin62 minigun VFX card submeshes in the opaque weapon mesh. |
| `Fishbones` | T1 Jinx skin62 rocket inner chassis, handle, and jaw-bearing regions | Coven Nami staff-top fins plus a small Bewitching Nami staff-face fragment | Replace the T1 outer silhouette with an anglerfish/coral maw. Preserve the top/bottom mouth split and handle position; rebuild teeth, eyes, fins, and coral branches into one coherent shell. |
| `Recall` | Fragments of Coven Nami's `Tentacle_Prop` | A few Coven Morgana feather/wing-tip shards | Rearrange into five original coral/tentacle arcs and weight them to `recall_wave1` through `recall_wave5`. Do not port either original recall prop wholesale. |

This keeps Jinx recognizable through her face, wiry proportions, twin long hair masses, manic expression, and two oversized Q weapons, while replacing the visible Ocean Song model completely.

## Compatibility findings

### Target skin65 influence palette

The target SKL contains 106 joints but exposes 72 joints in its SKN influence palette.

- Body and clothing: `Root`, `Spine1`, `Spine2`, `Spine3`, `Neck`, `Head`, `Jaw`, `Tooth`, `Pelvis`, both `Clavicle`, `Shoulder`, `Elbow`, `Hand`, `Hip`, `KneeLower`, `Foot`, `Toe`, `Index1/2`, `Middle1/2`, `Thumb1/2`, `eyeLow`, and `mouth` joints.
- Hair: `Hair_Bank_Front1`, `Hair_Bank_Front2`, and `L_Hair1` through `L_Hair6` plus `R_Hair1` through `R_Hair6`.
- Weapons: `Pistol`; `Minigun_Space`, `Minigun_Ammo_Drum`, `Minigun_Tank`, and `Minigun_Barrel1/2/3`; `Rocket_Launcher`, `Rocket_Launcher_Front`, `Rocket_Launcher_End`, and `Rocket_Launcher_Mouth_Top/Bottom`.
- Recall: `recall_wave1` through `recall_wave5`.

The target joint list contains `Minigun`, `Minigun_Body`, both minigun handle locators, both minigun straps, and `Rocket_Launcher_Handle`, but those names are not in the 72-entry influence palette.

### Cafe Cuties Jinx skin51

- `Body`: 12,049 vertices / 17,308 triangles.
- Every weighted joint in `Body` is present in the target's 72-entry influence palette.
- Bind-pose comparison to skin65 is effectively identical: maximum common-joint translation delta 0.000989 model units, rotation delta 0 degrees, and scale delta 0.000001.
- The source atlas is `jinx_skin51_main_tx_cm.tex`, 1024x1024 BC1.

This is the safest anatomical and facial foundation. The complete skin51 `Body` must not be used unchanged because it would read immediately as Cafe Cuties. Keep selected anatomical/hair regions, delete the maid silhouette, and rebuild the outfit.

Do not use skin51 `Emote` or `Recall`; both depend entirely on joints absent from skin65.

### T1 Jinx skin62 body and crown

- `Body`: 13,652 vertices / 21,336 triangles; all weighted names exist in target, but `Minigun_Strap_Back/Front` are outside the target influence palette. Those are stowed-weapon regions and should be excluded from the character extraction.
- `Crown`: 486 vertices / 700 triangles; 100% target influence-palette compatibility and negligible bind-pose delta.
- Body atlas: `jinx_skin62_tx_cm.tex`, 1024x1024 BC1; body mask: 256x256 BC1.

The crown is a good low-risk coral/hat frame. Selected hair islands are useful, but the complete T1 body should not be ported.

### T1 Jinx skin62 weapon

- `Weapon`: 9,853 vertices / 9,560 triangles.
- Dominant-bone split gives 4,700 PowPow-family vertices and 5,153 Fishbones-family vertices.
- All 12 weighted joint names exist in skin65's 106-joint list.
- Ten of the 12 are in skin65's influence palette. The missing two are `Minigun_Handle_Front` and `Rocket_Launcher_Handle`.
- Recommended palette-safe remaps are `Minigun_Handle_Front -> Minigun_Space` and `Rocket_Launcher_Handle -> Rocket_Launcher_Front`. These are the semantically closest available rigid frames. Do not use the generic ancestor fallback, which maps the minigun handle to `Pelvis`.
- `Rocket_Launcher_Mouth_Top` and `Rocket_Launcher_Mouth_Bottom` have a donor-to-target global bind-origin delta of `[0, 0.83501, 2.49599]`, magnitude 2.63196. Apply `target_global * inverse(donor_global)` to those bone-local pieces, or subtract that translation vector before exporting.
- Weapon atlas: `jinx_skin62_weapon_tx_cm.tex`, 512x512 BC3; mask: 256x256 BC3.

The source also contains 660 minigun VFX-card vertices and 3,449 rocket VFX-card vertices. Those should remain out of the opaque SKN shells; runtime particle work should supply the glow.

The T1 inner weapon framework is highly compatible, but retaining the complete outer weapon model would be another whole-skin port. Keep grips, pivots, drum/barrel cores, and jaw-bearing pieces; replace the exterior silhouette.

### Coven Nami skin51

| Submesh | Vertices | Triangles | Direct target-joint coverage | Use |
|---|---:|---:|---:|---|
| `Hair` | 1,508 | 2,404 | 50.0% | Small front/tentacle locks, manually reweighted to `Head` and Jinx hair chains |
| `Armor` | 3,870 | 5,104 | 23.1% | Horn, shoulder, and hip plate fragments only |
| `Ult_Armor` | 766 | 868 | 25.0% | Mask/collar shard reference; do not port the full form |
| `Body` | 4,539 | 7,060 | 36.5% | Proportion and surface-language reference, not a donor body |
| `Weapon` | 543 | 752 | 0% | Rigid decorative fragments after full transform/reweight |
| `Staff_Top_Ult` | 250 | 354 | 0% | Fishbones fin/muzzle motif |
| `Top_Staff_Norm` | 148 | 222 | 0% | Fishbones fin/muzzle motif |
| `Tentacle_Prop` | 3,456 | 6,720 | 0% | Recall fragments, reweighted to the five skin65 wave bones |

Useful atlases are:

- `nami_skin51_armor_tx_cm.tex`: 1024x1024 BC1.
- `nami_skin51_body_tx_cm.tex`: 1024x1024 BC1.
- `nami_skin51_hair_tx_cm.tex`: 512x512 BC1.
- `nami_skin51_weapon_tx_cm.tex`: 512x512 BC1.
- `nami_skin51_tentacle_prop_tx_cm.tex`: 256x256 BC3.
- `nami_skin51_armor_scolling_mat.tex`: 256x256 BC3.

These are reference/bake sources, not runtime materials. The scrolling, iridescent, and alpha material behavior must not be copied into the final champion materials.

### Bewitching Nami skin32

- `Body`: 11,576 vertices / 18,654 triangles; direct target-joint coverage 44.3%.
- `Weapon`: 2,392 vertices / 4,006 triangles; no direct target weapon-joint compatibility.
- Main atlas: `nami_skin32_tx_cm.tex`, 1024x1024 BC1.

The useful regions are the witch-hat/head component and a small expressive staff-head fragment. Both require component separation, placement, and new weights. The body, tail, and whole staff are unsuitable as direct ports.

### Deep Sea Nami skin07

- Single submesh: 3,499 vertices / 5,626 triangles.
- Direct target-joint coverage 44.6%.
- Main atlas: `nami_skin07_tx_cm.tex`; the separate `nami_skin07_tx_gm.tex` supplies a secondary material map.

This old, low-density model is best used for fin, horn, and collar shape language and for dark teal/purple color reference. It is not a suitable direct body donor beside the newer Jinx topology.

### Coven Morgana skin26

- 17,926 vertices / 21,952 triangles on a 233-joint skeleton.
- Overall direct target-joint coverage is only 16.7%.
- `Body`: 3,591 vertices; direct target-joint coverage 33.3%.
- Wing submeshes rely almost entirely on Morgana-specific wing and skirt chains.
- `morgana_skin26_tx_cm.tex` and `morgana_skin26_wings_tx_cm.tex` are 1024x1024 BC1; gold fresnel masks are also 1024x1024 BC1.

Only isolated horn/collar/feather-tip shapes are practical. Reposition and rigidly weight them to Jinx `Head`, `Spine3`, `Clavicle`, or `Pelvis`. The full body, dress, wings, owl, and recall cannot be directly retargeted without importing an unjustified skeleton.

## Texture and material plan

Every retained component currently points into a different donor atlas. Reassigning those UVs to one recolored texture will scramble the surface even if the SKN itself is valid. The final model needs a real atlas consolidation:

1. Import each donor with its correct source texture.
2. Cut, reshape, and align the chosen components while retaining donor material slots temporarily.
3. Join geometry by the five production outputs.
4. Create non-overlapping UV islands in the custom `seawitch_body`, `seawitch_armor`, `seawitch_weapon`, and `seawitch_recall` atlases.
5. Bake source color and hand-painted detail into those new atlases, then repaint them into one palette.
6. Use opaque texture-only materials for the champion and weapon shells. Any emissive mask should not enable whole-mesh alpha blending.

Recommended unified palette and surface language:

- abyss navy and kelp teal for the large cloth/hair masses;
- bruised violet for shadowed transitions;
- coral rose/magenta for branching hard growths;
- bone ivory for teeth, shell rims, and a few face-framing accents;
- restrained bioluminescent cyan for eyes, runes, and weapon cores;
- little or no warm gold.

Avoid Ocean Song holographic purple, Cafe Cuties food/pastel cues, T1 white-gold heraldry, Nami's mermaid-tail silhouette, and Morgana's red-black wing silhouette. Those cues would expose the source pieces instead of forming a coherent skin.

## Pistol/Zapper requirement

The five agreed names do not inherently guarantee a replacement for Jinx's `Pistol`-weighted Zapper geometry. Include a new coral-relic Zapper inside `WitchBody` and pack its UVs into the body atlas, or add an explicitly routed always-visible weapon submesh. Do not place it inside a Q-toggled submesh unless visibility tests prove it remains available for W in both Q states.

## External visual references

- Riot's [Origins: Jinx](https://nexus.leagueoflegends.com/en-us/2017/04/origins-jinx/) identifies the stable Jinx read: wiry body against oversized weapons, floor-length pigtails, and a manic expression. Those should survive the theme change.
- [Ocean's Embrace](https://sketchfab.com/3d-models/oceans-embrace-dae-weaponcraft-d93eaf43ef274883afbbd7e54b0c2bfd) is a 14.4k-triangle coral/deep-sea weapon reference. Use its layered coral-to-crystal hierarchy as reference, not as a direct port.
- [Dark Waters Samira](https://heleneslodowski.artstation.com/projects/g8gzPK) is useful for readable tentacle weapons and outward-facing creature eyes. Its strongest lesson is keeping the weapon silhouette readable under organic decoration.
- [Thallasomancy](https://gradshow.artcenter.edu/project/hideko-carnahan/thallasomancy) separates reef, kelp, abyss, and graveyard motifs into distinct sea-witch identities. For this skin, combine reef hard shapes with abyss lighting; do not mix every ocean motif equally.
- The [marine-creature rifle study](https://www.zbrushcentral.com/t/weapons-rifles-fanart-wayfinder/460764) is a useful reference for barnacle/coral growth placed over a legible mechanical gun core.

## Required visual acceptance before packaging

Do not declare this build finished from WAD, SKN, TEX, or overlay validation alone.

1. Render the final exported SKN using the exact final TEX files and the same opaque/alpha modes routed by the final BIN.
2. Save front, back, left, and right model screenshots plus close-ups of the face, PowPow, Fishbones, and Zapper.
3. Render PowPow-only and Fishbones-only visibility states and confirm the inactive Q weapon behaves as intended.
4. Render one posed or animated grip frame for each Q weapon and one W/Zapper frame.
5. Render the hidden and visible `Recall` states separately.
6. Compare the screenshots side-by-side with Cafe Cuties Jinx, T1 Jinx, Coven Nami, and Ocean Song Jinx. The final must not read as any one donor with a recolor.
7. Treat the package as a candidate until the user has seen the screenshots and approved the visual result.

## Research artifacts

- Machine-readable component, joint, influence-palette, bind-pose, UV, and texture audit: `build/research/source_component_audit.json`.
- Jinx candidate renders: `build/research/candidate_renders/`.
- Nami reference renders: `build/research/nami_renders/`.
- Coven Morgana reference renders: `build/research/morgana_renders/`.
- Research-only audit script: `build/research/audit_source_components.py`.
