#!/usr/bin/env python3
"""Consolidate every plan's `stills_wanted` into the art session's work order.

Priority is measured, not asserted: how many seconds a still actually holds the
screen after the rebuild, computed from the rendered narration audio. A still
that used to carry one 6-second beat and now carries four is the worst viewer
experience in the library, and it sorts to the top.
"""
import glob
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
MP = os.path.dirname(HERE)
LEAD, GAP, KJV_GAP = 0.28, 0.65, 1.60
# Thresholds set by what a viewer actually feels, not by what is easy to flag.
# The stills were composed for a ~6s Ken Burns drift. Past ~25s the drift has run
# out and the picture visibly stalls; that is the tier worth spending art on.
# 16-25s is noticeable but survivable. Below 16s needs no new artwork at all.
HIGH, MED = 25.0, 16.0


def _dur(p):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                        "-of", "csv=p=0", p], capture_output=True, text=True)
    try:
        return float(r.stdout.strip())
    except ValueError:
        return None


def spoken_of(mp3):
    if not os.path.exists(mp3):
        return None
    tmp = "/tmp/_cs.wav"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", mp3, "-af",
                    "areverse,silenceremove=start_periods=1:start_threshold=-50dB:"
                    "start_duration=0.02,areverse", "-c:a", "pcm_s16le", tmp],
                   capture_output=True)
    return _dur(tmp)


def main():
    entries = []
    for p in sorted(glob.glob(os.path.join(HERE, "plans", "*.json"))):
        plan = json.load(open(p))
        build = plan["build"]
        d = os.path.join(MP, build)
        wanted = plan.get("stills_wanted") or {}
        spk = {s["id"]: s["speaker"] for s in plan["segments"]}
        txt = {s["id"]: s.get("text", "") for s in plan["segments"]}
        vrs = {s["id"]: s.get("verse", "") for s in plan["segments"]}

        # seconds each still actually holds, from the rendered audio
        per, order = {}, []
        for beat in plan.get("beats", []):
            sid, still = beat[0], beat[1]
            s = spoken_of(os.path.join(d, "audio", f"{sid}.mp3"))
            if s is None:
                continue
            v = LEAD + s + (KJV_GAP if spk.get(sid) != "narrator" else GAP)
            if still not in per:
                per[still] = {"secs": 0.0, "beats": []}
                order.append(still)
            per[still]["secs"] += v
            per[still]["beats"].append(sid)

        for still in order:
            info = per[still]
            secs = round(info["secs"], 1)
            want = wanted.get(still, "")
            if secs < MED:
                continue          # under 16s the existing art still carries it
            pri = "high" if secs >= HIGH else "medium"
            lead = next((b for b in info["beats"] if spk.get(b) != "narrator"),
                        info["beats"][0])
            entries.append({
                "build": build,
                "reference": plan.get("reference", ""),
                "priority": pri,
                "beat": lead,
                "speaker": spk.get(lead, "narrator"),
                "verse": vrs.get(lead, ""),
                "caption_text": txt.get(lead, "")[:180],
                "seconds_on_screen": secs,
                "beats_on_this_still": info["beats"],
                "current_still": still,
                "reason": (f"{len(info['beats'])} beats now sit on this still "
                           f"({secs}s); splitting verses and adding the narrator's "
                           f"retelling multiplied the hold time"),
                "wants": want,
                "slug": "",
                "done": False,
            })

    entries.sort(key=lambda e: ({"high": 0, "medium": 1, "low": 2}[e["priority"]],
                                -e["seconds_on_screen"]))
    dest = os.path.join(HERE, "stills-needed.json")
    tmp = dest + ".tmp"
    with open(tmp, "w") as f:
        json.dump(entries, f, indent=1, ensure_ascii=False)
    os.replace(tmp, dest)

    from collections import Counter
    c = Counter(e["priority"] for e in entries)
    with_brief = sum(1 for e in entries if e["wants"])
    print(f"{len(entries)} stills flagged across "
          f"{len({e['build'] for e in entries})} builds")
    print(f"  priority: {dict(c)}")
    print(f"  with an art brief written: {with_brief}")
    print(f"  worst holds:")
    for e in entries[:10]:
        print(f"    {e['seconds_on_screen']:6.1f}s  {e['build'][:34]:34s} "
              f"{e['current_still']}")


if __name__ == "__main__":
    main()
