#!/usr/bin/env python3
"""Row 120 audio C-FIX INSTALL — replace jvA.mp3 so God says 'wast' as /wʌst/
(rhymes 'must') instead of 'waste'. Caption stays KJV 'wast' (decoupled — only the
SPOKEN token is respelled 'wust'). Same God voice (Bill) + settings as jv387/jvB.

Procedure (row-103/189 sanctioned technique):
  1. back up jvA.mp3 + jvA.timing.json + jvA.mp3.words.json -> audio-oldvoice-backup/
  2. render N takes of the phrase; keep only takes whose 'wust' vowel formant-validates
     as a BACK vowel (F2 < 1600, not the 'waste' F2~2395)
  3. pick the valid take whose duration is CLOSEST to the original 6.765714 s
  4. atempo-lock it to EXACTLY the original duration (pitch preserved) so NO caption
     window moves and the assemble timeline is unchanged
  5. verify final: duration drift <1 frame, vowel still back, God-voice F0 ~ jv387
  6. leave timing.json + words.json unchanged (duration identical -> windows preserved)
"""
import glob
import os
import re
import shutil
import subprocess
import sys

import numpy as np

_SHARED = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, _SHARED)
from mbm_eleven import render_segment  # noqa: E402
from mbm_speakers import GOD  # noqa: E402

KEY = re.search(r"sk_[A-Za-z0-9]+",
                open(glob.glob(os.path.join(_SHARED, "elevenlabs*KEY*.txt"))[0]).read()).group(0)

HERE = os.path.dirname(os.path.abspath(__file__))
AUD = os.path.join(HERE, "audio")
JVA = os.path.join(AUD, "jvA.mp3")
TARGET = 6.765714  # original jvA duration — locked
PHRASE = ("Where wust thou when I laid the foundations of the earth? "
          "declare, if thou hast understanding.")


def dur(p):
    return float(subprocess.check_output(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", p]).strip())


def vowel_f(mp3, a=0.40, b=0.82):
    raw = subprocess.check_output(
        ["ffmpeg", "-nostdin", "-v", "error", "-ss", str(a), "-to", str(b),
         "-i", mp3, "-ac", "1", "-ar", "16000", "-f", "f32le", "-"])
    x = np.frombuffer(raw, dtype=np.float32)
    seg = x[int(0.12 * len(x)):int(0.55 * len(x))] * np.hamming(
        len(x[int(0.12 * len(x)):int(0.55 * len(x))]))
    order = 12
    r = np.correlate(seg, seg, "full")[len(seg) - 1:len(seg) - 1 + order + 1]
    R = np.array([[r[abs(i - j)] for j in range(order)] for i in range(order)])
    A = np.concatenate(([1], -np.linalg.solve(R, r[1:order + 1])))
    roots = [z for z in np.roots(A) if np.imag(z) >= 0.01]
    fr = sorted(np.arctan2(np.imag(z), np.real(z)) * 16000 / (2 * np.pi) for z in roots)
    return [round(f) for f in fr if 90 < f < 4000][:4]


def f0(mp3):
    raw = subprocess.check_output(
        ["ffmpeg", "-nostdin", "-v", "error", "-i", mp3, "-ac", "1",
         "-ar", "16000", "-f", "f32le", "-"])
    x = np.frombuffer(raw, dtype=np.float32)
    # crude autocorr F0 over voiced middle
    s = x[len(x) // 3: 2 * len(x) // 3]
    s = s - s.mean()
    if s.std() < 1e-4:
        return None
    ac = np.correlate(s, s, "full")[len(s) - 1:]
    lo, hi = 16000 // 200, 16000 // 80  # 80-200 Hz
    if hi >= len(ac):
        return None
    lag = lo + int(np.argmax(ac[lo:hi]))
    return round(16000 / lag, 1)


def main():
    bak = os.path.join(HERE, "audio-oldvoice-backup")
    os.makedirs(bak, exist_ok=True)
    for f in ("jvA.mp3", "jvA.timing.json", "jvA.mp3.words.json"):
        src = os.path.join(AUD, f)
        dst = os.path.join(bak, f)
        if os.path.isfile(src) and not os.path.isfile(dst):
            shutil.copy2(src, dst)
            print(f"backed up {f}")

    takes = []
    for i in range(4):
        raw = f"/tmp/r120/jvA_take{i}.mp3"
        render_segment(PHRASE, GOD, raw, key=KEY)
        d = dur(raw)
        fmt = vowel_f(raw)
        back = len(fmt) >= 2 and fmt[1] < 1600
        print(f"take{i}: dur={d:.3f}s vowel={fmt} back={back}")
        if back:
            takes.append((abs(d - TARGET), d, raw, fmt))
    if not takes:
        raise SystemExit("NO take produced a back vowel — do NOT install; park audio.")
    takes.sort()
    _, d0, raw, fmt = takes[0]
    factor = d0 / TARGET
    print(f"CHOSEN raw dur={d0:.3f}s vowel={fmt} atempo={factor:.5f}")
    if not (0.5 <= factor <= 2.0):
        raise SystemExit(f"atempo {factor} out of clean range — park audio.")

    subprocess.run(
        ["ffmpeg", "-y", "-v", "error", "-i", raw, "-af", f"atempo={factor:.6f}",
         "-c:a", "libmp3lame", "-b:a", "128k", "-ar", "44100", "-ac", "1", JVA],
        check=True)
    df = dur(JVA)
    print(f"INSTALLED jvA.mp3 dur={df:.4f}s (target {TARGET:.4f}, "
          f"drift {abs(df-TARGET)*1000:.1f} ms)")
    print(f"final vowel={vowel_f(JVA)}  final F0={f0(JVA)} Hz  "
          f"(jv387 F0={f0(os.path.join(AUD,'jv387.mp3'))} Hz, "
          f"jvB F0={f0(os.path.join(AUD,'jvB.mp3'))} Hz)")


if __name__ == "__main__":
    main()
