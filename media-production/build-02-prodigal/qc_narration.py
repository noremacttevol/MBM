#!/usr/bin/env python3
"""Narration ear-check (NEW LAW, 2026-07-08 — Cameron's directive).

Transcribes every narration mp3 with speech-to-text and compares it
word-for-word against the intended script. Any segment whose transcription
drifts from the script is flagged BEFORE assembly. The AI must run this after
every make_narration.py run and fix flagged segments before building.
Born because bad pronunciations kept reaching Cameron — he must never be the
one catching broken audio.
"""
import re
import sys
from difflib import SequenceMatcher
from faster_whisper import WhisperModel

sys.path.insert(0, ".")
from make_narration import SEGMENTS  # noqa: E402


def norm(t):
    t = t.lower()
    t = re.sub(r"[^a-z0-9' ]+", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def main():
    model = WhisperModel("small", device="cpu", compute_type="int8")
    failures = 0
    for name, voice, rate, pitch, text in SEGMENTS:
        segs, _ = model.transcribe(f"audio/{name}.mp3", language="en")
        heard = " ".join(s.text for s in segs)
        a, b = norm(text), norm(heard)
        ratio = SequenceMatcher(None, a, b).ratio()
        status = "OK " if ratio >= 0.93 else "FAIL"
        if ratio < 0.93:
            failures += 1
        print(f"[{status}] {name}  match={ratio:.2f}")
        if ratio < 0.93:
            print(f"       script: {a}")
            print(f"       heard : {b}")
    if failures:
        print(f"\n{failures} segment(s) FAILED — fix before assembly.")
        sys.exit(1)
    print("\nAll narration segments verified against script.")


if __name__ == "__main__":
    main()
