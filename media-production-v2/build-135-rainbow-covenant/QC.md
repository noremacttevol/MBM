# QC / RUNNER HANDOFF — build-135-rainbow-covenant (Genesis 8-9)

AUTHORED FROM SCRATCH, 2026-08-05 (Machine A). `--check` PASSES, zero
WARNs. 44 beats, ~250 s — the batch's biggest row.

## THE EIGHT ARE ALWAYS EIGHT (this row's own complaint class)

Row 135 IS the counts row in the complaint corpus. EXACTLY eight in
every family frame: Noah (white beard, umber), his wife (moss-green),
three sons (rust/slate-blue/brown), three wives (olive/madder/
charcoal). COUNT THEM in b02, b04, b05, b06, b08, b09, b17, b20,
b22, b24, b25, b27, b29, b36, b38 (+1 born-since child ONLY in b38),
b43. A seven or a nine is an automatic reject.

## Content-care gates

- The drowned world is CLEAN AFTERMATH only: mud flats, waterlines,
  driftwood — NEVER bodies or human wreckage, in any frame
  (b01/b03/b08/b12/b26).
- GOD NEVER EMBODIED: blessing/covenant arrive as light over lifted
  faces (b06/b19/b20/b36); the I-will-look vantage (b35) is an
  aerial view above cloud — no figure, no eye imagery.
- b12's flood memory: the ark on grey water at merciful distance —
  endurance, never catastrophe imagery.

## The bow doctrine set (b30-b35, check together)

Real rainbow, no sparkle effects. The battle-bow vignettes: b31 at
rest on its rack, b33 hung on wall pegs by scarred hands, visibly
UNSTRUNG — never a war scene. b32 reads the rainbow's geometry as
the hung-up bow aimed AWAY. b35 is heaven's-side vantage (above the
cloud-tops looking down).

## The fear arc (the row's heart)

b09 (one cloud, one wary wife) → b16 (Noah's stillness) → b17 (real
grey, the eight drawn together — deliberate weather) → b18 (the
wife's grief, unpunishing light) → b19 (the break) → b29 (wonder
before we see the bow) → b43 (the SAME faces transformed).
Face-board the eight across this arc especially.

## Rhyme frames

- b14 bare furrows → b15 same terrace greened (weeks later) → b39
  same valley, later season, bow up again.
- b38: the string around the child's finger beside the bow — the
  row's tenderest frame; the child appears ONLY here.
- b40/b41/b42: timeless later age — period-neutral, NO modern
  objects (row-7); children's delight in b41, not one fearful face.

## Coverage shape

Two true wides with stated geometry: b03 (the stilled ark — camera
low on the slope, hull from the side) and b08 (camera behind the
eight's backs over the washed valleys). File order HEAVILY
scrambled (b02 at 50s, b12 at 1.49s, b25 at 15s, b36 at 25s) —
build by WINDOW.

- Plates: none auto-matched (clean). ARK promote-first from b03,
  MOUNTAIN from b01, ALTAR from b10, FAMILY face-board from b04.
- Animal pairs (b07/b24): orderly, natural species, calm.


---

## ✅ AUDIO-LANE FIX APPLIED — Opus audio-fix lane, Machine A `Dev`, 2026-08-11, $0

**STALE-V1 resolved (19 newer mp3s / +42.3s).** Added `AUDIO_FROM_V1_SEGMENTS = True` to `beats_v2.py`
(after `REF = True`). The authoritative track is now rebuilt from the V1 narration mp3s
at the extract_beats offsets instead of copying the stale V1 mp4's AAC stream that failed
`assert_v1_final_is_current`. **Validated ($0, no TTS, no Gemini):** rebuilt track = 263.338s,
delta 0.000s vs the mp3 timeline total (guard needs <0.5s). No re-voice — same voices,
wording, timing.

**Row is buildable.** 0 stills, so per the audio-fix protocol the board is flipped to
**AUTHORED / Audio OK / Ready ✅**; a picture runner generates the stills then runs
`v2_assemble.py 135` → AUDIO REBUILD PASS and ships the full cut on this fixed audio.
