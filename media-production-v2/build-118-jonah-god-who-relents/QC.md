## ⛔ C-FIX BILLING RE-CHECK 2026-08-12 (10th board-wide) — Opus runner, Machine A `Dev`, $0, 0 credits

Complaint-first + lowest-waiting → row 118. Staged fix VERIFIED in-file this pass
(b28 scale-cap L953/996 "no single figure looms", b33 living-warm-skin L1146/1164
"plainly alive, never still"); `--check` PASS (46 beats, v4). Real paid probe
`--only b28 b33 --redo --ceiling 645` → `429 prepay depleted` on the immediate try
AND the mandated 60s retry. Meter frozen **$617.34** (last successful gen board-
wide = build-135 @04:11 today). No $0 path (b28 = within-frame relative scale,
b33 = per-figure statue texture; neither croppable). mp4 NOT reshipped. The whole
image board (rows 82/95/116/118, all complained) is frozen on this ONE depletion —
this is the 10th consecutive confirmation of the identical wall; no agent can
manufacture Gemini credits. RESUME the instant billing is funded:
`python3 v2_gen_api.py build-118-jonah-god-who-relents --redo --ceiling 645` → `v2_assemble.py 118` (AUDIO LOCK PASS) → deploy step 7c.

---

## ⛔ C-FIX BILLING RE-CHECK 2026-08-12 (cont.) — Opus runner, Machine A `Dev`, $0, 0 credits

Re-verified this pass: staged fix INTACT (`v2_prompt.py build-118-jonah-god-who-relents --check` = PASS, 46 beats, v4 PASS; grep confirms b28 scale-cap L996 "no single figure looms" + b33 warm-skin L1179 "greys or deadens the skin"). Real paid probe `v2_gen_api.py build-118-jonah-god-who-relents --only v2-r118-b28 v2-r118-b33 --redo --ceiling 645` → **`429 RESOURCE_EXHAUSTED — prepay depleted`** on BOTH the immediate try and the mandated 60 s retry. Meter frozen **$617.34**. The ENTIRE image board is frozen on this one depletion — rows **82, 95, 116, 118** are all parked-billing behind it. No $0 path (b28 = within-frame relative scale, b33 = per-figure statue texture — neither croppable). mp4 NOT reshipped. **RESUME (ships touch-once the instant billing is funded):** `python3 media-production-v2/v2_gen_api.py build-118-jonah-god-who-relents --redo --ceiling 645` → `v2_assemble.py 118` (AUDIO LOCK PASS) → deploy per PROMPT-OPUS-RUNNER step 7c. HARD EXTERNAL BLOCK — only Cameron topping up https://ai.studio/projects clears it.

---

## ⛔ C-FIX BILLING RE-CHECK 2026-08-12 (cont. — PROMPT-WORDING VERIFIED) — Opus runner, Machine A `Dev`, $0, 0 credits

This pass went beyond `--check` and independently re-verified the fix will
actually LAND touch-once when billing returns:

1. **Re-traced + VIEWED the two complained frames from the LIVE mp4**
   (`jonah-1_jonah-god-who-relents.mp4`, the shipped cut): `ffmpeg -ss 157`
   (2:37) and `-ss 188` (3:08). Confirmed with my own eyes — **2:37** the green
   Jonah walking to the gate is a large foreground figure while the townsfolk
   flanking him at the same depth are much smaller = the "3× bigger" complaint is
   real; **3:08** the repentant crowd (esp. the bald grey heads foreground) reads
   as ashen terracotta statues = the "look dead" complaint is real.
2. **Read the FULL staged scene-prose for both beats** (not just the
   `must_not_show` lines) to confirm the words target the defect, since `--check`
   only proves the beat parses:
   - **b28** scene now forces *consistent human scale* — camera high and well
     back, Jonah a SMALL mid-distance figure with his BACK to us, townsfolk
     nearest the lens drawn LARGER than he is, people at his depth exactly his
     height, "no single figure looms out of proportion." This directly negates
     the giant-Jonah frame. Autopsy = **ALLOWED** (original prompt had no scale
     cap) → cap now present.
   - **b33** scene now forces *LIVING warm skin* — flushed, tear-streaked,
     breathing figures, "grief that is plainly alive, never still or frozen,"
     ash smudged on cloth and brow ONLY, "never greys or deadens the skin." This
     directly negates the corpse/statue crowd. Autopsy = **CAUSED** (the
     "ashes" + haircloth monochrome greyed the skin) → warm-living-skin
     constraint now present.
3. **Billing re-probed** with the real paid regen
   `v2_gen_api.py build-118-jonah-god-who-relents --only v2-r118-b28 v2-r118-b33 --redo --ceiling 645`:
   **`429 RESOURCE_EXHAUSTED — prepayment credits depleted`** on the immediate
   try AND on the mandated 60 s retry. Meter frozen **$617.34** (last successful
   gen board-wide was build-135 at 04:11 today, then depletion — same wall as
   rows 82/95).

**No $0 path** — b28 is a within-frame relative-scale defect (a crop can't shrink
Jonah vs the people beside him at the same depth) and b33 is a per-figure skin/
texture defect (a global warm grade can't revive statue-like figures; the frame
is already warm-toned). Both genuinely need a paid Gemini regen.

mp4 **NOT reshipped** — the live cut still carries both bad frames; shipping it
would repeat Cameron's exact complaint.

**RESUME (one command the instant Cameron funds https://ai.studio/projects):**
```
cd media-production-v2
python3 v2_gen_api.py build-118-jonah-god-who-relents --only v2-r118-b28 v2-r118-b33 --redo --ceiling 645
# then FULL-CUT GATE the two regens (view s28 + s33), reassemble, redeploy, verify, ship
python3 v2_assemble.py 118        # must print AUDIO LOCK PASS
```

Row stays **PARKED-BILLING**. GENUINE EXTERNAL BLOCKER — only Cameron's billing
top-up clears it; no agent can manufacture credits.

---

## ⛔ C-FIX BILLING RE-CHECK 2026-08-12 (cont.) — Opus runner, Machine A `Dev`, $0, 0 credits

Re-ran the row-118 C-FIX (Cameron: "2:37 jonah was 3 times bigger… fix it. The
people in 3:08 look dead, fix it."). Staged fix is INTACT and committed
(`beats_v2.py` clean, no uncommitted diff): `AUDIO_FROM_V1_SEGMENTS = True` (L92),
b28 `must_not_show` rejects "Jonah drawn larger than the people around him / any
giant, oversized or hero-scale foreground figure" (L954), b33 `must_not_show`
rejects "grey, ashen, or corpse-like skin; people who look dead" (L1147).
`v2_prompt.py build-118-jonah-god-who-relents --check` = **PASS (46 beats, v4
checklist PASS)**.

Re-probed billing with the paid regen `--only b28 b33 --redo --ceiling 644`:
**`429 RESOURCE_EXHAUSTED — prepayment credits depleted`** on the immediate try;
retried once after 60 s per the hard rail → **same 429**. The board-wide Google
AI Studio prepay is STILL empty (meter frozen **$617.34**; the last successful
gen in `api-spend.jsonl` was build-135 at 04:11 today, then depletion — the same
wall that blocked rows 82/95/118). $0 spent, 0 rerolls.

**No $0 path exists for this row** (unlike row 82's off-center crop): b28 is a
*within-frame relative-scale* defect — a crop cannot shrink Jonah relative to the
townsfolk standing beside him at the same depth; b33 is a *skin-color* defect — a
crop cannot add living warmth to ashen faces. Both genuinely require a paid
Gemini regen. mp4 **NOT re-assembled or re-shipped** — the live cut
(`data-hash=10282aa9cd46`, shipped 2026-08-11) still carries the giant-Jonah b28
and dead-crowd b33 frames; shipping it now would repeat Cameron's exact complaint.

Row stays **PARKED-BILLING**. GENUINE EXTERNAL BLOCKER — no agent can manufacture
credits; only Cameron can top up https://ai.studio/projects. Ships touch-once the
instant billing is funded, via the RESUME COMMAND block below.

---

## RUNNER PARK 2026-08-09 (Opus runner, Machine A `Dev`, UNATTENDED/HEADLESS)

**COMPLAINT LEDGER: none open** (`v2_outline.py 118` shows no complaints;
REVIEW-LESSONS.json has no `118` entry).

**Resumed** the dead 08-07 A-auto build (State RUNNING). Already-shipped check:
no committed mp4, live review card v118 still the OLD 2026-07-24 cut
(`data-hash=0a4a951344bf…`, no `data-review-wave="realistic-v2"`) → NOT shipped,
resume was correct. No live `v2_gen_api` owned the row (only the row-117 lane
was running). `v2_prompt.py --check` PASS (46 beats).

**Generation COMPLETE** — all 46 stills present + valid (no <2KB stubs), 4 place
plates (FISH/HILL/NINEVEH/SHIP) + JONAH portrait wired. `v2_gen_api --dry-run` = 0 shots.

**Light QC (one pass):**
- **s17 (b17) "and here is the first" — 4-panel COLLAGE** (sailors holding Jonah /
  lowering him / Jonah swimming by the fish / crew at the rail) → mandatory reroll
  (RUNNER-LESSONS collage family). Reroll #1 killed the collage but landed the wrong
  moment (harbor boarding, Jonah visible — violates must_not_show "Jonah not visible").
  Reroll #2 = KEEPER: crew at the rail staring at a glassy-calm sea = b17 must_show
  (aftermath, sea gone flat). 2 rerolls = my budget for the frame; kept the best take.
- **s26 (b26) "so he ran" — FIX-WAVE (not rerolled, no open complaint):** rendered a
  SUNSET over the sea he flees toward; QC direction note wanted a SUNRISE at his BACK.
  Also borderline-period leather slip-on shoes. Subtle, not garbage → FIX-WAVE per COST LAW.
- **s17 (b17) FIX-WAVE:** the SHIP plate (promoted from s08 boarding) pulls a
  green-robed figure to the rail that could faintly read as Jonah back aboard; both
  rerolls drifted toward the plate's composition. Ideal fix is a plate-free / de-Jonah'd
  aftermath frame — subtle, kept the best take.
- All other 44 frames: realistic (no cartoon/mix), upright (no rotation), Jonah's teal
  robe consistent, no cream/second-Jesus (no Jesus in this story), fish = same dark whale
  across s18/s23/s27, Nineveh spared on-screen (s33 king repents, s35 relenting) with NO
  destruction shown (care-J), no modern objects, counts read correctly (4 sailors lower at s16).

**PARK REASON — STALE-V1 AUDIO LOCK (row-69 class, author/audio decision):**
`v2_assemble.py 118` built the video track then REFUSED the AUDIO LOCK:
> STALE V1 FINAL: the V1 mp4 (rendered **2026-07-24 10:15:29**, commit `5bd6b82a9`)
> is older than all 22 narration mp3s (**2026-07-28 15:24:05**, commit `3d3e27661`
> "#118 build-118 … narration re-recorded"). Its audio stream predates the current
> narration; copying it would ship stale voices.

Confirmed a GENUINE stale-V1, not the tracked-mtime false alarm: the V1 mp4's audio
is `44100/96425` (old muxed AAC) while the source mp3s are `44100/128000` = the chosen
ElevenLabs cast, re-recorded 4 days AFTER the mp4. `total 278.217` vs V1 mp4 `278.152`
(Δ0.065s) → the re-record kept the same pacing, so the fix is purely mechanical.

The assembler's fix — add `AUDIO_FROM_V1_SEGMENTS = True` to beats_v2.py — is an
AUTHOR/AUDIO-LANE edit (runner hard-rail forbids editing beats_v2.py; RUNNER-LESSONS
§536 "the runner CANNOT fix this … author audio decision … mark NEEDS-AUDIO"; the
audio lane set exactly this flag for rows 185/189/200). So this row is PARKED
NEEDS-AUDIO, Audio→CHECK, Claim carries NO `AUDIO-FIX` token so the audio picker
selects it (low rows first).

**RESUME (audio lane, then picture runner):**
1. `AUDIO_FROM_V1_SEGMENTS = True` in `build-118-jonah-god-who-relents/beats_v2.py`.
2. Verify the V1-dir segments are the chosen cast (already confirmed 44100/128000).
3. `python3 media-production-v2/v2_assemble.py 118` → must print `AUDIO LOCK PASS`.
   After it, check `ffprobe segs/captioned.mp4` duration ≈ `extract_beats card seg_start`
   (262.135, ±0.2s) — STALE-V1 rows can overrun windows (RUNNER-LESSONS §519).
4. All 46 stills are DONE + valid on disk — do NOT regenerate (COST LAW). Ship + deploy.

$0 Gemini beyond 2 s17 rerolls ($0.26, meter 518.31→518.58). No picture defect
localizable to the parked audio; no re-voice attempted (audio-immutability).

---

# QC / RUNNER HANDOFF — build-118-jonah-god-who-relents (Jonah 1-4)

Lesson-12 + complaint-corpus pass done 2026-08-05 (Machine A). `--check`
PASSES, zero WARNs. 46 beats, ~262 s.

## The casting-overboard (the row's hardest action beat — b16)

It is a REQUESTED SACRIFICE, never an execution: four sailors LOWERING
him over the rail with gripped forearms, grief in every knuckle, faces
turned away — never hurling, never violence. Action-logic check every
render: what do the hands appear to be doing? (Lowering, not throwing.)

## The fish (b18/b23/b27)

Whale-vast, dark-backed, ONE calm huge eye — a prepared vessel, never
a monster on the hunt. The belly beat is painterly enclosing dark with
faint sea-light, not gore. Build-30's netted-beach-fish frame was
suggested by the stash and REJECTED (wrong creature class entirely) —
FISH is promote-first from b18. Same creature all three appearances.

## Direction law (Cameron's class)

- b26: Jonah flees WEST — sunrise squarely at his BACK. If the light
  is in his face the frame is wrong.
- b28: this time he walks IN — his back to camera, under the bulls.
- The two commissions are IDENTICAL words — b04 and b25 should rhyme
  visually (listening man, arriving word, no figure of God).

## Scripture-exactness

- God is NEVER embodied (word/sky/light only) — this row predates the
  113 body-order's scope; Jonah hears, never sees.
- Nineveh's destruction NEVER happens and is never previewed — no
  burning-city imagery anywhere, including b19's intact-walls dawn.
- The king repents AMONG his people (b33) — crown set aside, sackcloth
  on his own shoulders; dignity, not spectacle.

## Coverage shape

Nine true wides with stated geometry: b09 (gate crowds from the side),
b10 (storm — camera braced at the stern behind the sailors' backs),
b13 (the self-sentence past the ringed sailors' backs), b17 (calm —
behind the spared crew at the rail), b28 (entering — high behind him),
b31 (the sermon spreading down the great street), b33 (the kneeling
square past a thousand backs), b35 (relenting sky over bowed backs),
b44 (the sixscore-thousand lane from the side). Fourteen flips: lone-
Jonah beats, person-free cityscapes/seascapes, the fish frames.

- Light arc: lamplit night → green-black storm → blue-black deep →
  clean dawn → hazy day → dusk repentance → warm morning argument.
- Plates: build-38 HILL auto-match REJECTED (village doorway ≠ dry
  rise over Nineveh). NINEVEH promote-first from b02, SHIP from b08,
  HILL from b37, FISH from b18.
- Clone-crowd check hardest on b31/b33 (rows 90/107 class) — the
  square holds porters, beggars, soldiers, scribes, women: varied
  faces, varied cloth, all sackcloth by b33.
- Counts law: FOUR sailors lowering at b16.

---

## ✅ AUDIO-FIX SHIPPED — Opus audio-fix lane, Machine A `Dev`, 2026-08-11, $0

Rescued the stranded 08-09 audio-fix lane: it had set `AUDIO_FROM_V1_SEGMENTS = True`
in beats_v2.py (uncommitted) and left 46 valid stills on disk, then died before
assembling. Finished it this session.

- **Audio:** `v2_assemble.py 118` → **AUDIO REBUILD PASS SHA256=172b62c7…**, 278.2s,
  rebuilt from 22 V1 ElevenLabs segment mp3s (all 44100 Hz / 128 k = chosen cast:
  narrator Brian, God/scripture in the eleven cast). The stale ~0.893s tail on the
  old V1 mp4 is dropped. No re-voice — same voices, same wording, same timing. $0.
- **FULL-CUT GATE:** two contact sheets of the rendered mp4 viewed end-to-end —
  consistent Jonah (green robe throughout), realistic biblical photography (no
  cartoon/mix), captions bottom-band only, closing question card clean. No defect.
- **Ship:** mp4 committed `10282aa9cd46…`; review card v118 repointed to the V2
  realistic cut (0a4a951→10282aa9, data-review-wave="realistic-v2"); board → BUILT.
  Deployed `firebase deploy --only hosting` + live-verified.

---

## ⛔ C-FIX PARKED-BILLING — Opus runner, Machine A `Dev`, 2026-08-12, $0, 0 credits

**Cameron's complaint (against the live shipped cut, card hash 10282aa9):**
> "2:37 jonah was 3 times bigger than the people he was walking around, fix it.
> The people in 3:08 look dead, fix it."

### COMPLAINT LEDGER (both open, both CONFIRMED against the RENDERED mp4)
Traced each timestamp to the frame that actually renders at that second
(clip-duration cumulative on `segs/c*.mp4`, NOT beat-name guessing):

- **2:37 (157.0s) → clip c028 → beat b28 `s28-this-time-jonah-went-he.jpeg`**
  (seg n6, "He walked into the great city and cried out his warning").
  Extracted the live frame: Jonah in the sea-green robe stands at the very
  bottom-centre foreground and is ~3× the height of the townsfolk flanking
  him at the SAME depth plane. Complaint CONFIRMED — figure-scale failure
  (rubric lesson 14).
  **PROMPT AUTOPSY = ALLOWED.** The prompt asked for "small Jonah … swallowed
  by the vastness" but the framing line "camera high **behind him** as he walks
  in" invited placing him as the nearest, largest foreground hero, and NOTHING
  capped his size against same-plane people. Missing constraint added.
  **FIX (committed eff25e6df):** rewrote scene + must_show + must_not_show —
  camera "high and well back," Jonah a SMALL mid-distance figure walking away,
  "the ordinary townsfolk nearest the camera are drawn LARGER than he is, and
  the people standing at his own depth are exactly his height … no single figure
  looms out of proportion," + must_not_show now hard-rejects "Jonah drawn larger
  than the people around him / any giant, oversized or hero-scale foreground
  figure." `--check` PASS.

- **3:08 (188.0s) → clip c033 → beat b33 `s33-from-the-king-on-his.jpeg`**
  (seg n7, "From the king … the whole city turned — sackcloth, fasting").
  Extracted the live frame: the front-row kneeling crowd has grey / ashen,
  corpse-like skin and lifeless statue posture — they read as dead. Complaint
  CONFIRMED.
  **PROMPT AUTOPSY = CAUSED.** The scene words "rich and poor alike in rough
  cloth and **ashes** … haircloth across a hundred thousand backs" under a
  uniform dusk monochrome, with no living-warmth constraint, directly produced
  grey ash-skinned corpses.
  **FIX (committed eff25e6df):** rewrote scene + must_show + must_not_show —
  "LIVING people: warm human skin tones, faces flushed and tear-streaked, chests
  breathing … grief that is plainly alive," ash restricted to "cloth and
  foreheads only; it never greys or deadens the skin," + must_not_show now
  hard-rejects "grey, ashen or corpse-like skin; people who look dead, lifeless,
  statue-like or asleep." `--check` PASS.

### Why parked (not shipped)
The two prompt fixes are committed and pass `--check`, but the paid regen 429'd
TWICE (`RESOURCE_EXHAUSTED — Your prepayment credits are depleted`) — the same
Google AI Studio billing depletion currently freezing rows 82 and 95. Retried
once after 60 s per the 429 rule; still depleted. **The mp4 was NOT re-assembled
or re-shipped** — it still carries the giant-Jonah b28 and dead-crowd b33 frames.
Shipping now would repeat Cameron's exact complaint (worst failure), so the row
stays PARKED, the live reviewer keeps the current cut, and no false "fixed" card
goes up.

### RESUME COMMAND (run the instant billing is topped up — the prompt fixes are already in place)
```
cd media-production-v2
# 1) regen the two fixed beats (recompute ceiling from the live meter first)
python3 v2_gen_api.py build-118-jonah-god-who-relents --only b28 b33 --redo --ceiling <meter + 6*0.134*1.5 + 25>
# 2) view the two new frames: b28 = Jonah same scale as the townsfolk near him,
#    no foreground giant; b33 = warm living skin, no grey corpses. Reroll (max 2)
#    if still bad, then run the FULL-CUT GATE on ALL 46 rendered frames.
# 3) re-assemble (must print AUDIO LOCK PASS — audio is byte-identical):
python3 v2_assemble.py 118
# 4) ship: commit mp4+QC+boards, repoint site/review.html v118 data-hash + ?v=,
#    write the "what this cut changed" flag answering BOTH complaints in his words,
#    firebase deploy --only hosting, live-verify the new hash + mp4 HTTP 200.
# 5) board Claim → 'C-FIX 2026-08-12 SHIPPED'; publish_ledger sync; SESSION-LOG.
```
