# V2 PRODUCTION LEDGER

State of record for the V2 picture rebuild. **The repo is the memory; this file is
the state.** A fresh session reads `V2-KICKOFF.md` top to bottom, then this ledger,
then continues at the first row that is not DONE (finishing any IN-PROGRESS row from
its last completed step A–I).

Status values: `DONE` / `IN-PROGRESS (last step X)` / `BLOCKED(reason)`.

---

## Session 1 — 2026-07-28

- **Model:** Opus 5 (Claude Code), switched to Fable 5 by Cameron ~23:05
- **Machine:** Machine A — hostname `Dev`
- **Start:** 2026-07-28 22:01:09 EDT

### Bootstrap

| step | result |
|---|---|
| flow_driver check | `logged_in=True project=saved` |
| media-production-v2 skeleton | created (`.gitignore` blocks jpeg/jpg/png/mp4/mp3/wav/m4a/mov) |
| flow_driver `--model` | ADDED — the driver had no model selector; it used whatever the project remembered and only verified the chip said "Nano Banana". V2 needs Nano Banana Pro per shot, so `gen --model "Nano Banana Pro"` now selects it on the chip and ABORTS rather than spending on a lesser model (override: `--model-best-effort`). |
| Jesus V2 face | see below |

#### Jesus V2 face candidates

Three front bust portraits, **identity sentence byte-identical across all three** —
only light and background varied, so the comparison was "which render of the same
described man is best", not "which of three men". Prompts: `candidate-prompts.md`.

| candidate | light / background | outcome |
|---|---|---|
| **candidate-1** | soft even daylight, plain deep earth-brown background | **WINNER → `jesus-v2-face.jpeg`** |
| candidate-2 | warm low late-afternoon sun, limestone wall behind | kept for Cameron |
| candidate-3 | open shade, olive grove behind | kept for Cameron |

**Why candidate-1 won:** a face-lock reference wants neutral even light, a neutral
background and a straight-on symmetric view, so the model copies the FACE and not a
scene. Candidate-2 is the most beautiful of the three but bakes a warm backlight into
the hair edge — with a rim-light law on the books, that is the wrong thing to
propagate into 200 videos. Candidate-3 has the best fabric and the fullest beard and
is the runner-up. **All three are the same man**, so Cameron can swap the pick later
without re-locking anything.

Angle refs generated with the winner attached as `--ref`:
`jesus-v2-three-quarter.jpeg`, `jesus-v2-profile.jpeg`, `jesus-v2-full-body.jpeg`.
The three-quarter came back as a seated street scene rather than the plain-background
ref that was asked for — accepted as supporting reference (the face matches and the
FACE ref is the operative lock); not re-rolled, since rerolling a support asset buys
nothing. Useful signal: **ref-echo did not occur** — the model composed new scenes
rather than copying the portrait.

**JESUS V2 FACE = APPROVED. Cameron approved video #1 on 2026-07-28 ("it beautiful i approve already") and confirmed candidate 1 by number. The face is now the LOCK for all 200 — never regenerate it.**

#### Measured facts (record these — the plan rested on estimates)

| fact | measured value |
|---|---|
| Flow image model | chip reads **🍌 Nano Banana Pro**; the driver had NO model selector before today and was riding whatever the project remembered |
| Flow output resolution | **768×1376** for 9:16 — same as V1's painted refs. Flow's image size, not a model limit; build.py supersamples to 4320×7680 and lands at 1080×1920 |
| credit figure printed by the driver | `0 credits` on every generation this session (recorded verbatim, not interpreted) |
| generation wall-time | ~2–3.5 min per still including download |
| **Flow download sizes (found 23:4x after Cameron's "same quality from Flow")** | viewer Download menu: **1K 768×1376 (what the driver always fetched) · 2K 1536×2752 · 4K 3072×5504**. Measured on a real download each. `flow_driver.py gen --size 2K` is now the default path; `v2_prompt.py --gen` passes it. The API's only remaining edge is speed (~3×, no browser) at $0.134/picture. |

### Videos

| row | slug | start | end | mins | beats | gens | accepted | rerolls | credits-noted | status | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | build-01-cloak | 2026-07-28 22:06 | 2026-07-28 23:00 | 54 | 20 | 43 | 20 | 1× CREAM-CROWD, 1× STRAY-JESUS, 21 discarded on the Flow→API switch | Flow: `0 credits`/gen · API: $2.68 | **DONE · APPROVED by Cameron 2026-07-28** | 109.0 s · 19.8 MB · verify-mp4 OK |
| 2 | build-02-prodigal | 2026-07-28 23:07 | 2026-07-29 00:5x | ~110 | 24 | 43 | 24 | 2× CREAM-CROWD · 4× WRONG-DIRECTION · 3× WARDROBE-DRIFT · 3× CAST-DRIFT · 2× CGI-STYLE · 1× ROTATED · 1× BLACK-BAND | API $2.55 (19 gens, then credits depleted) · Flow: `0 credits`/gen × 24 | **DONE — awaiting Cameron's approval** | 158.4 s · 19.9 MB · verify-mp4 OK · 24 stills |

| 3 | build-03-zacchaeus | 2026-07-29 01:2x | — | — | 26 | — | — | — | Flow only | IN-PROGRESS (step E) | Machine A `Dev`. Steps A-D done: beats extracted, audio copied, beats_v2.py written, v4 checklist PASS. **FLOW ONLY** per Cameron 2026-07-29. |

#### Row 1 — build-01-cloak (Mark 5:25-34)

- **Steps A–D complete.** Beat truth extracted from the read-only V1 build; the V2
  timeline arithmetic reproduces the shipped V1 mp4 to within 0.03 s (109.0 vs 108.97).
  Audio COPIED, never moved. v4 checklist: PASS on all 20.
- **Coverage: 20 pictures, against V1's 11.** V1's two clear STORY-COVERAGE misses are
  fixed: `w28` — her only spoken line in all of Mark 5 — now has its own frame, and the
  hem-touch is separated from the pressing-through.
- **Defect: CREAM-CROWD (s05).** The crowd came back dressed in pale cream, so the one
  man who may wear cream did not read as different from anybody. Root cause was in the
  SETTING lock, not the beat: it said "earth-toned wool" and leaned on the sentence "no
  one but Jesus in cream" to do the work. Fixed at the lock (now **SETTING LOCK v2** —
  colours stated as SATURATED/DEEP/DARK and explicitly darker than his robe), so it
  cannot recur on the other 10 crowd shots.
- **Why the run was stopped to fix it:** 11 crowd shots were still queued behind s05 and
  would have inherited the same failure — ~35 min of generation to throw away. Cheaper
  to stop, fix the lock, resume.
- **s03/s04 regenerated too.** Both were visually fine under SETTING LOCK v1, but the
  law requires one byte-identical lock across a video's prompts, so they were re-shot
  under v2 rather than left as the odd ones out. Originals kept in
  `assets/_v1lock-fallback/` — if a re-shot one comes back worse, the better picture
  wins and the discrepancy gets recorded here honestly.
- **Second defect: STRAY-JESUS (s03 under lock v2).** The v2 lock fixed the crowd
  colours — and then put Jesus in a frame he does not belong in. The lock said "darker
  than Jesus's pale cream robe … Jesus alone wears cream", and the model did the
  reasonable thing with a named character: it painted him in, standing in the
  background in cream, **seven seconds before the narration introduces him**. The
  reveal at 15.11 s ("That day, Jesus was already on his way…") would have landed on a
  man the viewer had already been looking at.
- **Rule learned, written into the lock as a comment:** *a setting lock describes the
  street and the villagers and must never name a character, because naming one puts him
  in the frame.* **SETTING LOCK v3** states the villagers' colours and the no-pale-cloth
  rule with no character named; the cream contrast is carried by JESUS LOCK v4's own
  "(only he wears cream)", which is present in exactly the shots he belongs in. The two
  non-Jesus setting beats (b03, b09) also gained the positive line "Everyone in this
  frame is an ordinary villager."
- Cost of catching it here rather than at assembly: one still. Cost if the crowd fix
  had been trusted without re-QC: a stray Jesus in every non-Jesus street shot of 200
  videos.

**MID-ROW CHANGE — Flow → Gemini API at 2K (Cameron, 2026-07-28).** He lifted the
money law mid-build, so all 20 stills were re-shot through `v2_gen_api.py` on
`gemini-3-pro-image` at 2K. This is not a preference; Flow's 768×1376 sits BELOW the
1080×1920 delivery size, so every Ken Burns move was upscaling — the exact thing the
anti-shimmer law is written against. 1536×2752 gives real headroom to supersample.
Side benefits: no ~20 gens/hour ceiling, and nothing touches Cameron's screen.
Cost: $0.134/image → **$2.68 for row 1**; ~$536 for 200 videos at 20 stills each,
before rerolls. The 19 Flow stills were discarded rather than mixed — one video with
some frames at 4× the pixels of others would show.

QC record (V2 rubric — accept only ≥4 average with nothing below 3):

| still | verdict | note |
|---|---|---|
| s01-twelve-years | ACCEPT | alone in a bare room, cup and blanket, twelve years on her face; anatomy clean |
| s02-physicians | ACCEPT | the last coins visibly leaving her purse into his palm — action reads at a glance; woman consistent with s01 |
| s03-untouchable | re-shot under SETTING LOCK v2 | v1-lock version was good: a corridor of villagers stepping back, clear empty dust around her |
| s04-jairus-urging | re-shot under SETTING LOCK v2 | v1-lock version was good: **first Jesus shot — face matched the ref, composed the wide scene instead of echoing the portrait, only he in cream** |
| s05-crowd-pressing | **HARD FAIL → CREAM-CROWD** | composition and face were right; the crowd's cream wardrobe killed it |

**Final QC on the delivered 2K set** (all 20 re-shot on `gemini-3-pro-image`):

| still | verdict | note |
|---|---|---|
| s01-twelve-years | ACCEPT | alone in a bare room, cup and blanket; 2K brings real skin and fabric texture |
| s05-crowd-pressing | ACCEPT | **CREAM-CROWD fixed** — crowd in deep browns/russets/indigo, Jesus reads instantly as the only cream |
| s11-touches-hem | ACCEPT | the hinge: she is kneeling **BEHIND** him per Mark 5:27, fingertips open on the cloth, no gripping or bunching, he has not turned |
| s15-disciples-protest | ACCEPT | cast locks visibly holding — Peter blue-grey with arms thrown wide, young John in sand, Andrew in rust; exactly four men in front |
| s18-daughter | ACCEPT | he is **crouched to her level**, not standing over her; crowd drawn back in a ring |
| s20-goes-in-peace | ACCEPT | she walks away upright, villagers no longer step back, he watches her go |
| the other 14 | ACCEPT | woman's face held across all her shots on text lock alone; no cream on any villager; no halo/glow anywhere |

**Prompt bug found by QC, fixed in the file:** b20's scene text said "head uncovered"
while the WOMAN LOCK gives her a dust-rose head cloth in every shot. The model obeyed
the lock and ignored the scene text — the right call — but a prompt must never argue
with its own lock, so the scene text was corrected.

**Delivery gates (step G):**

| gate | result |
|---|---|
| `admin/verify-mp4.sh` | **OK** — video 108.971 s, audio 108.971 s, no truncation, moov present |
| runtime vs V1 | 109.0 s planned, 108.971 s delivered — matches the shipped V1 cut |
| dead air | worst spoken gap **1.58 s** before `n3b` (limit 2.5 s) |
| silence scan | no gap > 2.5 s anywhere in the spoken body |
| format | 1080×1920 · h264 · 30 fps · 19.8 MB (cap 24.3) · crf 20 |
| music bed | none — narration and intentional silence only |
| caption frame-strip | white narrator · **pink for her own line (w28)** · red for Jesus (j1) · cream invitation card — each on the correct scene, all inside the bottom band |

**Ministry gate:** PASS on all four (`MINISTRY-GATE.md`).

---

## Session 2 — 2026-07-28 (cont.)

- **Model:** Opus 5 (Claude Code) · **Machine:** Machine A — hostname `Dev`
- **Start:** 2026-07-28 23:31 EDT · resumed row 2 at step E per the ledger.

### BLOCKER HIT IMMEDIATELY — the Gemini API is out of money

`v2_gen_api.py` died on b20 with `RESOURCE_EXHAUSTED`: *"Your prepayment credits are
depleted."* That is Cameron's Google AI Studio billing; topping it up is his to do, not
something a session can or should do. **The line did not stall** — `V2-NEXT-SESSION-PROMPT`
already names Flow at 2K as the default path, so row 2 finished on
`flow_driver.py --size 2K`. Flow's 2K is an UPSCALE of 768×1376; the API's was native
2K. Same pixel dimensions, less real detail. Worth Cameron knowing when he decides
whether to refill the API.

### Row 2 QC — 19 API stills judged, 13 REJECTED

Every still was Read at full resolution. This is the honest tally, and it is worse than
row 1's: **6 accepted, 13 rejected.** Five defect families, four of them traced to a
root cause in the prompt system rather than to bad luck on one frame:

| defect | frames | root cause | fix |
|---|---|---|---|
| `CREAM-CROWD` (recurrence) | s01, s02 | PHARISEES LOCK leaned on the NEGATION "never white, never cream, never pale" — the model dressed all three in white striped prayer shawls, the largest pale mass in frame, beside the one man allowed cream | **PHARISEES LOCK v2** states the colours POSITIVELY and anchors them ("plainly DARKER than the sunlit stone wall behind them"). Row 1 paid for this exact lesson at the SETTING lock; it had not been generalised. |
| `WRONG-DIRECTION` | s04, s10, s11, s12 | the beats said *what* happened but never where the CAMERA stood, so the model defaulted to hero-shots facing the lens. **The father ran AWAY from his son in the icon shot of the whole parable**, and s04 read as the son ARRIVING while the narration says "Then he left" | every one of the four now opens with an explicit camera position and a stated travel direction ("SHOT FROM THE SIDE OF THE ROAD… far ahead of him IN THE DIRECTION HE IS RUNNING") |
| `WARDROBE-DRIFT` | s07, s09, s13 | the YOUNGER lock deliberately omits clothing (his wardrobe changes through the story) — so any beat whose scene text forgot to state it let the model invent one. Exactly the beats that forgot it drifted: rust-red → brown | clothing stated in every younger-son beat, plus **BAREFOOT until b14** so the gift of shoes in v22 still means something |
| `CAST-DRIFT` | s17, s18, s19 | text locks alone did NOT hold a face. The elder son came back as **three visibly different men** across s16/s17/s18 | **char_refs added to `v2_prompt.py`** — recurring characters are now locked by IMAGE (CAST-BIBLE principle), refs staged in `CAST-REF-V2/` from accepted stills. `flow_driver` already accepted repeated `--ref`; nothing was passing them. |
| `CGI-STYLE` | s12, s19 | STYLE-V2 forbids "plastic CGI" and it drifted anyway on two frames | rerolled; the attached photographic char_refs also anchor realism |
| `ROTATED` | s15 | the entire feast rendered sideways in the portrait canvas | b15 now states "A TALL VERTICAL FRAME… every figure upright with their feet on the floor". Reroll came back correct. |

**One systemic bug fixed in the assembler, not the beat:** the anti-panel clause was
only appended to `wide` beats, so tight shots had no panel protection at all — and
s18, a tight shot, came back with a landscape pasted in above the wall like a second
panel. `ANTI_PANEL` now goes on **every** prompt. A panel artifact was never a
wide-shot problem.

**ACCEPTED from the API pass (6, kept as-is):** s03 · s05 · s06 · s08 · s14 · s16.
All 13 rejects are preserved in `assets/_rejected/` — if a reroll comes back worse,
the better picture wins and the discrepancy gets recorded here honestly (row-1 rule).

### Flow reroll pass — 13 re-shot, then a second pass on 5

The lock/camera/ref fixes landed on the first try for 8 of the 13. Five needed one
more attempt, and the second attempt fixed all five:

| beat | first reroll | second reroll |
|---|---|---|
| b04 `he left` | composition fixed (father from behind at the gate) but the son still faced the camera, so "Then he left" STILL read as arriving | "SEEN FROM DIRECTLY BEHIND… HIS FACE ENTIRELY HIDDEN" → he now walks away up the road. **ACCEPT** |
| b11 `the father ran` | came back as a CGI illustration AND still running away from his son | recomposed from BEHIND the father, running away from camera toward the distant son. **ACCEPT — and it is now the best picture in the video** |
| b13 `the embrace` | wardrobe + bare feet fixed, but both men stood side by side facing the lens: a posed portrait, not "he fell on his neck" | "NEITHER MAN LOOKING AT THE CAMERA — this is a collision, not a portrait… COLLAPSED FORWARD INTO HIS SON" → **ACCEPT** |
| b19 `father came out` | CGI drift again | added the same photographic anchor sentence that had already fixed b12. **ACCEPT** |
| b20 `the hurt poured out` | **BLACK-BAND** — bottom third of the frame rendered solid black, unusable | full frame. **ACCEPT** (father's gaze drifts camera-ward rather than to his son; accepted as best-available under the three-reroll rule, noted honestly) |

**FINAL: 24/24 accepted.** Two lessons worth carrying to row 3:
1. **Stating the action is not enough; state the CAMERA.** Four separate frames put a
   travelling figure the wrong way round because the beat said what happened but not
   where the lens was. "Shot from behind X, facing away from us" is the fix, and it
   has to be in the beat, not in a QC note.
2. **A negation is a suggestion; a stated positive is an instruction.** This is now
   the same lesson three times (row 1 SETTING lock, row 2 PHARISEES lock, row 2
   CGI drift). "Never cream" fails; "the same saturated dark wool, darker than the
   wall behind them" works. "Not plastic CGI" fails; "real weathered skin, real
   coarse wool, photographed on location with a real camera" works.

**Delivery gates (step G):**

| gate | result |
|---|---|
| `admin/verify-mp4.sh` | **OK** — video 158.406 s, audio 158.406 s, no truncation |
| dead air | silencedetect at −45 dB / 2.5 s found **nothing** in the spoken body |
| format | 1080×1920 · h264 · 30 fps · 19.9 MB · crf 20 |
| music bed | none — narration and intentional silence only |
| markers | all 7 word-anchored switches resolve against the timing sidecars (verified BEFORE render) |
| caption frame-strip | white narrator · **red for every KJV line in Jesus's voice** (he is the one telling the parable) · cream question card — each on the correct scene, all inside the bottom band |
| V1 read-only | verified untouched — no file in `media-production/build-02-prodigal` modified this session |

**Ministry gate:** PASS on all four (`MINISTRY-GATE.md`).

**Open item for Cameron:** the Gemini API prepay balance is empty. Row 2 finished on
Flow, whose 2K is an upscale of 768×1376 rather than native 2K. **18 of the 24
delivered frames are Flow 2K; 6 are API-native 2K** (s03, s05, s06, s08, s14, s16 —
the ones QC accepted before the credits ran out). All 24 are 1536×2752 on disk, so
the mix is invisible in dimensions but the API six carry more real detail. If he
refills the API the whole row can be re-shot for pixel parity;
if not, Flow at 2K is the standing path and rows 3+ will be uniform.
