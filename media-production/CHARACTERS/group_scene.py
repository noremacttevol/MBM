#!/usr/bin/env python3
"""group_scene.py — cast a scene from the locked roster instead of inventing it.

Cameron, 2026-07-21: "we need all the disciples all 12 so we can use their
faces in scenes." A last-supper or upper-room shot has to keep twelve men
straight. This prints the block to paste into that prompt and the exact
--ref list, so nobody re-describes an apostle from memory.

    python3 CHARACTERS/group_scene.py --twelve
    python3 CHARACTERS/group_scene.py peter john-beloved thaddaeus
    python3 CHARACTERS/group_scene.py --twelve --refs-only

Nano Banana takes a limited number of reference images, so for a wide group
shot attach the faces of the apostles who are actually READABLE in frame (the
foreground few) and let the written locks carry the rest. The tool prints them
in that order: named-and-close first.
"""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from character_refs import lock_text, refs, resolve, twelve  # noqa: E402

# Positional wording beats counting: image models cannot count to twelve, but
# they can follow "left to right." See mbm-image-and-pronunciation-craft.
PREAMBLE = (
    "THE TWELVE ARE INDIVIDUALS, NOT A CROWD: every man below is a specific "
    "person with a locked look. Paint each one exactly as described, each in "
    "HIS OWN tunic colour, so no two men read alike. Nobody wears cream or "
    "off-white (that belongs to the Lord alone) and nobody wears pure white. "
    "Describe them by position in the frame, left to right, never by number."
)


def block(names, refs_only=False):
    slugs = [resolve(n) for n in names]
    if not refs_only:
        print(PREAMBLE + "\n")
        for s in slugs:
            print(lock_text(s) + "\n")
    print("--ref list (attach in this order, nearest/most readable first):")
    unrendered = []
    for s in slugs:
        try:
            for p in refs(s):
                if p.endswith("face-front.jpeg"):
                    print(f"  --ref {p}")
        except FileNotFoundError:
            unrendered.append(s)
    if unrendered:
        print("\nNOT YET RENDERED — do not generate this scene until these "
              f"sheets exist (rule 4): {', '.join(unrendered)}")
        print("  python3 CHARACTERS/render_sheet.py <name>")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("names", nargs="*")
    ap.add_argument("--twelve", action="store_true",
                    help="all twelve apostles in gospel order")
    ap.add_argument("--refs-only", action="store_true")
    a = ap.parse_args()
    names = twelve() if a.twelve else a.names
    if not names:
        ap.error("name some characters, or pass --twelve")
    block(names, a.refs_only)


if __name__ == "__main__":
    main()
