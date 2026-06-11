#!/usr/bin/env python3
"""
parallel_wide.py — run the ministry simulation against the WIDE generated persona
pool (generated_personas.json), in parallel, into a fresh output folder.

Why this exists:
  The old parallel_batch.py was hardcoded to the same 10 built-in personas and
  appended into the canonical trials.jsonl. That is exactly how the test kept
  getting "stuck on 10 people." This driver instead:
    - reads every persona id out of the generated pool file,
    - runs each one as its own run_sim.py process (so they parallelize),
    - writes each into its own subfolder under a FRESH output dir,
    - is RESUMABLE: a persona whose subfolder already holds a trial is skipped,
    - uses a fixed --seed so the run is reproducible (Hermes's fairness point),
    - at the end, concatenates every per-persona trials.jsonl into one
      <out>/trials.jsonl for verify_report.py to read.

Usage:
  python3 parallel_wide.py --pool generated_personas.json --out outputs/wide \
      --turns 3 --workers 6 --seed 42 [--limit N]
"""

import os
import sys
import json
import argparse
import subprocess
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

HERE = Path("/home/noremacttevol/Desktop/Brain/MBM/ministry-sim")


def load_api_key():
    if os.environ.get("ANTHROPIC_API_KEY"):
        return os.environ["ANTHROPIC_API_KEY"]
    env_path = HERE / "../mobile/.env"
    with open(env_path) as f:
        for line in f:
            if "ANTHROPIC_API_KEY" in line and "=" in line:
                return line.strip().split("=", 1)[1].strip().strip('"').strip("'")
    raise RuntimeError("ANTHROPIC_API_KEY not found")


def persona_ids(pool_path):
    data = json.load(open(pool_path))
    return [p["id"] for p in data.get("personas", []) if p.get("id")]


def already_done(out_dir, pid):
    """A persona is done if its subfolder holds a non-empty trials.jsonl."""
    f = Path(out_dir) / f"p_{pid}" / "trials.jsonl"
    return f.exists() and f.stat().st_size > 0


def run_one(pid, pool_path, out_dir, turns, seed, api_key):
    sub = Path(out_dir) / f"p_{pid}"
    sub.mkdir(parents=True, exist_ok=True)
    env = os.environ.copy()
    env["ANTHROPIC_API_KEY"] = api_key
    proc = subprocess.run(
        ["python3", str(HERE / "run_sim.py"),
         "--personas", pid,
         "--persona-file", str(pool_path),
         "--turns", str(turns),
         "--seed", str(seed),
         "--out", str(sub)],
        capture_output=True, text=True, env=env, cwd=str(HERE),
    )
    ok = proc.returncode == 0 and already_done(out_dir, pid)
    tail = (proc.stderr or proc.stdout or "").strip().splitlines()
    note = tail[-1][:120] if tail else ""
    return pid, ok, note


def concatenate(out_dir):
    out_dir = Path(out_dir)
    combined = out_dir / "trials.jsonl"
    n = 0
    with open(combined, "w") as dst:
        for sub in sorted(out_dir.glob("p_*")):
            tf = sub / "trials.jsonl"
            if tf.exists():
                for line in open(tf):
                    line = line.strip()
                    if line:
                        dst.write(line + "\n")
                        n += 1
    return combined, n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pool", default=str(HERE / "generated_personas.json"))
    ap.add_argument("--out", default=str(HERE / "outputs/wide"))
    ap.add_argument("--turns", type=int, default=3)
    ap.add_argument("--workers", type=int, default=6)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--limit", type=int, default=0, help="Only run the first N not-yet-done personas (0 = all).")
    args = ap.parse_args()

    api_key = load_api_key()
    Path(args.out).mkdir(parents=True, exist_ok=True)

    ids = persona_ids(args.pool)
    todo = [pid for pid in ids if not already_done(args.out, pid)]
    if args.limit:
        todo = todo[: args.limit]

    done_already = len(ids) - len([p for p in ids if not already_done(args.out, p)])
    print(f"Pool has {len(ids)} personas. Already done: {done_already}. "
          f"Running now: {len(todo)} (workers={args.workers}, turns={args.turns}, seed={args.seed}).",
          flush=True)

    completed = 0
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        futs = {ex.submit(run_one, pid, args.pool, args.out, args.turns, args.seed, api_key): pid
                for pid in todo}
        for fut in as_completed(futs):
            pid, ok, note = fut.result()
            completed += 1
            flag = "OK " if ok else "ERR"
            print(f"[{completed}/{len(todo)}] {flag} {pid[:40]:40s} {note}", flush=True)

    combined, n = concatenate(args.out)
    print(f"\nCombined {n} trials -> {combined}", flush=True)


if __name__ == "__main__":
    main()
