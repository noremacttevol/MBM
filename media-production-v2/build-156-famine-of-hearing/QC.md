# QC / RUNNER HANDOFF — build-156-famine-of-hearing (Amos 8:11-12)

AUTHORED FROM SCRATCH, 2026-08-05 (Machine A). `--check` PASSES, zero
WARNs. 22 beats, ~123 s. The word-famine row (BRIDGE; companion to
152/155 — Cameron's by-name story class from the QUEUE's original
row-128 slug, now living here).

## The famine is NEVER physical hunger

Every table FULL, every well brims, the granary heaped — the
starvation lives ONLY in eyes and empty scroll-niches. Any
starvation imagery is a reject. b06 is the row-141 fed-hollow rhyme.

## Amos and the GATE are row 152's (byte-identical)

Face-board Amos against build-152; share 152's promoted GATE frame
when it exists.

## The search with dignity

Seekers earnest and dignified always (b09-b16) — never mocked.
b13's map-scale wander: small parties on every road, camera high on
the ridge. b16: the shore as the land's LIMIT — sea to sea walked
out. b15: the hand closes on AIR.

## The proof-and-harvest turn

- b19: the lamp-shaped niche — the fit IS the proof (carved for
  exactly one thing, waiting).
- b18: hand pressed gently at the chest — locating, not clutching.
- b20: grain one day from ripe — the ache right before harvest.
- b21: loaves being carried IN — provision returning in hands.
- b22: the OPEN BOOK at the meal's centre + ONE empty stool drawn
  back toward the viewer. Script indistinct everywhere.

## Coverage shape

Two true wides with stated geometry: b01 (through the gateway past
the crowd's backs), b13 (camera high on the ridge, the land from
the side). No Jesus beats. File order HEAVILY scrambled (b05 at
2.88s, b07 at 7.17s, b12 at 95s, b17 at 116s) — build by WINDOW.

- Plates: none auto-matched. GATE shared with 152; SEEKERS varied
  (rows 90/107 clone law).

---

## 🅿️ RUNNER PARK → NEEDS-AUDIO — 2026-08-13 (Machine A `Dev`, Opus runner, headless)

**$0 spent. NO stills generated. Parked at the two-part audio PRE-FLIGHT before touching the meter.**

STALE-V1: row-147 class: durations match (~137.0s) but 11/11 V1-dir mp3s NEWER than the V1 mp4 (new-voice re-record) — so `v2_assemble`'s AUDIO LOCK refuses (the picture runner copies the V1 mp4's audio; `AUDIO_FROM_V1_SEGMENTS` is unset).

**FIX (audio lane, NOT runner — beats_v2.py is off the runner write-list):**
1. Voice-ID the V1-dir `audio/*.mp3` — confirm new-voice ElevenLabs cast.
2. Set `AUDIO_FROM_V1_SEGMENTS = True` in `beats_v2.py` (rebuild audio from the newer mp3s, $0, no re-voice).
3. 0 stills exist → hand back to the picture runner: board State NEEDS-AUDIO → AUTHORED, keep Ready ✅, Claim BLANK.

**RESUME (audio lane):** `python3 media-production-v2/v2_assemble.py 156` (refuses until the flag is set).

---

## ✅ AUDIO-FIX DONE → AUTHORED — 2026-08-13 (Machine A `Dev`, audio lane, $0, 0 stills)

STALE-V1 cleared. **Voice-ID:** all 11 placed V1-dir mp3s
(`media-production/build-156-famine-of-hearing/audio/*.mp3`) ffprobe as
**44100 Hz / 128 k = ElevenLabs new-voice**, and `audio-eleven.log` records all
11 (n1-n8, kv11/kv12 [god], card) cast through the ElevenLabs pipeline — no
edge-tts, no old voice. (The log's "undecided homograph 'does'" notes on n6/n8
are pre-existing render notes, not a Cameron complaint — no PRON fix asked for;
left untouched.) They were newer than the V1 mp4 (old-voice render), which is
why the AUDIO LOCK's STALE-V1-FINAL guard refused the packet-copy.

**Fix:** set `AUDIO_FROM_V1_SEGMENTS = True` in `beats_v2.py`. Track now rebuilt
from the new-voice mp3s at extract_beats offsets — no re-voice, no re-time, V1
read-only, **$0 (no Gemini, no ElevenLabs)**. Verified: extract_beats timeline
reads all 22 phrases cleanly (122.6 s); `v2_assemble 156` no longer refuses on
the audio lock, it stops only at the missing stills — the picture runner's job.

**Handed to the picture runner:** board State NEEDS-AUDIO → AUTHORED, Ready ✅,
Claim cleared. When the runner generates the stills, `v2_assemble` rebuilds the
new-voice track via the flag and ships. Nothing else touched.

---

## ✅ RUNNER SHIPPED (2026-08-24, Machine A `Dev`, Claude session)

Fresh build off the AUDIO-FIX handoff: all 22 stills this session. AMOS copied
byte-identical from build-152 (md5 461726d2… both sides). GATE promoted from b01
(152 had no promoted plate).

**Rerolls: 6/22 = 27% — OVER the 15% budget; honest ledger:**
- b08 ×3: (1) GATE plate CLONED b01's composition (corr 0.985, law 12m);
  (2) plateless reroll came back PAINTED (law 14 ship-blocker); (3) plate-on
  reroll cloned again (0.988). Fix that worked: GATE lock removed from the beat +
  authored geometry moved to a CLOSE side-on two-hands shot → corr 0.166, photo-real.
- b11 ×3: the AUTHORED prompt itself demanded "ridge shrine above and valley well
  below in one frame" — the model obeyed with a stacked two-panel composite
  (Cameron's row-153 complaint class) three times. Two of those rolls were wasted
  by THIS session's own botched prompt edits (unsaved file writes, $0.27 burned —
  recorded so the next session checks its edits landed before rolling). Fix that
  worked: must_show/scene rewritten to ONE camera behind the seekers, valley party
  tiny with true distance → clean single landscape.
- Root lessons: a plate on a second wide of the same place WILL clone the first
  wide — give later same-place beats different authored geometry or drop the
  plate lock; and an authored "X above and Y below in one frame" is a panel
  instruction, not a composition.

**FULL-CUT GATE — 22 beats + card viewed on the ENCODED mp4: PASS.** Famine never
physical (granary heaped, tables full, wells brim; hunger lives in eyes and the
bare niches b03/b14/b19); seekers dignified; b13 map-scale ridge wander; b15 hand
closes on air; b16 shore-as-limit; harvest turn b19-b22 lands with the open book
+ one empty stool. GOD-VOICE captions GREEN only on kv11 (b08) + kv12 (b16) —
Amos 8:11-12, the LORD's exact words; narrator white; no red, no blue (no Jesus,
no quoted-epistle). Encoded similarity matrix: no pair >0.92. Card clean.

**AUDIO:** rebuilt from the 11 new-voice ElevenLabs V1 mp3s
(`AUDIO_FROM_V1_SEGMENTS`) — **AUDIO REBUILD PASS SHA256=b752940116…**, 137.0s,
19.9 MB. **Cost: $3.76 total (22 gens + 6 rerolls)** — still under the $6.10
average despite the overage.
