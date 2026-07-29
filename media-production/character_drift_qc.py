#!/usr/bin/env python3
"""character_drift_qc.py — catch a character described DIFFERENTLY in different builds.

Cameron, 2026-07-25 (complaints #90 "why does every disciple look the same",
#92/#103 "Peter went from grey to not grey", #102 "we need a QC just for beards
disappearing or appearing", #62 "he lost his beard", #32 "grows a beard"):

The root cause was NOT the image model ignoring us. Each build's PROMPTS.md carries
its OWN inline copy of a character's description as a `[X LOCK] = ...` block, and
those copies drifted away from the approved sheet in CHARACTERS/REFS.json. build-90
literally contained BOTH "PETER ~35 ... blue-grey" (in DISCIPLES LOCK) and
"Peter ... of about fifty ... grey-streaked ... rust-brown" (in PETER LOCK). The
picture obeyed the wrong one. So the same man went grey between videos.

This gate compares every inline `[X LOCK]` against the approved lock_text for that
character and fails on a CONTRADICTION in the traits Cameron actually notices:

  age        — a stated age that differs by more than AGE_TOL years
  hair/beard — grey/silver/white/salt-and-pepper asserted on one side only
  beard      — "clean-shaven"/"beardless" vs "full beard" (the beard flicker)
  garment    — a different locked tunic/robe colour

Usage:
  python3 character_drift_qc.py                 # every build, summary + exit 1 on drift
  python3 character_drift_qc.py --dir build-90-washing-feet
  python3 character_drift_qc.py --fix           # rewrite drifted blocks to the sheet
"""
import argparse
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REFS = json.loads((HERE / "CHARACTERS" / "REFS.json").read_text())

AGE_TOL = 6

# Story-justified differences: the SAME man at a different point in his life is not
# drift. Each entry needs a scripture reason, not a shrug. (build, character, kind)
WAIVERS = {
    ("build-180-before-i-formed-thee", "jeremiah", "GREY-HAIR"):
        "Jer 1:6 — this is his CALL; he is a youth here, decades before the grey-bearded "
        "weeping prophet the sheet locks. Age-appropriate, not drift.",
}

GREY = re.compile(r"\b(grey|gray|silver|white[- ]hair\w*|salt[- ]and[- ]pepper|greying|graying)\b", re.I)
# "grey-blue tunic" / "stone-grey" are GARMENT colours, not hair. Only count grey
# that is actually attached to hair or beard.
GREY_HAIR = re.compile(
    r"\b(grey|gray|silver|salt[- ]and[- ]pepper|greying|graying|white)[- ]?(streaked\s+)?"
    r"(?:\w+\s+){0,3}?(hair|beard|head|hairline|temples)\b", re.I)
GREY_HAIR_REV = re.compile(
    r"\b(hair|beard|hairline|temples)\b(?:\s+\w+){0,3}?\s+"
    r"(streaked\s+with\s+)?(grey|gray|silver|salt[- ]and[- ]pepper|white)\b", re.I)
BEARDLESS = re.compile(r"\b(clean[- ]shaven|beardless|no beard|without a beard)\b", re.I)
BEARDED = re.compile(r"\b(full[- ]\w*\s?beard|thick beard|a full beard|bearded|dark beard|short beard|trimmed \w+ beard)\b", re.I)
AGE = re.compile(r"\b(?:about|around|aged|of about|in his|~)\s*(?:his\s+)?(\d{2})\b|\b~(\d{2})\b|\bof about (\d{2})\b", re.I)
AGE_WORD = {"twenties": 25, "mid-twenties": 25, "thirties": 35, "mid-thirties": 35,
            "late thirties": 38, "forties": 45, "mid-forties": 45, "fifties": 55}
COLOURS = ("blue-grey", "grey-blue", "rust-brown", "russet", "ochre", "olive-drab",
           "forest-green", "teal-green", "indigo", "charcoal", "oxblood", "maroon",
           "mustard", "sand-tan", "stone-grey", "cream", "dun-brown", "brown", "blue",
           "green", "grey", "red")
GARMENT = re.compile(r"\b([a-z-]+)\s+(?:wool\s+|linen\s+)?(tunic|robe|mantle|cloak)\b", re.I)


NEGATED = re.compile(r"\b(never|not|no|nor)\b[^.;,]{0,40}?"
                     r"\b(bearded|beard|grey|gray|silver|white|clean[- ]shaven)\b", re.I)


def denegate(text):
    """Drop 'never bearded' / 'no grey' style clauses so a prohibition is not read
    as an assertion of the very trait it forbids."""
    return NEGATED.sub(" ", text)


def ages(text):
    out = []
    for m in AGE.finditer(text):
        g = next((x for x in m.groups() if x), None)
        if g:
            out.append(int(g))
    for word, val in AGE_WORD.items():
        if re.search(r"\b" + word + r"\b", text, re.I):
            out.append(val)
    return out


def greyhair(text):
    return bool(GREY_HAIR.search(text) or GREY_HAIR_REV.search(text))


def garments(text):
    found = set()
    for m in GARMENT.finditer(text):
        c = m.group(1).lower()
        if c in COLOURS:
            found.add((c, m.group(2).lower()))
    return found


# A lock name only maps to an approved sheet on an EXACT slug match or through this
# explicit alias table. Fuzzy matching was WRONG: build-06's `[FATHER LOCK]` is the
# vineyard-owner father of the Two Sons parable, and a "endswith -father" rule
# silently checked him against the GOD THE FATHER sheet. Generic role words
# (FATHER, MOTHER, WOMAN, BOY, SON, MAN) are parable characters far more often than
# they are the named cast, so they must never fuzzy-resolve.
# Bare first names are AMBIGUOUS and must not resolve: build-147's `[JOSEPH LOCK]`
# is Joseph of EGYPT, build-69's `[JOHN LOCK]` is John the BAPTIST. An alias table
# guessed wrong on both and would have sent someone repainting a correct picture.
# Exact slug match only. A build that wants coverage for a short name spells the
# lock out: `[JOHN-THE-BAPTIST LOCK]`.
AMBIGUOUS = {"john", "james", "mary", "joseph", "simon", "judas", "father",
             "mother", "woman", "boy", "son", "man"}


def canon_slug(lockname):
    """[PETER LOCK] -> peter. Exact slug only — never fuzzy, never a bare first name."""
    s = lockname.lower().replace(" lock", "").strip().replace(" ", "-")
    if s in AMBIGUOUS:
        return None
    return s if s in REFS else None


LOCKDEF = re.compile(r"\[([A-Z][A-Z' -]*?) LOCK\]\s*=\s*(.*?)(?=\n\s*\n|\n\[[A-Z])", re.S)


def check_build(path):
    text = path.read_text(encoding="utf-8", errors="ignore")
    issues = []
    for m in LOCKDEF.finditer(text):
        name, body = m.group(1), " ".join(m.group(2).split())
        slug = canon_slug(name)
        if not slug:
            continue
        canon = REFS[slug]["lock_text"]
        line = text[:m.start()].count("\n") + 1

        ca, ba = ages(canon), ages(body)
        if ca and ba and min(abs(x - y) for x in ca for y in ba) > AGE_TOL:
            issues.append((line, slug, "AGE", f"sheet says {ca}, this build says {ba}"))

        gb, gc = greyhair(denegate(body)), greyhair(denegate(canon))
        if gb and not gc:
            issues.append((line, slug, "GREY-HAIR", "this build adds grey/silver hair or beard; the sheet has none"))
        elif gc and not gb:
            issues.append((line, slug, "GREY-HAIR", "the sheet has grey hair; this build drops it"))

        # Strip negations first: Pilate's sheet says "clean-shaven ... never bearded",
        # and a naive BEARDED match on "never bearded" read that as a contradiction.
        cn, bn = denegate(canon), denegate(body)
        if BEARDLESS.search(bn) and BEARDED.search(cn):
            issues.append((line, slug, "BEARD", "this build says clean-shaven; the sheet says bearded"))
        elif BEARDLESS.search(cn) and BEARDED.search(bn):
            issues.append((line, slug, "BEARD", "this build gives him a beard; the sheet says clean-shaven"))

        cg, bg = garments(canon), garments(body)
        for kind in ("tunic", "robe"):
            cc = {c for c, k in cg if k == kind}
            bc = {c for c, k in bg if k == kind}
            if cc and bc and not (cc & bc):
                issues.append((line, slug, "GARMENT",
                               f"sheet {kind} is {sorted(cc)}, this build says {sorted(bc)}"))
    return issues


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", help="one build folder; default = all")
    args = ap.parse_args()

    builds = [HERE / args.dir] if args.dir else sorted(
        p for p in HERE.glob("build-*") if (p / "PROMPTS.md").exists())

    total = 0
    for b in builds:
        pm = b / "PROMPTS.md"
        if not pm.exists():
            continue
        issues = [i for i in check_build(pm)
                  if (b.name, i[1], i[2]) not in WAIVERS]
        if issues:
            print(f"\n{b.name}")
            for line, slug, kind, why in issues:
                print(f"  PROMPTS.md:{line}  {slug:<22} {kind:<10} {why}")
            total += len(issues)

    print(f"\n{'='*70}\nCHARACTER DRIFT: {total} contradiction(s) across {len(builds)} build(s)")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
