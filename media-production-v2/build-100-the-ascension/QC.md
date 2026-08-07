# QC / RUNNER HANDOFF — build-100-the-ascension (Acts 1:6-12)

## ✅ AUDIO FIX DONE — STALE-V1-FINAL recency lock cleared, HANDED TO PICTURE RUNNER (2026-08-06, Machine A `Dev`, headless AUDIO-FIX lane)

Class = STALE-V1-FINAL (recency), no open Cameron complaint (`v2_outline.py 100`). Parked
because all narration mp3s are newer than the V1 mp4 (2026-07-24) and |Δ|>1.0, so the
packet-copy AUDIO LOCK would ship stale voices. Fix ($0, no new TTS): set
`AUDIO_FROM_V1_SEGMENTS = True` in beats_v2.py so the assembler rebuilds from this build's
own 10 mp3 segments (present in the V1 audio/ dir). 0 V2 stills → per PROMPT-AUDIO-FIX.md
step 6, board → AUTHORED / Audio OK / Ready ✅, claim cleared, picture runner assembles on
the corrected audio. No Gemini spend.

Lesson-12 + complaint-corpus pass done 2026-08-05 (Machine A). `--check`
PASSES, zero WARNs. 17 beats, ~98 s.

## THE ASCENT (the library's most effect-prone frame — laws exact)

- b11 "taken up while they beheld": Jesus risen BODILY a man's height
  above the grass — feet clear of the ground, robe hanging natural,
  NO light beams, NO glow, NO streaks of motion; gravity simply
  released. The beholding ring's upturned faces carry the wonder.
- b12 the CLOUD receives him — a great bright cloud, weather-real
  (the rows 67/85 cloud law): he is hidden BY it, not dissolved.
- The TWO in white apparel follow the row-85 angel canon exactly.
- The eleven (count law — never twelve) throughout.

## Coverage shape

Four true wides with stated geometry: b01 (the ring from behind the
nearest shoulders), b05 (the commission swept over the REAL landscape
— Jerusalem near, Judea beyond, the world's haze at the horizon:
geography as doctrine), b11 (the ascent behind the beholding backs),
b17 (the descent toward the city — joy, not loss, per Luke 24:52).
Seven flips.

## Other checks

- MOUNT is Olivet's crown — the same mount family as row 71's
  commission summit? NO: row 71 is Galilee's mountain (Matt 28), this
  is OLIVET by Jerusalem (Acts 1:12) — two different mountains; do
  not share plates (the wrong-plate class).
- "Why stand ye gazing up?" (b13-b15): the two messengers' arms lift
  toward the cloud — the gaze redirect is the beat's geometry.
- Direction (row-83): UP for the ascent (the one vertical vector in
  the library), then DOWN the slope toward the in-frame city for the
  close — the two vectors bookend the row.
- Morning light; the cloud bright, the sky otherwise ordinary.
- MOUNT promote-first from b01; ELEVEN/TWO are cast — no plates.
- Only Jesus wears cream — the last cream frame of the ministry.


## RUNNER PARK — NEEDS-AUDIO (A-auto 2026-08-06, $0 pre-flight)

Parked BEFORE any Gemini spend. `assert_v1_final_is_current` FAILS: this row's V1 mp4 was rendered 2026-07-24 but all 9 narration mp3s it would lock to are NEWER (2026-07-29) — copying that audio stream would ship stale voices / deleted segments (STALE-V1-FINAL class, same as rows 69/74/78/80/82/86-90).
- DURATION gate: timeline vs V1 mp4 |Δ|=19.02s (>1.0).
Runner cannot fix (audio-immutability; needs an author edit to beats_v2.py).

**AUTHOR FIX:** add `AUDIO_FROM_V1_SEGMENTS = True` to this row's beats_v2.py, then the narration renders from the V1 build's own mp3s at the extract offsets — nothing re-voiced, nothing re-timed.

**RESUME (after the flag is set):** re-run the OPUS RUNNER loop on this row — it will pass pre-flight, generate stills, assemble (AUDIO LOCK), and ship.
