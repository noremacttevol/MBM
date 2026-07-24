import glob, subprocess, re, json, os
from mbm_eleven import render_segment, eleven_spoken_text, _key
SC="/tmp/claude-1000/-home-noremacttevol-Downloads/886fef41-1c13-47f7-b822-f0bde708cd1e/scratchpad/transcripts-live/media-production/TRANSCRIPTS"; BK="/tmp/claude-1000/-home-noremacttevol-Downloads/886fef41-1c13-47f7-b822-f0bde708cd1e/scratchpad/AUDIO-BACKUP"; KEY=_key(); BUDGET=24000
def rate(f):
    try: return int(subprocess.run(["ffprobe","-v","quiet","-select_streams","a:0","-show_entries","stream=sample_rate","-of","csv=p=0",f],capture_output=True,text=True).stdout.strip() or 0)
    except: return 0
rev=[]
for d in sorted(glob.glob("build-*/")):
    b=d.rstrip("/"); mp3s=glob.glob(f"{b}/audio/*.mp3")
    if mp3s and any(rate(f)==24000 for f in mp3s): rev.append(b)
numdir={int(re.match(r"build-(\d+)-",b).group(1)):b for b in rev}
jobs=[]
for tf in glob.glob(SC+"/*.json"):
    j=json.load(open(tf)); r=j["row"]
    if r in numdir:
        jobs.append((sum(len(s["text"]) for s in j["segments"]), numdir[r], j["segments"]))
jobs.sort()
used=0; done=[]
for c,build,segs in jobs:
    if used+c>BUDGET: print(f"DEFER {build}"); continue
    os.makedirs(f"{build}/audio",exist_ok=True)
    for f in glob.glob(f"{build}/audio/*"): os.remove(f)
    ok=all((render_segment(eleven_spoken_text(s["text"]),s["speaker"],f"{build}/audio/{s['id']}.mp3",key=KEY) or rate(f"{build}/audio/{s['id']}.mp3")==44100) for s in segs)
    if ok:
        used+=c; done.append(build)
        os.makedirs(f"{BK}/{build}",exist_ok=True); subprocess.run(["cp","-r",f"{build}/audio",f"{BK}/{build}/"])
        print(f"OK {build} ({c}, tot {used})", flush=True)
print(f"DONE revoiced={len(done)} used~{used}")
open("/tmp/revoiced.txt","w").write("\n".join(done))
