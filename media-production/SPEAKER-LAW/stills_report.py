#!/usr/bin/env python3
"""Compute how long each still is on screen after the speaker rebuild, and emit
STILLS-NEEDED entries for the ones now carrying too much.

Run inside a rebuilt build folder. Splitting a mixed segment and adding the
narrator's retelling keeps the same picture but multiplies the time it has to
hold, so this is where the art shortage is measured rather than guessed.
"""
import json
import os
import subprocess
import sys

LEAD, GAP, KJV_GAP = 0.28, 0.65, 1.60
HIGH, MED = 15.0, 10.0


def _dur(p):
    return float(subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", p], capture_output=True, text=True).stdout.strip())


def spoken_of(p):
    subprocess.run(
        ["ffmpeg", "-y", "-v", "error", "-i", p, "-af",
         "areverse,silenceremove=start_periods=1:start_threshold=-50dB:"
         "start_duration=0.02,areverse", "-c:a", "pcm_s16le", "/tmp/_sr.wav"],
        check=True)
    return _dur("/tmp/_sr.wav")


def report(build_dir, beats, speaker, text, reference, wants=None):
    """beats: [(seg_id, still_filename, zoom_dir)]"""
    os.chdir(build_dir)
    from mbm_speakers import is_scripture

    per_still, order = {}, []
    for seg, still, _z in beats:
        s = spoken_of(f"audio/{seg}.mp3")
        v = LEAD + s + (KJV_GAP if is_scripture(speaker[seg]) else GAP)
        if still not in per_still:
            per_still[still] = {"seconds": 0.0, "beats": []}
            order.append(still)
        per_still[still]["seconds"] += v
        per_still[still]["beats"].append(seg)

    wants = wants or {}
    entries = []
    for still in order:
        info = per_still[still]
        secs = round(info["seconds"], 1)
        if secs < MED:
            continue
        pri = "high" if secs >= HIGH else "medium"
        lead_beat = next((b for b in info["beats"] if speaker[b] != "narrator"),
                         info["beats"][0])
        entries.append({
            "build": os.path.basename(build_dir),
            "reference": reference,
            "priority": pri,
            "beat": lead_beat,
            "speaker": speaker[lead_beat],
            "caption_text": text[lead_beat][:160],
            "seconds_on_screen": secs,
            "beats_on_this_still": info["beats"],
            "current_still": still,
            "reason": (f"{len(info['beats'])} beats now sit on one still "
                       f"({secs}s); split + retelling multiplied the hold time"),
            "wants": wants.get(still, ""),
            "slug": "",
            "done": False,
        })
    return entries


def merge(entries, path):
    """Append/replace this build's entries in the shared JSON, atomically."""
    existing = []
    if os.path.exists(path):
        try:
            with open(path) as f:
                existing = json.load(f)
        except Exception:
            existing = []
    builds = {e["build"] for e in entries}
    existing = [e for e in existing if e["build"] not in builds]
    existing.extend(entries)
    existing.sort(key=lambda e: ({"high": 0, "medium": 1, "low": 2}[e["priority"]],
                                 -e["seconds_on_screen"]))
    tmp = path + ".tmp"
    with open(tmp, "w") as f:
        json.dump(existing, f, indent=1)
    os.replace(tmp, path)
    return len(existing)


if __name__ == "__main__":
    print(__doc__)
    print("import and call report()/merge() from a build's rebuild step.")
    sys.exit(0)
