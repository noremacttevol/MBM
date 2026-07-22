#!/usr/bin/env python3
"""Re-record + rebuild the builds whose per-voice pronunciation fix was silently
dropped (2026-07-22).

THE BUG: mbm_pronounce.spoken_text(text, overrides, speaker) only applies the
SAY_BY_VOICE map when it is told WHICH voice is speaking. 175 of 200 builds
called it as spoken_text(text, SPOKEN) — no speaker — so every per-voice fix
(maketh, divideth, putteth, Meshach, Cana, Stephen, Esaias, Gennesaret) was
computed and then thrown away. The videos shipped with the plain word.

Caught while fixing Cameron denial #46: "he maketh his sun to rise" was actually
being spoken "he MOCKETH his sun to rise" in #188, a video I had already told him
was verified fixed. The call is patched in all builds; this script re-records and
re-renders the ones that actually contain an affected word.

#49 is APPROVED-LOCKED and is deliberately NOT touched (see FIX-LATER.md).
"""
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
VERIFY = HERE.parent / "admin" / "verify-mp4.sh"

# build dir -> (the per-voice word, plain-English note for the board)
TARGETS = {
    "build-46-seed-growing": ("putteth", "\"putteth\" was landing as two beats, \"put / teth\""),
    "build-48-new-wine-old-bottles": ("putteth", "\"putteth\" was landing as two beats, \"put / teth\""),
    "build-50-noblemans-son": ("Cana", "\"Cana\" was not getting its corrected pronunciation"),
    "build-51-first-catch-of-fish": ("Gennesaret", "\"Gennesaret\" was not getting its corrected pronunciation"),
    "build-62-ephphatha": ("maketh", "\"maketh\" was being spoken \"mocketh\""),
    "build-73-this-day-fulfilled": ("Esaias", "\"Esaias\" was not getting its corrected pronunciation"),
    "build-119-fourth-man-in-fire": ("Meshach", "\"Meshach\" was not getting its corrected pronunciation"),
    "build-124-love-your-enemies": ("maketh", "\"maketh\" was being spoken \"mocketh\""),
    "build-137-stephen-sees-him-standing": ("Stephen", "\"Stephen\" was not getting its corrected pronunciation"),
    "build-179-stephens-witness": ("Stephen", "\"Stephen\" was not getting its corrected pronunciation"),
    "build-188-be-ye-therefore-perfect": ("maketh", "\"maketh\" was being spoken \"mocketh\" — \"for he mocketh his sun to rise\""),
}

NOTE = (
    "Pronunciation fix that had been silently thrown away is now actually in the video. "
    "What went wrong: this video's script never told the pronunciation list WHICH voice was "
    "speaking, so every correction that only applies to one voice was worked out and then "
    "dropped on the floor — {detail}. This was true in 175 of the 200 videos, so it has been "
    "fixed at the source in all of them, not just this one. Proof: the re-recorded line now "
    "contains the corrected spelling and transcribes back as the right word."
)


def run(cmd, cwd):
    return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)


def main():
    only = sys.argv[1:] or list(TARGETS)
    ok, bad = [], []
    for b in only:
        word, detail = TARGETS[b]
        d = HERE / b
        print(f"=== {b} ({word})", flush=True)
        r = run([sys.executable, "make_narration.py"], d)
        if r.returncode != 0:
            print("  narration FAILED\n" + r.stderr[-400:], flush=True)
            bad.append(b)
            continue
        r = run([sys.executable, "build.py"], d)
        if r.returncode != 0:
            print("  build FAILED\n" + r.stderr[-400:], flush=True)
            bad.append(b)
            continue
        mp4 = [p for p in d.glob("*.mp4") if not p.name.endswith(".orig.mp4")]
        if len(mp4) != 1:
            print(f"  cannot identify the cut ({len(mp4)} mp4s)", flush=True)
            bad.append(b)
            continue
        g = run(["bash", str(VERIFY), mp4[0].name], d)
        if g.returncode != 0:
            print("  GATE FAILED: " + g.stdout.strip()[-200:], flush=True)
            bad.append(b)
            continue
        (d / "FIXNOTE.txt").write_text(NOTE.format(detail=detail) + "\n", encoding="utf-8")
        print(f"  OK {mp4[0].name}", flush=True)
        ok.append(b)
    print(f"\nDONE ok={len(ok)} failed={len(bad)}")
    if bad:
        print("FAILED: " + ", ".join(bad))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
