#!/usr/bin/env python3
"""Repo-wide homograph scan. For every build, find homograph words in the CAPTION
text that the build's SPOKEN dict does not explicitly decide. These are the lines
where the TTS is free to pick the wrong reading (tear=cry vs rip, lead=metal vs
guide). Output: build -> undecided homographs + the line each appears in.
"""
import ast, glob, os, re, sys
from mbm_pronounce import HOMOGRAPHS

# words that keep biting KJV readings but were missing from HOMOGRAPHS
EXTRA = {
    "tear", "torn", "rend", "rent", "leadeth", "lead", "leddest",
    "sow", "sowest", "soweth", "bowed", "wounds", "reads", "liveth",
    "number", "moment",  # not homographs — drop if noisy
}
WORDS = {w.lower() for w in HOMOGRAPHS} | {"tear", "torn", "leadeth", "lead"}

_WORD = re.compile(r"[A-Za-z]+")

def load(build):
    """Pull SEGMENTS caption strings and SPOKEN keys from a make_narration.py by
    parsing the AST — no importing/executing the module."""
    path = os.path.join(build, "make_narration.py")
    if not os.path.exists(path):
        return None, None
    src = open(path).read()
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return None, None
    segments, spoken = [], set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            names = [t.id for t in node.targets if isinstance(t, ast.Name)]
            if "SEGMENTS" in names and isinstance(node.value, (ast.List, ast.Tuple)):
                for elt in node.value.elts:
                    if isinstance(elt, (ast.Tuple, ast.List)) and elt.elts:
                        last = elt.elts[-1]
                        if isinstance(last, ast.Constant) and isinstance(last.value, str):
                            segments.append(last.value)
            if "SPOKEN" in names and isinstance(node.value, ast.Dict):
                for k in node.value.keys:
                    if isinstance(k, ast.Constant) and isinstance(k.value, str):
                        spoken.add(k.value.lower())
    return segments, spoken

rows = []
for build in sorted(glob.glob("build-*")):
    segs, spoken = load(build)
    if segs is None:
        continue
    hits = {}
    for text in segs:
        for m in _WORD.finditer(text):
            w = m.group(0).lower()
            if w in WORDS and w not in spoken:
                hits.setdefault(w, text.strip())
    if hits:
        rows.append((build, hits))

print(f"{len(rows)} builds with undecided homographs\n")
for build, hits in rows:
    print(f"### {build}")
    for w, line in hits.items():
        snip = (line[:110] + "…") if len(line) > 110 else line
        print(f"  [{w}]  {snip}")
    print()
