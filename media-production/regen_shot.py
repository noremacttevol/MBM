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
    "judas-iscariot": "judas", "james": "james-z", "james-son-of-zebedee": "james-z",
}


def style_block(text):
    # Header varies across builds: "**STILL STYLE BLOCK** (prepend to every
    # prompt, exactly):" or "STILL STYLE BLOCK (prepended ...):" — accept bold
    # markers, "prepend"/"prepended", and an optional leading "STILL".
    m = re.search(
        r"(?:^|\n)[#*\s]*(?:STILL\s+)?STYLE (?:BLOCK|PREFIX)[#*\s]*\([^)]*\)\s*:?\s*\n(.*?)\n\s*\n",
        text, re.S | re.I)
    if not m:  # build-17 style: STYLE = "Beautiful hand-painted ..."
        m = re.search(r'^STYLE\s*=\s*"(.*?)"', text, re.S | re.M)
    if not m:  # fallback: the canonical style sentence inlined in a shot (build-19)
        m = re.search(r"(Beautiful hand-painted 2D animation style.*?No modern objects\.)",
                      text, re.S)
    return " ".join(m.group(1).split()) if m else ""


def token_defs(text):
    """Continuity tokens -> dict of "[TOKEN]" -> expansion text. Two formats:
    A) `[TOKEN] = definition ...`  (definition may wrap lines)
    B) `**TOKEN** (append/prepend to every prompt, exactly ...):\n<block>` — the
       block until the next blank line (e.g. build-22's ANTI-PANEL CLAUSE)."""
    defs = {}
    for m in re.finditer(r"^\[([^\]]+)\]\s*=\s*(.+?)(?=\n\n|\n\[|\Z)", text, re.S | re.M):
        defs["[" + m.group(1) + "]"] = " ".join(m.group(2).split())
    for m in re.finditer(
            r"^\**\[?([A-Z][A-Z0-9 \-]+?)\]?\**\s*\((?:append|prepend|prepended)[^)]*\)\s*:\s*\n(.*?)\n\s*\n",
            text, re.S | re.M | re.I):
        key = "[" + m.group(1).strip() + "]"
        defs.setdefault(key, " ".join(m.group(2).split()))
    return defs


def shot_block(text, slug):
    # Header format varies: "## s1-slug — ..." or "### Shot 1 — s1-slug.jpeg (...)".
    # Match a markdown header line that CONTAINS the slug, then take everything
    # up to the next header line.
    m = re.search(r"^#{2,}[^\n]*" + re.escape(slug) + r"[^\n]*\n(.*?)(?=^#{2,}\s|\Z)",
                  text, re.S | re.M)
    if not m:
        sys.exit(f"shot '{slug}' not found in PROMPTS.md")
    lines = [l for l in m.group(1).splitlines()
             if l.strip() and not l.strip().lower().startswith("ref:")]
    return " ".join(lines)


def ref_paths(slug):
    # "twelve" -> the single group portrait of the Twelve (fast: 1 ref for a whole
    # background group instead of 2-3 per named disciple).
    if slug in ("twelve", "the-twelve"):
        g = CASTREF / "the-twelve.jpeg"
        return [g] if g.is_file() else []
    # Direct variant/character folder (e.g. aged-john, risen-jesus, infant-jesus)
    # that character_refs doesn't register — use its sheet jpegs directly.
    direct = HERE / "CHARACTERS" / slug
    if (direct / "face-front.jpeg").is_file():
        got = [direct / "face-front.jpeg", direct / "full-body.jpeg"]
        return [p for p in got if p.is_file()]
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
    style = style_block(text)
    if "[STILL STYLE BLOCK]" in prompt and not style:
        sys.exit(f"ABORT {a.dir}/{a.shot}: could not find the STILL STYLE BLOCK "
                 f"definition — refusing to generate a style-less (photoreal) image.")
    prompt = prompt.replace("[STILL STYLE BLOCK]", style)
    # build-17 style: a shot begins with a bare "STYLE " keyword to be expanded.
    if style and re.match(r"^\s*STYLE\s+\S", prompt) and "[STILL STYLE BLOCK]" not in shot_block(text, a.shot):
        prompt = re.sub(r"^\s*STYLE\s+", style + " ", prompt, count=1)
    for tok, val in token_defs(text).items():
        prompt = prompt.replace(tok, val)
    leftover = re.findall(r"\[[A-Z][A-Z0-9 \-]*\]", prompt)
    if leftover:
        sys.exit(f"ABORT {a.dir}/{a.shot}: unexpanded tokens remain {sorted(set(leftover))} "
                 f"— fix the token definitions before generating.")
    # Some builds (e.g. the great-commission) keep a "STYLE PREFIX" to prepend to
    # each scene, with no token in the shot. If the prompt still lacks the style,
    # prepend it rather than aborting.
    if style and not re.search(r"hand-painted|painterly|animation|storybook|illustrat", prompt, re.I):
        prompt = style + " " + prompt
    # Hard style guard: the house style is hand-painted 2D. If no painterly cue
    # survived into the prompt, something dropped the style — never ship photoreal.
    if not re.search(r"hand-painted|painterly|animation|storybook|illustrat", prompt, re.I):
        sys.exit(f"ABORT {a.dir}/{a.shot}: prompt has no painterly style cue — refusing.")
    # Universal anti-panel / anti-duplicate tail — some builds' prompts omit it
    # and Nano Banana then tiles the scene or paints a figure twice. Append once.
    prompt += (" ONE SINGLE UNIFIED SCENE filling the whole tall vertical 9:16 frame,"
               " painted edge to edge as one continuous picture — NOT a diptych or"
               " triptych, no panels, no horizontal or vertical split, no stacked or"
               " side-by-side frames, no dividing line or border. Each person appears"
               " EXACTLY ONCE — no duplicated or repeated figures.")

    refs = []
    for c in [x.strip() for x in a.chars.split(",") if x.strip()]:
        try:
            slug = resolve(c) or c
        except Exception:
            slug = c  # variant/direct folder (aged-john, risen-jesus, …)
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
