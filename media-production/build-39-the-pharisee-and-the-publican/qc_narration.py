#!/usr/bin/env python3
"""Narration ear-check (Ear-Check Law, 2026-07-08 — Cameron's directive).

Transcribes every narration mp3 with speech-to-text and compares it word-for-word
against the intended script. Any segment under 0.93 is regenerated BEFORE assembly.
Cameron must never be the one who catches broken audio.

This is the FIXED version carried forward from build-07-peter-water, per the
PRODUCTION-BIBLE note: the QC tool itself once had two bugs that failed perfect
audio.
  Bug 1: SequenceMatcher on long CHARACTER strings silently enables "autojunk",
         collapsing a 99%-identical pair to ~0.11. Fix: compare WORD lists with
         autojunk=False.
  Bug 2: whisper writes what it HEARS in its own spelling ("5" for "five",
         "knight" for "night"). Same sounds, correct audio. Fix: normalize known
         homophones/number spellings before comparing.

EQUIV extended for video #39, whose script leans on spoken counts: "one fast a
year", "twice a week", "the word I five times", "a prayer of only seven words",
"a tenth of everything".
"""
import re
import sys
from difflib import SequenceMatcher
from faster_whisper import WhisperModel

sys.path.insert(0, ".")
from make_narration import SEGMENTS  # noqa: E402

EQUIV = {
    "knight": "night",
    "1": "one", "2": "two", "3": "three", "4": "four", "5": "five",
    "6": "six", "7": "seven", "8": "eight", "9": "nine", "10": "ten",
    "1st": "first", "10th": "tenth", "18": "eighteen",
    "000": "thousand", "5000": "five thousand",
    # whisper sometimes writes the ordinal/number forms of these spoken words
    "twice": "twice", "tenth": "tenth",
}


def norm(t):
    t = t.lower()
    t = re.sub(r"[^a-z0-9' ]+", " ", t)
    t = re.sub(r"\s+", " ", t).strip()
    return " ".join(EQUIV.get(w, w) for w in t.split())


def check(model, name, text):
    segs, _ = model.transcribe(f"audio/{name}.mp3", language="en")
    heard = " ".join(s.text for s in segs)
    a, b = norm(text), norm(heard)
    ratio = SequenceMatcher(None, a.split(), b.split(), autojunk=False).ratio()
    return ratio, a, b


def main():
    model = WhisperModel("small", device="cpu", compute_type="int8")
    # Any FAIL is re-judged once by medium.en before it counts — the small model
    # mishears rare biblical words ("publican", "extortioners", "exalteth") that
    # bigger models get right. A real TTS error fails both.
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
