#!/usr/bin/env python3
"""Find every proper noun the narration has to say, and where it is said.

Cameron, 2026-07-19: "barabbas ... you have to look that one up and the reader
voice has to read it knowing how to say it."

The whisper sweep ranks by sound-difference, which buries names under
transcription noise (numbers come back as digits, 'yea' as 'yeah'). Names are the
thing that actually gets a video rejected, so they get their own pass: harvest
them, test each one through the ear, respell only the ones that come back wrong.

Writes NAMES/harvest.json: {name: {"count": n, "builds": {build: [segment ids]},
"voices": [speaker, ...]}} so each name can later be tested in the voice that
actually says it -- a respelling that fixes Eric can break Steffan.
"""
import json
import os
import re
import sys

MP = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(MP, "NAMES")

# Words that start a sentence or are ordinary English; capitalisation alone does
# not make something hard to say. Anything here is dropped before testing.
COMMON = {
    "the", "and", "but", "for", "so", "then", "when", "where", "what", "who",
    "why", "how", "this", "that", "these", "those", "he", "she", "they", "it",
    "his", "her", "their", "i", "you", "we", "us", "him", "them", "a", "an",
    "in", "on", "at", "to", "of", "by", "with", "from", "as", "if", "not",
    "no", "yes", "one", "two", "three", "four", "five", "six", "seven",
    "eight", "nine", "ten", "god", "lord", "jesus", "christ", "father", "son",
    "spirit", "holy", "there", "here", "now", "come", "go", "let", "look",
    "see", "hear", "take", "give", "make", "know", "think", "say", "said",
    "because", "before", "after", "every", "all", "some", "any", "man",
    "woman", "men", "people", "day", "night", "king", "temple", "city",
    "verily", "behold", "thou", "thee", "thy", "ye", "his", "my", "our",
    "amen", "well", "yet", "still", "even", "just", "only", "also", "up",
    "down", "out", "over", "under", "again", "away", "back", "into", "his",
}

# Ordinary English never needs a respelling no matter how it is capitalised.
# A name is worth testing when it is not a dictionary word -- crudely, when it
# carries letter runs English rarely uses, or simply is not in COMMON and is
# long enough to be a name.
TOKEN = re.compile(r"\b([A-Z][a-zA-Z]{2,})\b")


def segments_of(build):
    d = os.path.join(MP, build)
    sys.path.insert(0, d)
    cwd = os.getcwd()
    os.chdir(d)
    try:
        import importlib
        mn = importlib.import_module("make_narration")
        importlib.reload(mn)
        segs = []
        for s in mn.SEGMENTS:
            if len(s) >= 5:
                segs.append((s[0], "narrator", s[4]))
            else:
                segs.append((s[0], s[1], s[2]))
        spoken = getattr(mn, "SPOKEN", {}) or {}
        return segs, spoken
    finally:
        os.chdir(cwd)
        if d in sys.path:
            sys.path.remove(d)
        for m in ("make_narration", "mbm_speakers", "mbm_pronounce"):
            sys.modules.pop(m, None)


def builds():
    ds = [d for d in os.listdir(MP)
          if d.startswith("build-") and os.path.isdir(os.path.join(MP, d))
          and os.path.exists(os.path.join(MP, d, "make_narration.py"))]
    return sorted(ds, key=lambda d: int(re.match(r"build-(\d+)-", d).group(1)))


def main():
    os.makedirs(OUT, exist_ok=True)
    names = {}
    skipped = []
    for b in builds():
        try:
            segs, spoken = segments_of(b)
        except Exception as e:
            skipped.append((b, f"{type(e).__name__}: {e}"))
            continue
        for sid, speaker, text in segs:
            for w in TOKEN.findall(text):
                if w.lower() in COMMON:
                    continue
                e = names.setdefault(w, {"count": 0, "builds": {}, "voices": []})
                e["count"] += 1
                e["builds"].setdefault(b, [])
                if sid not in e["builds"][b]:
                    e["builds"][b].append(sid)
                if speaker not in e["voices"]:
                    e["voices"].append(speaker)
                # a name already respelled somewhere is recorded, so the pass
                # can reuse a fix that is known to work instead of re-deriving it
                if w in spoken:
                    e["existing"] = spoken[w]
    json.dump(names, open(os.path.join(OUT, "harvest.json"), "w"), indent=1)
    ranked = sorted(names.items(), key=lambda kv: -kv[1]["count"])
    print(f"{len(names)} distinct names across {len(builds())} builds")
    if skipped:
        print(f"SKIPPED {len(skipped)}: {skipped[:5]}")
    print("\ntop 40 by how often they are spoken:")
    for w, e in ranked[:40]:
        print(f"  {e['count']:4}  {w:22} in {len(e['builds'])} builds "
              f"({','.join(e['voices'])})"
              + (f"  [already respelled: {e['existing']}]" if "existing" in e else ""))


if __name__ == "__main__":
    main()
