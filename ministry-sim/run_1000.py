#!/usr/bin/env python3
"""
Parallel runner: scale the ministry sim to 1000+ new trials.
Uses ThreadPoolExecutor (not ProcessPool) to stay under the per-user process limit,
and spawns actual run_sim.py subprocess workers so each gets its own API session.

Architecture:
- 1 API call = 1 persona × 1 seed = 1 trial
- ThreadPoolExecutor with N workers runs trials in parallel
- Each trial writes to its own subfolder (p_{persona}_{seed})
- Trials.jsonl is appended per-run, never overwritten
- --resume skips subfolders that already have a trial

Usage:
    python3 run_1000.py --personas outputs/wide --seeds 3 --workers 8 --turns 3
"""
import os
import sys
import json
import time
import argparse
import subprocess
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

HERE = Path("/home/noremacttevol/Desktop/Brain/MBM/ministry-sim")
OUT_BASE = HERE / "outputs"


def load_api_key():
    candidates = [
        HERE / "../mobile/.env",
        HERE / "../server/.env",
    ]
    if os.environ.get("ANTHROPIC_API_KEY"):
        return os.environ["ANTHROPIC_API_KEY"]
    for env_path in candidates:
        if not os.path.exists(env_path):
            continue
        with open(env_path) as f:
            for line in f:
                if "ANTHROPIC_API_KEY" in line and "=" in line:
                    return line.strip().split("=", 1)[1].strip().strip('"').strip("'")
    raise RuntimeError("ANTHROPIC_API_KEY not found")


def load_pool(persona_file):
    """Load persona IDs from a pool file or directory."""
    pf = Path(persona_file)
    if pf.is_file():
        data = json.load(open(pf))
        personas = data.get("personas", data) if isinstance(data, dict) else data
        return [p["id"] for p in personas if p.get("id")]
    elif pf.is_dir():
        # Subfolders named p_{id}
        return [p.name[2:] for p in pf.glob("p_*") if p.is_dir()]
    else:
        raise ValueError(f"Cannot load personas from {persona_file}")


def trial_done(out_dir, pid, seed):
    """Check if this persona×seed already has a trial."""
    f = Path(out_dir) / f"p_{pid}_{seed}" / "trials.jsonl"
    return f.exists() and f.stat().st_size > 0


def run_trial(pid, seed, out_dir, turns, persona_file, api_key):
    sub = Path(out_dir) / f"p_{pid}_{seed}"
    sub.mkdir(parents=True, exist_ok=True)
    env = os.environ.copy()
    env["ANTHROPIC_API_KEY"] = api_key

    t0 = time.time()
    try:
        proc = subprocess.run(
            ["python3", str(HERE / "run_sim.py"),
             "--personas", pid,
             "--persona-file", str(Path(persona_file).resolve() if persona_file else ""),
             "--turns", str(turns),
             "--seed", str(seed),
             "--out", str(sub)],
            capture_output=True, text=True, env=env, cwd=str(HERE),
            timeout=240,
        )
        elapsed = time.time() - t0
        ok = proc.returncode == 0 and trial_done(out_dir, pid, seed)
        err = proc.stderr[:200] if proc.returncode != 0 else ""
        return pid, seed, ok, elapsed, err
    except subprocess.TimeoutExpired:
        return pid, seed, False, time.time() - t0, "TIMEOUT"
    except Exception as e:
        return pid, seed, False, time.time() - t0, str(e)[:200]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--personas", default=str(HERE / "generated_personas_v2.json"),
                    help="Persona pool file or 'outputs/wide' dir")
    ap.add_argument("--seeds", type=int, default=3,
                    help="How many seeds per persona (default 3)")
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--turns", type=int, default=3)
    ap.add_argument("--out", default=str(OUT_BASE / "run_1000"))
    ap.add_argument("--resume", action="store_true",
                    help="Skip trials already done (don't re-run)")
    ap.add_argument("--limit", type=int, default=0,
                    help="Max total trials (0 = unlimited)")
    args = ap.parse_args()

    api_key = load_api_key()
    Path(args.out).mkdir(parents=True, exist_ok=True)

    # Build work list
    pool_ids = load_pool(args.personas)
    seeds = list(range(1, args.seeds + 1))

    work = [(pid, seed) for pid in pool_ids for seed in seeds]
    if args.resume:
        work = [(pid, seed) for pid, seed in work if not trial_done(args.out, pid, seed)]

    if args.limit:
        work = work[:args.limit]

    done_already = len(load_pool(args.personas)) * args.seeds - len(work)
    total = len(work)

    print(f"Pool: {len(pool_ids)} personas × {args.seeds} seeds = {total + done_already} total "
          f"({done_already} already done, {total} to run)", flush=True)
    print(f"Workers: {args.workers} | Turns: {args.turns} | Output: {args.out}", flush=True)

    if not work:
        print("Nothing to do — all trials already complete.")
        return

    completed = 0
    successes = 0
    t_start = time.time()

    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        futures = {
            ex.submit(run_trial, pid, seed, args.out, args.turns, args.personas, api_key): (pid, seed)
            for pid, seed in work
        }
        for fut in as_completed(futures):
            pid, seed = futures[fut]
            p, s, ok, elapsed, err = None, None, False, 0, ""
            try:
                p, s, ok, elapsed, err = fut.result()
            except Exception as e:
                err = str(e)[:100]

            completed += 1
            if ok:
                successes += 1

            rate = successes / completed * 100 if completed > 0 else 0
            elapsed_str = f"{elapsed:.0f}s"
            flag = "OK" if ok else "ERR"
            pname = (p[:35] if p else pid[:35]) if p else str(pid)[:35]
            print(f"[{completed:3d}/{total}] {flag} {pname:35s} s={s} {elapsed_str:6s} "
                  f"(running avg success: {rate:.0f}%) {err[:80] if err else ''}", flush=True)

    total_elapsed = time.time() - t_start
    print(f"\nDone: {successes}/{total} succeeded in {total_elapsed/60:.1f} min "
          f"({total/max(1,total_elapsed)*60:.1f} trials/min)", flush=True)

    # Append all new trials to canonical trials.jsonl
    canonical = OUT_BASE / "trials.jsonl"
    new_trials = 0
    for sub in Path(args.out).glob("p_*"):
        tf = sub / "trials.jsonl"
        if tf.exists() and tf.stat().st_size > 0:
            with open(canonical, "a") as dst:
                with open(tf) as src:
                    for line in src:
                        line = line.strip()
                        if line:
                            dst.write(line + "\n")
                            new_trials += 1

    print(f"Appended {new_trials} new trials to {canonical}")
    print(f"New canonical total: "
          f"{sum(1 for _ in open(canonical))} trials")


if __name__ == "__main__":
    main()
