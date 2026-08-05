# Story 11 V4 QC — Calming the Storm

Final candidate: `mark-4_calming-the-storm-realistic-v4.mp4`

## Why V4 exists — Cameron DENIED V3 (board sync 2026-08-01), four complaints

1. **"The first picture is messed up… it was fine before."** V3's s01 buried
   Jesus inside the crowd with other standing men in pale robes. V4's s01 was
   regenerated at native 2K using the approved earlier composition as the
   rough-draft reference: Jesus set apart at the water's edge on the left,
   the whole crowd on the right facing him, correct last-light evening.
2. **"Someone climbing up that mast."** V3's s10 had a man wrapped around the
   mast and another hanging one-handed off a masthead rope. V4's s10 puts every
   man LOW in the hull — knees bent, feet flat on the deck, hands on gunwale,
   thwart, or chest-height rope. Nobody touches the mast. The beat prompt now
   forbids climbing permanently.
3. **"People pouring water inside the boat."** V3's s11 had a huge water arc
   curling back over the deck beside the bailer. V4's s11: the scoop is past
   the rail, mouth turned out and down, the only airborne water is one sheet
   falling OUTSIDE the hull toward the sea; the second man fills his scoop
   from the deck water. ACTION-LOGIC reads correctly at a glance.
4. **"Jesus didn't say peace, be still that fast."** j1 was 1.44 s with no
   pause. Re-rendered on the same ElevenLabs Jesus voice (same model, same
   pipeline, no time-stretch) at speed 0.8 with a real caesura: "Peace" …
   0.42 s pause … "be still." — 2.32 s total, weighty and unhurried.
   Ear-checked with faster-whisper: heard "Peace. Be still." Exact KJV kept
   in caption and script.

## Timeline correctness (found while fixing #4)

- build-11-storm's V1 `build.py` computes segment durations from RAW mp3
  lengths, but `extract_beats.py` assumed silence-trimmed lengths — the V3 cut
  was assembled on a timeline 7.9 s short, so captions and picture switches
  drifted up to ~8 s ahead of the voice by the end. `extract_beats.py` now
  reads each build's own formulas (raw vs trimmed, card_spoken vs card_dur,
  TAIL vs CARD_HOLD) from its build.py source.
- All 34 beat windows in `beats_v2.py` were re-timed onto the true timeline
  using each segment's ElevenLabs per-sentence timing, so every picture lands
  on the sentence it illustrates.
- The V1 final (`media-production/build-11-storm/mark-4_calming-the-storm.mp4`)
  was rebuilt by its own build.py with the new j1; V4's audio is that stream
  copied packet-for-packet. AUDIO LOCK PASS:
  `SHA256=631b100ce410058b4db16f6c1aaa3fc352a165ff5144c00324fa19a0a360432e`.

## Mechanical checks

- Final: 1080×1920 H.264, 30 fps, 234.900 s, 20.7 MB.
- Final SHA-1: `fde289913153d289b59958a8c149ddd17453896c`.
- Final SHA-256: `c36d5a8e8e72c87bbfb99a252d9e81bb02c20b59685552cebae42ecc8fc2e1f0`.
- `v2_prompt.py --check` (JESUS LOCK v5 / v4 checklist): PASS, 34 beats.
- Frame checks on the finished cut (extracted and eyeballed): s01 with its
  caption at 0:01; s10 at 1:07 under "This storm was savage…"; s11 at 1:11
  under "Waves broke over the side…"; s21 close-up at 2:11–2:13 with the red
  "Peace, be still." caption exactly while the line is spoken; closing card
  from 3:41; video ends 1.5 s (TAIL law) after the last spoken word.
- Silence map around j1 in the finished cut: n5 ends 129.7, LEAD breath,
  "Peace" 131.2–131.8, pause 0.42 s, "be still" 132.2–132.9, KJV gap, n6 at
  134.8 — unhurried, no dead air.
- No music bed anywhere — narration and intentional silence only.
- Captions bottom band only; nothing over the art.
- Stills only, slow Ken Burns; no AI motion clips.
- Night law holds from s05 onward (moon/stars/lightning, no sunset coloring);
  the great calm stays mirror-flat under stars.
- Wide boat views keep the eight-man early company with distinct recurring
  faces; only Jesus wears cream; no halo/glow/rim-light.
- The replacement media hash resets Story 11 to Unwatched in the reviewer
  while preserving its complaint history.

The visual storyboard and extracted review frames are rebuildable scratch under
`qc-v2/`; the mobile app and its live story video were not changed.

## OPEN CAMERON COMPLAINT — gates before rebuild

"too many pictures that are different from each other... 10 pictures
of 4 people in one kind of boat and 10 pictures of 5 people in a
different boat."
BOAT BOARD: before assembly, line up EVERY boat-bearing still
side-by-side and verify it is the SAME boat (plank pattern, mast,
stern platform, gunwale line) in every frame — treat the boat like a
locked face. CREW COUNT: any frame showing the whole company shows
the SAME EIGHT men; a cropped subset must read as a CROP (bodies
exiting frame edges), never as a smaller crew in an emptier boat.
Two boats or a changing headcount = the complaint repeated.
