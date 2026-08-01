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

---

## Session 4 — 2026-07-29 (pictures-only order, authoring pass)

- **Model:** Opus 5 (Claude Code)
- **Machine:** Machine A — hostname `Dev`
- **Job:** the PICTURES-ONLY order. Steps G (assemble), H (ministry gate) and every
  mp4 gate are suspended. This session's work is step C (author `beats_v2.py`) plus
  step F QC on what the unattended runner produces.

### Runner

`v2_run_all.py` was already alive from session 3 (PID 3817195) and was left alone all
session. It finished row 4 (30/30), rolled onto row 5, and picked up each new beat map
as it was committed **without a restart** — the re-scan design works as intended.
Observed throughput ≈ 1 picture per 1.3 min, better than the 3 min/picture estimate.

### Rows authored this session

| row | build | scripture | pictures | runtime | s/picture | checker |
|---|---|---|---|---|---|---|
| 5 | build-05-bent-woman | Luke 13:10-17 | 37 | 223.0 s | 6.0 | PASS |
| 6 | build-06-two-sons | Matt 21:28-32 | 16 | 73.1 s | 4.6 | PASS |
| 7 | build-07-peter-water | Matt 14:22-33 | 37 | 202.1 s | 5.5 | PASS |
| 8 | build-08-lost-coin | Luke 15:8-10 | 12 | 58.2 s | 4.9 | PASS |
| 9 | build-09-rich-ruler | Mark 10:17-22 | 31 | 177.4 s | 5.7 | PASS |
| 10 | build-10-well | John 4:1-42 | 49 | 282.4 s | 5.9 | PASS |
| 11 | build-11-storm | Mark 4:35-41 | 34 | 199.8 s | 5.9 | PASS |

**216 pictures queued**, all seven `--check --dump` clean. Density held at 4.6–6.0 s
per picture across every row, which is the band rows 1–4 shipped at. The two rows
below the band (6 and 8) are the two shortest stories, where the coverage law's floor
of 10 pictures binds before the scaling does.

### Tooling added

- **`media-production-v2/v2_outline.py`** — prints a prepped row's narration as one
  line per timing phrase with absolute audio windows. `beats.json` is ~40 KB of JSON
  per row and cannot be read at authoring speed; this is the form a beat map is
  actually written from. `v2_outline.py <row-number-or-dir>`.

### Defects found and fixed

1. **Flow driver dropped pictures silently** (`flow_driver.py select_model`). Row 5
   lost b01 and b08 to:
   `model chip reads: '?'` … `WARNING: could not select model 'Nano Banana Pro'
   (chip says: Nano Banana Pro)` — the warning naming the model it claimed it could
   not select. It read the chip ONCE, raced the page, got nothing, and dropped into
   the selection loop for a model that was already selected; the popup has no
   clickable row for the current model, so all four attempts failed and the
   generation was abandoned. **Fixed:** poll for the chip (6 × 500 ms), and re-check
   the chip before giving up — if it names the wanted model the model was right all
   along and only the READ was late. Cannot green-light a wrong model, since the
   True path still requires the chip's own text to match. `v2_run_all.py` re-scans
   for missing files each lap so nothing was permanently lost, but each miss burned
   a whole lap.

2. **The ground-level-camera rotation trap.** Row 5 s02 came back ROTATED 90° — the
   street running up the left edge, every figure on its side, unusable in a 9:16
   cut. Cause was my own prompt: *"the camera is set LOW, close to the paving
   stones, at the exact height her eyes have been."* Fixed the four beats across
   three rows carrying that phrasing (r5 b02, r7 b07, r7 b20, r8 b04) before they
   reached the generator, deleted the rotated jpeg for regeneration, and wrote the
   trap into `V2-NEXT-SESSION-PROMPT` step C. **Replacement pattern:** state the low
   VIEWPOINT, then pin the frame — *"an upright vertical photograph … the ground is
   at the bottom of the frame and the sky at the top, and the horizon is level — the
   picture is the right way up."*

### Step F QC — row 5 sample

Read at full resolution: s02 (FAIL, rotated — fixed above), s11, s17.

- **s11 `he-came-down-to-her`** — PASS, and the strongest evidence yet that the V2
  pipeline is right. Locked Jesus face with green eyes, cream robe with no cream
  anywhere else in the room, no halo or rim-light, her bent double with their gazes
  meeting, congregation in saturated deep earth colours, correct anatomy.
- **s17 `she-stood-up-straight`** — PASS. The POSTURE ARC holds: she is fully
  upright, shoulders back, chin level, face to face with him after twelve frames
  bent double. Two soft notes, neither a fail: the congregation reads seated and
  calm where the beat asked for half-risen and stunned, and the architecture leans
  slightly Byzantine (pointed arches, carved capitals) rather than plain
  first-century Galilean. Worth watching across the library; not worth a reroll.

### Notes carried forward

- **Row 6 (two sons):** Cameron's QUEUE note — "could explain in modern terms what a
  publican and a harlot are" — is a NARRATION change. Audio is preserved untouched
  under the pictures-only order, so it is logged here for the re-voice track.
- **Row 6 structural note:** the V1 audio has NO voice segments for either son, so
  the pictures carry both answers with no words to help them.
- **Row 10** introduces a WOMAN speaker (w9/w11/w15/w19/w25/w29) — first row in the
  queue with three distinct voices.

### Not done

- No mp4 assembled (steps G/H suspended by the pictures-only order).
- Push still blocked by this box's 12.7 GB backlog; all work committed locally.

---

## Session 5 — 2026-07-29 (rows 50+ picture pass)

- **Model:** Fable 5 (Claude Code)
- **Machine:** Machine A — hostname `Dev`
- **Job:** V2-SESSION-FROM-50 — pictures only, rows 50 upward. **Machine A claims
  rows 50-70.** Runner `v2_run_all.py --first 50` started (log `/tmp/v2-run-50.log`).
- Repo found mid-stale-rebase (807 pending, conflicts on build-08 mp3s) with
  origin/main already an ancestor of local main — aborted the rebase, main restored
  to 5cc5e963b, nothing lost.

| row | build | status |
|---|---|---|
| 50 | build-50-noblemans-son | beats_v2.py authored, 27 beats, checker PASS · generating |
| 51 | build-51-first-catch-of-fish | 26 beats, PASS · queued |
| 52 | build-52-demoniac-synagogue | 24 beats, PASS, Flag-A applied · queued |
| 53 | build-53-peters-mother-in-law | 15 beats, PASS · queued |
| 54 | build-54-the-leper | 24 beats, PASS · queued |
| 55 | build-55-withered-hand | 23 beats, PASS · queued |
| 56 | build-56-widow-of-nain | 22 beats, PASS, Flag-G applied · queued |
| 57 | build-57-jairus-daughter | 27 beats, PASS, Flag-G applied · queued |
| 58 | build-58-feeding-5000 | 24 beats, PASS · queued |
| 59 | build-59-feeding-4000 | 27 beats, PASS · queued |
| 60 | build-60-gerasene-demoniac | 39 beats, PASS, Flags A+R applied · queued |

Session 5 notes: another session's rebase-in-progress means NO commits from this
session until it lands; beats files live safely on disk. Flow runner (other
session's, v2-run-main.log) generating steadily ~1.4 min/picture. Flag-table
numbers are THE-200 numbering, not build numbers — flags matched BY STORY.
278 pictures queued rows 50-60.
| 61 | build-61-syrophoenician-woman | 31 beats, PASS, Flag-A (by story-kind) applied · queued |
| 62 | build-62-ephphatha | 34 beats, PASS · queued |

Session 5 close: rows 50-62 authored and checker-PASS = **343 pictures queued**.
Rows 63-70 prepped (beats.json + audio) for the next session. Commits still
blocked by the other session's in-progress rebase — ALL beats_v2.py files for
rows 50-62 exist ON DISK ONLY; whoever works next: commit them once the rebase
lands. Step F QC for rows 50+ not yet started (no row-50+ stills generated yet;
runner still clearing earlier rows).

---

## Session 6 — 2026-07-30 — CAMERON REJECTED THE V2 LOOK (Machine A / Dev)

**Cameron's words: the pictures look horrible; the redo attempt wasted his day.
This entry is the standing correction until a new pilot is approved.**

- **REJECTED: all V2 stills generated through 2026-07-29 (~443 across 15 builds).**
  Verified by eye on cloak s06, prodigal s06, zacchaeus s07 — same disease in each:
  flat noon light on every frame, figures posed and static like extras waiting for
  direction, Jesus looking into the camera, wide crowd-wallpaper of dozens of samey
  AI faces (mushy at distance), and the ONE emotion each beat exists for (desperate /
  rock-bottom / too-small-to-see) not landing on any face.
- **Root cause is the shared recipe, not Flow variance:** STYLE-V2 says "cinematic /
  depth of field" (words the model ignores) while the enforced FORCED-WIDE line
  ("never a portrait, never a close-up") pushes every multi-figure beat into a wide
  posed crowd; no per-beat light direction/time-of-day, no lens/DOF language, no
  mid-action requirement, no "nobody looks at the camera" rule. Every prompt shares
  the block, so every picture shares the failure.
- **LAW until further notice: NO mass generation. No Flow credits on V2 stills until
  Cameron approves a re-piloted strip from a rebuilt recipe.** Runner stays down.
- Open fork for Cameron: fix the photoreal-film direction (real cinematography:
  directional light, lenses, close-ups allowed, emotion-first) vs return toward the
  painted look. His call; it rewrites STYLE-V2 either way.

### Session 6 continued — CAMERON REVERSED FLOW-ONLY: THE API IS THE ENGINE (2026-07-30)

**Cameron, same session, his words:** *"the first ones you did were good becasue we
used and api key from gemini. i want to use that fro all 200 just so i get this done
and over with faster."* This supersedes the 2026-07-29 FLOW-ONLY order AND this
session's earlier "no generation until re-piloted recipe" line. The standing law now:

1. **`v2_gen_api.py` is UN-RETIRED** — gemini-3-pro-image, native 2K, the engine for
   all 200. Rebuilt with: hard `--ceiling` (refuses any image that would pass the
   cap), cross-session spend meter `api-spend.jsonl`, `--all` row-order mode, and
   automatic CAST-V2 reference attachment (front+quarter) whenever a beat's locks
   name a library character. Paid runs REQUIRE --ceiling; --dry-run prices free.
2. **Flow's only remaining job: character reference sheets.** `CAST-V2-REF/
   gen_cast_v2.sh` generates the library — 15 recurring characters x 2 angles
   (the Twelve + Mary mother + Mary Magdalene + John the Baptist), identities and
   wardrobe colours carried over from V1 CAST-BIBLE, photoreal, 2K, Nano Banana Pro.
   Sheets land in ~/Desktop/CAST-V2-APPROVAL for Cameron's approval; ONLY approved
   sheets get used as API locks.
3. **Curation-by-deletion replaces the blanket rejection of the 443.** All 443
   existing V2 stills are copied to ~/Desktop/V2-PICTURE-REVIEW named
   `<row-slug>__<shot>.jpeg`. Cameron deletes the bad ones; `v2_review_diff.py
   --apply` moves those originals to `_replaced/` and the API runner re-shoots
   exactly that set. Nothing is destroyed.
4. **Money, measured tonight:** 119 beat maps authored → 3,267 pictures spec'd →
   2,801 still to generate = **$375.33** at $0.134/image. Remaining ~81 rows to
   author at the same density ≈ $300 more. Replacements + rerolls ≈ $100-190.
   **Realistic all-in ≈ $800.** Credits are DEPLETED since row 2 — Cameron must top
   up Google AI Studio billing before any paid run; the first paid batch re-verifies
   $0.134 against the real bill.

---

## Session 7 — 2026-08-01 — CLAIM: story 02 (prodigal) realistic rebuild (Machine A / `Dev`)

- **Model:** Fable 5 (Claude Code) · **Machine:** Machine A — hostname `Dev`
- **CLAIM (2026-08-01): story 02 build-02-prodigal for the REALISTIC rebuild** —
  the lowest-numbered story with no realistic-standard cut on the reviewer
  (01 is APPROVED by Cameron 2026-07-28 and is not redone; 07 and 11 are shipped
  realistic cuts awaiting Cameron; 12 and 13 are claimed by Codex). Row 2's 24
  existing V2 stills fall under the Session 6 blanket rejection of the old look;
  they are kept in `assets/` untouched as rough-draft composition refs
  (ROUGH-DRAFT CONTINUITY LAW) and the realistic set generates to
  `assets-realistic/` via `v2_gen_api.py` (gemini-3-pro-image, native 2K, hard
  ceiling). Audio stays LOCKED to the V1 final; no re-voicing.
- Session results are appended below when the row closes.

### Row 2 close — realistic rebuild DONE, cut shipped (2026-08-01)

| row | slug | start | end | beats | gens | accepted | rerolls | spend | status | notes |
|---|---|---|---|---|---|---|---|---|---|---|
| 2 | build-02-prodigal | 2026-08-01 ~02:35 | 2026-08-01 ~03:20 | 24 | 28 | 24 | 1× RING-ON-WRONG-HAND (b14) · 2× HEADCOUNT-EDGE-FIGURE (b20) · 1× CAST-DRIFT (b24) | $3.75 (meter $10.72) | **DONE — realistic cut shipped, awaiting Cameron** | 157.9 s · 20.6 MB · AUDIO LOCK PASS · verify-mp4 OK |

- **Windows re-timed** from the fixed `extract_beats.py` (per-build formulas) and
  cross-checked against the real V1 audio with silencedetect — segment
  boundaries matched within 0.1 s, so row 2 never had storm-11's 8 s drift.
- **Tooling:** `v2_gen_api.py` now honours a build's `OUTPUT_ASSET_DIR` (it
  hardcoded `assets/`, which would have skipped every beat whose rejected-look
  rough existed) and attaches a beat's `rough_ref` as a ROUGH COMPOSITION DRAFT
  with its own preamble (faces always come from the face/character locks).
- **Lesson worth carrying (b20):** a rough draft carries its DEFECTS as
  faithfully as its virtues — the take-1/take-2 edge intruder was being copied
  from the rough itself; the fix was removing that beat's rough (`_NO_ROUGH`),
  not stronger prose. Check the rough for the defect before blaming the model.
- QC record: `build-02-prodigal/QC.md`. Rejected takes in
  `assets-realistic/_rejected/`. Ministry gate re-affirmed with a realistic
  addendum. Board card v2 → new hash `6dc2f2f5…` (returns to Unwatched);
  sync-reviews run; board redeployed to Firebase.

---

## Session 8 — 2026-08-01 — CLAIM: story 05 (bent-over woman) realistic rebuild (Machine A / `Dev`)

- **Model:** Fable 5 (Claude Code) · **Machine:** Machine A — hostname `Dev`
- **CLAIM (2026-08-01): story 05 build-05-bent-woman for the REALISTIC rebuild** —
  next open V2 wave row (02/03/07/11/13 shipped, 04 claimed by Codex). Row 5's 37
  existing V2 stills (Jul 29) fall under the Session 6 blanket rejection of the old
  look — 3 of them additionally 1K undersized per the resolution audit. They stay in
  `assets/` untouched as rough-draft composition refs; the realistic set generates to
  `assets-realistic/` via `v2_gen_api.py` (gemini-3-pro-image, native 2K, hard
  ceiling), build-02 pattern. Audio stays LOCKED to the authoritative narration;
  no re-voicing. Ships to Reviewer only; app feed untouched.
- Session results are appended below when the row closes.

### Row 5 close — realistic rebuild DONE, cut shipped (2026-08-01)

| row | slug | start | end | beats | gens | accepted | rerolls | spend | status | notes |
|---|---|---|---|---|---|---|---|---|---|---|
| 5 | build-05-bent-woman | 2026-08-01 ~11:20 | 2026-08-01 ~12:45 | 37 | 56 | 39 (37 beats + 2 anchors) | 2× FERRULE (s02/s05) · 2× JESUS-BLACK-HAIR (s08/s12) · 1× CAMERA-GAZE (s08) · 1× ROUGH-ECHO + 1× DUPLICATE (s09) · 2× RULER-DRIFT (s25/s27) · 1× FARMER-DRIFT (s26) · 4× STICK-CONTINUITY (s30/s31/s32/s36) · 1× GROUP-PHOTO (s35) · 2× WARDROBE-GREEN (s02) | $7.50 this build (formula ~$6.27; overage = the 17 defect-fix passes) | **DONE — realistic cut shipped, awaiting Cameron** | 247.8 s · 20.8 MB · AUDIO LOCK PASS 83916bed… · verify-mp4 OK |

- **ALL 37 windows re-timed** — the old beats_v2 windows carried the storm-11
  formula defect (total 236.7 s vs the real 247.7 s, ~13 s drift by the end).
  Recomputed as absolute phrase times from the fixed `extract_beats.py` and
  verified against the real audio with silencedetect (every boundary within 0.1 s).
- **Shared-meter lesson:** the api-spend meter is cross-session; a concurrent
  story-06 worker was spending in parallel, so a fixed `--ceiling` on the GLOBAL
  meter got eaten from outside and stopped the main run at 34/37. Slice runs with
  `--only` (item count caps your own spend) and treat the ceiling as the runaway
  brake, recomputing it per run from the live meter.
- **Stick continuity designed, not patched:** she keeps the 18-year stick until it
  falls exactly on "loosed from this bond" (s27); every frame that regenerated it
  back into her hands afterwards was identity-edited clean.
- QC record: `build-05-bent-woman/QC.md` · hash-locked boards `IDENTITY-QC.json`
  (52 appearances) · rejected takes in `assets-realistic/_rejected/` (from the
  edit passes on; the first four `--redo` rerolls overwrote in place — recorded
  honestly).
- Board card v5 → new hash `93738754…` (returns to Unwatched); sync-reviews run;
  board redeployed to Firebase. App-feed V1 untouched.

---

## Session 8 — 2026-08-01 — CLAIM: story 06 (two sons) realistic rebuild (Claude worker 4)

- **CLAIM (2026-08-01): story 06 build-06-two-sons for the REALISTIC rebuild** —
  row 6's 16 existing V2 stills fall under the Session 6 blanket rejection of the
  old look; they are kept in `assets/` untouched as rough-draft composition refs
  (ROUGH-DRAFT CONTINUITY LAW) and the realistic set generates to
  `assets-realistic/` via `v2_gen_api.py` (gemini-3-pro-image, native 2K, hard
  ceiling). Audio stays LOCKED to the V1 final; no re-voicing. Build-02
  (Session 7) is the template.
- Session results are appended below when the row closes.

### Row 6 close — realistic rebuild DONE, complaint fixed, cut shipped (2026-08-01)

| row | slug | beats | gens | accepted | rerolls | spend | status | notes |
|---|---|---|---|---|---|---|---|---|
| 6 | build-06-two-sons | 23 | 32 (4 anchors + 23 beats + 5 rerolls) | 23 | b01 PRIEST-COUNT · b10 EDGE-INTRUDER (defective rough dropped) · b14 CAMERA-GAZE · b16 TRIPTYCH (rough was ITSELF a triptych, dropped) · b22 STRAY-DISTANT-JESUS | ≈$4.29 | **DONE — realistic V2 shipped, awaiting Cameron** | 125.8 s · 19.9 MB · AUDIO LOCK PASS · verify-mp4 OK |

- **The real fix was upstream of the pictures.** Cameron's OPEN row-6 complaint
  (father's ask cut out) was an ASSEMBLY bug, not a script bug: the 2026-07-24
  REDO voiced the complete script (j28/j29/j29b/j30/s31/n1b/n2b/n5b) but V1
  build.py BEATS was never updated, so the 82.7 s cut silently dropped every
  new segment while the takes sat unused in audio/. BEATS now carries all 18
  segments with speaker-aware KJV gaps matching extract_beats; V1 final rebuilt
  at 125.8 s, whisper ear-check all-pass. Zero re-voicing.
- **Lesson worth carrying:** when a complaint says words are MISSING, diff the
  build's BEATS list against make_narration.SEGMENTS before assuming the script
  needs re-voicing — the audio may already exist. And the rough-defect lesson
  recurred TWICE (b10, b16): check the rough for the defect before blaming the
  model; a rough that is itself a triptych begets triptychs.
- QC record: `build-06-two-sons/QC.md`. Board card v6 → new hash `c660e5de…`
  (returns to Unwatched, complaint retained); sync-reviews run; board deployed.

---

## Session 9 — 2026-08-01 — CLAIM: story 08 (lost coin) realistic rebuild (Claude worker 5, Machine A / `Dev`)

- **Model:** Fable 5 (Claude Code) · **Machine:** Machine A — hostname `Dev`
- **CLAIM (2026-08-01): story 08 build-08-lost-coin for the REALISTIC rebuild** —
  next open V2 wave row (a parallel worker takes 09). Row 8's existing 11 untracked
  stills (+1 FAILED) are all 1536x2752 but predate the realistic wave close-out;
  each is QC'd against the realistic rubric at full size and reused ONLY if it
  genuinely passes — the rest regenerate to `assets/` via `v2_gen_api.py`
  (gemini-3-pro-image, native 2K, hard per-run ceiling recomputed from the live
  shared meter, `--only` slices). Prior reviewer lesson on this row ("cut the
  original video short") is RESOLVED — the full 58.2 s audio stays LOCKED via the
  v2_assemble encoded-audio hash lock; no re-voicing. Windows re-verified from the
  fixed `extract_beats.py` against the real audio with silencedetect. Ships to
  Reviewer only; app feed untouched.
- Session results are appended below when the row closes.

---

### Row 8 close — realistic rebuild DONE, cut shipped (2026-08-01)

| row | slug | beats | gens | accepted | rerolls | spend | status | notes |
|---|---|---|---|---|---|---|---|---|
| 8 | build-08-lost-coin | 12 | 23 (1 anchor + 12 beats + 10 rerolls) | 13 | s01 ROUGH-ECHO pre-V5 Jesus (rough dropped) · s02 COIN-COUNT ×2 (fixed by restating as nine-in-a-row + tenth in her fingers) · s03 COIN-COUNT (fixed as five-gap-four) · s06 EDGE-INTRUDER · s07 ROTATION ×2 + an unclothed blurred figure outside the door (rough dropped, ROTATION-TRAP) · s11 CAMERA-GAZE Jesus, then GROUP-PHOTO crowd | $2.95 | **DONE — realistic V2 shipped, awaiting Cameron** | 68.8 s · 19.9 MB · AUDIO LOCK PASS e219f876… · verify-mp4 OK |

- **ALL 12 windows re-timed** from the fixed `extract_beats.py` — the stale
  beats.json/windows drifted up to 4.2 s by n5 (55.70 vs real 59.94); every
  segment onset now matches silencedetect within 0.1 s. The jv8 b02/b03 split
  (10.60) sits in the measured mid-sentence pause after "silver,".
- **Counting lesson worth carrying:** the model cannot count a pile — "TEN
  countable coins" failed twice at 12 coins. What worked was restating the
  count as a COMPOSITION: "nine in a straight row, none overlapping, and she
  holds the tenth between finger and thumb" (and for the loss frame "five left
  of the gap, four right"). State object counts as geometry, not totals.
- Prior reviewer lesson ("cut the original video short", RESOLVED) not
  regressed: v2_assemble stream-copied the approved audio, hash lock PASS.
- QC record: `build-08-lost-coin/QC.md` · hash-locked boards `IDENTITY-QC.json`
  (11 appearances: woman 9, Jesus 2) · rejected takes in
  `assets-realistic/_rejected/` (7 preserved).
- Board card v8 → new blob hash `5bcb2b44…` (returns to Unwatched);
  sync-reviews run; board redeployed to Firebase. App-feed V1 untouched.

---


## Session 9 — 2026-08-01 — CLAIM: story 09 (rich young ruler) realistic rebuild (Claude worker 6, Machine A / `Dev`)

- **Model:** Fable 5 (Claude Code) · **Machine:** Machine A — hostname `Dev`
- **CLAIM (2026-08-01): story 09 build-09-rich-ruler for the REALISTIC rebuild** —
  assigned row (a parallel worker holds 08). Row 9's 21 existing V2 stills
  (Jul 29, partial — 31 beats authored, only 21 generated) fall under the
  Session 6 blanket rejection of the old look. They stay in `assets/` untouched
  as rough-draft composition refs (ROUGH-DRAFT CONTINUITY LAW); the realistic
  set generates to `assets-realistic/` via `v2_gen_api.py` (gemini-3-pro-image,
  native 2K, hard per-run ceiling recomputed from the live shared meter,
  `--only` slices). Audio stays LOCKED to the authoritative V1 narration
  (196.8 s) via the v2_assemble encoded-audio hash lock; no re-voicing. All 31
  windows re-timed from the fixed `extract_beats.py` (the Jul 29 windows carry
  the raw-vs-trimmed drift — old card at ~177 s vs real 189.0 s) and verified
  with silencedetect. The two weight-bearing frames (b12 "loved him", b29
  watching him go) QC to the beat map's love-not-pity standard before anything
  else ships. Ships to Reviewer only; app feed untouched.
- Session results are appended below when the row closes.

## 🛑 RESOLUTION AUDIT — 2026-07-30, Machine A (`Dev`): 159 of 424 pictures were 1K

Cameron asked what had actually been made this session. Counting it turned up a defect
nobody had looked for.

| resolution | count |
|---|---|
| 1536x2752 (2K, correct) | 265 |
| **768x1376 (1K — BELOW the 1080x1920 delivery size)** | **159 (37%)** |

**Affected stories:** `10-well` 32/32 · `11-storm` 32/32 · `12-bartimaeus` 35/35 ·
`13-roof` 43/43 · `14-ten-lepers` 14/31 · `05-bent-woman` 3/37. Rows 10-13 are
*entirely* 1K, which means Flow's upscaler was down for a long unbroken window and
every picture generated in it took the fallback.

**Cause, and why it went unnoticed.** `flow_driver.cmd_gen` catches `UpscaleFailed`,
takes the 1K original rather than losing the picture, and writes a `.size` marker
beside it so that — in its own words — *"a later pass can find every still that is not
at the intended size and re-pull it."* The fallback is the right call. **The later pass
was never written.** 158 markers accumulated and nothing ever read one, while both
`v2_prompt.gen()` and `v2_run_all` counted any file over 50 KB as DONE. So the library
quietly filled with pictures that will upscale on every Ken Burns move — the exact
thing the anti-shimmer law and Cameron's "same quality from Flow" order exist to stop.

**Fix (commit 4c3b11a45): a sub-2K still now counts as MISSING, not done.** Both the
single-row generator and the all-rows runner re-pull it on every lap until it comes
back at 2K, so the library self-heals with no list to maintain. The detector reads the
JPEG SOF header directly (no Pillow dependency), also honours a `.size` marker, and
was verified against Pillow on all 424 files — 424 agreements, 0 disagreements.

**Second failure, worth recording:** `v2_run_all` died at 2026-07-29 16:05 and nothing
restarted it, so Flow sat idle for ~9 hours. The runner was built to stop the browser
ever idling and then failed on exactly that, because it had no supervisor. A restarting
wrapper is the obvious next fix.

**Pictures generated this session by processes this machine started: 224.** Row 2 (22
Flow gens over two QC passes), row 3 zacchaeus (26), and 178 via the runner as other
sessions authored rows 4-11. The 3 Gemini API calls at the start saved nothing — all
failed on depleted credits, which is what led to the FLOW-ONLY law.

