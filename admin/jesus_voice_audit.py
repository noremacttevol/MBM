#!/usr/bin/env python3
"""WHICH Jesus voice is actually in each build? — authoritative, not a marker.

WHY (Cameron, 2026-07-25): the board kept showing videos as "ready" that still had
the OLD Jesus. The gate only asked "is this ElevenLabs (44100 Hz)" — which passes
audio voiced by CHRIS, even though Cameron re-cast Jesus to ALEXANDER. Worse, the
Alexander config got reverted in the shared clone at 07-24 21:47, so the redo loop
generated 207 more clips with the wrong voice. Half the board was trash.

HOW THIS IS DECIDED (no ledgers, no timestamps, no session's word):
ElevenLabs' account history records the voice that produced every generation. The
Alexander pipeline is the ONLY one that sends reverent pause tags
(`<break time="650ms" />`, see mbm_eleven.jesus_pauses), so a history entry whose
text carries those tags AND names Alexander is proof that build's Jesus line was
rendered with the approved voice. Chris-era entries have no pause tags. We rebuild
each build's Jesus text exactly as the engine would send it and look for that
signature.

A build passes only if EVERY Jesus line it uses is Alexander. Stories with no Jesus
lines are "n/a" (judged only by the ElevenLabs check in qc_gate).

Writes media-production/JESUS-VOICE.json:
  {"<build#>": {"voice": "Alexander"|"Chris"|"unknown"|"n/a", "how": "...", "ok": bool}}

Usage:
  python3 admin/jesus_voice_audit.py            # every build
  python3 admin/jesus_voice_audit.py 94 95 171  # only these
  REFRESH=1 python3 admin/jesus_voice_audit.py  # re-fetch ElevenLabs history first
"""
import glob
import json
import os
import re
import subprocess
import sys
import urllib.request

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MP = os.path.join(REPO, "media-production")
HIST_CACHE = "/tmp/eleven_history.json"
OUT = os.path.join(MP, "JESUS-VOICE.json")
REQUIRED_JESUS = "Alexander"          # Cameron's locked pick (mbm_eleven VOICE_ELEVEN)

sys.path.insert(0, MP)
from corpus import canonical_builds, load_build_segments  # noqa: E402


def _key():
    raw = open(glob.glob(os.path.join(MP, "elevenlabs*KEY*.txt"))[0]).read()
    m = re.search(r"sk_[A-Za-z0-9]+", raw)
    return m.group(0) if m else raw.strip()


def fetch_history(pages=None):
    """Pull generation history. pages=1 grabs only the newest page — enough to see
    clips rendered seconds ago, which is what the redo loop needs after re-voicing
    (a full pull is ~10 pages and far too slow to run per build)."""
    hdr = {"xi-api-key": _key()}
    items, last, n = [], None, 0
    while True:
        u = "https://api.elevenlabs.io/v1/history?page_size=1000"
        if last:
            u += f"&start_after_history_item_id={last}"
        d = json.load(urllib.request.urlopen(urllib.request.Request(u, headers=hdr), timeout=60))
        its = d.get("history", [])
        items += [{"voice": (h.get("voice_name") or "").split(" -")[0].strip(),
                   "text": h.get("text", ""), "date": h.get("date_unix", 0)} for h in its]
        n += 1
        if not d.get("has_more") or not its or (pages and n >= pages):
            break
        last = its[-1]["history_item_id"]
    return items


def load_history():
    """REFRESH=1 -> full re-pull. REFRESH=new -> merge just the newest page into the
    cache (fast; use right after re-voicing so the fresh clips are visible)."""
    mode = os.environ.get("REFRESH", "")
    if mode == "new" and os.path.exists(HIST_CACHE):
        try:
            cached = json.load(open(HIST_CACHE))
        except Exception:
            cached = []
        merged = cached + fetch_history(pages=1)
        seen, out = set(), []
        for h in merged:                       # de-dupe on (text, date, voice)
            k = (h["text"], h["date"], h["voice"])
            if k not in seen:
                seen.add(k)
                out.append(h)
        json.dump(out, open(HIST_CACHE, "w"))
        return out
    if mode or not os.path.exists(HIST_CACHE):
        items = fetch_history()
        json.dump(items, open(HIST_CACHE, "w"))
        return items
    try:
        return json.load(open(HIST_CACHE))
    except Exception:
        items = fetch_history()
        json.dump(items, open(HIST_CACHE, "w"))
        return items


def norm(s):
    return re.sub(r"\s+", " ", re.sub(r"[^a-z ]", "", s.lower())).strip()


def build_dir(n):
    return canonical_builds(MP).get(n)


def segments(d):
    return load_build_segments(d, executable=sys.executable) or []


def audit(n, voice_of_text, spoken_fn, pause_fn):
    d = build_dir(n)
    if not d:
        return {"voice": None, "how": "no build dir", "ok": False}
    segs = segments(d)
    if not segs:
        return {"voice": None, "how": "no segments", "ok": False}
    jes = [s for s in segs if str(s[1]).lower() in ("jesus", "jes", "j")]
    if not jes:
        return {"voice": "n/a", "how": "story has no Jesus lines", "ok": True}

    found, missing = set(), []
    for sid, _sp, txt in jes:
        clip = os.path.join(d, "audio", f"{sid}.mp3")
        if not os.path.exists(clip):
            missing.append(sid)
            continue
        spoken = spoken_fn(txt)
        v = voice_of_text(norm(pause_fn(spoken)))     # Alexander pipeline (pause tags)
        if v is None:
            v = voice_of_text(norm(spoken))           # pre-Alexander pipeline
        found.add(v or "unknown")
    if missing:
        return {"voice": "incomplete", "how": f"missing Jesus clip(s): {', '.join(missing[:5])}", "ok": False}
    if found == {REQUIRED_JESUS}:
        return {"voice": REQUIRED_JESUS, "how": f"all {len(jes)} Jesus line(s) match Alexander in history", "ok": True}
    others = sorted(v for v in found if v != REQUIRED_JESUS)
    return {"voice": others[0] if others else "unknown",
            "how": f"Jesus lines voiced by {', '.join(sorted(found))} — not {REQUIRED_JESUS}", "ok": False}


def main():
    nums = [int(a) for a in sys.argv[1:] if a.isdigit()] or list(range(1, 201))
    hist = load_history()
    # newest generation of a given text wins (that is what a re-render leaves behind)
    best = {}
    for h in sorted(hist, key=lambda x: x["date"]):
        best[norm(h["text"])] = h["voice"]
    sys.stderr.write(f"[jesus-audit] history items: {len(hist)}\n")

    from mbm_eleven import eleven_spoken_text, jesus_pauses

    out = {}
    if os.path.exists(OUT):
        try:
            out = json.load(open(OUT))
        except Exception:
            out = {}
    ok = bad = 0
    for n in nums:
        res = audit(n, best.get, eleven_spoken_text, jesus_pauses)
        out[str(n)] = res
        ok += res["ok"]
        bad += (not res["ok"])
        if not res["ok"]:
            print(f"#{n:>3}: {res['voice']}  ({res['how']})", flush=True)
    tmp = OUT + ".tmp"
    json.dump(out, open(tmp, "w"), indent=1, sort_keys=True)
    os.replace(tmp, OUT)
    print(f"\nJesus voice audit: {ok} OK ({REQUIRED_JESUS} or no Jesus lines), {bad} NOT the approved voice.")
    print(f"-> {os.path.relpath(OUT, REPO)}")


if __name__ == "__main__":
    main()
