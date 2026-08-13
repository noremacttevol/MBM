# QC / RUNNER HANDOFF — build-133-what-jesus-called-hell (Mark 9:43-48)

AUTHORED FROM SCRATCH, 2026-08-05 (Machine A). `--check` PASSES, zero
WARNs. 22 beats, ~139 s. Cameron asked for this story BY NAME
(2026-07-20 repeat purge): "Judgment is real; the torturer God is
not. CARE: no horror imagery — the real valley, the real words."

## ⚠ ROW-IDENTITY FIX MADE THIS SESSION

The board listed row 133 as build-133-many-mansions — an ARCHIVED
dupe of live row 185. Slug corrected to canonical
what-jesus-called-hell; a stale V2 many-mansions dir (wrong prep)
deleted; v2_scaffold.py fixed to honor CANONICAL_BUILD_SLUGS (it had
written the scaffold into the archived dupe's dir). Row 134's slug
also corrected on the board (other-sheep → today-in-paradise).

## THE STRICTEST CONTENT-CARE ROW IN THE LIBRARY

- NO horror imagery, ever: no torture, demons, pitchforks, suffering
  figures in fire, maiming. Automatic reject, no reroll.
- Hand/eye verses (b10/b12) NEVER literal: Jesus's own WHOLE raised
  hand and his own clear steady eyes carry the severity. b15's
  craftsman hand is whole and working.
- Topheth (b05/b06): NO children, NO fire, NOTHING enacted — ruined
  shrine stones + the prophet's grief/denunciation only. Absolute.
- b13 (worm/fire): empty ground, low banked embers, thin smoke — no
  figures, no leaping flame.
- Later-tradition art (b01/b17): muddy indistinct canvases only —
  nothing lurid resolves; b17's easel+pigments make the argument.
- b20: the child is SAFE, caught well back from the well's edge.

## The row's argument in frames (check as a set)

Real geography (b02/b03) → real history by ruins+prophet (b04-b07)
→ Jesus owns the severity (b08-b14) → what the images price
(b15) → love's registers (b16/b20) → what tradition added (b17)
vs scripture's own objects (b18) → the purpose: the turn (b19,
rhymes with 117's reversal) → the speaker's character (b21 lamb
carry) → the closing map (b22: Jesus BETWEEN valley and city
lights, hand pointing HOME).

## Coverage shape

One true wide with stated geometry: b22 (camera behind the
listeners' backs at the ledge; two-zone composition — ruin below
one way, warm home-light the other). Seven Jesus beats (b08, b09,
b10, b12, b16, b21, b22). Dim/grey/dusk frames all BY DESIGN (see
header arc). File order ≠ story order (b08 at 4.66s, b11 at 40.98s
before b09's 47s) — build by WINDOW.

- Plates: none auto-matched. VALLEY promote-first from b02, OVERLOOK
  from b09. PROPHET face-board b05/b06.
- Two drift-word FAILs caught and fixed pre-ship ('glowless',
  'glowing' → 'banked', 'warm-lit').

## 🅿️ RUNNER PARK — NOT AUDIO-READY (2026-08-11, Machine A `Dev`, $0)

**Blocked before ANY credit — no stills generated, meter untouched.** The
board said "Audio OK / Ready ✅", but this row cannot be assembled: its audio
is NOT wired for `v2_assemble`. Three independent facts, all measured this
session, prove it (every buildable sibling — rows 100/105/108 — has all three;
this row has none):

1. **No V1 final mp4.** `media-production/build-133-what-jesus-called-hell/`
   has NO `*.mp4`. The locked-mp4 audio path in `v2_assemble.main()` (line ~533,
   `locked_final = <v1dir>/<name>.mp4` → `audio_stream_hash`) has nothing to
   hash → the assemble AUDIO LOCK cannot run.
2. **No V1 segment mp3s.** `media-production/build-133-what-jesus-called-hell/audio/`
   holds only the `.timing.json` files — **zero `.mp3`**. So even the
   `AUDIO_FROM_V1_SEGMENTS` path (`rebuild_audio_from_segments(v1dir,…)`,
   line ~174) would `SystemExit("AUDIO REBUILD: missing V1 segment audio …")`.
   This also makes `extract_beats.extract(133)` itself crash
   (`dur_of('')` ValueError) because the beats carry SEGMENTS text so it does
   not skip them — it probes the missing mp3.
3. **`AUDIO_FROM_V1_SEGMENTS` is not set** in `beats_v2.py` (grep count 0).

The narration DOES exist, just not where assembly reads it: the V1 `segs/`
dir has `audio_mix.m4a` + per-segment `.mp4`s (n0–n6, j1–j3, Jul 28), and the
**V2 dir `media-production-v2/build-133-what-jesus-called-hell/audio/` has all
11 fresh mp3s (n0–n6, j1–j3, card, Aug 5)**. The V1 build got to `segs/` but
its final mux + `audio/*.mp3` were never landed/committed in the V1 dir.

**Why the runner will not fix this:** restoring mp3s into the read-only V1 dir
violates hard-protection #1; setting `AUDIO_FROM_V1_SEGMENTS` edits `beats_v2.py`,
which is an AUTHOR/audio-lane decision outside runner writes (row-69 lesson).
Improvising audio setup is explicitly banned by PROMPT-OPUS-RUNNER.

**RESUME (author / audio lane):** copy the 11 V2-dir mp3s
(`media-production-v2/build-133-what-jesus-called-hell/audio/{n0..n6,j1..j3,card}.mp3`)
into `media-production/build-133-what-jesus-called-hell/audio/`, set
`AUDIO_FROM_V1_SEGMENTS = True` in this build's `beats_v2.py`, then re-run the
$0 pre-flight: `python3 -c "import extract_beats as E; print(E.extract(133)['total'])"`
must succeed, and `rebuild_audio_from_segments` must find all 11. THEN the
picture runner builds the 22 beats on that audio (VALLEY promote-first from b02,
OVERLOOK from b09, PROPHET portrait already made). Until then this row stays
**NOT-READY** — Ready ✅ cleared on AUTHOR-BOARD so no runner burns $6 of stills
that cannot assemble.

## ✅ AUDIO-WIRED → BUILDABLE (author/audio lane, Machine A `Dev`, 2026-08-11, $0)
Executed the RESUME above. Copied all 11 V2-dir mp3s
(`media-production-v2/build-133-what-jesus-called-hell/audio/{n0..n6,j1..j3,card}.mp3`,
all 44100 Hz / 128 kbps mono = the new-voice ElevenLabs spec) into
`media-production/build-133-what-jesus-called-hell/audio/`, and set
`AUDIO_FROM_V1_SEGMENTS = True` in beats_v2.py. Pre-flight now PASSES:
`extract_beats.extract(133)['total'] = 149.897`, `v2_prompt --check` PASS (22 beats,
zero WARNs), `audio_audit` flags 0 old-voice segments. Board → Audio OK, Ready ✅.
Row is now a normal picture build for the Opus runner (VALLEY promote-first b02,
OVERLOOK b09, PROPHET portrait already made). Content-care laws above still bind.

## ✅ V2 FIRST CUT SHIPPED (Opus runner, Machine A `Dev`, headless, 2026-08-13)

REPLACED-story reconciliation VERIFIED before build (swap guardrail): the audio
transcribes as the Gehenna/Mark-9 script (n0 "Many of the pictures people carry of
hell…", n1 "Gehenna is the Greek form of the name Valley of Hinnom…", j1/j3 KJV Mark
9:43-48), new-voice ElevenLabs (44100/128k), CONTENT distinct from live #185
many-mansions (John 14:2); old dupe preserved in build-133-many-mansions. Buildable.

**COMPLAINT LEDGER: none open** (`v2_outline.py 133` shows no filed Cameron complaint —
this is a first cut of a Cameron-requested story). Built to the STRICTEST content-care
spec in this file.

- **22 realistic stills @ native 2K, 149.9s / 20.6MB.** VALLEY promote-first from the
  person-free b02 (clean period Valley of Hinnom: Herodian southern wall, ash heaps,
  thin smolder — the real burning-ground). OVERLOOK left on its text lock (forced
  no-promote: QC named b09 but b09 is a Jesus frame — promoting a Jesus-bearing frame
  is banned, lesson 1046; the only non-Jesus OVERLOOK beat b14 is a tight peopled
  faces-shot unsuitable as a location plate; b09/b22 also lock VALLEY so the valley
  stays anchored there).
- **CONTENT-CARE held (no horror, ever):** no torture/demons/pitchforks/maiming.
  Topheth b05/b06 = the prophet denouncing over ruined stones + ash only, NO children,
  NO fire enacted. Hand/eye verses NEVER literal — b10 = Jesus's own WHOLE raised hand
  (5 fingers, no cut), b12 = his own clear steady eyes; b15 craftsman hand whole &
  working. b13 worm/fire = empty ground, banked embers, thin smoke, NO figures, no
  leaping flame. Later-tradition art b01/b17 = muddy indistinct canvases + easel/pigments,
  nothing lurid resolves. b18 = scripture's own warning OBJECTS (lamp, chaff, broken
  vessel, hearth, shut door). b20 child SAFE, held back from the well's edge.
- **7 Jesus beats** (b08/09/10/12/16/21/22): ONE locked ref face, cream-only every
  appearance, ref-true GREEN/hazel eyes (NO brown iris-edit — rubric lesson 20), no
  halo/glow/rim-light, calm eyes, ordinary scale. Good Shepherd b21, closing "map" b22
  (Jesus between the smoking valley and the warm home-lit city, listeners' backs).
- **Rerolls: 3 paid (13.6% of 22, under the 15% COST-LAW budget) + 1 $0 crop-reuse.**
  b03 + b04 both drifted the wide Valley-of-Hinnom establishing frame to a PRESENT-DAY
  photo (modern apartment blocks, satellite dishes, red-tile roofs, roof water-tanks,
  hanging laundry, plastic trash in the ravine) — a modern-object/Law-6 drift while the
  plate-siblings b02/b07/b13 rendered clean. b04 cleared on 1 `--redo`. b03 stayed
  modern across BOTH rerolls (structural present-day-Hinnom prior for the wide-city
  framing) → hit the 2-reroll cap → fixed at $0 by a tighter PUNCH-IN CROP of the clean
  adjacent b02 (reads as a natural push-in, lesson 1354/1355; `s03.modern-reroll.bak`
  kept).
- **FULL-CUT GATE caught + FIXED a CAPTION↔AUDIO MISMATCH (would-be Cameron complaint).**
  This build's `make_narration.py` SEGMENTS hold an OLD "torture chamber / burning garbage
  dump" narrator draft, but the shipped audio speaks the Gehenna/valley script (verified
  vs every `audio/<seg>.timing.json`). Captions come from SEGMENTS, so every narrator
  caption + the card printed words the voice never says. Fixed with `TEXT_OVERRIDES`
  (n0-n6 + card) = the SPOKEN text; j1/j2/j3 already matched (KJV). Re-assembled → captions
  now match audio (verified in the rendered mp4), AUDIO byte-identical.
- **Assembly:** REPLACED new-story row has no V1 mp4 → set `OUTPUT_VIDEO_NAME` +
  `AUDIO_FROM_V1_SEGMENTS=True` (module-level config, row-140 lesson). No glob collision
  (archived build-133-many-mansions has no beats_v2.py). AUDIO REBUILD PASS
  SHA256=be761e925ecb63f74… Drop-check: concat_base = 22 clips == 22 BEATS (no dropped
  beat); video 149.900s ≈ audio 149.897s.
- FIX-WAVE (non-blocking): b14 background Jesus is authored `jesus:False`/no-ref so he
  isn't ref-locked; he reads plausibly on-model + cream-only and the scene contextually
  intends him (the teacher whose words the listeners react to, lesson 1209) — leave for a
  future author touch (set jesus:True + REF), not a runner coin-flip reroll.

## ✅ QC-VERIFY PASS — FULL-CUT GATE 6b (Opus runner, Machine A `Dev`, headless, 2026-08-13)

Completed the stranded QC-VERIFY claim (prior session committed the claim
`2eb9c7fde ... claim before viewing` but never landed the verdict — it moved on to
rows 139/136/142/145). Approval-guard FIRST: row 133 is MISSING from
`.approvals.json` (never approved, never complained) → eligible for verify, NOT the
approved-row-untouchable case (the 3 AM 2026-08-12 re-cut of approved 1/122/129 is
what that guard prevents; does not apply here). Live card `data-hash` =
`134c98705776d0300051ba38686485fd296cec43` is a real commit whose row-133 mp4 blob
`12afc6dd` == the working-tree mp4; `milk-b4-meat.web.app/review.html` serves that
hash; mp4 URL 302→raw HTTP 200. Claim already `QC-VERIFY 2026-08-13 LIVE` before any
frame was viewed.

**FULL-CUT GATE:** extracted ONE mid-window frame per beat from the RENDERED mp4
(22 per-beat clips c000–c021) + 2 card frames, viewed EVERY one. **22/22 beats + card
CLEAN.**
- 7 Jesus beats (b01/b09/b11/b12/b16/b21/b22): ONE locked face, cream-only, ref-green/
  hazel eyes (no brown iris-edit), no halo/glow/rim-light, ordinary scale every frame.
  b14 background teacher reads on-model + cream (authored no-ref, non-blocking FIX-WAVE
  as noted above — not a Cameron-complaint-level defect).
- CONTENT-CARE (strictest row) held everywhere: NO horror. Topheth b05/b06 = prophet
  denouncing over ruined stones + ash, NO children, NO fire enacted. Hand-verse b10 =
  Jesus's own WHOLE 5-finger raised hand; eye-verse b12 = his own clear steady eyes;
  craftsman b15 whole working hand. Worm/fire b13 = empty ground, banked red embers,
  thin smoke, NO figures, no leaping flame. Later-tradition art b01/b17 = muddy
  indistinct canvases + easel/pigments, nothing lurid resolves. b18 = scripture's own
  warning objects (lamp, chaff, broken vessel, hearth, shut door). b20 child SAFE, held
  back from the well's edge. b22 closing "map" = Jesus between the smoking valley and
  the warm home-lit city, listeners' backs, hand pointing home.
- Realistic-only (Law 14, no cartoon/mix); no modern objects; anatomy/hands clean every
  frame. Captions narrator-WHITE / Jesus-KJV-RED (b10/b11/b12/b13), bottom-band only.
  Reflection card clean serif, no typo-squares. Audio 149.897s ≈ video 149.900s, no
  ≥1.2s dead tail.
- No open complaint on this row → nothing to regress.

**Outcome:** clean row verified, **NO re-cut** ($0/0 gens — a clean row is not touched).
Board Claim → **QC-OK 2026-08-13**. Cut stands as shipped; Appr stays ⬜ (Cameron's alone).
