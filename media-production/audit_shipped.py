#!/usr/bin/env python3
"""Ear-check the ACTUAL shipped audio of every non-approved build.

This is the step every earlier pass skipped: gate_rebuilds compared the TEXT
sent to the TTS, and check_pronunciation --build RE-RENDERS fresh audio — but
nothing ever transcribed the audio/*.mp3 files that are muxed into the shipped
mp4s. This does exactly that: transcribe each segment mp3 with faster-whisper,
align it word-by-word against the caption text, and flag real mismatches.

Filters the documented false-alarm classes (PRONUNCIATION-LAW.md): archaic
forms whisper modernizes, digit rewrites, homophones that are the correct
sound, and function-word noise. Approved builds (approvals.json) are skipped.

Writes SWEEP/shipped-audit-state.json (resumable) and
SWEEP/SHIPPED-AUDIT.md ranked worst-first.
"""
import difflib
import importlib
import json
import os
import re
import sys

MP = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, MP)
import check_pronunciation as CP  # noqa: E402

OUT = os.path.join(MP, "SWEEP")
STATE = os.path.join(OUT, "shipped-audit-state.json")
REPORT = os.path.join(OUT, "SHIPPED-AUDIT.md")

ARCHAIC = {
    "hath", "saith", "doth", "spake", "shew", "shewed", "shewn", "hast",
    "wast", "wert", "art", "dost", "canst", "shalt", "wilt", "didst",
    "couldst", "wouldst", "thee", "thou", "thy", "thine", "ye", "unto",
    "yea", "nay", "verily", "wherefore", "hither", "thither", "whence",
    "aught", "ought", "mine", "brethren", "begat", "cometh", "goeth",
}
NOISE = {
    "a", "the", "and", "is", "was", "it", "that", "to", "of", "in", "he",
    "his", "him", "so", "but", "for", "on", "at", "as", "here", "there",
    "an", "or", "are", "were", "be", "been", "this", "these", "those",
    "with", "into", "upon", "said", "set", "had", "has", "have", "will",
    "shall", "would", "who", "whom", "whose", "which", "what", "when",
    "then", "than", "too", "two", "one", "won", "our", "your", "my",
}
# spelled differently, sounds the same — correct audio, not a defect
HOMOPHONES = [
    ("heir", "air"), ("draught", "draft"), ("ought", "awt"), ("sow", "so"),
    ("weigh", "way"), ("wait", "weight"), ("ark", "arc"), ("sell", "cell"),
    ("hole", "whole"), ("holy", "wholly"), ("write", "right"),
    ("write", "ride"), ("wrote", "rode"), ("rode", "wrote"), ("sion", "zion"),
    ("patience", "patients"), ("past", "passed"), ("eye", "i"),
    ("guest", "guessed"), ("son", "sun"), ("meat", "meet"), ("knew", "new"),
]


def norm_words(s):
    s = re.sub(r"[^a-z0-9' ]", " ", s.lower())
    return [w for w in s.split() if w]


def is_noise(a, b):
    """True when the (expected, heard) pair is a known non-defect."""
    if a in ARCHAIC or a in NOISE or b in NOISE:
        return True
    if a.isdigit() or b.isdigit() or not b:
        return True
    if a.rstrip("s") == b.rstrip("s"):
        return True
    for x, y in HOMOPHONES:
        if (a.startswith(x) and b.startswith(y)) or (a.startswith(y) and b.startswith(x)):
            return True
    # -eth/-est archaic verb endings whisper modernizes (calleth -> calls/called)
    if a.endswith(("eth", "est")) and difflib.SequenceMatcher(None, a[:-3], b[:3 + len(a)]).ratio() > 0.6:
        return True
    # t/d flap pairs (said/set class): differ only in final t/d
    if len(a) > 2 and len(b) > 2 and a[:-1] == b[:-1] and {a[-1], b[-1]} <= {"t", "d"}:
        return True
    return False


def compare(expected, heard):
    """Real suspects: (expected word, heard word, similarity)."""
    ew, hw = norm_words(expected), norm_words(heard)
    out = []
    sm = difflib.SequenceMatcher(None, ew, hw)
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal":
            continue
        exp = ew[i1:i2]
        got = hw[j1:j2]
        for k, a in enumerate(exp):
            b = got[k] if k < len(got) else (got[-1] if got else "")
            r = difflib.SequenceMatcher(None, a, b).ratio()
            if r >= 0.8 or is_noise(a, b):
                continue
            out.append((a, b, round(r, 2)))
    return out


def main():
    approved = set()
    try:
        approved = {int(k) for k in json.load(open(os.path.join(MP, "approvals.json")))}
    except Exception:
        pass
    try:
        state = json.load(open(STATE))
    except Exception:
        state = {"done": [], "hits": {}}

    dirs = sorted(d for d in os.listdir(MP) if d.startswith("build-")
                  and os.path.isfile(os.path.join(MP, d, "make_narration.py")))
    todo = []
    for d in dirs:
        m = re.match(r"build-(\d+)", d)
        if m and int(m.group(1)) in approved:
            continue
        if d in state["done"]:
            continue
        todo.append(d)

    for i, d in enumerate(todo, 1):
        bdir = os.path.join(MP, d)
        sys.path.insert(0, bdir)
        for mod in ("make_narration", "mbm_pronounce", "mbm_speakers",
                    "mbm_caption_timing"):
            sys.modules.pop(mod, None)
        try:
            mn = importlib.import_module("make_narration")
            pron = importlib.import_module("mbm_pronounce")
            segments = [(s[0], s[1], s[2]) for s in mn.SEGMENTS]
            spoken_over = getattr(mn, "SPOKEN", {}) or {}
        except Exception as e:
            print(f"[{i}/{len(todo)}] {d} IMPORT-ERROR {e}", flush=True)
            sys.path.pop(0)
            continue
        sys.path.pop(0)
        hits = []
        for sid, speaker, text in segments:
            mp3 = os.path.join(bdir, "audio", f"{sid}.mp3")
            if not os.path.isfile(mp3):
                hits.append({"seg": sid, "word": "(NO AUDIO FILE)", "heard": "",
                             "sim": 0.0})
                continue
            try:
                heard = CP.transcribe(mp3)
            except Exception as e:
                print(f"    {sid} TRANSCRIBE-ERROR {e}", flush=True)
                continue
            # A word is a defect only if the audio matches NEITHER the caption
            # NOR the intended spoken text. Caption-only mismatches are the
            # phrase joins (to day -> today); spoken-only mismatches are the
            # respellings themselves (zebbuhdee heard as zebedee = correct).
            expected = pron.spoken_text(text, spoken_over, speaker)
            cap_hits = compare(text, heard)
            spk_heard = {b for _, b, _ in compare(expected, heard)}
            for a, b, r in cap_hits:
                if b in spk_heard:
                    hits.append({"seg": sid, "word": a, "heard": b, "sim": r})
        state["done"].append(d)
        state["hits"][d] = hits
        json.dump(state, open(STATE, "w"))
        print(f"[{i}/{len(todo)}] {d}: {len(hits)} suspect(s)"
              + ("".join(f"\n    {h['seg']}: '{h['word']}' -> '{h['heard']}' {h['sim']}"
                         for h in hits) if hits else ""), flush=True)

    # report, worst first
    rows = [dict(h, build=b) for b, hs in state["hits"].items() for h in hs]
    rows.sort(key=lambda h: h["sim"])
    with open(REPORT, "w") as f:
        f.write("# Shipped-audio audit — transcribed the ACTUAL segment mp3s\n\n")
        f.write(f"{len(state['done'])} builds audited, {len(rows)} real suspects "
                "after false-alarm filtering.\n\n")
        f.write("| build | seg | caption says | audio says | match |\n|---|---|---|---|---|\n")
        for h in rows:
            f.write(f"| {h['build']} | {h['seg']} | {h['word']} | {h['heard']} | {int(h['sim']*100)}% |\n")
    print(f"\nAUDIT DONE: {len(rows)} suspects -> {REPORT}")


if __name__ == "__main__":
    main()
