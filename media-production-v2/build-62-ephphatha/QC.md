# QC / RUNNER HANDOFF — build-62-ephphatha

Complaint-gate addendum, 2026-08-05 (Machine A).

## OPEN CAMERON COMPLAINT — gates before build

"He lost his beard in one of the pictures."
BEARD BOARD (rubric lesson 13): every bearded recurring man — the
deaf man, Jesus, the friends — keeps his exact beard in every frame.
Step through every frame checking ONLY beards before assembly; one
appearing/disappearing/shrinking beard = reject that still.

## RUNNER SHIP — 2026-08-07, Machine A `Dev` (AUTHOR-BOARD row 62 resume)

Resumed a strand that DIED mid-build (State RUNNING / A-auto, 14/34 assets,
no committed mp4, no live `v2_gen_api` process → safe resume). Ran the
RUNNER-LESSONS already-shipped check first: no committed mp4 and the v62
review card was still the OLD V1 card (no `realistic-v2` wave) → NOT shipped,
resume authorized. `v2_prompt.py --check` v4 PASS. 0 portraits due (deafman.jpeg
already made). DEAFMAN wired in `REFS` → `CAST-REF-V2/deafman.jpeg` (the
structural fix for the beard complaint — a text lock alone does not hold a
face/beard; lessons 52/55).

Generated the remaining 20 beats (b15–b34), $2.68 this run, meter $419.55→$422.23,
under ceiling $449. **0 rerolls (0% of 34 beats — clean first attempt).**

### COMPLAINT LEDGER
- **OPEN — "He lost his beard in one of the pictures."** FIXED. Beard-boarded
  the deaf man across every legible frame he appears in (s05, s09, s11–s21,
  s24–s26, s30, s31, s33, s34): he carries the SAME close-trimmed dark beard +
  short dark hair in every frame — verified at full resolution on the two
  tightest close-ups (s18, s21) and the mid-shots (s09, s24, s34). The
  wired `REFS["DEAFMAN"]` image anchors his identity so the beard cannot drop
  the way it did in the V1 cut. Jesus and the friends (s29 elders, s30/s31)
  also keep consistent beards.

### LIGHT-QC PASS (all 34 frames, one pass)
- Jesus: one locked face, cream-only robe (no second cream figure anywhere),
  no halo/glow, warm brown eyes (NO pale-green stare — checked s21/s33
  close-ups), ordinary scale in the s32 aerial ring.
- No modern objects (s32 aerial = period sail-boats + dirt path, NOT a paved
  road; s29/s31/s34 skies clean, no thin utility wire), no collage/panel,
  no cartoon/CGI mix (Law 14 — all photographic), no lens-stares, anatomy
  and hand-counts correct (s31 three-man embrace, s33 raised hands).
- Decapolis Greco-Roman columns are period-correct for the ten Gentile cities.

### ASSEMBLY
`v2_assemble.py 62` → **AUDIO LOCK PASS** SHA256
`6786984813c4fe3bc99ed58b8e45f154484e11b1b5f5d19c0bcf384cdd8d3634`,
mark-7_ephphatha.mp4, 21.0 MB, 202.8s. Caption frames (output-seek) at 30s /
120s / 200s: captions in the bottom band only, in sync; question card clean
("He does not heal for an audience…"), correct margins, no glyph squares.

## C-FIX SHIP — 2026-08-07, Machine A `Dev` (AUTHOR-BOARD row 62, UNATTENDED/HEADLESS)

New OPEN Cameron complaint on the SHIPPED cut:
> "0:18 picture is bad it has someones eyes messed up"

DIAGNOSIS: the 0:18 still is `s03-now-they-come-running.jpeg` (beat
`v2-r062-b03`, window 14.59–22.76, on screen at t=18s under the caption "Last
time Jesus was on this side of the sea, the people asked him to leave"). The
old man at frame-left had a white AI smear across his eye sockets — a garbled
eye render. Confirmed at full res before touching anything.

FIX (touch-once, single frame): rerolled ONLY b03
(`v2_gen_api.py --only v2-r062-b03 --redo --ceiling 525`). Every other frame
byte-identical. New take: the old man and every legible face carry clean,
correctly-rendered eyes; Jesus is the ONLY cream robe (checked the center-back
crowd — muted tan working tunics, no second cream figure); no modern objects,
no collage, all photographic; the larger "whole neighborhood" crowd fits the
narration ("Now they come running… the whole neighborhood"). 1 reroll on a
34-beat row = 3% (inside the ≤15% budget). $0.13 this run, meter $498.61→$498.75.

### COMPLAINT LEDGER (C-FIX)
- **OPEN — "0:18 picture is bad it has someones eyes messed up."** FIXED.
  s03 rerolled; the old man's garbled eyes are gone, all faces clean-eyed.
  Verified in the RENDERED mp4 at t=18s (extracted frame), not just the still.

### RE-ASSEMBLY
`v2_assemble.py 62` → **AUDIO LOCK PASS** SHA256
`6786984813c4fe3bc99ed58b8e45f154484e11b1b5f5d19c0bcf384cdd8d3634` — IDENTICAL
to the prior ship: narration/voices/timing untouched, audio byte-identical.
mark-7_ephphatha.mp4, 21.0 MB, 202.8s.
