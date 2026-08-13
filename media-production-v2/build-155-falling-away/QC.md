# QC / RUNNER HANDOFF — build-155-falling-away (2 Thess 2:1-3)

AUTHORED FROM SCRATCH, 2026-08-05 (Machine A). `--check` PASSES, zero
WARNs. 22 beats, ~123 s. The foretold-apostasy row (BRIDGE): the
dimming was predicted, so the returning was always in the plan.

## THE MAN OF SIN IS NEVER DEPICTED (b17, absolute)

The clause is READ in the letter — no sinister figure, no shadowed
villain, anywhere in the row. Automatic reject.

## The lampstand is the row's engine (prop-board it hard)

ONE great standing lampstand, its state per-beat: FULL-lit (b01,
b08) → first flames out (b07) → mostly dark (b11) → dark with one
flame RE-CAUGHT (b19) → relighting flame by flame (b21). The
dimming is SORROWFUL (thin smoke threads, growing shadow) — never
sinister, no dark force, no wind, no hand.

## No villains anywhere

The drifters (b12) are ordinary people leaving unhurried — sorrow,
never sneering. The rumor-messenger (b16) is sincere-alarmed, the
forged letter's script indistinct. Rumor-chain (b04) is human
telephone, not malice.

## Paul is row-138's canon face

Lock byte-identical to build-138 — face-board. His register: calm
chosen on purpose (b03, the lamp-flame mirrors him), plainness
(b09), tenderness over hard words (b20).

## Rhymes

- b05 anchor vs tossed boats; b06 swirl vs one seated reader.
- b10/b15 the two waymarks — order readable, the near stone FIRST;
  b15's hand on the fulfilled marker.
- b14 = the 152 storm-warned household register.
- b18: night with faintly paling EAST.
- b19/b21/b22 = the 154 relighting rhyme, ending TAKEN (fingers
  close on the handle) — deliberate contrast with 154's open close.

## Coverage shape

One true wide with stated geometry: b01 (camera across the benches
past the believers' backs). No Jesus beats. File order ≠ story
order (b07 at 55s, b16 at 2.68s) — build by WINDOW.

- Plates: HALL --take from build-22 REJECTED (parable king's hall ≠
  modest house-courtyard). HALL promote-first from b01, ROOM from
  b02.

---

## 🅿️ RUNNER PARK → NEEDS-AUDIO — 2026-08-13 (Machine A `Dev`, Opus runner, headless)

**$0 spent. NO stills generated. Parked at the two-part audio PRE-FLIGHT before touching the meter.**

STALE-V1: row-147 class: durations match (~136.9s) but 11/11 V1-dir mp3s NEWER than the V1 mp4 (new-voice re-record) — so `v2_assemble`'s AUDIO LOCK refuses (the picture runner copies the V1 mp4's audio; `AUDIO_FROM_V1_SEGMENTS` is unset).

**FIX (audio lane, NOT runner — beats_v2.py is off the runner write-list):**
1. Voice-ID the V1-dir `audio/*.mp3` — confirm new-voice ElevenLabs cast.
2. Set `AUDIO_FROM_V1_SEGMENTS = True` in `beats_v2.py` (rebuild audio from the newer mp3s, $0, no re-voice).
3. 0 stills exist → hand back to the picture runner: board State NEEDS-AUDIO → AUTHORED, keep Ready ✅, Claim BLANK.

**RESUME (audio lane):** `python3 media-production-v2/v2_assemble.py 155` (refuses until the flag is set).

---

## ✅ AUDIO-FIX DONE → AUTHORED — 2026-08-13 (Machine A `Dev`, audio lane, $0, 0 stills)

STALE-V1 cleared. **Voice-ID:** all 11 placed V1-dir mp3s
(`media-production/build-155-falling-away/audio/*.mp3`) ffprobe as
**44100 Hz / 128 k = ElevenLabs new-voice**, and `audio-eleven.log` records all
11 segments (n1-n8, kv2, kv3, card) cast through the ElevenLabs pipeline — no
edge-tts, no old voice anywhere. They were newer than the V1 mp4 (old-voice
render), which is exactly why the AUDIO LOCK's STALE-V1-FINAL guard refused the
packet-copy.

**Fix:** set `AUDIO_FROM_V1_SEGMENTS = True` in `beats_v2.py`. The track is now
rebuilt from these new-voice mp3s at the extract_beats offsets — no re-voice, no
re-time, V1 stays read-only, **$0 (no Gemini, no ElevenLabs)**. Verified: the
extract_beats timeline reads all 25 phrases cleanly (123.1 s); `v2_assemble 155`
no longer refuses on the audio lock, it now stops only at the missing stills
("row not fully generated") — the picture runner's job.

**Handed to the picture runner:** board State NEEDS-AUDIO → AUTHORED, Ready ✅,
Claim cleared. When the runner generates the 22 stills, `v2_assemble` rebuilds
the new-voice track via the flag and ships. Nothing else touched — same voices,
same wording, same timing.
