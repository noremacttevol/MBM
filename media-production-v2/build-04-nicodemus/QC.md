# QC — row 4, build-04-nicodemus — REALISTIC rebuild (2026-08-01, Machine A `Dev`, Claude worker 8)

Cut: `john-3_nicodemus-realistic-v2.mp4` · **34 stills**, `assets-realistic-v3/`,
gemini-3-pro-image native 2K (1536x2752), JESUS LOCK v5 + the build's own
NICODEMUS / NIGHTROOM / COUNCIL / JERUSALEM locks.

## Reclaim

Codex claimed this row (commit `9fc3eeb05`) and then ran out of credits. That
claim commit is the LAST commit touching `build-04-nicodemus` — no progress was
ever committed. The row was reclaimed by push before any spend (`47e461f7e`).

What Codex did leave on disk, uncommitted, was **30 native-2K stills** matching
the current beat names. Those were AUDITED rather than regenerated — 30 pictures
already paid for, and re-rolling them blind would have cost ~$4 for no gain.
27 of the 30 were accepted; the audit is below.

## Two real defects found in the inherited set

1. **Camera-gaze on two Jesus close-ups** (s21 "and then Jesus said", s23 "not
   to condemn") — both were symmetrical portraits looking down the lens.
2. **s26 "an invitation" did not deliver its own beat.** The beat exists to show
   the lamplight full and warm on Nicodemus's face "for the first time in the
   whole conversation"; the inherited frame had his face cold-lit and shadowed,
   i.e. the exact opposite of the point. The lighting requirement was made
   explicit in the beat text and it came back right in one pass.

## The bigger finding: the windows were drifted, and the timeline had holes

Re-checking all 30 windows against the FIXED `extract_beats.py` (absolute times =
`audio_start` + raw phrase time) showed **23 of 30 windows misaligned**, several
by a whole beat — s21 "And then Jesus said the words" was sitting on top of
"For God sent not his Son", and s22 "For God so loved the world" started 12.7 s
after the line itself. Every window was recomputed from the extractor.

Re-timing also exposed **four stretches of narration with no picture at all**,
including a 16 s hole over "the darkest day". Four beats were authored and
generated to close them, so nothing sits on one still for more than ~14 s:

| new beat | window | covers |
|---|---|---|
| b25b `s25b-who-he-was-saying-it-to` | 206.09–211.89 | "Think about who he was saying that to" — the words landing on the man who came in the dark |
| b29b `s29b-they-turned-on-him` | 252.82–265.05 | the council rounding on him in full daylight |
| b29c `s29c-the-darkest-day` | 265.05–272.90 | the barred door, the apostles hiding (no crucifixion, no body — CONTENT-CARE) |
| b30b `s30b-a-hundred-pounds` | 283.27–292.21 | the sheer weight of the spices, a quantity fit for royalty |

Final timeline: 34 beats, 0.28 → 292.21 s, continuous with no gap or overlap,
then the question card to 307.20 s.

## Gates run before generation

| gate | result |
|---|---|
| claim | reclaimed by push (`47e461f7e`) BEFORE any spend |
| `v2_prompt.py --check` | PASS, 34 beats (re-run after every beat edit) |
| windows | all 34 recomputed from the fixed `extract_beats.py`; verified continuous |
| music bed | none — narration + intentional silence only |
| ceiling | every paid run carried `--ceiling` recomputed from the live meter, sliced with `--only` |

## Per-still QC

All 34 frames Read; the 30 inherited ones triaged on the ordered contact sheet
first, with full-size Reads on every frame where gaze, identity or lighting was
in question.

| still | verdict | note |
|---|---|---|
| s01–s12 | ACCEPT (inherited) | the daylight council world, the night street, the knock, "Rabbi, we know", the shuttered side room, the born-again exchange — one consistent Nicodemus throughout, deeply dyed indigo, never pale |
| s13 | ACCEPT | gaze off-lens; the expert handed something that will not fit his categories |
| s14–s20 | ACCEPT (inherited) | "when he is old", the wind beat (the wind never drawn — only the leaning flame), the guard coming down, "How can these things be?" — all off-lens |
| s21 | **take 2** | take 1 CAMERA-GAZE. Take 2: over-shoulder framing on the man he is speaking to, Jesus's gaze off-frame right, V5 face, no lamp-halo |
| s22 | ACCEPT (inherited) | John 3:16 said across a low table to ONE man, not preached |
| s23 | **take 2** | take 1 CAMERA-GAZE. Take 2: three-quarter, gaze off-frame left, both hands open, night window behind |
| s24/s25 | ACCEPT (inherited) | the quietness of it; light and darkness |
| s25b | ACCEPT (take 1, new) | eyes dropped to the flame, the recognition landing — no shame in it |
| s26 | **take 2** | take 1 failed its own lighting requirement (face cold and shadowed). Take 2: he holds the lamp, its warm light full across his forehead, eyes and beard, hope in the face, gaze off-lens |
| s27 | ACCEPT (inherited) | shot from behind, walking away into the first grey light, hood DOWN — the hinge of the whole story |
| s28/s29 | ACCEPT (inherited) | the daylight council; the one voice rising |
| s29b | **take 2** (new) | take 1 put him dead-centre facing the lens under a shaft of window light, with a pale near-white scarf on one councillor (COUNCIL lock bans pale cloth). Take 2: camera well off-axis, Nicodemus in three-quarter profile facing the benches, councillors half-risen and pointing, nobody at the lens, all robes dark |
| s29c | ACCEPT (take 1, new) | the barred door, one man listening against it, one with his face in his hands, hard shutter-blades of daylight — grief and fear without a single wound shown |
| s30 | ACCEPT (inherited) | the burial in the open, full daylight |
| s30b | ACCEPT (take 1, new) | hands lowering the enormous spice bundles, myrrh and aloes spilling on the stone, indigo sleeves, full daylight, no lamp |

## Time-of-day law

Held exactly as the beat map's visual spine requires: b01–b03 and b07 in the
public daylight world, b04–b26 NIGHT (single clay lamp, deep shadow, dark blue
window), b27 the pre-dawn hinge, b28 onward FULL DAYLIGHT with no lamp anywhere.
No lamp rim-lights Jesus's head in any night frame.

## Reroll rate

**4 defect passes across 34 keeps = 12%** — against the ~30% that had held on
every previous row. The three rerolls generated after the shared `DEFECT_LOCK`
went into `v2_prompt.py` all passed on the next attempt, and 3 of the 4 new
beats were right on take 1.

Spend this row: $1.07 (3 audit rerolls + 4 new beats + 1 reroll). The 30
inherited stills cost this session nothing.

## Delivery gates

| gate | result |
|---|---|
| AUDIO LOCK | PASS — encoded stream SHA256 `5e23f1c7…`, byte-for-byte identical to the approved V1 final |
| verify-mp4 | OK — video 307.23 s / audio 307.18 s / 19.3 MB |
| rendered frames | 12 frames extracted and eyeballed: captions bottom-band only, narrator white, scripture-voice blue ("Rabbi, we know"), Jesus's KJV red across John 3:16, card margins clean, and every caption lands on the picture it belongs to now that the windows are re-timed |
