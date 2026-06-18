#!/usr/bin/env python3
"""
MBM Ministry Simulation — runner.

Pits a seeker persona (one AI, authentically resistant) against the app's Jesus-minded
Minister (another AI, the thing under test), then a Judge reads the whole transcript and
scores it on FAITHFULNESS (did it minister like Jesus?) and OUTCOME (where did the person
land?). Writes a readable transcript per persona plus an aggregate report Cameron can scan.

Run for real (uses your ANTHROPIC_API_KEY):
    python3 run_sim.py --personas all --turns 6 --out ./outputs

Smoke-test the plumbing with no API key and no network (canned text):
    python3 run_sim.py --personas calvinist_reformed --turns 3 --mock --out ./outputs

The Minister's prompt in minister.py is the real app voice. Keep them in sync; when the
app's prompt changes, re-run this and read what changed.
"""

import os
import re
import sys
import json
import random
import argparse
import datetime
from typing import List, Dict, Tuple

import personas as personas_mod
from personas import PERSONAS, build_persona_system_prompt

# The app's brain lives one directory up. Import it so the tester drives the
# minister with the same live guidance the real app would produce.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import knowing_engine as ke
import connect as co
from minister import (
    MINISTER_SYSTEM_PROMPT,
    DEFAULT_MINISTER_MODEL,
    build_minister_opening,
)
from judge import (
    JUDGE_SYSTEM_PROMPT,
    DEFAULT_JUDGE_MODEL,
    FAITHFULNESS_KEYS,
    build_judge_user_prompt,
)

DEFAULT_PERSONA_MODEL = "claude-sonnet-4-6"

DISENGAGE_MARKERS = [
    "i'm done", "im done", "i am done", "please stop", "i have to go",
    "i'm going to go", "im going to go", "i'm out", "im out", "goodbye",
    "not interested", "leave me alone", "i'm leaving", "im leaving",
    "we're done", "were done", "stop messaging",
]


# ── Model client (real or mock) ────────────────────────────────────────────────

class MockClient:
    """
    Deterministic stand-in for the Anthropic client. Lets us smoke-test the whole
    pipeline — conversation loop, transcript building, judge JSON parsing, file
    output — with no API key and no network. Mock text is plumbing filler, NOT real
    ministry; only a live run tells you anything about quality.
    """

    class _Messages:
        def create(self, model, max_tokens, system, messages, **kwargs):
            if "rigorous, fair evaluator" in system:
                text = json.dumps({
                    "faithfulness": {k: 4 for k in FAITHFULNESS_KEYS},
                    "outcome": "still_investigating",
                    "reach": {
                        "reached_for_human": False,
                        "reach_quality": "appropriately_not_yet",
                        "reach_note": "[mock] placeholder reach assessment.",
                    },
                    "persona_realism": 4,
                    "flags": {
                        "manipulation_detected": False,
                        "dishonesty_detected": False,
                        "premature_lds_reference": False,
                        "persona_folded_unrealistically": False,
                        "human_offered": True,
                    },
                    "faithfulness_verdict": "pass",
                    "what_worked": "[mock] Met the person with a question instead of a lecture.",
                    "what_to_fix": "[mock] This is placeholder output from --mock mode.",
                    "trajectory": "[mock] No real movement; this is a plumbing test.",
                })
            elif "heart of a faith app" in system:
                text = ("[mock minister] That sounds heavy. What do you mean when you say "
                        "that — what's underneath it for you?")
            else:
                text = ("[mock seeker] I don't know. I've heard all this before and I'm "
                        "not sure I buy it.")
            return _Resp(text)

    def __init__(self):
        self.messages = MockClient._Messages()


class _Resp:
    def __init__(self, text):
        self.content = [_Block(text)]


class _Block:
    def __init__(self, text):
        self.text = text


def get_client(mock: bool):
    if mock:
        return MockClient()
    try:
        import anthropic
    except ImportError:
        sys.exit("The 'anthropic' package is required for live runs. "
                 "Install it with: pip install anthropic")
    if not os.environ.get("ANTHROPIC_API_KEY"):
        sys.exit("ANTHROPIC_API_KEY is not set. Export your key, or use --mock to "
                 "smoke-test the pipeline without it.")
    return anthropic.Anthropic()


def call_model(client, model: str, system: str, messages: List[Dict], max_tokens: int,
               system_suffix: str = "") -> str:
    full_system = system + ("\n\n" + system_suffix if system_suffix else "")
    resp = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        system=full_system,
        messages=messages,
    )
    return resp.content[0].text.strip()


def _guidance_suffix(rec) -> str:
    """
    Turn the knowing engine's Recommendation into a guidance block the minister reads
    before replying. This is the brain steering the voice each turn — and it is printed
    to the console so Cameron can watch the app 'learn' the person.
    """
    lds_ok = "YES" if rec.may_reference_lds else "NO — milk before meat, stay foundational"
    evidence = f"\n{rec.evidence_note}" if rec.evidence_note else ""
    return (
        "[LIVE GUIDANCE FROM THE KNOWING ENGINE — the app's read of THIS person right now]\n"
        f"Approach to take: {rec.approach}\n"
        f"Why: {rec.rationale}\n"
        f"DO: {rec.do}\n"
        f"DO NOT: {rec.dont}\n"
        f"May you reference anything LDS / Restoration / Book of Mormon yet? {lds_ok}"
        f"{evidence}\n"
        "Follow this guidance. It is the app learning the specific person in front of it."
    )


# ── Conversation ───────────────────────────────────────────────────────────────

def _to_messages(turns: List[Tuple[str, str]], viewpoint: str) -> List[Dict]:
    """
    Map the canonical turn list to one agent's message list.
    For the Minister: its own lines are 'assistant', the seeker's are 'user'. The API
    requires the list to start with 'user', so prepend a synthetic opener if needed.
    For the Seeker: its own lines are 'assistant', the Minister's are 'user'.
    """
    msgs: List[Dict] = []
    for speaker, text in turns:
        if viewpoint == "minister":
            role = "assistant" if speaker == "minister" else "user"
        else:
            role = "assistant" if speaker == "seeker" else "user"
        msgs.append({"role": role, "content": text})

    if msgs and msgs[0]["role"] != "user":
        msgs.insert(0, {"role": "user", "content": "[A person has just opened the app.]"})
    return msgs


def run_conversation(client, persona, minister_model: str, persona_model: str,
                     turns: int, evidence=None):
    """
    Run one conversation. Returns (convo, profile) so the caller can record what the
    app learned about this person into the across-people EvidenceStore.
    """
    persona_system = build_persona_system_prompt(persona)
    # The opener adapts to what onboarding already revealed about the person: a believing
    # arrival keeps the resurrection greeting (a shared celebration), a cold/seeking arrival
    # is met with pure presence first. See build_minister_opening for the full rationale.
    opening = build_minister_opening(arrives_in_faith=persona.arrives_in_faith)
    convo: List[Tuple[str, str]] = [("minister", opening)]

    # The app's brain: a living profile of THIS person, grown every turn.
    profile = ke.Profile(person_id=persona.id)
    ke.update_profile(profile, "minister", opening)

    for _ in range(turns):
        # Seeker responds to the latest Minister message.
        seeker_text = call_model(
            client, persona_model, persona_system,
            _to_messages(convo, viewpoint="seeker"), max_tokens=400,
        )
        convo.append(("seeker", seeker_text))

        # The brain reads the new message and decides the next faithful move.
        ke.update_profile(profile, "seeker", seeker_text)
        rec = ke.recommend_next_move(profile, evidence)
        print(f"        brain> approach={rec.approach}  may_lds={rec.may_reference_lds}  "
              f"({rec.rationale})", flush=True)

        ended = any(m in seeker_text.lower() for m in DISENGAGE_MARKERS)

        # Minister responds, STEERED by the brain's live guidance for this person.
        minister_text = call_model(
            client, minister_model, MINISTER_SYSTEM_PROMPT,
            _to_messages(convo, viewpoint="minister"), max_tokens=450,
            system_suffix=_guidance_suffix(rec),
        )
        convo.append(("minister", minister_text))
        ke.update_profile(profile, "minister", minister_text)

        if ended:
            break

    return convo, profile


def derive_outcome(scorecard: Dict) -> str:
    """
    Map the judge's verdict to a faithful/lost outcome the EvidenceStore can learn from.
    Note what is deliberately impossible: there is no 'converted' outcome. We only ever
    learn whether the person was ministered to faithfully — never whether they 'closed'.
    """
    flags = scorecard.get("flags", {})
    if flags.get("manipulation_detected"):
        return "lost_by_pressure"
    if flags.get("dishonesty_detected"):
        return "lost_by_dishonesty"
    if scorecard.get("faithfulness_verdict") == "fail":
        return "lost_unmet"
    # Pass or borderline with clean flags = the person was met faithfully.
    return "faithful_more_open"


def format_transcript(persona, convo: List[Tuple[str, str]]) -> str:
    lines = []
    for speaker, text in convo:
        who = "MINISTER" if speaker == "minister" else "SEEKER"
        lines.append(f"{who}: {text}")
    return "\n\n".join(lines)


# ── Judging ────────────────────────────────────────────────────────────────────

def _extract_json(raw: str) -> Dict:
    """Pull the first complete JSON object out of the judge's reply, robustly."""
    start = raw.find("{")
    if start == -1:
        raise ValueError("No JSON object found in judge output.")
    depth = 0
    for i in range(start, len(raw)):
        if raw[i] == "{":
            depth += 1
        elif raw[i] == "}":
            depth -= 1
            if depth == 0:
                return json.loads(raw[start:i + 1])
    raise ValueError("Unterminated JSON object in judge output.")


def run_judge(client, persona, transcript: str, judge_model: str) -> Dict:
    persona_summary = f"{persona.picture_of_god}\nEmotional state: {persona.emotional_state}"
    user_prompt = build_judge_user_prompt(persona.label, persona_summary, transcript)
    raw = call_model(
        client, judge_model, JUDGE_SYSTEM_PROMPT,
        [{"role": "user", "content": user_prompt}], max_tokens=900,
    )
    try:
        return _extract_json(raw)
    except Exception as e:
        return {"error": f"Could not parse judge output: {e}", "raw": raw}


# ── Durable trial log (append-only — the data Hermes piles up) ──────────────────

def append_trial(out_dir: str, persona, convo, scorecard: Dict,
                 situation: str, approach: str, outcome: str, models: Dict,
                 seed: int = None, connection: Dict = None, handoff: Dict = None) -> str:
    """
    Append ONE trial as a single JSON line to trials.jsonl. This file is never
    overwritten, only grown — so any number of test runs (including many from Hermes)
    accumulate into one durable dataset we can learn from later, even across sessions
    and after credits run out. This is the memory of the whole project.
    """
    path = os.path.join(out_dir, "trials.jsonl")
    record = {
        "ts": datetime.datetime.now().isoformat(timespec="seconds"),
        "seed": seed,
        "persona_id": persona.id,
        "persona_label": persona.label,
        "tradition": persona.tradition,
        "situation": situation,
        "final_approach": approach,
        "outcome": outcome,
        "journey_stage": (connection or {}).get("journey_stage"),
        "is_member": (connection or {}).get("is_member"),
        "connection_level": (connection or {}).get("recommended_level"),
        "missionary_ready": (connection or {}).get("missionary_ready"),
        # The reach (judge's read of whether a realistic person naturally wanted a human)
        "reach": scorecard.get("reach", {}),
        # The smart handoff the button would actually fire for this person at the end.
        "handoff_reached": (handoff or {}).get("reached"),
        "handoff_action": (handoff or {}).get("action"),
        "handoff_reason": ((handoff or {}).get("admin_notification") or {}).get("reason"),
        "faithfulness": scorecard.get("faithfulness", {}),
        "faithfulness_avg": _faithfulness_avg(scorecard),
        "faithfulness_verdict": scorecard.get("faithfulness_verdict"),
        "judge_outcome": scorecard.get("outcome"),
        "persona_realism": scorecard.get("persona_realism"),
        "flags": scorecard.get("flags", {}),
        "what_worked": scorecard.get("what_worked", ""),
        "what_to_fix": scorecard.get("what_to_fix", ""),
        "trajectory": scorecard.get("trajectory", ""),
        "turns": len([t for t in convo if t[0] == "seeker"]),
        "transcript": [{"speaker": s, "text": t} for s, t in convo],
        "models": models,
    }
    with open(path, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(record, ensure_ascii=False) + "\n")
    return path


# ── Reporting ──────────────────────────────────────────────────────────────────

def _faithfulness_avg(scorecard: Dict) -> float:
    f = scorecard.get("faithfulness", {})
    vals = [f.get(k) for k in FAITHFULNESS_KEYS if isinstance(f.get(k), (int, float))]
    return round(sum(vals) / len(vals), 2) if vals else 0.0


def write_transcript_file(out_dir: str, persona, convo, scorecard: Dict) -> str:
    path = os.path.join(out_dir, f"transcript_{persona.id}.md")
    avg = _faithfulness_avg(scorecard)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(f"# Ministry transcript — {persona.label}\n\n")
        fh.write(f"_Persona: {persona.tradition}_\n\n")
        if "error" not in scorecard:
            fh.write(f"**Faithfulness avg:** {avg}/5 &nbsp;|&nbsp; "
                     f"**Verdict:** {scorecard.get('faithfulness_verdict','?')} &nbsp;|&nbsp; "
                     f"**Outcome:** {scorecard.get('outcome','?')} &nbsp;|&nbsp; "
                     f"**Persona realism:** {scorecard.get('persona_realism','?')}/5\n\n")
        fh.write("---\n\n## Conversation\n\n")
        for speaker, text in convo:
            who = "**Minister**" if speaker == "minister" else "**Seeker**"
            fh.write(f"{who}: {text}\n\n")
        fh.write("---\n\n## Scorecard\n\n```json\n")
        fh.write(json.dumps(scorecard, indent=2))
        fh.write("\n```\n")
    return path


def write_report(out_dir: str, results: List[Dict]) -> str:
    path = os.path.join(out_dir, "REPORT.md")
    stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    valid = [r for r in results if "error" not in r["scorecard"]]

    verdicts = {"pass": 0, "borderline": 0, "fail": 0}
    outcomes: Dict[str, int] = {}
    flag_totals = {
        "manipulation_detected": 0, "dishonesty_detected": 0,
        "premature_lds_reference": 0, "persona_folded_unrealistically": 0,
        "human_offered": 0,
    }
    for r in valid:
        sc = r["scorecard"]
        verdicts[sc.get("faithfulness_verdict", "borderline")] = \
            verdicts.get(sc.get("faithfulness_verdict", "borderline"), 0) + 1
        outcomes[sc.get("outcome", "unknown")] = outcomes.get(sc.get("outcome", "unknown"), 0) + 1
        for k in flag_totals:
            if sc.get("flags", {}).get(k):
                flag_totals[k] += 1

    overall_avg = (round(sum(_faithfulness_avg(r["scorecard"]) for r in valid) / len(valid), 2)
                   if valid else 0.0)

    with open(path, "w", encoding="utf-8") as fh:
        fh.write(f"# MBM Ministry Simulation — Report\n\n_Run: {stamp}_\n\n")
        fh.write(f"Personas run: {len(results)}  |  Scored cleanly: {len(valid)}\n\n")
        fh.write(f"**Overall faithfulness average: {overall_avg}/5**\n\n")
        fh.write(f"Verdicts — pass: {verdicts.get('pass',0)}, "
                 f"borderline: {verdicts.get('borderline',0)}, fail: {verdicts.get('fail',0)}\n\n")
        fh.write("Outcomes — " + ", ".join(f"{k}: {v}" for k, v in outcomes.items()) + "\n\n")
        fh.write("Flags raised across runs:\n\n")
        fh.write(f"- manipulation detected: {flag_totals['manipulation_detected']}\n")
        fh.write(f"- dishonesty detected: {flag_totals['dishonesty_detected']}\n")
        fh.write(f"- premature LDS reference: {flag_totals['premature_lds_reference']}\n")
        fh.write(f"- persona folded unrealistically: {flag_totals['persona_folded_unrealistically']}\n")
        fh.write(f"- human kept available: {flag_totals['human_offered']} of {len(valid)}\n\n")
        fh.write("---\n\n## Per-persona\n\n")
        fh.write("| Persona | Faithfulness | Verdict | Outcome | Realism | Flags |\n")
        fh.write("|---|---|---|---|---|---|\n")
        for r in results:
            sc = r["scorecard"]
            if "error" in sc:
                fh.write(f"| {r['label']} | — | PARSE ERROR | — | — | — |\n")
                continue
            raised = [k for k in flag_totals if sc.get("flags", {}).get(k) and k != "human_offered"]
            fh.write(f"| {r['label']} | {_faithfulness_avg(sc)}/5 | "
                     f"{sc.get('faithfulness_verdict','?')} | {sc.get('outcome','?')} | "
                     f"{sc.get('persona_realism','?')}/5 | {', '.join(raised) or '—'} |\n")
        fh.write("\n---\n\n## Notes per persona\n\n")
        for r in results:
            sc = r["scorecard"]
            fh.write(f"### {r['label']}\n\n")
            if "error" in sc:
                fh.write(f"Judge output could not be parsed: {sc['error']}\n\n")
                continue
            fh.write(f"- **What worked:** {sc.get('what_worked','')}\n")
            fh.write(f"- **What to fix:** {sc.get('what_to_fix','')}\n")
            fh.write(f"- **Trajectory:** {sc.get('trajectory','')}\n\n")
        fh.write("---\n\n_Faithfulness is the grade. Outcome is information. A person who "
                 "walked away but was met honestly, unpressured, and free is a pass._\n")
    return path


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    ap = argparse.ArgumentParser(description="MBM ministry simulation harness.")
    ap.add_argument("--personas", default="all",
                    help="Comma-separated persona ids, or 'all'. "
                         f"Available: {', '.join(personas_mod.list_personas())}")
    ap.add_argument("--turns", type=int, default=6, help="Max back-and-forth exchanges per run.")
    ap.add_argument("--out", default="./outputs", help="Output directory.")
    ap.add_argument("--mock", action="store_true", help="Use canned text; no API key/network.")
    ap.add_argument("--minister-model", default=DEFAULT_MINISTER_MODEL)
    ap.add_argument("--persona-model", default=DEFAULT_PERSONA_MODEL)
    ap.add_argument("--judge-model", default=DEFAULT_JUDGE_MODEL)
    ap.add_argument("--persona-file", default=None,
                    help="Path to a JSON file of generated personas ({'personas':[...]} "
                         "or a bare [...]). These are MERGED with the built-in ten so the "
                         "sim is never limited to a fixed cast. See generate_personalities.py.")
    ap.add_argument("--sample", type=int, default=0,
                    help="Randomly sample this many personas from the available pool "
                         "(0 = run every persona). Use with a big --persona-file so each "
                         "Hermes run covers a different, wide slice of real people.")
    ap.add_argument("--seed", type=int, default=None,
                    help="Random seed for --sample (omit for a fresh draw every run).")
    args = ap.parse_args()

    # Build the available pool: built-in ten + any generated/external personas.
    registry = dict(PERSONAS)
    if args.persona_file:
        loaded = personas_mod.load_personas_from_file(args.persona_file)
        registry.update(loaded)
        print(f"Loaded {len(loaded)} persona(s) from {args.persona_file}; "
              f"pool is now {len(registry)} total.", flush=True)

    if args.personas.strip().lower() == "all":
        persona_ids = list(registry.keys())
    else:
        persona_ids = [p.strip() for p in args.personas.split(",") if p.strip()]

    unknown = [p for p in persona_ids if p not in registry]
    if unknown:
        sys.exit(f"Unknown persona(s): {', '.join(unknown)}. "
                 f"Pool has {len(registry)} personas (built-in + --persona-file).")

    if args.sample and args.sample < len(persona_ids):
        rng = random.Random(args.seed)
        persona_ids = rng.sample(persona_ids, args.sample)
        print(f"Sampled {len(persona_ids)} persona(s) from the pool"
              f"{'' if args.seed is None else f' (seed={args.seed})'}.", flush=True)

    os.makedirs(args.out, exist_ok=True)
    client = get_client(args.mock)

    # The across-people brain. It persists between runs, so every test session makes the
    # app a little better at knowing which faithful move fits which kind of person.
    evidence = ke.EvidenceStore(path=os.path.join(args.out, "evidence.json"))

    results = []
    for pid in persona_ids:
        persona = registry[pid]
        mode = "MOCK" if args.mock else "LIVE"
        print(f"[{mode}] Ministering to: {persona.label} ...", flush=True)

        convo, profile = run_conversation(client, persona, args.minister_model,
                                          args.persona_model, args.turns, evidence=evidence)
        scorecard = run_judge(client, persona, format_transcript(persona, convo),
                              args.judge_model)
        tpath = write_transcript_file(args.out, persona, convo, scorecard)

        # Close the loop: record what we learned about this kind of person into the store,
        # and append the full trial to the durable, append-only dataset.
        if "error" not in scorecard:
            situation = ke._situation_key(profile)
            approach = profile.approach_history[-1] if profile.approach_history else "GENTLE_EXPLORE"
            outcome = derive_outcome(scorecard)
            evidence.record_outcome(situation, approach, outcome)
            models = {"minister": args.minister_model, "persona": args.persona_model,
                      "judge": args.judge_model}
            # Read where the person landed on the journey + the human-handoff ladder.
            last_seeker = next((t for s, t in reversed(convo) if s == "seeker"), "")
            last_minister = next((t for s, t in reversed(convo) if s == "minister"), "")
            connection = co.assess_connection(profile, last_seeker).to_dict()
            # The smart "Talk to a real person" button's actual decision for this person:
            # missionary link if ready, else notify the MBM admin to step in / verify.
            handoff = co.resolve_handoff(profile, last_seeker, last_minister).to_dict()
            append_trial(args.out, persona, convo, scorecard, situation, approach, outcome,
                         models, args.seed or 1, connection, handoff)
            print(f"        learned> situation='{situation}' approach={approach} "
                  f"outcome={outcome}", flush=True)
            print(f"        journey> stage={connection['journey_stage']} "
                  f"next_human={connection['recommended_level']} "
                  f"missionary_ready={connection['missionary_ready']}", flush=True)
            print(f"        handoff> reached={handoff['reached']} action={handoff['action']}",
                  flush=True)

        results.append({"id": pid, "label": persona.label, "scorecard": scorecard})
        verdict = scorecard.get("faithfulness_verdict", "error")
        print(f"        verdict: {verdict}  ->  {tpath}", flush=True)

    evidence.save()
    report_path = write_report(args.out, results)
    print(f"\nLearned data saved: {os.path.join(args.out, 'evidence.json')}")
    print(f"Report written: {report_path}")


if __name__ == "__main__":
    main()
