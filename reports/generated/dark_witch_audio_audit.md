# Abyssal Siren Jinx 3.0.1 — dark-witch SFX audit

Status: **automated audio validation passed; live League playback is not yet confirmed**.

## Scope

- Target: Ocean Song Jinx, skin slot 65, League `16.17.8104348`.
- Replaced both skin-65 SFX banks: `jinx_skin65_sfx_audio.bnk` and `jinx_skin65_sfx_events.bnk`.
- Covered all 60 bank events: 48 Play events and 12 Stop events.
- Replaced all 63 unique media entries used by those events, including basic/critical attacks, Q, W, E, R, passive, death, joke, taunts, dance, recall, respawn, and winddown.
- Patched all 103 Wwise Sound objects that reference those media entries.
- Did not touch voice-over banks or animation/model/VFX assets.

## Donor direction

The curation uses one related dark-fantasy sound language rather than arbitrary clips:

- 16 media from Coven Evelynn skin 24.
- 13 media from Coven Morgana skin 26.
- 34 media from Sunken Shadows Nami skin 68 for abyssal-water movement and spell texture.

The installed skin metadata identifies Morgana and Evelynn as `skinline:coven` and Nami as `skinline:sunkenshadows`. Every selected donor media item is unique. The complete target-event-to-donor mapping, source media IDs, source hashes, semantic roles, decoded measurements, and source event names are recorded in `source/audio/dark_witch/manifest.json`.

## Codec and routing validation

- Source and output bank version: Wwise 145.
- Target audio-bank alignment preserved: 16 bytes.
- Every replacement remains modern Wwise Vorbis (`0xffff`).
- Every Sound object retains plugin ID `0x00040001` and embedded-bank stream type 0.
- Every selected replacement WEM decoded with vgmstream r2117 as `Custom Vorbis` before packing.
- The rebuilt DIDX retains all 63 original target media IDs and ordering.
- Re-extracted output media bytes exactly match the curated replacement bytes.
- Every one of the 60 event routes resolves only to replaced media IDs.
- Repeating the build produced byte-identical audio bank, event bank, and JSON report.

## Timing and audibility checks

- Replacement durations range from 0.367 to 9.872 seconds.
- Donor-to-target duration ratios are 0.663–1.973; role and duration matching prevents short weapon transients from receiving long ambience clips.
- The average absolute donor/target RMS difference is 1.84 dB.
- 48 of 63 replacements are within 3 dB of the original media RMS; 62 of 63 are within 6 dB.
- The single 8.43 dB outlier is one of two media routed by the passive-kill event, not a standalone attack/ability event.
- All decoded outputs contain non-zero audio. Decoded RMS spans -27.656 to -9.150 dBFS and peak level spans -10.281 to 0 dBFS.

These measurements reduce the risk of the previous silent/too-quiet result but do not substitute for listening in League, where event/container gains and the game mix apply.

## Output identity

- SFX audio BNK SHA-256: `810bdbd7791f77011ebba80ed1199a1adb74a3336e757c90eab1107d74ae0acf`
- SFX events BNK SHA-256: `87bbc6d9232db3ab760eff4343785d182104876aeb5d04b5c39fbed1413530b3`
- Curated manifest SHA-256: `3ffaaf9999782ff55f76efb8ce963df66210a859f417b62ac4bb4152ce0db8c8`
- Detailed validation report SHA-256: `37c4e44192e108a9a5015d86a879553a99923e61fc4676637bd3fcb49319fe13`

## Remaining acceptance test

After the complete 3.0.1 package is assembled, perform a Practice Tool smoke test with basic attacks in both Q states, W cast/travel/hit, E cast/arm/snare/expire, R cast/travel/hit, passive activation, death, recall, and respawn. Confirm both audibility and subjective fit against the final VFX/model. Package, codec, routing, and decode checks alone cannot prove live playback.
