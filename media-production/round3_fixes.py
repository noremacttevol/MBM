#!/usr/bin/env python3
"""Round 3: in-context A/B for every REAL defect from the shipped-audio audit
(SWEEP/SHIPPED-AUDIT.md, 2026-07-20). Same law as round 2: render the actual
segment in the actual voice, adopt a candidate only if it clearly beats the
baseline. Pause-respellings ("word,") are legal — measured to fix boundary
slurs (#132 "devils,").

Each SPEC row tests in ONE representative context; APPLY lists every flagged
(build, word) the winner should be applied to. Winners land in
SWEEP/round3-winners.json as {build: {word: respelling}}.
"""
import asyncio
import difflib
import importlib
import json
import os
import re
import sys

MP = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, MP)
import check_pronunciation as CP  # noqa: E402
from mbm_speakers import voice_of  # noqa: E402

OUT = os.path.join(MP, "SWEEP")
STATE = os.path.join(OUT, "round3-state.json")

# (test build, test segment, word, [candidates])
SPEC = [
    ("build-164-unity-of-faith", "n6", "gem", ["jemm", "jehm"]),
    ("build-62-ephphatha", "s37", "maketh", ["maiketh", "makith"]),
    ("build-84-no-room-manger", "n2", "nazareth", ["nazzureth"]),
    ("build-49-water-to-wine", "n2", "cana", ["kayna", "caynah"]),
    ("build-62-ephphatha", "j1", "ephphatha", ["ef fatha", "effata"]),
    ("build-03-zacchaeus", "j1b", "abide", ["abide", "uhbide"]),
    ("build-126-by-their-fruits", "card", "abide", ["abide", "uhbide"]),
    ("build-10-well", "w25", "messias", ["messyeus"]),
    ("build-51-first-catch-of-fish", "n1", "gennesaret", ["gunnesserett"]),
    ("build-57-jairus-daughter", "n3b", "jairus", ["jyrus"]),
    ("build-198-ensign-for-the-nations", "s2", "ensign", ["ensine"]),
    ("build-40-the-friend-at-midnight", "n5", "crumb", ["krum"]),
    ("build-40-the-friend-at-midnight", "n8", "meant", ["ment"]),
    ("build-40-the-friend-at-midnight", "n14a", "annoyed", ["annoid"]),
    ("build-155-falling-away", "n3", "anchored", ["ankered"]),
    ("build-88-triumphal-entry", "s5", "foal", ["fohl"]),
    ("build-182-spirit-returns-to-god", "s0", "nigh", ["nye"]),
    ("build-88-triumphal-entry", "s5", "sion", ["zyon"]),
    ("build-171-baptized-for-the-dead", "s20", "slept", ["slept,"]),
    ("build-83-weeping-over-jerusalem", "s41", "wept", ["wept,"]),
    ("build-72-calling-matthew", "s11", "eateth", ["eatith"]),
    ("build-173-dead-shall-hear", "j21", "raiseth", ["rayzeth"]),
    ("build-160-stone-cut", "kv45", "sawest", ["sawwest"]),
    ("build-192-the-fast-god-has-chosen", "g7", "seest", ["seeist"]),
    ("build-162-keys-of-kingdom", "n5", "men", ["menn"]),
    ("build-108-my-sheep-hear-my-voice", "n5", "sheep", ["sheep,"]),
    ("build-135-rainbow-covenant", "n2b", "fill", ["fill,"]),
    ("build-135-rainbow-covenant", "n1", "ark", ["ark,"]),
    ("build-66-malchus-ear", "n1", "luke", ["luke,"]),
    ("build-186-joint-heirs", "s2", "joint", ["joynt"]),
    ("build-111-lilies-and-sparrows", "jv33", "ye", ["yee"]),
    ("build-93-barabbas-goes-free", "n0", "barabbas", ["burabbus"]),
    ("build-18-emmaus", "n0", "emmaus", ["emmayus"]),
    ("build-88-triumphal-entry", "n0a2", "colt", ["coalt"]),
]

# winner of `word` also applies to these builds (every audit row of that word)
APPLY = {
    "gem": ["build-164-unity-of-faith", "build-165-laying-on-hands",
            "build-166-baptized-properly", "build-167-chosen-ordained",
            "build-168-born-water-spirit", "build-170-sacrament-worthily",
            "build-03-zacchaeus"],
    "maketh": ["build-62-ephphatha", "build-124-love-your-enemies",
               "build-188-be-ye-therefore-perfect", "build-150-shepherd-psalm"],
    "nazareth": ["build-84-no-room-manger", "build-88-triumphal-entry",
                 "build-73-this-day-fulfilled", "build-153-restitution"],
    "cana": ["build-49-water-to-wine", "build-50-noblemans-son"],
    "seest": ["build-192-the-fast-god-has-chosen", "build-44-two-debtors",
              "build-74-woman-washed-his-feet"],
    "men": ["build-162-keys-of-kingdom", "build-160-stone-cut",
            "build-45-wicked-tenants"],
    "abide": [],  # per-build: b03 (jesus) and b126 (narrator) decided separately
}


def seg_lookup(build):
    bdir = os.path.join(MP, build)
    sys.path.insert(0, bdir)
    for m in ("make_narration", "mbm_pronounce", "mbm_speakers",
              "mbm_caption_timing"):
        sys.modules.pop(m, None)
    mn = importlib.import_module("make_narration")
    pron = importlib.import_module("mbm_pronounce")
    sys.path.pop(0)
    segs = {s[0]: (s[1], s[2]) for s in mn.SEGMENTS}
    return segs, (getattr(mn, "SPOKEN", {}) or {}), pron


def word_score(word, transcript):
    tw = CP.norm(transcript)
    wn = re.sub(r"[^a-z]", "", word.lower())
    best = 0.0
    for i in range(max(1, len(tw))):
        cand = re.sub(r"[^a-z]", "", "".join(tw[i:i + max(1, len(word.split()))]))
        best = max(best, difflib.SequenceMatcher(None, wn, cand).ratio())
    return best


def hear(text, speaker):
    voice, rate, pitch = voice_of(speaker)
    tmp = os.path.join(OUT, "_round3.mp3")
    asyncio.run(CP.say(text, voice, rate, pitch, tmp))
    return CP.transcribe(tmp)


def main():
    try:
        state = json.load(open(STATE))
    except Exception:
        state = {}
    winners = {}
    cache = {}
    for build, seg, word, cands in SPEC:
        key = f"{build}|{seg}|{word}"
        if key not in state:
            if build not in cache:
                try:
                    cache[build] = seg_lookup(build)
                except Exception as e:
                    print(f"{key} LOOKUP-ERROR {e}", flush=True)
                    continue
            segs, spoken, pron = cache[build]
            if seg not in segs:
                print(f"{key} NO-SEGMENT", flush=True)
                continue
            speaker, text = segs[seg]
            try:
                heard = hear(pron.spoken_text(text, spoken, speaker), speaker)
            except Exception as e:
                print(f"{key} TTS-ERROR {e}", flush=True)
                continue
            rec = {"base": round(word_score(word, heard), 3), "cands": {}}
            for cand in cands:
                over = dict(spoken)
                over[word] = cand
                try:
                    h2 = hear(pron.spoken_text(text, over, speaker), speaker)
                except Exception as e:
                    print(f"{key}/{cand} TTS-ERROR {e}", flush=True)
                    continue
                rec["cands"][cand] = round(word_score(word, h2), 3)
            state[key] = rec
            json.dump(state, open(STATE, "w"), indent=1)
        rec = state[key]
        best_cand, best_s = None, rec["base"]
        for c, s in rec["cands"].items():
            if s > best_s + 0.1:
                best_cand, best_s = c, s
        print(f"{key}: base {rec['base']:.0%} -> "
              f"{'ADOPT ' + best_cand + f' {best_s:.0%}' if best_cand else 'keep as-is'}",
              flush=True)
        if best_cand:
            targets = APPLY.get(word, []) or [build]
            for t in targets:
                winners.setdefault(t, {})[word] = best_cand
    json.dump(winners, open(os.path.join(OUT, "round3-winners.json"), "w"),
              indent=1)
    print(f"\nwinners across {len(winners)} builds -> SWEEP/round3-winners.json")


if __name__ == "__main__":
    main()
