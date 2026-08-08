# QC / RUNNER HANDOFF — build-120-job-from-whirlwind (Job 1-2, 19, 38-42)

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
