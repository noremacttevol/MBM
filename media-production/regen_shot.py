#!/usr/bin/env python3
"""regen_shot.py — regenerate ONE still of a build with the RIGHT refs attached.

The reason characters drifted even after their sheets were approved: the old
`gen_shots.py` only ever attached the JESUS master face and never expanded the
`[PETER LOCK]` / `[MALCHUS LOCK]` continuity tokens or attached the character
sheets. This tool closes that gap — it is the picture-lane's regen workhorse.

For the named shot it:
  1. pulls the shot's prompt block out of PROMPTS.md (all lines under the
     `## <slug>` header up to the next `## `, minus bare `REF:` hint lines),
  2. expands `[STILL STYLE BLOCK]` and every `[X LOCK]` / `[X-Y LOCK]`
     continuity token defined in the file into full text,
  3. attaches the reference jpegs for each character in --chars (CAST-REF single
     portrait if it exists, else the CHARACTERS 3-view sheet face-front+full-body)
     and the JESUS master face when --jesus is set,
  4. calls `flow_driver.py gen` ($0 on Nano-Banana).

Usage:
  python3 regen_shot.py --dir build-66-malchus-ear --shot s2-the-moment-after \\
      --chars peter,malchus [--jesus] [--out assets/s2-the-moment-after.jpeg] [--dry-run]

--dry-run prints the fully-expanded prompt and the ref list and generates nothing.
Always run --dry-run once and eyeball the prompt before spending a burst.
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DRIVER = HERE / "flow_driver.py"
JESUS_REF = HERE / "JESUS-MASTER-REF" / "jesus-face.jpeg"
CASTREF = HERE / "CAST-REF"
sys.path.insert(0, str(HERE / "CHARACTERS"))
from character_refs import refs as char_refs, resolve  # noqa: E402

# CAST-REF single-portrait filenames differ from the CHARACTERS slug in a few
# cases; map the canonical slug -> CAST-REF stem where they diverge.
CASTREF_ALIAS = {
    "john-beloved": "john", "james-son-of-zebedee": "james-z",
    "james-son-of-alphaeus": "james-a", "simon-the-zealot": "simon-z",
    "judas-iscariot": "judas",
}


def style_block(text):
    m = re.search(r"STILL STYLE BLOCK \(prepended[^\n]*\):\n(.*?)\n\n", text, re.S)
    return " ".join(m.group(1).split()) if m else ""


def token_defs(text):
    """Every `[TOKEN] = definition` (definition may wrap lines) -> dict."""
    defs = {}
    for m in re.finditer(r"^\[([^\]]+)\]\s*=\s*(.+?)(?=\n\n|\n\[|\Z)", text, re.S | re.M):
        defs["[" + m.group(1) + "]"] = " ".join(m.group(2).split())
    return defs


def shot_block(text, slug):
    m = re.search(r"^##\s*" + re.escape(slug) + r"[^\n]*\n(.*?)(?=^##\s|\Z)",
                  text, re.S | re.M)
    if not m:
        sys.exit(f"shot '{slug}' not found in PROMPTS.md")
    lines = [l for l in m.group(1).splitlines()
             if l.strip() and not l.strip().lower().startswith("ref:")]
    return " ".join(lines)


def ref_paths(slug):
    stem = CASTREF_ALIAS.get(slug, slug)
    single = CASTREF / f"{stem}.jpeg"
    if single.is_file():
        return [single]
    got = char_refs(slug)  # [face-front, three-quarter, full-body]
    return [Path(got[0]), Path(got[2])] if len(got) >= 3 else [Path(p) for p in got]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", required=True)
    ap.add_argument("--shot", required=True)
    ap.add_argument("--chars", default="", help="comma-separated character slugs to attach")
    ap.add_argument("--jesus", action="store_true", help="attach JESUS-MASTER-REF")
    ap.add_argument("--out", default="")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    d = Path(a.dir)
    if not d.is_absolute():
        d = HERE / d
    text = (d / "PROMPTS.md").read_text()

    prompt = shot_block(text, a.shot)
    prompt = prompt.replace("[STILL STYLE BLOCK]", style_block(text))
    for tok, val in token_defs(text).items():
        prompt = prompt.replace(tok, val)
    leftover = re.findall(r"\[[A-Z][A-Z0-9 \-]*\]", prompt)
    if leftover:
        print(f"WARNING: unexpanded tokens remain: {sorted(set(leftover))}", file=sys.stderr)

    refs = []
    for c in [x.strip() for x in a.chars.split(",") if x.strip()]:
        slug = resolve(c) or c
        for p in ref_paths(slug):
            if not p.is_file():
                sys.exit(f"missing ref for {c}: {p}")
            refs.append(str(p))
    if a.jesus:
        refs.append(str(JESUS_REF))

    out = a.out or f"assets/{a.shot}.jpeg"
    out_abs = out if Path(out).is_absolute() else str(d / out)

    print(f"=== {a.dir} :: {a.shot} ===")
    print("REFS:", [Path(r).name for r in refs])
    print("PROMPT:", prompt)
    if a.dry_run:
        print("(dry-run — nothing generated)")
        return

    cmd = ["python3", str(DRIVER), "gen", "--prompt", prompt, "--out", out_abs]
    for r in refs:
        cmd += ["--ref", r]
    subprocess.run(cmd, check=True)


if __name__ == "__main__":
    main()
