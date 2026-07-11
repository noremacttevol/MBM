#!/usr/bin/env python3
"""
jesus_face_gate.py — THE FACE GATE (Cameron, 2026-07-11, Correction #18)

Cameron's law: we do NOT know what Jesus looked like, and no AI helping make
these videos is allowed to prompt Google Flow for a picture or clip that
CONSTRUCTS his face. Every story that builds a different invented face for the
Lord pulls the viewer onto the artwork instead of the story, and putting a
made-up face on him is not good worship. He stays a "mystery" figure: seen from
BEHIND, OVER-THE-SHOULDER, or AT A DISTANCE — a real, warm, Middle Eastern human
presence whose FACE is simply never in the frame.

This script is the mechanical gate that enforces that BEFORE any credit is spent.
It reads the written prompt sheets for a video and FAILS (exit code 1) if:

  1. FORBIDDEN — a sentence that names Jesus also contains face-constructing
     language (face, eyes, profile, portrait, close-up, expression, smile,
     looking at the camera, three-quarter view, jaw/cheek/nose/mouth/brow, etc.).

  2. MISSING CUE — a prompt paragraph that stages Jesus does NOT contain any
     approved face-hiding camera cue (from behind / over-the-shoulder / at a
     distance / face turned away / camera behind him ...). If nothing in the
     paragraph tells Flow to keep the camera off his face, Flow will invent one.

It PASSES (exit 0) only when every Jesus prompt is provably face-safe on paper.

This gate does NOT judge other characters — their faces are allowed and SHOULD
stay consistent within a story so viewers can follow it. It only guards Jesus.

It is a paper gate, not a replacement for the human high-zoom face audit of the
finished render (§5 QC). A prompt that fails here must be fixed before Flow.

USAGE
  python3 jesus_face_gate.py                # auto-scan every build-*/ prompt sheet
  python3 jesus_face_gate.py FILE [FILE...] # check specific files
  python3 jesus_face_gate.py --dir build-15-centurion

Exit code 0 = PASS (safe to generate). Exit code 1 = FAIL (fix before Flow).
"""

import sys
import os
import re
import glob

# ---------------------------------------------------------------------------
# The words that name Jesus in a prompt. We deliberately do NOT include bare
# pronouns ("he", "him") — too noisy — so prompt sheets should name him at least
# once per paragraph that stages him (which good prompts already do).
# ---------------------------------------------------------------------------
JESUS_TOKENS = [
    r"jesus",
    r"christ",
    r"the lord\b",
    r"the master\b",
    r"the messiah\b",
    r"the saviou?r\b",
    r"the teacher\b",
    r"rabboni",
    r"the son of god",
]

# ---------------------------------------------------------------------------
# FORBIDDEN: language that builds / reveals his face. If any of these appears in
# the SAME sentence as a Jesus token, the prompt is rejected. Extend this list
# whenever a new face-leaking phrase slips through — that is the whole point.
# NOTE: "hand"/"hands" are NOT here. Correction #16/#18 allow his Middle Eastern
# hands to show; only the FACE is withheld.
# ---------------------------------------------------------------------------
FORBIDDEN_FACE_TERMS = [
    r"\bface\b", r"\bfaces\b", r"\bfacial\b", r"\bface-on\b", r"\bface on\b",
    r"\bcountenance\b", r"\bvisage\b",
    r"\bprofile\b", r"\bside profile\b", r"\bside-profile\b",
    r"\bportrait\b",
    r"\bclose-?up\b", r"\bclose up\b",
    r"\bthree-quarter\b", r"\bthree quarter\b", r"\b3/4 view\b",
    r"\bfrontal\b", r"\bfront view\b", r"\bfront-on\b", r"\bfront on\b",
    r"\bfacing the camera\b", r"\bfacing the viewer\b", r"\bfacing us\b",
    r"\bfacing forward\b", r"\bturns to face\b", r"\bturning to face\b",
    r"\blooking at the camera\b", r"\blooking into the camera\b",
    r"\blooking at the viewer\b", r"\blooking toward the camera\b",
    r"\beye contact\b", r"\bmeets? (?:the|her|his|their) eyes\b",
    r"\bhis eyes\b", r"\bhis gaze\b", r"\bhis expression\b", r"\bhis features\b",
    r"\bhis smile\b", r"\bhis cheek\b", r"\bhis cheeks\b", r"\bhis jaw\b",
    r"\bhis jawline\b", r"\bhis nose\b", r"\bhis mouth\b", r"\bhis lips\b",
    r"\bhis brow\b", r"\bhis brows\b", r"\bhis beard\b", r"\bhis chin\b",
    r"\bhis forehead\b", r"\bhis teeth\b",
    r"\bsmiling warmly\b",  # only flagged when in a Jesus sentence (see logic)
]

# ---------------------------------------------------------------------------
# REQUIRED: at least one of these face-hiding camera cues must appear in any
# paragraph that stages Jesus. If none is present, Flow has no instruction to
# keep the camera off his face and will build one.
# ---------------------------------------------------------------------------
FACE_HIDING_CUES = [
    r"from behind", r"behind him", r"behind his", r"behind the figure",
    r"back of his head", r"back of the head", r"back of his",
    r"his back to the camera", r"back to the camera", r"turned away",
    r"over[- ]the[- ]shoulder", r"over his shoulder", r"over the man'?s shoulder",
    r"at a distance", r"in the distance", r"distant figure", r"a distance",
    r"far off", r"far away", r"far-?off", r"seen from behind",
    r"face turned away", r"face away", r"face is not shown", r"face not shown",
    r"face hidden", r"no view of his face", r"his face is never",
    r"camera behind", r"camera stays behind", r"away from view",
    r"on the far side", r"far side", r"silhouetted from behind",
    r"only his back", r"only the back", r"his shoulder and hair",
]

# A paragraph clearly stages Jesus (as opposed to merely mentioning him in
# narration/notes) if it also reads like a Flow prompt: it describes a shot.
# We treat ANY paragraph containing a Jesus token as needing a cue, but we skip
# obvious non-prompt lines (checklist items, narration script, headers) via
# lightweight filters below.
SKIP_LINE_HINTS = [
    "narrat", "kjv", "voice:", "seed question", "closing card", "must show",
    "must never show", "- [ ]", "- [x]", "correction", "#18", "face gate",
]

sentence_split = re.compile(r"(?<=[.!?;:])\s+|\n")


def compile_all(patterns):
    return [re.compile(p, re.IGNORECASE) for p in patterns]


JESUS_RE = compile_all(JESUS_TOKENS)
FORBIDDEN_RE = compile_all(FORBIDDEN_FACE_TERMS)
CUE_RE = compile_all(FACE_HIDING_CUES)


def has_jesus(text):
    return any(r.search(text) for r in JESUS_RE)


def find_forbidden(text):
    hits = []
    for r in FORBIDDEN_RE:
        m = r.search(text)
        if m:
            hits.append(m.group(0))
    return hits


def has_cue(text):
    return any(r.search(text) for r in CUE_RE)


def is_probably_prompt_paragraph(para):
    low = para.lower()
    # A prompt paragraph is prose that stages a shot; skip narration/checklist.
    for hint in SKIP_LINE_HINTS:
        if hint in low:
            return False
    return True


def check_file(path):
    """Return (fails, warns) where each is a list of (lineno, msg)."""
    fails = []
    warns = []
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as fh:
            raw = fh.read()
    except OSError as exc:
        return [(0, f"could not read file: {exc}")], []

    lines = raw.split("\n")

    # 1) FORBIDDEN check — sentence granularity, with accurate line numbers.
    #    Walk line by line; within a line, split into sentences.
    for lineno, line in enumerate(lines, start=1):
        if not has_jesus(line):
            continue
        for sentence in sentence_split.split(line):
            if not sentence.strip():
                continue
            if not has_jesus(sentence):
                continue
            hits = find_forbidden(sentence)
            if hits:
                fails.append(
                    (lineno,
                     f"Jesus + face language {sorted(set(hits))}: "
                     f"\"{sentence.strip()[:140]}\"")
                )

    # 2) MISSING-CUE check — paragraph granularity.
    #    Track the starting line number of each blank-line-delimited paragraph.
    para_lines = []
    para_start = 1
    for lineno, line in enumerate(lines, start=1):
        if line.strip() == "":
            if para_lines:
                _check_paragraph(para_lines, para_start, warns)
            para_lines = []
            para_start = lineno + 1
        else:
            para_lines.append(line)
    if para_lines:
        _check_paragraph(para_lines, para_start, warns)

    return fails, warns


def _check_paragraph(para_lines, start_lineno, warns):
    para = "\n".join(para_lines)
    if not has_jesus(para):
        return
    if not is_probably_prompt_paragraph(para):
        return
    if not has_cue(para):
        warns.append(
            (start_lineno,
             "Jesus staged with NO face-hiding camera cue "
             "(need 'from behind' / 'over-the-shoulder' / 'at a distance' / "
             "'face turned away' ...): "
             f"\"{para.strip()[:140]}\"")
        )


def gather_default_targets():
    here = os.path.dirname(os.path.abspath(__file__))
    patterns = [
        os.path.join(here, "build-*", "PROMPTS.md"),
        os.path.join(here, "build-*", "PREFLIGHT.md"),
        os.path.join(here, "build-*", "*PROMPT*.md"),
        os.path.join(here, "build-*", "*prompt*.md"),
    ]
    found = []
    for pat in patterns:
        found.extend(glob.glob(pat))
    # de-dup, stable order
    seen = set()
    out = []
    for f in sorted(found):
        if f not in seen:
            seen.add(f)
            out.append(f)
    return out


def main(argv):
    args = argv[1:]
    targets = []
    if not args:
        targets = gather_default_targets()
        if not targets:
            print("FACE GATE: no prompt sheets found to check "
                  "(looked for build-*/PROMPTS.md and *PROMPT*.md).")
            print("Pass files explicitly: python3 jesus_face_gate.py FILE ...")
            return 0
    elif args[0] == "--dir":
        if len(args) < 2:
            print("usage: jesus_face_gate.py --dir BUILD_DIR")
            return 2
        d = args[1]
        for name in ("PROMPTS.md", "PREFLIGHT.md"):
            p = os.path.join(d, name)
            if os.path.exists(p):
                targets.append(p)
        targets.extend(glob.glob(os.path.join(d, "*PROMPT*.md")))
        targets.extend(glob.glob(os.path.join(d, "*prompt*.md")))
        targets = sorted(set(targets))
        if not targets:
            print(f"FACE GATE: no prompt sheets found in {d}")
            return 2
    else:
        targets = args

    total_fails = 0
    total_warns = 0
    print("=" * 72)
    print("THE FACE GATE — Correction #18: Jesus's face is never prompted.")
    print("=" * 72)
    for path in targets:
        fails, warns = check_file(path)
        rel = path
        if not fails and not warns:
            print(f"  PASS  {rel}")
            continue
        print(f"  ----  {rel}")
        for lineno, msg in fails:
            print(f"    FAIL  line {lineno}: {msg}")
        for lineno, msg in warns:
            print(f"    WARN  line {lineno}: {msg}")
        total_fails += len(fails)
        total_warns += len(warns)

    print("-" * 72)
    if total_fails == 0 and total_warns == 0:
        print("RESULT: PASS — every Jesus prompt is face-safe. Safe to generate.")
        return 0
    print(f"RESULT: {total_fails} FAIL (face language), "
          f"{total_warns} WARN (no face-hiding cue).")
    if total_fails:
        print("FAILs are hard stops: rewrite the prompt so Jesus is staged from")
        print("behind / over-the-shoulder / at a distance, with NO face words,")
        print("BEFORE spending a single Flow credit. (Correction #18.)")
    else:
        print("No hard FAILs, but every WARN paragraph stages Jesus with no")
        print("camera instruction to keep the shot off his face — add one, or")
        print("Flow will invent a face. Treat WARNs as blocking too.")
    # WARNs are blocking: a Jesus prompt with no face-hiding cue is exactly how
    # a face leaks in. Exit nonzero for either.
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
