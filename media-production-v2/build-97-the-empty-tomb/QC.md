# QC / RUNNER HANDOFF — build-97-the-empty-tomb (Luke 24:1-8)

## ✅ AUDIO FIX DONE — STALE-V1-FINAL recency lock cleared, HANDED TO PICTURE RUNNER (2026-08-06, Machine A `Dev`, headless AUDIO-FIX lane)

Class = STALE-V1-FINAL (recency), no open Cameron complaint (`v2_outline.py 97`). Parked
because the narration mp3s are newer than the V1 mp4 (2026-07-24) and |Δ|>1.0, so the
packet-copy AUDIO LOCK would ship stale voices. Fix ($0, no new TTS): set
`AUDIO_FROM_V1_SEGMENTS = True` in beats_v2.py so the assembler rebuilds from this build's
own 13 mp3 segments (present in the V1 audio/ dir). 0 V2 stills → per PROMPT-AUDIO-FIX.md
step 6, board → AUTHORED / Audio OK / Ready ✅, claim cleared, picture runner assembles on
the corrected audio. No Gemini spend.

Lesson-12 + complaint-corpus pass done 2026-08-05 (Machine A). `--check`
PASSES, zero WARNs. 12 beats, ~65 s.

## THE TOMB — Jesus's own (row 71's law)

This is JESUS's garden tomb: NOT the Lazarus/parable cave (rows
17/37). Take row 71's promoted TOMB frame if it exists (its b12 sealed
frame is the same tomb one row earlier in time); else promote-first
here from b03's first good rock-face frame — and rows 96/98 share it.
NEVER --take the build-37 tomb the stash will offer by token name.

## The empty tomb (rendering laws)

- The stone stands ROLLED ASIDE from b05 on; the interior holds the
  FOLDED grave clothes (the linen lying, the napkin apart — if an
  interior frame renders, those two items and nothing else).
- NO risen Jesus appears in this row (Luke 24:1-8 — the absence IS
  the message; his appearing belongs to row 98). Any Jesus figure in
  a render is an automatic reject.
- The TWO in shining garments follow row 85's angel canon EXACTLY:
  real plain-robed figures, silver-grey shining like dawn cloth —
  wingless, unhaloed, feet on ground.

## Coverage shape

Three true wides with stated geometry: b01 (the dark walk in
profile), b04 (the disproportion — camera behind the three climbing
backs toward the rock face; the stone problem stated as scale), b12
(the emergence into the risen morning from the side). Four flips.

## Other checks

- THREE women (count law), spice jars in hand on the walk IN —
  and still carried, forgotten, on the run OUT (the detail that
  sells the turn).
- Arc of light: pre-dawn dark → first grey → risen morning — one
  direction, the light itself telling the story.
- Direction (row-83): up the path IN; out of the mouth and DOWN the
  path OUT — b12's emergence vector opposes b01's approach.
- WOMEN: distinct (Magdalene among them — her canonical face, if row
  98 builds first, anchors here; the three-Marys law holds: she is
  neither Bethany-Mary nor the mother).


## RUNNER PARK — NEEDS-AUDIO (A-auto 2026-08-06, $0 pre-flight)

Parked BEFORE any Gemini spend. `assert_v1_final_is_current` FAILS: this row's V1 mp4 was rendered 2026-07-24 but all 9 narration mp3s it would lock to are NEWER (2026-07-29) — copying that audio stream would ship stale voices / deleted segments (STALE-V1-FINAL class, same as rows 69/74/78/80/82/86-90).
- DURATION gate: timeline vs V1 mp4 |Δ|=1.92s (>1.0).
Runner cannot fix (audio-immutability; needs an author edit to beats_v2.py).

**AUTHOR FIX:** add `AUDIO_FROM_V1_SEGMENTS = True` to this row's beats_v2.py, then the narration renders from the V1 build's own mp3s at the extract offsets — nothing re-voiced, nothing re-timed.

**RESUME (after the flag is set):** re-run the OPUS RUNNER loop on this row — it will pass pre-flight, generate stills, assemble (AUDIO LOCK), and ship.
