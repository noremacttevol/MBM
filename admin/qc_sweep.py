#!/usr/bin/env python3
"""Run the QC gate across every build and write media-production/QC-STATUS.json —
the board's source of truth for "is this video actually ready for Cameron."

Each entry: { "pass": bool, "reasons": [...], "mp4": name, "whisper": bool }.
Default is the FAST gate (voice sample-rate + transcript echo + playable +
complete) so a full sweep finishes quickly; that already catches every old-voice
and every echoing-script cut. Pass --deep to also run the whisper audio-truth
pass on the builds that pass fast (slow; use for a final confirmation sweep).

Usage:
  python3 admin/qc_sweep.py            # fast sweep of all builds
  python3 admin/qc_sweep.py --deep     # + whisper on the fast-passers
  python3 admin/qc_sweep.py 1 3 6      # only these build numbers
"""
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import qc_gate  # noqa: E402

REPO = qc_gate.REPO
MP = qc_gate.MP
OUT = os.path.join(MP, "QC-STATUS.json")


def build_num(path):
    m = re.search(r"build-(\d+)-", os.path.basename(path))
    return int(m.group(1)) if m else None


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    deep = "--deep" in sys.argv
    only = {int(a) for a in args} if args else None

    dirs = sorted(glob.glob(os.path.join(MP, "build-[0-9]*")))
    status = {}
    passed = blocked = 0
    for d in dirs:
        n = build_num(d)
        if n is None or (only and n not in only):
            continue
        if not os.path.exists(os.path.join(d, "make_narration.py")):
            continue
        # fast first — cheap, and a fast failure needs no whisper
        res = qc_gate.gate(d, fast=True)
        if res["pass"] and deep:
            res = qc_gate.gate(d, fast=False)
        status[str(n)] = {
            "pass": res["pass"],
            "reasons": res["reasons"],
            "mp4": res.get("mp4", ""),
            "whisper": res.get("whisper", False),
        }
        if res["pass"]:
            passed += 1
        else:
            blocked += 1
            head = res["reasons"][0] if res["reasons"] else "?"
            print(f"BLOCK {n:>3}: {head}")
    # merge into any existing file (so a numbers-only run updates just those)
    prev = {}
    if os.path.exists(OUT):
        try:
            prev = json.load(open(OUT))
        except Exception:
            prev = {}
    prev.update(status)
    tmp = OUT + ".tmp"
    json.dump(prev, open(tmp, "w"), indent=1, sort_keys=True)
    os.replace(tmp, OUT)
    print(f"\nQC sweep: {passed} PASS, {blocked} BLOCK "
          f"({'deep' if deep else 'fast'}) -> {os.path.relpath(OUT, REPO)}")


if __name__ == "__main__":
    main()
