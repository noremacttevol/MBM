#!/usr/bin/env python3
"""Fix only row 161 n8's complained pronunciation of ``bowed``.

Cameron requires the past tense of bowing, /baʊd/, not /boʊd/.  The displayed
caption remains ``bowed``.  ElevenLabs Flash v2 receives the explicit CMU
phoneme B AW1 D in only the affected sentence, using the locked Brian narrator
voice.  That sentence is duration-matched and spliced into the existing n8 so
all other approved narration and all caption/picture windows remain fixed.
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
V1 = ROOT / "media-production" / "build-161-called-of-god"
V2 = ROOT / "media-production-v2" / "build-161-called-of-god"
VOICE_ID = "nPczCjzI2devNBz1zQrb"  # Brian — Cameron's locked narrator.
MODEL_ID = "eleven_flash_v2"       # Supports CMU phoneme tags.
SENTENCE = (
    "The right to speak and act for God has always come the same way: a real "
    "call, and hands laid on a bowed head."
)
TTS_SENTENCE = SENTENCE.replace(
    "bowed",
    '<phoneme alphabet="cmu-arpabet" ph="B AW1 D">bowed</phoneme>',
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


def render_sentence(path: Path) -> None:
    response = requests.post(
        f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}/with-timestamps",
        params={"output_format": "mp3_44100_128"},
        headers={"xi-api-key": key(), "Content-Type": "application/json"},
        json={
            "text": TTS_SENTENCE,
            "model_id": MODEL_ID,
            "voice_settings": {
                "stability": 0.55,
                "similarity_boost": 0.80,
                "style": 0.10,
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
    path.write_bytes(base64.b64decode(response.json()["audio_base64"]))


def splice(original: Path, sentence: Path, output: Path,
           start: float, end: float) -> None:
    old_duration = duration(original)
    sentence_duration = end - start
    raw_duration = duration(sentence)
    tempo = raw_duration / sentence_duration
    if not 0.5 <= tempo <= 2.0:
        raise RuntimeError(f"unsafe sentence atempo {tempo:.4f}")

    filt = (
        f"[0:a]atrim=start=0:end={start:.6f},asetpts=PTS-STARTPTS[pre];"
        f"[1:a]highpass=f=75,afftdn=nf=-32:nt=w,atempo={tempo:.9f},"
        f"atrim=duration={sentence_duration:.6f},asetpts=PTS-STARTPTS[mid];"
        f"[0:a]atrim=start={end:.6f}:end={old_duration:.6f},"
        "asetpts=PTS-STARTPTS[post];"
        f"[pre][mid][post]concat=n=3:v=0:a=1,apad,"
        f"atrim=duration={old_duration:.6f}[out]"
    )
    subprocess.run(
        [
            "ffmpeg", "-y", "-v", "error", "-i", str(original),
            "-i", str(sentence), "-filter_complex", filt,
            "-map", "[out]", "-ar", "44100", "-ac", "1",
            "-b:a", "128k", str(output),
        ],
        check=True,
    )
    if abs(duration(output) - old_duration) > 0.035:
        raise RuntimeError(
            f"duration lock failed: {duration(output):.6f} vs {old_duration:.6f}"
        )


def main() -> None:
    timing = json.loads((V1 / "audio" / "n8.timing.json").read_text())
    target = timing[1]
    if target["text"] != SENTENCE:
        raise RuntimeError("n8 sentence map changed; refusing an unsafe splice")

    backup = ROOT / "media-production" / "build-161-called-of-god" / \
        "audio-cfix-backup-2026-08-16"
    backup.mkdir(exist_ok=True)
    for label, build in (("v1", V1), ("v2", V2)):
        source = build / "audio" / "n8.mp3"
        saved = backup / f"n8-{label}.mp3"
        if not saved.exists():
            shutil.copy2(source, saved)

    with tempfile.TemporaryDirectory(prefix="mbm-r161-bowed-") as tmp_name:
        tmp = Path(tmp_name)
        sentence = tmp / "sentence.mp3"
        render_sentence(sentence)
        for label, build in (("v1", V1), ("v2", V2)):
            source = build / "audio" / "n8.mp3"
            fixed = tmp / f"n8-{label}.mp3"
            splice(source, sentence, fixed, target["start"], target["end"])
            shutil.copyfile(fixed, source)

    print(
        "row 161 n8: Brian/Flash-v2, bowed=B AW1 D (/baʊd/), "
        f"sentence locked {target['end'] - target['start']:.3f}s, "
        f"segment {duration(V1 / 'audio' / 'n8.mp3'):.6f}s"
    )


if __name__ == "__main__":
    main()
