#!/usr/bin/env python3
"""GREAT PLAN engine — one command per stage, per episode.

    python3 great-plan/gp/gp_engine.py audio    ep01
    python3 great-plan/gp/gp_engine.py wire     ep01
    python3 great-plan/gp/gp_engine.py check    ep01
    python3 great-plan/gp/gp_engine.py gen      ep01 --ceiling 8
    python3 great-plan/gp/gp_engine.py assemble ep01
    python3 great-plan/gp/gp_engine.py all      ep01 --ceiling 8

Every formula here is PORTED from the proven pipeline, never invented:
  * timeline arithmetic  = extract_beats.py (LEAD + trimmed-spoken + gap; card + TAIL)
  * Ken Burns chunks     = v2_assemble.build_chunk (same zoompan, fades, encoders)
  * captions             = the shared mbm_caption_timing.caption_filter, shifted
                           to global time exactly as v2_assemble does
  * closing card         = v2_assemble.build_card (same wrap law, all-I encode)
  * audio                = v2_assemble.rebuild_audio_from_segments (adelay+amix,
                           LUFS toward -15, limiter, bit-exact mux hash check)
  * images               = v2_gen_api.generate (same model, 2K, spend meter,
                           prepay-429 patience) with gp_prompt's era-aware blocks

Episode data lives in great-plan/episodes/epNN.py; build output in
great-plan/build-epNN-<slug>/.
"""
import argparse
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import tempfile
import textwrap

HERE = os.path.dirname(os.path.abspath(__file__))          # great-plan/gp
GPROOT = os.path.dirname(HERE)                             # great-plan
ROOT = os.path.dirname(GPROOT)                             # repo root
V2 = os.path.join(ROOT, "media-production-v2")
sys.path.insert(0, HERE)
sys.path.insert(1, V2)

import gp_prompt  # noqa: E402
from mbm_speakers import NARRATOR  # noqa: E402

FF = shutil.which("ffmpeg") or "ffmpeg"
FFPROBE = shutil.which("ffprobe") or "ffprobe"
FPS = 30
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
CREAM = "0xF7F2E9"
INK = "0x3B2A1E"
ENC = ["-c:v", "libx264", "-preset", "medium", "-crf", "16",
       "-pix_fmt", "yuv420p", "-r", str(FPS), "-an"]
CARD_ENC = ["-c:v", "libx264", "-preset", "medium", "-crf", "16",
            "-pix_fmt", "yuv420p", "-r", str(FPS), "-g", "1", "-bf", "0", "-an"]

LEAD, GAP, KJV_GAP, TAIL = 0.28, 0.72, 1.15, 1.5

# Great Plan recurring cast: lock token -> CAST-GP-REF/<stem>-{front,quarter}.jpeg
GP_CAST = {
    "FATHER": "father",
    "ADAM": "adam", "EVE": "eve", "MOSES-GP": "moses",
    "JOSEPH-SMITH": "joseph-smith", "MORONI-GP": "moroni",
    "JOSEPH-ADULT": "joseph-adult", "JOSEPH-1836": "joseph-adult",
    "ENOCH-GP": "enoch", "NOAH-GP": "noah", "ABRAHAM-GP": "abraham",
}
CAST_DIR = os.path.join(GPROOT, "CAST-GP-REF")


def run(cmd, **kw):
    print(">>", " ".join(str(c) for c in cmd)[:150], flush=True)
    subprocess.run(cmd, check=True, capture_output=True, **kw)


def dur_of(path):
    out = subprocess.run([FFPROBE, "-v", "error", "-show_entries",
                          "format=duration", "-of", "csv=p=0", path],
                         capture_output=True, text=True, check=True)
    return float(out.stdout.strip())


def spoken_of(path, tmpdir):
    tmp = os.path.join(tmpdir, "_spoken.wav")
    subprocess.run([FF, "-y", "-v", "error", "-i", path, "-af",
                    "areverse,silenceremove=start_periods=1:"
                    "start_threshold=-50dB:start_duration=0.02,areverse",
                    "-c:a", "pcm_s16le", tmp], check=True, capture_output=True)
    return dur_of(tmp)


def audio_stream_hash(path):
    probe = subprocess.run([FF, "-v", "error", "-i", path, "-map", "0:a:0",
                            "-c", "copy", "-f", "hash", "-hash", "sha256", "-"],
                           capture_output=True, text=True, check=True)
    return probe.stdout.strip()


def load_ep(name):
    path = os.path.join(GPROOT, "episodes", f"{name}.py")
    if not os.path.isfile(path):
        raise SystemExit(f"no episode module {path}")
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def build_dir(mod):
    d = os.path.join(GPROOT, f"build-ep{mod.NUM:02d}-{mod.SLUG}")
    os.makedirs(os.path.join(d, "audio"), exist_ok=True)
    os.makedirs(os.path.join(d, "assets"), exist_ok=True)
    os.makedirs(os.path.join(d, "segs"), exist_ok=True)
    return d


def out_name(mod):
    return f"the-great-plan-ep{mod.NUM:02d}_{mod.SLUG}.mp4"


# ------------------------------------------------------------------ audio ---
def stage_audio(mod, redo=False):
    from mbm_eleven import render_segment, eleven_spoken_text, _key
    d = build_dir(mod)
    key = _key()
    spoken_over = dict(getattr(mod, "SPOKEN", {}))
    todo = list(mod.SEGMENTS) + [mod.CARD_SEG]
    for seg_id, speaker, text in todo:
        out = os.path.join(d, "audio", f"{seg_id}.mp3")
        if not redo and os.path.isfile(out) and os.path.getsize(out) > 2000:
            continue
        spoken = eleven_spoken_text(text, spoken_over)
        sents = render_segment(spoken, speaker, out, key=key)
        print(f"  {seg_id:<6} {speaker:<9} {sents[-1]['end']:6.2f}s  {text[:70]}",
              flush=True)


# --------------------------------------------------------------- timeline ---
def timeline(mod):
    d = build_dir(mod)
    beats, t = [], 0.0
    with tempfile.TemporaryDirectory() as tmp:
        for seg_id, speaker, text in mod.SEGMENTS:
            mp3 = os.path.join(d, "audio", f"{seg_id}.mp3")
            if not os.path.isfile(mp3):
                raise SystemExit(f"missing audio {mp3} — run `audio` first")
            adur, sdur = dur_of(mp3), spoken_of(mp3, tmp)
            g = GAP if speaker == NARRATOR else KJV_GAP
            vdur = LEAD + sdur + g
            beats.append({"seg": seg_id, "speaker": speaker, "text": text,
                          "seg_start": round(t, 3),
                          "audio_start": round(t + LEAD, 3),
                          "spoken_end": round(t + LEAD + sdur, 3),
                          "seg_dur": round(vdur, 3)})
            t += vdur
        card_id, card_speaker, card_text = mod.CARD_SEG
        cmp3 = os.path.join(d, "audio", f"{card_id}.mp3")
        cdur = dur_of(cmp3)
        card = {"seg": card_id, "speaker": card_speaker, "text": card_text,
                "seg_start": round(t, 3), "audio_start": round(t + LEAD, 3),
                "seg_dur": round(LEAD + cdur + TAIL, 3)}
        total = round(t + LEAD + cdur + TAIL, 3)
    data = {"beats": beats, "card": card, "total": total}
    with open(os.path.join(d, "timeline.json"), "w") as f:
        json.dump(data, f, indent=1)
    return data


def resolve_anchor(anchor, data):
    if isinstance(anchor, (tuple, list)):
        seg_id, frac = anchor
    else:
        seg_id, frac = anchor, 0.0
    for b in data["beats"]:
        if b["seg"] == seg_id:
            return round(b["seg_start"] + frac * b["seg_dur"], 3)
    raise SystemExit(f"picture anchor {anchor!r}: no segment {seg_id!r}")


def picture_beats(mod, data):
    """PICTURES + timeline -> ordered beats with windows (start -> next start)."""
    out = []
    for pid, anchor, spec in mod.PICTURES:
        b = dict(spec)
        b["id"] = pid
        b["out"] = f"{pid}.jpeg"
        b["start"] = resolve_anchor(anchor, data)
        out.append(b)
    out.sort(key=lambda b: b["start"])
    card_start = data["card"]["seg_start"]
    for i, b in enumerate(out):
        b["end"] = out[i + 1]["start"] if i + 1 < len(out) else card_start
    if out[0]["start"] > 0.01:
        raise SystemExit(f"first picture starts at {out[0]['start']}s — must be 0")
    return out


def stage_wire(mod):
    data = timeline(mod)
    beats = picture_beats(mod, data)
    d = build_dir(mod)
    with open(os.path.join(d, "beats_gp.json"), "w") as f:
        json.dump([{k: v for k, v in b.items()} for b in beats], f, indent=1)
    print(f"{len(beats)} pictures over {data['total']:.1f}s "
          f"(card at {data['card']['seg_start']:.1f}s)")
    for b in beats:
        print(f"  {b['id']:<5} {b['start']:7.2f} -> {b['end']:7.2f}  "
              f"era={b.get('era', 'ancient')}"
              + ("  [JESUS ref]" if b.get("ref") else "")
              + ("  [devil]" if b.get("devil") else ""))
    return data, beats


# ------------------------------------------------------------------ check ---
def stage_check(mod):
    data = timeline(mod)
    beats = picture_beats(mod, data)
    mod.BEATS = beats  # gp_prompt.check reads .BEATS/.LOCKS
    fails, warns = gp_prompt.check(mod)
    dens = len(beats) / data["card"]["seg_start"] * 100
    if dens < 9:
        warns.append(f"picture density {dens:.1f}/100s is low (rubric ~15)")
    for w in warns:
        print(f"  WARN {w}")
    for x in fails:
        print(f"  FAIL {x}")
    if fails:
        raise SystemExit(f"{len(fails)} gate failure(s)")
    print(f"CHECK PASS — {len(beats)} beats, {dens:.1f} pics/100s, "
          f"{len(warns)} warning(s)")
    return data, beats


# -------------------------------------------------------------------- gen ---
def stage_gen(mod, ceiling, only=None, redo=False):
    import v2_gen_api as eng
    data = timeline(mod)
    beats = picture_beats(mod, data)
    d = build_dir(mod)
    assets = os.path.join(d, "assets")
    key = eng.load_key()
    face_b64 = eng.b64_file(os.path.join(ROOT, gp_prompt.JESUS_REF))

    refs_cache = {}
    for name, rel in (getattr(mod, "REFS", {}) or {}).items():
        paths = rel if isinstance(rel, (list, tuple)) else [rel]
        blobs = []
        for p in paths:
            full = p if os.path.isabs(p) else os.path.join(d, p)
            if os.path.isfile(full):
                blobs.append(eng.b64_file(full))
            else:
                print(f"  REF MISSING (skipped): {name} -> {p}")
        if blobs:
            refs_cache[name] = blobs

    made = 0
    for b in beats:
        if only and b["id"] not in only:
            continue
        dest = os.path.join(assets, b["out"])
        if not redo and os.path.isfile(dest) and os.path.getsize(dest) > 50000:
            continue
        if ceiling and eng.spent_so_far() + eng.COST_PER_IMAGE > ceiling:
            print(f"CEILING ${ceiling:.2f} reached — stopping cleanly.")
            break
        chars = []
        labels = []
        for tok in b.get("locks", []):
            if tok in refs_cache:
                chars += refs_cache[tok]
                labels.append(tok)
            elif tok in GP_CAST:
                stem = GP_CAST[tok]
                found = False
                for angle in ("front", "quarter"):
                    p = os.path.join(CAST_DIR, f"{stem}-{angle}.jpeg")
                    if os.path.isfile(p) and os.path.getsize(p) > 50000:
                        chars.append(eng.b64_file(p))
                        found = True
                if found:
                    labels.append(tok)
                else:
                    print(f"    WARNING: {tok} has no CAST-GP-REF sheet — "
                          f"renders text-only (face-board risk)")
        prompt = gp_prompt.assemble(b, mod.LOCKS)
        print(f"=== ep{mod.NUM:02d} {b['id']} -> {b['out']} ==="
              + ("  [JESUS ref]" if b.get("ref") else "")
              + (f"  [+refs {','.join(labels)}]" if labels else ""), flush=True)
        try:
            img = eng.generate(key, prompt,
                               face_b64 if b.get("ref") else None,
                               chars or None)
        except Exception as e:
            print(f"    FAILED: {e}", flush=True)
            continue
        with open(dest, "wb") as f:
            f.write(img)
        eng.record_spend(f"gp-ep{mod.NUM:02d}", b["id"], b["out"])
        made += 1
        print(f"    saved {b['out']} ({os.path.getsize(dest)//1024} KB)", flush=True)
    print(f"GEN DONE: {made} new picture(s); meter ${eng.spent_so_far():.2f}")


# --------------------------------------------------------------- assemble ---
def build_chunk(assets_dir, idx, src, dur, zdir, first, last, segs):
    frames = max(1, int(round(dur * FPS)))
    z = (f"1.001+0.10*on/{frames}" if zdir == "in"
         else f"1.101-0.10*on/{frames}")
    base = (f"[0:v]scale=2160:3868,setsar=1,"
            f"zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':"
            f"d={frames}:s=2160x3840:fps={FPS},"
            f"scale=1080:1920:flags=lanczos")
    tail = ""
    if first:
        tail = ",fade=t=in:st=0:d=1.2"
    if last and dur > 1.4:
        tail = f",fade=t=out:st={dur-1.2}:d=1.2"
    out = os.path.join(segs, f"c{idx:03d}.mp4")
    run([FF, "-y", "-loop", "1", "-i", os.path.join(assets_dir, src),
         "-t", f"{dur:.3f}", "-filter_complex", f"{base}{tail}[v]",
         "-map", "[v]"] + ENC + [out])
    return out


def build_card(segs, dur, text):
    size = 50
    lh = size + 22
    lines = [w for para in text.split("\n")
             for w in (textwrap.wrap(para, width=30) or [""])]
    L = len(lines)
    vf = ""
    for j, ln in enumerate(lines):
        if not ln.strip():
            continue
        tf = os.path.join(segs, f"card_{j}.txt")
        with open(tf, "w", encoding="utf-8") as f:
            f.write(ln)
        y = f"(h-{L * lh})/2+{j * lh}"
        vf += (f"drawtext=fontfile={SERIF}:textfile={tf}:fontsize={size}:"
               f"fontcolor={INK}:x=(w-text_w)/2:y={y},")
    vf += f"fade=t=in:st=0:d=0.8,fade=t=out:st={dur-0.8}:d=0.8"
    out = os.path.join(segs, "card.mp4")
    run([FF, "-y", "-f", "lavfi",
         "-i", f"color=c={CREAM}:s=1080x1920:r={FPS}:d={dur:.3f}",
         "-vf", vf] + CARD_ENC + [out])
    return out


def stage_assemble(mod):
    data = timeline(mod)
    beats = picture_beats(mod, data)
    d = build_dir(mod)
    assets, segs = "assets", "segs"
    for b in beats:
        p = os.path.join(d, assets, b["out"])
        if not os.path.isfile(p):
            raise SystemExit(f"missing picture: {p} — run `gen` first")

    prior = os.getcwd()
    os.chdir(d)
    try:
        # video chunks
        chunks = []
        card_start = data["card"]["seg_start"]
        for i, b in enumerate(beats):
            start = 0.0 if i == 0 else b["start"]
            end = beats[i + 1]["start"] if i + 1 < len(beats) else card_start
            dur = end - start
            if dur <= 0.05:
                continue
            chunks.append(build_chunk(assets, i, b["out"], dur,
                                      "in" if i % 2 == 0 else "out",
                                      first=(i == 0),
                                      last=(i + 1 == len(beats)), segs=segs))
        with open(os.path.join(segs, "concat_base.txt"), "w") as f:
            for c in chunks:
                f.write(f"file '{os.path.basename(c)}'\n")
        run([FF, "-y", "-f", "concat", "-safe", "0",
             "-i", os.path.join(segs, "concat_base.txt"),
             "-c", "copy", os.path.join(segs, "base.mp4")])

        # captions (shared caption_filter, shifted to global time)
        from mbm_caption_timing import caption_filter
        filters = []
        for s in data["beats"]:
            if not s["text"]:
                continue
            local_dur = s["seg_dur"]
            local_spoken_end = s["spoken_end"] - s["seg_start"]
            f = caption_filter(s["seg"], local_dur, local_spoken_end,
                               s["text"], s["speaker"])
            if not f:
                continue
            off = s["seg_start"]
            filters.append(f.replace("between(t,", f"between(t-{off:.3f},")
                           .lstrip(","))
        chain = "[0:v]" + ",".join(filters) + "[v]"
        run([FF, "-y", "-i", os.path.join(segs, "base.mp4"),
             "-filter_complex", chain, "-map", "[v]"] + ENC +
            [os.path.join(segs, "captioned.mp4")])

        # card + concat
        build_card(segs, data["card"]["seg_dur"], mod.CARD_TEXT)
        with open(os.path.join(segs, "concat.txt"), "w") as f:
            f.write("file 'captioned.mp4'\nfile 'card.mp4'\n")
        run([FF, "-y", "-f", "concat", "-safe", "0",
             "-i", os.path.join(segs, "concat.txt"),
             "-c", "copy", os.path.join(segs, "video_silent.mp4")])

        # audio: every segment + card at its computed offset
        total = data["total"]
        places = [(os.path.join("audio", f"{b['seg']}.mp3"), b["audio_start"])
                  for b in data["beats"]]
        places.append((os.path.join("audio", f"{data['card']['seg']}.mp3"),
                       data["card"]["audio_start"]))
        inputs, filters, labels = [], [], []
        for i, (path, start) in enumerate(places):
            inputs += ["-i", path]
            ms = int(start * 1000)
            filters.append(f"[{i}:a]aresample=44100,adelay={ms}|{ms},"
                           f"volume=1.0[a{i}]")
            labels.append(f"[a{i}]")
        filters.append("".join(labels) +
                       f"amix=inputs={len(labels)}:duration=longest:normalize=0,"
                       f"apad=whole_dur={total:.2f}[aout]")
        mix = os.path.join(segs, "audio_mix.m4a")
        run([FF, "-y"] + inputs + ["-filter_complex", ";".join(filters),
             "-map", "[aout]", "-t", f"{total:.2f}",
             "-c:a", "aac", "-b:a", "160k", mix])
        probe = subprocess.run([FF, "-i", mix, "-af", "ebur128", "-f", "null", "-"],
                               capture_output=True, text=True)
        lufs = None
        for line in probe.stderr.splitlines():
            line = line.strip()
            if line.startswith("I:") and "LUFS" in line:
                lufs = float(line.split()[1])
        gain = max(-6.0, min(16.0, -15.0 - lufs)) if lufs is not None else 0.0
        track = os.path.join(segs, "audio_final.m4a")
        run([FF, "-y", "-i", mix,
             "-af", f"volume={gain:.1f}dB,alimiter=limit=0.95",
             "-c:a", "aac", "-b:a", "128k", "-t", f"{total:.6f}", track])

        # final mux
        name = out_name(mod)
        dur = dur_of(track)
        vcap = max(300, int(24.5 * 8000 / dur) - 145)
        run([FF, "-y", "-i", os.path.join(segs, "video_silent.mp4"),
             "-i", track, "-map", "0:v:0", "-map", "1:a:0",
             "-c:v", "libx264", "-preset", "medium", "-crf", "19",
             "-maxrate", f"{vcap}k", "-bufsize", f"{2*vcap}k",
             "-pix_fmt", "yuv420p", "-r", str(FPS),
             "-c:a", "copy", "-movflags", "+faststart",
             "-t", f"{dur:.6f}", name])
        if audio_stream_hash(name) != audio_stream_hash(track):
            raise SystemExit("AUDIO MUX: track drifted during mux")
        size = os.path.getsize(name) / 1e6
        print(f"DONE {name}  {size:.1f} MB  {dur:.1f}s "
              f"({lufs} LUFS -> {gain:+.1f} dB)", flush=True)
    finally:
        os.chdir(prior)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("stage", choices=["audio", "wire", "check", "gen",
                                      "assemble", "all"])
    ap.add_argument("episode")
    ap.add_argument("--ceiling", type=float, default=None)
    ap.add_argument("--only", nargs="*", default=None)
    ap.add_argument("--redo", action="store_true")
    a = ap.parse_args()
    mod = load_ep(a.episode)
    if a.stage in ("gen", "all") and a.ceiling is None:
        raise SystemExit("gen requires --ceiling N (dollars)")
    if a.stage == "audio":
        stage_audio(mod, a.redo)
    elif a.stage == "wire":
        stage_wire(mod)
    elif a.stage == "check":
        stage_check(mod)
    elif a.stage == "gen":
        stage_gen(mod, a.ceiling, a.only, a.redo)
    elif a.stage == "assemble":
        stage_assemble(mod)
    elif a.stage == "all":
        stage_audio(mod)
        stage_check(mod)
        stage_gen(mod, a.ceiling)
        stage_assemble(mod)


if __name__ == "__main__":
    main()
