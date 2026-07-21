#!/usr/bin/env python3
"""Which builds' CURRENT audio no longer matches what the corrected dictionary
would speak? The timing.json sidecar next to every segment mp3 records the exact
sentence text edge-tts actually spoke, so this is an exact text gate — no audio
rendering needed.

For every non-approved build: expected = spoken_text(segment text, build SPOKEN,
speaker) vs actual = concatenated sidecar sentences. Normalized compare.
Writes SWEEP/rebuild-list.txt (one build per line) and prints a summary.

A build passes only if EVERY segment matches and every segment has a sidecar.
Approved builds (approvals.json — Cameron's yes) are never touched.
"""
import importlib
import json
import os
import re
import sys

MP = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, MP)


def norm(s):
    # keep parentheses: edge-tts SPEAKS ";)" aloud ("winky face"), so audio
    # rendered before the paren-drop rule must NOT pass the gate
    return re.sub(r"[^a-z0-9()]", "", s.lower())


def build_number(d):
    m = re.match(r"build-(\d+)", d)
    return int(m.group(1)) if m else None


def main():
    approved = set()
    try:
        approved = {int(k) for k in json.load(
            open(os.path.join(MP, "approvals.json")))}
    except Exception:
        pass

    dirs = sorted(d for d in os.listdir(MP)
                  if d.startswith("build-") and
                  os.path.isfile(os.path.join(MP, d, "make_narration.py")))
    need, clean, skipped = [], [], []
    for d in dirs:
        num = build_number(d)
        if num in approved:
            skipped.append(d)
            continue
        bdir = os.path.join(MP, d)
        sys.path.insert(0, bdir)
        for mod in ("make_narration", "mbm_pronounce", "mbm_speakers",
                    "mbm_caption_timing"):
            sys.modules.pop(mod, None)
        try:
            mn = importlib.import_module("make_narration")
            pron = importlib.import_module("mbm_pronounce")
            segments = mn.SEGMENTS
            spoken_over = getattr(mn, "SPOKEN", {}) or {}
        except Exception as e:
            need.append((d, [f"IMPORT-ERROR {e}"]))
            sys.path.pop(0)
            continue
        bad = []
        for seg in segments:
            sid, speaker, text = seg[0], seg[1], seg[2]
            expected = pron.spoken_text(text, spoken_over, speaker)
            tj = os.path.join(bdir, "audio", f"{sid}.timing.json")
            mp3 = os.path.join(bdir, "audio", f"{sid}.mp3")
            if not (os.path.isfile(tj) and os.path.isfile(mp3)):
                bad.append(f"{sid}:NO-AUDIO")
                continue
            try:
                sents = json.load(open(tj))
            except Exception:
                bad.append(f"{sid}:BAD-SIDECAR")
                continue
            actual = " ".join(s.get("text", "") for s in sents)
            if norm(actual) != norm(expected):
                bad.append(sid)
        sys.path.pop(0)
        (need if bad else clean).append((d, bad) if bad else (d, []))

    out = os.path.join(MP, "SWEEP", "rebuild-list.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w") as f:
        for d, bad in need:
            f.write(f"{d}\t{','.join(bad[:12])}\n")
    print(f"approved (untouched): {len(skipped)}")
    print(f"clean (audio already matches dict): {len(clean)}")
    print(f"NEED REBUILD: {len(need)} -> {out}")
    for d, bad in need[:40]:
        print(f"  {d}: {','.join(bad[:8])}")


if __name__ == "__main__":
    main()
