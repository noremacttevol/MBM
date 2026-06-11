#!/bin/bash
cd /home/noremacttevol/Desktop/Brain/MBM/ministry-sim
export ANTHROPIC_API_KEY="$(grep -E 'ANTHROPIC_API_KEY' ../mobile/.env | head -1 | sed -E 's/.*=//' | tr -d '\"' )"
export MBM_OUT="/home/noremacttevol/Desktop/Brain/MBM/ministry-sim/outputs"
mkdir -p "$MBM_OUT"

for p in catholic_traditional evangelical_born_again spiritual_not_religious grieving_seeker deconstructing_christian; do
  echo "Running: $p"
  python3 run_sim.py --personas "$p" --turns 3 --out "$MBM_OUT" || echo "FAILED: $p"
done

echo "Completed batch 1"
wc -l "$MBM_OUT/trials.jsonl"
