# QC / RUNNER HANDOFF — build-98-mary-her-name (John 20:11-18)

Lesson-12 + complaint-corpus pass done 2026-08-05 (Machine A). `--check`
PASSES, zero WARNs. 21 beats, ~121 s.

## TOMB UNWIRED (fifth wrong-plate catch — the parable-tomb trap again)

The stash keeps offering build-37's parable tomb by token name. This is
JESUS'S garden tomb — the rows 71/96/97 family. Take row 97's approved
frame; re-remove the build-37 wire if --wire reruns.

## MARY MAGDALENE (the third Mary — her canon starts here or in 97)

Madder-red per her lock — distinct from Bethany-Mary (dusty-indigo,
CAST-V2 sheet exists now) and the mother (indigo-blue veil). Whichever
of rows 97/98 builds first sets Magdalene's canonical face; the other
anchors. Never cross the three Marys.

## The risen Jesus (rendering law)

NATURAL — cream robe, warm, real; NO wounds shown, no shining, no
glow: the whole story turns on him being mistakable for the gardener
(b04-b07), so he must look like a MAN in a garden. Recognition comes
from her, not from effects.

## The recognition (b12 — the row's heart, kept TIGHT)

One word — her name — and she turns: the frame is her face blazing
alive mid-turn. "RABBONI." If the render gives a generic joyful
reunion instead of the mid-turn instant, reroll.

## The touch-me-not (b16 — gentleness law)

His raised hand is SOFT between them — a gentle hold, never a rebuff;
her reaching arms and his tenderness share the frame. Any cold or
rejecting render fails.

## Coverage shape

Three true wides with stated geometry: b01 (the stayer — figure and
doorway from the side), b10 (the love measured — both figures in one
profile), b14 (the flip — camera behind her rushing shoulder). Seven
flips including b20's LONE full-stride run (phantom trap).

- Direction (row-83): she faces the tomb; turns BACK to him; runs
  TOWARD the city at the send — three pivots, each readable.
- Early gold → full clear morning, one direction.
- Only Jesus wears cream.


## RUNNER PARK — NEEDS-AUDIO (A-auto 2026-08-06, $0 pre-flight)

Parked BEFORE any Gemini spend. `assert_v1_final_is_current` FAILS: this row's V1 mp4 was rendered 2026-07-24 but all 9 narration mp3s it would lock to are NEWER (2026-07-29) — copying that audio stream would ship stale voices / deleted segments (STALE-V1-FINAL class, same as rows 69/74/78/80/82/86-90).
- DURATION gate: timeline vs V1 mp4 |Δ|=1.02s (>1.0).
Runner cannot fix (audio-immutability; needs an author edit to beats_v2.py).

**AUTHOR FIX:** add `AUDIO_FROM_V1_SEGMENTS = True` to this row's beats_v2.py, then the narration renders from the V1 build's own mp3s at the extract offsets — nothing re-voiced, nothing re-timed.

**RESUME (after the flag is set):** re-run the OPUS RUNNER loop on this row — it will pass pre-flight, generate stills, assemble (AUDIO LOCK), and ship.
