# AUDIT BRIEF — add Length + Narration reads to assigned PRESCRIPTION.md files

Repo root: `/home/noremacttevol/Desktop/MBM`. Work in `media-production/`.

## Read first, fully
1. `LENGTH-AND-NARRATION-LAW.md` — the standard you apply (Part A length, Part B narration).
2. `SPEAKER-LAW.md` — voice + caption colour rules (for the scripture-lift and cast checks).
3. `build-57-jairus-daughter/PRESCRIPTION.md` — the format/structure of a prescription.

## Per build in your assigned range
- Find the folder (glob `build-<n>-*` / `build-0<n>-*`, ignore `archive/` and
  `_stale-dupes/`). For #89 use build-89-the-last-supper; #86 the-wise-men; #44
  two-debtors; #71 the-great-commission; #128 build-128-heart-far-from-me;
  #133 build-133-what-jesus-called-hell; #134 build-134-today-in-paradise.
- Read that build's `make_narration.py` SEGMENTS **and** the mp4's real duration if a
  `.mp4` is present (`ffprobe -v error -show_entries format=duration -of csv=p=0 FILE`).
- **This is the ONLY source** — audit only what the narration actually says. Never
  invent lines or a scripture quote from memory; a scripture lift must be a line the
  narration is already PARAPHRASING (you name the KJV it becomes, but you are lifting
  an existing paraphrase, not adding new content).
- Judge LENGTH (Part A): does every second earn its place? Over-explaining the moral,
  repetition, editorializing, dead stretches → TRIM; rushed turns / no words under a
  needed beat → EXPAND; else KEEP. Most builds over ~200s ramble — check those hard.
- Judge NARRATION (Part B): flag narrator lines that explain the moral / tell us what
  to feel / ramble / break reverent tone. Find SCRIPTURE LIFTS (narrator paraphrasing
  a figure's actual words → lift to that voice in KJV, red/green/blue/pink). Confirm
  the cast + colours per SPEAKER-LAW.
- **APPEND** two sections to that build's existing `PRESCRIPTION.md` (do not touch the
  sections already there), exactly:

```markdown
## Length read
Verdict: KEEP ~Ns  /  TRIM to ~Ns — cut <what> (<why>)  /  EXPAND — <what>
<one or two sentences of evidence from the actual narration>

## Narration read
- Narrator fixes: <seg id → cut/tighten/rephrase, or "clean">
- Scripture lifts: <seg → "paraphrase" → KJV line → SPEAKER/colour>, or "none available"
- Cast/colour: <missing voice or colour fix, or "correct">
```

You write the SPEC of needed changes — do NOT edit make_narration.py or any audio.

## When done
Reply with a plain list: each build number → `KEEP` / `TRIM` / `EXPAND` for length,
and the count of scripture-lifts found. Nothing else.
