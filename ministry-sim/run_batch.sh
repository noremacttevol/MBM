#!/bin/bash
cd /home/noremacttevol/Desktop/Brain/MBM/ministry-sim
export ANTHROPIC_API_KEY=*** -E 'ANTHROPIC_API_KEY' ../mobile/.env | head -1 | sed -E 's/.*=//' | tr -d '\"' )"
export MBM_OUT="/home/noremacttevol/Desktop/Brain/MBM/ministry-sim/outputs"
mkdir -p "$MBM_OUT"

PERSONAS="calvinist_reformed baptist_devout secular_agnostic atheist_skeptic exmormon_falling_away catholic_traditional evangelical_born_again spiritual_not_religious grieving_seeker deconstructing_christian"

for p in $PERSONAS; do
  echo "Running: $p"
  python3 run_sim.py --personas "$p" --turns 2 --out "$MBM_OUT" || echo "FAILED: $p"
done

echo "Batch done"
wc -l "$MBM_OUT/trials.jsonl"
