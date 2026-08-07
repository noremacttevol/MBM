# QC / RUNNER HANDOFF — build-96-it-is-finished (John 19:30 / Matt 27:51)

## ✅ AUDIO FIX DONE — STALE-V1-FINAL recency lock cleared, HANDED TO PICTURE RUNNER (2026-08-06, Machine A `Dev`, headless AUDIO-FIX lane)

Class = STALE-V1-FINAL (recency), no open Cameron complaint (`v2_outline.py 96`). Parked
because the narration mp3s are newer than the V1 mp4 (2026-07-24) and |Δ|>1.0, so the
packet-copy AUDIO LOCK would ship stale voices. Fix ($0, no new TTS): set
`AUDIO_FROM_V1_SEGMENTS = True` in beats_v2.py so the assembler rebuilds from this build's
own 14 mp3 segments (present in the V1 audio/ dir). 0 V2 stills → per PROMPT-AUDIO-FIX.md
step 6, board → AUTHORED / Audio OK / Ready ✅, claim cleared, picture runner assembles on
the corrected audio. No Gemini spend.

Lesson-12 + complaint-corpus pass done 2026-08-05 (Machine A). `--check`
PASSES, zero WARNs. 13 beats, ~73 s.

## Plates

- HILL UNWIRED (the recurring wrong build-38 auto-wire — rows 94/95's
  note applies): take row 94's approved HILL — one Skull across the
  passion block. Re-remove HILL if --wire reruns.
- TEMPLE wired from build-06 (the temple family) — the VEIL frames
  layer the great blue-purple-scarlet veil onto that architecture per
  the beat prose.

## The death (merciful distance, held to the end)

- The darkness (Matt 27:45) governs the hill beats: a darkened sky at
  midday — heavy unnatural gloom, NEVER night-with-stars and never a
  sunset (time-of-day law at its most doctrinal).
- The bowed head (b07) is the death frame: at distance, the head
  lowering — no death-agony close-up, no wound detail, ever.
- "It is finished" is a VICTORY declaration — the hill's stillness at
  b05 reads as something COMPLETED, not merely ended.

## THE VEIL (the row's second act — exactness laws)

- Torn TOP DOWN (Matt 27:51 "from the top to the bottom") — the split
  begins at the TOP in any mid-tear frame; a bottom-up tear is a
  scripture error, reject.
- The veil is the great blue-purple-scarlet hanging; behind it the
  Holy of Holies shows as DARK OPEN SPACE — never a depicted ark or
  furniture (content-care: no invented sacred objects).
- The duty PRIEST's terror (b10) is awe-fear, human; lamplight only.
- b13's closing (the veil hanging open in two halves, the way open)
  is the doctrine as architecture.

## Coverage shape

Two true wides with stated geometry: b05 (the declaration over the
whole dark hill) and b13 (the opened veil down the hall's length).
Five flips.


## RUNNER PARK — NEEDS-AUDIO (A-auto 2026-08-06, $0 pre-flight)

Parked BEFORE any Gemini spend. `assert_v1_final_is_current` FAILS: this row's V1 mp4 was rendered 2026-07-24 but all 9 narration mp3s it would lock to are NEWER (2026-07-29) — copying that audio stream would ship stale voices / deleted segments (STALE-V1-FINAL class, same as rows 69/74/78/80/82/86-90).
- DURATION gate: timeline vs V1 mp4 |Δ|=2.86s (>1.0).
Runner cannot fix (audio-immutability; needs an author edit to beats_v2.py).

**AUTHOR FIX:** add `AUDIO_FROM_V1_SEGMENTS = True` to this row's beats_v2.py, then the narration renders from the V1 build's own mp3s at the extract offsets — nothing re-voiced, nothing re-timed.

**RESUME (after the flag is set):** re-run the OPUS RUNNER loop on this row — it will pass pre-flight, generate stills, assemble (AUDIO LOCK), and ship.
