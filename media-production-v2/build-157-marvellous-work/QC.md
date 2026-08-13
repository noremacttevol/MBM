# QC / RUNNER HANDOFF — build-157-marvellous-work (Isaiah 29:11-14)

AUTHORED FROM SCRATCH, 2026-08-05 (Machine A). `--check` PASSES, zero
WARNs. 28 beats, ~159 s. The sealed-book row (BRIDGE, kept in
Isaiah's own frame).

## The BOOK is one sealed scroll (prop-board it hardest)

Heavy rolled parchment + dark crossed cords + THREE wax seals +
worn leather case — the SAME object every frame. State per-beat:
SEALED through b23, OPEN from b24 (cords loose beside UNBROKEN
seals — opened, not broken). Script indistinct always.

## The opening is God's act — light and result ONLY (absolute)

b21: first dawn shaft landing on the still-sealed scroll. b23:
broad dawn, still sealed. b24: simply OPEN in morning light — NO
hands, NO figure, NO mechanism, ever. Any depicted opening
mechanics = reject.

## Both askers are honourable

The SCHOLAR's "I cannot" is honest admission (never a fool); the
PLAIN man's refusal is kind (never mocked). b12 frames them as two
honest limits, equal. Face-board both across their beats.

## Registers and rhymes

- b14/b17 = the row-128 lips/heart register (correct mouths, absent
  eyes, fastidious hollow ceremony).
- b19 = the 151 spent-candle rhyme; b26 = dead stub vs risen sun.
- b16: God never embodied — the listening posture only.
- b20: the key-ring fluent in the wrong language.
- b28: kneeling OPEN hands receive the open scroll lowered from
  above frame — receiving, not grasping.

## Coverage shape

One true wide with stated geometry: b01 (camera behind Isaiah's
robed back at the window). No Jesus beats. File order HEAVILY
scrambled (b08 at 20.40s, b16 at 66s, b22 at 152s) — build by
WINDOW.

- Plates: PLAIN auto-wire REJECTED (a PERSON token wrongly matched
  to the build-38 doorway place-frame — note for the stash: person
  tokens should never place-wire). BOOK promote-first from b03.
- One drift-word FAIL ('aglow') caught and fixed pre-ship.

---

## 🅿️ RUNNER PARK → NEEDS-AUDIO — 2026-08-13 (Machine A `Dev`, Opus runner, headless)

**$0 spent. NO stills generated. Parked at the two-part audio PRE-FLIGHT before touching the meter.**

STALE-V1: row-141 class: V1 mp4 stale 209.8s vs current timeline 173.9s (+35.8s) AND 13/13 V1-dir mp3s NEWER (both tripwires fire) — so `v2_assemble`'s AUDIO LOCK refuses (the picture runner copies the V1 mp4's audio; `AUDIO_FROM_V1_SEGMENTS` is unset).

**FIX (audio lane, NOT runner — beats_v2.py is off the runner write-list):**
1. Voice-ID the V1-dir `audio/*.mp3` — confirm new-voice ElevenLabs cast.
2. Set `AUDIO_FROM_V1_SEGMENTS = True` in `beats_v2.py` (rebuild audio from the newer mp3s, $0, no re-voice).
3. 0 stills exist → hand back to the picture runner: board State NEEDS-AUDIO → AUTHORED, keep Ready ✅, Claim BLANK.

**RESUME (audio lane):** `python3 media-production-v2/v2_assemble.py 157` (refuses until the flag is set).

---

## ✅ AUDIO-FIX DONE → AUTHORED — 2026-08-13 (Machine A `Dev`, audio lane, $0, 0 stills)

STALE-V1 cleared (row-141 class, both tripwires). **Voice-ID:** all 13 placed
V1-dir mp3s (`media-production/build-157-marvellous-work/audio/*.mp3`) ffprobe as
**44100 Hz / 128 k = ElevenLabs new-voice**, and `audio-eleven.log` records all
13 (n1-n8, kv11, kv13a, kv13b [god], kv14 [god], card) cast through the
ElevenLabs pipeline — no edge-tts, no old voice. (The log's "undecided homograph"
notes on n1/n3/kv11 are pre-existing render notes, not a Cameron complaint — no
PRON fix asked for.) The V1 mp4 was BOTH stale-longer (209.8 s vs the current
~159-174 s timeline, i.e. carrying deleted segments) AND older than every mp3, so
the AUDIO LOCK's STALE-V1-FINAL guard fired both tripwires and refused the
packet-copy.

**Fix:** set `AUDIO_FROM_V1_SEGMENTS = True` in `beats_v2.py`. Track now rebuilt
from the new-voice mp3s at extract_beats offsets — the stale 209.8 s mp4 stream is
never touched, no re-voice, no re-time, V1 read-only, **$0 (no Gemini, no
ElevenLabs)**. Verified: extract_beats reads all 28 phrases cleanly (159.3 s);
`v2_assemble 157` no longer refuses on the audio lock, it stops only at the
missing stills — the picture runner's job.

**Handed to the picture runner:** board State NEEDS-AUDIO → AUTHORED, Ready ✅,
Claim cleared. When the runner generates the stills, `v2_assemble` rebuilds the
new-voice track via the flag and ships. Nothing else touched.
