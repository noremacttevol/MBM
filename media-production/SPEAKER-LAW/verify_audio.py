#!/usr/bin/env python3
"""Confirm the spoken audio actually says what the caption shows.

The caption keeps the true spelling while the TTS gets a respelled string, so the
two are deliberately different *inputs*. What must still be true is that the
SOUND matches the words on screen. This transcribes each segment's mp3 and
compares it to the caption text.

It catches the failure modes nothing else here would:
  * a respelling leaking into the caption, or the caption text drifting from the
    audio after a plan edit
  * segments rendered from a stale plan, so caption and voice disagree
  * a gross TTS misread of the kind that motivated this whole pass — #30's "uhs"
    read as "Oz", #41's "forsaketh" as "for-Saccath"

It CANNOT judge homographs: whisper transcribes both readings of live/close/bow
identically. Those remain a listening job, and are reported separately so the
list is at least known.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
MP = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, MP)          # mbm_pronounce lives beside the builds

_MODEL = None


def model():
    global _MODEL
    if _MODEL is None:
        from faster_whisper import WhisperModel
        _MODEL = WhisperModel("base.en", device="cpu", compute_type="int8")
    return _MODEL


def norm(s):
    s = re.sub(r"[^a-z0-9 ]", " ", s.lower())
    return re.sub(r"\s+", " ", s).strip()


def similarity(a, b):
    """Word-level overlap, order-insensitive enough to survive punctuation."""
    from difflib import SequenceMatcher
    return SequenceMatcher(None, norm(a).split(), norm(b).split()).ratio()


def check(build, floor=0.72):
    d = os.path.join(MP, build)
    plan_p = os.path.join(HERE, "plans", f"{build}.json")
    if not os.path.exists(plan_p):
        return None
    plan = json.load(open(plan_p))
    from mbm_pronounce import audit

    bad, homographs, checked = [], set(), 0
    for seg in plan["segments"]:
        sid, text = seg["id"], seg.get("text", "")
        if not text.strip() or seg.get("silent") or sid == "HUSH":
            continue
        mp3 = os.path.join(d, "audio", f"{sid}.mp3")
        if not os.path.exists(mp3):
            return {"build": build, "skipped": f"not rebuilt (no audio/{sid}.mp3)"}
        segs, _ = model().transcribe(mp3)
        heard = " ".join(s.text for s in segs)
        r = similarity(text, heard)
        checked += 1
        if r < floor:
            bad.append((sid, seg.get("speaker"), round(r, 2), text[:70], heard[:70]))
        for w in audit(text):
            homographs.add(w)
    return {"build": build, "checked": checked, "mismatches": bad,
            "homographs": sorted(homographs)}


def main():
    names = sys.argv[1:]
    if not names:
        d = json.load(open(os.path.join(HERE, "batch-log.json")))
        names = sorted(k for k, v in d.items() if v.get("status") == "shipped")
    allh, bad_builds = {}, 0
    for b in names:
        r = check(b)
        if not r:
            continue
        if r.get("skipped"):
            print(f"{b}: skipped — {r['skipped']}", flush=True)
            continue
        if r["homographs"]:
            allh[b] = r["homographs"]
        if r["mismatches"]:
            bad_builds += 1
            print(f"\n{b}: {len(r['mismatches'])} of {r['checked']} segments "
                  f"do not match", flush=True)
            for sid, sp, ratio, want, heard in r["mismatches"][:5]:
                print(f"    {sid} [{sp}] {ratio}", flush=True)
                print(f"       caption: {want}", flush=True)
                print(f"       heard  : {heard}", flush=True)
        else:
            print(f"{b}: ok ({r['checked']} segments match)", flush=True)

    print(f"\n{len(names) - bad_builds}/{len(names)} builds: audio matches caption")
    if allh:
        print(f"\nHOMOGRAPHS present in {len(allh)} builds — whisper cannot judge "
              f"these, they need an ear:")
        for b, ws in sorted(allh.items()):
            print(f"  {b}: {', '.join(ws)}")
    return 1 if bad_builds else 0


if __name__ == "__main__":
    sys.exit(main())
