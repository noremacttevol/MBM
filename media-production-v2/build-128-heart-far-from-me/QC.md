# QC / RUNNER HANDOFF — build-128-heart-far-from-me (Matt 15:1-9; Mark 7:1-13)

AUTHORED FROM SCRATCH (prepped + scaffolded + written this session),
2026-08-05 (Machine A). `--check` PASSES, zero WARNs. 16 beats, ~91 s.

## ⚠ ROW-IDENTITY FIX MADE THIS SESSION (read before touching)

The AUTHOR-BOARD listed row 128 as build-128-famine-of-hearing — the
RETIRED story (QUEUE.md retired it in favor of heart-far-from-me).
Board slug corrected; the wrongly-prepped famine V2 dir was deleted.
TWO SHARED TOOLS were also fixed: extract_beats.py now handles
SILENT-CARD builds (this build has CARD_TEXT/CARD_DUR and no
card.mp3 by design), and v2_prep_row.py now honors
CANONICAL_BUILD_SLUGS for dup-numbered rows instead of sorted()[0].

## The silent card

The closing card is SILENT by design — no card.mp3 exists or should
exist. Do NOT flag it as missing audio; nothing to ear-check there.

## Villain law (complaint-corpus standing rule)

The five LEADERS are earnest, dignified, sincere — scandalized
guardians of a fence they love. b03's shock is honest hurt; b12's
"not impressed" on Jesus is level stillness, NEVER a sneer on either
side. Exactly FIVE leaders every appearance (counts law).

## The corban pair (b11/b14 — the row's moral weight)

- b11: the tag knotted onto the pouch must read instantly (action-
  logic); the parents at FAR ground, outside his attention.
- b14: parents close — dignity total, need real, never abject
  (rows 44/74/75 class). Same couple as b10 (face-board).

## Composition-argument frames (check as a set)

- b05/b07: the SAME worshiper (face continuity) — correct lips,
  absent eyes; b07 adds the thousand-mile horizon behind him.
- b09/b13: the scroll swap then the scroll covering — old scroll
  dignified, all script indistinct, b13's under-scroll completely
  covered.
- b15: loud vessels front, quiet father-helped-over-threshold small
  through the doorway.

## Coverage shape

One true wide with stated geometry: b01 (camera past the
delegation's robed backs). Five Jesus beats (b01, b04, b08, b12,
b16) — locked face, no halo; b08's focus visibly PAST the ritual
hands; b16 ends on the dusty ordinary man welcomed. File order ≠
story order (b12 at 14.4s) — build by WINDOW.

- Plates: none auto-matched. COURT promote-first from b01; LEADERS
  is a recurring-group token (the build-06 chief-priests family may
  fit — compare before wiring); MEAL from b02; PARENTS face-board
  across b10/b11/b14.

---

## ⛔ RUNNER PARK — NEEDS-AUDIO (Opus runner, Machine A `Dev`, 2026-08-11, $0)

Audio pre-flight (batch with row 125) FAILS the STALE-V1 guard — generated nothing.
The V1 mp4 carries audio not in the current mp3 timeline (row 128 excess/newer flagged
STALE by `assert_v1_final_is_current`), so `v2_assemble` refuses the AUDIO LOCK.
FIX is audio-lane only: set `AUDIO_FROM_V1_SEGMENTS = True` in this build's beats_v2.py,
then `python3 media-production-v2/v2_assemble.py 128` must print AUDIO REBUILD PASS; the
row is then buildable for a picture runner. See build-125-i-never-knew-you/QC.md for the
full batch diagnosis (125/126/127 excess-tail ~0.9s; 128 has 8 newer mp3s).

---

## ✅ AUDIO-LANE FIX APPLIED — Opus audio-fix lane, Machine A `Dev`, 2026-08-11, $0

**STALE-V1 resolved (8 newer mp3s, −1.778s — the story was re-recorded but never
re-rendered into a new V1 mp4).** Added `AUDIO_FROM_V1_SEGMENTS = True` to
`beats_v2.py` so the track is rebuilt from the 8 CURRENT V1 segment mp3s
(n1,n2,j1,n3,j2,n4,j3,n5 — all present) at the extract_beats offsets. The stale V1
mp4's AAC (which failed `assert_v1_final_is_current`) is no longer used.

**Tooling fix required first:** this row's closing question card is SILENT
(`beats.json: "silent": true, seg=null, audio_start=null`), so
`rebuild_audio_from_segments` was crashing trying to load `audio/None.mp3`.
Patched it to skip a null-seg card (a silent card contributes no audio; `apad`
already pads the track through its 6.78s on-screen duration). Safe for every other
row — spoken cards have seg='card', unchanged.

**Validated ($0, no TTS, no Gemini):** rebuilt track = 97.445s, delta 0.000s vs the
mp3 timeline total. No re-voice — same voices, wording, timing.

**Row is buildable.** 0 stills → board flipped to **AUTHORED / Audio OK / Ready ✅**;
a picture runner builds the stills then runs `v2_assemble.py 128` → AUDIO REBUILD
PASS and ships the full cut.
