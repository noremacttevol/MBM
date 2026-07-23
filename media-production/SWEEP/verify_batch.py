#!/usr/bin/env python3
"""Load whisper ONCE, verify target words across many shipped mp4s (rule 2).
Edit JOBS below. Prints windows around each target word from the FINAL mp4 audio."""
import subprocess, tempfile, os
from faster_whisper import WhisperModel

import glob
def mp4(slug):
    hits=[f for f in glob.glob(slug+"/*.mp4")]
    return hits[0] if hits else slug+"/MISSING.mp4"
JOBS = [
    (mp4("build-63-man-born-blind"), ["siloam"]),
    (mp4("build-160-stone-cut"), ["chest"]),
    (mp4("build-11-storm"), ["carest"]),
    (mp4("build-115-ram-in-the-thicket"), ["fearest"]),
    (mp4("build-48-new-wine-old-bottles"), ["seweth"]),
    (mp4("build-20-samaritan"), ["spendest"]),
    (mp4("build-148-ruth-and-the-redeemer"), ["goest","lodgest"]),
]
m = WhisperModel("small", device="cpu", compute_type="int8")
for mp4, kws in JOBS:
    kws=[k.lower() for k in kws]
    if not os.path.exists(mp4):
        print(f"=== {mp4} MISSING ==="); continue
    wav=tempfile.mktemp(suffix=".wav")
    subprocess.run(["ffmpeg","-y","-i",mp4,"-vn","-ac","1","-ar","16000",wav],
                   stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,check=True)
    segs,_=m.transcribe(wav, word_timestamps=True, language="en")
    words=[w for s in segs for w in s.words]
    print(f"=== {os.path.basename(mp4)} ===")
    hit=False
    for i,w in enumerate(words):
        lw=w.word.lower().strip(" ,.!?;:\"'")
        if any(lw[:3]==k[:3] and abs(len(lw)-len(k))<=3 for k in kws) or any(k in lw for k in kws):
            ctx=" ".join(x.word.strip() for x in words[max(0,i-3):i+4])
            print(f"  {w.start:7.2f}  [{w.word.strip()}]  target={kws}  ...{ctx}...")
            hit=True
    if not hit: print(f"  (no window matched {kws})")
    os.remove(wav)
print("DONE")
