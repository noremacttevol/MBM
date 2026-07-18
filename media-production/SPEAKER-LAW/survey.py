#!/usr/bin/env python3
"""Survey every build: segments, which are currently rendered RED, text, CARD_HOLD.

Two build templates exist across the 200:
  A (184 builds) — `KJV = {...}` set in build.py, text from make_narration.SEGMENTS
  B (16 builds)  — 7-tuple SEGMENTS in build.py carrying a per-beat caption_style
Both are parsed here so the speaker migration can see all 438 currently-red beats.
"""
import ast
import glob
import json
import os
import re
import sys

MP = os.path.expanduser("~/Desktop/MBM/media-production")


def _consts(tree):
    out = {}
    for node in tree.body:
        if (isinstance(node, ast.Assign) and len(node.targets) == 1
                and isinstance(node.targets[0], ast.Name)
                and isinstance(node.value, ast.Constant)
                and isinstance(node.value.value, str)):
            out[node.targets[0].id] = node.value.value
    return out


def _lit(item, consts):
    if isinstance(item, ast.Constant):
        return item.value
    if isinstance(item, ast.Name):
        return consts.get(item.id, "@" + item.id)
    try:
        return ast.literal_eval(item)
    except Exception:
        return "<expr>"


def parse_build(d):
    b = os.path.basename(d)
    bp, mp = os.path.join(d, "build.py"), os.path.join(d, "make_narration.py")
    rec = {"dir": b, "template": None, "segments": [], "red": [],
           "card_hold": None, "mp4": None, "err": None}
    try:
        bsrc = open(bp, encoding="utf-8", errors="replace").read()
        rec["template"] = "B" if 'style == "kjv"' in bsrc else "A"

        ch = re.search(r"^CARD_HOLD\s*=\s*([0-9.]+)", bsrc, re.M)
        if ch:
            rec["card_hold"] = float(ch.group(1))
        mp4 = [f for f in os.listdir(d) if f.endswith(".mp4")]
        rec["mp4"] = mp4[0] if mp4 else None

        # narration segments (both templates keep spoken text here)
        if os.path.exists(mp):
            msrc = open(mp, encoding="utf-8", errors="replace").read()
            mtree = ast.parse(msrc)
            mc = _consts(mtree)
            for node in mtree.body:
                if isinstance(node, ast.Assign) and any(
                        isinstance(t, ast.Name) and t.id == "SEGMENTS"
                        for t in node.targets):
                    if isinstance(node.value, (ast.List, ast.Tuple)):
                        for el in node.value.elts:
                            if not isinstance(el, (ast.Tuple, ast.List)):
                                continue
                            v = [_lit(i, mc) for i in el.elts]
                            if len(v) >= 5:
                                rec["segments"].append(
                                    {"id": v[0], "voice": v[1], "rate": v[2],
                                     "pitch": v[3], "text": v[4]})

        if rec["template"] == "A":
            m = re.search(r"^KJV\s*=\s*(\{[^}]*\}|set\(\))", bsrc, re.M)
            if m:
                try:
                    rec["red"] = sorted(ast.literal_eval(m.group(1)))
                except Exception:
                    rec["red"] = re.findall(r'"([^"]+)"', m.group(1))
        else:
            # template B: SEGMENTS in build.py, last field is caption_style
            btree = ast.parse(bsrc)
            bc = _consts(btree)
            for node in btree.body:
                if isinstance(node, ast.Assign) and any(
                        isinstance(t, ast.Name) and t.id == "SEGMENTS"
                        for t in node.targets):
                    if isinstance(node.value, (ast.List, ast.Tuple)):
                        for el in node.value.elts:
                            if not isinstance(el, (ast.Tuple, ast.List)):
                                continue
                            v = [_lit(i, bc) for i in el.elts]
                            if v and v[-1] == "kjv":
                                rec["red"].append(v[0])
    except Exception as e:
        rec["err"] = f"{type(e).__name__}: {e}"
    return rec


def main():
    out = {}
    for d in sorted(glob.glob(os.path.join(MP, "build-*"))):
        if not os.path.isfile(os.path.join(d, "build.py")):
            continue          # skip the duplicate stub folders (row 87 etc.)
        r = parse_build(d)
        out[r["dir"]] = r

    dest = sys.argv[1] if len(sys.argv) > 1 else "survey.json"
    tmp = dest + ".tmp"
    with open(tmp, "w") as f:
        json.dump(out, f, indent=1)
    os.replace(tmp, dest)

    nseg = sum(len(r["segments"]) for r in out.values())
    nred = sum(len(r["red"]) for r in out.values())
    ta = sum(1 for r in out.values() if r["template"] == "A")
    tb = sum(1 for r in out.values() if r["template"] == "B")
    bad = [b for b, r in out.items() if r["err"] or not r["segments"]]
    print(f"builds: {len(out)}  (template A {ta}, template B {tb})")
    print(f"segments: {nseg}   currently-RED beats: {nred}")
    print(f"parse trouble: {len(bad)} -> {bad[:10]}")


if __name__ == "__main__":
    main()
