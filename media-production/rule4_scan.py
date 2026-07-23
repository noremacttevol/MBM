#!/usr/bin/env python3
"""Rule-4 echo detector (STORY-INTEGRITY-LAW Rule 4).

Rule 4: the old habit of quoting a line in old-English scripture and then having
the narrator repeat it in modern English is dropped. Restate a verse in plain
words ONLY when the old English is genuinely hard to follow; if it already lands,
let it stand.

This scans TRANSCRIPTS/*.json for the pattern: a NARRATOR segment sitting right
next to a verbatim-KJV segment (jesus/god/scripture/woman) whose content it
restates. It FLAGS candidates for human review — it does not edit. A flagged
narrator beat often also carries real teaching that must be KEPT; the reviewer
trims only the restatement, not the teaching.

Output: TRANSCRIPTS/TRIM-CANDIDATES.md, ranked by how much the narrator overlaps
the adjacent verse.

Usage: python3 rule4_scan.py [--min 0.34]
"""
import argparse
import glob
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "TRANSCRIPTS")
VERBATIM = {"jesus", "god", "scripture", "woman"}

_STOP = set("""a an the and or but of to in on at for from by with as is are was were
be been being this that these those he she it they them his her its their him you
your thou thee thy thine ye not no so if then when what which who whom how out up
one all any some there here into unto upon shall will would could should did do
done had has have said say came come go went make made had""".split())


def content(text):
    return [w for w in re.findall(r"[a-z]+", text.lower())
            if w not in _STOP and len(w) > 2]


def overlap(narr, verse):
    """Fraction of the verse's distinctive content words the narrator reuses."""
    nv, vv = set(content(narr)), set(content(verse))
    if not vv:
        return 0.0, set()
    shared = nv & vv
    return len(shared) / len(vv), shared


def scan_file(path, min_ratio):
    with open(path) as f:
        data = json.load(f)
    segs = data["segments"]
    hits = []
    for i, s in enumerate(segs):
        if s["speaker"] != "narrator":
            continue
        # compare to an immediately adjacent verbatim-KJV verse (either side)
        for j in (i - 1, i + 1):
            if 0 <= j < len(segs) and segs[j]["speaker"] in VERBATIM:
                r, shared = overlap(s["text"], segs[j]["text"])
                if r >= min_ratio and len(shared) >= 3:
                    hits.append({"narr_id": s["id"], "verse_id": segs[j]["id"],
                                 "verse_speaker": segs[j]["speaker"], "ratio": r,
                                 "shared": sorted(shared), "narr": s["text"],
                                 "verse": segs[j]["text"]})
    return data["row"], data["slug"], hits


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--min", type=float, default=0.34)
    args = ap.parse_args()
    files = sorted(glob.glob(os.path.join(OUT, "*.json")))
    rows = []
    for p in files:
        row, slug, hits = scan_file(p, args.min)
        if hits:
            rows.append((row, slug, hits))
    total = sum(len(h) for _, _, h in rows)
    with open(os.path.join(OUT, "TRIM-CANDIDATES.md"), "w") as f:
        f.write("# RULE-4 TRIM CANDIDATES — narrator beats that echo an adjacent "
                "KJV verse\n\n")
        f.write(f"{total} candidate(s) across {len(rows)} video(s), overlap "
                f">= {args.min:.0%} of the verse's content words. REVIEW each: cut "
                "only the modern restatement, KEEP any teaching the beat adds. "
                "Leave it if the old English was genuinely hard and the restatement "
                "earns its place.\n\n")
        for row, slug, hits in rows:
            f.write(f"## #{row} — {slug}\n\n")
            for h in sorted(hits, key=lambda x: -x["ratio"]):
                f.write(f"- **{h['narr_id']}** echoes **{h['verse_id']}** "
                        f"({h['verse_speaker']}, {h['ratio']:.0%} overlap; "
                        f"shared: {', '.join(h['shared'])})\n")
                f.write(f"    - verse [{h['verse_id']}]: {h['verse']}\n")
                f.write(f"    - narrator [{h['narr_id']}]: {h['narr']}\n")
            f.write("\n")
    print(f"{total} trim candidate(s) across {len(rows)} video(s) "
          f"-> TRANSCRIPTS/TRIM-CANDIDATES.md")


if __name__ == "__main__":
    main()
