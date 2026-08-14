#!/usr/bin/env python3
"""Render row 117's closing card with a forced American pronunciation.

Cameron rejected two Brian renders of the plain word ``dramatized``.  Do not
randomly reroll it again.  ElevenLabs' multilingual-v2 model ignores phoneme
tags, so this one segment deliberately uses Flash v2 and the exact CMUdict
pronunciation D R AE1 M AH0 T AY2 Z D (DRAM-uh-tized).  The displayed/caption
spelling remains ``dramatized`` and every other segment remains untouched.
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
V1 = ROOT / "media-production" / "build-117-hosea-buys-her-back"
V2 = ROOT / "media-production-v2" / "build-117-hosea-buys-her-back"
VOICE_ID = "nPczCjzI2devNBz1zQrb"  # Brian — Cameron's locked narrator voice.
MODEL_ID = "eleven_flash_v2"      # Required for CMU phoneme-tag support.
DISPLAY_TEXT = (
    "God dramatized his own love with a marriage: however far she wandered, "
    "he went and bought her back and brought her home. You are not too far "
    "gone to be wanted. What would it mean to be loved home like that?"
)
TTS_TEXT = DISPLAY_TEXT.replace(
    "dramatized",
    '<phoneme alphabet="cmu-arpabet" ph="D R AE1 M AH0 T AY2 Z D">'
    "dramatized</phoneme>",
)


def _key() -> str:
    key_file = ROOT / "media-production" / "elevenlabs API KEY.txt"
    raw = key_file.read_text(encoding="utf-8").strip()
    match = re.search(r"sk_[A-Za-z0-9]+", raw)
    if match:
        return match.group(0)
    if not raw:
        raise RuntimeError("ElevenLabs API key file is empty")
    return raw


def _duration(path: Path) -> float:
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


def render_card() -> None:
    v1_card = V1 / "audio" / "card.mp3"
    v2_card = V2 / "audio" / "card.mp3"
    target_duration = _duration(v1_card)

    response = requests.post(
        f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}/with-timestamps",
        params={"output_format": "mp3_44100_128"},
        headers={"xi-api-key": _key(), "Content-Type": "application/json"},
        json={
            "text": TTS_TEXT,
            "model_id": MODEL_ID,
            "voice_settings": {
                "stability": 0.45,
                "similarity_boost": 0.80,
                "style": 0.0,
                "use_speaker_boost": True,
            },
        },
        timeout=120,
    )
    if response.status_code != 200:
        raise RuntimeError(
            f"ElevenLabs {response.status_code}: {response.text[:200]}"
        )

    payload = response.json()
    with tempfile.TemporaryDirectory(prefix="mbm-r117-card-") as tmp_name:
        tmp = Path(tmp_name)
        raw = tmp / "raw.mp3"
        fixed = tmp / "card.mp3"
        raw.write_bytes(base64.b64decode(payload["audio_base64"]))
        raw_duration = _duration(raw)
        tempo = raw_duration / target_duration
        if not 0.5 <= tempo <= 2.0:
            raise RuntimeError(
                f"unsafe atempo {tempo:.3f} from {raw_duration:.3f}s "
                f"to {target_duration:.3f}s"
            )
        subprocess.run(
            [
                "ffmpeg", "-y", "-v", "error", "-i", str(raw),
                "-af", f"atempo={tempo:.9f}", "-ar", "44100", "-b:a", "128k",
                str(fixed),
            ],
            check=True,
        )
        if abs(_duration(fixed) - target_duration) > 0.05:
            raise RuntimeError("duration lock failed")
        for destination in (v1_card, v2_card):
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(fixed, destination)

    # The segment stays exactly the same duration and wording, so its three
    # already-approved display sentence windows remain authoritative.
    timing = [
        {"text": DISPLAY_TEXT.split(". ")[0] + ".", "start": 0.0, "end": 7.43},
        {"text": "You are not too far gone to be wanted.", "start": 7.43, "end": 10.368},
        {"text": "What would it mean to be loved home like that?", "start": 10.368, "end": 13.328},
    ]
    for build in (V1, V2):
        (build / "audio" / "card.timing.json").write_text(
            json.dumps(timing), encoding="utf-8"
        )

    print(
        f"row 117 card: Brian/{MODEL_ID}, CMU DRAM-uh-tized, "
        f"duration locked {target_duration:.3f}s"
    )


if __name__ == "__main__":
    render_card()
