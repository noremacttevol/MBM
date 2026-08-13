# QC / RUNNER HANDOFF — build-154-everlasting-gospel (Rev 14:6-7)

AUTHORED FROM SCRATCH, 2026-08-05 (Machine A). `--check` PASSES, zero
WARNs. 23 beats, ~129 s. The restored-good-news row (BRIDGE tone,
kept inside Revelation's own frame).

## The angel — row-85 canon, adapted for flight (absolute gates)

REAL robed figure, WINGLESS always, silver-grey layers, strong calm
face, ONE open book; aloft with mantle streaming, held by no visible
means; glory is light from ABOVE him, never from him. Wings = reject.
Light-being = reject. Never the drift words. Same figure in b04,
b06, b08, b14, b17 — face/robe-board.

## No-judgment-imagery gate (b17)

"The hour of his judgment is come" is SPOKEN — nothing fearful is
ever depicted below; the lands LISTEN.

## Dignified dark (b01/b02)

The gospel-less ages are tender longing — few guttering lamps,
lifted hands under sealed overcast; never mocking any people.

## The relighting arc (b21/b22/b23)

Physical flame lamp-to-lamp: the cold wick CATCHING (b21) → the
lane's windows warming one by one (b22) → the lamp held OUT toward
the viewer's edge, receiving hand absent (b23 — the question is the
space). All light physical.

## Other gates

- b12: every-nation variety real (dress/land/feature; rows 90/107
  clone law); ONE sky over all; no favoured group.
- b13: the farthest hut served — remoteness extreme, light's
  arrival unmistakable.
- b10: identical line-shapes on two ages of page — no readable
  text anywhere in the row.
- b15: all FOUR named creations in one panorama (heavens, earth,
  sea, spring).
- JOHN: aged ~90, sea-grey mantle — face-board b03/b07/b08.

## Coverage shape

One true wide with stated geometry: b06 (camera low on the dark
lands taking the height from the side). No Jesus beats. File order
≠ story order (b05 at 53s, b07 at 112s, b18 at 124s) — build by
WINDOW.

- Plates: none auto-matched (clean). PATMOS promote-first from
  b03; ANGEL face-board from b04.

---

## 🅿️ RUNNER PARK → NEEDS-AUDIO — 2026-08-13 (Machine A `Dev`, Opus runner, headless)

**$0 spent. NO stills generated. Parked at the two-part audio PRE-FLIGHT before touching the meter.**

STALE-V1: row-147 class: durations match (~141.3s) but 11/11 V1-dir mp3s NEWER than the V1 mp4 (new-voice re-record) — so `v2_assemble`'s AUDIO LOCK refuses (the picture runner copies the V1 mp4's audio; `AUDIO_FROM_V1_SEGMENTS` is unset).

**FIX (audio lane, NOT runner — beats_v2.py is off the runner write-list):**
1. Voice-ID the V1-dir `audio/*.mp3` — confirm new-voice ElevenLabs cast.
2. Set `AUDIO_FROM_V1_SEGMENTS = True` in `beats_v2.py` (rebuild audio from the newer mp3s, $0, no re-voice).
3. 0 stills exist → hand back to the picture runner: board State NEEDS-AUDIO → AUTHORED, keep Ready ✅, Claim BLANK.

**RESUME (audio lane):** `python3 media-production-v2/v2_assemble.py 154` (refuses until the flag is set).

## ✅ AUDIO-FIX DONE — 2026-08-13 (Machine A `Dev`, audio lane, headless)
STALE-V1 resolved, $0, 0 re-voice:
1. Voice-ID'd all 11 V1-dir mp3s (n1-n8, kv6, kv7, card) = **44100 Hz / 128 k = the chosen ElevenLabs new-voice cast** (no old edge-tts segment).
2. Set `AUDIO_FROM_V1_SEGMENTS = True` in `beats_v2.py` (rebuild from newer mp3s; nothing re-voiced/re-timed; V1 read-only).
3. Pre-flight PASS: `extract_beats 154` = 141.4s / 10 beats; `--check` v4 PASS (23 beats); `audio_audit --rows 154` = **0 old-voice segments**.
4. Handed to the PICTURE RUNNER: board State NEEDS-AUDIO → AUTHORED, Ready ✅, Claim cleared. $0 / 0 Gemini / 0 re-voice.

---

## ✅ REALISTIC-V2 FIRST CUT SHIPPED — 2026-08-13 (Opus runner, Machine A `Dev`, headless)

**COMPLAINT LEDGER: none open.** `.approvals.json` row 154 `approved:false`/`complaint:null`; `v2_outline.py 154` shows no filed complaint. Nothing to regress.

- **Build:** 23 realistic stills at native 2K (V1 was 8 Flow stills). Promote-first boards defeated the text-lock drift: **PATMOS** promoted from b03 (aged John on the rocky Patmos coast — carries setting + John across b03/b07/b08), **ANGEL** face-board promoted from b04 (wingless silver-grey robed figure, one open book — carries the angel across b04/b06/b08/b14/b17). JOHN is a wired GLOBAL_CAST character (front+quarter sheets attached automatically).
- **Angel canon held every beat** (row-85 adapted for flight): REAL robed figure, WINGLESS, silver-grey layers (NOT cream — no Jesus in this row), ONE open book (blank, no readable text), aloft, glory = light from ABOVE him never from him, NO halo/glow/rim-light. Same figure b04/b06/b08/b14/b17.
- **FULL-CUT GATE 6b (per-rendered-frame, my own eyes on the delivered mp4):** extracted one mid-window frame per beat (23) + 2 caption frames + 2 card frames, viewed EVERY one. **23/23 beats + captions + card CLEAN.** John aged/white-haired consistent b03/b07/b08; all four creations in b15 (stars/hills/sea/spring); dignified dark b01/b02; no-judgment-imagery b17 (lands listen); lamp-relight arc correct (b21 cold wick catching → b22 lane windows warming → b23 lamp offered toward the viewer). Realistic-only (Law 14, no cartoon/mix), no modern objects, anatomy/hands/scale clean, no letterbox, no lens-stare. Captions bottom-band only (narrator WHITE, scripture BLUE at kv6/kv7 — no Jesus so no red). Card clean serif, no typo-squares.
- **AUDIO:** `AUDIO_FROM_V1_SEGMENTS=True` (STALE-V1 resolved by the audio lane). AUDIO REBUILD PASS SHA256=6194925f122fe839a84dbd74dff9adda015a47f14c3aaf917734c9fe1c6f6068, 141.401s, 44100/128k ElevenLabs new-voice. concat_base=23==23 beats (no dropped beat); mp4 141.43s ≈ audio 141.40s (no dead tail).
- **Rerolls:** 4/23 = **17.4%** (over the 15% COST-LAW budget by ~2.4 pts — DOCUMENTED overage; all 4 were ship-blockers a single --redo cleared, not subtle drift): **b05** legible Hebrew script → worn indistinct book; **b11** painterly/CGI frame → photoreal people-panorama (Law 14 mix-fail); **b12** collage + disembodied hands + readable text → one coherent every-nation landscape, blank book held from above; **b23** anomalous droopy wick-flame → clean physical oil-lamp offering. Shipping garbage to stay under 15% would violate the FULL-CUT GATE (the higher law).
- **FIX-WAVE (non-blocking, logged for author):** b10's two manuscript pages carry a flowing decorative script that resembles a fictional alphabet (Tengwar-like). Non-readable and contextually an old book in a 3.7s Ken-Burns pan — not obvious garbage. Durable fix = author must_not_show "no lettering of any kind, only worn indistinct stains/creases" on b10 (and b05/b09 for safety).
- **COST:** ~$3.62 this row (27 gens: 2 anchors + 21 main + 4 rerolls) vs the $6.10/row running average — under budget, pushes the average DOWN despite the reroll overage.
- **Ship:** mp4 `revelation-14_everlasting-gospel.mp4` 20.2 MB. Board State RUNNING→BUILT, Appr left ⬜ (Cameron's alone). Deployed to Firebase + live-verified.
