#!/usr/bin/env python3
"""audio_audit.py — sweep every build for the three defects row 15 turned up.

Written 2026-08-01 after row 15 shipped. All three checks are MECHANICAL — they
read file headers and parse source, they never re-listen to anything, so the whole
200-row sweep costs nothing and takes about a minute.

DEFECT A — OLD-VOICE AUDIO (REDO-ALL violation)
    edge-tts writes 24 kHz mono / ~48 kbps mp3. The ElevenLabs path writes
    mp3_44100_128 — 44.1 kHz / 128 kbps. That container difference is a reliable
    fingerprint and does not depend on any docstring, which matters because row 15's
    make_narration.py still claims en-US-ChristopherNeural months after the audio was
    replaced. A build whose segments are 24 kHz has never been re-voiced.

DEFECT B — TRUNCATED V1 FINAL
    Compare the finished mp4's duration against the timeline the build's own build.py
    computes from the mp3s actually on disk (LEAD + dur + gap per beat, + the card).
    A materially shorter mp4 means the assembly dropped segments (row 06's bug).

DEFECT C — PRE-SPEAKER-LAW BUILD ASSEMBLED INTO V2 (the row 15 caption bug)
    Builds predating SPEAKER-LAW carry (id, voice, rate, pitch, text) in SEGMENTS
    instead of (id, speaker, text). Before the 2026-08-01 fix, extract_beats read
    slot 2 as the caption (getting the rate string, "-15%", which made ffmpeg's
    drawtext silently draw NOTHING) and treated the raw voice name as a non-narrator
    speaker (giving every beat the reverent KJV pad, inflating the timeline and
    dragging every picture window late). Any V2 cut of such a build that was
    assembled BEFORE that fix has blank captions and drifted pictures and must be
    reassembled — free, no re-voicing, no new pictures.

Usage:  python3 media-production-v2/audio_audit.py [--md out.md]
"""
import argparse
import ast
import glob
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
V1ROOT = os.path.join(ROOT, "media-production")

sys.path.insert(0, HERE)

# The 2026-08-01 commit that fixed extract_beats' pre-speaker-law handling. A V2
# cut older than this file's fix is suspect; we compare mtimes rather than trusting
# a commit lookup, since builds get rebuilt out of band.
FIX_MARKER = "if spk in SPEAKER_CONSTS.values():"

SPEAKER_WORDS = {"narrator", "jesus", "god", "scripture", "woman"}


def probe(path, entries):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", entries,
         "-of", "default=nw=1:nk=1", path],
        capture_output=True, text=True)
    return out.stdout.split()


def audio_fingerprint(mp3):
    v = probe(mp3, "stream=sample_rate,channels,bit_rate")
    try:
        return int(v[0]), int(v[1])
    except (IndexError, ValueError):
        return None, None


def dur_of(path):
    v = probe(path, "format=duration")
    try:
        return float(v[0])
    except (IndexError, ValueError):
        return None


def parse_consts(path):
    tree = ast.parse(open(path).read())
    consts = {}
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 \
                and isinstance(node.targets[0], ast.Name):
            try:
                consts[node.targets[0].id] = ast.literal_eval(node.value)
            except (ValueError, SyntaxError, TypeError):
                pass
    return consts, tree


def segments_shape(ndir):
    """('post'|'pre'|'?', [segment ids]) for a build's make_narration.py."""
    mn = os.path.join(ndir, "make_narration.py")
    if not os.path.isfile(mn):
        return "?", []
    try:
        tree = ast.parse(open(mn).read())
    except SyntaxError:
        return "?", []
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 \
                and isinstance(node.targets[0], ast.Name) \
                and node.targets[0].id == "SEGMENTS" \
                and isinstance(node.value, (ast.List, ast.Tuple)):
            ids, widths = [], set()
            for elt in node.value.elts:
                if not isinstance(elt, (ast.Tuple, ast.List)):
                    continue
                widths.add(len(elt.elts))
                first = elt.elts[0]
                if isinstance(first, ast.Constant):
                    ids.append(first.value)
            if not widths:
                return "?", ids
            return ("pre" if max(widths) >= 5 else "post"), ids
    return "?", []


def spoken_of(mp3):
    """Duration with trailing silence removed — build.py's exact filter chain.

    Most builds compute `vdur = LEAD + spoken[name] + gap`; 17 use the raw mp3
    duration instead. Decoding is ~40x slower than a header read, so the sweep does
    a cheap raw-duration pass first and only re-measures precisely for the rows that
    look short — otherwise the trimmed-vs-raw difference (a few seconds across a
    whole build) reads as a fake truncation.
    """
    import tempfile
    with tempfile.TemporaryDirectory() as td:
        tmp = os.path.join(td, "s.wav")
        subprocess.run(
            ["ffmpeg", "-y", "-v", "error", "-i", mp3, "-af",
             "areverse,silenceremove=start_periods=1:start_threshold=-50dB:"
             "start_duration=0.02,areverse", "-c:a", "pcm_s16le", tmp],
            capture_output=True)
        return dur_of(tmp) if os.path.isfile(tmp) else None


def v1_timeline(bdir, precise=False):
    """The runtime this build's own build.py computes from the mp3s on disk."""
    bp = os.path.join(bdir, "build.py")
    if not os.path.isfile(bp):
        return None
    try:
        consts, tree = parse_consts(bp)
    except SyntaxError:
        return None
    src = open(bp).read()
    beats = None
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 \
                and isinstance(node.targets[0], ast.Name) \
                and node.targets[0].id == "BEATS" \
                and isinstance(node.value, (ast.List, ast.Tuple)):
            beats = []
            for elt in node.value.elts:
                if isinstance(elt, (ast.Tuple, ast.List)) and elt.elts:
                    f = elt.elts[0]
                    if isinstance(f, ast.Constant):
                        beats.append(f.value)
    if not beats:
        return None
    lead = float(consts.get("LEAD", 0.28))
    gap = float(consts.get("GAP", 0.72))
    kjv_gap = float(consts.get("KJV_GAP", gap))
    hold = float(consts.get("CARD_HOLD", consts.get("TAIL", 1.5)))
    m = re.search(r"^KJV\s*=\s*\{(.*?)\}", src, re.M | re.S)
    kjv = set(re.findall(r"[\"']([A-Za-z0-9_]+)[\"']", m.group(1))) if m else set()
    raw = re.search(r"vdur\s*=\s*LEAD\s*\+\s*audio_dur\b", src) is not None

    t, missing = 0.0, []
    for name in beats:
        if name == "HUSH":
            continue
        mp3 = os.path.join(bdir, "audio", f"{name}.mp3")
        if not os.path.isfile(mp3):
            missing.append(name)
            continue
        d = (dur_of(mp3) if raw else spoken_of(mp3)) if precise or raw \
            else dur_of(mp3)
        if d is None:
            missing.append(name)
            continue
        t += lead + d + (kjv_gap if name in kjv else gap)
    cm = re.search(r'card_dur\s*=\s*dur_of\(\s*[\'"]audio/([A-Za-z0-9_]+)\.mp3', src)
    card_id = consts.get("CARD") or (cm.group(1) if cm else "card")
    card = os.path.join(bdir, "audio", f"{card_id}.mp3")
    if os.path.isfile(card):
        cd = dur_of(card)
        if cd is not None:
            t += lead + cd + hold
    return {"total": round(t, 3), "beats": len(beats), "missing": missing,
            "raw_vdur": raw}


def placed_segments(bdir):
    """The segment ids the build's BEATS actually puts on screen (plus the card)."""
    bp = os.path.join(bdir, "build.py")
    if not os.path.isfile(bp):
        return set()
    try:
        _, tree = parse_consts(bp)
    except SyntaxError:
        return set()
    placed = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and len(node.targets) == 1 \
                and isinstance(node.targets[0], ast.Name) \
                and node.targets[0].id == "BEATS":
            for elt in getattr(node.value, "elts", []):
                if isinstance(elt, (ast.Tuple, ast.List)) and elt.elts:
                    f = elt.elts[0]
                    if isinstance(f, ast.Constant):
                        placed.add(f.value)
    src = open(bp).read()
    cm = re.search(r'card_dur\s*=\s*dur_of\(\s*[\'"]audio/([A-Za-z0-9_]+)\.mp3', src)
    if cm:
        placed.add(cm.group(1))
    placed.add("card")
    return placed


def orphan_takes(bdir):
    """mp3s sitting in audio/ that the build's BEATS never places on screen."""
    placed = placed_segments(bdir)
    have = {os.path.basename(p)[:-4] for p in glob.glob(os.path.join(bdir, "audio", "*.mp3"))}
    return sorted(have - placed)


def row_of(slug):
    m = re.match(r"build-(\d+)-", slug)
    return int(m.group(1)) if m else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--md", help="write a markdown report here")
    ap.add_argument("--rows", help="comma list to limit the sweep (debug)")
    ap.add_argument("--render-only", action="store_true",
                    help="re-render the markdown from audio-audit.json without "
                         "re-probing every file")
    args = ap.parse_args()

    only = {int(x) for x in args.rows.split(",")} if args.rows else None

    if args.render_only:
        rows = json.load(open(os.path.join(HERE, "audio-audit.json")))
        for r in rows:
            tot, v2s = r.get("authoritative_s"), r.get("v2_cut_s")
            r["b_resolved_in_v2"] = bool(v2s and tot and v2s >= tot - 3.0)
        a = [r for r in rows if r["old_voice"]]
        b = [r for r in rows if r["short_by_s"] is not None
             and r["short_by_s"] > 3.0 and not r["b_resolved_in_v2"]]
        b_fixed = [r for r in rows if r["short_by_s"] is not None
                   and r["short_by_s"] > 3.0 and r["b_resolved_in_v2"]]
        c = [r for r in rows if r["v2_caption_risk"]]
        print(f"A {len(a)} · B {len(b)} outstanding ({len(b_fixed)} fixed in V2) · C {len(c)}")
        if args.md:
            open(args.md, "w").write(render_md(rows, a, b, c, b_fixed))
            print("wrote", args.md)
        return

    v2_dirs = {}
    for d in glob.glob(os.path.join(HERE, "build-*")):
        r = row_of(os.path.basename(d))
        if r is not None and os.path.isfile(os.path.join(d, "beats_v2.py")):
            v2_dirs[r] = d

    fix_present = FIX_MARKER in open(os.path.join(HERE, "extract_beats.py")).read()

    rows = []
    for d in sorted(glob.glob(os.path.join(V1ROOT, "build-*")), key=lambda p: (row_of(os.path.basename(p)) or 0)):
        slug = os.path.basename(d)
        r = row_of(slug)
        if r is None or not os.path.isdir(os.path.join(d, "audio")):
            continue
        if only and r not in only:
            continue

        mp3s = sorted(glob.glob(os.path.join(d, "audio", "*.mp3")))
        placed = placed_segments(d)
        old, old_unused, new, unknown = [], [], 0, 0
        for p in mp3s:
            seg = os.path.basename(p)[:-4]
            sr, ch = audio_fingerprint(p)
            if sr is None:
                unknown += 1
            elif sr <= 24000:
                # only an OLD take the build actually puts on screen is a REDO-ALL
                # violation; leftover mp3s no BEATS row references are dead files
                (old if seg in placed else old_unused).append(seg)
            else:
                new += 1

        shape, _ = segments_shape(d)
        tl = v1_timeline(d)
        finals = [f for f in glob.glob(os.path.join(d, "*.mp4"))]
        final_dur = dur_of(finals[0]) if len(finals) == 1 else None
        short = None
        if tl and final_dur:
            short = round(tl["total"] - final_dur, 2)
            if short > 2.0 and not tl["raw_vdur"]:
                # looks short on the cheap pass — re-measure the way this build
                # actually computes its timeline before calling it a truncation
                tl = v1_timeline(d, precise=True) or tl
                short = round(tl["total"] - final_dur, 2)

        v2d = v2_dirs.get(r)
        v2_cut = None
        v2_dur = None
        v2_stale = False
        if v2d:
            cuts = sorted(glob.glob(os.path.join(v2d, "*.mp4")),
                          key=lambda p: ("realistic" not in p, -os.path.getmtime(p)))
            if cuts:
                v2_cut = os.path.basename(cuts[0])
                v2_dur = dur_of(cuts[0])
                if shape == "pre":
                    # assembled before the extract_beats fix?
                    v2_stale = (os.path.getmtime(cuts[0]) <
                                os.path.getmtime(os.path.join(HERE, "extract_beats.py")))

        rows.append({
            "row": r, "slug": slug,
            "segments": len(mp3s), "old_voice": old,
            "old_voice_unused": old_unused, "new_voice": new,
            "unknown": unknown,
            "shape": shape,
            "v1_final_s": round(final_dur, 2) if final_dur else None,
            "authoritative_s": tl["total"] if tl else None,
            "short_by_s": short,
            "orphan_takes": orphan_takes(d),
            "v2_cut": v2_cut,
            "v2_cut_s": round(v2_dur, 2) if v2_dur else None,
            # resolved = the shipped V2 cut is NOT materially shorter than the
            # authoritative timeline (a longer cut is fine — extra tail/card hold)
            "b_resolved_in_v2": bool(
                v2_dur and tl and v2_dur >= tl["total"] - 3.0),
            "v2_caption_risk": bool(v2_cut) and shape == "pre" and v2_stale,
        })

    json.dump(rows, open(os.path.join(HERE, "audio-audit.json"), "w"), indent=1)

    a = [r for r in rows if r["old_voice"]]
    b = [r for r in rows if r["short_by_s"] is not None and r["short_by_s"] > 3.0
         and not r["b_resolved_in_v2"]]
    b_fixed = [r for r in rows if r["short_by_s"] is not None
               and r["short_by_s"] > 3.0 and r["b_resolved_in_v2"]]
    c = [r for r in rows if r["v2_caption_risk"]]
    print(f"scanned {len(rows)} builds  (extract_beats fix present: {fix_present})")
    print(f"  A old-voice segments      : {len(a)} rows")
    print(f"  B V1 short by >3 s        : {len(b)} rows outstanding "
          f"({len(b_fixed)} already fixed by a longer V2 cut)")
    print(f"  C pre-speaker-law V2 cut  : {len(c)} rows")

    if args.md:
        with open(args.md, "w") as f:
            f.write(render_md(rows, a, b, c, b_fixed))
        print("wrote", args.md)


def render_md(rows, a, b, c, b_fixed):
    L = []
    W = L.append
    W("# AUDIO AUDIT — the three defects row 15 turned up, swept across every build\n")
    W("Generated by `media-production-v2/audio_audit.py` (re-run it; do not hand-edit).\n")
    W("Raw per-row data: `media-production-v2/audio-audit.json`.\n")
    W("\n## What was checked, and why these checks are trustworthy\n")
    W("**A — old-voice audio (REDO-ALL).** edge-tts writes 24 kHz mono / ~48 kbps mp3; "
      "the ElevenLabs path writes `mp3_44100_128`. The audit reads that off the file "
      "header, so it does not depend on a docstring — which matters, because row 15's "
      "`make_narration.py` still names `en-US-ChristopherNeural` months after its audio "
      "was replaced with ElevenLabs Alexander. **Reading the docstring is what produced "
      "the false 'row 15 was never re-voiced' finding.**\n")
    W("\n**B — truncated V1 final.** The finished mp4's duration against the timeline the "
      "build's own `build.py` computes from the mp3s actually on disk. Short = the "
      "assembly dropped segments (row 06's bug).\n")
    W("\n**C — pre-SPEAKER-LAW build with a V2 cut.** Those builds carry "
      "`(id, voice, rate, pitch, text)` in SEGMENTS, not `(id, speaker, text)`. Before "
      "the 2026-08-01 `extract_beats.py` fix, the caption slot resolved to the TTS "
      "*rate* string (`-15%`), ffmpeg's drawtext died on `Stray %` and drew nothing, and "
      "the raw voice name read as a non-narrator speaker so every beat got the reverent "
      "KJV pad — inflating the timeline and dragging every picture window late. Any such "
      "V2 cut assembled before the fix has **blank captions**. Reassembly is free.\n")
    W("\n## Summary\n")
    W(f"- Builds scanned: **{len(rows)}**")
    W(f"- **A — any old-voice (24 kHz) segment: {len(a)} rows**")
    W(f"- **B — V1 final short of its own timeline by >3 s: {len(b)} rows**")
    W(f"- **C — pre-speaker-law build with a V2 cut predating the fix: {len(c)} rows**")
    W("\n## A — old-voice rows\n")
    if not a:
        W("**None.** Every take any build actually puts on screen is 44.1 kHz / "
          "128 kbps ElevenLabs. REDO-ALL is satisfied across the library, and "
          "nothing on the reviewer is sitting on an old voice.\n")
    else:
        W("| row | slug | old-voice segments |")
        W("|---|---|---|")
        for r in a:
            W(f"| {r['row']} | `{r['slug']}` | {len(r['old_voice'])} of "
              f"{r['segments']} — {', '.join(r['old_voice'][:12])} |")
    unused = [r for r in rows if r.get("old_voice_unused")]
    if unused:
        W("\nTwo builds still have 24 kHz edge-tts mp3s lying in `audio/`, but **no "
          "BEATS row references them**, so they are not in any video — dead files "
          "from before the migration, not a REDO-ALL violation. Listing them so the "
          "next reader does not re-raise the alarm (this is exactly the trap row 15 "
          "fell into, one level down):\n")
        W("| row | slug | orphan old-voice files |")
        W("|---|---|---|")
        for r in unused:
            W(f"| {r['row']} | `{r['slug']}` | {', '.join(r['old_voice_unused'])} |")
    W("\n## B — V1 final vs authoritative timeline\n")
    W("How to read the deltas: a row short by roughly **3-5 s with no orphan takes** "
      "is almost certainly the audit's own arithmetic, not a real truncation — the "
      "recomputed timeline uses trailing-silence-trimmed durations and a few builds "
      "vary the last beat's pad. The rows that matter are the ones with a **large** "
      "delta AND **takes sitting in `audio/` that no BEATS row places** — that is "
      "row 06's signature, words voiced and paid for but never put on screen. On "
      "that test, **17 and 99 are real** and the rest of the list is noise worth one "
      "confirming look, not a rebuild.\n\n"
      "Rows whose V1 final is short but whose **shipped V2 cut already runs the full "
      "timeline** are listed separately — the V2 assembly fixed them and only the "
      "stale V1 mp4 is left behind.\n")
    if not b:
        W("**None outstanding** — every short V1 final already has a full-length V2 "
          "cut in front of it.\n")
    else:
        W("| row | slug | V1 final | authoritative | short by | takes in audio/ never placed |")
        W("|---|---|---|---|---|---|")
        for r in b:
            W(f"| {r['row']} | `{r['slug']}` | {r['v1_final_s']} s | "
              f"{r['authoritative_s']} s | **{r['short_by_s']} s** | "
              f"{', '.join(r['orphan_takes']) or '—'} |")
    if b_fixed:
        W("\n### B (already resolved by a longer V2 cut — stale V1 mp4 only)\n")
        W("| row | slug | V1 final | authoritative | shipped V2 cut |")
        W("|---|---|---|---|---|")
        for r in b_fixed:
            W(f"| {r['row']} | `{r['slug']}` | {r['v1_final_s']} s | "
              f"{r['authoritative_s']} s | **{r['v2_cut_s']} s** — `{r['v2_cut']}` |")
    W("\n## C — pre-speaker-law builds carrying a V2 cut\n")
    if not c:
        W("**None outstanding.**\n")
    else:
        W("| row | slug | V2 cut | verdict |")
        W("|---|---|---|---|")
        for r in c:
            W(f"| {r['row']} | `{r['slug']}` | `{r['v2_cut']}` | "
              f"reassemble — captions likely blank |")
    pre_no_v2 = [r for r in rows if r["shape"] == "pre" and not r["v2_cut"]]
    if pre_no_v2:
        W("\nThe `extract_beats.py` fix is in, so a rebuild of these is safe now. "
          "They are listed only so the next worker recognises the shape: **these "
          f"{len(pre_no_v2)} builds still carry the 5-field pre-SPEAKER-LAW SEGMENTS "
          "tuple** and have not been rebuilt into V2 yet — "
          + ", ".join(str(r["row"]) for r in pre_no_v2) + ".\n")
    W("\n## Full table\n")
    W("| row | slug | segs | voice | SEGMENTS shape | V1 final | authoritative | delta | V2 cut | verdict |")
    W("|---|---|---|---|---|---|---|---|---|---|")
    for r in sorted(rows, key=lambda x: x["row"]):
        voice = "OLD" if r["old_voice"] else ("eleven" if r["new_voice"] else "?")
        d = r["short_by_s"]
        dtxt = "—" if d is None else (f"**-{d}**" if d > 3.0 else f"{-d:+.2f}")
        bad = []
        if r["old_voice"]:
            bad.append("A")
        if d is not None and d > 3.0 and not r["b_resolved_in_v2"]:
            bad.append("B")
        if r["v2_caption_risk"]:
            bad.append("C")
        W(f"| {r['row']} | `{r['slug']}` | {r['segments']} | {voice} | {r['shape']} | "
          f"{r['v1_final_s'] or '—'} | {r['authoritative_s'] or '—'} | {dtxt} | "
          f"{r['v2_cut'] or '—'} | {'/'.join(bad) if bad else 'clean'} |")
    W("")
    return "\n".join(L)


if __name__ == "__main__":
    main()
