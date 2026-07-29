#!/usr/bin/env python3
"""Assemble Story Video #7 — Peter Walks on Water (Matthew 14:22-33, FULL).

Full law stack per PRODUCTION-BIBLE.md + PREFLIGHT.md. Phase-1 stills-only:
12 painted stills with Ken Burns drift, edge-tts narration, serif captions,
closing question card on cream #F7F2E9. Assembly Craft Laws: supersampled
zoompan (anti-shimmer), crf-16 intermediates, crf step-up final, loudness
toward -15 LUFS, detuned-pair music beds.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Converted from the old
template B: the 8-tuple SEGMENTS with hardcoded durations and a per-beat
`caption_style` is gone. Who is speaking is declared ONCE in make_narration.py and
decides BOTH the narration voice and the caption colour. Beat durations are derived
from the narration audio (LEAD + spoken + gap), never hand-set, and the video ends
TAIL seconds after the last spoken word.

j1, j2 and j3 are Jesus in the flesh and a red-letter KJV inks all three, so they
stay red. Three verbatim lines that were buried in narrator paraphrase are now
SCRIPTURE (blue): s28 (Matthew 14:28), s30 (14:30) and s33 (14:33).

FULL-STORY law: v22-23 (praying alone — the WHY), v26 ("It is a spirit"),
and v32-33 (wind ceasing + "Of a truth thou art the Son of God") restored.

The caption look, the Ken Burns maths, the audio mix, the loudness pass and the
size ladder are unchanged.

Output: 1080x1920 H.264 30fps, <25MB.
"""
import os
import textwrap
import shutil
import subprocess

import make_narration  # SEGMENTS -> verbatim caption text + speaker per segment
from mbm_caption_timing import caption_filter
from mbm_speakers import is_scripture

FF = shutil.which("ffmpeg") or "ffmpeg"
FPROBE = shutil.which("ffprobe") or "ffprobe"
A = "assets"
S = "segs"
FPS = 30
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_BI = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"  # same KJV font as build-123 (DejaVu italic doesn't exist on this box)
CREAM = "0xF7F2E9"
INK = "0x3B2A1E"

ENC = ["-c:v", "libx264", "-preset", "medium", "-crf", "16",
       "-pix_fmt", "yuv420p", "-r", str(FPS), "-an"]

# 2026-07-11 REDO (Machine C): pictures-only (no AI clips) + Jesus face NEVER shown,
# no glow, real Middle Eastern man from behind. All Jesus stills regenerated under
# The Standing Laws. The two former Veo clips (walking, sinking) are now stills.
S1 = "s1-mountain-prayer.jpeg"
S1B = "s1b-the-crowds-went-home.jpeg"  # coverage 2026-07-29: the emptying hillside (n0 first half)      # v3 face-shown: Jesus prays, face lifted, moonlit mountain
S2 = "s2-boat-storm.jpeg"
S2B = "s2b-the-fourth-watch.jpeg"     # coverage 2026-07-29: exhausted rowers, fourth watch (n1b)           # disciples' boat in the storm (boat/crew lock)
# v4 REROLLS (Machine C, 2026-07-17, Cameron's 3rd rejection): every sea still now
# shows feet ON the water surface (ON-THE-WATER law), the walk direction is locked by
# side-view geometry to match the narration, Peter is barefoot in every water shot for
# continuity, and the end card renders per-line (no tofu). Kept: s1, s2, s4, s10, s11, s12.
S3 = "s3-fix.jpeg"
S3B = "s3b-it-is-i.jpeg"             # coverage 2026-07-29: the faces as the voice reaches them (j1)                  # Jesus distant, ON the water (feet on surface, ripples)
S4 = "s4-over-gunwale.jpeg"
S4B = "s4b-bid-me-come.jpeg"         # coverage 2026-07-29: Peter calling back (n3)         # they cry "it is a spirit" — crew pointing (boat/crew lock)
WALK = "s5-fix.jpeg"               # side view: Peter walks left->right TOWARD Jesus, both on the water
S6 = "s6-fix.jpeg"                  # Peter doubts, barefoot, still on the surface
SINK = "s7-fix.jpeg"               # Peter sinking (only he is in the water); Jesus reaches, on the surface
S8 = "s8-fix.jpeg"
S8B = "s8b-the-grip.jpeg"            # coverage 2026-07-29: the immediate catch close (n6+n7)
S8C = "s8c-the-question.jpeg"        # coverage 2026-07-29: asked from the holding hand (j3+n8)                 # the catch: Peter lifted clear, Jesus on the surface, open sea (no shore)
S9 = "s9-fix.jpeg"                  # side view: both walk left->right back TOWARD the boat, on the water
S10 = "s10-calm-sea.jpeg"           # wide calm moonlit sea, the boat at rest (boat/crew lock)
S11 = "s11-worship.jpeg"
S11B = "s11b-soaked-and-shaking.jpeg" # coverage 2026-07-29: the soaked men kneeling (n10)            # v3 face-shown: Jesus among the kneeling, worshipping disciples
S12 = "s12-worship.jpeg"            # v3 face-shown: closing worship, Jesus at the boat's center

TEXT = {s[0]: s[2] for s in make_narration.SEGMENTS}
# SPEAKER-LAW: declared once in make_narration, so the caption colour
# and the narration voice can never drift apart.
SPEAKER = {s[0]: s[1] for s in make_narration.SEGMENTS}
# SPEAKER-LAW: declared once in make_narration, so the caption colour
# and the narration voice can never drift apart.
SPEAKER = {s[0]: s[1] for s in make_narration.SEGMENTS}

# BEATS: (segment_name, still, zoom_dir). Zoom alternates in/out on a shared still.
BEATS = [
    ("n0", S1B, "in"),
    ("n0b", S1, "in"),
    ("n1", S2, "in"),
    ("n1b", S2B, "in"),
    ("n2", S3, "in"),
    ("j1", S3B, "in"),
    ("n3", S4B, "in"),
    ("s28", S4, "out"),
    ("j2", S4, "in"),
    ("n4", S4, "out"),
    ("n4b", WALK, "in"),
    ("n5", S6, "in"),
    ("n5b", SINK, "out"),
    ("s30", SINK, "in"),
    ("n6", S8, "in"),
    ("n7", S8B, "out"),
    ("j3", S8C, "in"),
    ("n8", S8C, "out"),
    ("n9", S9, "in"),
    ("n9b", S10, "out"),
    ("n10", S11B, "in"),
    ("s33", S11, "out"),
    ("n10b", S12, "out"),
]

# The closing card is narrated but is not a beat — build_card places it itself.
CARD = "n11"
# PEAK: the beat the music bed dies for. j1 is Jesus's voice across the water.
PEAK = "j1"

LEAD = 0.28
GAP = 0.65
KJV_GAP = 1.60
# No-dead-air law: the video ends TAIL seconds after the last spoken
# word. Derived, never hand-set. Clears the card's 0.8s fade-out so
# the last word and the fade are never clipped.
TAIL = 1.5


def run(cmd):
    print(">>", " ".join(str(c) for c in cmd)[:160], flush=True)
    subprocess.run(cmd, check=True, capture_output=True)


def dur_of(path):
    out = subprocess.run(
        [FPROBE, "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", path], capture_output=True, text=True)
    return float(out.stdout.strip())


def spoken_of(path):
    tmp = f"{S}/_spoken.wav"
    run([FF, "-y", "-v", "error", "-i", path, "-af",
         "areverse,silenceremove=start_periods=1:start_threshold=-50dB:"
         "start_duration=0.02,areverse", "-c:a", "pcm_s16le", tmp])
    return dur_of(tmp)


def build_still(seg_id, src, dur, zdir, spoken_end, cap_text, speaker,
                first, last):
    frames = int(dur * FPS)
    if zdir == "in":
        z = f"1.001+0.10*on/{frames}"
    else:
        z = f"1.101-0.10*on/{frames}"
    base = (f"[0:v]scale=2160:3868,setsar=1,"
            f"zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':"
            f"d={frames}:s=2160x3840:fps={FPS},"
            f"scale=1080:1920:flags=lanczos")
    tail = ""
    if first:
        tail = ",fade=t=in:st=0:d=1.2"
    if last:
        tail = f",fade=t=out:st={dur-1.2}:d=1.2"
    capf = caption_filter(seg_id, dur, spoken_end, cap_text, speaker)
    fc = f"{base}{capf}{tail}[v]"
    run([FF, "-y", "-loop", "1", "-i", f"{A}/{src}", "-t", str(dur),
         "-filter_complex", fc, "-map", "[v]"] + ENC + [f"{S}/{seg_id}.mp4"])


# --- MBM box-guard: strip Unicode line/paragraph separators + control chars that
# drawtext renders as tofu boxes at line ends (Cameron complaint 2026-07-23). ---
_MBM_SEP = {0x2028:0x20,0x2029:0x20,0x0085:0x20,0x000b:0x20,0x000c:0x20,0x000d:0x20}
for _c in list(range(0x00,0x09))+list(range(0x0e,0x20))+list(range(0x7f,0xa0)):
    _MBM_SEP[_c]=None
def _mbm_clean(_t):
    return _t.translate(_MBM_SEP)


def build_card(seg_id, dur, text):
    # AUTO-WRAP CARD LAW (2026-07-21, Cameron): the closing-question card ran
    # off-frame in 16 builds because this function trusted whatever line breaks
    # the narration text happened to carry. It no longer trusts the text: every
    # paragraph is re-wrapped to fit 1080px, and each line gets its OWN textfile
    # + drawtext (a newline never enters a textfile — the tofu bug). Rewriting
    # narration/card text can never break the card again.
    size = 50
    lh = size + 22
    lines = [w for para in text.split("\n")
             for w in (textwrap.wrap(para, width=30) or [""])]
    L = len(lines)
    vf = ""
    for j, ln in enumerate(lines):
        if not ln.strip():
            continue                   # blank line = vertical gap only
        tf = f"{S}/{seg_id}_{j}.txt"
        with open(tf, "w", encoding="utf-8") as f:
            f.write(ln)
        y = f"(h-{L * lh})/2+{j * lh}"
        vf += (f"drawtext=fontfile={SERIF}:textfile={tf}:fontsize={size}:"
               f"fontcolor={INK}:x=(w-text_w)/2:y={y},")
    vf += f"fade=t=in:st=0:d=0.8,fade=t=out:st={dur-0.8}:d=0.8"
    run([FF, "-y", "-f", "lavfi",
         "-i", f"color=c={CREAM}:s=1080x1920:r={FPS}:d={dur}",
         "-vf", vf] + ENC + [f"{S}/{seg_id}.mp4"])


def bed_filter(idx, start, end, style):
    dur = end - start
    if dur <= 1.0:
        return None
    if style == "a":
        # HUM PURGE (Cameron, 2026-07-16): the sine 'music bed' reads as a background hum in every video — amplitudes zeroed. Do not restore; narration + silence only (PRODUCTION-BIBLE #5b 2026-07-16).
        src = ("aevalsrc='0*(sin(2*PI*110*t)+sin(2*PI*110.6*t))"
               "+0*(sin(2*PI*164.81*t)+sin(2*PI*165.5*t))"
               "+0*sin(2*PI*220*t)+0*sin(2*PI*329.63*t)'")
        eq = "lowpass=f=750,tremolo=f=0.13:d=0.3,aecho=0.7:0.4:311|429:0.25|0.18"
        fin, fout = 6, 5
    else:
        # HUM PURGE (Cameron, 2026-07-16): the sine 'music bed' reads as a background hum in every video — amplitudes zeroed. Do not restore; narration + silence only (PRODUCTION-BIBLE #5b 2026-07-16).
        src = ("aevalsrc='0*(sin(2*PI*110*t)+sin(2*PI*110.5*t))"
               "+0*(sin(2*PI*138.59*t)+sin(2*PI*139.2*t))"
               "+0*sin(2*PI*164.81*t)+0*sin(2*PI*220*t)'")
        eq = "lowpass=f=700,tremolo=f=0.11:d=0.3,aecho=0.7:0.4:317|443:0.25|0.18"
        fin, fout = 5, 6
    if dur < fin + fout + 2:
        fin = fout = max(2, int((dur - 2) / 2))
    ms = int(start * 1000)
    delay = f",adelay={ms}|{ms}" if ms else ""
    return (f"{src}:s=44100:d={dur},{eq},"
            f"afade=t=in:st=0:d={fin},afade=t=out:st={dur-fout}:d={fout}"
            f"{delay}[mus{idx}]")


def main():
    os.makedirs(S, exist_ok=True)

    spoken = {n: spoken_of(f"audio/{n}.mp3") for n, _, _ in BEATS}
    card_spoken = spoken_of(f"audio/{CARD}.mp3")

    timeline = []
    audio_place = []
    start_of = {}
    t = 0.0
    for name, still, zdir in BEATS:
        speaker = SPEAKER[name]
        gap = KJV_GAP if is_scripture(speaker) else GAP
        vdur = LEAD + spoken[name] + gap
        a_start = t + LEAD
        audio_place.append((f"audio/{name}.mp3", a_start))
        start_of[name] = a_start
        timeline.append((name, still, zdir, vdur, a_start, speaker))
        t += vdur
    card_vdur = LEAD + card_spoken + TAIL
    card_start = t
    audio_place.append((f"audio/{CARD}.mp3", card_start + LEAD))
    total = t + card_vdur

    worst, worst_at = 0.0, None
    prev_end = None
    for name, _s, _z, _v, a_start, _sp in timeline:
        if prev_end is not None and a_start - prev_end > worst:
            worst, worst_at = a_start - prev_end, name
        prev_end = a_start + spoken[name]
    print(f"total runtime: {total:.1f}s ({total/60:.2f} min)", flush=True)
    print(f"worst spoken gap: {worst:.2f}s before {worst_at} (must be <= 2.5s)", flush=True)
    if worst > 2.5:
        raise SystemExit(f"DEAD AIR: {worst:.2f}s gap before {worst_at} exceeds 2.5s")
    print(f"sacred silence: {PEAK} at {start_of[PEAK]:.1f}s", flush=True)

    n_beats = len(timeline)
    for i, (seg_id, still, zdir, vdur, _a, speaker) in enumerate(timeline):
        build_still(seg_id, still, vdur, zdir, LEAD + spoken[seg_id],
                    TEXT[seg_id], speaker, first=(i == 0),
                    last=(i == n_beats - 1))
    build_card(CARD, card_vdur, TEXT[CARD])

    with open(f"{S}/concat.txt", "w") as f:
        for seg_id, *_ in timeline:
            f.write(f"file '{seg_id}.mp4'\n")
        f.write(f"file '{CARD}.mp4'\n")
    run([FF, "-y", "-f", "concat", "-safe", "0", "-i", f"{S}/concat.txt",
         "-c", "copy", f"{S}/video_silent.mp4"])

    # ---- audio: narration at derived offsets + detuned-pair beds ----
    # The bed is fully out before the peak so the sacred line lands in
    # silence, then a quieter, warmer bed returns until the closing card.
    peak_end = start_of[PEAK] + spoken[PEAK]
    beds = [
        (0.0, start_of[PEAK] - 1.2, "a"),
        (peak_end + 1.0, card_start - 0.8, "b"),
    ]

    inputs = []
    filters = []
    labels = []
    for i, (path, start) in enumerate(audio_place):
        inputs += ["-i", path]
        ms = int(start * 1000)
        filters.append(f"[{i}:a]aresample=44100,adelay={ms}|{ms},volume=1.0[a{i}]")
        labels.append(f"[a{i}]")
    bi = 0
    for (bs, be, st) in beds:
        bf = bed_filter(bi, bs, be, st)
        if bf:
            filters.append(bf)
            labels.append(f"[mus{bi}]")
            bi += 1
    n = len(labels)
    filters.append("".join(labels) +
                   f"amix=inputs={n}:duration=longest:normalize=0,"
                   f"apad=whole_dur={total:.2f}[aout]")
    run([FF, "-y"] + inputs + ["-filter_complex", ";".join(filters),
         "-map", "[aout]", "-t", f"{total:.2f}", "-c:a", "aac", "-b:a", "160k",
         f"{S}/audio_mix.m4a"])

    # ---- loudness law: measure EBU R128, lift toward -15 LUFS ----
    probe = subprocess.run(
        [FF, "-i", f"{S}/audio_mix.m4a", "-af", "ebur128", "-f", "null", "-"],
        capture_output=True, text=True)
    lufs = None
    for line in probe.stderr.splitlines():
        line = line.strip()
        if line.startswith("I:") and "LUFS" in line:
            lufs = float(line.split()[1])
    gain = 0.0
    if lufs is not None:
        gain = max(-6.0, min(16.0, -15.0 - lufs))
    print(f"loudness: measured {lufs} LUFS, applying {gain:+.1f} dB", flush=True)

    # ---- final mux: runtime-computed rate cap, crf step-up ----
    vcap = max(300, int(24.5 * 8000 / total) - 145)
    size = 0.0
    crf = 21
    for crf in (21, 22, 23, 24, 25):
        run([FF, "-y", "-i", f"{S}/video_silent.mp4",
             "-i", f"{S}/audio_mix.m4a", "-map", "0:v", "-map", "1:a",
             "-c:v", "libx264", "-preset", "slow", "-crf", str(crf),
             "-maxrate", f"{vcap}k", "-bufsize", f"{vcap*2}k",
             "-pix_fmt", "yuv420p",
             "-af", f"volume={gain:.1f}dB,alimiter=limit=0.95",
             "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart",
             "matthew-14_peter-walks-on-water.mp4"])
        size = os.path.getsize("matthew-14_peter-walks-on-water.mp4") / 1e6
        if size <= 24.5:
            break
        print(f"  {size:.1f} MB at crf {crf} — over budget, stepping up",
              flush=True)
    print(f"DONE: matthew-14_peter-walks-on-water.mp4  {size:.1f} MB, {total:.1f}s "
          f"(crf {crf}, vcap {vcap}k)", flush=True)


if __name__ == "__main__":
    main()
