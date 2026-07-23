#!/usr/bin/env python3
"""Narrator-echo scanner (Agent #1 / Planner).

An "echo" is a NARRATOR sentence that merely repeats a verbatim character/scripture
line sitting right next to it (jesus/god/scripture/woman = exact KJV). Rule 4 /
STORY-INTEGRITY-LAW: keep the character line, cut (or rewrite with NEW meaning) the
narrator sentence that restates it.

Reads each build's make_narration.py SEGMENTS (the source of truth) directly, so it
does not depend on TRANSCRIPTS/ being fresh. echo_trim.py imports scan_build() from
here so the trimmer and the scanner use ONE definition — driving this to zero is
therefore real, not gamed.

Prints per-build counts and, last line, `TOTAL echo pairs: N`.
Usage: python3 echo_scan.py            (or --min 0.6 to change the sentence cut)
"""
import argparse
import glob
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
VERBATIM = {"jesus", "god", "scripture", "woman"}
CUT = 0.6  # fraction of a narrator sentence's own content words found in the verse

_STOP = set("""a an the and or but of to in on at for from by with as is are was were
be been being this that these those he she it they them his her its their him you
your thou thee thy thine ye not no so if then when what which who whom how out up
one all any some there here into unto upon shall will would could should did do done
had has have said say saith came come go went make made too then now""".split())

# reuse the AST SEGMENTS parser
import export_transcripts as X


def content(text):
    return [w for w in re.findall(r"[a-z]+", text.lower())
            if w not in _STOP and len(w) > 2]


def sentences(text):
    return [p for p in re.split(r"(?<=[.!?;:]) +", text.strip()) if p]


def is_echo(sent, verse, cut):
    sv = content(sent)
    if len(sv) < 2:
        return False
    vv = set(content(verse))
    frac = sum(1 for w in sv if w in vv) / len(sv)
    # a capitalized content word absent from the verse = new info -> not an echo
    proper_new = any(w[0].isupper() and w.lower() not in vv
                     for w in re.findall(r"[A-Za-z]+", sent)
                     if len(w) > 2 and w.lower() not in _STOP)
    return frac >= cut and not proper_new


def scan_build(folder, cut=CUT):
    """[(narr_idx, narr_id, verse_id, echo_sents, kept_sents)] for one build."""
    mn = os.path.join(folder, "make_narration.py")
    if not os.path.exists(mn):
        return []
    segs = X.parse_segments(mn)
    if not segs:
        return []
    out = []
    for i, s in enumerate(segs):
        if s["speaker"] != "narrator":
            continue
        best = None
        for j in (i - 1, i + 1):
            if 0 <= j < len(segs) and segs[j]["speaker"] in VERBATIM:
                verse = segs[j]["text"]
                echoes = [x for x in sentences(s["text"]) if is_echo(x, verse, cut)]
                if echoes and (best is None or len(echoes) > len(best[2])):
                    kept = [x for x in sentences(s["text"])
                            if not is_echo(x, verse, cut)]
                    best = (i, s["id"], segs[j]["id"], echoes, kept)
        if best:
            out.append(best)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--min", type=float, default=CUT)
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args()
    builds = sorted(glob.glob(os.path.join(HERE, "build-*")))
    total, dirty = 0, 0
    for b in builds:
        if not os.path.isdir(b):
            continue
        echoes = scan_build(b, args.min)
        n = sum(len(e[3]) for e in echoes)  # count each restating SENTENCE
        if n:
            dirty += 1
            print(f"{os.path.basename(b)}: {n}")
            if args.verbose:
                for _, nid, vid, ec, _ in echoes:
                    for s in ec:
                        print(f"    {nid} echoes {vid}: {s}")
        total += n
    print(f"\n{dirty} build(s) with echoes")
    print(f"TOTAL echo pairs: {total}")


if __name__ == "__main__":
    main()
