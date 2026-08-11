# QC / RUNNER HANDOFF — build-120-job-from-whirlwind (Job 1-2, 19, 38-42)

## ✅ REALISTIC-V2 BUILT + FULL-CUT-GATED + SHIPPED (Opus runner, Machine A `Dev`, 2026-08-11)

**42 stills built on the NEW-voice audio (`AUDIO_FROM_V1_SEGMENTS=True`).
AUDIO REBUILD PASS SHA256=3dae1e77c128cd8ae52174a7db3c7a8a456333fc03e222984362dd6e2982d3fb,
258.6 s, 21.0 MB. 0 rerolls / 42 (0% vs 15% budget). Row ≈ $5.76 (1 portrait +
3 anchors + 39 gen, no rerolls) — under the $6.10 average, COST LAW trend DOWN.**

**COMPLAINT LEDGER: none open** (`v2_outline.py 120` shows no complaint; this is a
first-attempt realistic-v2 build, the STALE-V1 park was a new-voice currency fix).

**THE #1 GATE — GOD IS NEVER EMBODIED — HELD.** Every whirlwind beat
(b07/b20/b21/b22/b23/b24/b32/b33/b34/b35/b37/b42) and every cosmic-vision beat
(b25/b26/b29/b31/b36 person-free; b27/b28/b38 Job-only) renders the divine
presence as WEATHER + LIGHT only — a tall storm/whirlwind column with quiet
lightning, no face/mouth/eye/hand/figure in the cloud. b38's washed light is
Job's seeing, viewer sees only light. Verified by extracting one frame per beat
from the RENDERED mp4 (full-cut gate 6b).

**Place plates promoted-first:** ASHES←s10 (single Job on clean ash heap, potsherd,
illness-with-dignity), WHIRLWIND←s20 (storm column + Job before it, no embodiment).
HOME **deliberately NOT promoted** — its anchor b01 is a CROWDED prosperity feast and
HOME also covers the loss beats (b03/b04/b30); per lesson-842/row-114 a crowded plate
bleeds people into solo/loss beats, so HOME renders from its own text (JOB ref holds
identity). Forced no-promote, logged.

**Gates verified frame-by-frame from the mp4:**
- Person-free cosmic beats (b25/b26/b29/b31/b36): all person-free ✓.
- b27 constellations ACCURATE: seven-star Pleiades cluster + Orion with the
  three-star belt (+ red Betelgeuse) ✓.
- Counts: FOUR men in the b12 wide (Job + three distinct friends) ✓; three
  friends carried in b02/b13.
- b30 losses: ruined feast-house at FAR distance + Job's grief, NO bodies, no
  children's deaths shown ✓. Illness-with-dignity (ash-dust, potsherd, never gore) ✓.
- Captions bottom-band only, never over the art. SPEAKER-LAW colours correct:
  narrator WHITE, Job's own KJV (naked-came-I / redeemer-liveth / behold-I-am-vile /
  mine-eye-seeth-thee) light-BLUE scripture, God's KJV (where-wast-thou /
  morning-stars / Pleiades) GREEN. Question card clean, well-margined, doctrinally
  sound (God draws near to the broken — presence not explanation).
- Ear-check b38/s425: caption reads "now mine eye seeth **thee**" (correct KJV, not
  the scaffold typo "seeth thih"); new-voice audio, AUDIO REBUILD PASS is the proof.
- No modern objects, no cartoon/mix (all photographic — Law 14 held), no lens-stare,
  anatomy/hands fine, no second-cream figure (no Jesus in this story), scale correct.

**FIX-WAVE (subtle, author-domain — a runner reroll REPRODUCES them, per
lessons §628/row-15 and §605; kept the takes, 0 budget spent):**
1. Job's head-hair continuity: the arc is largely coherent (fuller hair pre-catastrophe
   s01/s03 → shaved in mourning s05/s06/s09, caption "shaved his head" matches →
   short regrown hair through the long ashes section). The one outlier is **s08**
   (fuller dark hair between shaved s06 and shaved s09). It is portrait-driven (JOB
   ref is haired); a plain reroll defaults back to the haired portrait, so this is an
   author beat-text/portrait item, not a runner reroll. No open complaint on it.
2. **s14** (their-tidy-answers, a tighter friends shot) drops to 2 friends visible;
   the b12 establishing wide carries all four (§605 tight-frame count drift = FIX-WAVE,
   not a reroll).

Continuity that HELD: mantle whole in b01/b03, torn from the mourning beats on;
friends recognizable and distinct across b02/b12/b13; Job's russet robe + dark sash
consistent (only-Job, no cream anywhere).



## 🅿️ RUNNER PARK → NEEDS-AUDIO (Opus runner, Machine A `Dev`, 2026-08-07, $0, 0 credits)

**STALE-V1 (OLD VOICE) — the shipping V1 mp4 predates the ElevenLabs re-record.
Building now would ship the OLD-voice narration = NOT ready under the REDO-ALL
law. Generated NOTHING. No open complaint on this row (`v2_outline.py 120`).**

- V1 mp4 `job-38_job-from-whirlwind.mp4` committed **2026-07-24 10:15:29**.
- All 22 segment mp3s re-recorded **2026-07-28 15:25:04** — commit
  `df1b6bfeb "#120 build-120-job-from-whirlwind: narration re-recorded"` (part of
  the ElevenLabs voice migration batch). So the mp4 = OLD voice, mp3s = new voice.
- Durations essentially match (excess −0.07) so only the RECENCY gate fails:
  `assert_v1_final_is_current` → "22 of the 22 mp3s are NEWER than the mp4."
- `AUDIO_FROM_V1_SEGMENTS` is unset, so `v2_assemble` would stream-copy the OLD
  mp4 audio. Per RUNNER-LESSONS §536/§548, a STALE-V1 row is an author
  audio-config decision → park.

**AUDIO LANE JOB ($0, no re-voice — the new voice is already in the mp3s):** add
`AUDIO_FROM_V1_SEGMENTS = True` to `beats_v2.py`, commit, flip AUTHOR-BOARD row
120 → **AUTHORED + Ready ✅** (0 stills yet). The picture runner then builds all
42 beats on the new-voice audio.

**RESUME (picture runner, after the flag is set):**
`cd media-production-v2 && python3 v2_story_cast.py build-120-job-from-whirlwind`
`python3 v2_gen_api.py build-120-job-from-whirlwind --ceiling <meter + (42+portraits)*0.134*1.5 + 25>`
`python3 v2_assemble.py 120   # must print AUDIO REBUILD PASS`

**COMPLAINT LEDGER: none open.** (The park is a new-voice currency fix, not a
complaint fix.)

---

## ✅ AUDIO-FIX DONE → AUTHORED + Audio OK (AUDIO-FIX lane, Machine A `Dev`, 2026-08-09, $0, 0 credits)

Set `AUDIO_FROM_V1_SEGMENTS = True` in beats_v2.py (before BEATS). Verified $0:
all 22 V1-dir segment mp3s probe `44100,128000` (ElevenLabs new voice), dated
2026-07-29 — they postdate the old-voice V1 mp4 (2026-07-24), so the flag makes
v2_assemble render narration from the NEW-voice mp3s instead of copying the
old-voice mp4 stream (satisfies REDO-ALL). Nothing re-voiced, nothing re-timed,
V1 read-only; no open complaint. 0 V2 stills yet → handed to the picture runner:
it builds all 42 beats on the new-voice audio; **AUDIO REBUILD PASS** in
`v2_assemble.py 120` is the proof the new voice ships. Board flipped
NEEDS-AUDIO → AUTHORED + Audio OK + Ready ✅, claim cleared.

---


AUTHORED FROM SCAFFOLD + lesson-12 + complaint-corpus pass, 2026-08-05
(Machine A). `--check` PASSES, zero WARNs. 42 beats, ~242 s.
NOTE: the board said AUTHORED but this row was a raw scaffold — every
scene, lock and header written this session.

## GOD IS NEVER EMBODIED (the row's #1 gate)

The whirlwind is WEATHER — a vast slow-turning silver-grey column,
veined with quiet lightning, destroying nothing. If any render puts a
face, mouth, eye, hand or figure in the cloud (b20-b24, b32-b37,
b42), reject it without a reroll spent. Same rule for b38's washed
light: the seeing is JOB'S, the viewer sees only light. This is the
rows-102/104/105 reconciliation — Job's scripture hides him.

## CONTENT-CARE gates

- Children's deaths NEVER shown (b30): the fallen-roof feast-house at
  FAR distance + Job's buckling knees carry everything. No bodies.
- Illness with dignity (row-15 grey-sick lesson, b10 on): warm human
  skin under grey ash dust, never corpse-grey; boils by gauntness and
  the potsherd, never gore.
- No Satan, no heavenly council — not in the narration, not pictured.
- The lament (b11) is honest, never grotesque.

## Continuity traps (changing conditions — check every frame)

- Mantle: WHOLE in b01/b03/b04 only; TORN from b05 through b41.
- Head: FULL-HAIRED in b01/b03/b04; SHAVED from b05 on (beard stays).
  b01 is the ONLY prosperous-Job frame — face-board it against the
  ruined frames; same man, different condition.
- File order ≠ story order (scaffold windows): b30 (children) sits at
  13.88s between b03 and b04; b02 (explaining) at 70s; b07/b28 late.
  Build by WINDOW, not by beat number.

## Person-free frames (row-11 phantom-people trap)

b25, b26, b29, b31, b36 end with "No people anywhere in this frame."
Any human figure in a render of these is an automatic reject. b27's
constellations must be ACCURATE — seven-star Pleiades cluster, Orion
with the three-star belt.

## Coverage shape

Two true wides with stated geometry: b01 (the golden estate past the
household's backs — the only prosperity frame, establish HOME once)
and b12 (the seven-day silence behind the three friends' seated
backs — their best act). Everything else singles, close faces,
storm-scale frames and person-free visions — this is an intimate
story told against cosmic backdrops; lesson-12 says exactly this
shape.

- Plates: FRIENDS --take from build-13 REJECTED (those are the
  roof-story friends, different characters). HOME promote-first from
  b01, ASHES from b10, WHIRLWIND from b20.
- Counts law: THREE friends always; FOUR men in b12's frame.
- Ear-check seg s425 (b38): the scaffold narration text carried a
  typo ("seeth thih") — beats text corrected to KJV "seeth thee";
  verify the recorded audio says "thee", else mark NEEDS-AUDIO (audio
  is immutable — never re-voice).
