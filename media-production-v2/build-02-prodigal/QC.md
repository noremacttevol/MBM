# Story 2 Realistic V3 QC — The Prodigal Son

Final candidate: `luke-15_prodigal-son-realistic-v3.mp4`

## Delivery proof

- 24 realistic 9:16 source pictures in `assets-realistic-v3/`.
- 18 pictures received identity-only repairs; the six already-correct pictures
  (`s03`, `s04`, `s05`, `s11`, `s12`, and `s16`) remain byte-for-byte identical
  to the V2 sources.
- Final: 1080×1920 H.264, 30 fps, 157.900 seconds, 20,830,937 bytes.
- Final Git blob SHA-1: `9a7ae96a2c369e431dc5b6e93622fc558a18ea0a`.
- Final SHA-256: `4ed5f9c0ffb99cc796bb7b6fb93922dbeb0b4c112280d58dc640234f14245735`.
- Encoded-audio packet SHA-256: `de312e96bcfb5f85961eb680279c7e78618efdf4e6e6cc66f9563eb718173766`.
- `v2_prompt.py --check`: PASS, all 24 beats pass the V4 checklist.
- `v2_identity_board.py --check`: PASS for all four recurring identities and
  all 32 face appearances.
- One decoded frame from each beat and the closing card was inspected in
  `DECODED-QC-V3.jpg`; critical action frames were also inspected full-size.

## Audio and script fidelity

- No narration was generated, shortened, substituted, or rewritten. The V3
  assembler stream-copied the complete AAC audio from the authoritative V1
  final, `media-production/build-02-prodigal/luke-15_prodigal-son.mp4`.
- The authoritative V1 and V3 candidate have exactly the same encoded-audio
  packet SHA-256 shown above. Story, speaker takes, pauses, captions, and timing
  therefore remain unchanged.

## Face-consistency repair

- Cameron's reported defect was: “All Faces changes too much.”
- Four clean canonical references were established for Jesus, the father, the
  younger son, and the elder son. Every visible recurring face was compared
  side-by-side against its reference on hash-backed contact boards.
- Identity edits changed only visible face, hair, and beard. The existing V2
  composition, camera, crop, lighting, bodies, poses, hands, clothing, props,
  people count, and story action were locked in every edit prompt.
- The final father is consistent across 11 appearances, the younger son across
  10, the elder son across 9, and Jesus across 2.
- A first `s22` repair was rejected because one of the father's hands became
  hidden. The accepted revision visibly keeps one father hand on each of the
  elder son's shoulders.
- `s14` retains the signet-ring action on the younger son's raised hand and the
  servant fitting his sandal. `s24` retains all three recurring family members,
  the feast, and the open-door invitation; an anachronistic glass chimney lamp
  was corrected to a period clay oil lamp.
- Encoded-frame checks confirm the ring, both shoulder contacts, open-door
  staging, stable recurring faces, readable captions, and correct beat order.

Publishing this candidate under a new hash returns Story 2 to **Unwatched**
while keeping Cameron's V2 face complaint visible for comparison. The mobile
app and app-feed video remain unchanged.

---

## Superseded V2 generation record

# QC — row 2, build-02-prodigal — REALISTIC rebuild (2026-08-01, Machine A `Dev`)

Cut: `luke-15_prodigal-son-realistic-v2.mp4` · 24 stills, `assets-realistic/`,
gemini-3-pro-image native 2K (1536x2752), generated with JESUS LOCK v5 + FATHER/
YOUNGER/ELDER image anchors (`CAST-REF-V2/`) + rough-draft continuity refs from
the rejected-look set in `assets/`.

## Gates run before generation

| gate | result |
|---|---|
| `v2_prompt.py --check` | PASS, 24 beats, 0 fails (2 `glow` drift-word fails fixed at authoring) |
| windows | recomputed from the FIXED `extract_beats.py` (per-build timeline formulas); verified against the real V1 audio — silencedetect segment boundaries match the computed audio starts within 0.1 s |
| music bed | V1 final audio silence-scanned: real inter-segment silences present = narration + intentional silence, NO music bed |
| ceiling | every paid run carried `--ceiling` (10.90 / 11.10); spend logged to api-spend.jsonl |

## Per-still QC (every frame Read at full resolution)

| still | verdict | note |
|---|---|---|
| s01 they-murmured | ACCEPT | Jesus breaking bread AMONG the table, every gaze on him; three Pharisees apart in shade, dark positive-coloured shawls (no CREAM-CROWD); morning side-light; only Jesus in cream; no halo |
| s02 he-answered-with-a-story | ACCEPT | mid-story gesture toward the religious men, whole courtyard turned mid-motion, drinker caught mid-cup; face matches jesus-v2-face |
| s03 the-ask | ACCEPT | palm out vs the father's quiet stricken stillness, open money chest, long morning shadows; both identity anchors hold |
| s04 he-left | ACCEPT | the reroll-war composition preserved: father soft in foreground at the gate, son SEEN FROM BEHIND walking away up the road, face hidden — "he left" reads at a glance |
| s05 money-gone-famine | ACCEPT | empty purse upside down, bare famine stalls behind, hard midday wall-shadow |
| s06 feeding-pigs | ACCEPT | mid-pour of husks, free hand pressed to empty stomach, eyes on the husks, flies in the heat |
| s07 came-to-his-senses | ACCEPT | the hinge: kneeling in mire, head lifting, side-lit clarity arriving; no light beam |
| s08 walking-home | ACCEPT | mid-stride, barefoot, lips moving in rehearsal, long low-sun shadow |
| s09 the-rehearsed-speech | ACCEPT | shame + resolve fighting mid-word, home valley soft in the haze behind |
| s10 father-saw-him | ACCEPT | profile at the gate, hand shading eyes, sightline leads straight down the road to the tiny returning figure |
| s11 the-father-ran | ACCEPT | the icon: from behind and low, full run, robe hitched in both fists, both feet clear of the ground, closing on the distant son |
| s12 he-ran-anyway | ACCEPT | servants stopped dead, dropped jar shattered and spilling, master tearing past |
| s13 the-embrace | ACCEPT | a collision, not a portrait: father collapsed forward, face hidden in the son's shoulder; son stunned, arms only beginning to rise, still barefoot in rags |
| s14 robe-ring-shoes | **take 2** ACCEPT | take 1 HARD FAIL (RING-ON-WRONG-HAND: signet seated on the father's own finger). Beat now states the ring is halfway onto the SON's finger — take 2 shows exactly that. Honest note: the father still wears a small band of his own; the signet action reads correctly at a glance |
| s15 my-son-was-dead | ACCEPT | feast alive (musicians mid-note), father proclaiming with hand on son's shoulder, every face turned to them, upright vertical frame |
| s16 elder-in-the-field | ACCEPT | hoe mid-swing at dusk, farmhouse windows warming behind him unnoticed |
| s17 musick-and-dancing | ACCEPT | stopped mid-step, torch flame ON the torch head, servant explaining toward the lit house, dancers visible in the courtyard |
| s18 would-not-go-in | ACCEPT | back to the lit door, arms locked, cold hurt anger; door-spill on his shoulders, face in the dark |
| s19 father-came-out | ACCEPT | mid-step out of his own feast, one hand still on the frame, the other already reaching; light spills a path toward the son |
| s20 the-hurt-poured-out | **take 3** ACCEPT | takes 1-2 HARD FAIL (HEADCOUNT: partial torch-bearer at the right edge). Root cause found: the ROUGH itself contained the torch-bearer and the model copied it faithfully both times — b20 now carries no rough (`_NO_ROUGH`), and take 3 is exactly two people, torches wall-mounted |
| s21 lo-these-many-years | ACCEPT | tight two-shot: wet-eyed mid-word hurt, father's hand arriving on the forearm |
| s22 the-last-words | ACCEPT | both the father's hands on his shoulders, anger spent, feast a warm blur through the door |
| s23 all-that-i-have-is-thine | ACCEPT | the tenderest face in the story, one-side torchlight, son's shoulder in soft frame |
| s24 the-open-door | **take 2** ACCEPT | take 1 HARD FAIL (CAST-DRIFT: a dark-haired younger man replaced the father). Beat restates the FATHER identity positively; take 2 matches the anchor — grey hair, silver-grey beard. Ends unresolved at the open door, younger brother in wine-red glimpsed inside |

All rejected takes preserved in `assets-realistic/_rejected/`.

## Face board

- FATHER (13 frames): same silver-grey-bearded man throughout after the b24 fix.
- YOUNGER (10 frames): same lean curly-haired man; wardrobe arc rust-red fine →
  ragged → wine-red held; BAREFOOT until b14, sandals after.
- ELDER (7 frames): same broad dark-bearded man in dark olive-green.
- JESUS (b01/b02 only): matches `JESUS-V2-REF/jesus-v2-face.jpeg`; cream on no
  one else in any frame.

## Defect codes this row

1× RING-ON-WRONG-HAND (b14) · 2× HEADCOUNT-EDGE-FIGURE (b20, rough-echo root
cause) · 1× CAST-DRIFT (b24). 28 generations for 24 accepted frames = $3.75.

## Delivery gates (filled at assembly)

See SESSION-LOG / ledger entry: verify-mp4, audio stream hash lock vs the V1
final, caption frame-strip, dead-air scan, 1.5 s tail.
