#!/usr/bin/env python3
"""Generate the #11 stills on Flow (Nano Banana, 9:16, $0) from the SAME shot
data that writes PROMPTS.md, so the file Cameron reads and the prompt the model
gets can never drift apart.

CHARACTER LAW: a shot tagged [<NAME> SHEET] gets that character's locked spec
text AND their reference jpegs attached as --ref. FACE LAW v3: Jesus is text-
locked only — no --ref (an attached bust echoes into the picture, playbook).

  python3 gen_stills_flow.py --list
  python3 gen_stills_flow.py --print s3b-boat-filling
  python3 gen_stills_flow.py --only s3b-boat-filling
  python3 gen_stills_flow.py --all          # every shot, overwriting
  python3 gen_stills_flow.py                # only shots with no jpeg yet
"""
import argparse
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DRIVER = HERE.parent / "flow_driver.py"
ASSETS = HERE / "assets"
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent / "CHARACTERS"))

from write_prompts import SHOTS, LOCKS, STYLE, PANEL, QUALITY  # noqa: E402
from character_refs import refs as _refs  # noqa: E402

SHEET_SLUG = {"PETER SHEET": "peter", "ANDREW SHEET": "andrew",
              "JAMES SHEET": "james", "JOHN SHEET": "john-beloved"}


def prompt_for(slug):
    for s, head, locks, scene in SHOTS:
        if s == slug:
            parts = []
            for lk in locks:
                txt = LOCKS[lk]
                # the REF: line is a gate marker for PROMPTS.md, not prompt text
                txt = " ".join(l for l in txt.splitlines()
                               if not l.strip().upper().startswith("REF:"))
                parts.append(" ".join(txt.split()))
            body = " ".join([PANEL] + parts + [STYLE, scene, QUALITY])
            return " ".join(body.split())
    raise SystemExit(f"no shot {slug}")


def refs_for(slug):
    for s, _h, locks, _sc in SHOTS:
        if s == slug:
            sheets = [SHEET_SLUG[l] for l in locks if l in SHEET_SLUG]
            if not sheets:
                return []
            # Flow gets slow and literal with a big pile of refs. One face per
            # character once three or more are locked into the same picture;
            # the full three-view sheet when it is only one or two men.
            per = 1 if len(sheets) >= 3 else 3
            out = []
            for name in sheets:
                out += [str(p) for p in _refs(name)[:per]]
            return out
    return []


def gen(slug):
    out = ASSETS / f"{slug}.jpeg"
    cmd = [sys.executable, str(DRIVER), "gen", "--prompt", prompt_for(slug),
           "--out", str(out)]
    for r in refs_for(slug):
        cmd += ["--ref", r]
    print(f"=== generating {slug}  ({len(refs_for(slug))} refs) ===", flush=True)
    rc = subprocess.run(cmd).returncode
    return rc == 0 and out.exists()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--print", dest="pr")
    ap.add_argument("--only", action="append", default=[])
    ap.add_argument("--all", action="store_true")
    a = ap.parse_args()
    ASSETS.mkdir(parents=True, exist_ok=True)
    if a.list:
        for s, _h, locks, _sc in SHOTS:
            print(s, "|", ",".join(l for l in locks if l in SHEET_SLUG) or "-")
        return
    if a.pr:
        print(prompt_for(a.pr))
        return
    todo = a.only or [s for s, _h, _l, _sc in SHOTS
                      if a.all or not (ASSETS / f"{s}.jpeg").exists()]
    failed = [s for s in todo if not gen(s)]
    if failed:
        sys.exit("FAILED: " + ", ".join(failed))
    print("ALL STILLS GENERATED")


if __name__ == "__main__":
    main()
