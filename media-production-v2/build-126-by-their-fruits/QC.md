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

---

## ✅ SHIPPED — realistic-V2 first cut (Opus runner, Machine A `Dev`, headless, 2026-08-13)

**COMPLAINT LEDGER: none open** (`v2_outline.py 126` shows no filed complaint on this row). This is the first realistic-V2 cut of the 2026-07-17 ASSEMBLY-D verse-card placeholder.

- **Build:** 17 painted stills @ native 2K, Matt 7:15-20. FARMER portrait auto-wired via `v2_story_cast` (REFS["FARMER"]=CAST-REF-V2/farmer.jpeg) — kills the text-lock-only farmer drift risk. Jesus beats (b01/b03/b17) auto-attach the V2 master face (green/hazel ref-true eyes — lesson 20, NOT brown-edited).
- **Plates:** ORCHARD promoted from b07 (two doctrinal trees — laden fig + blighted barren — locked by IMAGE across 11 beats; PLACE_REFS["ORCHARD"]). FOLD deliberately NOT promoted: b02 contains the fleece-wolf and promoting it would inject the wolf into b04 (which must be a *human* false-shepherd) — the exact person-in-a-place-plate trap the author flagged for build-21; FOLD's 2 beats carried by its lock text instead. HILLSIDE text-only (the only sibling plates, 121/122, contain Jesus — cannot wire a Jesus-bearing plate to a place).
- **Rerolls: 2/17 = 11.8%** (under 15% COST-LAW budget). Both on **b04**: take 1 rendered a MODERN British hill-farm (galvanized wire fence + buttoned wool overcoat/trousers/boots — historical-coherence fail); take 2 rendered LETTERBOXED (16:9 padded into portrait = grey bars); take 3 clean (full-frame period dry-stone fold at dusk, robed false-shepherd w/ staff+sandals, sheep edged behind). PROMPT-AUTOPSY b04 = **ALLOWED / generator-drift** (b02 rendered period-correct with the same FOLD lock → per-frame drift, not a text defect → --redo, not a text edit).
- **FULL-CUT GATE (one frame per beat from the RENDERED mp4 + 3 caption frames + card): 17/17 + card PASS.** Realistic photography throughout (Law 14, no cartoon/mix). Jesus ONE locked face b01/b03/b17 (cream-only, green/hazel ref-true eyes, calm gaze, no halo, ordinary scale). Wolf frame = unease not violence (fleece draped, sheep unharmed, no blood/lunge). Fire (b14) = orchard branch-fire at distance, axe on the barren trunk only. Two trees consistent via ORCHARD plate. Scratched hand (b08) light, no gore. Market test (b16) = buyer's gaze on the short measure. **SPEAKER LAW pixel-verified:** Jesus KJV segs (j1a/j2/jv18) captions RED, all narrator segs WHITE, NO green (no God-voice) — correct. Captions bottom-band; card clean (no tofu). DROP-CHECK: concat_base = 17 clips == 17 beats (row-173 last-beat-drop risk cleared); mp4 106.1s == audio.
- **FIX-WAVE (non-blocking, for the deep pass):** (1) b12 farmer's hair/beard render fuller & darker than the balding-grey farmer in b05/b06/b09/b14/b15 (5-of-6 consistent; b12 outlier) — harmonize via lesson-10 identity-edit, NOT a blind reroll (preserves the excellent green-fig-vs-black-fig composition). (2) b07/b11 a small grey cloth/mesh on the dry-stone-wall bottom-right corner (ambiguous sackcloth vs netting; mostly behind the caption band / Ken-Burns-cropped) — verify or edit at the deep pass.
- **Audio:** AUDIO_FROM_V1_SEGMENTS=True (audio-lane STALE-V1 fix already applied) → track rebuilt byte-consistent from the 11 V1 segment mp3s, nothing re-voiced/re-timed. **AUDIO REBUILD PASS SHA256 07846dc0…, 106.098s, 19.9 MB.**
- **Cost:** ~$2.67 this row ($0.13 farmer portrait + $0.27 anchors + $2.01 body + $0.26 two b04 rerolls), 11.8% rerolls — under the $6.10 / 19% running average (COST LAW downward trend holds).

Resume (if ever needed): row is BUILT + shipped; nothing pending except the FIX-WAVE items above (deep pass, not a re-cut).
