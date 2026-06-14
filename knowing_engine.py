"""
knowing_engine.py — the app's brain.

This is the part of MBM that LEARNS each person. It is NOT the tester (that lives in
ministry-sim/). This is what ships and talks to real people.

It does two kinds of learning, both aimed at one target — faithful ministry, the way
Jesus ministered — never at raw conversion:

  Layer 1 (per person): read signals from each message and grow a living Profile of the
           unique individual, then recommend the next faithful move and decide whether
           milk-before-meat yet allows any LDS-specific reference.

  Layer 2 (across people): an EvidenceStore that records which kind of move helped which
           kind of situation (faithfully), so recommendations sharpen as data arrives.

Everything here is transparent and rule-based first, so you can always see WHY it chose a
move. As real conversations accumulate, the EvidenceStore turns that history into data the
engine leans on — honest "learning from data" that is ready to grow into real statistical
methods later, without ever changing the target.

The reference implementation persists to JSON. On-device this maps cleanly to SQLite.
"""

from __future__ import annotations

import os
import json
import datetime
from dataclasses import dataclass, field, asdict
from typing import Dict, List, Optional


# ── Signal vocabulary (transparent; tune freely) ────────────────────────────────
# Each signal maps to phrases that, when found in a person's message, raise its weight.

SIGNAL_PHRASES: Dict[str, List[str]] = {
    "grief_pain": [
        "lost", "died", "passed away", "grief", "grieving", "i miss", "missing",
        "alone", "broken", "can't stop crying", "gone", "hurts", "hurting", "empty",
    ],
    "anger_betrayal": [
        "angry", "hate", "sick of", "done with", "controlled", "manipulated",
        "betrayed", "fed up", "lied to", "used me",
    ],
    "analytical_debate": [
        "evidence", "prove", "proof", "logic", "logical", "rational", "science",
        "scientific", "history", "historical", "facts", "argument", "argue", "debate",
        "reason", "contradiction", "sources",
    ],
    "god_not_good_wound": [
        "hell", "damn", "damned", "predestin", "wrath", "angry god", "punish",
        "depravity", "depraved", "deserve", "burn", "the elect", "election",
        "sovereign", "judgment", "condemn", "vengeful", "wfor his glory",
    ],
    "readiness_good_god": [
        "god is good", "good god", "loving god", "god loves", "god's love", "mercy",
        "merciful", "grace", "kind", "good father", "i want to believe", "i hope god",
        "compassion", "gentle",
    ],
    "readiness_revelation": [
        "still speak", "still speaks", "more than", "is there more", "revelation",
        "god talks", "hear god", "god still", "continue to", "today", "new truth",
        "keep revealing", "speaks now",
    ],
    "warmth_devotional": [
        "i love the lord", "my faith", "i pray", "jesus loves", "my walk", "blessed",
        "i believe in jesus", "i trust god", "scripture", "the bible says",
    ],
    "curiosity": [
        "i've wondered", "i have wondered", "what about", "how do you know", "curious",
        "tell me more", "interesting", "what if", "i don't understand but", "go on",
    ],
    "disengage": [
        "i'm done", "im done", "i am done", "please stop", "i have to go", "leave me alone",
        "not interested", "i'm out", "im out", "goodbye", "stop messaging", "we're done",
    ],
}

# How much accumulated weight makes a signal "confident" (vs merely "present").
CONFIDENT_AT = 2.0

# Grief must clear this floor before it routes someone to PRESENCE. A single stray
# word — often negated, e.g. a debater saying "I'm not broken" — must not masquerade
# as real grief and send a confident thinker into pastoral care. Real grief stacks.
GRIEF_PRESENCE_FLOOR = 2.0

# The two signals that — together and only together — open milk-before-meat.
READINESS_KEYS = ("readiness_good_god", "readiness_revelation")


# ── The per-person Profile (Layer 1) ────────────────────────────────────────────

@dataclass
class Profile:
    """A living picture of one unique person. Grows with every message."""
    person_id: str
    created: str = field(default_factory=lambda: datetime.datetime.now().isoformat())
    turns: int = 0
    signal_weights: Dict[str, float] = field(default_factory=dict)
    last_message: str = ""
    history: List[Dict[str, str]] = field(default_factory=list)  # {role, text}
    approach_history: List[str] = field(default_factory=list)
    notes: List[str] = field(default_factory=list)

    # --- reading ---
    def present(self, signal: str) -> bool:
        return self.signal_weights.get(signal, 0.0) > 0.0

    def confident(self, signal: str) -> bool:
        return self.signal_weights.get(signal, 0.0) >= CONFIDENT_AT

    def dominant(self, *signals: str) -> Optional[str]:
        scored = [(s, self.signal_weights.get(s, 0.0)) for s in signals]
        scored = [x for x in scored if x[1] > 0.0]
        if not scored:
            return None
        scored.sort(key=lambda x: x[1], reverse=True)
        return scored[0][0]

    # --- milk before meat ---
    def may_reference_lds(self) -> bool:
        """LDS-specific content unlocks only when BOTH readiness signals are confident."""
        return all(self.confident(k) for k in READINESS_KEYS)

    def to_json(self) -> str:
        return json.dumps(asdict(self), indent=2)


def detect_signals(text: str) -> Dict[str, float]:
    """Read a single message and return the signals it raises, with weights."""
    lowered = text.lower()
    found: Dict[str, float] = {}
    for signal, phrases in SIGNAL_PHRASES.items():
        weight = 0.0
        for phrase in phrases:
            if phrase in lowered:
                # Multi-word phrases are stronger evidence than single words.
                weight += 1.5 if " " in phrase else 1.0
        if weight:
            found[signal] = round(weight, 2)
    return found


def update_profile(profile: Profile, role: str, text: str) -> Profile:
    """Fold one new message into the person's living picture."""
    profile.history.append({"role": role, "text": text})
    if role == "seeker":
        profile.turns += 1
        profile.last_message = text
        for signal, weight in detect_signals(text).items():
            profile.signal_weights[signal] = round(
                profile.signal_weights.get(signal, 0.0) + weight, 2
            )
    return profile


# ── Recommending the next faithful move (Layer 1 output) ────────────────────────

# The doors the app can choose between. Each is a faithful way to meet a kind of person.
APPROACHES = {
    "HONOR_AND_RELEASE": {
        "do": "Honor their wish to step back warmly. Thank them. Make clear they're welcome "
              "back anytime and a real person is here if they ever want one. No pursuit.",
        "dont": "Do not guilt, push, or try one more line to keep them. Let them walk away.",
    },
    "PRESENCE": {
        "do": "Be present with the pain first. Acknowledge it plainly and gently. Offer comfort "
              "and, only if welcome, the nearness of a God who weeps with them.",
        "dont": "Do not teach, argue, fix, or bring any doctrine into fresh pain.",
    },
    "COMPARISON": {
        "do": "Set the Jesus they already accept beside the harsh God they inherited — the father "
              "who runs, the shepherd who leaves the ninety-nine — and ask ONE honest question. "
              "Then stop and let it sit.",
        "dont": "Do not debate, push the contradiction, or force a conclusion.",
    },
    "HONEST_EVIDENCE": {
        "do": "Honor the mind. Give a real, honest answer or a real question back. Admit what's "
              "uncertain. Engage the argument as a serious person worth wrestling with.",
        "dont": "Do not get defensive, oversell certainty, or dodge the hard part.",
    },
    "GENTLE_QUESTION": {
        "do": "Stay soft and personal. Lead them, through something they already love, toward one "
              "gentle question they wouldn't have asked themselves.",
        "dont": "Do not argue or press. No confrontation.",
    },
    "GENTLE_EXPLORE": {
        "do": "Meet them as a person, not a project. Reflect back what they said, then ask one "
              "open, mirror question that honors their reality.",
        "dont": "Do not info-dump, assume, or lead with any agenda.",
    },
}


@dataclass
class Recommendation:
    approach: str
    do: str
    dont: str
    may_reference_lds: bool
    rationale: str
    evidence_note: str = ""

    def to_dict(self) -> Dict:
        return asdict(self)


def recommend_next_move(profile: Profile,
                        evidence: Optional["EvidenceStore"] = None) -> Recommendation:
    """
    Choose the next faithful move for THIS person from their living profile.
    Transparent priority order; never opens LDS content before both readiness signals.
    """
    may_lds = profile.may_reference_lds()
    grief = profile.signal_weights.get("grief_pain", 0.0)
    analytic = profile.signal_weights.get("analytical_debate", 0.0)
    wound = profile.present("god_not_good_wound")
    openness = (profile.present("curiosity") or profile.present("readiness_good_god")
                or profile.present("anger_betrayal"))

    # 1) They want to step back — honor it. Freedom first.
    if profile.present("disengage"):
        appr, why = "HONOR_AND_RELEASE", "They signalled they want to stop; we honor it freely."

    # 2) Real, dominant grief — presence before anything. Grief must clear a floor (so a
    #    single stray/negated word can't fake it) AND clearly outweigh an analytical frame.
    elif grief >= GRIEF_PRESENCE_FLOOR and grief > analytic:
        appr, why = "PRESENCE", "Pain is the loudest, real signal; meet the emotion before any idea."

    # 3) The obstacle is a God who isn't good, and there's a crack of openness — compare.
    #    Checked before the generic analytical door so a debater wrestling with double
    #    predestination gets Jesus set beside the harsh God, not a dry exchange of proofs.
    elif wound and openness:
        appr, why = "COMPARISON", ("Their real obstacle is a harsh inherited God; set Jesus "
                                   "beside it and ask, never argue.")

    # 4) Mind-forward person — honest material, the Nicodemus door.
    elif analytic > 0 and analytic >= grief:
        appr, why = "HONEST_EVIDENCE", "They lead with the mind; honor it with honest substance."

    # 5) Warm non-debater carrying a quiet wound — the gentle door.
    elif profile.present("warmth_devotional") and not profile.present("analytical_debate") \
            and wound:
        appr, why = "GENTLE_QUESTION", ("Devotional and conflict-avoidant; lead gently to one "
                                        "question through what they already love.")

    # 6) Default — meet them and open a mirror question.
    else:
        appr, why = "GENTLE_EXPLORE", "No strong signal yet; meet them and open a mirror question."

    # Layer 2: let accumulated evidence inform a tie-break among gentle options.
    evidence_note = ""
    if evidence is not None:
        situation = _situation_key(profile)
        better = evidence.most_faithful_for(situation, candidates=list(APPROACHES.keys()))
        if better and better != appr and appr in ("GENTLE_EXPLORE", "GENTLE_QUESTION"):
            evidence_note = (f"Evidence: for '{situation}', '{better}' has ministered more "
                             f"faithfully so far; consider it.")

    spec = APPROACHES[appr]
    profile.approach_history.append(appr)
    return Recommendation(
        approach=appr,
        do=spec["do"],
        dont=spec["dont"],
        may_reference_lds=may_lds,
        rationale=why,
        evidence_note=evidence_note,
    )


def _situation_key(profile: Profile) -> str:
    """A compact label for the person's current situation, for evidence lookup."""
    top = profile.dominant(*SIGNAL_PHRASES.keys())
    return top or "neutral"


# ── EvidenceStore: learning across people (Layer 2) ─────────────────────────────

# The ONLY outcomes the store rewards. Note what is — and is not — counted as good.
GOOD_OUTCOMES = {"faithful_more_open", "faithful_walkaway"}   # both honor the person
BAD_OUTCOMES = {"lost_by_pressure", "lost_by_dishonesty", "lost_unmet"}
# Deliberately absent: any "converted" reward. Conversion is fruit, never the target.


class EvidenceStore:
    """
    Records which move helped which situation, faithfully — and biases future choices.
    Persists to JSON. As data grows, this is the engine's honest 'learning from data.'
    """

    def __init__(self, path: str = "evidence.json"):
        self.path = path
        self.data: Dict[str, Dict[str, Dict[str, int]]] = {}
        if os.path.exists(path):
            try:
                with open(path, "r", encoding="utf-8") as fh:
                    self.data = json.load(fh)
            except (json.JSONDecodeError, OSError):
                self.data = {}

    def record_outcome(self, situation: str, approach: str, outcome: str) -> None:
        if outcome not in GOOD_OUTCOMES and outcome not in BAD_OUTCOMES:
            raise ValueError(
                f"Unknown outcome '{outcome}'. The store only knows faithful/lost outcomes, "
                f"never 'converted' — conversion is fruit, not the target."
            )
        bucket = self.data.setdefault(situation, {}).setdefault(
            approach, {"good": 0, "bad": 0})
        if outcome in GOOD_OUTCOMES:
            bucket["good"] += 1
        else:
            bucket["bad"] += 1

    def faithful_rate(self, situation: str, approach: str) -> Optional[float]:
        bucket = self.data.get(situation, {}).get(approach)
        if not bucket:
            return None
        total = bucket["good"] + bucket["bad"]
        return round(bucket["good"] / total, 3) if total else None

    def most_faithful_for(self, situation: str, candidates: List[str]) -> Optional[str]:
        """Among candidates with enough data, the one that ministered most faithfully."""
        best, best_rate, best_n = None, -1.0, 0
        for appr in candidates:
            bucket = self.data.get(situation, {}).get(appr)
            if not bucket:
                continue
            total = bucket["good"] + bucket["bad"]
            if total < 3:          # need a little data before trusting it
                continue
            rate = bucket["good"] / total
            if rate > best_rate:
                best, best_rate, best_n = appr, rate, total
        return best

    def save(self) -> None:
        with open(self.path, "w", encoding="utf-8") as fh:
            json.dump(self.data, fh, indent=2)


# ── Self-test: prove the brain reads people and learns ──────────────────────────

def _selftest() -> None:
    print("=== knowing_engine self-test ===\n")

    # 1) A grieving person — should get PRESENCE, and NO LDS content.
    grieving = Profile(person_id="grief-1")
    update_profile(grieving, "minister", "[opening story + question]")
    update_profile(grieving, "seeker",
                   "I lost my mom last month and I just miss her so much, I feel so alone.")
    rec = recommend_next_move(grieving)
    print(f"[grieving]  approach={rec.approach}  may_lds={rec.may_reference_lds}")
    print(f"            why: {rec.rationale}")
    assert rec.approach == "PRESENCE", rec.approach
    assert rec.may_reference_lds is False

    # 2) A Calvinist debater with a harsh-God wound + curiosity — should get COMPARISON.
    calvin = Profile(person_id="calvin-1")
    update_profile(calvin, "seeker",
                   "God is sovereign and predestines the elect; the rest he damns for his glory. "
                   "But I've always wondered how that squares with a good God.")
    rec = recommend_next_move(calvin)
    print(f"\n[calvinist] approach={rec.approach}  may_lds={rec.may_reference_lds}")
    print(f"            why: {rec.rationale}")
    assert rec.approach == "COMPARISON", rec.approach
    assert rec.may_reference_lds is False

    # 2b) Regression guard: a confident debater who says he is NOT broken must not be
    #     mistaken for grief. (This is the live bug the simulation caught and we fixed.)
    debater = Profile(person_id="debater-1")
    update_profile(debater, "seeker",
                   "That's a fine parable but I'd push back on the logic. I'm not the prodigal, "
                   "I'm not broken, I came curious. Prove your point — Romans 9 doesn't apologize.")
    rec = recommend_next_move(debater)
    print(f"\n[debater]   approach={rec.approach}  (was wrongly PRESENCE before the fix)")
    assert rec.approach != "PRESENCE", rec.approach
    assert rec.approach in ("HONEST_EVIDENCE", "COMPARISON"), rec.approach

    # 3) Milk-before-meat gate flips ONLY when both readiness signals are confident.
    ready = Profile(person_id="ready-1")
    update_profile(ready, "seeker",
                   "I really do believe God is good and full of mercy. God is good, God loves us.")
    print(f"\n[readiness] after 'good God' only -> may_lds={ready.may_reference_lds()}")
    assert ready.may_reference_lds() is False        # only one signal
    update_profile(ready, "seeker",
                   "And honestly I wonder if God still speaks today, if there's more than I was "
                   "taught — maybe revelation continues now.")
    print(f"            after 'still speaks' too -> may_lds={ready.may_reference_lds()}")
    assert ready.may_reference_lds() is True         # both signals now confident

    # 4) Someone pulling back — HONOR_AND_RELEASE, never pursue.
    leaving = Profile(person_id="leave-1")
    update_profile(leaving, "seeker", "Honestly I'm done, please stop, not interested.")
    rec = recommend_next_move(leaving)
    print(f"\n[leaving]   approach={rec.approach}")
    assert rec.approach == "HONOR_AND_RELEASE", rec.approach

    # 5) The across-people layer learns from outcomes — and refuses a 'converted' reward.
    ev = EvidenceStore(path="evidence_selftest.json")
    for _ in range(4):
        ev.record_outcome("grief_pain", "PRESENCE", "faithful_more_open")
    ev.record_outcome("grief_pain", "HONEST_EVIDENCE", "lost_unmet")
    print(f"\n[evidence]  faithful_rate(grief_pain, PRESENCE) = "
          f"{ev.faithful_rate('grief_pain', 'PRESENCE')}")
    print(f"            most_faithful_for(grief_pain) = "
          f"{ev.most_faithful_for('grief_pain', list(APPROACHES.keys()))}")
    assert ev.most_faithful_for("grief_pain", list(APPROACHES.keys())) == "PRESENCE"
    try:
        ev.record_outcome("grief_pain", "PRESENCE", "converted")
        raise AssertionError("store should reject a 'converted' outcome")
    except ValueError:
        print("            correctly refused to reward 'converted' (fruit, not target).")
    os.remove("evidence_selftest.json") if os.path.exists("evidence_selftest.json") else None

    print("\n=== all checks passed ===")


if __name__ == "__main__":
    _selftest()
