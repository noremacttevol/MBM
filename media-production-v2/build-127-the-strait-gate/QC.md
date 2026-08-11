# QC / RUNNER HANDOFF — build-127-the-strait-gate (Matthew 7:13-14)

AUTHORED FROM SCRATCH (scaffolded + written this session), 2026-08-05
(Machine A). `--check` PASSES, zero WARNs. 10 beats, ~59 s.

## CONTENT-CARE — destruction is NEVER depicted

The broad road is genuinely pleasant and its far end dissolves into
flat featureless HAZE — no cliff, no fire, no doom imagery, no
falling figures, in any frame. The travellers on it are ordinary and
cheerful, never villains. The row's weight is the CHOICE; the only
destination ever shown is the narrow way's payoff (b09: high green
living country — spring, trees, light).

## The GATES landscape is one place (prop-board it)

Wide handsome gateway + narrow low gate a stone's throw apart at ONE
fork — same gates, same rocks, same roads in b02-b08 and b10. Both
gates stand OPEN in every frame (never barred/chained/guarded —
b10's narration says so out loud).

## Direction / action gates

- b05: the traveller STOOPS through the strait gate — the gate asks
  something of the body.
- b08: the chooser's weight on NEITHER foot — genuinely undecided.
- b10: mid-step TOWARD the narrow gate, unmistakable — the closing
  image is one deliberate footfall.
- b07: exactly THREE walkers spaced on the switchbacks (counts law).

## Coverage shape

One true wide with stated geometry: b01 (camera past the seated
crowd's backs; Jesus STANDING here — the only standing-Jesus frame
of the sermon set, per "Jesus stood" in the narration). One Jesus
beat total (b01). Fair-light law: both roads get the same clear
morning — no gloomy weather on either. File order ≠ story order
(b02 at 45s, b05 at 25s before b04's 19s neighbor b06) — build by
WINDOW.

- Plates: none auto-matched (clean). GATES promote-first from b03,
  HILLSIDE shared with 121-126.
- Clone-check the b03/b06 broad-road travellers (rows 90/107).

---

## ⛔ RUNNER PARK — NEEDS-AUDIO (Opus runner, Machine A `Dev`, 2026-08-11, $0)

Audio pre-flight (batch with row 125) FAILS the STALE-V1 guard — generated nothing.
The V1 mp4 carries audio not in the current mp3 timeline (row 127 excess/newer flagged
STALE by `assert_v1_final_is_current`), so `v2_assemble` refuses the AUDIO LOCK.
FIX is audio-lane only: set `AUDIO_FROM_V1_SEGMENTS = True` in this build's beats_v2.py,
then `python3 media-production-v2/v2_assemble.py 127` must print AUDIO REBUILD PASS; the
row is then buildable for a picture runner. See build-125-i-never-knew-you/QC.md for the
full batch diagnosis (125/126/127 excess-tail ~0.9s; 128 has 8 newer mp3s).


---

## ✅ AUDIO-LANE FIX APPLIED — Opus audio-fix lane, Machine A `Dev`, 2026-08-11, $0

**STALE-V1 resolved (+0.889).** Added `AUDIO_FROM_V1_SEGMENTS = True` to `beats_v2.py`
(after `REF = True`). The authoritative track is now rebuilt from the V1 narration mp3s
at the extract_beats offsets instead of copying the stale V1 mp4's AAC stream that failed
`assert_v1_final_is_current`. **Validated ($0, no TTS, no Gemini):** rebuilt track = 66.711s,
delta 0.000s vs the mp3 timeline total (guard needs <0.5s). No re-voice — same voices,
wording, timing.

**Row is buildable.** 0 stills, so per the audio-fix protocol the board is flipped to
**AUTHORED / Audio OK / Ready ✅**; a picture runner generates the stills then runs
`v2_assemble.py 127` → AUDIO REBUILD PASS and ships the full cut on this fixed audio.
