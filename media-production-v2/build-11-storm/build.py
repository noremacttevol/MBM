#!/usr/bin/env python3
"""Assemble Story #11 V2 — Calming the Storm (Mark 4:35-41).

This is a pictures-only rebuild.  The authoritative V1 final remains the audio
source: its AAC stream is copied packet-for-packet into the V2 MP4.  The local
V2 audio folder is deliberately ignored because it contains an older,
non-authoritative narration pass.

The old generic V2 extractor trims trailing silence from every narration file.
Story 11's approved V1 build did not: it used each complete MP3 duration.  That
difference is about eight seconds, so this story-specific assembler reproduces
the actual V1 timeline from the complete canonical MP3s before placing the 34
new pictures.  Mid-segment picture changes use the canonical V1 timing JSON.

Output: mark-4_calming-the-storm.mp4, 1080x1920 H.264 30 fps, <25 MB.
"""

import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import textwrap

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
V1 = os.path.join(ROOT, "media-production", "build-11-storm")
ASSETS = os.path.join(HERE, "assets-realistic")
SEGS = os.path.join(HERE, "segs-v2")
LOCKED_FINAL = os.path.join(V1, "mark-4_calming-the-storm.mp4")
OUT = os.path.join(HERE, "mark-4_calming-the-storm-realistic-v3.mp4")

FF = shutil.which("ffmpeg") or "ffmpeg"
FPROBE = shutil.which("ffprobe") or "ffprobe"
FPS = 30
LEAD = 0.28
GAP = 0.72
KJV_GAP = 1.15
TAIL = 1.5
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
CREAM = "0xF7F2E9"
INK = "0x3B2A1E"
CARD_TEXT = (
    "The same Jesus is in your boat. Bring him your storm — and let him "
    "speak his peace."
)

BASE_ENC = [
    "-c:v", "libx264", "-preset", "medium", "-crf", "16",
    "-pix_fmt", "yuv420p", "-r", str(FPS), "-an",
]


def run(cmd):
    print(">>", " ".join(str(c) for c in cmd)[:180], flush=True)
    subprocess.run(cmd, check=True)


def duration_of(path):
    probe = subprocess.run(
        [
            FPROBE, "-v", "error", "-show_entries", "format=duration",
            "-of", "csv=p=0", path,
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    return float(probe.stdout.strip())


def audio_stream_hash(path):
    probe = subprocess.run(
        [
            FF, "-v", "error", "-i", path, "-map", "0:a:0", "-c", "copy",
            "-f", "hash", "-hash", "sha256", "-",
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    return probe.stdout.strip()


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def canonical_timing(seg_id):
    path = os.path.join(V1, "audio", f"{seg_id}.timing.json")
    with open(path, encoding="utf-8") as handle:
        return json.load(handle)


def segment_id(spec):
    return spec.split()[0]


def phrase_number(spec):
    match = re.search(r"\bp(\d+)", spec)
    return int(match.group(1)) if match else 1


def build_chunk(index, picture, frames, zoom, first, last):
    out = os.path.join(SEGS, f"c{index:03d}.mp4")
    expected = frames / FPS
    source = os.path.join(ASSETS, picture)
    if (
        os.path.isfile(out)
        and os.path.getmtime(out) >= os.path.getmtime(source)
        and abs(duration_of(out) - expected) < 0.06
    ):
        print(f"== reuse {os.path.basename(out)} ({expected:.3f}s)", flush=True)
        return out

    if zoom == "in":
        z = f"1.001+0.10*on/{frames}"
    else:
        z = f"1.101-0.10*on/{frames}"
    vf = (
        "scale=2160:3868,setsar=1,"
        f"zoompan=z='{z}':x='iw/2-(iw/zoom/2)':"
        f"y='ih/2-(ih/zoom/2)':d={frames}:s=2160x3840:fps={FPS},"
        "scale=1080:1920:flags=lanczos"
    )
    if first:
        vf += ",fade=t=in:st=0:d=1.0"
    if last and expected > 1.3:
        vf += f",fade=t=out:st={expected - 1.0:.3f}:d=1.0"
    run(
        [
            FF, "-y", "-loglevel", "error", "-loop", "1",
            "-i", source, "-vf", vf,
            "-frames:v", str(frames),
        ]
        + BASE_ENC
        + [out]
    )
    return out


def build_card(frames, final_enc):
    duration = frames / FPS
    lines = textwrap.wrap(CARD_TEXT, width=30)
    line_height = 72
    filters = []
    for index, line in enumerate(lines):
        text_path = os.path.join(SEGS, f"card_{index}.txt")
        with open(text_path, "w", encoding="utf-8") as handle:
            handle.write(line)
        y = f"(h-{len(lines) * line_height})/2+{index * line_height}"
        filters.append(
            f"drawtext=fontfile={SERIF}:textfile={text_path}:fontsize=50:"
            f"fontcolor={INK}:x=(w-text_w)/2:y={y}"
        )
    filters.extend(
        [
            "fade=t=in:st=0:d=0.8",
            f"fade=t=out:st={max(0.0, duration - 0.8):.3f}:d=0.8",
        ]
    )
    out = os.path.join(SEGS, "card.mp4")
    run(
        [
            FF, "-y", "-loglevel", "error", "-f", "lavfi",
            "-i", f"color=c={CREAM}:s=1080x1920:r={FPS}",
            "-vf", ",".join(filters), "-frames:v", str(frames),
        ]
        + final_enc
        + [out]
    )
    return out


def main():
    os.makedirs(SEGS, exist_ok=True)
    # The shared caption renderer writes its small drawtext files to a relative
    # `segs/` folder.  Keep that scratch inside this V2 build, never in V1 or at
    # the repository root.
    os.chdir(HERE)
    os.makedirs("segs", exist_ok=True)
    if not os.path.isfile(LOCKED_FINAL):
        raise SystemExit(f"missing authoritative V1 final: {LOCKED_FINAL}")

    v2 = load_module("storm_beats_v2", os.path.join(HERE, "beats_v2.py"))
    narration = load_module(
        "storm_v1_narration", os.path.join(V1, "make_narration.py")
    )
    text = {row[0]: row[2] for row in narration.SEGMENTS}
    speaker = {row[0]: row[1] for row in narration.SEGMENTS}

    pictures = []
    for beat in v2.BEATS:
        picture = beat["out"]
        if not os.path.isfile(os.path.join(ASSETS, picture)):
            raise SystemExit(f"missing picture: {picture}")
        pictures.append(
            {
                "picture": picture,
                "spec": beat["seg"],
                "seg": segment_id(beat["seg"]),
                "phrase": phrase_number(beat["seg"]),
            }
        )
    if len(pictures) != 34:
        raise SystemExit(f"expected 34 pictures, found {len(pictures)}")

    # Reproduce the actual V1 build: complete MP3 duration, not spoken-trimmed
    # duration.  This is the timeline present in the authoritative final MP4.
    segment_order = [
        "n0", "j0", "n1", "n1b", "n2", "n2b", "n3", "n4", "s38",
        "n4b", "n5", "j1", "n6", "n7", "j2", "n8", "n9", "s41", "n9b",
    ]
    starts = {}
    durations = {}
    t = 0.0
    for seg in segment_order:
        starts[seg] = t
        audio_dur = duration_of(os.path.join(V1, "audio", f"{seg}.mp3"))
        gap = KJV_GAP if speaker[seg] != "narrator" else GAP
        durations[seg] = LEAD + audio_dur + gap
        t += durations[seg]
    card_start = t
    locked_duration = duration_of(LOCKED_FINAL)
    expected_total = (
        card_start
        + LEAD
        + duration_of(os.path.join(V1, "audio", "n10.mp3"))
        + TAIL
    )
    if abs(expected_total - locked_duration) > 0.1:
        raise SystemExit(
            f"timeline mismatch: calculated {expected_total:.3f}s, "
            f"locked final {locked_duration:.3f}s"
        )

    # First picture owns the opening lead.  A segment's first picture owns its
    # segment lead; later pictures switch on the canonical phrase timestamp.
    picture_starts = []
    for index, picture in enumerate(pictures):
        seg = picture["seg"]
        phrase = picture["phrase"]
        if index == 0:
            start = 0.0
        elif phrase <= 1:
            start = starts[seg]
        else:
            timing = canonical_timing(seg)
            if phrase > len(timing):
                raise SystemExit(
                    f"{picture['picture']}: phrase p{phrase} exceeds "
                    f"{seg}'s {len(timing)} timing rows"
                )
            start = starts[seg] + LEAD + float(timing[phrase - 1]["start"])
        picture_starts.append(round(start * FPS) / FPS)

    card_frame = round(card_start * FPS)
    chunk_files = []
    for index, picture in enumerate(pictures):
        start_frame = 0 if index == 0 else round(picture_starts[index] * FPS)
        end_frame = (
            round(picture_starts[index + 1] * FPS)
            if index + 1 < len(pictures)
            else card_frame
        )
        frames = end_frame - start_frame
        if frames <= 1:
            raise SystemExit(
                f"non-positive visual window for {picture['picture']}: {frames}"
            )
        chunk_files.append(
            build_chunk(
                index,
                picture["picture"],
                frames,
                "in" if index % 2 == 0 else "out",
                first=index == 0,
                last=index + 1 == len(pictures),
            )
        )

    concat_base = os.path.join(SEGS, "concat_base.txt")
    with open(concat_base, "w", encoding="utf-8") as handle:
        for chunk in chunk_files:
            handle.write(f"file '{os.path.basename(chunk)}'\n")
    base = os.path.join(SEGS, "base.mp4")
    run(
        [
            FF, "-y", "-loglevel", "error", "-f", "concat", "-safe", "0",
            "-i", concat_base, "-c", "copy", base,
        ]
    )

    # Use the V1 caption implementation, but redirect its timing-file loader to
    # canonical V1 JSON.  That prevents the stale V2 audio folder from affecting
    # either caption timing or the finished soundtrack.
    sys.path.insert(0, V1)
    captions = load_module(
        "storm_v1_captions", os.path.join(V1, "mbm_caption_timing.py")
    )

    def locked_timing_loader(mp3_path):
        seg = os.path.basename(os.path.splitext(mp3_path)[0])
        return canonical_timing(seg)

    captions._load_timing = locked_timing_loader

    filters = []
    for seg in segment_order:
        local_dur = durations[seg]
        timing = canonical_timing(seg)
        spoken_end = LEAD + float(timing[-1]["end"])
        layer = captions.caption_filter(
            seg, local_dur, spoken_end, text[seg], speaker[seg]
        )
        if not layer:
            continue
        layer = layer.replace(
            "between(t,", f"between(t-{starts[seg]:.6f},"
        )
        filters.append(layer.lstrip(","))

    audio_kbps = 127
    mux_kbps = 35
    video_cap = max(
        450, int(24.0 * 8000 / locked_duration) - audio_kbps - mux_kbps
    )
    final_enc = [
        "-c:v", "libx264", "-preset", "medium", "-crf", "19",
        "-maxrate", f"{video_cap}k", "-bufsize", f"{video_cap * 2}k",
        "-pix_fmt", "yuv420p", "-r", str(FPS), "-an",
    ]
    captioned = os.path.join(SEGS, "captioned.mp4")
    run(
        [
            FF, "-y", "-loglevel", "error", "-i", base,
            "-filter_complex", "[0:v]" + ",".join(filters) + "[v]",
            "-map", "[v]",
        ]
        + final_enc
        + [captioned]
    )

    total_frames = round(locked_duration * FPS)
    card_frames = max(1, total_frames - card_frame)
    build_card(card_frames, final_enc)
    concat_final = os.path.join(SEGS, "concat_final.txt")
    with open(concat_final, "w", encoding="utf-8") as handle:
        handle.write("file 'captioned.mp4'\nfile 'card.mp4'\n")
    silent = os.path.join(SEGS, "video_silent.mp4")
    run(
        [
            FF, "-y", "-loglevel", "error", "-f", "concat", "-safe", "0",
            "-i", concat_final, "-c", "copy", silent,
        ]
    )

    locked_hash = audio_stream_hash(LOCKED_FINAL)
    run(
        [
            FF, "-y", "-loglevel", "error", "-i", silent, "-i", LOCKED_FINAL,
            "-map", "0:v:0", "-map", "1:a:0", "-c:v", "copy", "-c:a", "copy",
            "-movflags", "+faststart", OUT,
        ]
    )
    rebuilt_hash = audio_stream_hash(OUT)
    if rebuilt_hash != locked_hash:
        raise SystemExit(
            f"AUDIO LOCK FAILED: V1 {locked_hash}, V2 {rebuilt_hash}"
        )
    size = os.path.getsize(OUT) / 1_000_000
    if size > 24.3:
        raise SystemExit(
            f"size limit failed: {size:.2f} MB (cap was {video_cap} kbps)"
        )
    print(f"AUDIO LOCK PASS: {rebuilt_hash}", flush=True)
    print(
        f"DONE: {os.path.basename(OUT)}  {size:.2f} MB  "
        f"{duration_of(OUT):.3f}s  34 pictures",
        flush=True,
    )


if __name__ == "__main__":
    main()
