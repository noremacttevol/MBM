#!/usr/bin/env python3
"""Assemble Story Video #22 — The Unmerciful Servant (Matthew 18:21-35).
Phase-1 STILLS-ONLY + Face Law. Parable (Jesus only in s1, from behind).
Windows build. Timeline computed from measured narration durations."""
import os, subprocess
FF = "ffmpeg"
A, S, FPS = "assets", "segs", 30
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_BI = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"
CREAM, INK = "0xF7F2E9", "0x3B2A1E"
ENC = ["-c:v","libx264","-preset","medium","-crf","16","-pix_fmt","yuv420p","-r",str(FPS),"-an"]

# (id, kind, src, dur, zoom_dir, caption, style)  style: "n" plain / "kjv" italic-cream / "close" card
SEGMENTS = [
    ("s1a","still","s1.jpeg",11.37,"in",
     "Peter came to Jesus with a\nquestion about forgiveness.","n"),
    ("s1b","still","s1.jpeg",12.81,"out",
     "How many times must I forgive\nmy brother — seven times?","n"),
    ("s1c","still","s1.jpeg",8.43,"in",
     "“I say not, Until seven times:\nbut, Until seventy times seven.”","kjv"),
    ("s1d","still","s1.jpeg",10.75,"out",
     "In other words — stop counting.\nThen Jesus told them a story.","n"),
    ("s2a","still","s2.jpeg",9.36,"in",
     "A king began to settle\naccounts with his servants.","n"),
    ("s2b","still","s2.jpeg",16.56,"out",
     "One man owed him ten thousand\ntalents — a debt he could\nnever hope to repay.","n"),
    ("s3a","still","s3.jpeg",12.02,"in",
     "He had nothing to pay. The king\nordered all he owned be sold\nto cover it.","n"),
    ("s3b","still","s3.jpeg",10.45,"out",
     "The servant fell down and begged:\n‘Be patient — I will pay it all!’","n"),
    ("s4a","still","s4.jpeg",9.50,"in",
     "The king looked at him —\nand his heart broke\nwith compassion.","n"),
    ("s4b","still","s4.jpeg",12.60,"out",
     "He cancelled the whole debt.\nEvery coin — forgiven, gone.\nThe man walked out free.","n"),
    ("s5a","still","s5.jpeg",17.49,"in",
     "But that servant found a man\nwho owed him a hundred coins —\na tiny debt beside his own.","n"),
    ("s5b","still","s5.jpeg",8.31,"out",
     "He grabbed him by the throat:\n‘Pay me what you owe me!’","n"),
    ("s6a","still","s6.jpeg",13.15,"in",
     "The man fell down and begged\nwith the very same words\nhe himself had used.","n"),
    ("s6b","still","s6.jpeg",8.44,"out",
     "But he refused — and had him\nthrown into prison.","n"),
    ("s7","still","s7.jpeg",9.12,"in",
     "The other servants saw it,\ngrieved, and told the king\neverything.","n"),
    ("s8a","still","s8.jpeg",14.23,"in",
     "‘You wicked servant! I forgave\nyou everything. Should you not\nhave shown the same mercy?’","n"),
    ("s8b","still","s8.jpeg",11.85,"out",
     "In anger the king handed him\nover to be punished\nuntil all was paid.","n"),
    ("s8c","still","s8.jpeg",11.05,"in",
     "“So likewise shall my Father do\nunto you, if ye forgive not\nyour brother from your hearts.”","kjv"),
    ("s4c","still","s4.jpeg",13.10,"out",
     "Look at the two debts side by side —\nthe mountain we were forgiven,\nthe handful we forgive each other.","n"),
    ("s5c","still","s5.jpeg",14.10,"in",
     "To be given an ocean of mercy —\nthen choke a man over a cup of it.\nThat he cannot bear.","n"),
    ("card","card",None,10.20,None,
     "You were forgiven a debt\nyou could never repay.\n\n"
     "Who is holding a small one\nagainst you — that you could\nlet go of today?","close"),
]

AUDIO = [
    ("audio/n0.mp3",   0.500),
    ("audio/n1.mp3",  11.372),
    ("audio/j1.mp3",  24.180),
    ("audio/n2.mp3",  32.608),
    ("audio/n3.mp3",  43.360),
    ("audio/n4.mp3",  52.720),
    ("audio/n5.mp3",  69.280),
    ("audio/n6.mp3",  81.304),
    ("audio/n7.mp3",  91.748),
    ("audio/n8.mp3", 101.248),
    ("audio/n9.mp3", 113.852),
    ("audio/n10.mp3",131.344),
    ("audio/n11.mp3",139.648),
    ("audio/n12.mp3",152.796),
    ("audio/n13.mp3",161.244),
    ("audio/n14.mp3",170.364),
    ("audio/n15.mp3",184.592),
    ("audio/j2.mp3", 196.440),
    ("audio/n16.mp3",207.488),
    ("audio/n17.mp3",220.592),
    ("audio/card.mp3",234.688),
]

# gentle drones; go SILENT under the king's compassion (s4) and under j2 the seal
BEDS = [
    (0.0,    90.5,  "a"),
    (114.5,  195.5, "b"),
    (208.0,  245.0, "a"),
]

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print("FFMPEG ERROR:\n", r.stderr[-1600:], flush=True); raise SystemExit(1)

def caption_overlay(seg_id, dur, text, style):
    if not text: return None
    tf = f"{S}/{seg_id}.txt"
    with open(tf,"w",encoding="utf-8") as f: f.write(text)   # UTF-8 REQUIRED (curly quotes/em-dashes)
    font,size,color = (SERIF_BI,46,"0xFFF3DC") if style=="kjv" else (SERIF,40,"white")
    fo = max(0.0, dur-0.6)
    return (f"color=c=black@0.0:s=1080x1920:r={FPS}:d={dur},format=rgba,"
            f"drawtext=fontfile='{font}':textfile='{tf}':fontsize={size}:fontcolor={color}:"
            f"line_spacing=14:x=(w-text_w)/2:y=min(h-460\\,h-150-text_h):"
            f"shadowcolor=black@0.85:shadowx=2:shadowy=2:box=1:boxcolor=black@0.34:boxborderw=18,"
            f"fade=t=in:st=0:d=0.5:alpha=1,fade=t=out:st={fo}:d=0.5:alpha=1[cap]")

def assemble(seg_id, base, dur, cap, style, tail=""):
    capf = caption_overlay(seg_id, dur, cap, style)
    return f"{base}[base];{capf};[base][cap]overlay=format=auto{tail}[v]" if capf else f"{base}{tail}[v]"

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
        src=("aevalsrc='0.020*(sin(2*PI*110*t)+sin(2*PI*110.6*t))+0.015*(sin(2*PI*164.81*t)+sin(2*PI*165.5*t))+0.010*sin(2*PI*220*t)'")
        eq="lowpass=f=760,tremolo=f=0.12:d=0.3,aecho=0.7:0.4:311|429:0.24|0.17"; fin,fout=6,6
    else:
        src=("aevalsrc='0.014*(sin(2*PI*110*t)+sin(2*PI*110.5*t))+0.011*(sin(2*PI*146.83*t)+sin(2*PI*147.5*t))+0.009*sin(2*PI*196*t)'")
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
    OUT="matthew-18_unmerciful-servant.mp4"
    vcap=max(300,int(24.5*8000/total)-145); size=0.0
    for crf in (21,22,23,24,25):
        run([FF,"-y","-i",f"{S}/video_silent.mp4","-i",f"{S}/audio_mix.m4a","-map","0:v","-map","1:a",
             "-c:v","libx264","-preset","medium","-crf",str(crf),"-maxrate",f"{vcap}k","-bufsize",f"{vcap*2}k",
             "-pix_fmt","yuv420p","-af",f"volume={gain:.1f}dB,alimiter=limit=0.95","-c:a","aac","-b:a","128k",
             "-movflags","+faststart",OUT])
        size=os.path.getsize(OUT)/1e6
        if size<=24.5: break
    print("DONE:",OUT,round(size,1),"MB",round(total,1),"s crf",crf,flush=True)

if __name__=="__main__": main()
