import shutil
#!/usr/bin/env python3
"""Assemble Story Video #37 — The Rich Man and Lazarus (Luke 16:19-31).
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
    ("b_n0","still","s1.jpeg",7.644,"in",
     "Jesus told of two men who lived\nside by side — yet worlds apart.","n"),
    ("b_n1","still","s1.jpeg",7.672,"out",
     "One was rich: dressed in purple and\nfine linen, every day a feast.","n"),
    ("b_n2","still","s2.jpeg",6.760,"in",
     "At his gate lay a poor beggar\nnamed Lazarus.","n"),
    ("b_n3","still","s2.jpeg",11.536,"out",
     "Covered in sores, longing for the\nscraps from the rich man's table —\neven the dogs licked his wounds.","n"),
    ("b_n4","still","s3.jpeg",9.328,"in",
     "The rich man passed that gate\nevery day, and did nothing.","n"),
    ("b_n5","still","s4.jpeg",11.848,"in",
     "Lazarus died — and the angels\ncarried him to Abraham's side,\ninto light and comfort at last.","n"),
    ("b_n6","still","s5.jpeg",10.648,"in",
     "The rich man died too, and woke\nin torment — a dark, thirsty place,\nfar from the light.","n"),
    ("b_n7","still","s5.jpeg",12.526,"out",
     "Far off he saw Abraham and Lazarus,\nand begged for one drop of water\nto cool his tongue.","n"),
    ("b_j1","still","s6.jpeg",13.246,"in",
     "“Son, remember that thou in thy lifetime\nreceivedst thy good things, and likewise\nLazarus evil things: but now he is\ncomforted, and thou art tormented.”","kjv"),
    ("b_n8","still","s6.jpeg",8.368,"out",
     "Between them a great gulf was fixed —\none no one could ever cross.","n"),
    ("b_n9","still","s7.jpeg",8.728,"in",
     "He begged again: send someone\nto warn my five brothers,\nso they never come here.","n"),
    ("b_n10","still","s7.jpeg",14.272,"out",
     "They have Moses and the prophets —\nlet them listen. But surely, he said,\none from the dead would make them turn.","n"),
    ("b_n11","still","s6.jpeg",3.502,"in",
     "And Abraham gave his final answer.","n"),
    ("b_j2","still","s6.jpeg",8.446,"out",
     "“If they hear not Moses and the prophets,\nneither will they be persuaded, though\none rose from the dead.”","kjv"),
    ("b_n12","still","s8.jpeg",10.144,"in",
     "A warning to all who have everything\nand walk past those who have nothing —\nbut underneath it, a mercy.","n"),
    ("b_n13","still","s8.jpeg",12.208,"out",
     "There is still a gate before you today.\nStill someone you walk past.\nStill time to stop, and see, and turn.","n"),
    ("card","card",None,9.224,None,
     "There is a gate before you today,\nand someone waiting at it.\n\n"
     "Who are you walking past —\nand will you stop while there is still time?","close"),
]

AUDIO = [
    ("audio/n0.mp3",   0.500),
    ("audio/n1.mp3",   7.644),
    ("audio/n2.mp3",  15.316),
    ("audio/n3.mp3",  22.076),
    ("audio/n4.mp3",  33.612),
    ("audio/n5.mp3",  42.940),
    ("audio/n6.mp3",  54.788),
    ("audio/n7.mp3",  65.436),
    ("audio/j1.mp3",  77.962),
    ("audio/n8.mp3",  91.208),
    ("audio/n9.mp3",  99.576),
    ("audio/n10.mp3",108.304),
    ("audio/n11.mp3",122.576),
    ("audio/j2.mp3", 126.078),
    ("audio/n12.mp3",134.524),
    ("audio/n13.mp3",144.668),
    ("audio/card.mp3",156.876),
]

# gentle drones; go SILENT under both KJV lines (j1 Abraham 16:25, j2 Abraham 16:31)
BEDS = [
    (0.0,   77.0,  "a"),
    (91.4, 125.6,  "b"),
    (134.7,166.1,  "a"),
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
    tail = ",fade=t=in:st=0:d=1.2" if seg_id=="b_n0" else ""
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
    OUT="luke-16_rich-man-lazarus.mp4"
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
