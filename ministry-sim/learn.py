#!/usr/bin/env python3
"""
learn.py — the refinement intake for MBM.

Hermes (or anyone) runs run_sim.py over and over and piles trials into
outputs/trials.jsonl. That file is the project's durable memory: it survives
sessions and keeps growing even after API credits run out. This script reads the
WHOLE pile and turns it into things a builder can act on:

  1. A rebuilt EvidenceStore (outputs/evidence.json) computed from all history, so the
     app's across-people brain reflects everything ever learned — not just the last run.
  2. A human-readable LEARNINGS.md report: where the minister is strong, where it keeps
     failing, which faithful move fits which kind of person, and the recurring fixes the
     judge asks for — ranked by how often they come up.

Nothing here calls a model or spends credits. It only reads data already gathered.

Usage:
    python3 learn.py                 # reads ./outputs/trials.jsonl
    python3 learn.py --dir ./outputs # explicit directory
"""

import os
import sys
import json
import argparse
import datetime
from collections import defaultdict, Counter

# Import the app's brain so we rebuild the SAME EvidenceStore the app uses.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import knowing_engine as ke


FAITHFULNESS_KEYS = [
    "met_where_they_were", "emotion_before_answer", "asked_more_than_answered",
    "comparison_method", "no_pressure_no_manipulation", "honesty",
    "milk_before_meat", "ministered_when_ready", "left_them_free",
]


def load_trials(path: str):
    """Read every trial line. Skips blank/corrupt lines without dying."""
    trials = []
    if not os.path.exists(path):
        sys.exit(f"No trial data found at {path}. Run run_sim.py first to generate trials.")
    with open(path, "r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                trials.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    if not trials:
        sys.exit(f"{path} exists but has no readable trials yet.")
    return trials


def rebuild_evidence(trials, out_dir: str) -> str:
    """Recompute the across-people EvidenceStore from the full history of trials."""
    store = ke.EvidenceStore(path=os.path.join(out_dir, "evidence.json"))
    store.data = {}  # rebuild from scratch so it reflects ALL data, not just recent runs
    for t in trials:
        situation = t.get("situation")
        approach = t.get("final_approach")
        outcome = t.get("outcome")
        if not (situation and approach and outcome):
            continue
        try:
            store.record_outcome(situation, approach, outcome)
        except ValueError:
            # The store refuses unknown/forbidden outcomes (e.g. 'converted') by design.
            continue
    store.save()
    return store.path


def _avg(nums):
    nums = [n for n in nums if isinstance(n, (int, float))]
    return round(sum(nums) / len(nums), 2) if nums else 0.0


def write_learnings(trials, out_dir: str, store: ke.EvidenceStore) -> str:
    path = os.path.join(out_dir, "LEARNINGS.md")
    stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    n = len(trials)

    overall = _avg([t.get("faithfulness_avg") for t in trials])
    verdicts = Counter(t.get("faithfulness_verdict") for t in trials)

    # Per dimension: where is the minister strong / weak across everything?
    dim_scores = defaultdict(list)
    for t in trials:
        f = t.get("faithfulness", {})
        for k in FAITHFULNESS_KEYS:
            # null/N-A dimensions (e.g. comparison_method when no 'God isn't good'
            # obstacle arose) are excluded so a non-event never drags the average down.
            if isinstance(f.get(k), (int, float)):
                dim_scores[k].append(f[k])
    dim_avgs = {k: _avg(v) for k, v in dim_scores.items()}
    weakest = sorted(dim_avgs.items(), key=lambda x: x[1])[:3]
    strongest = sorted(dim_avgs.items(), key=lambda x: x[1], reverse=True)[:3]

    # Flags raised across the whole pile (these are concrete failures to fix).
    flag_counts = Counter()
    for t in trials:
        for k, v in (t.get("flags") or {}).items():
            # human_offered is good when TRUE; everything else is bad when TRUE.
            if k == "human_offered":
                if not v:
                    flag_counts["human_NOT_offered"] += 1
            elif v:
                flag_counts[k] += 1

    # Per persona/tradition: how are we doing with each kind of person?
    by_persona = defaultdict(list)
    for t in trials:
        by_persona[t.get("persona_label", "?")].append(t.get("faithfulness_avg", 0))

    # Which faithful move fits which situation (from the rebuilt evidence store)?
    situation_best = {}
    for situation in store.data:
        best = store.most_faithful_for(situation, candidates=list(ke.APPROACHES.keys()))
        rates = {a: store.faithful_rate(situation, a) for a in store.data[situation]}
        situation_best[situation] = (best, rates)

    # The journey toward Christ: where people land, and how ready for human handoff.
    journey_counts = Counter(t.get("journey_stage") for t in trials if t.get("journey_stage"))
    connection_counts = Counter(t.get("connection_level") for t in trials if t.get("connection_level"))
    missionary_ready_n = sum(1 for t in trials if t.get("missionary_ready"))
    members_n = sum(1 for t in trials if t.get("is_member"))
    # Ordered so the ladder reads from furthest-from-Him to baptized.
    journey_order = ["UNREACHED", "CURIOUS", "BELIEVES_GOD_GOOD", "OPEN_TO_RESTORATION",
                     "SEEKING_TRUTH", "READY_FOR_MISSIONARIES", "BAPTISM", "DISCIPLE_GROWING"]

    # Recurring fixes the judge asks for — the refinement backlog.
    fixes = [t.get("what_to_fix", "").strip() for t in trials if t.get("what_to_fix")]

    with open(path, "w", encoding="utf-8") as fh:
        fh.write(f"# MBM — Learnings from accumulated trials\n\n_Generated: {stamp}_\n\n")
        fh.write(f"Trials analyzed: **{n}**  |  Overall faithfulness: **{overall}/5**\n\n")
        fh.write(f"Verdicts — pass: {verdicts.get('pass',0)}, "
                 f"borderline: {verdicts.get('borderline',0)}, fail: {verdicts.get('fail',0)}\n\n")

        fh.write("## Where the minister is weakest (fix these first)\n\n")
        for k, v in weakest:
            fh.write(f"- **{k}**: {v}/5\n")
        fh.write("\n## Where the minister is strongest\n\n")
        for k, v in strongest:
            fh.write(f"- **{k}**: {v}/5\n")

        fh.write("\n## Concrete failures flagged across all trials\n\n")
        if flag_counts:
            for k, c in flag_counts.most_common():
                fh.write(f"- **{k}**: {c} of {n} trials\n")
        else:
            fh.write("- None. No manipulation, dishonesty, premature LDS, or missing-human flags.\n")

        fh.write("\n## How we do with each kind of person\n\n")
        for label, scores in sorted(by_persona.items(), key=lambda x: _avg(x[1])):
            fh.write(f"- **{label}**: {_avg(scores)}/5  (n={len(scores)})\n")

        fh.write("\n## Which faithful move fits which person (learned from data)\n\n")
        if situation_best:
            for situation, (best, rates) in sorted(situation_best.items()):
                rate_str = ", ".join(f"{a}={r}" for a, r in rates.items() if r is not None)
                tag = f"best so far: **{best}**" if best else "not enough data yet"
                fh.write(f"- **{situation}** — {tag}  ({rate_str})\n")
        else:
            fh.write("- Not enough data yet.\n")

        fh.write("\n## Journey toward Christ — where people landed\n\n")
        fh.write("_How far people freely traveled. This is observed fruit, not a target the app "
                 "pushes anyone toward._\n\n")
        for stage in journey_order:
            if journey_counts.get(stage):
                fh.write(f"- **{stage}**: {journey_counts[stage]}\n")
        other = [s for s in journey_counts if s not in journey_order]
        for s in other:
            fh.write(f"- **{s}**: {journey_counts[s]}\n")
        fh.write(f"\nMembers (discipleship track): {members_n}  |  "
                 f"Reached missionary-referral readiness: {missionary_ready_n} of {n}\n\n")

        fh.write("## Human-relationship handoff — the app is a helper, not a destination\n\n")
        fh.write("_What the app would surface next to move the person toward real people._\n\n")
        for level in ["AI_ONLY", "HUMAN_APPROVED", "HUMAN_CONVERSATION", "MISSIONARY_REFERRAL"]:
            if connection_counts.get(level):
                fh.write(f"- **{level}**: {connection_counts[level]}\n")

        fh.write("\n## Refinement backlog — recurring fixes the judge asked for\n\n")
        if fixes:
            for i, fx in enumerate(fixes[-20:], 1):  # most recent 20
                fh.write(f"{i}. {fx}\n")
        else:
            fh.write("- None recorded.\n")

        fh.write("\n---\n\n_Faithfulness is the grade; conversion is never tracked or rewarded. "
                 "This report exists so the app keeps getting better at meeting each person the "
                 "way Jesus did._\n")
    return path


def main():
    ap = argparse.ArgumentParser(description="Learn from accumulated MBM trial data.")
    ap.add_argument("--dir", default="./outputs", help="Directory holding trials.jsonl.")
    args = ap.parse_args()

    trials_path = os.path.join(args.dir, "trials.jsonl")
    trials = load_trials(trials_path)

    store = ke.EvidenceStore(path=os.path.join(args.dir, "evidence.json"))
    store_path = rebuild_evidence(trials, args.dir)
    # reload the rebuilt store for reporting
    store = ke.EvidenceStore(path=store_path)

    report_path = write_learnings(trials, args.dir, store)

    print(f"Read {len(trials)} trials from {trials_path}")
    print(f"Rebuilt evidence store: {store_path}")
    print(f"Wrote learnings report: {report_path}")


if __name__ == "__main__":
    main()
