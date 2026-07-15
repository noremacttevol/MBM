#!/usr/bin/env python3
"""Build full Flow prompts for #101 from PROMPTS.md and generate stills via
flow_driver.py (Nano Banana 2, $0). No Jesus figure in this video, so no --ref.

Usage:
  python3 gen_stills_flow.py --list                 # print shot slugs
  python3 gen_stills_flow.py --print s1-...          # print one full prompt
  python3 gen_stills_flow.py --only s1-...           # generate ONE shot
  python3 gen_stills_flow.py                         # generate ALL missing shots
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
DRIVER = HERE.parent / "flow_driver.py"
MASTER_REF = HERE.parent / "JESUS-MASTER-REF" / "jesus-face.jpeg"
JESUS_SHOTS = set()  # scene shots are prompt-driven (LOCK v3); a bust-portrait --ref makes Nano Banana copy the portrait instead of composing the scene (Machine C 2026-07-15)
PROMPTS = HERE / "PROMPTS.md"
ASSETS = HERE / "assets"

STYLE = 'Beautiful hand-painted 2D animation style, reverent and warm, like a classic illustrated storybook of scripture brought to life. Soft painterly brushstroke textures, glowing golden light, muted earth tones with warm gold highlights. First-century Judea. Sacred, hushed tone. Not photorealistic. No text or captions in the image. Historically modest clothing: rough-woven wool and linen in undyed earth colors. No modern objects.'


def parse_shots():
    text = PROMPTS.read_text()
    shots = []
    for m in re.finditer(r"^## (\S+)[^\n]*\n(.+?)(?=\n## |\Z)", text, re.S | re.M):
        slug, body = m.group(1), m.group(2).strip()
        # keep only the actual image-prompt line(s); drop REF: marker lines
        body = "\n".join(l for l in body.splitlines() if not l.strip().upper().startswith("REF:"))
        if "[STILL STYLE BLOCK]" not in body:
            continue
        body = body.replace("[STILL STYLE BLOCK]", STYLE)
        body = " ".join(body.split())
        shots.append((slug, body))
    return shots


def gen(slug, body):
    out = ASSETS / f"{slug}.jpeg"
    cmd = ["python3", str(DRIVER), "gen", "--prompt", body, "--out", str(out)]
    if slug in JESUS_SHOTS:
        cmd += ["--ref", str(MASTER_REF)]
    print(f"=== generating {slug} ===", flush=True)
    r = subprocess.run(cmd)
    return r.returncode == 0 and out.exists()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--print", dest="pr")
    ap.add_argument("--only")
    args = ap.parse_args()
    shots = parse_shots()
    ASSETS.mkdir(parents=True, exist_ok=True)
    if args.list:
        for s, _ in shots:
            print(s)
        return
    if args.pr:
        for s, b in shots:
            if s == args.pr:
                print(b)
        return
    if args.only:
        for s, b in shots:
            if s == args.only:
                ok = gen(s, b)
                sys.exit(0 if ok else 1)
        sys.exit(f"no shot {args.only}")
    # all missing
    failed = []
    for s, b in shots:
        if (ASSETS / f"{s}.jpeg").exists():
            print(f"skip {s} (exists)")
            continue
        if not gen(s, b):
            failed.append(s)
    if failed:
        sys.exit("FAILED: " + ", ".join(failed))
    print("ALL STILLS GENERATED")


if __name__ == "__main__":
    main()
