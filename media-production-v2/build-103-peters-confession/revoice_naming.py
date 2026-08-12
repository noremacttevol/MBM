#!/usr/bin/env python3
"""Row 103 NAMING re-voice (Cameron 2026-08-12): np/n5 said 'Simon Peter'/'Peter'
BEFORE Jesus renames him. Reworded to 'Simon'. Re-voice ONLY np + n5 through the
SAME ElevenLabs narrator (Brian) the rest of the row uses; edge-tts is banned.
Atempo-lock each new take to its ORIGINAL duration so NO beats window moves.
Everything else on disk is left byte-identical.
"""
import os
import subprocess
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "media-production")))
from mbm_eleven import render_segment  # noqa: E402
from mbm_speakers import NARRATOR      # noqa: E402

# id -> (new spoken text, locked original duration in seconds)
JOBS = {
    "np": ("And Simon answered him.", 1.671837),
    "n5": ("Not a prophet. Not a teacher. Simon said out loud the thing the "
           "others had only half-dared to hope.", 6.164898),
}


def dur(path):
    out = subprocess.check_output(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", path], text=True)
    return float(out.strip())


def main():
    key = None
    for seg, (text, target) in JOBS.items():
        raw = f"audio/{seg}.raw.mp3"
        final = f"audio/{seg}.mp3"
        print(f"[{seg}] rendering ElevenLabs Brian: {text!r}")
        render_segment(text, NARRATOR, raw, key=key)
        d0 = dur(raw)
        # atempo tempo factor to stretch/squeeze raw -> target duration (pitch preserved)
        factor = d0 / target
        print(f"[{seg}] raw={d0:.4f}s target={target:.4f}s atempo={factor:.5f}")
        subprocess.run(
            ["ffmpeg", "-y", "-v", "error", "-i", raw,
             "-af", f"atempo={factor:.6f}",
             "-c:a", "libmp3lame", "-b:a", "128k", "-ar", "44100", final],
            check=True)
        d1 = dur(final)
        print(f"[{seg}] LOCKED final={d1:.4f}s (target {target:.4f}s, drift {abs(d1-target)*1000:.1f}ms)")
        os.remove(raw)
        # render_segment wrote a .timing.json for the RAW; regenerate proportional caption
        # timing against the locked duration by scaling the raw timing by 1/factor.
        _rescale_timing(seg, factor)


def _rescale_timing(seg, factor):
    import json
    tj = f"audio/{seg}.timing.json"
    if not os.path.isfile(tj):
        return
    sents = json.load(open(tj))
    for s in sents:
        s["start"] = s["start"] / factor
        s["end"] = s["end"] / factor
    json.dump(sents, open(tj, "w"))


if __name__ == "__main__":
    main()
