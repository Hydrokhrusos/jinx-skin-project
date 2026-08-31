import argparse
import collections
import hashlib
import json
import math
import re
import shutil
import struct
import subprocess
import sys
import wave
from array import array
from pathlib import Path


PROJECT_VERSION = "3.0.0"
BANK_VERSION = 145
VORBIS_PLUGIN_ID = 0x00040001
MANIFEST_SCHEMA = 1


def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()


def sha256_file(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def fnv1_32(name):
    value = 2166136261
    for byte in name.lower().encode("utf-8"):
        value = ((value * 16777619) & 0xFFFFFFFF) ^ byte
    return value


def u32(data, offset):
    return struct.unpack_from("<I", data, offset)[0]


def set_u32(data, offset, value):
    struct.pack_into("<I", data, offset, value)


def chunk_bytes(tag, payload):
    return tag + struct.pack("<I", len(payload)) + payload


def parse_chunks(data):
    chunks = []
    offset = 0
    while offset < len(data):
        if offset + 8 > len(data):
            raise ValueError(f"Truncated BNK chunk header at {offset}")
        tag = data[offset : offset + 4]
        size = u32(data, offset + 4)
        end = offset + 8 + size
        if end > len(data):
            raise ValueError(f"Truncated {tag!r} BNK chunk at {offset}")
        chunks.append({"tag": tag, "payload": data[offset + 8 : end], "offset": offset})
        offset = end
    return chunks


def find_chunk(chunks, tag):
    matches = [chunk for chunk in chunks if chunk["tag"] == tag]
    if len(matches) != 1:
        raise ValueError(f"Expected one {tag!r} chunk, found {len(matches)}")
    return matches[0]


def bank_version(chunks):
    bkhd = find_chunk(chunks, b"BKHD")["payload"]
    if len(bkhd) < 16:
        raise ValueError("Truncated BKHD chunk")
    return u32(bkhd, 0)


def parse_audio_entries(bank_data):
    chunks = parse_chunks(bank_data)
    version = bank_version(chunks)
    if version != BANK_VERSION:
        raise ValueError(f"Expected Wwise bank version {BANK_VERSION}, got {version}")
    bkhd = find_chunk(chunks, b"BKHD")["payload"]
    didx = find_chunk(chunks, b"DIDX")["payload"]
    data = find_chunk(chunks, b"DATA")["payload"]
    if len(didx) % 12:
        raise ValueError("DIDX size is not a multiple of 12")
    alignment = u32(bkhd, 12) & 0xFFFF
    if alignment <= 0 or alignment > 4096 or alignment & (alignment - 1):
        raise ValueError(f"Invalid bank alignment {alignment}")
    entries = []
    seen = set()
    for offset in range(0, len(didx), 12):
        media_id, data_offset, size = struct.unpack_from("<III", didx, offset)
        if media_id in seen:
            raise ValueError(f"Duplicate media ID {media_id}")
        if data_offset + size > len(data):
            raise ValueError(f"Media {media_id} exceeds DATA chunk")
        seen.add(media_id)
        entries.append(
            {
                "id": media_id,
                "offset": data_offset,
                "size": size,
                "data": data[data_offset : data_offset + size],
            }
        )
    return chunks, entries, alignment


def inspect_wwise_vorbis_wem(data, label):
    if len(data) < 12 or data[:4] != b"RIFF" or data[8:12] != b"WAVE":
        raise ValueError(f"{label} is not RIFF/WAVE")
    if u32(data, 4) + 8 != len(data):
        raise ValueError(f"{label} has an invalid RIFF size")
    chunks = {}
    offset = 12
    while offset < len(data):
        if offset + 8 > len(data):
            raise ValueError(f"Truncated WEM chunk header in {label}")
        tag = data[offset : offset + 4]
        size = u32(data, offset + 4)
        end = offset + 8 + size
        if end > len(data):
            raise ValueError(f"Truncated WEM chunk {tag!r} in {label}")
        chunks[tag] = data[offset + 8 : end]
        # Wwise commonly omits the optional pad byte after an odd-sized final
        # data chunk even though intermediate RIFF chunks remain word-aligned.
        offset = end if end == len(data) else end + (size & 1)
    if offset != len(data) or b"fmt " not in chunks or b"data" not in chunks:
        raise ValueError(f"Malformed WEM chunks in {label}")
    fmt = chunks[b"fmt "]
    if len(fmt) < 8 or struct.unpack_from("<H", fmt, 0)[0] != 0xFFFF:
        raise ValueError(f"{label} is not Wwise Vorbis")
    return {
        "riff_bytes": len(data),
        "format_tag": "0xffff",
        "channels": struct.unpack_from("<H", fmt, 2)[0],
        "sample_rate": u32(fmt, 4),
        "fmt_bytes": len(fmt),
        "data_bytes": len(chunks[b"data"]),
        "hash_chunk_present": b"hash" in chunks,
    }


def run_checked(command, label):
    completed = subprocess.run(command, capture_output=True, text=True, errors="replace")
    output = "\n".join(
        value.strip() for value in (completed.stdout, completed.stderr) if value.strip()
    )
    if completed.returncode:
        raise ValueError(f"{label} failed with exit code {completed.returncode}: {output}")
    return output


def decoded_features(wav_path):
    with wave.open(str(wav_path), "rb") as decoded:
        channels = decoded.getnchannels()
        sample_width = decoded.getsampwidth()
        sample_rate = decoded.getframerate()
        frame_count = decoded.getnframes()
        compression = decoded.getcomptype()
        frames = decoded.readframes(frame_count)
    if sample_width != 2 or compression != "NONE" or channels < 1:
        raise ValueError(
            f"Unexpected decoded WAV format in {wav_path}: "
            f"{channels}ch/{sample_width * 8}-bit/{compression}"
        )
    samples = array("h")
    samples.frombytes(frames)
    if not samples:
        raise ValueError(f"Decoded WEM is silent/empty: {wav_path}")
    sum_squares = sum(int(sample) * int(sample) for sample in samples)
    rms = math.sqrt(sum_squares / len(samples))
    peak = max(abs(int(sample)) for sample in samples)
    if peak == 0 or rms == 0:
        raise ValueError(f"Decoded WEM contains only zero samples: {wav_path}")
    mono = []
    if channels == 1:
        mono = samples
    else:
        for index in range(0, len(samples), channels):
            mono.append(sum(int(samples[index + channel]) for channel in range(channels)) // channels)
    crossings = 0
    previous = mono[0]
    for sample in mono[1:]:
        if (previous < 0 <= sample) or (previous >= 0 > sample):
            crossings += 1
        previous = sample
    return {
        "channels": channels,
        "sample_width": sample_width,
        "sample_rate": sample_rate,
        "frames": frame_count,
        "duration_seconds": round(frame_count / sample_rate, 6),
        "rms_dbfs": round(20.0 * math.log10(rms / 32767.0), 3),
        "peak_dbfs": round(20.0 * math.log10(peak / 32767.0), 3),
        "zero_crossing_rate": round(crossings / max(1, len(mono) - 1), 6),
    }


def decode_wem(vgmstream, data, wem_path, wav_path, label):
    wem_path.parent.mkdir(parents=True, exist_ok=True)
    wav_path.parent.mkdir(parents=True, exist_ok=True)
    wem_path.write_bytes(data)
    output = run_checked(
        [str(vgmstream), "-i", "-o", str(wav_path), str(wem_path)],
        f"vgmstream decode for {label}",
    )
    if "encoding: Custom Vorbis" not in output:
        raise ValueError(f"vgmstream did not identify {label} as Custom Vorbis: {output}")
    return {**decoded_features(wav_path), "decoder_identified": "Custom Vorbis"}


def parse_hirc_objects(hirc):
    if len(hirc) < 4:
        raise ValueError("Truncated HIRC chunk")
    count = u32(hirc, 0)
    objects = []
    offset = 4
    for index in range(count):
        if offset + 5 > len(hirc):
            raise ValueError(f"Truncated HIRC object {index}")
        object_type = hirc[offset]
        size = u32(hirc, offset + 1)
        payload_offset = offset + 5
        end = payload_offset + size
        if end > len(hirc) or size < 4:
            raise ValueError(f"Invalid HIRC object {index}")
        objects.append(
            {
                "index": index,
                "type": object_type,
                "offset": offset,
                "payload_offset": payload_offset,
                "size": size,
                "id": u32(hirc, payload_offset),
            }
        )
        offset = end
    if offset != len(hirc):
        raise ValueError(f"HIRC object table leaves {len(hirc) - offset} trailing bytes")
    return objects


def patch_events_bank(bank_data, media_sizes):
    chunks = parse_chunks(bank_data)
    if bank_version(chunks) != BANK_VERSION:
        raise ValueError(f"Expected Wwise event bank version {BANK_VERSION}")
    hirc_chunk = find_chunk(chunks, b"HIRC")
    hirc = bytearray(hirc_chunk["payload"])
    objects = parse_hirc_objects(hirc)
    references = collections.Counter()
    patched = []
    sound_objects = [item for item in objects if item["type"] == 2]
    for item in sound_objects:
        if item["size"] < 22:
            raise ValueError(f"Unexpectedly short sound object {item['id']}")
        payload = item["payload_offset"]
        plugin_id = u32(hirc, payload + 4)
        stream_type = hirc[payload + 8]
        media_id = u32(hirc, payload + 9)
        old_size = u32(hirc, payload + 13)
        if media_id not in media_sizes:
            raise ValueError(
                f"Sound object {item['id']} references media {media_id}, which is not replaced"
            )
        if plugin_id != VORBIS_PLUGIN_ID or stream_type != 0:
            raise ValueError(
                f"Target sound object {item['id']} has unexpected plugin/stream "
                f"0x{plugin_id:08x}/{stream_type}"
            )
        new_size = media_sizes[media_id]
        set_u32(hirc, payload + 13, new_size)
        references[media_id] += 1
        patched.append(
            {
                "object_id": item["id"],
                "media_id": media_id,
                "plugin_id": f"0x{plugin_id:08x}",
                "old_media_size": old_size,
                "new_media_size": new_size,
            }
        )
    if set(references) != set(media_sizes):
        missing = sorted(set(media_sizes) - set(references))
        raise ValueError(f"Replacement media are unreferenced in event bank: {missing}")
    output = bytearray()
    for chunk in chunks:
        payload = bytes(hirc) if chunk["tag"] == b"HIRC" else chunk["payload"]
        output.extend(chunk_bytes(chunk["tag"], payload))
    return bytes(output), patched, dict(sorted(references.items())), len(objects)


def rebuild_audio_bank(bank_data, replacements):
    chunks, entries, alignment = parse_audio_entries(bank_data)
    entry_ids = {entry["id"] for entry in entries}
    if entry_ids != set(replacements):
        missing = sorted(entry_ids - set(replacements))
        extra = sorted(set(replacements) - entry_ids)
        raise ValueError(f"Full-bank replacement mismatch: missing={missing}, extra={extra}")
    data_payload = bytearray()
    didx_payload = bytearray()
    changed = []
    for entry in entries:
        padding = (-len(data_payload)) % alignment
        data_payload.extend(b"\0" * padding)
        data_offset = len(data_payload)
        media = replacements[entry["id"]]
        data_payload.extend(media)
        didx_payload.extend(struct.pack("<III", entry["id"], data_offset, len(media)))
        old_sha = sha256_bytes(entry["data"])
        new_sha = sha256_bytes(media)
        if old_sha == new_sha:
            raise ValueError(f"Media {entry['id']} did not actually change")
        changed.append(
            {
                "media_id": entry["id"],
                "old_bytes": entry["size"],
                "new_bytes": len(media),
                "old_sha256": old_sha,
                "new_sha256": new_sha,
            }
        )
    output = bytearray()
    for chunk in chunks:
        payload = chunk["payload"]
        if chunk["tag"] == b"DIDX":
            payload = bytes(didx_payload)
        elif chunk["tag"] == b"DATA":
            payload = bytes(data_payload)
        output.extend(chunk_bytes(chunk["tag"], payload))
    _, output_entries, output_alignment = parse_audio_entries(bytes(output))
    if output_alignment != alignment or [item["id"] for item in output_entries] != [
        item["id"] for item in entries
    ]:
        raise ValueError("Rebuilt audio bank changed its index structure")
    for output_entry in output_entries:
        if output_entry["data"] != replacements[output_entry["id"]]:
            raise ValueError(f"Rebuilt bank media mismatch for {output_entry['id']}")
    return bytes(output), changed, alignment


def parse_wwiser_dump(path):
    text = Path(path).read_text(encoding="utf-8")
    starts = list(re.finditer(r"(?m)^\s+obj  (CAk[^\n]+)\n", text))
    objects = {}
    for index, match in enumerate(starts):
        end = starts[index + 1].start() if index + 1 < len(starts) else len(text)
        block = text[match.start() : end]
        type_match = re.search(r"eHircType = 0x([0-9A-Fa-f]+) \[([^\]]+)\]", block)
        id_match = re.search(r"\bsid\s+ulID = (\d+)", block)
        if not type_match or not id_match:
            continue
        object_id = int(id_match.group(1))
        item = {
            "id": object_id,
            "type": int(type_match.group(1), 16),
            "label": type_match.group(2),
            "actions": [int(value) for value in re.findall(r"ulActionID = (\d+)", block)],
            "children": [int(value) for value in re.findall(r"ulChildID = (\d+)", block)],
        }
        for key, pattern in (
            ("parent", r"DirectParentID = (\d+)"),
            ("source", r"sourceID = (\d+)"),
            ("ext", r"idExt = (\d+)"),
        ):
            value = re.search(pattern, block)
            item[key] = int(value.group(1)) if value else None
        objects[object_id] = item
    return objects


def event_routes(dump_path, metadata_path):
    objects = parse_wwiser_dump(dump_path)
    names = set(
        re.findall(
            r'"((?:Play|Stop)_sfx_[^"]+)"',
            Path(metadata_path).read_text(encoding="utf-8"),
        )
    )
    names_by_id = {fnv1_32(name): name for name in names}
    parents = collections.defaultdict(list)
    for item in objects.values():
        if item["parent"]:
            parents[item["parent"]].append(item["id"])

    def media_for_root(root_id):
        media = set()
        stack = [root_id]
        seen = set()
        while stack:
            object_id = stack.pop()
            if object_id in seen:
                continue
            seen.add(object_id)
            item = objects.get(object_id)
            if not item:
                continue
            if item["source"]:
                media.add(item["source"])
            stack.extend(item["children"])
            stack.extend(parents.get(object_id, []))
        return media

    routes = {}
    unknown = []
    for event in [item for item in objects.values() if item["type"] == 4]:
        name = names_by_id.get(event["id"])
        if not name:
            unknown.append(event["id"])
            name = str(event["id"])
        media = set()
        for action_id in event["actions"]:
            action = objects.get(action_id)
            if action and action["ext"]:
                media.update(media_for_root(action["ext"]))
        routes[name] = sorted(media)
    return {
        "routes": dict(sorted(routes.items())),
        "event_count": len(routes),
        "play_event_count": sum(name.startswith("Play_") for name in routes),
        "stop_event_count": sum(name.startswith("Stop_") for name in routes),
        "media_ids": sorted({media_id for media in routes.values() for media_id in media}),
        "sound_object_count": sum(item["type"] == 2 for item in objects.values()),
        "hirc_object_count": len(objects),
        "unknown_event_ids": unknown,
    }


def classify_event(name):
    value = name.lower()
    if any(token in value for token in ("dance", "joke", "laugh", "taunt", "idle")):
        return "emote"
    if "death" in value:
        return "death"
    if any(token in value for token in ("recall", "respawn", "winddown", "homeguard")):
        return "transition"
    if any(token in value for token in ("passive", "stealth", "icon")):
        return "buff"

    def phase(prefix):
        if any(token in value for token in ("hit", "detonate", "snare", "deactivate")):
            return f"{prefix}_impact"
        if any(token in value for token in ("missile", "boosterlaunch", "loop")):
            return f"{prefix}_projectile"
        if any(token in value for token in ("activate", "mark", "buff")):
            return f"{prefix}_buff"
        return f"{prefix}_cast"

    if "basicattack" in value or "critattack" in value or "jinxqattack" in value:
        return phase("attack")
    if "jinxr_" in value or "morganar_" in value or "namir_" in value or "evelynnr_" in value:
        return phase("ultimate")
    if "jinxe" in value or "emine" in value:
        return phase("trap")
    if any(token in value for token in ("jinxw", "morganaq", "morganaw", "morganae", "namiq", "namiw", "namie", "evelynnq", "evelynnw", "evelynne")):
        return phase("spell")
    return phase("spell")


ROLE_COMPATIBILITY = {
    "attack_cast": ["attack_cast", "spell_cast"],
    "attack_projectile": ["attack_projectile", "spell_projectile"],
    "attack_impact": ["attack_impact", "spell_impact"],
    "attack_buff": ["buff", "spell_buff", "attack_cast"],
    "spell_cast": ["spell_cast", "attack_cast", "trap_cast"],
    "spell_projectile": ["spell_projectile", "attack_projectile", "trap_projectile"],
    "spell_impact": ["spell_impact", "attack_impact", "trap_impact"],
    "spell_buff": ["spell_buff", "buff", "trap_buff"],
    "trap_cast": ["spell_cast", "trap_cast", "buff"],
    "trap_projectile": ["spell_projectile", "trap_projectile", "buff"],
    "trap_impact": ["spell_impact", "trap_impact", "attack_impact"],
    "trap_buff": ["buff", "spell_buff", "trap_buff", "emote"],
    "ultimate_cast": ["ultimate_cast", "spell_cast"],
    "ultimate_projectile": ["ultimate_projectile", "spell_projectile"],
    "ultimate_impact": ["ultimate_impact", "spell_impact"],
    "ultimate_buff": ["ultimate_buff", "spell_buff", "buff"],
    "buff": ["buff", "spell_buff", "trap_buff", "emote"],
    "emote": ["emote", "transition", "buff"],
    "death": ["death", "transition", "emote"],
    "transition": ["transition", "emote", "buff", "death"],
}


def media_roles(routes):
    roles = collections.defaultdict(set)
    events = collections.defaultdict(set)
    for name, media_ids in routes.items():
        if not name.startswith("Play_"):
            continue
        role = classify_event(name)
        for media_id in media_ids:
            roles[media_id].add(role)
            events[media_id].add(name)
    return roles, events


def role_penalty(target_roles, donor_roles):
    best = 12.0
    for target_role in target_roles:
        compatible = ROLE_COMPATIBILITY.get(target_role, [target_role])
        for donor_role in donor_roles:
            if donor_role in compatible:
                best = min(best, compatible.index(donor_role) * 1.25)
            elif donor_role.split("_", 1)[-1] == target_role.split("_", 1)[-1]:
                best = min(best, 3.5)
    return best


def mapping_cost(target, donor):
    duration_ratio = max(target["features"]["duration_seconds"], 0.01) / max(
        donor["features"]["duration_seconds"], 0.01
    )
    duration_cost = abs(math.log(duration_ratio)) * 3.0
    # The donor HIRC gain hierarchy is not ported, so favor media whose
    # integrated level is already close to the original Jinx clip. This keeps
    # the preserved Jinx event/container mix audible and avoids surprise jumps.
    rms_cost = abs(target["features"]["rms_dbfs"] - donor["features"]["rms_dbfs"]) * 0.35
    zcr_cost = abs(
        target["features"]["zero_crossing_rate"] - donor["features"]["zero_crossing_rate"]
    ) * 3.0
    channels_cost = 0.2 if target["features"]["channels"] != donor["features"]["channels"] else 0.0
    family_cost = 0.0
    primary = sorted(target["roles"])[0]
    if primary.startswith("attack") and donor["label"] == "sunken_shadows_nami":
        family_cost = 0.35
    elif primary in ("emote", "transition") and donor["label"] == "coven_evelynn":
        family_cost = 0.25
    return (
        role_penalty(target["roles"], donor["roles"])
        + duration_cost
        + rms_cost
        + zcr_cost
        + channels_cost
        + family_cost
    )


def parse_donor_arg(values):
    label, audio_bank, dump, metadata = values
    return {
        "label": label,
        "audio_bank": Path(audio_bank),
        "dump": Path(dump),
        "metadata": Path(metadata),
    }


def curate(args):
    target_audio_path = Path(args.target_audio)
    target_audio_data = target_audio_path.read_bytes()
    _, target_entries, _ = parse_audio_entries(target_audio_data)
    target_route_info = event_routes(args.target_dump, args.target_metadata)
    target_ids = {entry["id"] for entry in target_entries}
    if set(target_route_info["media_ids"]) != target_ids:
        raise ValueError("Target route media do not exactly cover the target SFX audio bank")
    if target_route_info["unknown_event_ids"]:
        raise ValueError(f"Unresolved target events: {target_route_info['unknown_event_ids']}")
    target_roles, target_events = media_roles(target_route_info["routes"])

    work_dir = Path(args.work_dir)
    clips_dir = Path(args.clips_dir)
    work_dir.mkdir(parents=True, exist_ok=True)
    clips_dir.mkdir(parents=True, exist_ok=True)
    vgmstream = Path(args.vgmstream)

    targets = []
    for entry in target_entries:
        media_id = entry["id"]
        fmt = inspect_wwise_vorbis_wem(entry["data"], f"target media {media_id}")
        features = decode_wem(
            vgmstream,
            entry["data"],
            work_dir / "target_wem" / f"{media_id}.wem",
            work_dir / "target_wav" / f"{media_id}.wav",
            f"target media {media_id}",
        )
        targets.append(
            {
                "id": media_id,
                "data": entry["data"],
                "sha256": sha256_bytes(entry["data"]),
                "format": fmt,
                "features": features,
                "roles": target_roles[media_id] or {"spell_cast"},
                "events": target_events[media_id],
            }
        )

    donors = []
    donor_sources = []
    for raw_spec in args.donor:
        spec = parse_donor_arg(raw_spec)
        bank_data = spec["audio_bank"].read_bytes()
        _, entries, _ = parse_audio_entries(bank_data)
        route_info = event_routes(spec["dump"], spec["metadata"])
        route_ids = set(route_info["media_ids"])
        entry_ids = {entry["id"] for entry in entries}
        if not route_ids.issubset(entry_ids):
            raise ValueError(
                f"{spec['label']} routes reference absent embedded media: {sorted(route_ids-entry_ids)}"
            )
        roles, events = media_roles(route_info["routes"])
        usable_count = 0
        skipped_prefetch = []
        for entry in entries:
            media_id = entry["id"]
            if media_id not in roles:
                continue
            try:
                fmt = inspect_wwise_vorbis_wem(
                    entry["data"], f"{spec['label']} media {media_id}"
                )
            except ValueError as error:
                # Banks paired with a WPK may embed only the initial prefetch
                # bytes. They retain the full RIFF size but are not standalone
                # donor media, so exclude them from the curated pool.
                if "invalid RIFF size" in str(error):
                    skipped_prefetch.append(media_id)
                    continue
                raise
            features = decode_wem(
                vgmstream,
                entry["data"],
                work_dir / "donor_wem" / spec["label"] / f"{media_id}.wem",
                work_dir / "donor_wav" / spec["label"] / f"{media_id}.wav",
                f"{spec['label']} media {media_id}",
            )
            donors.append(
                {
                    "id": media_id,
                    "label": spec["label"],
                    "data": entry["data"],
                    "sha256": sha256_bytes(entry["data"]),
                    "format": fmt,
                    "features": features,
                    "roles": roles[media_id],
                    "events": events[media_id],
                }
            )
            usable_count += 1
        donor_sources.append(
            {
                "label": spec["label"],
                "audio_bank": spec["audio_bank"].name,
                "audio_bank_sha256": sha256_bytes(bank_data),
                "event_count": route_info["event_count"],
                "embedded_media_count": len(entries),
                "routed_embedded_media_count": len(route_ids),
                "usable_standalone_media_count": usable_count,
                "skipped_prefetch_media": sorted(skipped_prefetch),
            }
        )

    if len(donors) < len(targets):
        raise ValueError(f"Not enough unique donor media: {len(donors)} for {len(targets)} targets")
    unused = {(item["label"], item["id"]): item for item in donors}
    replacements = []
    # Constrain the most timing-sensitive clips first.
    targets.sort(key=lambda item: (len(item["roles"]), item["features"]["duration_seconds"], item["id"]))
    for target in targets:
        candidates = list(unused.values())
        target_duration = target["features"]["duration_seconds"]
        timing_candidates = [
            item
            for item in candidates
            if 0.45 <= item["features"]["duration_seconds"] / max(target_duration, 0.01) <= 2.2
        ]
        if timing_candidates:
            candidates = timing_candidates
        selected = min(candidates, key=lambda item: (mapping_cost(target, item), item["label"], item["id"]))
        unused.pop((selected["label"], selected["id"]))
        clip_name = f"{target['id']}.wem"
        (clips_dir / clip_name).write_bytes(selected["data"])
        replacements.append(
            {
                "target_media_id": target["id"],
                "source_file": clip_name,
                "source_sha256": selected["sha256"],
                "donor": selected["label"],
                "donor_media_id": selected["id"],
                "target_roles": sorted(target["roles"]),
                "donor_roles": sorted(selected["roles"]),
                "target_events": sorted(target["events"]),
                "donor_events": sorted(selected["events"]),
                "target_features": target["features"],
                "donor_features": selected["features"],
                "mapping_cost": round(mapping_cost(target, selected), 6),
            }
        )

    manifest = {
        "schema_version": MANIFEST_SCHEMA,
        "project_version": PROJECT_VERSION,
        "theme": "dark witchcraft with abyssal water, occult attacks, and Coven spell impacts",
        "source_policy": "locally installed League SFX banks only; no voice-over media",
        "target": {
            "champion": "Jinx",
            "skin_slot": 65,
            "source_audio_bank": target_audio_path.name,
            "source_audio_bank_sha256": sha256_bytes(target_audio_data),
            "source_events_bank": Path(args.target_events).name,
            "source_events_bank_sha256": sha256_file(args.target_events),
            "bank_version": BANK_VERSION,
            "media_count": len(target_entries),
            **target_route_info,
        },
        "donors": donor_sources,
        "replacements": sorted(replacements, key=lambda item: item["target_media_id"]),
        "coverage": {
            "all_target_media_replaced": len(replacements) == len(target_entries),
            "all_target_events_routed": not target_route_info["unknown_event_ids"],
            "unique_donor_media": len({(item["donor"], item["donor_media_id"]) for item in replacements}),
            "voice_over_included": False,
        },
    }
    manifest_path = Path(args.manifest)
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(
        f"AUDIO_CURATION=PASSED TARGET_MEDIA={len(target_entries)} "
        f"DONOR_MEDIA={len(donors)} SELECTED={len(replacements)}"
    )


def build(args):
    manifest_path = Path(args.manifest)
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("schema_version") != MANIFEST_SCHEMA:
        raise ValueError(f"Unsupported manifest schema: {manifest.get('schema_version')}")
    if manifest.get("project_version") != PROJECT_VERSION:
        raise ValueError(f"Manifest is not for project {PROJECT_VERSION}")
    target_audio_path = Path(args.target_audio)
    target_events_path = Path(args.target_events)
    target_audio_data = target_audio_path.read_bytes()
    target_events_data = target_events_path.read_bytes()
    expected = manifest["target"]
    if sha256_bytes(target_audio_data) != expected["source_audio_bank_sha256"]:
        raise ValueError("Target SFX audio bank checksum does not match the curated 16.17 source")
    if sha256_bytes(target_events_data) != expected["source_events_bank_sha256"]:
        raise ValueError("Target SFX events bank checksum does not match the curated 16.17 source")
    _, entries, _ = parse_audio_entries(target_audio_data)
    if len(entries) != expected["media_count"]:
        raise ValueError("Target media count changed")
    clips_dir = Path(args.clips_dir)
    replacements = {}
    manifest_by_id = {}
    decoded = []
    decoded_dir = Path(args.decoded_dir)
    vgmstream = Path(args.vgmstream)
    for item in manifest["replacements"]:
        media_id = item["target_media_id"]
        if media_id in replacements:
            raise ValueError(f"Duplicate replacement mapping for media {media_id}")
        clip_path = clips_dir / item["source_file"]
        data = clip_path.read_bytes()
        if sha256_bytes(data) != item["source_sha256"]:
            raise ValueError(f"Curated donor clip checksum mismatch: {clip_path}")
        wem_format = inspect_wwise_vorbis_wem(data, f"replacement media {media_id}")
        features = decode_wem(
            vgmstream,
            data,
            decoded_dir / "wem" / f"{media_id}.wem",
            decoded_dir / "wav" / f"{media_id}.wav",
            f"replacement media {media_id}",
        )
        replacements[media_id] = data
        manifest_by_id[media_id] = item
        decoded.append(
            {
                "media_id": media_id,
                "donor": item["donor"],
                "donor_media_id": item["donor_media_id"],
                "source_sha256": item["source_sha256"],
                "wem_format": wem_format,
                "decoded_validation": features,
            }
        )
    output_audio, changed, alignment = rebuild_audio_bank(target_audio_data, replacements)
    media_sizes = {media_id: len(data) for media_id, data in replacements.items()}
    output_events, patched_objects, references, hirc_object_count = patch_events_bank(
        target_events_data, media_sizes
    )
    if len(patched_objects) != expected["sound_object_count"]:
        raise ValueError(
            f"Expected {expected['sound_object_count']} patched sound objects, got {len(patched_objects)}"
        )
    replacement_ids = set(replacements)
    for name, event_media in expected["routes"].items():
        if not set(event_media).issubset(replacement_ids):
            raise ValueError(f"Event route is not fully replaced: {name}")

    out_audio = Path(args.out_audio)
    out_events = Path(args.out_events)
    out_audio.parent.mkdir(parents=True, exist_ok=True)
    out_events.parent.mkdir(parents=True, exist_ok=True)
    out_audio.write_bytes(output_audio)
    out_events.write_bytes(output_events)
    report = {
        "status": "PASSED",
        "project_version": PROJECT_VERSION,
        "target": {
            "champion": "Jinx",
            "skin_slot": 65,
            "bank_version": BANK_VERSION,
            "audio_bank_alignment": alignment,
            "event_count": expected["event_count"],
            "play_event_count": expected["play_event_count"],
            "stop_event_count": expected["stop_event_count"],
            "media_count": len(entries),
            "sound_object_count": len(patched_objects),
            "hirc_object_count": hirc_object_count,
        },
        "coverage": {
            "all_sfx_bank_media_replaced": len(changed) == len(entries),
            "unique_replaced_media": len(changed),
            "all_60_sfx_events_route_only_to_replaced_media": True,
            "patched_sound_objects": len(patched_objects),
            "native_wwise_vorbis_plugin_preserved": all(
                item["plugin_id"] == "0x00040001" for item in patched_objects
            ),
            "every_replacement_decodes_with_vgmstream": len(decoded) == len(entries),
            "non_target_sfx_media_remaining": 0,
            "voice_over_changed": False,
            "live_league_playback_tested": False,
        },
        "donor_usage": dict(
            sorted(collections.Counter(item["donor"] for item in manifest["replacements"]).items())
        ),
        "event_routes": expected["routes"],
        "media_reference_counts": {str(key): value for key, value in references.items()},
        "changed_media": changed,
        "decoded_replacements": decoded,
        "mapping": manifest["replacements"],
        "banks": {
            "audio": {
                "source_bytes": len(target_audio_data),
                "output_bytes": len(output_audio),
                "source_sha256": sha256_bytes(target_audio_data),
                "output_sha256": sha256_bytes(output_audio),
            },
            "events": {
                "source_bytes": len(target_events_data),
                "output_bytes": len(output_events),
                "source_sha256": sha256_bytes(target_events_data),
                "output_sha256": sha256_bytes(output_events),
            },
        },
        "limitations": [
            "Automated checks prove bank structure, routing, codec, and decode integrity only.",
            "Live League playback and subjective mix levels still require an in-game smoke test.",
        ],
    }
    report_path = Path(args.report)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(
        f"DARK_WITCH_AUDIO=PASSED EVENTS={expected['event_count']} MEDIA={len(changed)} "
        f"SOUND_OBJECTS={len(patched_objects)}"
    )


def make_parser():
    parser = argparse.ArgumentParser(
        description="Curate and build the complete Abyssal Siren Jinx dark-witch SFX bank."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    curate_parser = subparsers.add_parser("curate")
    curate_parser.add_argument("--target-audio", required=True)
    curate_parser.add_argument("--target-events", required=True)
    curate_parser.add_argument("--target-dump", required=True)
    curate_parser.add_argument("--target-metadata", required=True)
    curate_parser.add_argument(
        "--donor",
        action="append",
        nargs=4,
        metavar=("LABEL", "AUDIO_BANK", "WWISER_DUMP", "SKIN_METADATA"),
        required=True,
    )
    curate_parser.add_argument("--vgmstream", required=True)
    curate_parser.add_argument("--work-dir", required=True)
    curate_parser.add_argument("--clips-dir", required=True)
    curate_parser.add_argument("--manifest", required=True)
    curate_parser.set_defaults(func=curate)

    build_parser = subparsers.add_parser("build")
    build_parser.add_argument("--target-audio", required=True)
    build_parser.add_argument("--target-events", required=True)
    build_parser.add_argument("--manifest", required=True)
    build_parser.add_argument("--clips-dir", required=True)
    build_parser.add_argument("--vgmstream", required=True)
    build_parser.add_argument("--decoded-dir", required=True)
    build_parser.add_argument("--out-audio", required=True)
    build_parser.add_argument("--out-events", required=True)
    build_parser.add_argument("--report", required=True)
    build_parser.set_defaults(func=build)
    return parser


def main():
    args = make_parser().parse_args()
    args.func(args)


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"DARK_WITCH_AUDIO=FAILED ERROR={error}", file=sys.stderr)
        raise
