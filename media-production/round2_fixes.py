#!/usr/bin/env python3
"""A/B candidate respellings IN CONTEXT for the real suspects from the sweep.

Each entry names the build, segment, written word, and candidate respellings.
The segment's REAL text is rendered in its REAL voice — first as the build
currently speaks it (baseline), then once per candidate — and each render is
transcribed back. A candidate is adopted only if it beats the baseline by a
clear margin (PRONUNCIATION-LAW: never commit an untested respelling; ties go
to the plain word). Winners land in SWEEP/round2-winners.json as
{build: {word: respelling}} for merging into each build's SPOKEN dict.

Suspects that are transcription noise were excluded on purpose: digit rewrites
(twelve->12), archaic normalization (hath->has), homophones that are already
the CORRECT reading (heir=air, draught=draft, ought=awt), and t/d flaps.
"""
import asyncio
import difflib
import json
import os
import re
import sys

MP = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, MP)
import check_pronunciation as CP  # noqa: E402
from mbm_speakers import voice_of  # noqa: E402

OUT = os.path.join(MP, "SWEEP")
STATE = os.path.join(OUT, "round2-state.json")

# (build, segment, written word/phrase, [candidate respellings])
SPEC = [
    ("build-62-ephphatha", "j1", "ephphatha", ["effuhthuh", "effathah"]),
    ("build-22-unmerciful-servant", "j4", "owest", ["ohest", "ohwest"]),
    ("build-160-stone-cut", "kv45", "sawest", ["sawist"]),
    ("build-63-man-born-blind", "j2", "siloam", ["sylohum"]),
    ("build-92-peters-denial", "n5b", "wept", ["weppt"]),
    ("build-83-weeping-over-jerusalem", "s41", "wept", ["weppt"]),
    ("build-59-feeding-4000", "s4", "whence", ["wence"]),
    ("build-72-calling-matthew", "s11", "eateth", ["eeteth"]),
    ("build-21-lost-sheep", "s2", "eateth", ["eeteth"]),
    ("build-104-boy-samuel", "n3", "eli", ["eelye"]),
    ("build-99-flesh-and-bone-thomas", "n4b", "doubt", ["dowt"]),
    ("build-27-leaven", "n6", "dough", ["doh"]),
    ("build-151-ask-of-god", "n4", "kneels", ["neels"]),
    ("build-195-prove-all-things", "s19", "quench", ["kwench"]),
    ("build-115-ram-in-the-thicket", "n3", "climbed", ["climed"]),
    ("build-88-triumphal-entry", "s5", "sion", ["zyon"]),
    ("build-150-shepherd-psalm", "s2", "maketh", ["maykuth"]),
    ("build-150-shepherd-psalm", "s2", "leadeth", ["leedeth"]),
    ("build-150-shepherd-psalm", "s3a", "restoreth", ["ristoreth"]),
    ("build-127-the-strait-gate", "j2", "leadeth", ["leedeth"]),
    ("build-150-shepherd-psalm", "s4", "yea", ["yay"]),
    ("build-116-graven-on-his-palms", "jv15", "yea", ["yay"]),
    ("build-116-graven-on-his-palms", "jv16", "palms", ["pahms"]),
    ("build-41-counting-the-cost", "j1", "yea", ["yay"]),
    ("build-19-shore", "s16", "yea", ["yay"]),
    ("build-164-unity-of-faith", "n6", "gem", ["jem"]),
    ("build-50-noblemans-son", "jv50", "liveth", ["livveth"]),
    ("build-57-jairus-daughter", "jtal", "talitha", ["tuhleethuh"]),
    ("build-71-calling-the-fishermen", "n7", "zebedee", ["zebbuhdee"]),
    ("build-87-boy-in-the-temple", "j1", "wist", ["wisst"]),
    ("build-154-everlasting-gospel", "kv6", "tongue", ["tung"]),
    ("build-187-ye-are-gods", "n82g", "psalm", ["sahm"]),
    ("build-171-baptized-for-the-dead", "s20", "slept", ["sleppt"]),
    ("build-148-ruth-and-the-redeemer", "n3", "boaz", ["bohaz"]),
    ("build-114-abraham-sodom", "card", "interceding", ["interseeding"]),
    ("build-149-hannah-is-heard", "n3a", "watched", ["wotched"]),
    ("build-68-multitudes-mountain", "n7", "faint", ["faynt"]),
    ("build-192-the-fast-god-has-chosen", "g7", "seest", ["seeust"]),
    ("build-44-two-debtors", "jv44", "seest", ["seeust"]),
    ("build-101-still-small-voice", "jv9", "doest", ["dooust"]),
    ("build-169-fulfil-righteousness", "s14", "comest", ["comust"]),
    ("build-69-baptism", "s14", "comest", ["comust"]),
    ("build-120-job-from-whirlwind", "jvB", "canst", ["kanst"]),
]

APPROVED = set()
try:
    APPROVED = {int(k) for k in json.load(open(os.path.join(MP, "approvals.json")))}
except Exception:
    pass


def seg_lookup(build):
    bdir = os.path.join(MP, build)
    sys.path.insert(0, bdir)
    for m in ("make_narration", "mbm_pronounce", "mbm_speakers",
              "mbm_caption_timing"):
        sys.modules.pop(m, None)
    import importlib
    mn = importlib.import_module("make_narration")
    pron = importlib.import_module("mbm_pronounce")
    sys.path.pop(0)
    segs = {s[0]: (s[1], s[2]) for s in mn.SEGMENTS}
    return segs, (getattr(mn, "SPOKEN", {}) or {}), pron


def word_score(word, transcript):
    """Best similarity of `word` against any same-length word window."""
    tw = CP.norm(transcript)
    n = max(1, len(word.split()))
    wn = re.sub(r"[^a-z]", "", word.lower())
    best = 0.0
    for i in range(max(1, len(tw) - n + 1)):
        cand = re.sub(r"[^a-z]", "", "".join(tw[i:i + n]))
        r = difflib.SequenceMatcher(None, wn, cand).ratio()
        best = max(best, r)
    return best


def hear(text, speaker):
    voice, rate, pitch = voice_of(speaker)
    tmp = os.path.join(OUT, "_round2.mp3")
    asyncio.run(CP.say(text, voice, rate, pitch, tmp))
    return CP.transcribe(tmp)


def main():
    os.makedirs(OUT, exist_ok=True)
    try:
        state = json.load(open(STATE))
    except Exception:
        state = {}
    winners = {}
    cache = {}
    for build, seg, word, cands in SPEC:
        m = re.match(r"build-(\d+)", build)
        if m and int(m.group(1)) in APPROVED:
            print(f"SKIP approved {build}")
            continue
        key = f"{build}|{seg}|{word}"
        if key in state:
            rec = state[key]
        else:
            if build not in cache:
                try:
                    cache[build] = seg_lookup(build)
                except Exception as e:
                    print(f"{key} LOOKUP-ERROR {e}")
                    continue
            segs, spoken, pron = cache[build]
            if seg not in segs:
                print(f"{key} NO-SEGMENT")
                continue
            speaker, text = segs[seg]
            base_txt = pron.spoken_text(text, spoken, speaker)
            try:
                heard = hear(base_txt, speaker)
            except Exception as e:
                print(f"{key} TTS-ERROR {e}")
                continue
            base = word_score(word, heard)
            rec = {"base": round(base, 3), "base_heard_has": base >= 0.85,
                   "cands": {}}
            for cand in cands:
                over = dict(spoken)
                over[word] = cand
                ctxt = pron.spoken_text(text, over, speaker)
                try:
                    h2 = hear(ctxt, speaker)
                except Exception as e:
                    print(f"{key}/{cand} TTS-ERROR {e}")
                    continue
                rec["cands"][cand] = round(word_score(word, h2), 3)
            state[key] = rec
            json.dump(state, open(STATE, "w"), indent=1)
        best_cand, best_s = None, rec["base"]
        for c, s in rec["cands"].items():
            if s > best_s + 0.1:
                best_cand, best_s = c, s
        tag = f"ADOPT {best_cand} {best_s:.0%}" if best_cand else "keep plain"
        print(f"{key}: base {rec['base']:.0%} -> {tag}")
        if best_cand:
            winners.setdefault(build, {})[word] = best_cand
    json.dump(winners, open(os.path.join(OUT, "round2-winners.json"), "w"),
              indent=1)
    print(f"\nwinners in {len(winners)} builds -> SWEEP/round2-winners.json")


if __name__ == "__main__":
    main()
