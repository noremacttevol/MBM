#!/usr/bin/env python3
"""FREE recovery of ElevenLabs audio from account history — no credits spent.

Every clip ever generated is stored in the ElevenLabs history and re-downloads for
free. When the shared clone reverts a build's audio to the old edge-tts voice, we do
NOT re-voice (that bills again) — we pull the exact clip back down from history and
regenerate its timing.json locally. This is the fix for the credit waste: paid audio
is recovered, never re-bought.

Usage:
  python3 recover_from_history.py <transcripts_dir>            # recover all not-yet-44100 builds
  python3 recover_from_history.py <transcripts_dir> --all      # recover every build
"""
import glob, json, os, re, subprocess, sys
import requests
from mbm_eleven import eleven_spoken_text, SPEAKER_ALIAS

SC = sys.argv[1]
ALL = "--all" in sys.argv
KEY = re.search(r"sk_[A-Za-z0-9]+", open(glob.glob("elevenlabs*KEY*.txt")[0]).read()).group(0)
H = {"xi-api-key": KEY}
VN = {"narrator": "Brian", "jesus": "Chris", "god": "Bill", "scripture": "Roger", "woman": "Matilda"}
_SENT = re.compile(r"[^.!?]*[.!?]+|\S[^.!?]*$")

def norm(s): return re.sub(r"\s+", " ", re.sub(r"[^a-z ]", "", s.lower())).strip()
def rate(f):
    try: return int(subprocess.run(["ffprobe","-v","quiet","-select_streams","a:0","-show_entries","stream=sample_rate","-of","csv=p=0",f],capture_output=True,text=True).stdout.strip() or 0)
    except: return 0
def dur(f):
    try: return float(subprocess.run(["ffprobe","-v","quiet","-show_entries","format=duration","-of","csv=p=0",f],capture_output=True,text=True).stdout.strip() or 0)
    except: return 0.0

# history index: (voice, normalized text) -> newest history_id
hist = json.load(open("/tmp/eleven_history.json"))
idx = {}
for h in hist:
    v = h["voice"].split(" -")[0].strip()
    k = (v, norm(h["text"]))
    if k not in idx or h["date"] > idx[k][1]:
        idx[k] = (h["id"], h["date"])

def timing_for(text, mp3):
    d = dur(mp3); sents = [m.group(0).strip() for m in _SENT.finditer(text) if m.group(0).strip()]
    tot = sum(len(s) for s in sents) or 1; out=[]; t=0.0
    for s in sents:
        seg = d*len(s)/tot; out.append({"text":s,"start":round(t,3),"end":round(t+seg,3)}); t+=seg
    return out

def build_map():
    m={}
    for dd in glob.glob("build-*/"):
        mm=re.match(r"build-(\d+)-",dd)
        if mm: m[int(mm.group(1))]=dd.rstrip("/")
    return m
BUILDS=build_map()

def needs_recovery(build, segs):
    if ALL: return True
    for s in segs:
        f=f"{build}/audio/{s['id']}.mp3"
        if not os.path.exists(f) or rate(f)!=44100: return True
    return False

ok=miss=skip=0; missing=[]
for tf in sorted(glob.glob(f"{SC}/*.json")):
    j=json.load(open(tf)); build=BUILDS.get(j["row"]); segs=j["segments"]
    if not build: continue
    if not needs_recovery(build, segs): skip+=1; continue
    os.makedirs(f"{build}/audio", exist_ok=True)
    good=True
    for s in segs:
        sp=SPEAKER_ALIAS.get(s["speaker"], s["speaker"])
        hit=idx.get((VN[sp], norm(eleven_spoken_text(s["text"]))))
        if not hit: good=False; missing.append((build,s["id"])); continue
        out=f"{build}/audio/{s['id']}.mp3"
        a=requests.get(f"https://api.elevenlabs.io/v1/history/{hit[0]}/audio",headers=H)
        open(out,"wb").write(a.content)
        if rate(out)!=44100: good=False; continue
        json.dump(timing_for(eleven_spoken_text(s["text"]), out), open(f"{build}/audio/{s['id']}.timing.json","w"))
    if good:
        open(f"{build}/.audio-eleven-done","w").close(); ok+=1
        print(f"RECOVERED {build} ({len(segs)} clips, FREE)", flush=True)
    else:
        miss+=1; print(f"PARTIAL   {build}", flush=True)
print(f"\nrecovered={ok} partial={miss} already-good-skipped={skip} missing_segments={len(missing)}")
