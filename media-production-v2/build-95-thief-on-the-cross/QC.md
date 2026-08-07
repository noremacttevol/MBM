# QC / RUNNER HANDOFF — build-95-thief-on-the-cross (Luke 23:39-43)

## ✅ AUDIO FIX DONE — STALE-V1-FINAL recency lock cleared, HANDED TO PICTURE RUNNER (2026-08-06, Machine A `Dev`, headless AUDIO-FIX lane)

Class = STALE-V1-FINAL (recency), no open Cameron complaint (`v2_outline.py 95`). Parked
because the narration mp3s are newer than the V1 mp4 (2026-07-24), so the packet-copy AUDIO
LOCK would ship stale voices. Fix ($0, no new TTS): set `AUDIO_FROM_V1_SEGMENTS = True` in
beats_v2.py so the assembler rebuilds from this build's own 11 mp3 segments (present in the
V1 audio/ dir). 0 V2 stills → per PROMPT-AUDIO-FIX.md step 6, board → AUTHORED / Audio OK /
Ready ✅, claim cleared, picture runner assembles on the corrected audio. No Gemini spend.

Lesson-12 + complaint-corpus pass done 2026-08-05 (Machine A). `--check`
PASSES, zero WARNs. 11 beats, ~60 s.

## ⚠ HILL UNWIRED (same wrong build-38 auto-wire as row 94)

Golgotha shares ONE Skull across rows 94/95/96: take row 94's approved
HILL frame once it exists (--take HILL=build-94...). The --wire tool
will re-add the wrong build-38 wire on every invocation — re-remove it
if you rerun wiring.

## Merciful distance (row 94's law binds here identically)

Crosses at distance, no wound detail, no gore, ever. The row's
closeness peaks at the two faces across the gap (b07) — faces, not
bodies.

## The three crosses (identity + geometry)

- The cross-LINE: Jesus CENTRE, the mocker on one side, the penitent
  THIEF on the other — the sides NEVER swap between frames (row-83
  class: b03's rebuke crosses IN FRONT of the silent centre; b07's
  request crosses the gap between centre and right; if the thief
  changes sides, the geometry lies).
- MOCKER and THIEF are distinct men per their locks (face-board);
  the thief's arc — mocking silenced → honest reckoning → the ask →
  "today" — plays entirely in his face at distance.
- "Remember me" / "To day shalt thou be with me in paradise": the
  exchange is two turned heads across the gap — the eye-line must
  CONNECT (row 92's look law, at the hardest angle in the library).

## Coverage shape

Two true wides with stated geometry: b01 (the three against the grey,
behind the watchers) and b03 (the rebuke — all three in one profile).
Three flips — the request (b07) is the tight heart.

- Grey morning throughout; SOLDIERS if visible follow row 94's
  build-15 group ref.
- Only Jesus wears cream — already stripped here; the divided robe
  belongs to row 94's dice frames, not this row.


## RUNNER PARK — NEEDS-AUDIO (A-auto 2026-08-06, $0 pre-flight)

Parked BEFORE any Gemini spend. `assert_v1_final_is_current` FAILS: this row's V1 mp4 was rendered 2026-07-24 but all 9 narration mp3s it would lock to are NEWER (2026-07-29) — copying that audio stream would ship stale voices / deleted segments (STALE-V1-FINAL class, same as rows 69/74/78/80/82/86-90).
- DURATION gate: within 1.0s (recency is the blocker).
Runner cannot fix (audio-immutability; needs an author edit to beats_v2.py).

**AUTHOR FIX:** add `AUDIO_FROM_V1_SEGMENTS = True` to this row's beats_v2.py, then the narration renders from the V1 build's own mp3s at the extract offsets — nothing re-voiced, nothing re-timed.

**RESUME (after the flag is set):** re-run the OPUS RUNNER loop on this row — it will pass pre-flight, generate stills, assemble (AUDIO LOCK), and ship.
