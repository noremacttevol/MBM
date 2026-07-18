#!/usr/bin/env python3
"""Build full Flow prompts for #64 (pool of Bethesda) from PROMPTS.md and generate
stills via flow_driver.py (Nano Banana 2, 9:16, $0). FACE LAW v3 TEXT-ONLY: the
JESUS LOCK v3 paragraph is inline in each Jesus shot; NO --ref (the attached bust
echoes — playbook). Continuity locks ([INFIRM-MAN LOCK], [BETHESDA-SETTING LOCK])
are parsed from PROMPTS.md's CONTINUITY LOCKS section and expanded per shot.

Usage:
  python gen_stills_flow.py --list        # print shot slugs
  python gen_stills_flow.py --print SLUG  # print one full prompt
  python gen_stills_flow.py --only SLUG   # generate ONE shot
  python gen_stills_flow.py               # generate ALL missing shots
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

# COSMIC STYLE (Cameron denial #181, 2026-07-18: "the pictures need to be better
# made i dont think they fit the story well"). The shared house style block says
# "First-century Judea" and "historically modest clothing" — correct for the gospel
# stories, but this video is Job 38, BEFORE the earth's foundations were laid. Those
# two clauses dragged every cosmic prompt back to earth: s3 came out a Judean village
# with olive trees and s5 came out a full NATIVITY. The setting clauses are replaced
# with the creation setting; the painterly look is kept byte-for-byte so this video
# still matches the rest of the 200.
STYLE = 'Beautiful hand-painted 2D animation style, reverent and warm, like a classic illustrated storybook of scripture brought to life. Soft painterly brushstroke textures, glowing golden light, deep blue-black cosmic tones with warm gold highlights. The creation itself, seen from the deep of space BEFORE the earth was finished — painted starfields, nebulae and newborn light at cosmic scale. Sacred, hushed tone. Not photorealistic. No text or captions in the image. There is NO landscape, NO ground, NO horizon line, NO buildings, NO village, NO houses, NO trees, NO animals, NO people, NO human figures, NO infant, NO manger and NO nativity anywhere in the image — nothing of the earth has been made yet. Sky, stars and light only. No modern objects.'


def parse_locks(text):
    locks = {}
    for m in re.finditer(r"^\[([A-Z][A-Z -]+ LOCK)\] = (.+?)(?=\n\n|\n\[|\n---)", text, re.S | re.M):
        locks[m.group(1)] = m.group(1) + ": " + " ".join(m.group(2).split())
    return locks


def parse_shots():
    text = PROMPTS.read_text(encoding="utf-8")
    locks = parse_locks(text)
    shots = []
    for m in re.finditer(r"^## (s\S+)[^\n]*\n(.+?)(?=\n## |\n### |\Z)", text, re.S | re.M):
        slug, body = m.group(1), m.group(2).strip()
        body = "\n".join(l for l in body.splitlines() if not l.strip().upper().startswith("REF:"))
        if "[STILL STYLE BLOCK]" not in body:
            continue
        body = body.replace("[STILL STYLE BLOCK]", STYLE)
        for name, val in locks.items():
            body = body.replace(f"[{name}]", val)
        body = " ".join(body.split())
        shots.append((slug, body))
    return shots


def gen(slug, body):
    out = ASSETS / f"{slug}.jpeg"
    print(f"=== generating {slug} ===", flush=True)
    r = subprocess.run([sys.executable, str(DRIVER), "gen", "--prompt", body, "--out", str(out)])
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
                sys.exit(0 if gen(s, b) else 1)
        sys.exit(f"no shot {args.only}")
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
