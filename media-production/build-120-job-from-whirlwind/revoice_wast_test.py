#!/usr/bin/env python3
"""Row 120 audio C-FIX test — Cameron: jvA 'wast' reads like 'waste' (front /eɪ/,
measured F1=412 F2=2395). Correct archaic 'wast' is a BACK vowel /wʌst/~/wɒst/
(rhymes must/lost). Caption stays KJV 'wast'; only the SPOKEN token is respelled.
Render candidates to /tmp and formant-check the target word — pick the winner,
THEN install it (separate step). Same God voice (Bill) + settings as jv387/jvB.
"""
import os
import subprocess
import sys

import numpy as np

import glob
import re
# use the SHARED media-production modules, not the older local build-dir copies
_SHARED = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, _SHARED)
from mbm_eleven import render_segment  # noqa: E402
from mbm_speakers import GOD  # noqa: E402

_kf = glob.glob(os.path.join(_SHARED, "elevenlabs*KEY*.txt"))[0]
KEY = re.search(r"sk_[A-Za-z0-9]+", open(_kf).read()).group(0)

PHRASE = ("Where {W} thou when I laid the foundations of the earth? "
          "declare, if thou hast understanding.")
CANDS = {"wust": "wust", "wost": "wost", "wawst": "wawst"}


def formants(mp3, a=0.35, b=0.78):
    raw = subprocess.check_output(
        ["ffmpeg", "-nostdin", "-v", "error", "-ss", str(a), "-to", str(b),
         "-i", mp3, "-ac", "1", "-ar", "16000", "-f", "f32le", "-"])
    x = np.frombuffer(raw, dtype=np.float32)
    if len(x) < 200:
        return []
    seg = x[int(0.12 * len(x)):int(0.55 * len(x))]
    seg = seg * np.hamming(len(seg))
    order = 12
    r = np.correlate(seg, seg, "full")[len(seg) - 1:len(seg) - 1 + order + 1]
    R = np.array([[r[abs(i - j)] for j in range(order)] for i in range(order)])
    a_ = np.linalg.solve(R, r[1:order + 1])
    A = np.concatenate(([1], -a_))
    roots = [z for z in np.roots(A) if np.imag(z) >= 0.01]
    fs = 16000
    fr = sorted(np.arctan2(np.imag(z), np.real(z)) * fs / (2 * np.pi) for z in roots)
    return [round(f) for f in fr if 90 < f < 4000][:4]


if __name__ == "__main__":
    print("target: F2 must drop well below ~1600 (back vowel), not ~2395 (waste)")
    for tag, spell in CANDS.items():
        out = f"/tmp/r120/jvA_{tag}.mp3"
        render_segment(PHRASE.format(W=spell), GOD, out, key=KEY)
        d = float(subprocess.check_output(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "csv=p=0", out]).strip())
        # 'Where' ~0.0-0.42, target word starts ~0.42; scan a small window
        f = formants(out, 0.40, 0.82)
        print(f"[{tag:5}] dur={d:.3f}s  target-word formants={f}")
