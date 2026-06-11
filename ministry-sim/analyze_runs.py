#!/usr/bin/env python3
"""Analyze all trials and generate a comprehensive report."""

import json
import os
import argparse
from pathlib import Path
from collections import Counter, defaultdict
from typing import Dict, List, Any

# Import our modules
from evidence_store import EvidenceStore, load_trials_from_jsonl, rebuild_evidence_store
from approaches import APPROACHES, all_approach_names


def analyze_trials(args: Any) -> None:
    """Main analysis function."""
    
    # Load all trials
    trials = load_trials_from_jsonl(args.out)
    
    if not trials:
        print("No trials found. Run ministry-sim first.")
        return
    
    print("=" * 70)
    print(f"MINISTRY-SIM ANALYSIS REPORT: {len(trials)} trials")
    print("=" * 70)
    
    # 1. Overall statistics
    print("\n## OVERALL STATISTICS")
    print("-" * 40)
    
    outcomes = Counter(t.get("outcome", "unknown") for t in trials)
    total = len(trials)
    faithful = sum(outcomes.get(f, 0) for f in ["faithful_more_open", "faithful_walkaway"])
    faith_rate = faithful / total * 100 if total > 0 else 0
    
    print(f"Total trials: {total}")
    print(f"Faithful outcomes: {faithful} ({faith_rate:.1f}%)")
    print("\nOutcome breakdown:")
    for outcome, count in outcomes.most_common():
        pct = count / total * 100
        print(f"  {outcome:30s}: {count:3d} ({pct:5.1f}%)")
    
    # 2. Situation distribution
    print("\n## SITUATION DISTRIBUTION")
    print("-" * 40)
    situations = Counter(t.get("situation", "unknown") for t in trials)
    for situation, count in situations.most_common():
        pct = count / total * 100
        print(f"  {situation:35s}: {count:3d} ({pct:5.1f}%)")
    
    # 3. Persona coverage (how evenly distributed)
    print("\n## PERSONA COVERAGE")
    print("-" * 40)
    personas = Counter(t.get("persona_label", "unknown") for t in trials)
    for persona, count in personas.most_common():
        pct = count / total * 100
        print(f"  {persona:45s}: {count:2d} ({pct:5.1f}%)")
    
    # 4. Evidence store analysis
    print("\n## EVIDENCE STORE ANALYSIS")
    print("-" * 40)
    
    store = rebuild_evidence_store(trials)
    
    for situation in store.all_situations():
        approaches_for_sit = store.data.get(situation, {})
        if not approaches_for_sit:
            continue
        
        # Calculate best approach for this situation
        best_approach = store.best_approach(situation, min_trials=2)
        
        print(f"\n  Situation: {situation}")
        print(f"  Best known approach: {best_approach}")
        
        # Show all approaches tried for this situation
        for approach, bucket in approaches_for_sit.items():
            good = bucket.get("good", 0)
            bad = bucket.get("bad", 0)
            total_trials = good + bad
            rate = good / total_trials * 100 if total_trials > 0 else 0
            print(f"    {approach:25s}: {good:2d}/{bad:2d} ({rate:5.1f}% faithful, n={total_trials})")
    
    # 5. Journey stages reached
    print("\n## JOURNEY PROGRESS")
    print("-" * 40)
    
    stages = Counter(t.get("journey_stage", "unknown") for t in trials)
    stage_order = [
        "UNREACHED", "CURIOUS", "SEEKING_TRUTH", "BELIEVES_GOD_GOOD",
        "OPEN_TO_RESTORATION", "DISCIPLE_GROWING", "DISCIPLE_ACTIVE",
        "EVANGELISM_SHARED"
    ]
    
    for stage in stage_order:
        count = stages.get(stage, 0)
        pct = count / total * 100 if total > 0 else 0
        symbol = "→" if count > 0 else " "
        print(f"  {symbol} {stage:30s}: {count:3d} ({pct:5.1f}%)")
    
    # 6. Human handoff readiness
    print("\n## HUMAN HANDOFF ANALYSIS")
    print("-" * 40)
    
    missionary_ready = [t for t in trials if t.get("missionary_ready")]
    handoff_count = len(missionary_ready)
    handoff_rate = handoff_count / total * 100 if total > 0 else 0
    
    print(f"Missionary-ready handoffs: {handoff_count}/{total} ({handoff_rate:.1f}%)")
    
    # Breakdown by recommended level
    levels = Counter(t.get("recommended_level", "unknown") for t in trials if t.get("missionary_ready"))
    if levels:
        print("\nHandoff levels:")
        for level, count in levels.most_common():
            pct = count / handoff_count * 100 if handoff_count > 0 else 0
            print(f"  {level:20s}: {count:2d} ({pct:5.1f}%)")
    
    # 7. Per-situation faithful rates
    print("\n## SITUATION SUCCESS METRICS")
    print("-" * 40)
    
    situ_outcomes = defaultdict(lambda: {"good": 0, "bad": 0, "total": 0})
    for t in trials:
        sit = t.get("situation", "unknown")
        outcome = t.get("outcome", "unknown")
        situ_outcomes[sit]["total"] += 1
        if outcome in ["faithful_more_open", "faithful_walkaway"]:
            situ_outcomes[sit]["good"] += 1
        elif outcome in ["lost_by_pressure", "lost_by_dishonesty", "lost_unmet"]:
            situ_outcomes[sit]["bad"] += 1
    
    print("\nBy situation (faithful outcomes):")
    for sit, counts in sorted(situ_outcomes.items(), key=lambda x: -x[1]["total"]):
        if counts["total"] == 0:
            continue
        good_rate = counts["good"] / counts["total"] * 100
        bad_rate = counts["bad"] / counts["total"] * 100
        print(f"  {sit:30s}: {good_rate:5.1f}% good / {bad_rate:5.1f}% bad (n={counts['total']})")
    
    # 8. Connection quality metrics
    print("\n## CONNECTION QUALITY METRICS")
    print("-" * 40)
    
    # Extract connection data from trials
    connections = [t.get("connection", {}) for t in trials if t.get("connection")]
    
    if connections:
        # Count by connection_level_recommended
        levels = Counter(c.get("connection_level_recommended", "unknown") for c in connections)
        print("\nConnection level recommendations:")
        for level, count in levels.most_common():
            pct = count / len(connections) * 100
            print(f"  {level:25s}: {count:2d} ({pct:5.1f}%)")
        
        # Average connection scores
        trust_scores = [c.get("trust_score", 0) for c in connections if c.get("trust_score") is not None]
        openness_scores = [c.get("openness_score", 0) for c in connections if c.get("openness_score") is not None]
        human_ready_scores = [c.get("human_ready_score", 0) for c in connections if c.get("human_ready_score") is not None]
        
        if trust_scores:
            avg_trust = sum(trust_scores) / len(trust_scores)
            print(f"\nAverage trust score: {avg_trust:.2f}/100")
        if openness_scores:
            avg_openness = sum(openness_scores) / len(openness_scores)
            print(f"Average openness score: {avg_openness:.2f}/100")
        if human_ready_scores:
            avg_ready = sum(human_ready_scores) / len(human_ready_scores)
            print(f"Average human-ready score: {avg_ready:.2f}/100")
    
    # 9. Generate summary markdown
    print("\n## SAVING REPORT")
    print("-" * 40)
    
    # Write report to the same directory as trials.jsonl or to current dir
    trials_path = Path(args.out)
    if trials_path.suffix == '.jsonl':
        report_dir = trials_path.parent
    else:
        report_dir = Path(args.out)
    report_path = report_dir / "ANALYSIS.md"
    
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("# Ministry-Sim Analysis Report\n\n")
        f.write(f"Total trials analyzed: {total}\n\n")
        
        # Add key findings
        f.write("## Key Findings\n\n")
        f.write(f"- **Faithful rate**: {faith_rate:.1f}%\n")
        f.write(f"- **Most common situation**: {situations.most_common(1)[0][0] if situations else 'N/A'}\n")
        
        # Find best situations
        if situ_outcomes:
            best_sit = max(situ_outcomes.items(), 
                          key=lambda x: x[1]["good"]/x[1]["total"] if x[1]["total"] > 0 else 0)
            f.write(f"- **Best situation**: {best_sit[0]} ({best_sit[1]['good']/best_sit[1]['total']*100:.1f}% faithful)\n")
        
        f.write(f"\n## Full Analysis\n\n")
        f.write("See terminal output for detailed breakdown.\n")
    
    print(f"Report saved to: {report_path}")
    print(f"\n{'=' * 70}")


def main():
    parser = argparse.ArgumentParser(description="Analyze ministry-sim trials")
    parser.add_argument("--out", default="./outputs/trials.jsonl", help="Path to trials.jsonl")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    args = parser.parse_args()
    
    analyze_trials(args)


if __name__ == "__main__":
    main()
