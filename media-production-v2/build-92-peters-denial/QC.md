# QC / RUNNER HANDOFF — build-92-peters-denial (Luke 22:54-62)

Lesson-12 + complaint-corpus pass done 2026-08-05 (Machine A). `--check`
PASSES, zero WARNs. 10 beats, ~40+ s (short row).

## ⚑ OPEN COMPLAINT ON THIS EXACT ROW (Cameron): "Old voice still"

REDO-ALL law: verify the assembled MP4's encoded audio is the verified
new-voice source (the board's Audio column says OK from the audit, but
the complaint means the V1 cut on the reviewer was old-voice — this V2
build must be checked on the RENDERED product before the card goes up).

## Coverage shape

Two true wides with stated geometry: b01 (the fire in the midst —
camera behind the fire-ring's backs) and b07 (THE LOOK — both poles in
one profile: Jesus under guard on the porch, Peter at the fire; the
axis of the whole story). Three flips.

## The look (b07 — the row's soul)

The eye-line between Jesus and Peter must CONNECT across the yard —
both faces visible, the gaze geometry unmistakable (Cameron's Peter
class in its purest form: if the look doesn't land, the story doesn't
exist). No anger in Jesus's face — the look that breaks Peter is
knowing sorrow.

## Other checks

- PETER carries his global sheet — face-board; his arc (warming
  himself → lying → frozen → weeping out the gate) is one man's face
  collapsing by stages.
- The MAID and accusers distinct (90/107); firelight only (period
  flame law); the cock is HEARD, not necessarily shown — if shown,
  one rooster on a wall, dawn-grey sky hint.
- Direction: b09 he stumbles OUT through the arched gate into the
  dark — away from the fire's light (the geometry of shame).
- Night → first grey of dawn across the row, one direction.
- Only Jesus wears cream — visible under guard on the porch.
- YARD promote-first from b01.


## RUNNER PARK — NEEDS-AUDIO (A-auto 2026-08-06, $0 pre-flight)

Parked BEFORE any Gemini spend. `assert_v1_final_is_current` FAILS: this row's V1 mp4 was rendered 2026-07-24 but all 9 narration mp3s it would lock to are NEWER (2026-07-29) — copying that audio stream would ship stale voices / deleted segments (STALE-V1-FINAL class, same as rows 69/74/78/80/82/86-90).
- DURATION gate: timeline vs V1 mp4 |Δ|=14.12s (>1.0).
Runner cannot fix (audio-immutability; needs an author edit to beats_v2.py).

**AUTHOR FIX:** add `AUDIO_FROM_V1_SEGMENTS = True` to this row's beats_v2.py, then the narration renders from the V1 build's own mp3s at the extract offsets — nothing re-voiced, nothing re-timed.

**RESUME (after the flag is set):** re-run the OPUS RUNNER loop on this row — it will pass pre-flight, generate stills, assemble (AUDIO LOCK), and ship.
