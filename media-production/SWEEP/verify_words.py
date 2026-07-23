#!/usr/bin/env python3
"""Transcribe a shipped mp4's audio and print windows around target words.
Usage: verify_words.py <mp4> <kw1> <kw2> ...
Used by the SWEEP to check REAL archaic-word defects in the FINAL mp4 (rule 2)."""
import sys, subprocess, tempfile, os
from faster_whisper import WhisperModel

mp4 = sys.argv[1]
kws = [k.lower() for k in sys.argv[2:]]
wav = tempfile.mktemp(suffix=".wav")
subprocess.run(["ffmpeg","-y","-i",mp4,"-vn","-ac","1","-ar","16000",wav],
               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
m = WhisperModel("small", device="cpu", compute_type="int8")
segs,_ = m.transcribe(wav, word_timestamps=True, language="en")
words=[w for s in segs for w in s.words]
print(f"=== {os.path.basename(mp4)} ===")
hit=False
for i,w in enumerate(words):
    lw=w.word.lower().strip(" ,.!?;:\"'")
    if any(k in lw or lw in k for k in kws) or any(abs(len(lw)-len(k))<=2 and lw[:3]==k[:3] for k in kws):
        ctx=" ".join(x.word.strip() for x in words[max(0,i-3):i+4])
        print(f"  {w.start:7.2f}  [{w.word.strip()}]  ...{ctx}...")
        hit=True
if not hit:
    print("  (no window matched — word may be dropped or heard very differently)")
os.remove(wav)
