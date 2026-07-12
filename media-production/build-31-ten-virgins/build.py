#!/usr/bin/env python3
"""Assemble Story Video #31 — The Ten Virgins (Matthew 25:1-13).
Phase-1 STILLS-ONLY + Face Law. Parable; bridegroom only distant/from-behind.
Windows build. Timeline computed from measured narration durations."""
import os, subprocess
FF = ("C:/Users/ellil/AppData/Local/Microsoft/WinGet/Packages/"
      "Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe/"
      "ffmpeg-8.1.2-full_build/bin/ffmpeg.exe")
A, S, FPS = "assets", "segs", 30
SERIF = "C\\:/Windows/Fonts/georgia.ttf"
SERIF_BI = "C\\:/Windows/Fonts/georgiai.ttf"
CREAM, INK = "0xF7F2E9", "0x3B2A1E"
ENC = ["-c:v","libx264","-preset","medium","-crf","16","-pix_fmt","yuv420p","-r",str(FPS),"-an"]

# (id, kind, src, dur, zoom_dir, caption, style)  style: "n" plain / "kjv" italic-cream / "close" card
SEGMENTS = [
    ("s1a","still","s1.jpeg",5.804,"in",
     "Jesus told a story of ten women\nwaiting for a wedding.","n"),
    ("s1b","still","s1.jpeg",9.984,"out",
     "A village would wait for the\nbridegroom to come and lead\nthem in to the feast.","n"),
    ("s1c","still","s1.jpeg",6.168,"in",
     "Ten young women took their\nlamps and went out to meet him.","n"),
    ("s2a","still","s2.jpeg",7.632,"in",
     "Five were wise — they carried\nextra oil in little jars.","n"),
    ("s2b","still","s2.jpeg",6.600,"out",
     "Five were foolish — they brought\nlamps, but no extra oil.","n"),
    ("s3","still","s3.jpeg",10.488,"in",
     "The bridegroom was delayed.\nHour by hour, all ten\ngrew drowsy and slept.","n"),
    ("s4a","still","s4.jpeg",7.752,"in",
     "At midnight a cry rang out:\n‘The bridegroom is coming!’","n"),
    ("s4b","still","s4.jpeg",7.920,"out",
     "They woke and trimmed their lamps.\nThe wise ones burned bright.","n"),
    ("s5a","still","s5.jpeg",7.488,"in",
     "But the foolish lamps\nwere sputtering out —\nthey had no oil left.","n"),
    ("s5b","still","s5.jpeg",4.992,"out",
     "‘Please,’ they cried,\n‘give us some of your oil!’","n"),
    ("s5c","still","s5.jpeg",7.704,"in",
     "‘There isn't enough for all,’\nthey said. ‘Go buy your own.’","n"),
    ("s6a","still","s6.jpeg",6.552,"in",
     "While they hurried off in the dark,\nthe bridegroom arrived.","n"),
    ("s6b","still","s6.jpeg",6.216,"out",
     "The ready went in to the feast —\nand the door was shut.","n"),
    ("s7a","still","s7.jpeg",10.944,"in",
     "The others returned, knocking:\n‘Open to us!’ But the answer came:\n‘I do not know you.’","n"),
    ("s7b","still","s7.jpeg",4.548,"out",
     "Then Jesus told them\nwhy he had shared this story.","n"),
    ("s4c","still","s4.jpeg",8.188,"in",
     "“Watch therefore, for ye know\nneither the day nor the hour\nwherein the Son of man cometh.”","kjv"),
    ("s2c","still","s2.jpeg",12.048,"out",
     "The oil is what you cannot borrow —\na heart truly ready,\na faith that is your own.","n"),
    ("s6c","still","s6.jpeg",9.512,"in",
     "But the door is still open now.\nTonight your lamp can be filled.\nHe is worth being ready for.","n"),
    ("card","card",None,7.400,None,
     "You cannot borrow\nsomeone else's oil.\n\n"
     "Is your own lamp burning —\nare you ready to meet him?","close"),
]

AUDIO = [
    ("audio/n0.mp3",   0.500),
    ("audio/n1.mp3",   5.804),
    ("audio/n2.mp3",  15.788),
    ("audio/n3.mp3",  21.956),
    ("audio/n4.mp3",  29.588),
    ("audio/n5.mp3",  36.188),
    ("audio/n6.mp3",  46.676),
    ("audio/n7.mp3",  54.428),
    ("audio/n8.mp3",  62.348),
    ("audio/n9.mp3",  69.836),
    ("audio/n10.mp3", 74.828),
    ("audio/n11.mp3", 82.532),
    ("audio/n12.mp3", 89.084),
    ("audio/n13.mp3", 95.300),
    ("audio/n14.mp3",106.244),
    ("audio/j1.mp3", 110.792),
    ("audio/n15.mp3",118.980),
    ("audio/n16.mp3",131.028),
    ("audio/card.mp3",140.540),
]

# gentle drones; go SILENT under j1 the KJV seal
BEDS = [
    (0.0,   109.5, "a"),
    (119.5, 148.0, "b"),
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
    OUT="matthew-25_ten-virgins.mp4"
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
