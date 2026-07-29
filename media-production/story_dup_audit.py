#!/usr/bin/env python3
"""Story-level duplicate audit — does any EVENT get told twice (incl. the same
scene from different gospels)? Folder-dedup already ran; this checks CONTENT.

Two signals:
  1. Transcript similarity — TF cosine over content words across every pair of
     videos. A high score = the two narrations cover the same material.
  2. Same scripture reference — rows in QUEUE.md citing the same book+chapter.

Neither proves a duplicate on its own (layering across the three shelves is BY
DESIGN — a chapter re-used for a different audience/purpose is intended; see
STORY-INTEGRITY-LAW). This surfaces candidates for the Planner to judge.

Output: TRANSCRIPTS/STORY-DUP-AUDIT.md
"""
import glob
import json
import math
import os
import re
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "TRANSCRIPTS")

import rule4_scan as R  # content()

# same-scene told across gospels — event keyword sets the Planner should confirm
# are each told ONCE (or intentionally kept distinct per STORY-INTEGRITY-LAW).
KEEP_DISTINCT = {
    (58, 59): "two feedings (5000 vs 4000) — intended distinct",
    (17, 56): "raisings — Lazarus vs widow of Nain — intended distinct",
    (17, 57): "raisings — Lazarus vs Jairus — intended distinct",
    (56, 57): "raisings — Nain vs Jairus — intended distinct",
    (12, 63): "blind healings — Bartimaeus vs man born blind — intended distinct",
}


def load():
    vids = {}
    for p in sorted(glob.glob(os.path.join(OUT, "*.json"))):
        d = json.load(open(p))
        text = " ".join(s["text"] for s in d["segments"])
        vids[d["row"]] = {"slug": d["slug"], "vec": Counter(R.content(text))}
    return vids


def cosine(a, b):
    common = set(a) & set(b)
    if not common:
        return 0.0
    dot = sum(a[w] * b[w] for w in common)
    na = math.sqrt(sum(v * v for v in a.values()))
    nb = math.sqrt(sum(v * v for v in b.values()))
    return dot / (na * nb) if na and nb else 0.0


def queue_refs(path):
    refs = {}
    if not os.path.exists(path):
        return refs
    for line in open(path):
        m = re.match(r"\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|", line)
        if m:
            refs.setdefault(int(m.group(1)),
                            (m.group(2).strip().strip('"'), m.group(3).strip()))
    return refs


def norm_ref(ref):
    m = re.match(r"([\dA-Za-z ]+?)\s*(\d+)", ref)
    return f"{m.group(1).strip().lower()} {m.group(2)}" if m else None


def main():
    vids = load()
    rows = sorted(vids)
    refs = queue_refs(os.path.join(HERE, "QUEUE.md"))

    pairs = []
    for i, a in enumerate(rows):
        for b in rows[i + 1:]:
            s = cosine(vids[a]["vec"], vids[b]["vec"])
            if s >= 0.35:
                pairs.append((s, a, b))
    pairs.sort(reverse=True)

    bychap = defaultdict(list)
    for r, (title, ref) in refs.items():
        nr = norm_ref(ref)
        if nr:
            bychap[nr].append((r, title))
    shared = {k: v for k, v in bychap.items() if len(v) > 1}

    with open(os.path.join(OUT, "STORY-DUP-AUDIT.md"), "w") as f:
        f.write("# STORY DUPLICATE AUDIT (content-level)\n\n")
        f.write("## 1. Most similar transcript pairs (TF cosine >= 0.35)\n\n")
        f.write("High similarity = candidate same-event retelling. Some are "
                "intended-distinct or by-design shelf layering — noted inline.\n\n")
        f.write("| sim | A | B | note |\n|---|---|---|---|\n")
        for s, a, b in pairs[:60]:
            note = KEEP_DISTINCT.get((a, b)) or KEEP_DISTINCT.get((b, a)) or ""
            f.write(f"| {s:.2f} | {a} {vids[a]['slug']} | {b} {vids[b]['slug']} | {note} |\n")
        f.write(f"\n_{len(pairs)} pair(s) at/above 0.35._\n\n")
        f.write("## 2. Rows citing the same book+chapter\n\n")
        f.write("Same chapter can be intended (layering across shelves) — verify "
                "each is TAUGHT distinctly, not re-narrated.\n\n")
        for nr in sorted(shared):
            f.write(f"- **{nr}**: " + "; ".join(f"#{r} {t}" for r, t in shared[nr]) + "\n")
    print(f"{len(pairs)} similar pair(s); {len(shared)} shared-chapter group(s) "
          f"-> TRANSCRIPTS/STORY-DUP-AUDIT.md")
    print("\nTop 15 most-similar pairs:")
    for s, a, b in pairs[:15]:
        note = KEEP_DISTINCT.get((a, b)) or KEEP_DISTINCT.get((b, a)) or ""
        print(f"  {s:.2f}  #{a} {vids[a]['slug']:28s} ~ #{b} {vids[b]['slug']:28s} {note}")


if __name__ == "__main__":
    main()
