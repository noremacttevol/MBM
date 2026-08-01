#!/usr/bin/env python3
"""Assemble a complete V2 audio master from existing tracked source MP3s.

This is the recovery path for a V1 final MP4 that is stale or shortened relative
to its own current make_narration.py and audio/ directory.  It never generates,
rewrites, trims, or substitutes a voice file.  It places every existing segment
at the timeline derived by extract_beats, records source hashes and durations,
and creates one version-lockable AAC stream for the final mux.
"""
import hashlib
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import extract_beats  # noqa: E402
from v2_assemble import v2_dir_of  # noqa: E402

FF = "ffmpeg"
FPROBE = "ffprobe"


def run(cmd):
    print(">>", " ".join(str(c) for c in cmd)[:180], flush=True)
    subprocess.run(cmd, check=True, capture_output=True)


def duration(path):
    p = subprocess.run(
        [FPROBE, "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", path], capture_output=True, text=True, check=True)
    return float(p.stdout.strip())


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def audio_hash(path):
    p = subprocess.run(
        [FF, "-v", "error", "-i", path, "-map", "0:a:0", "-c", "copy",
         "-f", "hash", "-hash", "sha256", "-"],
        capture_output=True, text=True, check=True)
    return p.stdout.strip().split("=", 1)[1]


def main():
    row = int(sys.argv[1])
    data = extract_beats.extract(row)
    v1dir = os.path.join(ROOT, data["v1_dir"])
    v2dir = v2_dir_of(row)
    segs = os.path.join(v2dir, "segs")
    os.makedirs(segs, exist_ok=True)

    placed = []
    for beat in data["beats"]:
        placed.append((beat["seg"], beat["audio_start"]))
    placed.append((data["card"]["seg"], data["card"]["audio_start"]))

    inputs = []
    filters = []
    labels = []
    manifest_segments = []
    for i, (seg, start) in enumerate(placed):
        path = os.path.join(v1dir, "audio", f"{seg}.mp3")
        if not os.path.isfile(path):
            raise SystemExit(f"missing authoritative source audio: {path}")
        inputs += ["-i", path]
        ms = int(start * 1000)
        filters.append(
            f"[{i}:a]aresample=44100,adelay={ms}|{ms},volume=1.0[a{i}]")
        labels.append(f"[a{i}]")
        manifest_segments.append({
            "seg": seg,
            "timeline_start": round(start, 6),
            "duration": round(duration(path), 6),
            "sha256": sha256(path),
            "source": os.path.relpath(path, ROOT),
        })

    total = data["total"]
    filters.append(
        "".join(labels)
        + f"amix=inputs={len(labels)}:duration=longest:normalize=0,"
        + f"apad=whole_dur={total:.6f}[aout]")
    raw = os.path.join(segs, "source-audio-complete-160k.m4a")
    run([FF, "-y"] + inputs + [
        "-filter_complex", ";".join(filters), "-map", "[aout]",
        "-t", f"{total:.6f}", "-c:a", "aac", "-b:a", "160k", raw,
    ])

    probe = subprocess.run(
        [FF, "-i", raw, "-af", "ebur128", "-f", "null", "-"],
        capture_output=True, text=True)
    lufs = None
    for line in probe.stderr.splitlines():
        line = line.strip()
        if line.startswith("I:") and "LUFS" in line:
            lufs = float(line.split()[1])
    gain = 0.0 if lufs is None else max(-6.0, min(16.0, -15.0 - lufs))

    locked = os.path.join(segs, "source-audio-complete-locked.m4a")
    run([FF, "-y", "-i", raw,
         "-af", f"volume={gain:.1f}dB,alimiter=limit=0.95",
         "-t", f"{total:.6f}", "-c:a", "aac", "-b:a", "128k", locked])

    manifest = {
        "row": row,
        "timeline_duration": round(total, 6),
        "source_segment_count": len(manifest_segments),
        "source_segments": manifest_segments,
        "measured_lufs": lufs,
        "applied_gain_db": round(gain, 1),
        "locked_audio": os.path.relpath(locked, ROOT),
        "locked_audio_duration": round(duration(locked), 6),
        "locked_audio_packet_sha256": audio_hash(locked),
    }
    out = os.path.join(v2dir, "AUDIO-SOURCE-MANIFEST.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)
        f.write("\n")
    print(f"SOURCE AUDIO LOCK: {manifest['locked_audio_packet_sha256']}")
    print(f"DONE {locked}  {manifest['locked_audio_duration']:.3f}s")


if __name__ == "__main__":
    main()
