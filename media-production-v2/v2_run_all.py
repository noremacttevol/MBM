#!/usr/bin/env python3
"""v2_run_all.py — keep Flow generating, forever, across every row.

Cameron, 2026-07-29: *"just make all 3000 pictures don't worry about the making the
videos"* / *"dont stop do that to all 200 stories"*.

THE PROBLEM THIS SOLVES. Flow is serial: one picture at a time, ~2.5-3 min each. That
is the hard floor on the whole job, so the only real sin is letting the browser sit
idle. Before this, generation stopped whenever a session stopped to author the next
row's beat map. Now the two run independently:

    this runner  ->  walks every row in order, generates whatever is authored
    the model    ->  authors beats_v2.py for rows that still need one

It RE-SCANS on every pass, so a beat map authored ten minutes from now gets picked up
on the next lap without restarting anything. Rows without a beats_v2.py are skipped
and reported, never guessed at — a machine-written beat map would reproduce exactly
the V1 mistakes V2 exists to fix.

FLOW ONLY (Cameron, 2026-07-29). This shells out to v2_prompt.py --gen, which drives
Flow on his subscription at 2K. There is no API path and none may be added.

Usage:
    nohup python3 media-production-v2/v2_run_all.py > /tmp/v2-run-all.log 2>&1 &
    python3 media-production-v2/v2_run_all.py --dry-run
    python3 media-production-v2/v2_run_all.py --first 50 --last 100
"""
import argparse
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
V2 = os.path.join(ROOT, "media-production-v2")
PROMPT = os.path.join(HERE, "v2_prompt.py")


def beats_of(build_dir):
    """Beat ids + output names for a build, without importing side effects."""
    sys.path.insert(0, HERE)
    from v2_prompt import load_beats  # noqa: E402
    mod = load_beats(build_dir)
    return [(b["id"], b["out"]) for b in mod.BEATS]


def rows():
    out = []
    for d in sorted(os.listdir(V2)):
        p = os.path.join(V2, d)
        if not (d.startswith("build-") and os.path.isdir(p)):
            continue
        try:
            n = int(d.split("-")[1])
        except (IndexError, ValueError):
            continue
        out.append((n, d, p))
    return out


def missing_for(path):
    """Beats with no jpeg on disk yet. Returns None if the row isn't authored."""
    if not os.path.exists(os.path.join(path, "beats_v2.py")):
        return None
    try:
        beats = beats_of(path)
    except SystemExit as e:
        print(f"  ! beats_v2.py unusable: {e}", flush=True)
        return []
    sys.path.insert(0, HERE)
    from v2_prompt import _below_2k  # noqa: E402
    assets = os.path.join(path, "assets")
    miss = []
    for bid, out in beats:
        f = os.path.join(assets, out)
        # Sub-2K counts as MISSING. flow_driver silently falls back to the 1K
        # original when Flow's upscaler is down, and 159 of the first 424 pictures
        # (rows 10-13 entirely) were left at 768x1376 — below the 1080x1920
        # delivery size. Re-pulling them is not optional.
        if not (os.path.exists(f) and os.path.getsize(f) > 50000) or _below_2k(f):
            miss.append(bid)
    return miss


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--first", type=int, default=1)
    ap.add_argument("--last", type=int, default=999)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--idle-sleep", type=int, default=180,
                    help="seconds to wait before re-scanning when nothing is authored")
    a = ap.parse_args()

    lap = 0
    while True:
        lap += 1
        did_work = False
        pending_authoring = []
        for n, slug, path in rows():
            if not (a.first <= n <= a.last):
                continue
            miss = missing_for(path)
            if miss is None:
                pending_authoring.append(n)
                continue
            if not miss:
                continue
            print(f"\n=== lap {lap} · row {n} {slug} · {len(miss)} to generate ===",
                  flush=True)
            if a.dry_run:
                print("   " + " ".join(miss), flush=True)
                did_work = True
                continue
            # One row at a time, one picture at a time — the Flow profile lock
            # enforces serial anyway, and a crash mid-row must never lose the rest.
            r = subprocess.run(
                [sys.executable, PROMPT, path, "--gen", "--only", *miss],
                cwd=ROOT)
            print(f"=== row {n} pass done (exit {r.returncode}) ===", flush=True)
            did_work = True

        if a.dry_run:
            print(f"\nrows still needing beats_v2.py: {pending_authoring}")
            return
        if not did_work:
            print(f"[lap {lap}] nothing generatable. "
                  f"{len(pending_authoring)} row(s) awaiting beats_v2.py: "
                  f"{pending_authoring[:15]}", flush=True)
            time.sleep(a.idle_sleep)


if __name__ == "__main__":
    main()
