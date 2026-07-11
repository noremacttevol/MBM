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


# 2026-07-09 (video #7, n0): two QC-tool bugs found and fixed — the AUDIO
# was perfect but the tool scored it 0.11.
# Bug 1: SequenceMatcher on long CHARACTER strings silently enables
#   "autojunk" (any char appearing in >1% of a 200+ char string is junked),
#   collapsing a 99%-identical pair to ~0.11. Fix: compare WORD lists with
#   autojunk=False.
# Bug 2: whisper writes what it hears in its own spelling — "5 000" for
#   "five thousand", "knight" for "night". Same sounds, correct audio.
#   Fix: normalize known homophones/number spellings before comparing.
EQUIV = {
    "bartimeus": "bartimaeus", "bartimaus": "bartimaeus",
    "bartimayus": "bartimaeus",
    "knight": "night",
    "5": "five", "000": "thousand", "5000": "five thousand",
    "two": "two", "2": "two", "3": "three", "6": "six",
    "18": "eighteen", "38": "thirty eight",
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
    # 2026-07-09 (video #3): the small model misheard the proper noun
    # "Zacchaeus" as "secchias" in a six-word clip while base.en AND
    # medium.en both heard it perfectly — a false positive on a rare
    # biblical name, not a TTS defect. New rule: any FAIL is re-judged
    # once by medium.en before it counts. A real TTS error fails both.
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
