#!/usr/bin/env python3
"""Generate the v4 REROLL stills for #7 (Peter walks on water) via flow_driver.py
(Nano Banana 2, 9:16, $0). FACE LAW v3 TEXT-ONLY: the JESUS LOCK v3 paragraph is
inline in each shot; NO --ref (the attached bust echoes — playbook, build-99).
Only the five -fix shots from PROMPTS.md's "v4 REROLLS" section are generated;
the seven kept stills are untouched.

Usage:
  python3 gen_stills_flow.py --list        # print shot slugs
  python3 gen_stills_flow.py --print SLUG  # print one full prompt
  python3 gen_stills_flow.py --only SLUG   # generate ONE shot
  python3 gen_stills_flow.py               # generate ALL missing -fix shots
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DRIVER = HERE.parent / "flow_driver.py"
PROMPTS = HERE / "PROMPTS.md"
ASSETS = HERE / "assets"

# The #7 NIGHT style block (never golden-hour) — byte-identical to the sheet header.
STYLE = ('Beautiful hand-painted 2D animation style, reverent and warm, like a classic '
         'illustrated storybook of scripture brought to life. Soft painterly brushstroke '
         'textures, muted earth tones under cool blue moonlight. First-century Judea, the '
         'fourth watch of the night — moonlight, starlight, dark water, never golden-hour '
         'daylight. Sacred, hushed tone. Not photorealistic. No text or captions in the '
         'image. Historically modest clothing: rough-woven wool and linen in undyed earth '
         'colors. No modern objects.')


def parse_shots():
    text = PROMPTS.read_text(encoding="utf-8")
    v4 = text.split("# v4 REROLLS", 1)[1]
    shots = []
    for m in re.finditer(r"^## (s\S+?-fix)[^\n]*\n(.+?)(?=\n## |\Z)", v4, re.S | re.M):
        slug, body = m.group(1), m.group(2).strip()
        body = "\n".join(l for l in body.splitlines()
                         if not l.strip().upper().startswith("REF:"))
        body = body.replace("[STILL STYLE BLOCK]", STYLE)
        body = " ".join(body.split())
        shots.append((slug, body))
    return shots


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--print", dest="show")
    ap.add_argument("--only")
    args = ap.parse_args()

    shots = parse_shots()
    if args.list:
        for slug, _ in shots:
            print(slug)
        return
    if args.show:
        for slug, body in shots:
            if slug == args.show:
                print(body)
                return
        sys.exit(f"no shot {args.show}")

    for slug, body in shots:
        if args.only and slug != args.only:
            continue
        out = ASSETS / f"{slug}.jpeg"
        if out.exists() and not args.only:
            print(f"skip {slug} (exists)")
            continue
        print(f"=== generating {slug} ===", flush=True)
        r = subprocess.run([sys.executable, str(DRIVER), "gen",
                            "--prompt", body, "--out", str(out)])
        if r.returncode != 0:
            sys.exit(f"driver failed on {slug}")


if __name__ == "__main__":
    main()
