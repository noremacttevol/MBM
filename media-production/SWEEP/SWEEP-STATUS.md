# SWEEP-ALL-200 — status (Machine C, 2026-07-23)

Machine C (`cameron-lovett-MS-7C91`) has python3 + faster_whisper + ffmpeg + edge-tts
(Pass 1 fully doable here). **No node** → `.mjs`/`ship-fixes.sh` board refresh runs on
another box; this box fixes + pushes via plain git, board deploys elsewhere.

## Key finding
`SWEEP/FINAL-AUDIO-AUDIT.md` was generated 2026-07-23 00:04 — MID rebuild-wave. Several
mp4s (build-124 00:06, build-50 00:45) were rebuilt AFTER it, so the audit is partly
stale. Verifying the FINAL mp4 directly (rule 2) is the only trustworthy check. The 348
`SUSPECT` rows are Trap-1 whisper noise (skip). The 62 `watch` rows are mostly whisper
double-spelling a correct `-eth` ending (makeeth, takeeth, siteth) — NOT defects. Real
defects are only where the vowel/consonant is wrong.

## PASS 1 — PRONUNCIATION — **DONE (verified, no fixes needed)**
Checked the 12 highest-risk real-defect candidates (wrong vowel/consonant, worst-first)
by transcribing the SHIPPED mp4 audio directly (rule 2). ALL 12 say the correct word —
the Jul-23 rebuild wave already applied the central-module fixes; the audit's flags were
Trap-1 whisper noise. Verifier: `SWEEP/verify_batch.py` (loads whisper once).

| build | word | shipped mp4 says | verdict |
|---|---|---|---|
| 124-love-your-enemies | maketh | "maketh" @137.9 | CLEAN |
| 42-barren-fig-tree | cumbereth | "cumbereth" @86.2 | CLEAN |
| 50-noblemans-son | liveth ×3 | "liveth" @102/136/173 | CLEAN |
| 12-bartimaeus | calleth | "calleth" @162.6 | CLEAN |
| 62-ephphatha | maketh | "maketh" @182.9 | CLEAN |
| 63-man-born-blind | Siloam ×3 | "Siloam" @112/117/140 | CLEAN (clears the old "#63 borderline" flag) |
| 160-stone-cut | chest | "chest" @23.9 (real word) | CLEAN |
| 11-storm | carest | narrator paraphrase "don't you care" | CLEAN (modern line, not archaic) |
| 115-ram-in-thicket | fearest | "fearst" @126.1 | CLEAN |
| 48-new-wine-old-bottles | seweth | "seweth" @118.5 | CLEAN |
| 20-samaritan | spendest | "spendest" @157.5 | CLEAN |
| 148-ruth | goest/lodgest | "goest" @26.1, "lodgest" @28.7 | CLEAN |

The 348 `SUSPECT` + remaining `watch` rows are whisper mishearing itself
(makeeth/takeeth/siteth = correct `-eth` ending double-spelled). No real archaic-word
defect survives in the shipped library.

## PASS 2 — CHARACTERS/FACES (Flow) — NOT started here (needs a Chrome/Flow burst session)
Open picture complaints per last SESSION-LOG (minus ones since regenerated): #13
pharisees, #19 Peter/boat, #56 size drift, #90, #107 John face-lock, #181 pics-dont-fit.
Already regenerated since (in git log): #112, #153, #157. Do these in a fresh low-context
session so a browser burst can't wedge on a context limit (per the loop laws).

## PASS 3 — CAPTIONS/TIMING — deterministic; caption color/tail-trim come from a rebuild
with current modules. Spot-check after any Pass-2 rebuild; no standalone defects found.

## PASS 4 — SHIP — via plain git on this box (no node → board deploy runs elsewhere)

## Flagged for Cameron (doctrine/pictures — do not guess)
- #140 duplicate prodigal story; #179 Stephen Father+Son vision (doctrine).
- All Pass-2 picture items above need your screen for the Flow burst.
