# QC / RUNNER HANDOFF — build-130-what-manner-of-spirit (Luke 9:51-56)

AUTHORED FROM SCRATCH (prepped + scaffolded + written this session),
2026-08-05 (Machine A). `--check` PASSES, zero WARNs. 10 beats, ~59 s.

## NO FIRE, EVER (the row's #1 gate)

Fire is what the brothers WANTED, not what happened. No render may
show fire falling, threatening skies, judgment smoke, or a scorched
village — automatic reject, no reroll. The fire lives only in raised
arms and burning faces (b02/b03/b04). The ONLY flame-adjacent thing
in the whole row is the village's own peaceful hearth-smoke and
lamplight at dusk (b07) — deliberate, homely, safe.

## James and John are the shared cast tokens

JAMES-Z and JOHN from CAST-V2-REF — same two faces as every other
build (face-board against the sheets). Their arc must read across
frames: burning (b02/b03) → arms lowering (b06) → quieted and
following (b10, same faces as b03, visibly calmed). Hot ZEAL, never
villainy.

## Direction law makes the sermon (b05)

Jesus TURNED: his back fully to the village, correcting hand toward
his OWN disciples. If a render aims any part of the rebuke at the
village, it inverts the scripture — reject.

## The village is never punished and never villainous

Wary elders, a politely turned hand, a closed gate (b01) — no
hostility theatre. The village appears whole and at peace in every
frame through the very last road shot (b09: tiny, intact, distant).

## Coverage shape

One true wide with stated geometry: b01 (camera past the
travellers' dusty backs up the slope). Six Jesus beats (b01, b05,
b06, b08, b09, b10). Late-afternoon → golden evening along one road;
b07's dusk is by design. File order ≠ story order (b03 at 39s) —
build by WINDOW.

- Plates: ROAD (build-38 b39, third rejection of that road-through-
  doorway frame) and VILLAGE (b46 doorway corner) both REJECTED.
  VILLAGE promote-first from b01, ROAD from b08.
- Walking-on beats (b08-b10): backs to the village, nobody glancing
  back in anger.


---

## ✅ AUDIO-LANE FIX APPLIED — Opus audio-fix lane, Machine A `Dev`, 2026-08-11, $0

**STALE-V1 resolved (+1.215).** Added `AUDIO_FROM_V1_SEGMENTS = True` to `beats_v2.py`
(after `REF = True`). The authoritative track is now rebuilt from the V1 narration mp3s
at the extract_beats offsets instead of copying the stale V1 mp4's AAC stream that failed
`assert_v1_final_is_current`. **Validated ($0, no TTS, no Gemini):** rebuilt track = 65.496s,
delta 0.000s vs the mp3 timeline total (guard needs <0.5s). No re-voice — same voices,
wording, timing.

**Row is buildable.** 0 stills, so per the audio-fix protocol the board is flipped to
**AUTHORED / Audio OK / Ready ✅**; a picture runner generates the stills then runs
`v2_assemble.py 130` → AUDIO REBUILD PASS and ships the full cut on this fixed audio.
