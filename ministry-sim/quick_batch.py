#!/usr/bin/env python3
"""Quick batch runner. Run 80+ trials to reach 100 total."""

import subprocess
import os
from pathlib import Path

cd_path = "/home/noremacttevol/Desktop/Brain/MBM/ministry-sim"

# Load API key correctly
env_path = Path(cd_path) / "../mobile/.env"
with open(env_path) as f:
    api_key = None
    for line in f:
        if "ANTHROPIC_API_KEY" in line:
            api_key = line.strip().split("=", 1)[1].strip('"')
            break

personas = [
    "calvinist_reformed", "baptist_devout", "secular_agnostic",
    "atheist_skeptic", "exmormon_falling_away", "catholic_traditional",
    "evangelical_born_again", "spiritual_not_religious",
    "grieving_seeker", "deconstructing_christian"
]

# Run 8 more passes (80 trials) to reach 100+
for pass_num in range(1, 9):
    print(f"\n=== PASS {pass_num} ===")
    for i, p in enumerate(personas):
        os.chdir(cd_path)
        env = os.environ.copy()
        env["ANTHROPIC_API_KEY"] = api_key
        
        proc = subprocess.run(
            ["python3", "run_sim.py", "--personas", p, "--turns", "2", "--out", "outputs"],
            capture_output=True, text=True, env=env
        )
        
        verdict = "pass"
        if "borderline" in proc.stdout or "failed" in proc.stdout:
            verdict = "borderline"
        
        print(f"  {i+1:2d}. {p[:25]:25s} -> {verdict}")
    
    # Read current count
    trials_file = Path(cd_path) / "outputs/trials.jsonl"
    if trials_file.exists():
        with open(trials_file) as f:
            count = sum(1 for _ in f)
        print(f"  Total: {count} trials")

# Final
trials_file = Path(cd_path) / "outputs/trials.jsonl"
with open(trials_file) as f:
    final = sum(1 for _ in f)
print(f"\n*** FINAL COUNT: {final} ***")
