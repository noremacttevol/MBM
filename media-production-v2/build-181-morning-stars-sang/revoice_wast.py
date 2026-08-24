#!/usr/bin/env python3
"""Render only row 181 g4 with the accepted pronunciation of wast.

Cameron rejected the delivered God-voice pronunciation. The visible KJV spelling
stays wast. ElevenLabs Flash v2 receives the explicit American stressed CMU
pronunciation W AO1 S T (/wɔst/, rhyming with "lost") in the locked Bill voice.
The complete g4 segment is duration-locked to the authoritative V1 segment so no
other narration, picture window, or closing-card timing moves.
"""

from __future__ import annotations

import base64
import json
from pathlib import Path
import re
import shutil
import subprocess
import tempfile

import requests


ROOT = Path(__file__).resolve().parents[2]
V1 = ROOT / "media-production" / "build-181-morning-stars-sang"
V2 = ROOT / "media-production-v2" / "build-181-morning-stars-sang"
VOICE_ID = "pqHfZKP75CvOlQylNhV4"  # Bill — Cameron's locked God voice.
MODEL_ID = "eleven_flash_v2"       # Supports CMU phoneme tags.
DISPLAY_TEXT = (
    "Where wast thou when I laid the foundations of the earth? "
    "declare, if thou hast understanding."
)
TTS_TEXT = DISPLAY_TEXT.replace(
    "wast",
    '<phoneme alphabet="cmu-arpabet" ph="W AO1 S T">wast</phoneme>',
)


def key() -> str:
    raw = (ROOT / "media-production" / "elevenlabs API KEY.txt").read_text(
        encoding="utf-8"
    )
    match = re.search(r"sk_[A-Za-z0-9]+", raw)
    if not match:
        raise RuntimeError("no ElevenLabs API token found")
    return match.group(0)


def duration(path: Path) -> float:
    result = subprocess.run(
        [
            "ffprobe", "-v", "error", "-show_entries", "format=duration",
            "-of", "default=nw=1:nk=1", str(path),
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    return float(result.stdout.strip())


def render_g4() -> None:
    v1_audio = V1 / "audio" / "g4.mp3"
    target_duration = duration(v1_audio)
    timing = [
        {
            "text": "Where wast thou when I laid the foundations of the earth?",
            "start": 0.0,
            "end": 3.32,
        },
        {
            "text": "declare, if thou hast understanding.",
            "start": 3.32,
            "end": 6.734,
        },
    ]

    response = requests.post(
        f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}/with-timestamps",
        params={"output_format": "mp3_44100_128"},
        headers={"xi-api-key": key(), "Content-Type": "application/json"},
        json={
            "text": TTS_TEXT,
            "model_id": MODEL_ID,
            "voice_settings": {
                "stability": 0.60,
                "similarity_boost": 0.80,
                "style": 0.0,
                "use_speaker_boost": True,
                "speed": 0.92,
            },
        },
        timeout=120,
    )
    if response.status_code != 200:
        raise RuntimeError(
            f"ElevenLabs {response.status_code}: {response.text[:200]}"
        )

    with tempfile.TemporaryDirectory(prefix="mbm-r181-wast-") as tmp_name:
        tmp = Path(tmp_name)
        raw = tmp / "g4-raw.mp3"
        fixed = tmp / "g4.mp3"
        raw.write_bytes(base64.b64decode(response.json()["audio_base64"]))
        raw_duration = duration(raw)
        tempo = raw_duration / target_duration
        if not 0.5 <= tempo <= 2.0:
            raise RuntimeError(
                f"unsafe atempo {tempo:.3f}: {raw_duration:.3f}s "
                f"to {target_duration:.3f}s"
            )
        subprocess.run(
            [
                "ffmpeg", "-y", "-v", "error", "-i", str(raw),
                "-af", (
                    f"atempo={tempo:.9f},apad,"
                    f"atrim=duration={target_duration:.9f}"
                ),
                "-ar", "44100", "-ac", "1", "-b:a", "128k", str(fixed),
            ],
            check=True,
        )
        if abs(duration(fixed) - target_duration) > 0.035:
            raise RuntimeError(
                f"duration lock failed: {duration(fixed):.6f} "
                f"vs {target_duration:.6f}"
            )
        for build in (V1, V2):
            destination = build / "audio" / "g4.mp3"
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(fixed, destination)
            (build / "audio" / "g4.timing.json").write_text(
                json.dumps(timing), encoding="utf-8"
            )

    print(
        "row 181 g4: Bill/Flash-v2, wast=W AO1 S T (/wɔst/), "
        f"segment locked {duration(v1_audio):.6f}s"
    )


if __name__ == "__main__":
    render_g4()

