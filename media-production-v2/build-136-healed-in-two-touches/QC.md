# QC / RUNNER HANDOFF — build-136-healed-in-two-touches (Mark 8:22-26)

AUTHORED FROM SCRATCH, 2026-08-05 (Machine A). `--check` PASSES, zero
WARNs. 10 beats, ~56 s.

## The spitting is NEVER rendered as fluid (b03)

Scripture-exact by POSTURE only: head bent close, thumbs at the
closed eyelids. Any render with visible fluid is a reject.

## The trees-walking blur is INTENTIONAL (b04)

The background figures are deliberately soft-blurred, tall and
swaying, tree-like — this is the man's painted half-vision, NOT a
phantom-people or render defect. Do not "fix" it. The near world
stays crisp. b07 is the contrast: everything crisp, leaf veins
readable, distant figures unmistakably people.

## The two-touch rhyme (b03 ↔ b06)

Same hand positions exactly — thumbs at lids, palms at temples.
Prop-board the gesture. b08 delivers the first true eye-contact of
the story (healed eyes on their healer).

## Dignity + direction gates

- The blind man: warm living skin, clouded eyes early, no
  disfigurement (row-15 class); guided by friends, never dragged.
- b02: OUT through the gate, away from town (camera follows the
  handhold). b10: sent HOME by the away-road — never back through
  the town gate.
- b05: zero impatience on Jesus at the honest half-report — the
  warmth IS the frame.

## Coverage shape

One true wide with stated geometry: b01 (camera down the lane past
the group's backs). Seven Jesus beats (b01, b02, b03, b05, b06,
b08, b10). One soft clear morning throughout — the light mirrors
the healing. File order = story order.

- Plates: VILLAGE (build-38 b46 doorway — SIXTH build it has
  wrongly matched) and FRIENDS take (build-13 roof-friends, second
  rejection) both REJECTED. VILLAGE promote-first from b01.
- BLINDMAN face-board across all 10; eye-state arc: clouded →
  half-clear → clear.


---

## ✅ AUDIO-LANE FIX APPLIED — Opus audio-fix lane, Machine A `Dev`, 2026-08-11, $0

**STALE-V1 resolved (8 newer mp3s / +13.3s).** Added `AUDIO_FROM_V1_SEGMENTS = True` to `beats_v2.py`
(after `REF = True`). The authoritative track is now rebuilt from the V1 narration mp3s
at the extract_beats offsets instead of copying the stale V1 mp4's AAC stream that failed
`assert_v1_final_is_current`. **Validated ($0, no TTS, no Gemini):** rebuilt track = 49.061s,
delta 0.000s vs the mp3 timeline total (guard needs <0.5s). No re-voice — same voices,
wording, timing.

**Row is buildable.** 0 stills, so per the audio-fix protocol the board is flipped to
**AUTHORED / Audio OK / Ready ✅**; a picture runner generates the stills then runs
`v2_assemble.py 136` → AUDIO REBUILD PASS and ships the full cut on this fixed audio.
