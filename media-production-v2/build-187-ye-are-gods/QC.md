# QC / RUNNER HANDOFF — build-187-ye-are-gods (John 10:31-36, Psalm 82:6)

**Authored 2026-08-07 (Machine A `Dev`, Fable-5 author lane, $0).** 15-beat V2 map,
`v2_prompt.py --check` PASS (0 warnings), windows contiguous+monotonic 0.000→64.415=card,
every speech onset in-window, audio OK (default stream-copy).

## COMPLAINT LEDGER (LEARNING LAW)
`v2_outline.py 187` shows **NO open complaint.** Nothing to answer.

## The story / speaker law
Jesus in the temple court answers the leaders who took up stones by quoting their own
Psalm.
- **j1 = GOD-voice → GREEN caption** (the Psalm's own "I have said, Ye are gods…"), but
  **GOD IS NEVER SHOWN** — it is the SCRIPTURE Jesus reads aloud from their scroll. b04/b05
  picture Jesus reading/declaring it (jesus=True); the green caption sits over that, no God
  figure (row-169 pattern).
- **j2 = Jesus's own words → RED caption** on Jesus's face (b08/b09/b10).
- Everything else is the narrator (white).

## HARD GATES
- **GOD / THE FATHER IS NEVER EMBODIED.** j1 (the Psalm) and every "the Father" line
  (n2/j2/n2b) are carried by JESUS himself — the one the Father set apart and sent,
  embodied before them — and by the written scroll, NEVER by a figure, throne, hand, beam
  or rays. No dove/triangle/all-seeing-eye/Trinitarian symbol. Only embodied divine person
  = Jesus the Son.
- **CONTENT-CARE:** this is a DISPUTE OVER SCRIPTURE, not a lynching. A few leaders may
  hold loose stones low at the far edge of the b01 wide (John 10:31), but NO stone is ever
  raised, NO violence, NO blood, NO cornered/cowering Jesus. Jesus is calm and unafraid
  throughout.
- No halo/ring/rim-light (drift-word gate). Warm plain daylight (winter feast — not sunset).

## Places
- **TEMPLE-COURT** — shared/global lock, all 15 beats. **Reusable plate in the stash**
  (build-39 / build-173 both carry PLACE-REF/temple-court.jpeg). RUNNER: run
  `python3 media-production-v2/v2_stash.py --wire build-187-ye-are-gods` (`--scan` first if
  the index is stale) and `--take` the SUGGESTED temple-court plate so it copies into
  PLACE-REF/ and records into PLACE_REFS. **No NEW place to promote in this row.**
- **BACKGROUND-CAST** — shared lock, on the b01 wide only.

## Cast locks
- **LEADERS** — build-local text lock: the hostile fine-robed religious rulers; distinct
  recognizable men (not a mob of twins), same faces across b01/b04/b05/b07/b09/b13/b15.
  Beard-board + face-board them.
- **Jesus** — injected on all 15 beats; JESUS-MASTER-REF + LOCK v5; only he wears cream;
  `jesus_face_gate.py` must exit 0 on the build.

## Runner steps
1. `v2_stash.py --wire build-187-ye-are-gods` → `--take` the temple-court plate.
2. Generate all 15 stills at native 2K. Reroll budget ≤15% of 15 (≈2 beats).
3. Gates: face-board + beard-board (Jesus across all 15; LEADERS across their beats);
   scale gate (Jesus ordinary-sized, within natural height of the leaders); only-Jesus-cream;
   realistic Law 14; GOD-never-embodied on every beat (esp. b04/b05 j1-green + b07/b08/b12
   "Father" lines); content-care on b01/b09 (no raised stone, no violence); caption QC
   (b04/b05 GREEN god-voice, b08/b09/b10 RED jesus, rest white; bottom band; card clean).
4. Assemble with `v2_assemble.py` (AUDIO LOCK stream-copy, byte-identical — do NOT
   re-voice). Verify final ≈ 70.8s, tail/card intact.
5. Ship with a review card stating the realistic-V2 build (no open complaint).
