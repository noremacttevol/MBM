#!/usr/bin/env python3
"""render_sheet.py — render one character's 3-view reference sheet from SPEC.md.

Parses CHARACTERS/<slug>/SPEC.md, builds the three one-line prompts (style
block + section text), and drives flow_driver.py gen for each view:
  face-front            (no ref, unless the SPEC's face-front header names one)
  three-quarter         (--ref face-front.jpeg)
  full-body             (--ref face-front.jpeg)

Skips views whose jpeg already exists (so a QC reroll = delete the bad jpeg
and run again). Usage:
  python3 CHARACTERS/render_sheet.py <slug> [view]
"""
import re
import subprocess
import sys
from pathlib import Path

MP = Path(__file__).resolve().parent.parent      # media-production/
CH = MP / "CHARACTERS"

VIEWS = ["face-front", "three-quarter", "full-body"]


def parse_spec(slug):
    spec = (CH / slug / "SPEC.md").read_text()
    m = re.search(r"STYLE BLOCK \(prepended[^\n]*\):\n(.*?)\n\n### ", spec, re.S)
    if not m:
        sys.exit(f"{slug}: no style block found")
    style = " ".join(m.group(1).split())
    prompts = {}
    for view in VIEWS:
        vm = re.search(r"### " + view + r"[^\n]*\n(.*?)(?=\n### |\n\*\*Note|\Z)",
                       spec, re.S)
        if not vm:
            sys.exit(f"{slug}: no section for {view}")
        body = " ".join(vm.group(1).split())
        body = body.replace("[STYLE BLOCK]", style)
        prompts[view] = body
        # extra refs named in the section header, e.g. (ref: ../x.jpeg)
        hm = re.search(r"### " + view + r".*?\(refs?:([^)]+)\)", spec)
        prompts[view + "::refs"] = [r.strip() for r in hm.group(1).split("+")] if hm else []
    return prompts


def gen(prompt, out, refs):
    cmd = ["python3", str(MP / "flow_driver.py"), "gen",
           "--prompt", prompt, "--out", str(out)]
    for r in refs:
        cmd += ["--ref", str(r)]
    print(f"  gen -> {out.name}  (refs: {[Path(r).name for r in refs] or 'none'})")
    res = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
    tail = (res.stdout + res.stderr).strip().splitlines()
    print("   ", tail[-1] if tail else "(no output)")
    return res.returncode == 0 and out.exists()


def resolve_ref(slug, token):
    token = token.strip()
    for base in (CH / slug, CH, MP):
        p = (base / token).resolve()
        if p.exists():
            return p
    # tokens like "JESUS-MASTER-REF/jesus-face.jpeg" or "../../JESUS-MASTER-REF/..."
    p = (CH / slug / token).resolve()
    return p


def main():
    slug = sys.argv[1]
    only = sys.argv[2] if len(sys.argv) > 2 else None
    prompts = parse_spec(slug)
    d = CH / slug
    face = d / "face-front.jpeg"
    for view in VIEWS:
        if only and view != only:
            continue
        out = d / f"{view}.jpeg"
        if out.exists():
            print(f"  {out.name} exists — skip (delete to reroll)")
            continue
        refs = [resolve_ref(slug, t) for t in prompts[view + "::refs"]]
        refs = [r for r in refs if r.exists()]
        if view != "face-front" and face.exists() and face not in refs:
            refs.insert(0, face)
        ok = gen(prompts[view], out, refs)
        if not ok:
            sys.exit(f"{slug}/{view}: generation FAILED")
    print(f"{slug}: done")


if __name__ == "__main__":
    main()
