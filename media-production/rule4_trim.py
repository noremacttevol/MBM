#!/usr/bin/env python3
"""Rule-4 sentence-level trim PROPOSER (and careful applier).

For each narrator beat flagged by rule4_scan.py, split it into sentences and
score EACH sentence against the adjacent KJV verse. A sentence most of whose own
content words are already in the verse is a restatement (Rule 4 cuts it); a
sentence that adds new words is teaching (KEEP). We never empty a beat and never
cut a sentence carrying a proper noun the verse lacks.

Default = DRY: writes TRANSCRIPTS/TRIM-PROPOSALS.md for review. With --apply it
edits each build's make_narration.py in place (exact-text replace of the beat),
then you re-export + re-scan.

Usage:
  python3 rule4_trim.py                     # dry proposals for all flagged rows
  python3 rule4_trim.py --rows 5,18         # only these rows
  python3 rule4_trim.py --rows 5 --apply    # apply to make_narration.py
  --cut 0.6   sentence-overlap at/above which a sentence is a restatement (def .6)
"""
import argparse
import glob
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "TRANSCRIPTS")

import rule4_scan as R  # reuse content()/overlap()/scan_file()


def sentences(text):
    return [p for p in re.split(r"(?<=[.!?;:]) +", text.strip()) if p]


def sent_restates(sent, verse, cut):
    """A sentence restates the verse if most of ITS content words are in the
    verse AND it introduces no proper noun the verse lacks."""
    sv = R.content(sent)
    if not sv:
        return False
    vv = set(R.content(verse))
    frac = sum(1 for w in sv if w in vv) / len(sv)
    # a capitalized word not in the verse = new proper noun -> keep (teaching)
    proper_new = any(w[0].isupper() and w.lower() not in vv
                     for w in re.findall(r"[A-Za-z]+", sent)
                     if len(w) > 2 and w.lower() not in R._STOP)
    return frac >= cut and not proper_new


def propose(row, cut):
    """Return [(beat_id, old_text, new_text, kept, dropped)] for a row."""
    hits = glob.glob(os.path.join(OUT, f"{row:03d}-*.json"))
    if not hits:
        return None, []
    data = json.load(open(hits[0]))
    segs = data["segments"]
    idx = {s["id"]: i for i, s in enumerate(segs)}
    _, _, flags = R.scan_file(hits[0], 0.34)
    out = []
    for h in flags:
        i = idx[h["narr_id"]]
        verse = h["verse"]
        beat = segs[i]["text"]
        ss = sentences(beat)
        keep = [s for s in ss if not sent_restates(s, verse, cut)]
        dropped = [s for s in ss if sent_restates(s, verse, cut)]
        if dropped and keep:  # never empty a beat
            out.append((h["narr_id"], beat, " ".join(keep), keep, dropped))
    return data["slug"], out


def apply_to_build(row, slug, edits):
    folders = glob.glob(os.path.join(HERE, f"build-*{row}-{slug}")) \
        or glob.glob(os.path.join(HERE, f"build-*-{slug}"))
    folder = next((f for f in folders
                   if re.match(rf"build-0*{row}-", os.path.basename(f))), None)
    if not folder:
        return f"#{row}: build folder not found for slug {slug}"
    mn = os.path.join(folder, "make_narration.py")
    src = open(mn).read()
    n = 0
    for beat_id, old, new, *_ in edits:
        if old in src:
            src = src.replace(old, new, 1)
            n += 1
    open(mn, "w").write(src)
    return f"#{row}: applied {n}/{len(edits)} trim(s) to {os.path.basename(folder)}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rows")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--cut", type=float, default=0.6)
    args = ap.parse_args()
    if args.rows:
        rows = [int(x) for x in args.rows.split(",")]
    else:
        rows = sorted(int(re.match(r"(\d+)-", os.path.basename(p)).group(1))
                      for p in glob.glob(os.path.join(OUT, "*.json")))

    report, total = [], 0
    for row in rows:
        slug, edits = propose(row, args.cut)
        if not edits:
            continue
        total += len(edits)
        report.append((row, slug, edits))
        if args.apply:
            print(apply_to_build(row, slug, edits))

    if not args.apply:
        with open(os.path.join(OUT, "TRIM-PROPOSALS.md"), "w") as f:
            f.write(f"# RULE-4 TRIM PROPOSALS (sentence-level, cut>={args.cut:.0%})\n\n")
            f.write(f"{total} beat(s) across {len(report)} video(s). Each shows the "
                    "sentences that would be DROPPED (restatement) vs KEPT (teaching). "
                    "Review, then apply with `rule4_trim.py --rows N --apply`.\n\n")
            for row, slug, edits in report:
                f.write(f"## #{row} — {slug}\n\n")
                for beat_id, old, new, keep, dropped in edits:
                    f.write(f"- **{beat_id}**\n")
                    for d in dropped:
                        f.write(f"    - ✂️ DROP: {d}\n")
                    for k in keep:
                        f.write(f"    - ✅ keep: {k}\n")
                f.write("\n")
        print(f"{total} proposed trim(s) across {len(report)} video(s) "
              f"-> TRANSCRIPTS/TRIM-PROPOSALS.md")


if __name__ == "__main__":
    main()
