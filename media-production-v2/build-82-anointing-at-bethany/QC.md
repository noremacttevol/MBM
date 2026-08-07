# QC / RUNNER HANDOFF — build-82-anointing-at-bethany (Mark 14:3-9)

## ✅ AUDIO FIX DONE — AUDIO-FIX session, Machine A, 2026-08-06 ($0)

**STALE-V1 audio-lock CLEARED.** Added `AUDIO_FROM_V1_SEGMENTS = True` to
beats_v2.py. The V1 mp4 `mark-14_anointing-at-bethany.mp4` failed BOTH tripwires
in `assert_v1_final_is_current` (all 19 segment mp3s newer than the mp4 AND the
mp4 ~+7s longer than the summed timeline). With the flag set, v2_assemble
rebuilds narration from the V1 build's OWN new-voice mp3s at the extract offsets
— nothing re-voiced/re-timed, V1 read-only. **Segment parity 19/19 exact.**
Validated: `v2_assemble.py 82` now clears the audio gate and stops only on
missing stills (0 V2 stills); `v2_prompt.py 82 --check` PASSES (25 beats). Board
NEEDS-AUDIO → AUTHORED / Audio OK / Ready ✅, claim cleared → picture runner
generates + assembles on corrected audio. Same mechanism as shipped row 69.

---


Lesson-12 + complaint-corpus pass done 2026-08-05 (Machine A). `--check`
PASSES, zero WARNs. 25 beats, ~141 s.

## THREE-WOMEN LAW (do not cross the anointings)

The library now has three distinct anointing-adjacent women:
1. Luke 7's sinner (rows 44/74) — wine-dark dress, Simon the
   PHARISEE's house, feet anointed, tears.
2. THIS row's unnamed woman (Mark 14) — OLIVE-GREEN, Simon the
   LEPER's house, HEAD anointed, silent, two days before Passover.
3. Mary of Bethany (build-16/17's dusty-indigo Mary) — appears in her
   own rows only.
Never reuse faces or dresses across the three. This woman is
story-local — story-cast her fresh.

## The anointing (this telling's exact facts — reroll anything else)

- The flask is BROKEN AT THE NECK (v3) — not unstopped; body intact
  in her hands, snapped neck; shards later.
- Poured ON HIS HEAD — oil bright in his hair and beard through
  b03→b20 (persistent, like row 17's tears — he does not reset to
  dry hair).
- She NEVER SPEAKS — silence as strength in every frame.
- "She hath done what she could... for a memorial of her" — the
  closing (b25) is her quiet exit into the night, honored.

## Coverage shape

Four true wides with stated geometry: b01 (the supper in profile), b09
(the shield — the interposition in profile: halting palm to critics,
open hand to her), b15 (the room divided by what its faces know), b20
(the memorial decreed in profile). Nine flips — the pour (b03) is
TIGHT.

## Other checks

- CRITICS indignant but human (90/107); "three hundred pence" is
  spoken arithmetic, not shown coins.
- Lamplit interior evening throughout (intentional; not the row-11
  night defect — stated in docstring).
- Direction (row-83): she enters from the door-shadow ALONG the
  table's edge; the murmuring leans INWARD; she exits through the
  same door.
- ROOM promote-first from b01. JAR is a prop lock — no plate.
- Only Jesus wears cream.

---
## RUNNER PARK — NEEDS-AUDIO (A-auto 2026-08-06, $0 pre-flight, generated NOTHING)

STALE-V1 audio class (row-69/74/78). $0 audio-lock pre-flight FAILS BOTH
tripwires:
- RECENCY: newer_mp3s=19 (all placed mp3s re-rendered AFTER the V1 mp4).
- DURATION: timeline total=147.76s vs V1 mp4 d=154.77s → excess=+7.00s (abs>1.0).
V1 mp4 `mark-14_anointing-at-bethany.mp4` is out of date vs the current
narration. Runner is forbidden to re-render/edit beats_v2.py (audio-immutability).

AUTHOR FIX: add `AUDIO_FROM_V1_SEGMENTS = True` to this row's beats_v2.py (rebuilds
the track from this build's own mp3s at the extract_beats offsets — nothing
re-voiced), OR re-render the V1 mp4. Then set Ready ✅ + Audio OK on AUTHOR-BOARD.
RUNNER RESUME (after author fix): `python3 media-production-v2/v2_story_cast.py build-82-anointing-at-bethany` then `v2_gen_api.py build-82-anointing-at-bethany --ceiling …`.
No stills were generated; nothing to reuse yet.
