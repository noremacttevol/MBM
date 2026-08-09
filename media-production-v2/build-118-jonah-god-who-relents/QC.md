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
