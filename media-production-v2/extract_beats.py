#!/usr/bin/env python3
"""extract_beats.py — V2 step B: pull the beat truth out of a V1 build, read-only.

V2-KICKOFF step B. For a given row, this reads the CANONICAL V1 build folder and
reproduces exactly the timeline arithmetic that build's own build.py performs, so
every V2 picture can be hung on the same audio windows the finished V1 video uses.

WHY IT PARSES INSTEAD OF IMPORTS
--------------------------------
V1 is read-only (V2-KICKOFF hard protection #1). Importing a build's build.py would
be tempting — it exposes BEATS and the constants directly — but its `spoken_of()`
writes `segs/_spoken.wav` INTO the V1 folder, and its module imports drag in the
TTS stack. So we parse `make_narration.py` and `build.py` with `ast` (no execution,
no side effects, no dependencies) and do the silence-trim ourselves into a temp dir.

The constants LEAD / GAP / KJV_GAP / TAIL vary per build — we always read THAT
build's values, never a remembered default.

Usage:
    python3 media-production-v2/extract_beats.py 1
    python3 media-production-v2/extract_beats.py 1 --json out.json
"""
import argparse
import ast
import glob
import json
import os
import re
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V1 = os.path.join(ROOT, "media-production")

# Dup-numbered rows: the one build folder that is canonical for that row.
# Mirrors media-production/corpus.py CANONICAL_BUILD_SLUGS.
CANONICAL_BUILD_SLUGS = {
    65: "help-mine-unbelief",
    67: "the-transfiguration",
    86: "the-wise-men",
    89: "the-last-supper",
    128: "heart-far-from-me",
    133: "what-jesus-called-hell",
    134: "today-in-paradise",
    137: "one-as-we-are-one",
    140: "naaman-washes",
}

SPEAKER_CONSTS = {
    "NARRATOR": "narrator",
    "JESUS": "jesus",
    "GOD": "god",
    "SCRIPTURE": "scripture",
    "WOMAN": "woman",
}


def build_dir(row):
    """Resolve row number -> the canonical V1 build folder."""
    cands = sorted(glob.glob(os.path.join(V1, f"build-{row:02d}-*")))
    if not cands:
        cands = sorted(glob.glob(os.path.join(V1, f"build-{row}-*")))
    cands = [c for c in cands if os.path.isfile(os.path.join(c, "build.py"))]
    if not cands:
        raise SystemExit(f"row {row}: no V1 build folder with a build.py")
    want = CANONICAL_BUILD_SLUGS.get(row)
    if want:
        exact = [c for c in cands
                 if re.sub(rf"^build-0*{row}-", "", os.path.basename(c)) == want]
        if len(exact) != 1:
            raise SystemExit(
                f"row {row}: canonical slug {want!r} not unique in "
                + ", ".join(os.path.basename(c) for c in cands))
        return exact[0]
    if len(cands) > 1:
        raise SystemExit(
            f"row {row}: {len(cands)} build folders and no canonical slug — "
            + ", ".join(os.path.basename(c) for c in cands))
    return cands[0]


def _const(node, consts):
    """Evaluate a literal, or a Name that resolves to one of the module's consts."""
    if isinstance(node, ast.Constant):
        return node.value
    if isinstance(node, ast.Name):
        if node.id in SPEAKER_CONSTS:
            return SPEAKER_CONSTS[node.id]
        if node.id in consts:
            return consts[node.id]
        return node.id
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
        return -_const(node.operand, consts)
    # Multi-still segments nest: ("n0", [(S1, "in"), (S2, "marker words")], "in").
    # Rows 10/18/19 (the word-anchored marker builds) all use this shape and were
    # failing extraction outright because the resolver only handled flat nodes.
    if isinstance(node, (ast.List, ast.Tuple)):
        return [_const(e, consts) for e in node.elts]
    raise ValueError(ast.dump(node))


def parse_module(path):
    """Return (module-level simple constants, tree) for a source file."""
    tree = ast.parse(open(path).read())
    consts = {}
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 \
                and isinstance(node.targets[0], ast.Name):
            try:
                consts[node.targets[0].id] = _const(node.value, consts)
            except ValueError:
                pass
    return consts, tree


def parse_list_of_tuples(tree, name, consts):
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 \
                and isinstance(node.targets[0], ast.Name) \
                and node.targets[0].id == name:
            rows = []
            for elt in node.value.elts:
                rows.append(tuple(_const(e, consts) for e in elt.elts))
            return rows
    raise SystemExit(f"{name} not found")


def dur_of(path):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", path], capture_output=True, text=True)
    return float(out.stdout.strip())


def spoken_of(path, tmpdir):
    """Duration with trailing silence removed — build.py's exact filter chain.

    Writes the scratch wav into a temp dir, never into the read-only V1 folder.
    """
    tmp = os.path.join(tmpdir, "_spoken.wav")
    subprocess.run(
        ["ffmpeg", "-y", "-v", "error", "-i", path, "-af",
         "areverse,silenceremove=start_periods=1:start_threshold=-50dB:"
         "start_duration=0.02,areverse", "-c:a", "pcm_s16le", tmp],
        check=True, capture_output=True)
    return dur_of(tmp)


def extract(row):
    bdir = build_dir(row)
    slug = os.path.basename(bdir)
    nconsts, ntree = parse_module(os.path.join(bdir, "make_narration.py"))
    bconsts, btree = parse_module(os.path.join(bdir, "build.py"))

    segments = parse_list_of_tuples(ntree, "SEGMENTS", nconsts)
    beats = parse_list_of_tuples(btree, "BEATS", bconsts)

    text = {s[0]: s[2] for s in segments}
    speaker = {s[0]: s[1] for s in segments}

    lead = float(bconsts.get("LEAD", 0.28))
    gap = float(bconsts.get("GAP", 0.72))
    kjv_gap = float(bconsts.get("KJV_GAP", gap))
    tail = float(bconsts.get("TAIL", 1.5))

    out = {
        "row": row, "slug": slug, "v1_dir": os.path.relpath(bdir, ROOT),
        "constants": {"LEAD": lead, "GAP": gap, "KJV_GAP": kjv_gap, "TAIL": tail},
        "beats": [],
    }

    with tempfile.TemporaryDirectory() as tmpdir:
        t = 0.0
        for name, still, zdir in beats:
            mp3 = os.path.join(bdir, "audio", f"{name}.mp3")
            adur = dur_of(mp3)
            sdur = spoken_of(mp3, tmpdir)
            spk = speaker.get(name, "narrator")
            g = kjv_gap if spk != "narrator" else gap
            vdur = lead + sdur + g
            timing_path = os.path.join(bdir, "audio", f"{name}.timing.json")
            timing = json.load(open(timing_path)) if os.path.exists(timing_path) else []
            out["beats"].append({
                "seg": name, "v1_still": still, "zoom": zdir, "speaker": spk,
                "text": text.get(name, ""),
                "seg_start": round(t, 3),
                "audio_start": round(t + lead, 3),
                "spoken_end": round(t + lead + sdur, 3),
                "seg_end": round(t + vdur, 3),
                "audio_dur": round(adur, 3), "spoken_dur": round(sdur, 3),
                "seg_dur": round(vdur, 3),
                "timing": timing,
            })
            t += vdur

        # The closing card's segment id varies per build: most use "card", but e.g.
        # build-02 declares CARD = "n8". Read THAT build's constant, same as the
        # timing constants — never assume.
        # Builds declare the card three different ways, so ASK THE BUILD, never
        # assume: build-02 has CARD = "n8"; build-03 has no CARD constant at all and
        # hardcodes `card_dur = dur_of("audio/n10.mp3")` with the words in a separate
        # CARD_TEXT constant. Falling through to the "card" default made ffprobe
        # return nothing and blew up on float('').
        card_id = bconsts.get("CARD")
        if not card_id:
            m = re.search(r'card_dur\s*=\s*dur_of\(\s*[\'"]audio/([A-Za-z0-9_]+)\.mp3',
                          open(os.path.join(bdir, "build.py")).read())
            card_id = m.group(1) if m else "card"
        card_mp3 = os.path.join(bdir, "audio", f"{card_id}.mp3")
        if not os.path.exists(card_mp3):
            raise SystemExit(
                f"card segment {card_id!r} has no mp3 in {bdir}/audio — "
                f"read that build's build.py and pass the right id")
        card_dur = dur_of(card_mp3)
        out["card"] = {
            "seg": card_id,
            "text": text.get(card_id, ""),
            "seg_start": round(t, 3),
            "audio_start": round(t + lead, 3),
            "seg_dur": round(lead + card_dur + tail, 3),
        }
        out["total"] = round(t + lead + card_dur + tail, 3)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("row", type=int)
    ap.add_argument("--json", default=None)
    a = ap.parse_args()
    data = extract(a.row)
    if a.json:
        os.makedirs(os.path.dirname(os.path.abspath(a.json)), exist_ok=True)
        json.dump(data, open(a.json, "w"), indent=1)
    print(f"row {data['row']}  {data['slug']}  total {data['total']:.1f}s  "
          f"{len(data['beats'])} beats  constants {data['constants']}")
    for b in data["beats"]:
        print(f"  {b['seg']:<5} {b['speaker']:<9} {b['audio_start']:7.2f}"
              f" → {b['spoken_end']:7.2f}  ({b['spoken_dur']:5.2f}s spoken)"
              f"  still={b['v1_still']}")
        print(f"        {b['text'][:110]}")
    print(f"  card  {data['card']['audio_start']:7.2f}  {data['card']['text'][:90]}")


if __name__ == "__main__":
    main()
