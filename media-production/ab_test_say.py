#!/usr/bin/env python3
"""A/B the GLOBAL respelling dict against plain spelling, and keep what wins.

mbm_pronounce.SAY is applied to EVERY segment of EVERY video at narration time.
56 of its 65 entries are written with hyphens and ALL-CAPS stress marks --
exactly the two forms PRONUNCIATION-LAW.md says get read aloud wrong:

    "Hyphens split a word into two. `for-SAY-keth` became 'for Seyketh'.
     Never put hyphens or ALL-CAPS stress marks in a respelling."

The law was written 2026-07-18; the dict predates it and was never re-measured.
Because it is global, one bad entry mispronounces a word in all 200 videos, which
matches Cameron's report that the rebuild made pronunciation worse, not better.

This does not assume the law is right either. Every entry is rendered BOTH ways,
transcribed back, and scored against the true word. The dict is only rewritten
where the measurement says so, and the losing form is kept in the report so the
call is auditable.
"""
import json
import os
import re
import sys

MP = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, MP)
import check_pronunciation as CP  # noqa: E402

OUT = os.path.join(MP, "NAMES")
CARRIER = "He said {} to them plainly."


def hear(word_form, voice, rate, pitch):
    import asyncio
    import tempfile
    with tempfile.TemporaryDirectory() as td:
        mp3 = os.path.join(td, "t.mp3")
        asyncio.run(CP.say(CARRIER.format(word_form), voice, rate, pitch, mp3))
        heard = CP.transcribe(mp3)
    frame = {"he", "said", "to", "them", "plainly", "the", "a", "and"}
    return " ".join(w for w in CP.norm(heard) if w not in frame) or "-"


def main():
    os.makedirs(OUT, exist_ok=True)
    sys.path.insert(0, os.path.join(MP, "build-93-barabbas-goes-free"))
    import mbm_pronounce as P
    say = dict(P.SAY)

    state_path = os.path.join(OUT, "say-ab.json")
    try:
        state = json.load(open(state_path))
    except Exception:
        state = {}

    # narrator carries most runtime; scripture is the other heavy user of these
    # archaic forms. A form must not be adopted on one voice alone.
    voices = [("narrator", CP.VOICES["narrator"], *CP.RATES["narrator"]),
              ("scripture", CP.VOICES["scripture"], *CP.RATES["scripture"])]

    for i, (word, respell) in enumerate(sorted(say.items()), 1):
        if word in state:
            continue
        rec = {"respell": respell, "voices": {}}
        for sp, voice, rate, pitch in voices:
            try:
                plain_heard = hear(word, voice, rate, pitch)
                resp_heard = hear(respell, voice, rate, pitch)
            except Exception as e:
                print(f"  {word}/{sp} ERROR {e}", flush=True)
                continue
            ps = CP.similarity(word, plain_heard)
            rs = CP.similarity(word, resp_heard)
            rec["voices"][sp] = {"plain_heard": plain_heard, "plain": round(ps, 3),
                                 "respell_heard": resp_heard, "respell": round(rs, 3)}
        v = rec["voices"]
        if v:
            plain_avg = sum(d["plain"] for d in v.values()) / len(v)
            resp_avg = sum(d["respell"] for d in v.values()) / len(v)
            rec["plain_avg"] = round(plain_avg, 3)
            rec["respell_avg"] = round(resp_avg, 3)
            # keep the respelling only if it actually beats the plain word; a tie
            # goes to the plain word, because the plain word cannot be read as two
            # words and never needs maintaining
            rec["verdict"] = ("keep-respelling" if resp_avg > plain_avg + 0.05
                              else "use-plain-word")
            mark = "KEEP " if rec["verdict"] == "keep-respelling" else "DROP "
            print(f"[{i}/{len(say)}] {mark} {word:16} plain {plain_avg:.0%} "
                  f"vs '{respell}' {resp_avg:.0%}", flush=True)
        state[word] = rec
        json.dump(state, open(state_path, "w"), indent=1)

    drops = [w for w, r in state.items() if r.get("verdict") == "use-plain-word"]
    keeps = [w for w, r in state.items() if r.get("verdict") == "keep-respelling"]
    print(f"\nDROP the respelling for {len(drops)} words: {sorted(drops)}")
    print(f"\nKEEP the respelling for {len(keeps)} words: {sorted(keeps)}")


if __name__ == "__main__":
    main()
