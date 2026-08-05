# QC — row 9, build-09-rich-ruler — REALISTIC rebuild (2026-08-01, Machine A `Dev`, Claude worker 6)

Cut: `mark-10_rich-ruler-realistic-v2.mp4` · 31 stills, `assets-realistic/`,
gemini-3-pro-image native 2K (1536x2752), JESUS LOCK v5 + RULER image anchor
(`CAST-REF-V2/ruler-ref.jpeg`, generated this session) + the four named
disciples in s21 anchored to the shared `CAST-V2-REF/` library sheets +
rough-draft continuity refs from the rejected-look set in `assets/` (Session 6
blanket rejection; 21 of 31 beats had roughs, 11 were used — the other 10
roughs carried the exact defect their beat must avoid and were dropped
up-front per the rough-echo lesson, recorded in the beats_v2 docstring).

## Gates run before generation

| gate | result |
|---|---|
| `v2_prompt.py --check` | PASS, 31 beats, 0 fails (re-run after every beat edit) |
| windows | ALL 31 recomputed from the FIXED `extract_beats.py` — the Jul 29 windows carried the raw-vs-trimmed drift (card at ~177 s vs real 189.03 s, ~12 s late-story error). New windows are absolute audio phrase times (leading silence rides inside each segment's mp3, so audio_start + raw phrase time IS absolute); the three sub-phrase splits (n0b p4a/p4b at the "everyone," breath, j1 a/b/c at the real KJV clause pauses) were placed with silencedetect on the actual V1 mp3s |
| music bed | none — narration + intentional silence only (V1 audio copied packet-for-packet) |
| ceiling | every paid run carried `--ceiling` recomputed from the live shared meter and sliced with `--only`; a concurrent story-08 worker was spending in parallel and ate two ceilings mid-run exactly as the Session 8 lesson predicts — each stop was resumed with a fresh ceiling; spend itemised below |
| claim | claimed by push (68446d47d) BEFORE any spend |

## Per-still QC (contact sheets for triage, 100%-scale face-crop boards, full-size Reads on every retake and both weight-bearing frames)

All 31 frames ACCEPTED after the passes below. Highlights:

| still | verdict | note |
|---|---|---|
| s01 | **take 2** ACCEPT | take 1: Jesus gazing into the lens, face drifted off V5, and a bead NECKLACE (no-ornament violation). Take 2: V5 face, gaze up the road, no ornament, distant runner reads at a glance |
| s02 | **take 2** ACCEPT | take 1 echoed the (dropped) rough anyway: a dignified jog, robe not gripped. Take 2 is a genuine sprint — robe flying, dust, townspeople staring |
| s03 | **take 2** ACCEPT | same jog defect in take 1; take 2 sprints past the two appalled men of his own rank |
| s04–s07 | ACCEPT | arrival, kneeling, "Good Master" close-up (blue scripture-voice caption verified on the rendered frame), the listening pause — all first takes, roughs held |
| s05 | ACCEPT + noted | one background villager wears a light-tan robe — noticeably lighter than the crowd but clearly darker/greyer than Jesus's cream; Jesus reads unique in-frame. Accepted, recorded honestly (same class of deviation as row 5's tallitot note) |
| s08 | **take 2** ACCEPT | take 1 HARD FAIL: Jesus SEATED on a ledge making a two-finger sign — the rough's own defect reproduced even with the rough dropped (the scene text never said "standing"; it does now). Take 2: standing over the kneeling man, counting on his fingers |
| s09 | **take 1 restored** | take 2 came back standing and posed at the lens; take 1's only flaw was a roadside dry-stone wall reading close behind him — which the ROAD lock itself puts on both sides of the road. Take 1 is the truthful candid frame |
| s12 | **take 2** ACCEPT | ⚠️ the most important frame. Take 1's love read through lowered lids (risk of reading as sadness); take 2 has the eyes OPEN, luminous, fixed on the man with a faint warm smile — unmistakably love, V5 identity exact, no glow. Take 1 preserved in `_rejected/` |
| s14 | **take 2** ACCEPT | take 1 had an out-of-focus cream shoulder+head at the frame edge — a stray unlocked Jesus in a frame whose must_not bans him. Take 2: the man entirely alone, gaze lifted above the lens at the off-frame Jesus, rings plain on both hands |
| s17 | ACCEPT | the poor at the gate, dignified — and the rendered frame at 98 s carries the red KJV "and give to the poor" exactly over them |
| s19/s20 | ACCEPT | the ring-clutch as the price lands; the offered open hand held steady with the warm face above it |
| s21 | **take 2** ACCEPT | take 1 failed the cast law: John short-haired (his lock is long flowing light-brown hair), James off-sheet, two gazes near the lens. Take 2: all four match the CAST-V2-REF sheets at a glance (Peter arms-folded/heavy brows, Andrew in his olive tunic, long-haired James, young clean-shaven long-haired John), all four gazes angled off-frame left at the encounter |
| s22 | **take 2** ACCEPT | take 1 CAMERA-GAZE; take 2 lost profile turned back toward the town he owns |
| s23–s26 | ACCEPT | the face falling, the no-argument silence, the wet-eyed profile, the walk away shot from behind (face hidden, nobody following) |
| s27 | **take 4** ACCEPT | take 1 ACTION-LOGIC FAIL (Jesus facing the camera while the departing figure walked away BEHIND him); take 2 muddied the read with three stranger figures on the road; take 3 was burned by a text-edit that failed to apply before the reroll (recorded honestly — the prompt regenerated unchanged); take 4: camera behind Jesus's shoulder, the solitary purple-robed figure small down the road, arms loose, nobody else anywhere |
| s28 | **take 3** ACCEPT | take 1 CAMERA-GAZE; take 2 had a figure walking away down the road — at a glance it read as someone chasing the man, the exact thing the narration denies. Take 3: road beyond the group completely empty, Jesus in profile, one disciple's half-step-and-question held |
| s29 | ACCEPT (take 1) | ⚠️ the second weight-bearing frame, right first time: wet eyes with real tears, the same love as s12 now carrying grief, watching down the road, warm low light, zero glow |
| s30/s31 | ACCEPT | the empty road at sunset (not one person — the narration's "The road emptied. The sun went down." makes sunset CORRECT here, see the beats_v2 TIME-OF-DAY note); s31 **take 2** — take 1 had Jesus facing toward the camera with the town behind him (facing the wrong way); take 2 is shot from behind, his face turned away toward the town, still looking the way the young man went |

Rejected takes preserved in `assets-realistic/_rejected/` (11 take-1 files +
later takes; the b31 take 1 is `s31-...take1.jpeg`).

## Face boards

- JESUS (17 appearances): matches `JESUS-V2-REF/jesus-v2-face.jpeg` — V5 hair
  (dark brown with bronze lights), luminous green-amber eyes, cream on no one
  else, no halo/rim-light in any frame.
- RICH YOUNG MAN (21): one actor, anchored to `CAST-REF-V2/ruler-ref.jpeg` —
  tidy dark hair, trimmed short beard, large earnest brown eyes, Tyrian-purple
  robe over deep indigo, gold rings; likeable and sincere in every frame,
  never smug (the row's stated QC watch-point).
- PETER / ANDREW / JAMES-Z / JOHN (1 each, s21): match the CAST-V2-REF sheets.
- Hash record: `IDENTITY-QC.json` (42 appearances, all pass, SHA-256 locked).

## Defect codes this row

1× CAMERA-GAZE+FACE-DRIFT+ORNAMENT (s01) · 2× SPRINT-ECHO (s02, s03 — the
dropped rough's jog reproduced from the scene text alone) · 1× SEATED-STAGING
(s08) · 1× POSED-AT-LENS (s09 take 2, rejected in favour of take 1) ·
1× LOWERED-LIDS on the love frame (s12) · 1× STRAY-BLURRED-JESUS (s14) ·
1× CAST-LAW FAIL John/James + gaze (s21) · 1× CAMERA-GAZE (s22) ·
1× ACTION-LOGIC direction (s27) + 1× STORY-READ three strangers (s27 t2) +
1× WASTED-REROLL unapplied prompt edit (s27 t3) · 1× CAMERA-GAZE (s28) +
1× CHASE-READ walking figure (s28 t2) · 1× WRONG-FACING (s31).

**Spend: 46 generations for 32 accepted images (31 beats + 1 anchor) ≈ $6.16
this build** (32 keeps + 14 defect passes at $0.134; the formula 31+20% priced
~$5.00 — the overage is the reroll passes above, each fixing a defect class
Cameron has rejected cuts for). Meter shared cross-session; this build's rows
are the `build-09-rich-ruler` entries in `api-spend.jsonl`.

## Delivery gates

| gate | result |
|---|---|
| AUDIO LOCK | PASS — encoded stream SHA256 `925aaf90…` equals the V1 final `mark-10_rich-ruler.mp4` packet-for-packet |
| verify-mp4 | OK — video 196.87 s / audio 196.84 s / 21.9 MB |
| rendered frames | 14 frames extracted and eyeballed across the cut: captions bottom-band only, narrator white, scripture-voice blue on "Good Master…", Jesus's KJV red across j1 (the "give to the poor" clause lands ON the picture of the poor), card margins clean, sunset only after "The sun went down" |

## OPEN CAMERON COMPLAINT — gates before rebuild

"The young rich man lost his beard at 52 seconds. The picture at
1:14 is dumb and not needed."
1. BEARD BOARD (rubric lesson 13): the RULER's short dark beard is
   present and identical in EVERY beat he appears in — step through
   all his frames checking only the beard. Hardest at b10 (0:52).
2. b13 (1:14) was REPLACED with the counter-shot to b12: the young
   man's face alone, being loved. It must NOT read as a repeat of
   b10/b12 — a genuinely different composition or the complaint
   stands.
