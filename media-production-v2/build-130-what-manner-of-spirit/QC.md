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

---

## ✅ PICTURE-RUNNER RESUME + SHIP — Opus runner, Machine A `Dev`, 2026-08-11 (unattended/headless)

Resumed the strand a prior autopilot lane left at RUNNING/A-auto (State RUNNING,
9/10 stills present). Already-shipped check FIRST: no committed mp4, review card
`v130` was old-era (`81719a74`/2026-07-28, no `realistic-v2`) → NOT shipped, safe
to resume. Generated the ONE missing beat only.

**COMPLAINT LEDGER: none open.** `v2_outline.py 130` shows no Cameron complaint on
this row — nothing to answer.

- **Generated:** s10 `anger-that-wants-to-destroy` (b10, ROAD place) — $0.13, 1 shot,
  ceiling $607. Passing frames s01–s09 were NEVER re-pulled (COST LAW).
- **Light QC — all 10 source stills viewed, 0 rerolls:** NO FIRE anywhere (the row's
  #1 gate holds — zeal lives only in fists/raised arms/burning faces at b02/b03/b04;
  the only flame-adjacent thing is peaceful hearth-smoke + b07 dusk lamplight, by
  design). Jesus ONE locked face + cream-only every appearance; fully realistic (no
  cartoon/mix); s05 rebuke aims at the two disciples, NOT the village (direction law);
  s07 dusk village-at-peace by design; s09 village intact/distant; James-John zeal
  reads as hot ZEAL not villainy; period props only; hands/scale/anatomy correct; no
  modern objects.
- **Assemble:** AUDIO REBUILD PASS SHA256 `12d78dfe467b436fb1e5cdb4f892cd2efaa09b1af8a3c2062dc64c07f2347c66`
  (V1 segments, `AUDIO_FROM_V1_SEGMENTS=True` from the earlier audio-lane fix), 65.496s,
  20.7 MB. mp4 `luke-9_what-manner-of-spirit.mp4`.
- **FULL-CUT GATE (6b) PASS:** extracted one rendered frame per beat + caption frames +
  card from the mp4 and viewed every one. Captions bottom-band 3-voice — white narrator
  / BLUE disciples' KJV scripture ("Lord, wilt thou that we command fire…") / RED Jesus
  KJV ("For the Son of man is not come to destroy men's lives, but to save them.");
  KJV text exact; art uncovered; question card ("He came to save, not to burn…") clean.
  No fire in any rendered frame; Ken Burns crops keep every subject framed.
- **COST-LAW:** this session $0.13 / 0 rerolls (0%) — far under the $6.10 avg + 15%
  budget; the resume touched the row ONCE. Row total across sessions = 10 stills ≈ $1.34.
