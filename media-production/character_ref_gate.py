#!/usr/bin/env python3
"""character_ref_gate.py — refuse to spend Flow credit on a drifting character.

CHARACTER LAW rule 3 (Cameron, 2026-07-21; all 63 sheets approved and locked):
every still that shows a rostered character must condition on that character's
LOCKED sheet AND describe them from the sheet's spec. This gate is the
mechanical check, the same shape as `jesus_face_gate.py`:

    python3 media-production/character_ref_gate.py --dir build-NN-slug

Exit 0 = every rostered character named in PROMPTS.md carries their lock.
Exit 1 = a name appears with no lock text — fix it BEFORE generating.

For each character the build shows, PROMPTS.md must contain their lock marker
(e.g. "PETER LOCK") — `character_refs.lock_text('peter')` gives the exact
paragraph to paste. Attach their three jpegs as --ref alongside it.

A name that is mentioned but never DEPICTED (an epistle's author, a genealogy,
someone spoken about) is exempted by one line anywhere in PROMPTS.md:

    CHARACTER-REF-EXEMPT: james (epistle author, never on screen)

Scripture citations ("Matt 9:9", "daniel-3_slug") are ignored automatically.
"""
import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "CHARACTERS"))
from character_refs import find_in_text, resolve  # noqa: E402

EXEMPT = re.compile(r"CHARACTER-REF-EXEMPT:\s*([^\n(]+)", re.I)


def check(folder):
    d = Path(folder)
    p = d / "PROMPTS.md"
    if not p.is_file():
        print(f"FAIL {d.name}: no PROMPTS.md")
        return False
    text = p.read_text()

    exempt = set()
    for line in EXEMPT.findall(text):
        for name in line.replace(",", " ").split():
            try:
                exempt.add(resolve(name))
            except KeyError:
                pass

    shown = [s for s in find_in_text(text) if s not in exempt]
    missing = []
    for slug in shown:
        marker = slug.replace("-", " ").upper() + " LOCK"
        alt = slug.split("-")[0].upper() + " LOCK"   # "MARY MAGDALENE" -> "MARY LOCK"
        if marker not in text.upper() and alt not in text.upper():
            missing.append(slug)

    if missing:
        print(f"FAIL {d.name}: locked character(s) with no lock text in "
              f"PROMPTS.md: {', '.join(missing)}")
        print("     paste character_refs.lock_text('<name>') into each prompt "
              "they appear in, and attach their 3 jpegs as --ref.")
        print("     (if they are only MENTIONED, not painted, add: "
              "CHARACTER-REF-EXEMPT: <name> (reason))")
        return False

    note = f"{len(shown)} locked character(s): {', '.join(shown)}" if shown \
        else "no rostered characters"
    print(f"OK   {d.name}: {note}"
          + (f"; exempt: {', '.join(sorted(exempt))}" if exempt else ""))
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", required=True, nargs="+")
    a = ap.parse_args()
    ok = all([check(d) for d in a.dir])
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
