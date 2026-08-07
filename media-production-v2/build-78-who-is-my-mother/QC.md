# QC / RUNNER HANDOFF — build-78-who-is-my-mother (Mark 3:31-35)

## ✅ AUDIO FIX DONE — AUDIO-FIX session, Machine A, 2026-08-06 ($0)

**STALE-V1 audio-lock CLEARED.** Added `AUDIO_FROM_V1_SEGMENTS = True` to
beats_v2.py. The V1 mp4 `media-production/build-78.../mark-3_who-is-my-mother.mp4`
(09:47) is older than all 11 re-voiced segment mp3s (2026-07-29 23:03), so
`assert_v1_final_is_current` (recency tripwire) refused to copy its stale AAC —
the same class as the shipped row-69 fix. With the flag set, v2_assemble
rebuilds the narration from the V1 build's OWN 11 new-voice mp3s at the
extract_beats offsets — nothing re-voiced, nothing re-timed, V1 stays read-only.

**Segment parity 11/11 exact** (n0, n1a, n1b, n1c, s32, j1, n2, j2, j3, n3,
card) across make_narration.py ↔ media-production-v2 audio ↔ V1 build audio.

**Validated:** `python3 v2_assemble.py 78` now clears the audio gate and stops
only on "missing picture … row not fully generated" (0 V2 stills) — i.e. the
STALE-V1 AUDIO LOCK no longer fires. `v2_prompt.py 78 --check` PASSES (12 beats).

**No visual ship** (0 stills, no ElevenLabs, $0). Board: NEEDS-AUDIO →
AUTHORED / Audio OK / Ready ✅, claim cleared → the picture runner generates
stills and assembles on the corrected (new-voice) audio. RESUME below still
applies.

---

## RUNNER PARK — NEEDS-AUDIO (A-auto 2026-08-06, $0 spent, 0 credits) — RESOLVED ABOVE

Pre-flighted the stale-V1 AUDIO LOCK at step 2 BEFORE any generate (row-74
lesson). GENUINELY STALE: V1 `mark-3_who-is-my-mother.mp4` rendered
2026-07-24 10:15:29, but all 11 locked mp3s are NEWER (2026-07-28 14:27:49);
timeline total=72.61s vs V1 mp4 dur=77.79s (excess=+5.18s).
`assert_v1_final_is_current` REFUSES → shipping it would carry stale voices.

Runner cannot fix: the assembler's own hint is to set
`AUDIO_FROM_V1_SEGMENTS = True` in this row's beats_v2.py, which is an AUTHOR
audio decision (editing beats_v2.py is outside runner writes; audio-immutability
law). No stills generated — this parks at $0.

**AUTHOR FIX:** set `AUDIO_FROM_V1_SEGMENTS = True` in beats_v2.py (renders
narration from the V1 build's OWN mp3s at extract_beats offsets — nothing
re-voiced/re-timed) OR re-render the V1 mp4. Then set Ready ✅ / Audio OK.
**RESUME (after author fix):** `python3 media-production-v2/v2_story_cast.py build-78-who-is-my-mother`
then `v2_gen_api.py build-78-who-is-my-mother --ceiling …` then `v2_assemble.py 78`.


Lesson-12 + complaint-corpus pass done 2026-08-05 (Machine A). `--check`
PASSES, zero WARNs. 12 beats, ~66 s — a short row.

## THREE-MARYS LAW (from row 49's QC — applies here)

The MOTHER outside is Mary the mother of Jesus. If row 49
(water-to-wine) has an approved mother-Mary frame by build time,
REFS-anchor this row's MOTHER to it; if this row builds first, ITS
approved frame becomes the canon and row 49 + the nativity/passion
rows anchor to it. Never a Bethany-Mary or Magdalene face.

## The inside/outside geometry (the story IS this)

The whole doctrine is spatial: family STANDING WITHOUT in the bright
street; the seated ring WITHIN the lamp-dim packed house; the message
relayed inward; the gaze circuit; the declaration landing on the ring
itself. Four wides with stated geometry hold the two worlds: b01 (the
packed ring from behind its backs), b02 (the family and doorway from
the side — bright street palette), b08 (the gaze circuit from behind
two shoulders), b12 (the whole room from the high corner). Three flips.

- The mother and brothers are NEVER rendered resentful — patient,
  loving concern (the scene texts have it; reject any sour render).
  The declaration honors the ring WITHOUT dishonoring them: Jesus's
  face carries warmth in both directions.
- Light law: hard bright exterior vs warm dim interior — the two
  palettes never bleed; the doorway is the only place they meet (b02).
- Direction (row-83): the message relays INWARD hand to hand (b03) —
  a readable chain; the sweep (b09) covers the RING, not the door.
- BROTHERS: distinct men sharing family resemblance with the mother
  (90/107 + family-likeness).
- HOUSE: Bethany-lane suggested a NINTH time — DECLINED (Capernaum
  packed one-room house). Promote-first from b01.
- Only Jesus wears cream.
