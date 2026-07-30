#!/usr/bin/env python3
"""v2_story_cast.py — one face sheet per character per story, so faces stop drifting.

CAMERON'S BUG REPORT, 2026-07-30 (this file exists because of it):
  *"i do have a concern within each story, i seen that the api made the prodigal son
  and maybe it was flows fault but idk but the face of the other son kept changing and
  that throws people off so if we need to have a character sheet for each story to keep
  it staying the same in the story then we need to tell the api to do that"*

He is right, and it was already measured: row 2's QC found the elder son came back as
THREE VISIBLY DIFFERENT MEN across s16/s17/s18. It was fixed mid-row by attaching an
accepted still of him as a reference to every later beat — and it held on every frame
after. That fix was never generalised, so every other story still had the bug.

WHY TEXT ALONE CANNOT WORK. A lock like "the same man in every shot — late twenties,
broader than his brother, straight dark hair, full trimmed dark beard" describes a
whole family of faces, not one face. The model picks a different member of that family
each call. Identity has to be carried by an IMAGE — that is the whole CAST-BIBLE
lesson, proven twice now.

WHAT THIS DOES.
  1. Reads a story's beats_v2.py LOCKS and works out which are PEOPLE (not settings).
  2. Generates ONE clean neutral front portrait per person, from that person's own
     byte-identical lock text, into <build>/CAST-REF-V2/<name>.jpeg.
  3. Writes REFS = {...} into the build so v2_gen_api attaches each person's portrait
     to every beat whose `locks` name them. Already-supported machinery; nothing new
     is needed downstream.

The Twelve and other cross-story cast are handled globally by CAST-V2-REF/ and are
skipped here — this is only for characters who live inside one story.

MONEY. 1 portrait per character, ~136-200 portraits for all 118 authored stories,
~$0.134 each = roughly $20-27 total, and it protects ~3,200 beats from face drift.
--dry-run prices it and spends nothing. Always dry-run first.

Usage:
    python3 media-production-v2/v2_story_cast.py --all --dry-run
    python3 media-production-v2/v2_story_cast.py build-02-prodigal
    python3 media-production-v2/v2_story_cast.py --all --ceiling 30
"""
import argparse
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from v2_prompt import STYLE_V2, load_beats  # noqa: E402

# Global cast lives in CAST-V2-REF/ and is attached by v2_gen_api already.
GLOBAL_CAST = {
    "JESUS", "PETER", "JOHN", "ANDREW", "JAMES-A", "JAMES-Z", "PHILIP",
    "BARTHOLOMEW", "MATTHEW", "THOMAS", "SIMON-Z", "JUDAS", "THADDAEUS",
    "MARY-MAGDALENE", "MARY", "MARTHA",
}

# A lock is a PERSON if it describes a body. Biased toward INCLUSION on purpose:
# a needless portrait costs $0.13, a missing one costs a whole story's consistency.
BODY = re.compile(
    r"\b(his|her|their) face|\bsame (man|woman|boy|girl|person|men|women|people)\b"
    r"|\bbeard\b|\bhair\b|\beyes\b|\bskin\b|\bcomplexion\b|\bshoulders\b"
    r"|\bof about (thirty|forty|fifty|sixty|seventy|twenty|ten|eight|nine)"
    r"|\b(early|late|mid) (twenties|thirties|forties|fifties|sixties)\b"
    r"|\byears old\b|\bface is shown clearly\b", re.I)
# Strong place signals — only used to veto when NO body signal is present.
PLACE = re.compile(
    r"\b(street|room|hall|house|courtyard|village|town|city|field|hill|lake|sea|shore|"
    r"synagogue|temple|chamber|tomb|garden|road|well|tree|wall|farm|estate|vineyard|"
    r"boat|stall|market|doorway|landscape)\b", re.I)


# ONE person, singular. A group lock ("the religious men ARE the same three") must be
# skipped: a single portrait cannot lock a crowd, and attaching one as if it were one
# character would make the pictures worse, not better.
# Allow an adjective: row 6's lock says "is the same YOUNG man", which the first
# version missed, silently dropping SECOND-SON and leaving his face unlocked.
SINGULAR = re.compile(
    r"\bis the same (?:\w+ ){0,2}(man|woman|boy|girl|person|lad|girl|child)\b", re.I)
PLURAL = re.compile(r"\bare the same\b|\bthe same (three|two|four|group)\b", re.I)


def people_in(mod):
    """Which of a story's LOCKS name ONE person who needs a face sheet."""
    out = []
    for name, text in (getattr(mod, "LOCKS", {}) or {}).items():
        if name.upper() in GLOBAL_CAST:
            continue
        if PLURAL.search(text):
            continue                      # a crowd cannot be locked by one portrait
        if SINGULAR.search(text):
            out.append(name)              # unambiguous single character
            continue
        # No explicit "is the same man" — accept only if it clearly describes a body
        # AND is not really a place. This is what caught row 1's WOMAN and row 6's
        # FIRST-SON, both of which the first draft filed as settings.
        if BODY.search(text) and not PLACE.search(text):
            out.append(name)
    return out


def portrait_prompt(lock_text):
    """A neutral front reference portrait built from that character's own lock.

    Neutral light and a plain background on purpose: a face-lock reference wants the
    model to copy the FACE, not a scene. That is the lesson from the Jesus v2 face
    bootstrap, where the evenly-lit plain-background candidate was chosen for exactly
    this reason over a prettier backlit one.
    """
    return " ".join((
        STYLE_V2,
        "A REFERENCE PORTRAIT for character consistency: a single person, "
        "head-and-shoulders, face straight to camera and filling most of the frame, "
        "neutral even soft daylight, a plain neutral dark earth-brown background with "
        "nothing else in the picture, a calm neutral expression, both eyes open and "
        "clearly visible. One person only.",
        lock_text,
    ).__iter__()) if False else " ".join([
        STYLE_V2,
        "A REFERENCE PORTRAIT for character consistency: a single person, "
        "head-and-shoulders, face straight to camera and filling most of the frame, "
        "neutral even soft daylight, a plain neutral dark earth-brown background with "
        "nothing else in the picture, a calm neutral expression, both eyes open and "
        "clearly visible. One person only.",
        lock_text,
    ])


def refs_block(names):
    lines = ["", "# Per-story face sheets, generated by v2_story_cast.py. Identity is",
             "# carried by IMAGE, not by wording — text locks let the elder son come",
             "# back as three different men in row 2 (Cameron, 2026-07-30).",
             "REFS = {"]
    for n in names:
        lines.append(f'    "{n}": "CAST-REF-V2/{n.lower()}.jpeg",')
    lines.append("}")
    return "\n".join(lines) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("build", nargs="?")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--ceiling", type=float, default=None)
    a = ap.parse_args()

    builds = (sorted(glob.glob(os.path.join(HERE, "build-*/")))
              if a.all else [os.path.join(HERE, a.build) + os.sep])
    plan, total = [], 0
    for d in builds:
        if not os.path.exists(os.path.join(d, "beats_v2.py")):
            continue
        try:
            mod = load_beats(d)
        except Exception as e:
            print(f"  ! {os.path.basename(d.rstrip(os.sep))}: {e}")
            continue
        names = people_in(mod)
        if not names:
            continue
        have_refs = bool(getattr(mod, "REFS", None))
        plan.append((d, mod, names, have_refs))
        total += sum(1 for n in names
                     if not os.path.exists(os.path.join(d, "CAST-REF-V2", n.lower() + ".jpeg")))

    print(f"{len(plan)} stories · {total} portraits still to make · "
          f"~${total * 0.134:.2f} at 2K")
    for d, mod, names, have in plan[:80]:
        print(f"  {os.path.basename(d.rstrip(os.sep)):34s} {'REFS set' if have else 'no REFS':9s} {names}")

    if a.dry_run:
        print("\n--dry-run: nothing generated, nothing spent.")
        return
    if a.ceiling is not None and total * 0.134 > a.ceiling:
        raise SystemExit(f"would cost ~${total*0.134:.2f}, over --ceiling {a.ceiling}")

    # Generation is delegated to the API engine so the spend meter, ceiling and 2K
    # settings all stay in ONE place. Writing a second generation path would be how
    # the 1K fallback bug happened in the first place.
    from v2_gen_api import generate_one  # noqa: E402
    for d, mod, names, _have in plan:
        outdir = os.path.join(d, "CAST-REF-V2")
        os.makedirs(outdir, exist_ok=True)
        for n in names:
            dest = os.path.join(outdir, n.lower() + ".jpeg")
            if os.path.exists(dest):
                continue
            print(f"=== {os.path.basename(d.rstrip(os.sep))} :: {n} ===", flush=True)
            generate_one(portrait_prompt(mod.LOCKS[n]), dest, refs=[])
        block = refs_block(names)
        src = open(os.path.join(d, "beats_v2.py")).read()
        if "\nREFS = {" not in src:
            open(os.path.join(d, "beats_v2.py"), "a").write(block)
            print(f"  REFS written into {os.path.basename(d.rstrip(os.sep))}/beats_v2.py")


if __name__ == "__main__":
    main()
