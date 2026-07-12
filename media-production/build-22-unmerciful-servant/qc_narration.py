#!/usr/bin/env python3
"""Narration ear-check (LAW, 2026-07-08 — Cameron's directive).

Transcribes every narration mp3 with speech-to-text and compares it
word-for-word against the intended script. Any segment whose transcription
drifts from the script is flagged BEFORE assembly. Run after every
make_narration.py run and fix flagged segments before building.

Adapted for #22 (Unmerciful Servant): EQUIV covers this story's numbers and
KJV forms (ten thousand talents, a hundred pence, seventy times seven,
trespasses) that whisper re-spells but are not audio defects.
"""
import re
import sys
from difflib import SequenceMatcher
from faster_whisper import WhisperModel

sys.path.insert(0, ".")
from make_narration import SEGMENTS  # noqa: E402


EQUIV = {
    # numbers whisper commonly writes as digits (norm() collapses digit-group
    # spaces first, so "10 000" and "10,000" both arrive here as "10000")
    "10000": "ten thousand", "10,000": "ten thousand",
    "100": "hundred", "7": "seven",
    # KJV forms whisper re-spells (not audio defects)
    "trespasses": "trespasses", "ye": "ye", "thee": "thee", "thou": "thou",
    "unto": "unto", "saith": "saith", "shalt": "shalt",
    # carried-forward general homophones
    "knight": "night",
}


def norm(t):
    t = t.lower()
    t = re.sub(r"[^a-z0-9' ]+", " ", t)
    t = re.sub(r"\s+", " ", t).strip()
    # collapse whisper's digit-group spacing ("10 000" -> "10000") so the EQUIV
    # number map catches it — a spelling artifact, never an audio defect.
    t = re.sub(r"(?<=\d) (?=\d)", "", t)
    return " ".join(EQUIV.get(w, w) for w in t.split())


def check(model, name, text):
    segs, _ = model.transcribe(f"audio/{name}.mp3", language="en")
    heard = " ".join(s.text for s in segs)
    a, b = norm(text), norm(heard)
    ratio = SequenceMatcher(None, a.split(), b.split(), autojunk=False).ratio()
    return ratio, a, b


def main():
    model = WhisperModel("small", device="cpu", compute_type="int8")
    tiebreak = None
    failures = 0
    for name, voice, rate, pitch, text in SEGMENTS:
        ratio, a, b = check(model, name, text)
        if ratio < 0.93:
            if tiebreak is None:
                tiebreak = WhisperModel("medium.en", device="cpu",
                                        compute_type="int8")
            ratio2, a2, b2 = check(tiebreak, name, text)
            if ratio2 >= 0.93:
                print(f"[OK ] {name}  match={ratio:.2f} small / "
                      f"{ratio2:.2f} medium.en (tie-break passed)")
                continue
            ratio, a, b = ratio2, a2, b2
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
