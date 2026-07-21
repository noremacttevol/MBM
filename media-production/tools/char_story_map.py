#!/usr/bin/env python3
"""Map every rostered character -> the story numbers they appear ON SCREEN in.

Scripture citations ("John 3:16", "James 1:5", "1 Sam 3") name BOOKS, not people,
so they are stripped before matching — otherwise every gospel quote looks like an
apostle standing in the shot. We match only against the visual prompt text.
"""
import json, os, re, sys, collections

ROOT = os.path.expanduser("~/Desktop/MBM/media-production")
SCRATCH = "/tmp/claude-1000/-home-noremacttevol-Downloads/1f244745-22a7-4cb5-888f-0a43ae0e77ca/scratchpad"
sys.path.insert(0, os.path.join(ROOT, "CHARACTERS"))
from character_refs import find_in_text  # noqa

BOOKS = (r"Matt(?:hew)?|Mark|Luke|John|Acts|Rom(?:ans)?|Cor|Gal|Eph|Phil|Col|"
         r"Thes|Tim|Tit|Heb|Jas|James|Pet(?:er)?|Jude|Rev(?:elation)?|Gen(?:esis)?|"
         r"Ex(?:od(?:us)?)?|Lev|Num|Deut|Josh(?:ua)?|Judg|Ruth|Sam(?:uel)?|Kgs|Kings|"
         r"Chr(?:on)?|Ezra|Neh|Esth|Job|Ps(?:a|alm|alms)?|Prov|Eccl|Song|Isa(?:iah)?|"
         r"Jer(?:emiah)?|Lam|Ezek(?:iel)?|Dan(?:iel)?|Hos(?:ea)?|Joel|Amos|Obad|"
         r"Jonah|Mic|Nah|Hab|Zeph|Hag|Zech|Mal(?:achi)?|D&C|Moro|Alma|Nephi|Morm")

# "John 3:16", "1 Sam 3", "Matt 2:11-12", "(Luke 24)" -> gone
CITE = re.compile(rf"\b(?:[1-3]\s*)?(?:{BOOKS})\b\s*\.?\s*\d+(?::\d+(?:[-–]\d+)?)?", re.I)
# bare "the gospel of John", "the book of James"
OFBOOK = re.compile(rf"\b(?:gospel|book|epistle)\s+of\s+(?:{BOOKS})\b", re.I)

def clean(t):
    return OFBOOK.sub(" ", CITE.sub(" ", t))

by_char = collections.defaultdict(set)
by_build = {}
for b in sorted(os.listdir(ROOT)):
    m = re.match(r"build-(\d+)-", b)
    if not b.startswith("build-") or not m:
        continue
    num = int(m.group(1))
    text = ""
    for fn in ("PROMPTS.md", "gen_stills_flow.py"):   # VISUAL prompt text only
        p = os.path.join(ROOT, b, fn)
        if os.path.exists(p):
            text += open(p, encoding="utf-8", errors="replace").read() + "\n"
    if not text.strip():
        continue
    try:
        found = find_in_text(clean(text))
    except Exception as e:
        print(f"  !! {b}: {e}", file=sys.stderr)
        continue
    by_build[num] = sorted(found)
    for c in found:
        by_char[c].add(num)

out = {c: sorted(v) for c, v in sorted(by_char.items(), key=lambda kv: -len(kv[1]))}
json.dump({"by_char": out, "by_build": by_build},
          open(os.path.join(SCRATCH, "charmap.json"), "w"), indent=1)
print(f"builds scanned: {len(by_build)}   characters on screen: {len(out)}\n")
for c, nums in out.items():
    print(f"{c:24s} {len(nums):3d}  {','.join(map(str, nums))}")
