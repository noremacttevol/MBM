import shutil
#!/usr/bin/env python3
"""Assemble Story Video #34 — The Rich Fool (Luke 12:16-21).
Phase-1 STILLS-ONLY + Face Law. Parable (no Jesus figure). Windows build.
Timeline computed from measured narration durations."""
import os, subprocess
from mbm_caption_timing import caption_filter
FF = shutil.which("ffmpeg") or "ffmpeg"
A, S, FPS = "assets", "segs", 30
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_BI = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"
CREAM, INK = "0xF7F2E9", "0x3B2A1E"
ENC = ["-c:v","libx264","-preset","medium","-crf","16","-pix_fmt","yuv420p","-r",str(FPS),"-an"]

# (id, kind, src, dur, zoom_dir, caption, style)  style: "n" plain / "kjv" italic-cream / "close" card
SEGMENTS = [
    ("s1a","still","s1.jpeg",5.924,"in",
     "Jesus told a story of a rich man\nwho had a very good year.","n"),
    ("s1b","still","s1.jpeg",8.112,"out",
     "His fields gave an enormous harvest —\nmore than he'd ever gathered.","n"),
    ("s2","still","s2.jpeg",5.352,"in",
     "He had so much,\nhe ran out of room to store it.","n"),
    ("s3a","still","s3.jpeg",8.280,"in",
     "So he thought: I'll tear down\nmy barns and build bigger ones.","n"),
    ("s3b","still","s3.jpeg",4.656,"out",
     "There I'll store\nall my grain and goods.","n"),
    ("s4a","still","s4.jpeg",10.056,"in",
     "Then I'll tell myself: you've plenty\nfor years — relax, eat, drink, be merry.","n"),
    ("s4b","still","s4.jpeg",8.952,"out",
     "Every plan was about himself —\nhis barns, his goods, his comfort.","n"),
    ("s5a","still","s5.jpeg",6.876,"in",
     "But one thing he never planned for.\nThat night, God spoke to him.","n"),
    ("s5b","still","s5.jpeg",10.636,"in",
     "“Thou fool, this night thy soul\nshall be required of thee:\nthen whose shall those things be,\nwhich thou hast provided?”","kjv"),
    ("s6a","still","s6.jpeg",11.448,"in",
     "That night his life was over.\nAll he had piled up\nwould pass to someone else.","n"),
    ("s6b","still","s6.jpeg",8.304,"out",
     "He planned for everything\nbut the one thing certain:\nthat he would stand before God.","n"),
    ("s6c","still","s6.jpeg",4.428,"in",
     "And Jesus ended the story\nwith these words.","n"),
    ("s7a","still","s7.jpeg",7.492,"in",
     "“So is he that layeth up treasure\nfor himself, and is not rich\ntoward God.”","kjv"),
    ("s6d","still","s6.jpeg",9.480,"out",
     "His barns were full,\nbut his soul was empty.","n"),
    ("s7b","still","s7.jpeg",12.512,"out",
     "There's nothing wrong with a harvest.\nThe question is quieter:\nare you storing up only for yourself —\nor a life rich with God?","n"),
    ("card","card",None,9.000,None,
     "His barns were full.\nHis soul was empty.\n\n"
     "What are you storing up for yourself —\nand what are you storing up with God?","close"),
]

AUDIO = [
    ("audio/n0.mp3",   0.500),
    ("audio/n1.mp3",   5.924),
    ("audio/n2.mp3",  14.036),
    ("audio/n3.mp3",  19.388),
    ("audio/n4.mp3",  27.668),
    ("audio/n5.mp3",  32.324),
    ("audio/n6.mp3",  42.380),
    ("audio/n7.mp3",  51.332),
    ("audio/j1.mp3",  58.208),
    ("audio/n8.mp3",  68.844),
    ("audio/n9.mp3",  80.292),
    ("audio/n10.mp3", 88.596),
    ("audio/j2.mp3",  93.024),
    ("audio/n11.mp3",100.516),
    ("audio/n12.mp3",109.996),
    ("audio/card.mp3",122.508),
]

# gentle drones; go SILENT under both divine lines (j1 God's rebuke, j2 the seal)
BEDS = [
    (0.0,   57.5,  "a"),
    (69.5,  92.0,  "b"),
    (101.5, 131.6, "a"),
]

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print("FFMPEG ERROR:\n", r.stderr[-1600:], flush=True); raise SystemExit(1)

def caption_overlay(seg_id, dur, text, style):
    if not text: return None
    tf = f"{S}/{seg_id}.txt"
    with open(tf,"w",encoding="utf-8") as f: f.write(text)   # UTF-8 REQUIRED (curly quotes/em-dashes)
    font,size,color = (SERIF_BI,44,"0xFFF3DC") if style=="kjv" else (SERIF,40,"white")
    fo = max(0.0, dur-0.6)
    return (f"color=c=black@0.0:s=1080x1920:r={FPS}:d={dur},format=rgba,"
            f"drawtext=fontfile='{font}':textfile='{tf}':fontsize={size}:fontcolor={color}:"
            f"line_spacing=14:x=(w-text_w)/2:y=min(h-460\\,h-150-text_h):"
            f"shadowcolor=black@0.85:shadowx=2:shadowy=2:box=1:boxcolor=black@0.34:boxborderw=18,"
            f"fade=t=in:st=0:d=0.5:alpha=1,fade=t=out:st={fo}:d=0.5:alpha=1[cap]")

def assemble(seg_id, base, dur, cap, style, tail=""):
    # CAPTION LAW: Jost adaptive band drawn on the opaque still.
    if not cap:
        return f"{base}{tail}[v]"
    capf = caption_filter(seg_id, dur, dur, " ".join(cap.split()), style == "kjv")
    return f"{base}{capf}{tail}[v]"
def build_still(seg_id, src, dur, zdir, cap, style):
    frames = int(dur*FPS)
    z = f"1.001+0.09*on/{frames}" if zdir=="in" else f"1.091-0.09*on/{frames}"
    base = (f"[0:v]scale=2160:3840:force_original_aspect_ratio=increase,crop=2160:3840,setsar=1,"
            f"zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={frames}:s=2160x3840:fps={FPS},"
            f"scale=1080:1920:flags=lanczos")
    tail = ",fade=t=in:st=0:d=1.2" if seg_id=="s1a" else ""
    run([FF,"-y","-loop","1","-i",f"{A}/{src}","-t",str(dur),"-filter_complex",
         assemble(seg_id,base,dur,cap,style,tail),"-map","[v]"]+ENC+[f"{S}/{seg_id}.mp4"])

def build_card(seg_id, dur, text):
    tf=f"{S}/{seg_id}.txt"
    with open(tf,"w",encoding="utf-8") as f: f.write(text)
    vf=(f"drawtext=fontfile='{SERIF}':textfile='{tf}':fontsize=48:fontcolor={INK}:line_spacing=20:"
        f"x=(w-text_w)/2:y=(h-text_h)/2,fade=t=in:st=0:d=0.8,fade=t=out:st={dur-0.8}:d=0.8")
    run([FF,"-y","-f","lavfi","-i",f"color=c={CREAM}:s=1080x1920:r={FPS}:d={dur}","-vf",vf]+ENC+[f"{S}/{seg_id}.mp4"])

def bed_filter(idx, start, end, style):
    dur = end-start
    if style=="a":
        src=("aevalsrc='0*(sin(2*PI*110*t)+sin(2*PI*110.6*t))+0*(sin(2*PI*164.81*t)+sin(2*PI*165.5*t))+0*sin(2*PI*220*t)'")
        eq="lowpass=f=760,tremolo=f=0.12:d=0.3,aecho=0.7:0.4:311|429:0.24|0.17"; fin,fout=6,6
    else:
        # HUM PURGE (Cameron, 2026-07-16): the sine 'music bed' reads as a background hum in every video — amplitudes zeroed. Do not restore; narration + silence only (PRODUCTION-BIBLE #5b 2026-07-16).
        src=("aevalsrc='0*(sin(2*PI*110*t)+sin(2*PI*110.5*t))+0*(sin(2*PI*146.83*t)+sin(2*PI*147.5*t))+0*sin(2*PI*196*t)'")
        eq="lowpass=f=720,tremolo=f=0.10:d=0.3,aecho=0.7:0.4:317|443:0.24|0.17"; fin,fout=5,7
    if dur<fin+fout+2: fin=fout=max(2,int((dur-2)/2))
    ms=int(start*1000); delay=f",adelay={ms}|{ms}" if ms else ""
    return (f"{src}:s=44100:d={dur},{eq},afade=t=in:st=0:d={fin},afade=t=out:st={dur-fout}:d={fout}{delay}[mus{idx}]")

def main():
    os.makedirs(S,exist_ok=True)
    total=sum(s[3] for s in SEGMENTS); print("total runtime:",round(total,1),"s",flush=True)
    for sid,kind,src,dur,zdir,cap,style in SEGMENTS:
        (build_still(sid,src,dur,zdir,cap,style) if kind=="still" else build_card(sid,dur,cap))
    with open(f"{S}/concat.txt","w",encoding="utf-8") as f:
        for s in SEGMENTS: f.write(f"file '{s[0]}.mp4'\n")
    run([FF,"-y","-f","concat","-safe","0","-i",f"{S}/concat.txt","-c","copy",f"{S}/video_silent.mp4"])
    inputs,filters,labels=[],[],[]
    for i,(path,start) in enumerate(AUDIO):
        inputs+=["-i",path]; ms=int(start*1000)
        filters.append(f"[{i}:a]aresample=44100,adelay={ms}|{ms},volume=1.0[a{i}]"); labels.append(f"[a{i}]")
    for bi,(bs,be,st) in enumerate(BEDS):
        filters.append(bed_filter(bi,bs,be,st)); labels.append(f"[mus{bi}]")
    n=len(labels)
    filters.append("".join(labels)+f"amix=inputs={n}:duration=longest:normalize=0,apad=whole_dur={total}[aout]")
    run([FF,"-y"]+inputs+["-filter_complex",";".join(filters),"-map","[aout]","-t",str(total),
         "-c:a","aac","-b:a","160k",f"{S}/audio_mix.m4a"])
    probe=subprocess.run([FF,"-i",f"{S}/audio_mix.m4a","-af","ebur128","-f","null","-"],capture_output=True,text=True)
    lufs=None
    for line in probe.stderr.splitlines():
        line=line.strip()
        if line.startswith("I:") and "LUFS" in line:
            try: lufs=float(line.split()[1])
            except ValueError: pass
    gain=0.0 if lufs is None else max(-6.0,min(12.0,-15.0-lufs)); print("loudness",lufs,"gain",gain,flush=True)
    OUT="luke-12_rich-fool.mp4"
    vcap=max(300,int(24.5*8000/total)-145); size=0.0
    for crf in (20,21,22,23,24):
        run([FF,"-y","-i",f"{S}/video_silent.mp4","-i",f"{S}/audio_mix.m4a","-map","0:v","-map","1:a",
             "-c:v","libx264","-preset","medium","-crf",str(crf),"-maxrate",f"{vcap}k","-bufsize",f"{vcap*2}k",
             "-pix_fmt","yuv420p","-af",f"volume={gain:.1f}dB,alimiter=limit=0.95","-c:a","aac","-b:a","128k",
             "-movflags","+faststart",OUT])
        size=os.path.getsize(OUT)/1e6
        if size<=24.5: break
    print("DONE:",OUT,round(size,1),"MB",round(total,1),"s crf",crf,flush=True)

if __name__=="__main__": main()
