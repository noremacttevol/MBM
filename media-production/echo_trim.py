#!/usr/bin/env python3
"""Apply the echo trim (Agent #1 / Planner). Shares echo_scan's detection.

For each narrator beat echo_scan flags: drop the restating sentence(s); if the beat
has nothing left, delete the whole narrator segment. Keeps every non-echo sentence
(teaching) and every character/scripture line. Edits only make_narration.py
SEGMENTS. Preserves interspersed `# verse` comments and code outside SEGMENTS.

New-format builds (id, SPEAKER, text) are rewritten precisely. Old-format
(id, SPEAKER, rate, pitch, text) builds are REPORTED for manual editing (they are
few) rather than risk breaking their main() unpacking.

After editing a build it removes .eleven-done / .audio-eleven-done so #2 re-voices.

Usage:
  python3 echo_trim.py --dry            # show what would change
  python3 echo_trim.py --apply          # do it (all dirty builds)
  python3 echo_trim.py --apply --rows 5,18
"""
import argparse
import ast
import glob
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
import echo_scan as E
import export_transcripts as X

SPEAKER_CONST = {"narrator": "NARRATOR", "jesus": "JESUS", "god": "GOD",
                 "scripture": "SCRIPTURE", "woman": "WOMAN"}


def _py(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def _list_node(tree):
    for n in ast.walk(tree):
        if isinstance(n, ast.Assign):
            for t in n.targets:
                if isinstance(t, ast.Name) and t.id == "SEGMENTS":
                    return n.value
    return None


def _new_format(node):
    return isinstance(node, (ast.List, ast.Tuple)) and all(
        isinstance(el, (ast.Tuple, ast.List)) and len(el.elts) == 3
        for el in node.elts)


def plan(folder):
    """{narr_id: new_text_or_None(delete)} from echo_scan."""
    edits = {}
    for _, nid, vid, echoes, kept in E.scan_build(folder):
        edits[nid] = " ".join(kept) if kept else None
    return edits


def clear_markers(folder, dry):
    for m in (".eleven-done", ".audio-eleven-done"):
        p = os.path.join(folder, m)
        if os.path.exists(p) and not dry:
            os.remove(p)


def apply_build(folder, dry):
    edits = plan(folder)
    if not edits:
        return "clean", 0
    mn = os.path.join(folder, "make_narration.py")
    src = open(mn).read()
    tree = ast.parse(src)
    node = _list_node(tree)
    if node is None:
        return "no SEGMENTS", 0
    if not _new_format(node):
        return "OLD-FORMAT (manual)", 0

    segs = {s["id"]: s for s in X.parse_segments(mn)}
    lines = src.split("\n")
    start_map = {}
    for el in node.elts:
        sid = ast.literal_eval(el.elts[0])
        start_map[el.lineno] = (el.end_lineno, sid)

    out = lines[:node.lineno - 1]
    i, end = node.lineno, node.end_lineno
    ndel = ntrim = 0
    while i <= end:
        if i in start_map:
            e_end, sid = start_map[i]
            if sid in edits:
                if edits[sid] is None:
                    ndel += 1  # delete whole segment: emit nothing
                else:
                    const = SPEAKER_CONST[segs[sid]["speaker"]]
                    out.append(f'    ("{sid}", {const}, {_py(edits[sid])}),')
                    ntrim += 1
            else:
                out.extend(lines[i - 1:e_end])  # unchanged element, verbatim
            i = e_end + 1
        else:
            out.append(lines[i - 1])
            i += 1
    out += lines[end:]
    new_src = "\n".join(out)
    try:
        ast.parse(new_src)
    except SyntaxError as ex:
        return f"REWRITE-BROKE ({ex})", 0
    if not dry:
        open(mn, "w").write(new_src)
        clear_markers(folder, dry)
    return f"trimmed {ntrim}, deleted {ndel} seg(s)", ntrim + ndel


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--dry", action="store_true")
    ap.add_argument("--rows")
    args = ap.parse_args()
    dry = not args.apply
    only = set(int(x) for x in args.rows.split(",")) if args.rows else None

    builds = sorted(glob.glob(os.path.join(HERE, "build-*")))
    manual, changed = [], 0
    for b in builds:
        if not os.path.isdir(b):
            continue
        if only:
            m = re.match(r"build-(\d+)-", os.path.basename(b))
            if not m or int(m.group(1)) not in only:
                continue
        status, n = apply_build(b, dry)
        if status == "clean":
            continue
        print(f"{os.path.basename(b)}: {status}")
        if "OLD-FORMAT" in status:
            manual.append(os.path.basename(b))
        elif n:
            changed += 1
    print(f"\n{'DRY — ' if dry else ''}{changed} build(s) "
          f"{'would change' if dry else 'changed'}")
    if manual:
        print(f"{len(manual)} OLD-FORMAT build(s) need MANUAL edit: "
              + ", ".join(manual))


if __name__ == "__main__":
    main()
