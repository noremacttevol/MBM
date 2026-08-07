# QC / RUNNER HANDOFF — build-94-father-forgive-them (Luke 23:33-34)

## ✅ AUDIO FIX DONE — STALE-V1-FINAL recency lock cleared, HANDED TO PICTURE RUNNER (2026-08-06, Machine A `Dev`, headless AUDIO-FIX lane)

Class = STALE-V1-FINAL (recency), no open Cameron complaint (`v2_outline.py 94`). Parked
because the narration mp3s are newer than the V1 mp4 (2026-07-24), so the packet-copy AUDIO
LOCK would ship stale voices. Fix ($0, no new TTS): set `AUDIO_FROM_V1_SEGMENTS = True` in
beats_v2.py so the assembler rebuilds from this build's own 11 mp3 segments (present in the
V1 audio/ dir). 0 V2 stills → per PROMPT-AUDIO-FIX.md step 6, board → AUTHORED / Audio OK /
Ready ✅, claim cleared, picture runner assembles on the corrected audio. No Gemini spend.

Lesson-12 + complaint-corpus pass done 2026-08-05 (Machine A). `--check`
PASSES, zero WARNs. 12 beats, ~66 s.

## ⚠ HILL plate UNWIRED (fourth wrong-plate catch) — do NOT re-wire

The stash matched build-38's warm golden village frame by token name —
wrong world for Golgotha's bare rise under cold grey sky. IMPORTANT
TOOL TRAP: every `--wire` invocation RE-RUNS auto-wiring and will
re-add HILL from build-38 — if you run --wire on this build again,
re-remove HILL afterward (it is deliberately absent from PLACE_REFS).
HILL is promote-first from b01; its approved frame seeds rows 95/96 —
ONE Skull across the passion block.

## MERCIFUL DISTANCE (the row's rendering law — absolute)

The crucifixion is shown the way this build authored it: the three
crosses at DISTANCE, figures small, under a cold grey sky. NO close-up
of wounds, no nails driven, no blood detail, ever — the nearest
approach is the lifted face at mid-distance for the prayer. Any render
that closes in on gore is an automatic reject. The horror lives in the
dice game's obscene casualness (b06), not in wounds.

## The prayer (the row's center)

"Father, forgive them; for they know not what they do" — spoken OVER
the ones dividing his garments: the words and the dice game share the
geometry (b06/b09/b11: the reach of the prayer measured across every
figure on the hill — soldiers, mockers, watchers; the wide must hold
them all beneath it).

## Other checks

- SOLDIERS group ref wired from build-15 (the centurion's Romans —
  named recurring group exception, same legion look across the
  library; face-board the dice players against it).
- Garments: the CREAM robe among the divided clothing at the cross's
  foot — the one cream item, in the soldiers' hands (only-Jesus-
  wears-cream carried to its terrible endpoint).
- Cold grey light throughout; the sky heavy but not yet the darkness
  (that belongs to row 96).
- Direction: the watchers' gazes UP the rise; the dice players' DOWN
  at the dust — the contrast is the sermon.


## RUNNER PARK — NEEDS-AUDIO (A-auto 2026-08-06, $0 pre-flight)

Parked BEFORE any Gemini spend. `assert_v1_final_is_current` FAILS: this row's V1 mp4 was rendered 2026-07-24 but all 9 narration mp3s it would lock to are NEWER (2026-07-29) — copying that audio stream would ship stale voices / deleted segments (STALE-V1-FINAL class, same as rows 69/74/78/80/82/86-90).
- DURATION gate: within 1.0s (recency is the blocker).
Runner cannot fix (audio-immutability; needs an author edit to beats_v2.py).

**AUTHOR FIX:** add `AUDIO_FROM_V1_SEGMENTS = True` to this row's beats_v2.py, then the narration renders from the V1 build's own mp3s at the extract offsets — nothing re-voiced, nothing re-timed.

**RESUME (after the flag is set):** re-run the OPUS RUNNER loop on this row — it will pass pre-flight, generate stills, assemble (AUDIO LOCK), and ship.
