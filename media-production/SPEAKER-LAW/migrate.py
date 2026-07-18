#!/usr/bin/env python3
"""Apply a speaker plan to one build: rewrite narration + build, render, verify.

A "plan" is the judgment half of the job — which speaker every line belongs to,
which segments must be split, and what the narrator's retelling says. Plans are
produced per build (see SPEAKER-LAW/plans/) and applied here deterministically.

Plan schema (plans/<build>.json):
{
  "build": "build-114-abraham-sodom",
  "reference": "Genesis 18",
  "segments": [
    {"id":"n1","speaker":"narrator","text":"..."},
    {"id":"g1","speaker":"god","text":"...","verse":"Gen 18:20"},
    {"id":"n1b","speaker":"narrator","text":"...retelling..."}
  ],
  "beats": [["n1","s1-....jpeg","in"], ...],
  "spoken": {"bow":"boh"},
  "notes": "why anything moved out of red"
}

EVERY file write goes to a temp path and is renamed into place. A killed process
once left six build.py files at 0 bytes and they were committed and pushed; that
must never repeat.
"""
import json
import os
import re
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
MP = os.path.dirname(HERE)
SHARED = ("mbm_speakers.py", "mbm_pronounce.py", "mbm_caption_timing.py")


def write_atomic(path, text):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(text)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, path)


def py_str(s):
    """Emit a Python string literal that survives round-tripping."""
    return json.dumps(s, ensure_ascii=False)


def render_narration(plan):
    segs = []
    for s in plan["segments"]:
        v = s.get("verse")
        if v:
            segs.append(f"    # {v}")
        segs.append(f'    ({py_str(s["id"])}, {s["speaker"].upper()}, '
                    f'{py_str(s["text"])}),')
    used = sorted({s["speaker"].upper() for s in plan["segments"]})
    spoken = plan.get("spoken", {})
    spoken_lit = ("{\n" + "".join(f"    {py_str(k)}: {py_str(v)},\n"
                                  for k, v in spoken.items()) + "}") if spoken else "{}"
    notes = plan.get("notes", "").strip()
    return f'''#!/usr/bin/env python3
"""Narration for {plan["build"]} — {plan["reference"]}.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

{notes}
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import {", ".join(used)}

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
{chr(10).join(segs)}
]

# Homographs this build decides for itself (never auto-replaced globally).
SPOKEN = {spoken_lit}


async def main():
    os.makedirs("audio", exist_ok=True)
    for name, speaker, text in SEGMENTS:
        flagged = [w for w in audit(text) if w not in SPOKEN]
        if flagged:
            print(f"  ! {{name}}: undecided homograph(s) {{flagged}}")
        await save_speaker_narration(spoken_text(text, SPOKEN), speaker,
                                     f"audio/{{name}}.mp3")
        print(f"saved audio/{{name}}.mp3  [{{speaker}}]")


if __name__ == "__main__":
    asyncio.run(main())
'''


# Retired local caption helpers. Verified across all 200 builds: every build
# renders through the shared caption_filter, and NOT ONE of these is called
# (caption_layers 137 defined / 0 called, caption_overlay 56 / 0). They still
# speak the old `kjv` boolean, which makes a migration impossible to verify by
# grepping, so they are cut. `timed_chunks` and `wrapped` ARE live (6/6 and
# 45/45) and are renamed instead — never stripped.
DEAD_HELPERS = ("caption_layers", "caption_overlay")


def strip_dead_helpers(src):
    lines = src.splitlines(keepends=True)
    out, i = [], 0
    while i < len(lines):
        if any(lines[i].startswith(f"def {h}(") for h in DEAD_HELPERS):
            i += 1
            while i < len(lines) and not (lines[i].startswith("def ")
                                          or lines[i].startswith("# ---- ")):
                i += 1
            while out and out[-1].strip() == "":
                out.pop()
            out.append("\n\n")
            continue
        out.append(lines[i])
        i += 1
    return "".join(out)


def rename_kjv_params(src):
    """A LIVE helper that takes `kjv` keeps a plain identifier as its parameter.

    `kjv` is a boolean there, so the call site passes is_scripture(speaker) — but
    the parameter itself must stay a name. Rename the parameter and every use of
    it inside that function's body to `scripture`, so the later blanket rewrite
    only ever sees the uses in main().
    """
    lines = src.splitlines(keepends=True)
    out, i = [], 0
    while i < len(lines):
        line = lines[i]
        m = re.match(r"def (\w+)\(([^)]*)\):", line)
        # build_still is NOT a boolean consumer — it forwards to caption_filter,
        # which needs the speaker itself to pick a colour. Left to the structural
        # rules below.
        if m and m.group(1) != "build_still" and re.search(r"\bkjv\b", m.group(2)):
            out.append(re.sub(r"\bkjv\b", "scripture", line))
            i += 1
            while i < len(lines) and not lines[i].startswith("def "):
                out.append(re.sub(r"\bkjv\b", "scripture", lines[i]))
                i += 1
            continue
        # a def whose signature wraps onto the next line
        if line.startswith("def ") and "(" in line and ")" not in line:
            block = [line]
            i += 1
            while i < len(lines) and "):" not in lines[i]:
                block.append(lines[i])
                i += 1
            if i < len(lines):
                block.append(lines[i])
                i += 1
            sig = "".join(block)
            if re.search(r"\bkjv\b", sig):
                out.append(re.sub(r"\bkjv\b", "scripture", sig))
                while i < len(lines) and not lines[i].startswith("def "):
                    out.append(re.sub(r"\bkjv\b", "scripture", lines[i]))
                    i += 1
            else:
                out.append(sig)
            continue
        out.append(line)
        i += 1
    return "".join(out)


def patch_build(src, plan):
    """Rewrite an existing build.py onto the speaker system, in place.

    Deliberately surgical: the caption look, the zoom/Ken Burns maths, the audio
    mix, the loudness pass and the size ladder are all left exactly as they are.
    """
    out = rename_kjv_params(strip_dead_helpers(src))

    # TEXT/ SPEAKER maps -------------------------------------------------------
    out = re.sub(r"^TEXT = \{s\[0\]: s\[\d\] for s in make_narration\.SEGMENTS\}",
                 "TEXT = {s[0]: s[2] for s in make_narration.SEGMENTS}\n"
                 "# SPEAKER-LAW: declared once in make_narration, so the caption colour\n"
                 "# and the narration voice can never drift apart.\n"
                 "SPEAKER = {s[0]: s[1] for s in make_narration.SEGMENTS}",
                 out, count=1, flags=re.M)

    # retire the KJV set -------------------------------------------------------
    out = re.sub(r"^KJV = \{[^}]*\}\n", "", out, count=1, flags=re.M)

    # import ------------------------------------------------------------------
    if "from mbm_speakers import is_scripture" not in out:
        out = out.replace("from mbm_caption_timing import caption_filter",
                          "from mbm_caption_timing import caption_filter\n"
                          "from mbm_speakers import is_scripture", 1)

    # BEATS -------------------------------------------------------------------
    beats = ",\n".join(f'    ({py_str(b[0])}, {b[1]}, {py_str(b[2])})'
                       for b in plan["beats"])
    out = re.sub(r"^BEATS = \[.*?^\]", f"BEATS = [\n{beats},\n]",
                 out, count=1, flags=re.M | re.S)

    # CARD_HOLD -> derived TAIL ------------------------------------------------
    out = re.sub(r"^CARD_HOLD = [0-9.]+.*$",
                 "# No-dead-air law: the video ends TAIL seconds after the last spoken\n"
                 "# word. Derived, never hand-set. Clears the card's 0.8s fade-out so\n"
                 "# the last word and the fade are never clipped.\nTAIL = 1.5",
                 out, count=1, flags=re.M)
    out = out.replace("LEAD + card_spoken + CARD_HOLD", "LEAD + card_spoken + TAIL")
    out = out.replace("LEAD + card_dur + CARD_HOLD", "LEAD + card_dur + TAIL")

    # per-beat speaker instead of the kjv boolean ------------------------------
    # The 184 template-A builds share the `kjv = name in KJV` line but then use it
    # in seven different `gap = ...` shapes, so the assignment and the uses are
    # converted independently rather than as one fixed pair.
    out = re.sub(r"^(\s*)kjv = name in KJV\s*$", r"\1speaker = SPEAKER[name]",
                 out, flags=re.M)

    # Every `kjv` still standing lives in main() (the live boolean helpers already
    # had their parameters renamed above). It now holds the SPEAKER, so rename it
    # wholesale and then repair the handful of places that genuinely wanted a
    # boolean. Renaming first and repairing second is what keeps the seven
    # different `gap = ...` shapes from each needing their own rule.
    out = re.sub(r"\bkjv\b", "speaker", out)
    out = re.sub(r"for (\w+), _s, _z, _v, (\w+), _k in timeline",
                 r"for \1, _s, _z, _v, \2, _sp in timeline", out)

    # boolean contexts — a speaker string is truthy for the narrator too, so an
    # unwrapped `if speaker` would silently give every narrator line the KJV gap.
    out = re.sub(r"\bif speaker else\b", "if is_scripture(speaker) else", out)
    out = re.sub(r"\(speaker or\b", "(is_scripture(speaker) or", out)
    out = re.sub(r"\bif speaker:", "if is_scripture(speaker):", out)
    out = re.sub(r"\bif speaker\b(?! *(?:else|\)|,))", "if is_scripture(speaker)", out)
    # live boolean helpers keep taking a bool
    for fn in ("timed_chunks", "wrapped"):
        out = re.sub(rf"({fn}\([^()]*(?:\([^()]*\)[^()]*)*?),\s*speaker\)",
                     r"\1, is_scripture(speaker))", out)

    # Windows-authored builds: repoint to this box -----------------------------
    out = re.sub(r'^SERIF = "C:/Windows/Fonts/georgia\.ttf"$',
                 'SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"',
                 out, flags=re.M)
    out = re.sub(r'^SERIF_BI = "C:/Windows/Fonts/georgiai\.ttf"$',
                 'SERIF_BI = "/usr/share/fonts/truetype/liberation/'
                 'LiberationSerif-Italic.ttf"', out, flags=re.M)
    return out


def orphaned_ids(build_src, plan):
    """Segment ids the build hardcodes that the plan no longer defines.

    Builds refer to specific beats by name outside BEATS — the sacred-silence
    music beds, `start_of['jv26']`, progress prints. A plan that RENAMES a
    segment silently orphans those and the build dies at render time with a
    KeyError. So plans keep the original ids and only ever ADD new ones; this
    catches a violation before any ffmpeg work is done.
    """
    have = {s["id"] for s in plan["segments"]}
    refs = set()
    for m in re.finditer(r"""(?:start_of|spoken|audio_dur|TEXT)\[["'](\w+)["']\]""",
                         build_src):
        refs.add(m.group(1))
    for m in re.finditer(r"""^PEAK\s*=\s*["'](\w+)["']""", build_src, re.M):
        refs.add(m.group(1))
    return sorted(r for r in refs if r not in have and r != "card")


def leftover_kjv(text):
    """Any surviving reference to the retired boolean is a migration miss."""
    hits = []
    for i, line in enumerate(text.splitlines(), 1):
        if re.search(r"\bkjv\b", line) and not line.lstrip().startswith("#"):
            if "KJV_GAP" in line or "KJV_MAX_FS" in line:
                continue
            hits.append(f"{i}: {line.strip()}")
    return hits


def migrate(build, render=True):
    d = os.path.join(MP, build)
    plan = json.load(open(os.path.join(HERE, "plans", f"{build}.json")))
    for m in SHARED:
        shutil.copy2(os.path.join(MP, m), os.path.join(d, m))

    for f in ("make_narration.py", "build.py"):
        p = os.path.join(d, f)
        if not os.path.exists(p + ".pre-speaker"):
            shutil.copy2(p, p + ".pre-speaker")

    src = open(os.path.join(d, "build.py"), encoding="utf-8").read()
    orphans = orphaned_ids(src, plan)
    if orphans:
        raise SystemExit(
            f"{build}: plan drops segment id(s) the build still references: "
            f"{orphans}. Keep the original ids and ADD new ones instead of "
            f"renaming — the music beds and start_of[] lookups depend on them.")

    write_atomic(os.path.join(d, "make_narration.py"), render_narration(plan))
    patched = patch_build(src, plan)
    miss = leftover_kjv(patched)
    if miss:
        raise SystemExit(f"{build}: build.py still references kjv:\n  " +
                         "\n  ".join(miss))
    write_atomic(os.path.join(d, "build.py"), patched)

    for f in ("make_narration.py", "build.py"):
        p = os.path.join(d, f)
        if os.path.getsize(p) < 500:
            raise SystemExit(f"{build}: {f} is suspiciously small — refusing")

    if not render:
        return "patched"

    mp4 = [f for f in os.listdir(d) if f.endswith(".mp4")]
    before = os.path.getmtime(os.path.join(d, mp4[0])) if mp4 else 0
    subprocess.run([sys.executable, "make_narration.py"], cwd=d, check=True)
    subprocess.run([sys.executable, "build.py"], cwd=d, check=True)
    mp4 = [f for f in os.listdir(d) if f.endswith(".mp4")]
    after = os.path.getmtime(os.path.join(d, mp4[0]))
    if after <= before:
        raise SystemExit(f"{build}: mp4 mtime did NOT advance — not rebuilt")
    return "rebuilt"


if __name__ == "__main__":
    for b in sys.argv[1:]:
        try:
            print(f"{b}: {migrate(b)}")
        except Exception as e:
            print(f"{b}: FAILED — {e}")
