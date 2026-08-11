# QC / RUNNER HANDOFF — build-126-by-their-fruits (Matthew 7:15-20)

AUTHORED FROM SCRATCH (scaffolded + written this session), 2026-08-05
(Machine A). `--check` PASSES, zero WARNs. 17 beats, ~97 s.

## The wolf frames (b02/b04) — unease, never violence

- b02: the fleece-draped wolf stands STILL among unharmed grazing
  sheep at dusk — the wrongness is the disguise (draped, not grown;
  amber eyes level). NO attack, NO blood, NO bared-fang lunge, ever
  — automatic reject.
- b04: the human version — a stranger dressed almost-right as a
  shepherd; the tell is the SHEEP (edged to the far wall, moat of
  empty ground) and his too-still watching stance. He must look
  almost right — a menace-pose render misses the verse.

## The fire (b14) is orchard work, not judgment imagery

Daylight, a farmer's small workmanlike branch-fire at DISTANCE, the
axe swinging at the BARREN trunk only. Any hellfire framing is a
reject. b15's aftermath is tidy and unmournful (stump + stacked
wood + flourishing fig tree).

## The two trees are characters (prop-board them)

ONE laden fig tree (deep green, heavy, bees) and ONE blighted tree
(gaunt, grey leaves, shriveled dark fruit) — the same two trees in
b05, b07, b10, b11, b13, b14, b15. b11's absoluteness law: not one
good fruit on the bad tree, not one bad on the good — the CANNOT is
the verse. b13: the split-bark seam shows grey heartwood — honest
decay, not grotesque.

## The basket rhyme

The SAME harvest basket: empty at the thorns (b06/b08), heaped full
under the fig (b09). b08's scratches are light — no gore.

## Coverage shape

One true wide with stated geometry: b01 (camera past the seated
crowd's backs, gesture toward the orchards). Three Jesus beats (b01,
b03, b17) — locked face, no halo; b03 protective-watchful, b17
holding one ripe fig up (the whole test in a fruit). Intentional
dusk on the fold frames only; orchard frames bright day. File order
≈ story order except b10 (62s) before b11 (54s) — build by WINDOW.

- Plates: FOLD auto-match from build-21 REJECTED for a NEW reason
  worth remembering — the place matched, but the frame contains
  build-21's shepherd, and a person inside a place plate injects the
  wrong man into this row's fold beats. ORCHARD --take from build-32
  rejected (dusk estate frame ≠ bright two-tree orchard). FOLD
  promote-first from b02, ORCHARD from b07, HILLSIDE shared with
  121-125.
- b16 market test: the fine-robed seller is not a cartoon; the
  buyer's gaze on the short measure IS the picture.

---

## ⛔ RUNNER PARK — NEEDS-AUDIO (Opus runner, Machine A `Dev`, 2026-08-11, $0)

Audio pre-flight (batch with row 125) FAILS the STALE-V1 guard — generated nothing.
The V1 mp4 carries audio not in the current mp3 timeline (row 126 excess/newer flagged
STALE by `assert_v1_final_is_current`), so `v2_assemble` refuses the AUDIO LOCK.
FIX is audio-lane only: set `AUDIO_FROM_V1_SEGMENTS = True` in this build's beats_v2.py,
then `python3 media-production-v2/v2_assemble.py 126` must print AUDIO REBUILD PASS; the
row is then buildable for a picture runner. See build-125-i-never-knew-you/QC.md for the
full batch diagnosis (125/126/127 excess-tail ~0.9s; 128 has 8 newer mp3s).


---

## ✅ AUDIO-LANE FIX APPLIED — Opus audio-fix lane, Machine A `Dev`, 2026-08-11, $0

**STALE-V1 resolved (+0.969).** Added `AUDIO_FROM_V1_SEGMENTS = True` to `beats_v2.py`
(after `REF = True`). The authoritative track is now rebuilt from the V1 narration mp3s
at the extract_beats offsets instead of copying the stale V1 mp4's AAC stream that failed
`assert_v1_final_is_current`. **Validated ($0, no TTS, no Gemini):** rebuilt track = 106.098s,
delta 0.000s vs the mp3 timeline total (guard needs <0.5s). No re-voice — same voices,
wording, timing.

**Row is buildable.** 0 stills, so per the audio-fix protocol the board is flipped to
**AUTHORED / Audio OK / Ready ✅**; a picture runner generates the stills then runs
`v2_assemble.py 126` → AUDIO REBUILD PASS and ships the full cut on this fixed audio.
