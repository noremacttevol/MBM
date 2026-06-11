#!/usr/bin/env python3
"""Parallel batch runner to finish 100 trials quickly."""

import subprocess
import os
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor, as_completed

cd_path = "/home/noremacttevol/Desktop/Brain/MBM/ministry-sim"

# Load API key
env_path = Path(cd_path) / "../mobile/.env"
with open(env_path) as f:
    api_key = None
    for line in f:
        if "ANTHROPIC_API_KEY" in line:
            api_key = line.strip().split("=", 1)[1].strip('"')
            break

if not api_key:
    raise RuntimeError("ANTHROPIC_API_KEY not found")

personas = [
    "calvinist_reformed", "baptist_devout", "secular_agnostic",
    "atheist_skeptic", "exmormon_falling_away", "catholic_traditional",
    "evangelical_born_again", "spiritual_not_religious",
    "grieving_seeker", "deconstructing_christian"
]

def run_trial(args):
    """Run one trial and return result."""
    persona, turn_idx = args
    os.chdir(cd_path)
    
    env = os.environ.copy()
    env["ANTHROPIC_API_KEY"] = api_key
    
    # Use unique subfolder for each parallel run
    outdir = f"outputs/p_{persona}_{turn_idx}"
    os.makedirs(outdir, exist_ok=True)
    
    proc = subprocess.run(
        ["python3", "run_sim.py", "--personas", persona, "--turns", "2", "--out", outdir],
        capture_output=True, text=True, env=env
    )
    
    verdict = "pass"
    if "borderline" in proc.stdout or "failed" in proc.stdout:
        verdict = "borderline"
    
    return (persona, turn_idx, verdict, proc.returncode == 0)

def copy_to_main_outputs():
    """Copy all trial results to main outputs folder."""
    os.chdir(cd_path)
    
    # Append to main trials.jsonl
    main_trials = Path("outputs/trials.jsonl")
    
    for p_sub in Path("outputs").glob("p_*"):
        if p_sub.is_dir():
            trials_file = p_sub / "trials.jsonl"
            if trials_file.exists():
                with open(main_trials, "a") as mainf:
                    with open(trials_file) as src:
                        mainf.write(src.read())

def main():
    print(f"Starting 30 parallel passes (300 trials)...")
    
    # Create args for 30 passes of all 10 personas = 300 trials
    args_list = [(p, t) for t in range(1, 31) for p in personas]
    
    results = []
    with ProcessPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(run_trial, arg) for arg in args_list]
        for i, future in enumerate(as_completed(futures), 1):
            persona, turn_idx, verdict, success = future.result()
            status = "✓" if success else "✗"
            print(f"{i:2d}/{len(args_list)} {status} {persona[:25]:25s} ({turn_idx}) -> {verdict}")
            results.append((persona, turn_idx, verdict, success))
    
    # Copy all results to main outputs
    print("\nCopying results to main outputs folder...")
    copy_to_main_outputs()
    
    # Count total
    main_trials = Path(cd_path) / "outputs/trials.jsonl"
    with open(main_trials) as f:
        total = sum(1 for _ in f)
    
    success_count = sum(1 for r in results if r[3])
    print(f"\n*** COMPLETED: {total} total trials ***")
    print(f"Success: {success_count}/{len(results)}")

if __name__ == "__main__":
    main()
