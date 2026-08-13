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

## ✅ AUDIO-FIX DONE — 2026-08-13 (Machine A `Dev`, audio lane, headless)
STALE-V1 resolved, $0, 0 re-voice:
1. Voice-ID'd all 11 V1-dir mp3s (n1-n8, kv7, kv8, card) = **44100 Hz / 128 k = the chosen ElevenLabs new-voice cast** (no old edge-tts segment).
2. Set `AUDIO_FROM_V1_SEGMENTS = True` in `beats_v2.py` (rebuild audio from the newer mp3s; nothing re-voiced or re-timed; V1 read-only).
3. Pre-flight PASS: `extract_beats 152` = 131.3s / 10 beats; `v2_prompt build-152-revealeth-his-secret --check` = v4 checklist PASS (21 beats); `audio_audit --rows 152` = **0 old-voice segments**.
4. Handed to the PICTURE RUNNER: board State NEEDS-AUDIO → AUTHORED, Ready ✅, Claim cleared. Runner builds the 21 beats on the now-valid audio and ships. $0 / 0 Gemini / 0 re-voice.

---

## ✅ RUNNER BUILD + SHIP — 2026-08-13 (Machine A `Dev`, Opus runner, headless)

**FIRST-ATTEMPT realistic-v2 cut SHIPPED. 21/21 stills, 131.3s, 0 rerolls (0% vs 15% budget), ~$2.95 incl. portrait (well under $6.10 avg — COST LAW trend DOWN). Meter $708.59.**

- Cross-checked QUEUE.md row 152 = Amos 3:7 "revealeth his secret unto his servants the prophets" — slug matches, NOT swapped. Buildable.
- Approval-guard: `.approvals.json` "152" `approved:False`, `approvedHash:None`, `complaint:None` → not a current approval, not complained. Eligible.
- **AMOS is a TEXT-LOCK spine character (10 beats, HILLS↔GATE) = the top RUNNER-LESSON cross-location-drift BLOCK risk.** DEFUSED by `v2_story_cast.py` which generated + wired `REFS={"AMOS":"CAST-REF-V2/amos.jpeg"}` (the portrait pins identity to an IMAGE). Portrait QC'd first: plain Middle-Eastern herdsman ~45, dark grey-streaked hair+beard, rough brown wool, leather satchel — strong distinctive anchor.
- **Place plate decision:** author QC suggested `HILLS promote-first from b01`, BUT b01 CONTAINS Amos+flock — promoting it would inject the herdsman into the person-free lion beats b15/b17 (rows-114/126 "distinctive subject in a plate" trap). Since AMOS identity is now IMAGE-locked, built HILLS/GATE on text-lock and judged uniformity in the gate. HILLS read consistent across all 8 beats; GATE consistent across 3. No plate needed. PLACE_REFS stays `{}`.
- **Mechanical gates:** `--check` v4 PASS (21 beats); `v2_assemble` AUDIO REBUILD PASS SHA256=17ba1d4eb0f59aa978cd8a98dafe2a08cc86cb838003b697b68fb156269747d1 (AUDIO_FROM_V1_SEGMENTS, 11 V1-dir mp3s, byte-identical, 44100/128k ElevenLabs new-voice); concat_base 21 clips == 21 BEATS (no dropped beat, RUNNER-LESSONS row-173/89); video 131.262 == audio 131.262 (no dead tail); last beat b21 window ends before card_start 118.602.
- **FULL-CUT GATE 6b (one mid-window frame per beat from the RENDERED mp4 + card + captions, EVERY one viewed):** 21/21 + card CLEAN.
  - Amos identity consistent across all 9 appearances (b01/b03/b04/b07/b08/b11/b12/b16/b18) — image-ref held, no HILLS↔GATE drift.
  - GOD NEVER EMBODIED (b03/b04/b08): stilled man + moving wind, no figure, no UFO/disc/orb. LION at distance (b15/b17): far dusk ridge, mid-roar, no attack, not monstrous. Watchmen intentionally DIFFERENT (b05 older+leather-cap vs b20 younger — succession). Household TIMELESS no-modern (b19), children child-sized+dark-haired.
  - Realistic photography throughout, NO cartoon/mix (Law 14); no modern objects (draped cloths not pegged, period balance-scale/oil-lamps/scrolls, indistinct script); clean anatomy/hands; no owl-neck/letterbox/rotation/collage; scale ordinary every frame.
  - Captions narrator-WHITE / scripture-BLUE (b08 "revealeth his secret", b15 "lion hath roared", b16 "Lord GOD hath spoken"), bottom-band only. Card clean serif, no typo-squares.
  - Subtle FIX-WAVE (non-blocking, NOT rerolled per COST LAW): b11 mild travel-direction ambiguity (home village behind him); b20/b21 distant-town borderline-modern at haze distance (no clear high-rise/wire/vehicle); Amos belt-buckle faintly modern (consistent, inherited from portrait).
- **COMPLAINT LEDGER: none open.** `v2_outline.py 152` shows no filed complaint; `.approvals.json` 152 never approved/never complained. Nothing to regress.
- **Ship:** mp4 `amos-3_revealeth-his-secret.mp4` force-added; board Built✅ (Appr left ⬜ — Cameron's alone); review.html card id="v152" data-hash=commit A; deployed Firebase + live-verified.
