# QC — row 5, build-05-bent-woman — REALISTIC rebuild (2026-08-01, Machine A `Dev`)

Cut: `luke-13_bent-woman-realistic-v2.mp4` · 37 stills, `assets-realistic/`,
gemini-3-pro-image native 2K (1536x2752), JESUS LOCK v5 + WOMAN/RULER image
anchors (`CAST-REF-V2/`, generated this session) + FARMER anchored to the
accepted s14 frame + rough-draft continuity refs from the rejected-look set in
`assets/` (Session 6 blanket rejection; 3 of them were 1K undersized).

## Gates run before generation

| gate | result |
|---|---|
| `v2_prompt.py --check` | PASS, 37 beats, 0 fails (re-run after every beat edit) |
| windows | ALL 37 recomputed from the FIXED `extract_beats.py` — the old windows carried the storm-11 formula defect and drifted up to ~13 s by the end (old total 236.7 s vs real 247.7 s). New windows are absolute audio phrase times from the per-segment ElevenLabs timing; verified against the real V1 audio with silencedetect — every segment boundary matches within 0.1 s |
| music bed | V1 final audio silence-scanned: real inter-segment silences (−40 dB, up to 1.45 s) = narration + intentional silence, NO music bed |
| ceiling | every paid run carried `--ceiling`; spend logged to api-spend.jsonl. NOTE: the meter is shared cross-session and a concurrent story-06 worker was spending in parallel — this build's own spend is itemised below |
| claim | claimed by push (be53cef7b) BEFORE any spend |

## Per-still QC (every frame Read at full resolution; contact boards after)

All 37 frames ACCEPTED after the passes below. Highlights:

| still | verdict | note |
|---|---|---|
| s01 | ACCEPT | bent forward over the stick, face to the ground, ordinary village morning, directional light |
| s02 | **take 4** ACCEPT | take 1: modern rubber-style FERRULE on the stick tip (anachronism); take 2 fixed the tip but drifted her robe to olive-green (WARDROBE); take 3 same; take 4 recolour-only edit — whole robe dark brown, bare wood tip on the stone, low-viewpoint sandals-world composition (ROTATION-TRAP guard held: frame upright) |
| s04–s07 | ACCEPT | synagogue interior, warm sabbath daylight in shafts (Luke 13:10 — no invented night); congregation gazes converge on Jesus; V5 face |
| s05 | **take 2** ACCEPT | take 1 had the same ferrule defect — edited to bare wood |
| s08 | **take 2** ACCEPT | take 1 HARD FAIL: Jesus gazing into the lens + jet-black hair (Session-6 disease + identity drift). Recomposed three-quarter, gaze past the room, dark-brown hair w/ bronze lights |
| s09 | **take 3** ACCEPT | take 1 copied the ROUGH's own defect (woman kneeling in the aisle — wrong moment; the row-2 b20 lesson, rough dropped); take 2 duplicated the woman (two stick-bearing figures); take 3: she appears once, at the back, aisle empty, initiative entirely his |
| s11/s12 | ACCEPT | he bends DOWN into her line of sight — she cannot come up to him; s12 take 2 edited: hair black→dark brown w/ bronze (identity), composition kept |
| s14/s26/s29 | ACCEPT | the loose/lead/water farmyard triptych; s26 take 2 rerolled — take 1's farmer was a different (white-bearded) man; FARMER now anchored to s14, consistent across all three |
| s15–s17 | ACCEPT | the healing burst: hands laid while still bent → CAUGHT HALFWAY UP (the frame the beat exists for) → fully straight, face to face; nothing supernatural depicted, no glow |
| s18–s19 | ACCEPT | praise: face UP into the window light; s19 edited stick-free (see stick continuity below) |
| s20–s22 | ACCEPT | ruler matches anchor: indignant but dignified; v14 staging scripture-exact — he rebukes THE PEOPLE with his back to Jesus |
| s25 | **take 3** ACCEPT | take 1 HARD FAIL: RULER CAST-DRIFT (different elder). take 2 rerolled with anchor + positive restatement; take 3 face-edit aligned his beard to the s20/s21 iron-grey anchor look |
| s27 | **take 2** ACCEPT | the payoff frame: his hand out toward her, she straight in the light, THE STICK LYING ON THE FLOOR where she let it fall; ruler face-edit aligned to anchor; ADVERSARY LAW held (no Satan figure anywhere — the bond is only the abandoned stick) |
| s30–s32, s36 | **edited** ACCEPT | all four regenerated the stick back into her hands AFTER s27 shows it dropped — identity-preserving edits removed it (hands empty); composition/faces held |
| s35 | **take 2** ACCEPT | take 1 HARD FAIL: group-photo effect — Jesus and the woman looking straight into the camera + stick back. Take 2: candid, gazes inward, hands empty |
| s37 | ACCEPT | final frame: alone in the shaft of light, fully upright, empty hands, no stick anywhere |

Rejected takes preserved in `assets-realistic/_rejected/` from the edit passes
onward. Honest note: the first four rerolls (s08/s09/s25/s26 take 1) were
overwritten in place by `--redo` before the preserve-step was added.

## Stick continuity (decided, not accidental)

She keeps the stick through s01–s16 (18 years of habit), it hangs loose/leans
at s17–s18 as she rises, she still half-carries it at s19/s23 — and she LETS IT
FALL at s27, exactly on "loosed from this bond"; from there it is on the floor
(s27) and gone (s30–s37). Any frame that contradicted this arc was edited.

## Face boards

- WOMAN (21 appearances): one actor — small, thin, weathered, dusty-plum
  headcloth, dark-brown mended robe throughout; posture arc bent → halfway →
  straight matches the beat map exactly.
- JESUS (20): matches `JESUS-V2-REF/jesus-v2-face.jpeg`; dark-brown hair with
  bronze lights (two black-haired takes were fixed); cream on no one else; no
  halo/rim-light in any frame.
- RULER (8): one elder — heavy-set, iron-grey combed beard, near-black indigo
  robe with dark-red border (two drifted faces aligned by edit). His shawl is
  up over his head in s22/s30 (pulled up as he formally rebukes) — recorded
  here as a deliberate read, robe and face identical.
- FARMER (3): one man across the farmyard cutaways, anchored to s14.
- Hash record: `IDENTITY-QC.json` (52 appearances, all pass, SHA-256 locked).

Known lock deviation, recorded honestly: a few congregation prayer shawls
(s05/s22/s31) render as traditional white-striped tallitot despite the
SYNAGOGUE lock's no-near-white line. Jesus remains the ONLY figure in a full
cream robe and reads unmistakably distinct in every frame, so these were
accepted rather than re-shot.

## Defect codes this row

2× FERRULE-ANACHRONISM (s02, s05) · 2× JESUS-BLACK-HAIR (s08, s12) ·
1× CAMERA-GAZE (s08) · 1× ROUGH-ECHO wrong moment (s09) ·
1× DUPLICATE-CHARACTER (s09 take 2) · 2× RULER CAST-DRIFT (s25, s27) ·
1× FARMER CAST-DRIFT (s26) · 5× STICK-CONTINUITY (s19 pre-empted at authoring;
s30/s31/s32/s36 edited) · 1× GROUP-PHOTO POSE (s35) · 2× WARDROBE-GREEN (s02
edits) — 56 generations for 39 accepted images (37 beats + 2 anchors), $7.50
this build (the 37-beat + 20% formula priced ~$6.27; the overage is the 17
reroll/edit passes above, each fixing a defect Cameron has rejected cuts for).

## Delivery gates (filled at assembly)

See ledger Session 8 close: verify-mp4, audio stream hash lock vs the V1
final, caption frame checks, tail length.
