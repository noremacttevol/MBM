#!/usr/bin/env python3
"""Export every video's narration into clean TRANSCRIPTS/ — the handoff the
ElevenLabs voice session reads from. See TRANSCRIPT-LANE.md.

Source of truth is each build's make_narration.py `SEGMENTS` list. We AST-parse
it (no importing, no side effects, no TTS) and handle BOTH shapes:
  new: (id, SPEAKER, text)
  old: (id, SPEAKER, rate, pitch, text)
speaker is always the 2nd element; the spoken text is always the LAST element.

For each build we write:
  TRANSCRIPTS/<NNN>-<slug>.json  machine-readable: [{id,speaker,text}]  (for the
                                 voice session — speaker picks the voice)
  TRANSCRIPTS/<NNN>-<slug>.txt   human-readable, speaker-tagged (for Cameron)
and TRANSCRIPTS/INDEX.md listing every video, its segment/word counts.

Usage:
  python3 export_transcripts.py            # export all
  python3 export_transcripts.py --rows 5,140
"""
import argparse
import ast
import glob
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "TRANSCRIPTS")

SPEAKER_NAMES = {"NARRATOR": "narrator", "JESUS": "jesus", "GOD": "god",
                 "SCRIPTURE": "scripture", "WOMAN": "woman"}


def _str(node):
    """Evaluate a string node: plain literal, implicit/`+` concatenation."""
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
        return _str(node.left) + _str(node.right)
    if isinstance(node, ast.JoinedStr):  # f-string — join the literal parts
        return "".join(v.value for v in node.values
                       if isinstance(v, ast.Constant))
    return ast.literal_eval(node)  # last resort; raises on anything exotic


def _speaker(node):
    if isinstance(node, ast.Name):
        return SPEAKER_NAMES.get(node.id, node.id.lower())
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value.lower()
    return "narrator"


def parse_segments(path):
    with open(path) as f:
        tree = ast.parse(f.read())
    seg_node = None
    for n in ast.walk(tree):
        if isinstance(n, ast.Assign):
            for t in n.targets:
                if isinstance(t, ast.Name) and t.id == "SEGMENTS":
                    seg_node = n.value
    if seg_node is None or not isinstance(seg_node, (ast.List, ast.Tuple)):
        return None
    segs = []
    for el in seg_node.elts:
        if not isinstance(el, (ast.Tuple, ast.List)) or len(el.elts) < 3:
            continue
        try:
            sid = _str(el.elts[0])
            speaker = _speaker(el.elts[1])
            text = _str(el.elts[-1])
        except Exception:
            continue
        segs.append({"id": sid, "speaker": speaker, "text": text.strip()})
    return segs


def row_of(folder):
    m = re.match(r"build-(\d+)-(.+)", os.path.basename(folder))
    return (int(m.group(1)), m.group(2)) if m else (None, None)


_STOP = {"the", "a", "of", "and", "in", "to", "his", "her", "thou", "mine"}


def _tokens(s):
    return {w for w in re.findall(r"[a-z]+", s.lower()) if w not in _STOP}


def queue_titles(queue_path):
    """{row: story title} from QUEUE.md's 'The 200' table rows."""
    titles = {}
    if not os.path.exists(queue_path):
        return titles
    with open(queue_path) as f:
        for line in f:
            m = re.match(r"\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|", line)
            if m:
                titles.setdefault(int(m.group(1)), m.group(2).strip().strip('"'))
    return titles


def _score(folder, slug, segs, title):
    """Higher = more likely the CURRENT canonical build. The QUEUE story title
    dominates (an archived old build keeps its mp4, so mp4 alone can't decide);
    then a shipped mp4, the modern speaker format, and segment count break ties."""
    import glob as _g
    overlap = len(_tokens(slug) & _tokens(title)) if title else 0
    has_mp4 = bool(_g.glob(os.path.join(folder, "*.mp4")))
    with open(os.path.join(folder, "make_narration.py")) as f:
        speaker_fmt = "from mbm_speakers import" in f.read()
    return (overlap * 1000 + (100 if has_mp4 else 0)
            + (10 if speaker_fmt else 0) + len(segs))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rows")
    args = ap.parse_args()
    only = set(int(x) for x in args.rows.split(",")) if args.rows else None

    os.makedirs(OUT, exist_ok=True)
    titles = queue_titles(os.path.join(HERE, "QUEUE.md"))
    # Group folders by row so a row with several folders (stale/archived builds)
    # resolves to ONE canonical transcript. Extra folders become a dedup report.
    by_row = {}
    for b in sorted(glob.glob(os.path.join(HERE, "build-*"))):
        if not os.path.isdir(b):
            continue
        row, slug = row_of(b)
        if row is None:
            continue
        mn = os.path.join(b, "make_narration.py")
        segs = parse_segments(mn) if os.path.exists(mn) else None
        by_row.setdefault(row, []).append(
            {"folder": b, "slug": slug, "segs": segs,
             "score": _score(b, slug, segs, titles.get(row)) if segs else -1})

    index, exported, skipped, dups = [], 0, [], []
    for row in sorted(by_row):
        if only and row not in only:
            continue
        cands = by_row[row]
        usable = [c for c in cands if c["segs"]]
        if not usable:
            skipped.append((row, "no parseable SEGMENTS in any folder"))
            continue
        usable.sort(key=lambda c: c["score"], reverse=True)
        best = usable[0]
        for c in cands:
            if c["folder"] != best["folder"]:
                dups.append((row, os.path.basename(c["folder"]),
                             os.path.basename(best["folder"])))
        segs, slug = best["segs"], best["slug"]
        stem = f"{row:03d}-{slug}"
        words = sum(len(s["text"].split()) for s in segs)
        with open(os.path.join(OUT, stem + ".json"), "w") as f:
            json.dump({"row": row, "slug": slug, "segments": segs}, f, indent=2)
        with open(os.path.join(OUT, stem + ".txt"), "w") as f:
            for s in segs:
                f.write(f"[{s['speaker']}] {s['text']}\n\n")
        index.append((row, slug, len(segs), words))
        exported += 1

    with open(os.path.join(OUT, "INDEX.md"), "w") as f:
        f.write("# TRANSCRIPTS INDEX — narration handed to the ElevenLabs voice "
                "session\n\n")
        f.write("Generated by `export_transcripts.py` from each build's "
                "make_narration.py SEGMENTS. Speaker tags: narrator / jesus / god "
                "/ scripture / woman (each maps to a voice).\n\n")
        f.write("| # | Story | Segments | Words |\n|---|---|---|---|\n")
        for row, slug, nseg, words in index:
            f.write(f"| {row} | {slug} | {nseg} | {words} |\n")
    with open(os.path.join(OUT, "DUPLICATES.md"), "w") as f:
        f.write("# DUPLICATE / STALE BUILD FOLDERS — one row, several folders\n\n")
        f.write("Each row below has more than one `build-<row>-*` folder. The "
                "canonical one (shipped mp4 > modern speaker format > most "
                "segments) was exported; the others are stale or archived-in-place "
                "(2026-07-20 audit) and were NOT exported. Do not delete archived "
                "builds; this is the list to verify against the QUEUE.\n\n")
        if dups:
            f.write("| Row | Not exported (stale/archived) | Canonical (exported) |\n")
            f.write("|---|---|---|\n")
            for row, stale, best in dups:
                f.write(f"| {row} | {stale} | {best} |\n")
        else:
            f.write("_None — every row resolved to a single folder._\n")
    print(f"exported {exported} transcripts -> TRANSCRIPTS/ (one per row)")
    if dups:
        print(f"resolved {len(dups)} duplicate folder(s) — see TRANSCRIPTS/DUPLICATES.md:")
        for row, stale, best in dups:
            print(f"  #{row}: kept {best}, skipped {stale}")
    if skipped:
        print(f"skipped {len(skipped)}:")
        for row, why in skipped:
            print(f"  #{row}: {why}")


if __name__ == "__main__":
    main()
