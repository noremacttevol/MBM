# QC / RUNNER HANDOFF — build-139-lamp-on-a-stand (Matthew 5:14-16)

AUTHORED FROM SCRATCH, 2026-08-05 (Machine A). `--check` PASSES, zero
WARNs. 10 beats, ~48 s.

## Shares row 121's canon (build/wire together)

HILLSIDE, CROWD, LAMPHOUSE and HILLTOWN locks are BYTE-IDENTICAL to
build-121 — same sermon, same one-room house (same lamp, stand and
bushel), same far town. When 121 promotes any of these, wire them
here identically. The lamp/stand/basket must be the SAME props as
121's b17-b20 chain.

## Light law (doubly binding — this is a light row)

Every light physical: sun, clay flame, dusk windows. Any light
effect ON a person = automatic reject; watch the drift words on
rerolls. b02's only light is the SUN. Dusk/evening frames (b03,
b04, b05, b07, b08, b10) are BY DESIGN.

## Anti-vanity pair (b07/b08, the 121/122 class)

b07: the giver's eyes on the task, gone before the door opens —
nobody watching. b08: the widow's gaze travels UP PAST the departing
helper to the sky — nothing in the sky.

## The close (b10)

A careful hand PLACING the lamp deliberately — unhurried, exact,
flame steady. The deliberateness is the sermon.

## Coverage shape

One true wide with stated geometry: b01 (camera past the seated
crowd's backs). Four Jesus beats (b01, b02, b06, b09); b06 is the
identity-before-assignment register — naming, not tasking. File
order ≠ story order (b06 at 2.73s) — build by WINDOW.

- Plates: none auto-matched. Share HILLSIDE/HILLTOWN/LAMPHOUSE with
  121 when promoted; the bushel visible and UNUSED in b05.


---

## ✅ AUDIO-LANE FIX APPLIED — Opus audio-fix lane, Machine A `Dev`, 2026-08-11, $0

**STALE-V1 resolved (8 newer mp3s / +10.4s).** Added `AUDIO_FROM_V1_SEGMENTS = True` to `beats_v2.py`
(after `REF = True`). The authoritative track is now rebuilt from the V1 narration mp3s
at the extract_beats offsets instead of copying the stale V1 mp4's AAC stream that failed
`assert_v1_final_is_current`. **Validated ($0, no TTS, no Gemini):** rebuilt track = 55.109s,
delta 0.000s vs the mp3 timeline total (guard needs <0.5s). No re-voice — same voices,
wording, timing.

**Row is buildable.** 0 stills, so per the audio-fix protocol the board is flipped to
**AUTHORED / Audio OK / Ready ✅**; a picture runner generates the stills then runs
`v2_assemble.py 139` → AUDIO REBUILD PASS and ships the full cut on this fixed audio.
