# QC — row 8, build-08-lost-coin — REALISTIC rebuild (2026-08-01, Machine A `Dev`, Claude worker 5)

Cut: `luke-15_lost-coin-realistic-v2.mp4` · 12 stills, `assets-realistic/`,
gemini-3-pro-image native 2K (1536x2752), JESUS LOCK v5 + WOMAN image anchor
(`CAST-REF-V2/woman-ref.jpeg`, generated this session) + rough-draft continuity
refs from the rejected-look 2026-07-29 set in `assets/` (Session 6 blanket
rejection — that set also carried the pre-V5 Jesus face, so it could not be
reused directly; every beat regenerated).

## Gates run before generation

| gate | result |
|---|---|
| claim | claimed by push (c035f59f2) BEFORE any spend |
| `v2_prompt.py --check` | PASS, 12 beats, 0 fails (re-run after every beat edit) |
| windows | ALL 12 re-timed from the FIXED `extract_beats.py` — the old windows carried the raw-vs-trimmed drift (jv8 6.93 vs real 7.45; n5 55.70 vs real 59.94 — up to 4.2 s late). New windows are absolute phrase times; verified against the real V1 audio with silencedetect (every segment onset within 0.1 s). The b02/b03 split inside jv8 (10.60) sits in the measured mid-sentence pause after "silver," (raw jv8.mp3 silence 2.80–3.50 → absolute 10.25–10.95). Stale `beats.json` regenerated from the fixed extractor. |
| ceiling | every paid run carried a hard `--ceiling` recomputed from the live shared meter, sliced with `--only` (Session 8 shared-meter lesson; a story-09 worker was spending in parallel); spend logged to api-spend.jsonl |
| prior reviewer lesson | "You cut the original video short" — RESOLVED, not regressed: the full 68.8 s V1 audio is stream-copied and the encoded-audio hash lock passed |

## Per-still QC (every frame Read at full resolution; coin counts verified on zoom crops)

| still | verdict | note |
|---|---|---|
| s01 | **take 2** ACCEPT | take 1 ROUGH-ECHO: copied the rough's pre-V5 Jesus face (dark-eyed, no bronze lights) — rough dropped for b01 (row-2 b20 lesson); take 2 carries the V5 face, open-hand story gesture, gazes converge, no camera-gaze |
| s02 | **take 3** ACCEPT | takes 1–2 COIN-COUNT FAIL (12 coins both times, the model cannot count a loose pile); beat restated as NINE in a straight row + the TENTH held up between finger and thumb — take 3 counts exactly 9+1, hands clear of the row |
| s03 | **take 2** ACCEPT | take 1 COIN-COUNT FAIL (ten coins remained beside the gap); restated as FIVE left of the gap, FOUR right — take 2 counts exactly nine, hand stopped dead above the empty space |
| s04 | ACCEPT | first frantic seconds: cloth shaken out, nine coins spilled on the stone, no lamp yet |
| s05 | ACCEPT | clay OIL LAMP (KJV "candle"), wick just caught, sheltering hand, flame the only light — no wax candle anywhere in the build |
| s06 | **take 2** ACCEPT | take 1 EDGE-INTRUDER: a strange man sat in her doorway (she lives alone in the parable); "COMPLETELY ALONE" line added — take 2 broom in contact mid-stroke, dust rolling, lamp down on the stones, head turned listening for the ring |
| s07 | **take 4** ACCEPT | take 1 ROTATED 90°; take 2 upright but a blurred bare-legged figure stood outside the open door (reads unclothed — hard fail); take 3 ROTATED again — the rough itself invites the rotation (low-viewpoint composition), rough dropped (ROTATION-TRAP); take 4 upright, cheek low, lamp raking the stones, room taken apart |
| s08 | ACCEPT | the find: dull coin pinched up into the lamplight, face breaking open, hand to chest — nothing supernatural, no light off the coin |
| s09 | ACCEPT | doorway in hard daylight, coin held high, neighbours already coming (jar on hip, child running); rooftop cylinder zoomed — reads as clay vessel, not modern |
| s10 | ACCEPT | courtyard full: a dozen neighbours, laughter, platter of bread and olives, children — a street's worth of joy over one small coin |
| s11 | **take 3** ACCEPT | take 1 CAMERA-GAZE (Jesus straight into the lens — the Session 6 disease); take 2 fixed Jesus but two centre women stared into the lens (GROUP-PHOTO); take 3 candid — his gaze on the listeners, every face turned to him, no angels/sky-shaft/halo (CONTENT-CARE held: v10's angels are NOT painted) |
| s12 | ACCEPT | one ordinary tax collector's face, eyes shining fixed past the lens, jaw loose — the story landing on one person; no starfield anywhere in the build (V1 used stars.jpeg for 4 of 6 stills) |

Rejected takes preserved in `assets-realistic/_rejected/` (7 takes).

## Face boards

- WOMAN (9 appearances, s02–s10): one actor — about forty, sun-weathered,
  dusty-ochre headcloth, dark russet-brown mended robe, thin work-roughened
  hands; anchored by `CAST-REF-V2/woman-ref.jpeg` attached to every beat.
- JESUS (2 appearances, s01/s11): matches `JESUS-V2-REF/jesus-v2-face.jpeg`
  (V5 lock); cream on no one else; no halo/rim-light in any frame.
- Hash record: `IDENTITY-QC.json` (11 appearances, all pass, SHA-256 locked);
  boards in `identity-boards/`.

## Defect codes this row

1× ROUGH-ECHO pre-V5 Jesus (s01) · 3× COIN-COUNT (s02 ×2, s03) ·
1× EDGE-INTRUDER (s06) · 2× ROTATION-TRAP (s07 takes 1/3) ·
1× UNCLOTHED-FIGURE in doorway (s07 take 2) · 1× CAMERA-GAZE Jesus (s11) ·
1× GROUP-PHOTO crowd gaze (s11 take 2) — 23 generations for 13 accepted images
(12 beats + 1 anchor), $2.95 this build at $0.134/image.

## Delivery gates

| gate | result |
|---|---|
| AUDIO LOCK | PASS — encoded AAC stream hash e219f876… identical to the V1 final `luke-15_lost-coin.mp4` (68.82 s audio, zero re-voicing) |
| verify-mp4 | OK — video 68.833 s, audio 68.824 s, 19.9 MB, 1080x1920 30fps |
| rendered frames | 13 frames extracted across the cut and eyeballed: captions bottom-band only, narrator white / KJV Jesus words red, splits land with the voice, KJV question card and ~1.5 s tail present, no music bed |
