# QC / RUNNER HANDOFF — build-80-come-unto-me (Matthew 11:28-30)

Lesson-12 + complaint-corpus pass done 2026-08-05 (Machine A). `--check`
PASSES, zero WARNs. 14 beats, ~83 s.

## Coverage shape

Three true wides with stated geometry: b01 (the homeward lane in
profile — every spine writing the same sentence), b03 (the offer —
camera behind the burdened listeners' shoulders as the arms open), b06
(the yoke cutaway — team and beam in profile beside the furrow). Five
flips.

## THE YOKE (the row's own doctrine-prop)

- A carved wooden DOUBLE yoke with two bow-loops — a SHARED beam for
  two oxen. Never a single-animal harness, never leather tack (the
  entire teaching lives in the two-sidedness).
- The arc: one ox laboring beside an EMPTY loop (the vacancy visible)
  → the second ox stepping IN under the open loop (b12) → the pair
  pulling as one (b13). Same two russet oxen, same beam, all frames.
- The plough keeps biting in b13 — rest is SHARED pulling, not
  stopping (the honest promise; do not render the field finished).

## The carrier's echo arc (mirrors the oxen on purpose)

Sack roped on his back alone (b01/b04) → coming WHILE loaded (b07 —
no precondition; the load stays ON through the offer) → the closing
(b14): Jesus walking BESIDE him, one hand steadying the sack's weight
— shared, not removed. If a render takes the sack away, it breaks the
doctrine; reject.

## Other checks

- Day's-end gold throughout, deepening to last light — a CORRECT
  story sunset (stated in the docstring; not the row-11 defect).
- The weary are dignified — tired workers, never wretched caricatures
  (row-15 dignity class). Crowd varied (90/107).
- Direction (row-83): homeward flow one way down the lane; the
  carrier turns TOWARD Jesus mid-step; the second ox steps IN under
  the loop.
- LANE wired from build-38's golden village-edge frame (light-
  compatible). OXFIELD promote-first from b06.
- Only Jesus wears cream.

---

## RUNNER PARK — NEEDS-AUDIO (A-auto Machine A `Dev`, 2026-08-06, $0 spent)

**Pre-flighted at step 2 BEFORE any generation (lesson-74 $0 park). NOTHING
generated — zero credits.**

`assert_v1_final_is_current(row 80)` FAILS: the V1 final
`media-production/build-80-come-unto-me/matthew-11_come-unto-me.mp4` was
rendered **2026-07-24 10:15:29**, but ALL 11 of its narration mp3s are NEWER
(**2026-07-28 14:28:20**). Timeline total = 90.6s, mp4 dur = 88.5s (excess
-2.1s), newer_mp3s = 11/11. The V1 mp4's audio stream predates the current
narration, so `v2_assemble` refuses AUDIO LOCK — copying it would ship stale
voices / a shortened timeline (rubric audio-immutability law).

This is the **row-69 / row-74 / row-78 STALE-V1 class.** The runner is
forbidden from fixing it (the fix edits `beats_v2.py`, an author audio
decision outside runner writes).

**AUTHOR FIX:** add `AUDIO_FROM_V1_SEGMENTS = True` to this build's
`beats_v2.py` (renders narration from the V1 build's OWN mp3s at the
extract_beats offsets — nothing re-voiced, nothing re-timed, V1 stays
read-only), OR re-render the V1 mp4 from the current narration.

**RESUME (runner, after author fixes audio):** `Read
media-production-v2/PROMPT-OPUS-RUNNER.md and run the next ready rows.` — the
14 authored beats are ready to generate (`v2_prompt.py build-80-come-unto-me
--check` = PASS). No stills exist yet; a full build from step 2.
