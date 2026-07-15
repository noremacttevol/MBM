#!/usr/bin/env python3
"""THE FACE GATE v3 — REVERSED BY CAMERON 2026-07-15.

OLD LAW (dead, 2026-07-11..15): Jesus's face was never shown or prompted.
NEW LAW (Cameron): Jesus's face IS shown — the SAME face in every picture, in every
video: a Middle Eastern man, warm tan skin, dark brown-black hair, full dark beard,
warm BROWN eyes. Modeled on the familiar depiction of Jesus in modern Christian art,
but unmistakably Middle Eastern — never caucasian, never pale, never blue-eyed,
never blond. No halo, no glow.

Consistency is enforced by IMAGE, not by words: the approved portraits in
media-production/JESUS-MASTER-REF/ are attached (REF) to every generation where he
appears. Prose never invents his face; the reference pictures ARE his face.

What this gate now checks in a build's PROMPTS.md:
  FAIL if a shot mentions Jesus but is missing the exact JESUS LOCK v3 paragraph.
  FAIL if a Jesus shot is missing its "REF: jesus-master-ref" line.
  FAIL if ANY prompt contains banned drift language (caucasian/pale/blue eyes/
       blond/halo/glow) — the wrong-Jesus words.
Exit 0 = safe to generate. Same usage as before:
  python3 media-production/jesus_face_gate.py --dir <build-folder>
"""
import argparse
import re
import sys
from pathlib import Path

LOCK_V3 = (
    "JESUS LOCK v3: the SAME man as the attached JESUS-MASTER-REF images — identical "
    "face, hair and beard in every picture: a Middle Eastern Jewish man of about "
    "thirty-three, warm tan olive-brown skin, shoulder-length dark brown-black wavy "
    "hair, a full dark beard, kind warm BROWN eyes, one plain undyed off-white cream "
    "wool robe (only he wears cream). No halo, no glow. Never caucasian, never pale, "
    "never blue-eyed, never blond."
)

BANNED = [
    r"\bcaucasian\b", r"\bpale skin\b", r"\bwhite skin\b", r"\bfair[- ]skinned\b",
    r"\bblue eyes\b", r"\bblue[- ]eyed\b", r"\bblond\b", r"\bblonde\b",
    r"\bgolden hair\b", r"\bhalo\b", r"\bglowing face\b", r"\brim[- ]light\b",
]

JESUS_WORDS = re.compile(r"\b(jesus|the lord|the saviour|the savior|christ)\b", re.I)
SHOT = re.compile(r"^##\s+", re.M)


def check(md_path: Path):
    text = md_path.read_text()
    fails = []
    idx = [m.start() for m in SHOT.finditer(text)] + [len(text)]
    blocks = [text[idx[i]:idx[i + 1]] for i in range(len(idx) - 1)] if idx[:-1] else []
    for b in blocks:
        head = b.splitlines()[0][:70]
        if JESUS_WORDS.search(b):
            if LOCK_V3 not in b:
                fails.append(f"MISSING JESUS LOCK v3 (byte-identical) in: {head}")
            if not re.search(r"^\s*REF:.*jesus-master-ref", b, re.M | re.I):
                fails.append(f"MISSING 'REF: jesus-master-ref' line in: {head}")
    for pat in BANNED:
        for m in re.finditer(pat, text, re.I):
            ln = text[:m.start()].count("\n") + 1
            fails.append(f"BANNED drift language {m.group(0)!r} at line {ln}")
    return fails


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", required=True)
    args = ap.parse_args()
    build = Path(args.dir)
    md = build / "PROMPTS.md"
    print("=" * 72)
    print("THE FACE GATE v3 — same face, every picture (Cameron, 2026-07-15)")
    print("=" * 72)
    if not md.exists():
        sys.exit(f"No PROMPTS.md in {build}")
    fails = check(md)
    for f in fails:
        print(f"    FAIL  {f}")
    print("-" * 72)
    if fails:
        print(f"RESULT: {len(fails)} FAIL. Every Jesus shot needs the byte-identical")
        print("JESUS LOCK v3 paragraph + a 'REF: jesus-master-ref' line, and no")
        print("wrong-Jesus drift words anywhere. Fix and re-run.")
        sys.exit(1)
    print("RESULT: PASS — every Jesus prompt is locked to the master face. Generate.")


if __name__ == "__main__":
    main()
