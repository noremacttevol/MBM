# QC — row 170, build-170-sacrament-worthily (The Sacrament, 1 Corinthians 11:23-28)

**Authored 2026-08-07, Machine A `Dev`, Fable-5 author lane, $0** (0 pictures
generated, 0 audio touched). `v2_prompt.py --check` PASS (24 beats, no warnings).
Windows contiguous + monotonic 0.280 → 119.402 (card_start), every segment onset
in-window. Audio column OK on AUTHOR-BOARD.

## COMPLAINT LEDGER
- **No open Cameron complaint on file** (`v2_outline.py 170` shows no prior
  reviewer lesson). Fresh authoring — the job is the LEARNING and COST laws in
  the positive.

## Two registers (the narration splits the video in half)
- **A) THE INSTITUTION at the Last Supper (b01-b09):** the upper room at NIGHT,
  lamplit; Jesus (the Master) present with his locked face; a few friends
  reclining (NOT the whole Twelve crowded in — movie coverage). `ROOM` + `MEAL`
  locks are **byte-identical to row 89** (build-89-last-supper) for cross-video
  consistency of the Last-Supper room.
- **B) THE ONGOING ORDINANCE + INVITATION (b10-b24):** later first-century
  believers at a plain `GATHERING` table — remembering, examining themselves,
  the covenant renewed, and a place kept open for "you." **No Jesus** in register
  B (every beat jesus=False; nobody in cream).

## Speaker law (NOT the usual red-letter — read this)
This is **Paul's epistle recounting** the supper. kv24 and kv25 quote Jesus's
institution words, BUT beats.json marks them the **SCRIPTURE voice** (Paul
handing it on) → their captions are **LIGHT-BLUE, not red**. The PICTURES still
show Jesus (jesus=True, ref=True, cream) because the event is the Last Supper and
he is physically there — the jesus flag drives the picture, the segment speaker
drives the caption colour. s26 and s28 are likewise SCRIPTURE (blue) and sit on
the believers. **There is NO Jesus-red and NO God-voice anywhere in this row** —
if the assembler paints kv24/kv25 red, that is a caption bug, not this map.

## Content-care (row 170 is GREEN in the flag table)
One restraint applies by spirit: **"remembering a sacrifice already made" (b14)
is a believer's REMEMBERING FACE with the bread and cup — NEVER a crucifixion,
cross, blood or wound image.** kv25 ("the new testament in my blood") shows only
the cup of dark wine, never blood. Scale gate on b01/b02: Jesus is
ordinary-sized among the reclining friends (no giant Master).

## Places + objects
- **ROOM** (upper room, night) — NEW place, byte-identical to row 89's lock.
  Runner PROMOTES from **b01**, wires the register-A beats (b01-b09).
- **GATHERING** (later believers' room) — NEW place, build-local lock. Runner
  PROMOTES from **b10**, wires the register-B beats (b10-b24).
- **MEAL** (Passover table) — byte-identical to row 89; on b01/b02 (the laid
  table). Small-object lock, carried by text.
- **ELEMENTS** (the loaf + two-handled clay cup) — build-local small-object lock,
  attached across both registers so the same bread and same cup read consistently
  in every insert. Carried by text — no plate.
- **BACKGROUND-CAST** (shared) — on the multi-figure beats for distinct faces
  (lesson 3), never twins.
- Jesus: locked V2 face + REF auto-attached by the jesus/ref flags on b01-b09;
  only Jesus wears cream.

## RUNNER — do this (paid picture lane; audio is DONE and untouched)
1. Confirm `--check` PASS on this machine. `v2_stash.py --scan` optional.
2. Generate **b01 first**, QC it, `v2_stash.py --promote build-170-sacrament-worthily ROOM <b01 asset>`; generate **b10**, QC it, `--promote … GATHERING <b10 asset>`; then generate the remaining 22 on the existing audio (Audio OK — do NOT re-voice; AUDIO LOCK byte-identical to V1).
3. **Face board (lesson 10):** Jesus is the locked V2 face across b01-b09. The
   friends/believers are distinct people (BACKGROUND-CAST), never twins.
   **Beard board (lesson 13)** on any recurring visible face.
4. **Scale gate (lesson 14)** on b01/b02 (Jesus ordinary-sized). **Restraint
   gate:** no cross/wound/blood anywhere (esp. b09, b12, b14).
5. Assemble (`v2_assemble.py` — AUDIO LOCK PASS required), technical gates,
   caption QC (bottom-band; **kv24/kv25/s26/s28 all light-blue scripture**,
   narrator default — verify kv24/kv25 are NOT red), publish to review.html, ship.
6. **Reroll budget ≤15% of 24 = ~3-4 beats.** Two failed rerolls → FIX-WAVE,
   keep best, move on. Log $/row + reroll % vs the $6.10 average. Expected cost
   ~24 × $0.20 ≈ $4.8 (all-new build).
