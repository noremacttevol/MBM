"""Clean evidence store implementation."""

import json
from pathlib import Path
from typing import Dict, Optional, List


GOOD_OUTCOMES = {"faithful_more_open", "faithful_walkaway"}
BAD_OUTCOMES = {"lost_by_pressure", "lost_by_dishonesty", "lost_unmet"}


class EvidenceStore:
    """Records (situation, approach, outcome) and computes faithful rates."""

    def __init__(self, path: str = "evidence.json"):
        self.path = Path(path)
        self.data: Dict[str, Dict[str, Dict[str, int]]] = {}
        if self.path.exists():
            try:
                with open(self.path, "r", encoding="utf-8") as fh:
                    self.data = json.load(fh)
            except (json.JSONDecodeError, OSError):
                self.data = {}

    def record_outcome(self, situation: str, approach: str, outcome: str) -> None:
        """Record an outcome. Skips neutral/unknown outcomes."""
        if outcome not in GOOD_OUTCOMES and outcome not in BAD_OUTCOMES:
            return
        bucket = self.data.setdefault(situation, {}).setdefault(
            approach, {"good": 0, "bad": 0}
        )
        if outcome in GOOD_OUTCOMES:
            bucket["good"] += 1
        else:
            bucket["bad"] += 1

    def faithful_rate(self, situation: str, approach: str) -> Optional[float]:
        """Get faithful rate for (situation, approach) pair."""
        bucket = self.data.get(situation, {}).get(approach)
        if not bucket:
            return None
        g, b = bucket["good"], bucket["bad"]
        return g / (g + b) if (g + b) > 0 else None

    def best_approach(self, situation: str, min_trials: int = 2) -> Optional[str]:
        """Best approach for this situation (highest faithful rate, min_trials)."""
        approaches = self.data.get(situation, {})
        candidates = [
            (a, self.faithful_rate(situation, a))
            for a in approaches
            if (approaches[a].get("good", 0) + approaches[a].get("bad", 0)) >= min_trials
        ]
        if not candidates:
            return None
        return max(candidates, key=lambda x: x[1] or 0)[0]

    def all_situations(self) -> List[str]:
        """List all known situations."""
        return list(self.data.keys())

    def all_outcomes(self) -> Dict[str, Dict[str, Dict[str, int]]]:
        """Return full data structure."""
        return self.data

    def save(self) -> None:
        """Persist to disk."""
        with open(self.path, "w", encoding="utf-8") as fh:
            json.dump(self.data, fh, indent=2)


def load_trials_from_jsonl(path: str = "outputs/trials.jsonl") -> List[dict]:
    """Load all trials from the main trials.jsonl file."""
    trials = []
    p = Path(path)
    if p.exists():
        with open(p, "r", encoding="utf-8") as fh:
            for line in fh:
                if line.strip():
                    trials.append(json.loads(line))
    return trials


def rebuild_evidence_store(trials: List[dict] = None) -> EvidenceStore:
    """Rebuild evidence store from all trials."""
    if trials is None:
        trials = []
        trials = load_trials_from_jsonl()
    store = EvidenceStore()
    store.data = {}
    for t in trials:
        situation = t.get("situation", "neutral")
        approach = t.get("approach", "GENTLE_EXPLORE")
        outcome = t.get("outcome", "neutral")
        store.record_outcome(situation, approach, outcome)
    return store


if __name__ == "__main__":
    trials = load_trials_from_jsonl()
    store = rebuild_evidence_store(trials)
    print(f"Loaded {len(trials)} trials, rebuilt store with {len(store.all_situations())} situations")
    store.save()
