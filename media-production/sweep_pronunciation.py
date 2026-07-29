#!/usr/bin/env python3
"""Run the pronunciation ear over EVERY build and rank what is actually wrong.

check_pronunciation.py checks one build. Nobody had ever run it across all 199,
which is why Cameron kept catching mispronunciations by hand, one video at a
time (COMPLAINTS #3 Zacchaeus, #4 Nicodemus, #6 verily, #8 calleth, #119 bow).

Writes:
  SWEEP/<build>.txt   raw output per build
  SWEEP/REPORT.md     ranked real suspects, worst first
  SWEEP/state.json    which builds are done, so a restart resumes

The report drops the known false alarms documented in PRONUNCIATION-LAW.md --
whisper modernizes hath/saith/doth no matter what the audio says, and it swaps
articles and contractions freely. Chasing those wastes a session.
"""
import json
import os
import re
import subprocess
import sys

MP = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(MP, "SWEEP")
STATE = os.path.join(OUT, "state.json")

# Trap 1 in PRONUNCIATION-LAW.md: the transcriber modernizes these. A flag on one
# of them says nothing about the audio.
ARCHAIC = {
    "hath", "saith", "doth", "spake", "shew", "shewed", "shewn", "hast",
    "wast", "wert", "art", "dost", "canst", "shalt", "wilt", "didst",
    "couldst", "wouldst", "thee", "thou", "thy", "thine", "ye",
}
# Whisper rewrites these freely; they are transcription noise, not narration.
NOISE = {
    "a", "the", "and", "is", "was", "it", "that", "to", "of", "in", "he",
    "his", "him", "so", "but", "for", "on", "at", "as", "here", "there",
}


def builds():
    ds = sorted(d for d in os.listdir(MP)
                if d.startswith("build-")
                and os.path.isdir(os.path.join(MP, d))
                and os.path.exists(os.path.join(MP, d, "make_narration.py")))
    return sorted(ds, key=lambda d: int(re.match(r"build-(\d+)-", d).group(1)))


def load_state():
    try:
        return json.load(open(STATE))
    except Exception:
        return {}


def run_one(b):
    r = subprocess.run(
        [sys.executable, os.path.join(MP, "check_pronunciation.py"), "--build", b],
        cwd=MP, capture_output=True, text=True, timeout=3600)
    txt = r.stdout + ("\n" + r.stderr if r.returncode else "")
    open(os.path.join(OUT, f"{b}.txt"), "w").write(txt)
    return txt, r.returncode


HIT = re.compile(r"!! '([^']+)' -> heard '([^']*)'\s+\(sound match (\d+)%\)")
SEG = re.compile(r"^\[(BAD  |minor|OK   )\] (\S+)", re.M)


def parse(txt, build):
    """Pull the real suspects out of one build's output."""
    hits, seg = [], "?"
    for line in txt.splitlines():
        m = SEG.match(line)
        if m:
            seg = m.group(2)
            continue
        m = HIT.search(line)
        if not m:
            continue
        said, heard, score = m.group(1), m.group(2), int(m.group(3))
        w = said.lower().strip(".,;:!?'\"")
        if w in ARCHAIC or w in NOISE:
            continue
        if heard.lower().strip(".,;:!?'\"") in NOISE:
            continue
        if len(w) <= 2:
            continue
        hits.append({"build": build, "segment": seg, "word": said,
                     "heard": heard, "score": score})
    return hits


def write_report(all_hits, done, total):
    all_hits.sort(key=lambda h: (h["score"], h["build"]))
    by_word = {}
    for h in all_hits:
        by_word.setdefault(h["word"].lower(), []).append(h)
    repeat = sorted((w, hs) for w, hs in by_word.items() if len(hs) > 1)
    with open(os.path.join(OUT, "REPORT.md"), "w") as f:
        f.write("# Pronunciation sweep\n\n")
        f.write(f"Swept {done}/{total} builds. {len(all_hits)} real suspects "
                f"across {len(by_word)} distinct words.\n\n")
        f.write("Known false alarms (archaic forms whisper modernizes, and "
                "articles) are already filtered out -- see PRONUNCIATION-LAW.md.\n\n")
        f.write("## Words wrong in more than one video -- fix these first\n\n")
        f.write("A word that misreads in several builds is a global respelling, "
                "not a one-off.\n\n")
        f.write("| word | videos | worst match | heard as |\n|---|---|---|---|\n")
        for w, hs in sorted(repeat, key=lambda x: -len(x[1])):
            vids = ", ".join(sorted({h["build"].split("-")[1] for h in hs}))
            f.write(f"| {w} | {len(hs)} ({vids}) | {min(h['score'] for h in hs)}% "
                    f"| {hs[0]['heard']} |\n")
        f.write("\n## Every suspect, worst sound match first\n\n")
        f.write("| build | segment | text says | voice said | match |\n")
        f.write("|---|---|---|---|---|\n")
        for h in all_hits:
            f.write(f"| {h['build']} | {h['segment']} | {h['word']} | "
                    f"{h['heard']} | {h['score']}% |\n")
    json.dump(all_hits, open(os.path.join(OUT, "hits.json"), "w"), indent=1)


def main():
    os.makedirs(OUT, exist_ok=True)
    bs = builds()
    state = load_state()
    all_hits = []
    for b, hits in state.get("hits", {}).items():
        all_hits += hits
    for i, b in enumerate(bs, 1):
        if b in state.get("done", []):
            continue
        print(f"[{i}/{len(bs)}] {b}", flush=True)
        try:
            txt, rc = run_one(b)
        except subprocess.TimeoutExpired:
            print(f"    TIMEOUT {b}", flush=True)
            continue
        hits = parse(txt, b)
        all_hits += hits
        print(f"    {len(hits)} suspect(s)", flush=True)
        state.setdefault("done", []).append(b)
        state.setdefault("hits", {})[b] = hits
        json.dump(state, open(STATE, "w"))
        write_report(all_hits, len(state["done"]), len(bs))
    write_report(all_hits, len(state.get("done", [])), len(bs))
    print(f"SWEEP DONE: {len(all_hits)} suspects -> SWEEP/REPORT.md")


if __name__ == "__main__":
    main()
