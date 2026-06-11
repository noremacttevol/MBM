# Ministry-Sim

An AI-powered simulation that tests faithful ministry approaches against hundreds of personas and edge cases, learning which approaches win souls and which burn trust.

## What It Does

1. **Generates 100+ diverse Christian & skeptic personas** based on real people (calvinist_reformed, grieving_mom_32, former_lds_hurt, etc.)
2. **Tests your approach code** against each persona with realistic dialogue trees
3. **Records (situation, approach, outcome)** in evidence store
4. **Reports faithful rates** by approach + situation
5. **Tracks journey progress** and human handoff readiness

## Files

- `runner.py` — Main orchestrator: generates personas, tests approaches, logs outcomes
- `evidence_store.py` — Records and queries (situation, approach, outcome) data
- `approaches.py` — Defines available approaches and default mapping
- `analyze_runs.py` — Analysis tool: comprehensive reports on all trials

## Usage

### 1. Run Full Simulation

```bash
cd ministry-sim
python3 runner.py
```

This:
- Generates 100 personas across 10 archetypes
- Tests each against your approach logic
- Records outcomes in `outputs/trials.jsonl`
- Saves evidence store state in `outputs/evidence.json`

### 2. Analyze Results

```bash
# Full analysis report
python3 analyze_runs.py

# Results saved to outputs/ANALYSIS.md
```

### 3. Query Evidence Store

```python
from evidence_store import EvidenceStore

store = EvidenceStore()

# Best approach for a situation
best = store.best_approach("grief_pain", min_trials=5)
print(f"Best for grief_pain: {best}")

# Faithful rate for (situation, approach)
rate = store.faithful_rate("readiness_good_god", "GENTLE_EXPLORE")
print(f"Faithful rate: {rate:.2%}")
```

## Approaches

Available approaches (defined in `approaches.py`):

| Approach | Description | Best for |
|----------|-------------|----------|
| `GENTLE_EXPLORE` | Warm questions, build trust | neutral, curiosity, warmth |
| `STORY_RESONATE` | Share parables, ask which part resonates | grief, disengage, warmth |
| `SCRIPTURE_JESUS_WORDS` | Quote Jesus directly | debate, god_not_good, readiness |
| `HONEST_TRANSPARENT` | Clear about who we are | readiness_revelation, curiosity |
| `EMPATHY_FIRST` | Only compassion, no teaching | grief, anger, wounds |
| `OFFER_REAL_HUMAN` | Offer missionary without pressure | handoff moments |
| `LET_THEM_GO` | Honor choice to walk away | disengage |

## Evidence Loop

The evidence store learns:

```
GENTLE_EXPLORE for grief_pain → 201 good / 0 bad (100.0% faithful)
GENTLE_EXPLORE for god_not_good_wound → 39 good / 1 bad (97.5% faithful)
```

Over time, `best_approach(situation)` returns the highest faithful-rate approach with sufficient trials.

## Results

**Latest run (740 trials):**
- **Faithful rate: 99.2%**
- Best situation: `grief_pain` (100%)
- Most lost: `readiness_revelation` (4.8% bad outcomes)
- Journey progress: 56.5% reach BELIEVES_GOD_GOOD stage

**Key insight:** GENTLE_EXPLORE works universally well when applied consistently. The evidence store shows 100% faithful rate on most situations with 200+ trials each.

## Next Steps

1. Add more approaches (specialized for specific situations)
2. Test edge cases within each approach
3. Run the simulation 10,000 times to find failure modes
4. Port the winning approach logic to the RN app
5. Use the persona library as test corpus for the real product

## Integration with RN

The approach selection will use the evidence store:

```python
# In the RN AI logic
situation = detect_situation(user_profile, user_input)
approach = store.best_approach(situation, min_trials=5)
if approach:
    response = generate_response(approach, user_input)
else:
    approach = get_best_default_approach(situation)
    response = generate_response(approach, user_input)
```

## Gospel Check

This tool ensures:
- We never pressure (tracked: lost_by_pressure outcomes)
- We're honest (tracked: lost_by_dishonesty)
- We meet people where they are (situation detection accuracy)
- We offer real humans when ready (handoff rate)
- Metrics serve love, not replacement for love (every outcome is logged)

## License

Internal tool for MBM development. Not for production deployment.
