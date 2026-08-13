# QC / RUNNER HANDOFF — build-152-revealeth-his-secret (Amos 3:7-8)

AUTHORED FROM SCRATCH, 2026-08-05 (Machine A). `--check` PASSES, zero
WARNs. 21 beats, ~119 s. The living-prophets pattern row
(MAINTENANCE/BRIDGE tone).

## God never embodied

The word arrives as wind in the grass + arrested listening (b03/b04/
b08) — no figure, no visualized voice, ever. Automatic reject.

## The lion (b15/b17) — distance only

A real lion mid-roar on a FAR dusk ridge; NO attack, NO hunt, never
monstrous. Its whole effect is every head turning (b17: flock ears,
shepherd, lifting birds — universal involuntary attention).

## The continuing pattern (b19-b21) — timeless, never modern

Household hearing words read → a NEW watchman (different man, SAME
post — succession) at dawn → the listening posture. Row-7 law holds
doubly: one modern object anywhere is a reject. The pattern is
carried by repetition of office only.

## Mercy register on all warning imagery

Watchman (b05), lamp-goes-first (b06), storm-warned household
(b10 — storm FAR, household calm), mended wall + walker-home (b14).
Preparation, never panic. b13's turning faces: softened and
resolved, not frightened.

## Amos gates

Plain working man — ordinariness IS the doctrine; the unpracticed
writing hand (b07); the level unedited delivery (b18 — neither rage
nor apology). Gate crowd (b12): mixed and honest, no mob, no
cartoon scoffers. Face-board Amos across 10 appearances.

## Coverage shape

One true wide with stated geometry: b01 (camera low on the ridge,
flock-line from the side). No Jesus beats. Script indistinct
wherever written words appear. File order = story order except
b11's segment start.

- Plates: none auto-matched (clean). HILLS promote-first from b01,
  GATE from b12.

---

## 🅿️ RUNNER PARK → NEEDS-AUDIO — 2026-08-13 (Machine A `Dev`, Opus runner, headless)

**$0 spent. NO stills generated. Parked at the two-part audio PRE-FLIGHT before touching the meter.**

STALE-V1: row-147 class: durations match (131.3s) but 11/11 V1-dir mp3s NEWER than the V1 mp4 (new-voice re-record) — so `v2_assemble`'s AUDIO LOCK refuses (the picture runner copies the V1 mp4's audio; `AUDIO_FROM_V1_SEGMENTS` is unset).

**FIX (audio lane, NOT runner — beats_v2.py is off the runner write-list):**
1. Voice-ID the V1-dir `audio/*.mp3` — confirm new-voice ElevenLabs cast.
2. Set `AUDIO_FROM_V1_SEGMENTS = True` in `beats_v2.py` (rebuild audio from the newer mp3s, $0, no re-voice).
3. 0 stills exist → hand back to the picture runner: board State NEEDS-AUDIO → AUTHORED, keep Ready ✅, Claim BLANK.

**RESUME (audio lane):** `python3 media-production-v2/v2_assemble.py 152` (refuses until the flag is set).
