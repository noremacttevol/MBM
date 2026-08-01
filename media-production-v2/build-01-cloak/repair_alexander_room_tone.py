#!/usr/bin/env python3
"""Mux Story 1 V3 with the two existing Alexander takes selectively denoised.

This is intentionally narrower than the normal V2 audio lock. Cameron's open
reviewer complaint names background sound while Jesus speaks, so the original
V1 final remains the base audio and only the exact time occupied by j0 and j1
is replaced. The replacements are the same already-approved Alexander source
files, at the same V1 timeline positions, after the shared MBM room-tone filter.
No TTS request is made and no text, pause, duration, or other speaker is changed.

Run after:
    python3 media-production-v2/v2_assemble.py 1 --prepare-only
"""

from __future__ import annotations

import hashlib
import importlib.util
import os
from pathlib import Path
import shutil
import subprocess


BUILD = Path(__file__).resolve().parent
V2_ROOT = BUILD.parent
ROOT = V2_ROOT.parent
V1_BUILD = ROOT / "media-production" / "build-01-cloak"
V1_FINAL = V1_BUILD / "mark-5_woman-touches-his-cloak.mp4"
SILENT_MASTER = BUILD / "segs" / "video_silent.mp4"
OUTPUT = BUILD / "mark-5_woman-touches-his-cloak-realistic-v3.mp4"
FFMPEG = shutil.which("ffmpeg") or "ffmpeg"
FFPROBE = shutil.which("ffprobe") or "ffprobe"

# These are the exact files tied to Alexander (UMnEnzK9QLLdRwnUyxMW) in the
# ElevenLabs history audit. Hash locks prevent a stale or substituted voice.
SOURCE_SHA256 = {
    "j0": "263c8ac528f79f44ec0aca32acec2522c80820b364e1f9461ef535e8d75f096c",
    "j1": "15bd6f0b0c126df5ff3249bca03e0819a80b61a0281936bd8ad7256e0093abd7",
}

# The original final limits these two lines differently. These measured gains
# keep the repaired lines within 0.4 dB of their original mean loudness.
GAIN_DB = {"j0": 7.0, "j1": 7.8}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def duration(path: Path) -> float:
    result = subprocess.run(
        [FFPROBE, "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", str(path)],
        check=True, capture_output=True, text=True,
    )
    return float(result.stdout.strip())


def audio_packet_hash(path: Path) -> str:
    result = subprocess.run(
        [FFMPEG, "-v", "error", "-i", str(path), "-map", "0:a:0",
         "-c", "copy", "-f", "hash", "-hash", "sha256", "-"],
        check=True, capture_output=True, text=True,
    )
    return result.stdout.strip().split("=", 1)[-1]


def load_timeline() -> dict:
    source = V2_ROOT / "extract_beats.py"
    spec = importlib.util.spec_from_file_location("extract_beats", source)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module.extract(1)


def main() -> int:
    for required in (V1_FINAL, SILENT_MASTER):
        if not required.is_file():
            raise SystemExit(f"missing required input: {required}")

    timeline = load_timeline()
    beats = {beat["seg"]: beat for beat in timeline["beats"]}
    sources = {seg: V1_BUILD / "audio" / f"{seg}.mp3" for seg in GAIN_DB}
    for seg, path in sources.items():
        actual = sha256(path)
        if actual != SOURCE_SHA256[seg]:
            raise SystemExit(
                f"ALEXANDER SOURCE LOCK FAILED for {seg}: {actual}"
            )

    windows = []
    for seg in ("j0", "j1"):
        start = float(beats[seg]["audio_start"])
        end = start + duration(sources[seg])
        windows.append((seg, start, end))

    enable = "+".join(
        f"between(t,{start:.3f},{end:.3f})" for _seg, start, end in windows
    )
    filters = [f"[1:a]volume=0:enable='{enable}'[base]"]
    for input_index, (seg, start, _end) in enumerate(windows, start=2):
        delay_ms = int(start * 1000)
        filters.append(
            f"[{input_index}:a]highpass=f=75,afftdn=nf=-32:nt=w,"
            f"volume={GAIN_DB[seg]:.1f}dB,alimiter=limit=0.95,"
            f"adelay={delay_ms}|{delay_ms}[{seg}]"
        )
    filters.append("[base][j0][j1]amix=inputs=3:duration=first:normalize=0[aout]")

    locked_duration = duration(V1_FINAL)
    if abs(duration(SILENT_MASTER) - locked_duration) > 0.05:
        raise SystemExit("visual master duration does not match the authoritative V1")
    vcap = max(300, int(24.5 * 8000 / locked_duration) - 145)

    command = [
        FFMPEG, "-y", "-v", "error", "-i", str(SILENT_MASTER),
        "-i", str(V1_FINAL), "-i", str(sources["j0"]),
        "-i", str(sources["j1"]), "-filter_complex", ";".join(filters),
        "-map", "0:v:0", "-map", "[aout]", "-c:v", "libx264",
        "-preset", "medium", "-crf", "19", "-maxrate", f"{vcap}k",
        "-bufsize", f"{2 * vcap}k", "-pix_fmt", "yuv420p", "-r", "30",
        "-c:a", "aac", "-b:a", "96k", "-movflags", "+faststart",
        "-t", f"{locked_duration:.6f}", str(OUTPUT),
    ]
    subprocess.run(command, check=True)

    rebuilt_duration = duration(OUTPUT)
    if abs(rebuilt_duration - locked_duration) > 0.05:
        raise SystemExit(
            f"duration changed: V1={locked_duration:.6f}, V3={rebuilt_duration:.6f}"
        )
    size = OUTPUT.stat().st_size
    if size > 24_500_000:
        raise SystemExit(f"candidate exceeds reviewer cap: {size} bytes")

    print("ALEXANDER SOURCE LOCK PASS")
    for seg, start, end in windows:
        print(
            f"  {seg}: {SOURCE_SHA256[seg]} at {start:.3f}-{end:.3f}s; "
            "highpass=75Hz afftdn=-32dB"
        )
    print(f"DURATION LOCK PASS: {rebuilt_duration:.6f}s")
    print(f"AUDIO PACKET SHA256: {audio_packet_hash(OUTPUT)}")
    print(f"FILE SHA256: {sha256(OUTPUT)}")
    print(f"DONE: {OUTPUT} ({size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
