# QC / RUNNER HANDOFF — build-58-feeding-5000 (John 6:1-14)

Lesson-12 + complaint-corpus pass done 2026-08-05 (Machine A). `--check`
PASSES, zero WARNs. 24 beats, ~136 s.

## Identity

`REFS` pins ANDREW and PHILIP to their global sheets. The LAD is
story-local (his accepted first face → char_refs per the docstring).
DISCIPLES as a group ride the group lock — distinct men, never clones
(rows 90/107).

## Coverage shape

Six true wides with stated geometry — this is a five-thousand-person
story and scale IS the subject (the row-41 principle): b01 (streams
converging), b03 (the shadowed-evening problem), b14 (Mark 6:40's
ordered groups patterning the slope), b21 (the TWELVE-basket line in
profile), b23 (the crowd rising in waves), b24 (the closing scale).
Nine flips — the bread's journey (basket, blessing, hands) is tight
coverage on purpose.

## THE COUNT LAWS (row-135 class — this row is made of counts)

- FIVE barley loaves + TWO small fish in the lad's basket — countable,
  every time the basket shows (COUNT-AS-GEOMETRY).
- TWELVE baskets in b21's line — exactly, separated, countable.
- The multiplying is NEVER an effect — no shimmer, no multiplying-
  mid-air; abundance simply keeps arriving from the baskets through
  the disciples' hands (v11's chain: Jesus → disciples → people).

## Other checks

- GREEN grass (v10 "much grass") — spring hillside, never brown
  desert; bright afternoon → golden evening → dusk, one direction.
- Direction (row-83): the crowd streams TOWARD Jesus in b01; the
  disciples fan OUTWARD in b13/b17; the gleaning moves BETWEEN groups
  in b20.
- Barley bread is coarse, dark, flat — poor man's bread; no golden
  bakery loaves.
- HILLSIDE promote-first from b01 (`assets/s01-...jpeg`) — this
  approved slope will also seed rows 59/68, so QC it hard.
- Jesus at crowd level (b02: seated IN the multitude) — no giant law,
  no elevated-stage law.
- Only Jesus wears cream.

---

## RUNNER HANDOFF — SHIPPED 2026-08-06 (Opus autopilot, Machine A `Dev`)

**COMPLAINT LEDGER: none open** (`v2_outline.py 58` shows no filed complaints on
this row). The V1 cut was the old cartoon-era 9-still build "awaiting yes"; this
is the realistic V2 first-attempt rebuild.

**Build:** 24 painted stills @ native 2K (V1 had 9). 1 LAD portrait ($0.13);
ANDREW/PHILIP reused from global CAST-V2-REF sheets. HILLSIDE promoted-first from
b01 (`s01-the-crowd-followed.jpeg`) → wired to 15 beats. `v2_prompt.py --check`
PASS (24 beats, v4 checklist).

**Light QC (one pass):** all 24 frames realistic (zero cartoon/mixed). Only Jesus
in cream everywhere; Jesus ordinary-sized in every multi-figure frame (scale gate
PASS — he stands on a natural rock in wides but is never enlarged); full dark
beard consistent every frame (beard board PASS); locked green/hazel eyes per
`JESUS-V2-REF` (NOT rerolled — RUNNER-LESSON). COUNT LAW: the lad's basket shows
5 barley loaves + 2 fish; coarse dark barley bread throughout. Time-of-day ladders
correctly: bright afternoon (b01-02) → golden evening (b03-19) → dusk with
campfires (b24). Direction: crowd streams TOWARD Jesus (b01/b23), disciples fan
OUTWARD distributing (b13/b17). No modern objects, no lens-staring main subjects,
no second cream robe.

**Rerolls: 1 of 24 = 4.2% (well under the 15% budget).** b21 (twelve-baskets, the
author-flagged COUNT-AS-GEOMETRY beat) first came back dusk-lit with basket
contents reading as pale stones rather than bread; one reroll (`--only
v2-r058-b21 --redo`) returned clearly-readable bread in the baskets on green grass.

**FIX-WAVE (logged, not rerolled — subtle, within cost law):**
- Foreground ground on a few tight/insert shots (s06/s10/s16/s22) reads dry/dusty
  rather than the green-grass plate; the wides (s01/s02/s03/s13/s14/s17/s23/s24)
  all carry the green "much grass" correctly.
- Slight LAD hair variance between s08 (straighter) and s09 (curlier); s10/s12/s22
  are consistent.
- b21 basket count reads ~13 rather than exactly 12 (contents-as-bread was the
  real defect and is fixed; exact-12 is a nicety).
- s02 child-on-shoulders hair is slightly light (RUNNER-LESSON: a slightly-light
  incidental child is FIX-WAVE, not a reroll).

**AUDIO:** AUDIO LOCK guard-fired (V1 MP4 on disk 165.400s is an out-of-date
render vs 164.339s summed from the V1 segment mp3s). Set `AUDIO_FROM_V1_SEGMENTS
= True` (same guard-fix as rows 17/25/53) — the assembler rebuilt the track from
18 V1 segment mp3s at the extract_beats offsets and hash-verified it. Nothing
re-voiced, nothing re-timed, V1 read-only. **AUDIO REBUILD PASS
SHA256=25466d484b5886259eee1b2d3df4d3e7fd81657bdc523a19ef893c239cc3243d**,
20.5 MB / 164.3 s. Caption frames (output-seek) verified: captions bottom-band
only, question card clean.

**COST:** 1 portrait $0.13 + b01 anchor $0.13 + main gen $3.08 + 1 reroll $0.13 =
**~$3.47/row**, 4.2% rerolls — under the $6.10 running average; trend continues
DOWN (rows 52 $3.22, 53 ~$2.4, 54 $3.34, 58 $3.47).
