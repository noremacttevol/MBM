#!/usr/bin/env python3
"""Narration ear-check (LAW, 2026-07-08 — Cameron's directive).

Transcribes every narration mp3 with speech-to-text and compares it
word-for-word against the intended script. Any segment whose transcription
drifts from the script is flagged BEFORE assembly. The AI must run this after
every make_narration.py run and fix flagged segments before building.
Born because bad pronunciations kept reaching Cameron — he must never be the
one catching broken audio.

Carried forward from the build-07-peter-water lineage: WORD-list comparison
with autojunk=False (SequenceMatcher silently junks common chars in long
strings and collapses a 99% match to ~0.11) + an EQUIV normalization table for
whisper's own spelling of homophones/numbers/proper nouns (not audio defects),
and a medium.en tie-break re-judge on any FAIL (the small model false-positives
on rare biblical names).
"""
import re
import sys
from difflib import SequenceMatcher
from faster_whisper import WhisperModel

sys.path.insert(0, ".")
from make_narration import SEGMENTS  # noqa: E402


# whisper writes what it hears in its own spelling — normalize known
# homophones / number spellings / proper nouns before comparing so a correct
# audio file is not flagged for a spelling difference.
EQUIV = {
    # numbers whisper commonly writes as digits — the flock counts in this story
    "100": "hundred", "99": "ninety nine", "98": "ninety eight",
    "1": "one", "2": "two",
    "ninety-nine": "ninety nine", "ninety-eight": "ninety eight",
    # KJV forms whisper re-spells (not audio defects)
    "repented": "repenteth", "repenteth": "repenteth",
    "thinkest": "thinkest", "verily": "verily",
    "neighbours": "neighbors", "neighbour": "neighbor",
    # carried-forward general homophones
    "knight": "night",
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
    # any FAIL is re-judged once by medium.en before it counts — the small
    # model false-positives on rare biblical proper nouns while medium.en and
    # base.en hear them perfectly. A real TTS error fails both.
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
