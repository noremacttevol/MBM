#!/usr/bin/env python3
"""Fix only row 171's complained closing-card pronunciation of ``lives``.

Cameron requires the verb /lɪvz/, not the plural-noun sound /laɪvz/.  The
caption remains correctly spelled ``lives``.  ElevenLabs Flash v2 receives the
explicit CMU phoneme L IH1 V Z in only the affected sentence, using the locked
Brian narrator.  The sentence is duration-matched and spliced into the existing
card, preserving the first sentence and the established video timeline.
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
V1 = ROOT / "media-production" / "build-171-baptized-for-the-dead"
V2 = ROOT / "media-production-v2" / "build-171-baptized-for-the-dead"
VOICE_ID = "nPczCjzI2devNBz1zQrb"  # Brian — Cameron's locked narrator.
MODEL_ID = "eleven_flash_v2"       # Supports CMU phoneme tags.
SENTENCE = (
    "Because He lives, there is hope for every name on the other side of the veil."
)
TTS_SENTENCE = SENTENCE.replace(
    "lives",
    '<phoneme alphabet="cmu-arpabet" ph="L IH1 V Z">lives</phoneme>',
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
    backup = V1 / "audio-cfix-backup-2026-08-16"
    backup.mkdir(exist_ok=True)
    builds = (("v1", V1), ("v2", V2))
    for label, build in builds:
        source = build / "audio" / "card.mp3"
        saved = backup / f"card-{label}.mp3"
        if not saved.exists():
            shutil.copy2(source, saved)

    with tempfile.TemporaryDirectory(prefix="mbm-r171-lives-") as tmp_name:
        tmp = Path(tmp_name)
        sentence = tmp / "sentence.mp3"
        render_sentence(sentence)
        for label, build in builds:
            timing_path = build / "audio" / "card.timing.json"
            timing = json.loads(timing_path.read_text(encoding="utf-8"))
            target = timing[1]
            if not target["text"].startswith("Because He liv"):
                raise RuntimeError(f"{label} card sentence map changed")
            source = build / "audio" / "card.mp3"
            fixed = tmp / f"card-{label}.mp3"
            splice(source, sentence, fixed, target["start"], target["end"])
            shutil.copyfile(fixed, source)
            target["text"] = SENTENCE
            timing_path.write_text(json.dumps(timing), encoding="utf-8")

    print(
        "row 171 card: Brian/Flash-v2, lives=L IH1 V Z (/lɪvz/), "
        f"V1 duration {duration(V1 / 'audio' / 'card.mp3'):.6f}s, "
        f"V2 duration {duration(V2 / 'audio' / 'card.mp3'):.6f}s"
    )


if __name__ == "__main__":
    main()
