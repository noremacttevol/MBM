#!/usr/bin/env python3
"""Whisper-transcribe the FINAL mp4 audio of every build and diff vs the script.

audit_shipped.py transcribed the segment mp3s in audio/ — but those are inputs,
not the deliverable. A build whose mp3s were re-recorded but whose mp4 was never
re-muxed (or was truncated) ships audio the mp3 audit never heard. This sweep
transcribes the audio track of the shipped mp4 itself, so what is checked is
exactly what a viewer hears.

Diff target is the concatenated SEGMENTS caption text, with the same false-alarm
filters as audit_shipped (archaic modernization, homophones, noise words). Two
outputs per build:
  - suspects: mismatches that fail against BOTH the caption text and the
    rendered spoken text (real-misread candidates)
  - archaic_watch: -eth/-est pairs the noise filter would normally hide, kept
    for ear-review because Cameron's complaints are mostly archaic forms
    (calleth, findeth, liveth, maketh, abideth, overcometh...)

Resumable: SWEEP/final-audio-state.json. Report: SWEEP/FINAL-AUDIO-AUDIT.md.
Usage: python3 sweep_final_audio.py [--max-seconds N] [--only build-NN-slug ...]
"""
import argparse
import difflib
import glob
import importlib
import json
import os
import re
import sys
import time

MP = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, MP)
import check_pronunciation as CP  # noqa: E402
from audit_shipped import compare as base_compare, norm_words, is_noise  # noqa: E402

OUT = os.path.join(MP, "SWEEP")
STATE = os.path.join(OUT, "final-audio-state.json")
REPORT = os.path.join(OUT, "FINAL-AUDIO-AUDIT.md")


def final_mp4(bdir):
    """The shipped cut: the one root mp4 that is not a .orig backup."""
    c = [f for f in glob.glob(os.path.join(bdir, "*.mp4"))
         if not f.endswith(".orig.mp4")]
    return c[0] if len(c) == 1 else None


def compare_watch(expected, heard):
    """Like audit_shipped.compare but ALSO returns the -eth/-est pairs the
    noise filter hides, with the crude sound-skeleton similarity."""
    ew, hw = norm_words(expected), norm_words(heard)
    suspects, watch = [], []
    sm = difflib.SequenceMatcher(None, ew, hw)
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal":
            continue
        exp, got = ew[i1:i2], hw[j1:j2]
        for k, a in enumerate(exp):
            b = got[k] if k < len(got) else (got[-1] if got else "")
            r = difflib.SequenceMatcher(None, a, b).ratio()
            if a.endswith(("eth", "est")) and a not in ("best", "rest", "west",
                                                        "lest", "test"):
                watch.append((a, b, round(CP.similarity(a, b), 2)))
            if r >= 0.8 or is_noise(a, b):
                continue
            suspects.append((a, b, round(r, 2)))
    return suspects, watch


def load_build(bdir):
    """(segments, spoken_overrides, pron_module) via the build's own modules."""
    sys.path.insert(0, bdir)
    for mod in ("make_narration", "mbm_pronounce", "mbm_speakers",
                "mbm_caption_timing"):
        sys.modules.pop(mod, None)
    try:
        mn = importlib.import_module("make_narration")
        pron = importlib.import_module("mbm_pronounce")
        segs = [(s[0], s[1], s[2]) if len(s) < 5 else (s[0], None, s[4])
                for s in mn.SEGMENTS]
        return segs, (getattr(mn, "SPOKEN", {}) or {}), pron
    finally:
        sys.path.pop(0)
        for mod in ("make_narration", "mbm_pronounce", "mbm_speakers",
                    "mbm_caption_timing"):
            sys.modules.pop(mod, None)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-seconds", type=int, default=0,
                    help="stop cleanly after this many seconds (resumable)")
    ap.add_argument("--only", nargs="*", help="specific build dirs")
    a = ap.parse_args()
    t0 = time.time()

    os.makedirs(OUT, exist_ok=True)
    try:
        state = json.load(open(STATE))
    except Exception:
        state = {"done": [], "builds": {}}

    dirs = a.only or sorted(
        d for d in os.listdir(MP)
        if d.startswith("build-") and final_mp4(os.path.join(MP, d)))
    todo = [d for d in dirs if d not in state["done"]]

    for i, d in enumerate(todo, 1):
        if a.max_seconds and time.time() - t0 > a.max_seconds:
            print(f"TIME BUDGET REACHED — {len(todo)-i+1} builds left, state saved")
            break
        bdir = os.path.join(MP, d)
        mp4 = final_mp4(bdir)
        try:
            segs, spoken_over, pron = load_build(bdir)
        except Exception as e:
            print(f"[{i}/{len(todo)}] {d} IMPORT-ERROR {e}", flush=True)
            state["done"].append(d)
            state["builds"][d] = {"error": f"import: {e}"}
            json.dump(state, open(STATE, "w"))
            continue
        caption_full = " ".join(t for _, _, t in segs)
        spoken_full = " ".join(pron.spoken_text(t, spoken_over, sp)
                               for _, sp, t in segs)
        try:
            heard = CP.transcribe(mp4)
        except Exception as e:
            print(f"[{i}/{len(todo)}] {d} TRANSCRIBE-ERROR {e}", flush=True)
            state["done"].append(d)
            state["builds"][d] = {"error": f"transcribe: {e}"}
            json.dump(state, open(STATE, "w"))
            continue
        cap_sus, cap_watch = compare_watch(caption_full, heard)
        spk_sus, spk_watch = compare_watch(spoken_full, heard)
        spk_heard = {b for _, b, _ in spk_sus}
        # real suspect: wrong against the caption AND not explained by a
        # respelling that whisper wrote back differently
        suspects = [(x, b, r) for x, b, r in cap_sus if b in spk_heard]
        # archaic watch: wrong-looking against BOTH caption and spoken forms
        spk_watch_heard = {b for _, b, _ in spk_watch}
        watch = [(x, b, r) for x, b, r in cap_watch
                 if b in spk_watch_heard and x != b]
        state["done"].append(d)
        state["builds"][d] = {
            "mp4": os.path.basename(mp4),
            "heard": heard,
            "suspects": suspects,
            "watch": watch,
        }
        json.dump(state, open(STATE, "w"))
        line = f"[{i}/{len(todo)}] {d}: {len(suspects)} suspect(s), {len(watch)} archaic-watch"
        for x, b, r in suspects:
            line += f"\n    SUSPECT '{x}' -> heard '{b}' ({r})"
        for x, b, r in watch:
            line += f"\n    watch   '{x}' -> heard '{b}' (sound {r})"
        print(line, flush=True)

    rows = []
    for b, v in state["builds"].items():
        for x, hb, r in v.get("suspects", []):
            rows.append((b, "SUSPECT", x, hb, r))
        for x, hb, r in v.get("watch", []):
            rows.append((b, "watch", x, hb, r))
    rows.sort(key=lambda t: (t[1] != "SUSPECT", t[4]))
    with open(REPORT, "w") as f:
        f.write("# Final-audio audit — transcribed the SHIPPED mp4 audio track\n\n")
        f.write(f"{len(state['done'])} builds audited.\n\n")
        f.write("| build | class | script says | audio says | match |\n|---|---|---|---|---|\n")
        for b, cls, x, hb, r in rows:
            f.write(f"| {b} | {cls} | {x} | {hb} | {int(r*100)}% |\n")
    print(f"\n{len(state['done'])} done -> {REPORT}")


if __name__ == "__main__":
    main()
