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

### Session 10 CLOSE — 2026-08-01 (Claude worker 8, Machine A / `Dev`) — SHIPPED

Worker 7 died mid-run. Worker 8 read the TRUE state from disk (not from the
commit message): 38 of 49 images on disk, 11 beats with nothing — their take-1
files already in `_rejected/`. Worker 7 had already hardened all 17 reroll
beats' text, so no re-authoring was needed; the outstanding b20 no-rope clause
was committed, `v2_prompt.py --check` re-run (PASS, 49 beats), and the 11
generated under recomputed ceilings.

- 11 finishing shots + 5 reroll passes = $1.87 this session (meter $39.40 →
  $41.54). Row total across both sessions ~$9.64. Reroll rate 30% (21 defect
  passes / 50 keeps).
- Three law violations caught at QC: s22 (a second bearded man **in cream**
  blurred at the frame edge — the only-Jesus-wears-cream law — plus lens gaze),
  s31 and s38 (camera-gaze). **Lesson: the wording that fixed all three was
  GEOMETRIC, not prohibitive** — say where the camera sits relative to the
  eyeline and which frame edge the gaze exits through ("the camera sits BELOW
  his eyeline… his eyes are aimed clearly ABOVE and to the left of the lens…
  his pupils are never centred on the lens"), instead of only forbidding
  "looking at the camera". A pure prohibition failed twice on s22; the
  side-three-quarter geometry fixed it in one pass.
- **AUDIO FINDING:** row 10's V1 "final" MP4 is a TRUNCATED 67.70 s render —
  V1 never actually finished this row, though the reviewer card had been
  pointing at it since July. The extracted timeline is 294.294 s, so the
  byte-identical audio lock correctly refused to mux. Fixed WITHOUT re-voicing:
  the master audio was rebuilt from the authoritative per-segment mp3s in
  `media-production/build-10-well/audio/`, each placed at its own `seg_start`
  from the fixed `extract_beats.py`. Result 294.294 s, matching the picture
  timeline to 6 ms. Same approved voices; nothing re-recorded.
- Shipped: `build-10-well/john-4_woman-at-the-well-realistic-v2.mp4`,
  verify-mp4 OK 294.30 s video / 294.294 s audio / 21.7 MB. Reviewer card
  repointed with the new blob hash + cache-buster; `sync-reviews.mjs` run.


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

### Row 9 close — realistic rebuild DONE, cut shipped (2026-08-01)

| row | slug | beats | gens | accepted | rerolls | spend | status | notes |
|---|---|---|---|---|---|---|---|---|
| 9 | build-09-rich-ruler | 31 | 46 (1 anchor + 31 beats + 14 reroll passes) | 32 | s01 GAZE+DRIFT+ORNAMENT · s02/s03 SPRINT-ECHO · s08 SEATED-STAGING · s09 t2 rejected (t1 restored) · s12 LOWERED-LIDS (love frame retake) · s14 STRAY-BLURRED-JESUS · s21 CAST-LAW (John's hair) · s22 CAMERA-GAZE · s27 ×3 (direction logic, three-stranger read, one WASTED reroll on an unapplied prompt edit — recorded honestly) · s28 ×2 (gaze, chase-read) · s31 WRONG-FACING | ≈$6.16 | **DONE — realistic V2 shipped, awaiting Cameron** | 196.8 s · 21.9 MB · AUDIO LOCK PASS 925aaf90… · verify-mp4 OK |

- **All 31 windows re-timed** from the fixed `extract_beats.py` — the Jul 29
  windows put the card at ~177 s vs the real 189.03 s. Key discovery worth
  keeping: the V1 mp3s keep their LEADING silence (only trailing is trimmed),
  so `audio_start + raw phrase time` IS the absolute time — no lead-trim
  arithmetic. Sub-phrase splits (n0b "everyone," / j1's KJV clauses) were
  placed on real breath pauses measured with silencedetect.
- **Shared-meter lesson held:** the concurrent story-08 worker ate two of this
  build's `--ceiling`s mid-run; `--only` slices with per-run recomputed
  ceilings resumed cleanly each time, exactly as Session 8 prescribed.
- **Rough-echo lesson recurred in a new form:** s02/s03's roughs were DROPPED
  for the jog defect and the model still reproduced the jog from the scene
  text alone — when a rough is dropped for a defect, the scene text must be
  hardened against that same defect in the same edit.
- The founding-story frames: b12 take 2 (eyes open, unmistakable love) and b29
  take 1 (tears, love + grief, no relief) both pass the beat map's own
  standard; both Read individually at 2K.
- QC record: `build-09-rich-ruler/QC.md` · hash-locked boards
  `IDENTITY-QC.json` (42 appearances) · rejected takes in
  `assets-realistic/_rejected/`.
- Board card v9 → new hash `e8cb3734…` (returns to Unwatched); sync-reviews
  run; board deployed to Firebase. App-feed V1 untouched.

## Session 11 — 2026-08-01 — RECLAIM + SHIP: story 04 (Nicodemus at night) realistic rebuild (Claude worker 8, Machine A / `Dev`)

- **Reclaimed from Codex**, which claimed the row (`9fc3eeb05`) and ran out of
  credits. That claim commit is the last commit touching `build-04-nicodemus`;
  no progress was ever committed. Reclaim pushed (`47e461f7e`) before any spend.
- **30 uncommitted native-2K stills were found on disk and AUDITED, not
  regenerated** — re-rolling work already paid for would have cost ~$4 for
  nothing. 27 kept. 3 rerolled: two Jesus close-ups with CAMERA-GAZE, and s26,
  which failed its own beat (the whole point is the lamplight full and warm on
  Nicodemus's face for the first time; the frame had it cold and shadowed).
- **The windows were badly drifted: 23 of 30, several by a WHOLE BEAT** — s22
  "For God so loved the world" started 12.7 s after the line, and s21 sat on top
  of "For God sent not his Son". All recomputed from the fixed `extract_beats.py`.
- Re-timing exposed **four stretches of narration with no picture at all**,
  including a 16 s hole over "the darkest day". Four beats were authored and
  generated (b25b the words landing on the man who came in the dark, b29b the
  council turning on him, b29c the barred door with the apostles hiding — no
  crucifixion, no body — and b30b the hundred pounds of spices). Final timeline
  34 beats, continuous, nothing held longer than ~14 s.
- **Reroll rate 12% (4 passes / 34 keeps)** against the ~30% that had held on
  every previous row. Every reroll generated after the shared `DEFECT_LOCK`
  landed passed on the next attempt, and 3 of the 4 new beats were right on
  take 1. Spend this row: $1.07.
- Shipped: `build-04-nicodemus/john-3_nicodemus-realistic-v2.mp4`. AUDIO LOCK
  PASS (`5e23f1c7…`, byte-identical to the approved V1 final); verify-mp4 OK
  307.23 s / 19.3 MB. Reviewer card repointed, `sync-reviews.mjs` run, hosting
  deployed. App feed untouched.

### SHARED-RECIPE CHANGE (applies to every future row)

`v2_prompt.py` now prepends a `DEFECT_LOCK` block to EVERY prompt, alongside
STYLE-V2 and QUALITY_LOCK. It was added because the reroll rate had held at
~30% across builds 05/06/07/08/09/10 at a flat $0.134/image — $2-3 of pure waste
per video — and the same four defect families caused nearly all of it: lens
gaze, a stray unlocked figure (usually in CREAM) at a frame edge, uncountable
quantities, and recurring cast drifting off their sheets. The wording is PORTED
from the phrasings that measurably fixed each defect in the QC.md files of
rows 8, 9 and 10, not invented.

**The load-bearing lesson, learned the expensive way on row 10 s22 (a bare
prohibition failed TWICE; the geometry fixed it in one pass): state the
GEOMETRY, not the prohibition.** Say where the camera sits relative to the
eyeline and which frame edge the gaze exits through — "the camera sits BELOW his
eyeline… his eyes are aimed clearly ABOVE and to the left of the lens… his
pupils are never centred on the lens" — instead of only forbidding "looking at
the camera". The same held on row 4 s29b: "nobody faces the camera" failed, and
"the camera is well off to one side, not square to the room, so he is seen at a
three-quarter angle with his head turned away from the lens" fixed it.

---

## Session 12 — 2026-08-01 — RECIPE PROMOTION + CLAIM: story 15 (centurion's servant) realistic rebuild (Claude worker 10, Machine A / `Dev`)

- **Model:** Opus 5 (Claude Code) · **Machine:** Machine A — hostname `Dev`
- **RECIPE PROMOTION (commit `e2504586a`), done before any spend:** row 14's measured
  lesson is now in the shared `v2_prompt.py` recipe, so every later row gets it free.
  `WIDE_GEOMETRY_LOCK` is appended to every `wide` beat (ported byte-for-byte from row
  14's accepted b04/b19/b29 prompts), `POSITIVE_INVENTORY_LOCK` states headcount as
  what IS present ("ten men and no eleventh"), `JESUS_INVENTORY_LOCK` ("the only man
  in cream anywhere in the frame") rides only on beats Jesus is actually in, and
  `--check` now WARNs when a wide beat's own scene text never names the camera's
  position relative to the subjects' backs.
- **CLAIM (2026-08-01): story 15 `build-15-centurion` for the REALISTIC rebuild.**
  41 beats already prepped. New set generates to `assets-realistic/` via
  `v2_gen_api.py` (gemini-3-pro-image, native 2K, hard per-run ceiling recomputed from
  the live shared meter, `--only` slices). Audio LOCKED — no re-voicing. Windows
  re-timed from the fixed `extract_beats.py` and verified with silencedetect. The
  centurion carries ONE identity anchor (Roman officer, period-correct uniform, never
  cream); his soldiers and the Jewish elders stay visibly distinct groups. Ships to
  Reviewer only.

---

### Session 13 — 2026-08-01 (Claude worker 11, Machine A / `Dev`) — ROW 15 SHIPPED + LIBRARY-WIDE AUDIO AUDIT

Row 15 was handed over "blocked on audio, needs a re-voice". **Neither defect was
real, and the fix cost nothing.** Both were the same root cause, one level below
where the previous session looked.

| step | result |
|---|---|
| defect 1 — "never re-voiced" | **FALSE.** The mp3s on disk are 44.1 kHz / 128 kbps = ElevenLabs `mp3_44100_128`; edge-tts writes 24 kHz mono / 48 kbps. `JESUS-VOICE.json` independently records all four Jesus lines as Alexander. The only thing still naming `en-US-ChristopherNeural` was `make_narration.py`'s docstring, which was never updated after the migration. Nothing was re-voiced; REDO-ALL was already satisfied. |
| defect 2 — "V1 truncated at 256.000 s" | **FALSE — the 265.451 s timeline was wrong, not the video.** `extract_beats.py` decides the per-beat pad with `speaker != "narrator"`. This build predates SPEAKER-LAW, so its SEGMENTS carry the raw edge-tts voice name where the speaker constant goes; the test was true for all 26 beats, every one got the 1.15 s reverent KJV pad instead of 0.72 s, and the extracted timeline inflated by +0.43 s per narrator beat = **+9.45 s**. Rebuilding the V1 with its own `build.py` reproduced 256.0 s exactly, and `build.py`'s printed `j2 at 147.1 s` matches the fixed extractor's 147.106 s. |
| defect 3 — found while eyeballing frames | The same tuple-shape confusion put the TTS **rate** string in the caption slot (`SEGMENTS` here is `(id, voice, rate, pitch, text)`, so slot 2 is `"-15%"`). ffmpeg's `drawtext` failed with `Stray %` and **silently drew nothing** — the first assembly came out with caption BANDS and no words, and the closing card was blank too. `extract_beats` now uses V1 `build.py`'s own rule, `s[4] if len(s) >= 5 else s[2]`. |
| knock-on | the 42 windows the previous session re-derived off the inflated timeline were up to **9.03 s late**; all 42 shifted back and verified beat-by-beat against `silencedetect` on the real mix (n2 13.819 vs 13.823 measured, j1 76.12 vs 76.17, n13 124.60 vs 124.68, …) |
| delivered | 256.0 s · 21.7 MB · **AUDIO LOCK PASS** (packet-identical to the authoritative V1) · `verify-mp4` OK · captions white-narrator / red-Jesus in the bottom band · closing card whole and inside frame |
| spend | **$0.00** — no generation, no TTS. The V1 mp4 was rebuilt to prove the timeline, then reverted once its audio hash proved identical, so the repo carries no 21 MB of churn. |

**Library-wide sweep** — `media-production-v2/audio_audit.py` → `AUDIO-AUDIT.md`
(210 builds, header reads and source parsing only, no re-listening):

- **A — old-voice audio in a shipped video: ZERO rows.** Every take any build
  actually places on screen is ElevenLabs. Nothing on the reviewer is on an old
  voice. Rows 105 and 139 have leftover 24 kHz mp3s in `audio/` that no BEATS row
  references — dead files, called out explicitly so nobody re-raises the alarm.
- **B — V1 final short of its own timeline: 8 rows outstanding** (10 and 13 already
  fixed by a longer V2 cut). Only **17** and **99** carry row 06's real signature —
  a large delta *and* paid takes sitting in `audio/` that no beat places. The 3-5 s
  rows have no orphan takes and sit inside the audit's own arithmetic.
- **C — pre-speaker-law build with a V2 cut: zero outstanding.** Row 15 was the only
  one. Eleven more builds carry that SEGMENTS shape and are safe to rebuild now that
  the tool is fixed.

**The lesson worth carrying, and it is the second time this month:** when a build
looks broken, read what the FILES say, not what the SCRIPT'S PROSE says. Row 06's
complaint was "words are missing" and the audio was already there. Row 15's handoff
said "never re-voiced" and the ElevenLabs audio was already there — the claim came
from a docstring nobody had updated. Row 15's "truncated final" came from trusting a
derived number over the artefact it was derived from. Measure the artefact.

---

### Session 12 CLOSE — 2026-08-01 (Claude worker 10, Machine A / `Dev`) — PICTURES DONE, SHIP BLOCKED ON AUDIO

| step | result |
|---|---|
| recipe promotion | `e2504586a` + `5189766df` — WIDE_GEOMETRY_LOCK on every wide beat, POSITIVE_INVENTORY_LOCK on every beat, JESUS_INVENTORY_LOCK on Jesus beats, and a `--check` WARN when a wide beat's scene never states camera-to-back geometry |
| claim | pushed before any spend (`c0e8431f8`) |
| timeline | **V1 IS TRUNCATED.** The authoritative timeline is 265.451 s; `matthew-8_centurion.mp4` is exactly 256.000 s and its AUDIO STREAM is 256.000 s too, so the closing question card (narration 251.38 → 261.25 s) is cut off mid-sentence in the finished V1. |
| windows | all 42 re-derived as `audio_start + raw phrase start` from the fixed extract_beats. The inherited map drifted progressively to **+9.92 s** by n22 (j3 sat at 193.95 when the line starts at 202.25). |
| coverage hole | n1 held ONE picture for 12.49 s; authored `b01b` (the occupation arriving in the same lane) so the picture turns where the narration turns |
| beats | every one of the 42 upgraded to the realistic rubric: a real lens and aperture, a named light direction, and camera-to-back geometry on the wide multi-figure beats. b21's soldier no longer steps "toward the camera". |
| pictures | 42 at native 2K (1536×2752), `gemini-3-pro-image`, ceilings $49.35 / $55.20 / $55.70 recomputed from the live meter each run |
| reroll rate | **7 of 42 = 17%** (49 paid images, ≈$6.57) |
| defects found | a SECOND officer invented in the sickroom (b06); the centurion marching straight INTO the lens down a posed corridor (b08); camera gaze on a close (b09); the locked cuirass missing entirely, tunic only (b10); a cream-coloured foreground shoulder that reads as a second Jesus (b17); Jesus staring into the lens on the marvel frame (b24); the servant redrawn as a different young man (b38) |
| what fixed them | the same lesson, per beat: state the geometry / the positive inventory. All 7 came back correct in ONE pass. |
| **did the promotion work?** | **yes.** Row 14: 5 of 9 rerolls were wide-shot camera gaze. Row 15 with the lock in the shared recipe: **1 of 28 wide beats** failed that way (b08), and it was a beat whose own scene text still said the figures were "in the near frame" — the shared block alone caught the other 27. |
| tooling | `v2_assemble.py` now takes a `SPEAKER_OVERRIDES` map from a build's beats_v2 and falls back to `narrator` for unknown speakers. Pre-speaker-law builds store the raw edge-tts voice name in SEGMENTS, which crashed the caption colour lookup (`KeyError: 'en-US-AndrewNeural'`). |
| **SHIP BLOCKED — needs an audio pass, NOT pictures** | two coupled problems, both in the audio, both outside a picture worker's remit: (1) **the row was never re-voiced.** Its four Jesus lines (j1/j2/j2b/j3) are the old `en-US-ChristopherNeural` take — under the REDO-ALL law a cut carrying the old voice must not sit on the reviewer. (2) **the V1 audio itself is truncated** at 256.000 s, so locking V2 to it would ship a video whose closing question is cut off. Fixing (2) is assembly-only (the per-segment mp3s are all present and total 265.451 s) exactly like row 06's fix; fixing (1) is a re-voice. Both must happen before this row goes to the Reviewer. **The reviewer card was deliberately NOT repointed.** |

**Everything except the audio is finished and pushed:** 42 accepted 2K pictures in
`assets-realistic/`, the corrected 42-window beat map, and the rejected first
takes kept in `rejected/` for comparison.

---

## Session 11 — 2026-08-01 — CLAIM: story 14 (ten lepers) realistic rebuild (Claude worker 9, Machine A / `Dev`)

- **Model:** Opus 5 (Claude Code) · **Machine:** Machine A — hostname `Dev`
- **CLAIM (2026-08-01): story 14 `build-14-ten-lepers` for the REALISTIC rebuild.**
  Row 14 carries an open Cameron FIX-LATER ("~0:55 the ten lepers look like GIANTS
  next to Jesus and the disciples; fix the scale") — the rebuild must fix the scale
  by stating the geometry (where the camera stands, how far up each group of figures
  reaches in frame), not by forbidding "giants". 14 of its 31 existing V2 stills are
  768x1376 per the resolution audit; all fall under the Session 6 blanket rejection.
  New set generates to `assets-realistic/` via `v2_gen_api.py` (gemini-3-pro-image,
  native 2K, hard per-run ceiling from the live shared meter, `--only` slices).
  Audio LOCKED to the authoritative narration — no re-voicing. Windows re-timed from
  the fixed `extract_beats.py` and verified with silencedetect. Ships to Reviewer only.
### Session 11 CLOSE — 2026-08-01 (Claude worker 9, Machine A / `Dev`) — SHIPPED

| step | result |
|---|---|
| claim | pushed before any spend (STATUS + QUEUE + ledger, own files only) |
| timeline | V1 final is 219.133 s and NOT truncated — but the inherited `beats_v2.py` was written against a 197.7 s timeline, so **every one of its 35 windows was wrong**, drifting up to ~9 s by the end (j3 sat at 174.00 when the line actually starts at 183.26). All 37 re-derived as `audio_start + raw phrase start` from the fixed `extract_beats`, and `n6`'s single phrase sub-split with silencedetect (pause 4.24–4.73 s → 97.93 absolute). |
| coverage holes | two beats were holding one picture across 11.9 s (`n9 p3-p4`) and 11.5 s (`n11 p5-p6`). Authored `b24b` (the outsider alone in the circle they left around him) and `b30b`, and rewrote `b30` as the nine tiny and walking away. |
| pictures | 37 at native 2K (1536×2752), `gemini-3-pro-image`, ceilings $48.00 / $49.30 / $49.20 recomputed from the live meter each run |
| reroll rate | **9 of 37 = 24%** (b19/b29 twice → 48 paid images, ≈$6.43) |
| defects found | camera gaze on 5 wide travelling shots (b01 b04 b05 b12 b26) — the model's default for "group in the foreground" is a posed line facing the lens; **a SECOND, UNLOCKED JESUS standing in the middle of the line of ten lepers in b08** (long loose hair, bare face, pale robe); cast drift on b20 (a different, younger, black-bearded Samaritan than b21/b22/b28); reversed travel direction on b19 (the nine running *toward* camera, which destroys the "and he turned around" reversal) and b29 (walking *away* from the gate they were supposed to be entering) |
| what fixed them | the DEFECT_LOCK's own lesson, applied per beat: **state the geometry, not the prohibition.** "THE CAMERA STANDS BEHIND JESUS AND THE DISCIPLES AND SHOOTS PAST THEM: their BACKS fill the near frame … not one face is turned toward the lens" fixed b04 in one pass where a bare no-camera-gaze rule had already failed. For b08 the fix was positive inventory — "HE IS THE ONLY MAN IN CREAM AND THE ONLY MAN WITH LONG LOOSE HAIR AND AN UNCOVERED FACE … TEN men and no eleventh, every one with a strip of grey linen across the lower half of his face". For b20, text alone never held the Samaritan; the accepted `s21` was attached as a `char_refs` image anchor. For b19/b29, naming which way the *backs* face ("the viewer sees NINE BACKS … and NOT ONE FACE"). |
| assembly | `v2_assemble.py 14` — AUDIO LOCK PASS, SHA256 `5da3ec2951b0a294389f2739f75570b30f72f56ece33bbac8e615bab504db35c`; 1080×1920, 219.133 s, 22.1 MB; captions checked on 11 extracted frames (bottom band only, white narrator, red KJV Jesus, question card intact) |
| ship | card `v14` repointed to the new blob hash `cd69c450…` with cache-buster, `sync-reviews.mjs` run, Firebase hosting deployed, live card verified serving the new hash |

**Lesson for the shared recipe (worth porting):** in any wide shot where named
figures stand in the foreground, the model's default is a posed line facing the
lens — the DEFECT_LOCK alone does not beat it, because the scene text says
"stand in the foreground" and the model resolves that as a portrait. Naming the
camera's position relative to their BACKS beats it every time, and usually makes
a better picture: b04 shot past the travellers' shoulders turned the empty gap
itself into the subject, which is exactly what that beat is about.

---

## Session 10 — 2026-08-01 — CLAIM: story 10 (woman at the well) realistic rebuild (Claude worker 7, Machine A / `Dev`)

- **Model:** Fable 5 (Claude Code) · **Machine:** Machine A — hostname `Dev`
- **CLAIM (2026-08-01): story 10 build-10-well for the REALISTIC rebuild** —
  assigned row (parallel workers hold 04/08/09 etc.). Row 10's 32 existing V2
  stills are ALL 768x1376 (the resolution audit below: the entire row generated
  inside Flow's upscaler-down window) AND fall under the Session 6 blanket
  rejection — none can ship. They stay in `assets/` untouched as rough-draft
  composition refs at most (ROUGH-DRAFT CONTINUITY LAW; rough-echo corollary
  from row 9 applies — if a dropped rough's defect reproduces from scene text,
  the scene text gets hardened in the same edit). The realistic set generates
  to `assets-realistic/` via `v2_gen_api.py` (gemini-3-pro-image, native 2K,
  hard per-run ceiling recomputed from the live shared meter, `--only` slices).
  Audio stays LOCKED to the authoritative narration — this is one of the app's
  FOUNDING stories (the onboarding uses it); no re-voicing, encoded-audio hash
  lock at assembly. This row carries a WOMAN speaker (w9/w11/w15/w19/w25/w29
  KJV lines) alongside narrator + Jesus. All windows re-timed from the fixed
  `extract_beats.py` (the old windows carry the raw-vs-trimmed drift) and
  verified with silencedetect. NOON light is CORRECT here ("the sixth hour").
  Ships to Reviewer only; app feed untouched.
- Session results are appended below when the row closes.

---

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



---

## Row 16 — Mary and Martha (Luke 10) — realistic V2 rebuild

**Claimed 2026-08-01, Claude worker 11, Machine A (`Dev`).** Beats already authored
(25 pictures, evening interior at Bethany). Audio is LOCKED to the authoritative
narration — nothing re-voiced. Plan: `v2_prompt.py --check` PASS, generate at native
2K under a hard ceiling, QC every image by eye, re-time all windows from the fixed
`extract_beats.py`, assemble, verify rendered frames, ship to the Reviewer only.

**Shipped 2026-08-01 (43c9d5716 / 48e970c0a).** 26 pictures at native 2K; 51 paid
generations for 26 finals (49% reroll), ≈$6.83, meter $62.44. Every reroll was a law
violation, and the same four families accounted for nearly all of them:

1. **Period-wrong light.** Glass kerosene hurricane lamps, a modern hanging fixture and
   a wrought-iron candelabra kept appearing. Root cause: the HOUSE lock (which names the
   clay saucer lamps) was only attached to the wide beats, so the 14 tight shots invented
   their own lighting. Fix: HOUSE now rides every beat in the build.
2. **Establishing-shot anachronism.** An aerial Bethany-over-Jerusalem came back twice
   with the Dome of the Rock, satellite dishes, tiled roofs and street lights, and once
   letterboxed. Naming the period did not beat it; replacing the aerial panorama with a
   GROUND-LEVEL village lane did, first try. Lesson: when a shot's subject is a skyline,
   the model fills it from photographs of the modern city — remove the skyline.
3. **Identity drift on the two sisters.** Martha's hair came loose, Mary grew a
   headscarf, aprons turned into modern bib aprons and skin went pale. Fixed by writing
   the invariants INTO the character locks (hair always bound/always bare, olive-brown
   skin, no buttons or closed shoes) plus a second image anchor for Martha.
4. **Style/format breaks.** Two beats returned as painted illustrations and one as a
   three-panel strip. Both were cured by one sentence in the beat's own scene text
   naming it as ONE photograph on a fast prime lens with grain.

Also worth recording: `v2_gen_api.py --only` matches beat ids by SUBSTRING, so `--only b03`
also regenerates `b03b`. That silently overwrote a character anchor mid-run once. And
`v2_assemble.py`'s AUDIO LOCK requires exactly one MP4 in the V1 folder; row 16's V1 folder
holds a committed pre-REDO backup (`...orig.mp4`) alongside the authoritative cut, so the
backup was moved aside for the mux and restored immediately afterwards — V1 is unchanged.


---

## ROW 18 — The Road to Emmaus (Luke 24) — Claude worker 12, Machine A `Dev`, 2026-08-01

**CLAIMED** before any spend. V1 `media-production/build-18-emmaus/luke-24_emmaus.mp4`
is 243.322 s and carries only EIGHT distinct stills for the whole story (S9B/S10B were
authored and then dropped from BEATS), so this row needs a full realistic beat map, not a
repair. All 18 narration segments are already ElevenLabs (44.1 kHz / 128 kbps) — audio is
LOCKED and will not be re-voiced.

**SHIPPED 2026-08-01** — `luke-24_emmaus-realistic-v2.mp4`, 243.3 s / 21.4 MB, AUDIO LOCK
PASS (SHA256 6827c039…), verify-mp4 OK, blob `e0e3e726…` live on the reviewer.
41 pictures, ≈$12.06, reroll rate 39% (16 of 41).

WHAT THIS ROW COST AND WHY — read this before the next one:

1. **~$4 of the $12.06 was pure operational waste, not rerolls.** A `v2_gen_api.py` run
   was moved to the background by the harness; `pgrep` showed nothing and the log file was
   empty, so it was judged dead and restarted. It was not dead. Worse, the restart command
   was issued TWICE (the first one's `tail` failed on an unexpanded variable, which read as
   the whole command failing when only the tail had). Three processes then generated the
   same beats concurrently and every one of them was billed: 90 images were charged for 41
   keepers. **An empty log file and a silent pgrep are NOT proof a paid process is dead.
   Confirm by the artefacts it is writing (the asset mtimes), and never issue a second
   start command without first proving the first one is gone.**

2. **Reroll families, all fixed in SHARED locks (row-16 lesson holding):**
   - *Anachronistic Jerusalem.* The skyline came back with a minaret, a church campanile
     and red pitched tile roofs. New `JERUSALEM` lock states the AD 33 city positively
     (dressed limestone, square crenellated towers, flat roofs, the Second Temple highest).
   - *Direction of travel reversed.* The walled city rendered at the END of the road in
     front of the men, so the picture read as walking TO Jerusalem. New `OUTBOUND` lock:
     "THE ROAD AHEAD ENDS IN EMPTY HILLS, NOT IN A CITY," attached to all 15 outbound beats.
   - *Glass kerosene lamps in tight interiors.* Exactly row 16's failure, in a build whose
     HOUSE lock named clay lamps but never forbade glass. The full prohibition now rides
     the HOUSE lock so tight shots inherit it.
   - *Recurring-character drift.* The companion rendered as a beardless youth three times.
     Root cause worth recording: **both image anchors showed him only from BEHIND, so no
     anchor carried his face.** An anchor that does not show the character's face does not
     hold the character. Fixed by writing the invariant into his lock AND swapping the
     anchor to a frame where both disciples' faces are clearly visible.

3. **A beat's own scene text must not contradict the shared locks — and I wrote the
   contradiction myself.** The b01 geometry sentence said the men's backs faced "the camera
   and Jerusalem", which puts the city where the lens is. The model resolved that
   impossibility by moving the city in front of them, defeating the OUTBOUND lock. When a
   beat needs both a character's back AND a landmark they are leaving, the camera has to go
   to an elevated or side vantage; it cannot stand where the landmark is.

4. **`site/review.html` flag strings are NOT unique** — `🛠 What this cut changed
   (2026-07-28): narration re-recorded` appears 132 times. A bare `str.replace(old,new,1)`
   silently edited **row 17's** card (the deferred Lazarus row). Caught and reverted before
   commit. **Always slice the card out by its `id="vNN"` boundaries and edit inside that
   slice**, then check `git diff` line counts before committing.

5. Two beats needed a second reroll after the first fix: b28 (the profile framing let the
   model reinvent Jesus's face younger and shorter-haired — cured by naming the reference's
   hair and beard explicitly in the beat) and b35 (the upper room returned as a stacked
   three-panel strip — cured by the recorded "ONE SINGLE PHOTOGRAPH FILLING THE WHOLE 9:16
   FRAME, not two or three stacked horizontal panels" sentence in the beat's own text).

---

## Row 19 — Breakfast on the Shore (John 21) — Claude worker 13, Machine A `Dev`, 2026-08-01

SHIPPED to the reviewer 2026-08-02. Audio LOCKED (reused unchanged, never re-voiced).
37 pictures at native 2K against V1's 16; every window recomputed from the fixed
`extract_beats.py`. **Spend $6.56** — $4.96 first pass (37 images), $1.47 rerolls (11),
$0.13 a second reroll of b27. One generator process at a time, every run under a hard
`--ceiling` recomputed from the live meter; meter $74.50 → $81.07, zero duplicate billing.
Reroll rate 32% (12 of 37). Full detail in `build-19-shore/QC.md`.

### Lessons this row paid for

1. **A NEW SETTING is where the money goes, and the fix belongs in the SHARED recipe.**
   Rows 16 and 18 both paid for the interior half of this lesson (glass kerosene lamps, a
   candelabra, a modern fixture) and both times the fix went into ONE build's HOUSE lock —
   so row 19, the first build set in an open boat on a shore, had no protection at all and
   invented a modern circular cast net with moulded floats and a dressing-gown robe. Two new
   shared blocks now ride on EVERY V2 prompt: **PERIOD-MATERIALS** (what everything IS made
   of — hewn wood, twisted flax, fired clay, hand-forged iron, hand-woven wool; every open
   flame a bare wick or a wood/charcoal fire) and **GARMENT-CONSTRUCTION** (a garment is a
   straight woven rectangle; no shawl collar, lapel, placket, cuff, buttons or bow-tied sash).

2. **An approved character sheet does not hold a character who is SMALL in the frame.**
   Peter came back as a grey-haired old man in three shots — every one of them a wide or
   middle-distance frame — while every close-up matched the sheet perfectly. The CAST-V2
   images are face sheets, so their weight collapses with subject size. Cure: an explicit
   AGE-AND-HAIR INVARIANT in text (`PETER-HOLD`), attached to every beat that names him,
   restating the invariant "near, far, sharp or blurred". Row 18 learned that an anchor must
   SHOW the face; row 19 adds that an anchor cannot carry a figure the size of a thumbnail.

3. **A face can come back as a light SOURCE.** Two background figures around night coals
   rendered as burning red masks. The scene said "faces lit orange from below", and the model
   resolved "lit" as "luminous". The COURTYARD lock now says a face receives light and never
   emits it — worth porting to any future night-fire build.

4. **The lens-gaze defect can survive a correctly-worded fix.** b27 (the "lovest thou me"
   frame) kept putting Jesus's pupils on the lens even after the geometry sentence named the
   camera's position. What finally cured it was giving the gaze a TARGET INSIDE THE FRAME:
   an over-the-shoulder two-shot with Peter's out-of-focus shoulder in the near frame. When a
   tight shot of one person keeps looking at the viewer, put the other person in the picture.

5. **The V2 folder's copy of a build's narration script can be STALE.** build-19-shore's V2
   copy of `make_narration.py` and `audio/` predate the V1 folder's by a day and are missing
   four retellings that ARE in the shipped audio. `extract_beats.py` reads the V1 build, which
   is correct; a beat map written from the V2 folder's script would have been wrong about four
   segments. Never read a build's script from the V2 folder.

6. **`site/review.html` card edit, done safely:** the card was sliced out by its `id="v19"` /
   `id="v20"` boundaries, edited inside that slice, and the result diffed — exactly 3 lines
   changed, all inside v19, and the v12, v17, v18, v20 and v21 cards verified byte-identical
   by SHA-256 before commit.


---

## Session — 2026-08-02 · Row 20 (The Good Samaritan, Luke 10) — DONE

- **Worker:** Claude worker 14 · Machine A `Dev` · Fable 5
- **Shipped:** `build-20-samaritan/luke-10_good-samaritan-realistic-v2.mp4`
  186.665 s / 21.5 MB · AUDIO LOCK PASS `d3fe79df…` · blob `ae1a417e2096`
- **Pictures:** 42 at native 2K (V1 had 8) · reroll rate **12 % (5 of 42)** · **$6.30**
  (meter $81.07 → $87.37, one generator process at a time, hard ceiling every run)
- **QC:** `build-20-samaritan/QC.md`

### Lessons this row paid for

1. **THE SCRIPT CAN BE STALE EVEN INSIDE THE V1 FOLDER.** Session 19 concluded "never read
   a build's script from the V2 folder" — row 20 shows the V1 folder's own
   `make_narration.py` can also be wrong. It was rewritten programmatically AFTER the voices
   were cut (string quoting flipped `"` → `'` throughout) and the rewrite STRIPPED the
   plain-English retellings out of n1b / n12 / n14 / n15. All four are audibly in the shipped
   mp3s. `make_narration.py.pre-echo` is the file that matches the audio.
   **Rule: when a build has a `.pre-echo` / `.pre-speaker` sibling that DISAGREES with the
   live script, transcribe the mp3s before trusting either file.** The tell is cheap — the
   `timing.json` sidecar lists the phrases that were actually synthesised, so if it has three
   entries and the script has two sentences, the script lost something.

2. **Stale caption text is not only wrong words, it is wrong TIMING.** `timed_windows` matches
   the caption text character-by-character against the timing sidecar, so a segment whose text
   no longer matches its audio gets both the wrong words *and* the wrong `enable=` windows.

3. **New shared hook: `TEXT_OVERRIDES` in `v2_assemble.py`.** A build may declare
   `TEXT_OVERRIDES = {seg: text}` with the words genuinely spoken; the assembler logs each
   one as it applies it. Opt-in, so no existing row changes behaviour, and V1 is never edited
   (hard protection #1). This is the shared-lock discipline applied to the audio side.

4. **ANCHOR-FIRST ORDER CUT THE REROLL RATE FROM ~32 % TO 12 %.** Six face-showing beats were
   generated as their own run, inspected, and wired into `REFS`; the other 36 then ran with
   every recurring face attached. Rows 16/19 generated everything in one pass and paid 49 %
   and 32 %.
   **But `v2_gen_api` builds its REFS cache ONCE at the start of a run**, so any anchor that
   lands mid-run is invisible to the rest of that run — b29's Samaritan came back as a
   grey-haired old man for exactly this reason. Anchors must be a SEPARATE process invocation.

5. **The row-19 lens-gaze cure generalises and works first time.** b38 was a tight 135 mm
   portrait of Jesus with his pupils effectively on the lens; rebuilding it as an
   over-the-shoulder two-shot fixed it in one pass. Do not spend a second roll on a lone
   tight portrait — put the other person in the frame immediately.

6. **New settings invented their own anachronisms again, as predicted:** a metal pin buckle on
   a sandal and pale moulded shoe soles (footwear is a fresh surface every row), and a cream
   head-cloth in a crowd foreground. All three were cured by stating the object POSITIVELY —
   what the sandal IS made of, what colour every piece of cloth IS — never by prohibition.

7. **`site/review.html` card edit, done safely:** each of the three edits was anchored on
   something unique to row 20 (its old `data-hash`, its V1 mp4 path, and a flag line located
   strictly between the v20 card tag and `id="v21"`), then diffed — exactly 3 lines changed,
   all on the v20 card. Rows 12 and 17 untouched. The row-20 card was also given the
   `data-review-wave="realistic-v2"` attribute that `admin/sync-reviews.mjs` requires for the
   version lock; **note that row 19's card is still missing it**, so row 19's hash is not being
   overridden in the sync and someone should fix that card.

---

## ROW 21 — The Lost Sheep (Luke 15) — DONE 2026-08-02

Claude worker 15, Machine A `Dev`. 33 pictures at native 2K against V1's SEVEN.
Delivered `media-production-v2/build-21-lost-sheep/luke-15_lost-sheep-realistic-v2.mp4`,
147.237 s / 20.9 MB, AUDIO LOCK PASS (SHA256 `cec51e8c…`), blob `a57264ac…` live on the
reviewer. **≈$5.36** (meter $87.37 → $92.73): 3 anchors $0.40, 2 anchor rerolls $0.27,
30-shot main pass $4.02, 5 beat rerolls $0.67. One generator process at a time, a hard
`--ceiling` recomputed from the live meter on every paid run, no duplicate billing.

1. **The sourcing check paid off by NOT costing anything.** This build carries BOTH a
   `make_narration.py.pre-echo` and a `.pre-speaker` sibling, and `.pre-echo` disagrees
   with the live script on n9b. Rather than trust either file, the mp3 was transcribed
   with faster-whisper: the LIVE script is what is spoken, and its `timing.json` agrees
   (3 phrases, 5.759 s against a 5.799 s file). No `TEXT_OVERRIDES`. **The cheap tell
   from row 20 generalises — compare the timing sidecar's phrase text against the script
   before assuming either file is right.**

2. **V1's picture starvation was the worst yet on any row so far:** ONE still held the
   screen from 96.6 s to 138.5 s — 42 seconds across four separate segments.

3. **A repeated STORY needs a different ROOM.** Luke 15 holds the prodigal (row 2), the
   lost coin (row 8) and this parable, told at one sitting to one audience. Rows 2 and 8
   already staged that opening outdoors, so row 21 is staged INSIDE a village house at
   the meal with the religious men standing in the doorway refusing to cross it — which
   is also the truest reading of v2, since the offence is that he EATS with them. **Check
   what the library already shows before staging a shared occasion.**

4. **Anchor-first casting again: 21 % reroll (7 of 33).** Higher than row 20's 12 %,
   entirely because this row invented three new settings at once (a house interior, a
   dry-stone fold, a hill village) and each one minted its own anachronism, exactly as
   the ledger predicted. The anchors themselves held: the shepherd is the same man in
   all 15 of his frames, near, far, front and back.

5. **THE PHRASE "UNDYED GREY-BROWN WOOL" IS WHAT MAKES CROWDS COME BACK NEAR-WHITE.**
   Both crowd locks listed it as a lawful earth colour while the same sentence forbade
   cream, and the model resolved it as pale oatmeal — two enormous near-white backs in
   the foreground of the opening wide. Removed from both palettes, plus a new clause
   pinning the ONE OR TWO FIGURES NEAREST THE CAMERA (the biggest shapes in the picture)
   to deep umber and dark indigo. **A colour lock has to name what the biggest shape in
   the frame IS, not just what nobody may wear.**

6. **The same trap bit the shepherd's own costume.** His lock gave him a "sheepskin
   over-mantle of dark brown fleece"; it rendered as a large CREAM fleece across the
   chest of the video's central recurring character. The garment was deleted from the
   lock outright rather than re-described — the cheapest fix for a garment that keeps
   coming back the wrong colour is to not put it in the scene.

7. **New settings, new anachronisms, all cured POSITIVELY and in a SHARED lock:**
   plastic ear tags on the sheep → a no-modern-marks clause in FLOCK and ONE-SHEEP;
   galvanised pipes and a plastic roof vent on the village skyline → VILLAGE now states
   what a first-century roof carries and that nothing else projects from it; a printed
   page seam and gutter down one frame → an explicit one-photograph-edge-to-edge sentence
   (the anti-panel clause alone did not catch a *page* seam).

8. **The lens-gaze cure worked first time for the third row running.** The celebration
   wide came back with the shepherd's pupils on the lens; giving his gaze a named target
   inside the frame (the old man beside him) fixed it in one pass, and the same move
   turned the lane shot from advancing-into-camera into a cross-frame stride.

9. **Review-board edit, done safely:** anchored on row 21's old `data-hash`, its V1 mp4
   path, and a flag line located strictly between the v21 card tag and `id="v22"`, then
   diffed — exactly 3 lines changed, all on the v21 card, rows 12 and 17 byte-identical.
   The card carries `data-review-wave="realistic-v2"`, verified on the LIVE page after
   deploy. Note for the next worker: `media-production-v2/.gitignore` ignores `*.mp4`,
   so the delivered cut needs `git add -f` — a plain `git add` of the build folder
   silently commits nothing.

---

## Session — 2026-08-02 · Row 22 (The Unmerciful Servant, Matt 18) · Claude worker 16

- **Machine:** Machine A — hostname `Dev`
- **Status:** `BLOCKED(firebase hosting storage quota)` — the cut, the beat map and the
  repointed review card are all built, verified and committed; only the deploy is blocked.
- **Spend:** ≈$6.71 (50 paid images at $0.134: 48 delivered + 2 extra passes on the king
  anchor). Meter $92.73 → $99.96. No duplicate billing; one generator process throughout.
- **Reroll rate:** 10% (5 of 48 delivered beats needed a second pass).
- **Cut:** `media-production-v2/build-22-unmerciful-servant/matthew-18_unmerciful-servant.mp4`
  — 225.033 s / 21,676,069 bytes, AUDIO LOCK PASS (SHA256 9ce3eb99…), identical duration to V1.

### What this row cost, and what it taught

1. **THE SOURCING TRAP BIT, AND BOTH SIBLINGS WERE WRONG.** This build carries a
   `.pre-echo` and a `.pre-speaker` narration sibling, and the live script disagrees with
   `.pre-echo` on TWO segments. Transcribing the shipped mp3s with faster-whisper split the
   verdict: on **n14** the LIVE script is right, but on **n1 NEITHER file is** — the mp3 is
   2.534 s long and contains only "Peter must have thought he was being generous.", while
   both scripts open it with a retelling nobody says. Printing either would have drawn words
   Cameron never hears AND mistimed the segment, because `timed_windows` matches caption text
   against the timing sidecar character by character. Fixed with the shared `TEXT_OVERRIDES`
   hook; V1 was never edited. **Lesson: "the live script is authoritative" is not a rule —
   transcribe when the siblings disagree, and be ready for the answer to be "neither".**

2. **An inherited beat map can be worse than no map.** The 38-beat map dated 2026-07-29 had
   THREE windows that were copy-paste wrecks (b29 122.03-123.52, b31 13.45-15.09, b34
   19.62-25.38) — all sitting at the END of the story while pointing back into its first
   thirty seconds — plus a 7.79 s hole where Jesus's "until seventy times seven", the single
   most important line in the row, had NO PICTURE AT ALL. It was discarded, not re-timed.

3. **A SHARED TOOL BUG that would have hit future rows: `v2_assemble` globbed every `.mp4`
   in the V1 folder** and demanded exactly one. Three V1 builds keep a pre-fix backup beside
   the shipped cut; build-22 has a stale 245.000 s `.orig.mp4` next to the real 225.033 s
   cut, so the AUDIO LOCK refused to run at all. Backup suffixes (`.orig/.bak/.old/.prev`)
   are now excluded in `v2_assemble.py`, with V1 left read-only.

4. **New settings invent new anachronisms — the palace hall proved it twice.** The king's
   identity anchor came back with a GOTHIC-TRACERY chair and a HALF-TIMBERED European wall,
   and a later hall wide had a MODERN LIGHT FIXTURE mounted above the doorway. Both fixes
   went into the SHARED `HALL` lock stated positively (the seat is plain squared cedar with
   straight incised banding; every wall is smooth lime plaster over dressed stone with no
   exposed timber framing; the clerestory slots are the only light and nothing else emits).

5. **`--redo` INHERITS THE DEFECT IT IS MEANT TO FIX.** The first king reroll used `--redo`,
   which attaches the defective frame as the rough-draft ref, and the ROUGH-DRAFT CONTINUITY
   LAW then told the model to preserve the very wall and chair being rejected — so the
   anachronism survived a paid pass. **To fix a composition-level defect: delete the file,
   withhold that character's own REFS entry, and generate fresh with no reference.** That
   cost one image to learn.

6. **A face sheet does not hold a character who is small in frame — again.** The debtor
   drifted into a fair-skinned, short-brown-haired, near-clean-shaven man in the one wide
   where he is the near figure seen from behind. Restating his locked identity POSITIVELY
   inside that beat's own scene text ("weathered olive-brown skin, cropped black hair
   receding at the temples, thin black beard … never a different man from the one who lay
   on the hall floor") fixed it in one pass.

7. **The lens-gaze cure worked first time for the fourth row running.** Both Peter beats
   came back with his pupils on the lens; giving the gaze a NAMED TARGET INSIDE THE FRAME
   (Jesus's face on the step) and putting the camera behind his shoulder fixed both at once.

8. **Staging checked across the library:** rows 2, 8 and 21 already stage Luke 15 teaching
   scenes and row 16 a lamplit interior, so this frame story sits OUTSIDE on a BLACK BASALT
   Capernaum doorstep. Basalt rather than the honey limestone every other row uses makes the
   row instantly distinguishable. Matthew 18:26 and 18:29 are shot as a deliberate mirror —
   same camera height, same seen-from-behind stretched-out posture — so the two beggings
   rhyme and the forgiven man is standing exactly where the king stood.

9. **Review-board edit, done safely:** anchored on the v22 card's own `id` + old `data-hash`,
   its old V1 mp4 URL and its own flag line; diffed afterwards — 6 lines changed, all on the
   v22 card, rows 12 and 17 byte-identical. The card carries `data-review-wave="realistic-v2"`.

### ⚠️ HANDOFF — the one thing not finished

`npx firebase-tools deploy --only hosting` fails with **HTTP 429: "You have exceeded the
Hosting storage quota for your Firebase project."** Only the `live` channel exists, so the
storage is accumulated release versions of that channel. Clearing it means either deleting
Cameron's Hosting release history or moving the project to the Blaze plan — both are his
call, and the CLI exposes no `hosting:versions:delete`, so the next worker should NOT try to
brute-force it. Everything else for row 22 is committed and verified; the board will show
the new cut the moment a deploy succeeds.

---

## Row 23 — The Workers in the Vineyard (Matthew 20) — realistic V2, 2026-08-02

**Spend ≈$6.16** (4 anchors $0.54 + 36 beats $4.82 + 6 rerolls $0.80). Meter after: $106.13.
**Reroll rate 15% (6 of 40).** 40 pictures against V1's EIGHT; 202.967 s delivered, identical
to V1 to the millisecond; AUDIO LOCK PASS (SHA256 25ee3f63…). Git blob 35c29eba…

1. **V1's real defect was coverage, and it was the worst yet on the rows I have seen.**
   `s3-eleventh-hour.jpeg` held the screen from 32.83 s to 73.79 s — FORTY-ONE SECONDS across
   six separate segments (n5, j6, j7a, n5b, j7b, n6). That single still covered the entire
   turn of the parable: the owner's question, the labourers' answer "no man hath hired us,"
   and the retelling of both. `s7-friend-reply.jpeg` held another 34 s across n11/j1/n12.

2. **SOURCING TRAP checked and CLEARED.** The `.pre-speaker` sibling is the whole
   pre-SPEAKER-LAW script and contains none of j6/j7a/j7b/j12/n5b/n10b, yet all six mp3s
   exist in `audio/`. Eight segments (n1, n5, n5b, n6, n10, n10b, n14, card) were transcribed
   with faster-whisper and every one matches the LIVE script word for word — including the two
   the SPEAKER-LAW rebuild trimmed. No `TEXT_OVERRIDES` needed on this row.

3. **The inherited 30-beat map was DISCARDED, not re-timed** — it ran on a 171.6 s timeline
   against the real 202.9 s. Every window recomputed from the fixed `extract_beats.py` and
   split on each segment's own `timing.json` phrase boundaries: contiguous 0.28 s → 196.518 s,
   zero gaps, 4.91 s/picture, and all 22 segment speech-starts verified to fall inside the
   window written for them.

4. **THE CLOCK IS THE PLOT on this row**, so the time of day carries the story without a word:
   first light (blue-grey, gold only on the ridge) → third hour → hard white overhead noon →
   warm mid-afternoon → the eleventh hour with shadows stretched the length of the square →
   evening lit by one clay oil lamp. No orange sunset palette anywhere; evening arrives blue.

5. **Anchor-first casting held the rate to 15%** (4 face-showing anchors — landowner, last-hired
   man, foreman, first-hired man — generated in their OWN run, then wired into REFS).

6. **NEW SHARED LOCK — SEASON.** One frame came back with bare, winter-pruned vine stumps while
   every other frame in the row was in full leaf and fruit. Fixed by a SEASON clause written into
   this build's shared `VINEYARD` lock ("every vine stands in FULL GREEN LEAF and carries heavy
   clusters of dusty dark ripe grapes … no vine anywhere is a bare pruned-back winter stump").
   **Generalisable lesson for the library: any story that revisits one outdoor location across
   several hours needs the SEASON pinned in the setting lock, not just the light.** A setting
   lock that fixes time-of-day but not season will still produce a continuity break.

7. **Reroll causes, each fixed at the level that prevents recurrence:**
   - b04 came back as a posed line of men squared up to the lens (the camera sat directly behind
     the landowner, so their converging eyelines read as looking at the viewer). Cured by moving
     the camera SIDE-ON to the whole scene so every eyeline runs horizontally ACROSS the frame.
     This is the geometry lesson again: the fix was where the camera stands, not a prohibition.
   - b14 and b24 lost their locked man when he was mid-frame — the last-hired man drifted into a
     different, heavier man in a PALE TAN tunic, and the first-hired man lost his headband and
     face. Both fixed by restating the locked identity POSITIVELY inside that beat's own scene
     text (the row-22 lesson). A face sheet in REFS still does not hold a character on its own.
   - b32, the sentence the whole video is built to land ("Is thine eye evil, because I am good?"),
     came back with the man looking out at the viewer. The row-19/20 lens-gaze cure worked in one
     pass for the sixth row running: give the gaze a NAMED TARGET INSIDE THE FRAME — the
     landowner was moved to the left edge, softly out of focus but plainly there.
   - b36 had the dawn crew walking INTO the camera with faces to the lens. Fixed by moving the
     camera inside the yard to shoot at their backs as they leave through the gate.

8. **STAGING checked across the library:** rows 2, 8 and 21 stage Luke 15 teaching scenes, row 16
   a lamplit interior and row 22 a black basalt Capernaum doorstep, so this frame story sits on a
   TERRACED HILLSIDE ABOVE THE VINEYARD ITSELF — the parable's own landscape behind the man
   telling it, which no other row uses.

9. **Firebase note for future workers — CORRECTED 2026-08-02 (main session).** Worker 16 hit a real
   HTTP 429 Hosting storage quota on row 22 and correctly declined to delete release history on its
   own. The main session then ran `python3 media-production/prune_hosting_versions.py` (output:
   "pruned 7 old versions; live version kept: 86f38f18a869136a") and the redeploy succeeded,
   publishing row 22's card — verified live. Worker 17's later deploy succeeded because the quota
   had ALREADY been pruned, not because 429 is transient. **Do NOT conclude 429 clears on retry.**
   When the quota is genuinely full, retrying forever will not help: run the prune tool, then deploy.
   The prune is safe — hosting release versions are stale copies of a site fully reproducible from git.

---

## Row 24 — The Sower (Matthew 13) — realistic V2, 2026-08-02

**Spend ≈$4.82** (3 anchors $0.40 + 32 beats $4.29 + 1 reroll $0.13). Meter after: $110.95.
**Reroll rate 2.9% (1 of 35) — the lowest of the wave.** 35 pictures against V1's EIGHT;
167.6 s delivered, identical to V1 to the millisecond; AUDIO LOCK PASS (SHA256 e9a026c8…).
Git blob f3fc5125…

1. **V1's real defect was coverage.** `s6-good-harvest.jpeg` held the screen from 87.37 s to
   132.21 s — FORTY-FOUR SECONDS across four segments (j8, n9, j3, n10). That one still
   covered the whole good-ground half of the parable, including Jesus's own fifteen-second
   explanation in j3. `s3-wayside-birds.jpeg` held another 25 s across j4, n4 and n5.

2. **The inherited 25-beat map was DISCARDED, not re-timed** — it ran on a 140.8 s timeline
   against the real 167.5 s, adrift by nearly twenty-seven seconds by the end. Every window
   recomputed from the fixed `extract_beats.py` and split on each segment's own `timing.json`
   phrase boundaries: contiguous 0.28 s → 161.223 s, zero gaps, 4.60 s/picture, all 18
   segment speech-starts verified with silencedetect to fall inside the window written for
   them, and no segment left without a picture.

3. **SOURCING TRAP checked and CLEARED.** The live script and the `.pre-speaker` sibling DO
   disagree: the SPEAKER-LAW rebuild ADDED three segments the sibling has never heard of
   (s3 = the black-letter frame of Matt 13:3, j4 = Matt 13:4, j8 = Matt 13:8) and all three
   mp3s exist in `audio/`. Six segments (n1, n3, n8, n11, n12, card) were transcribed with
   faster-whisper and every one matches the LIVE script word for word. No `TEXT_OVERRIDES`.

4. **NEW SHARED LESSON — SEASON IS NOT ALWAYS A GLOBAL LOCK.** Row 23 established that a
   story revisiting one outdoor location across one day must pin the SEASON in the setting
   lock. Row 24 is the counter-case and refines the rule: this parable spans a whole growing
   season on ONE field, so a global season lock would be a lie. **The general rule for the
   library: pin the TERRAIN as the invariant and let each beat state its own GROWTH STAGE.**
   Here the `FIELD` lock fixes the positions of the beaten path, the limestone shelf, the
   thorn brake and the dark tilled corner and then says in as many words that the growth
   stage is stated separately by each scene and is the only thing that changes. Bare earth →
   green shoots → ripe gold barley → cut stubble all read as the same field.

5. **Anchor-first casting took the rate to 2.9%** — three face-showing anchors (the SOWER
   stepping through the field gate, the YOUNG MAN lit up with joy, the WOMAN at the moment
   she understands) generated in their OWN run, then wired into REFS. Every beat naming a
   locked person also restates that person positively in its own scene text.

6. **The single reroll, and why it was NOT a `--redo`.** b24 came back with a large
   out-of-focus CREAM shoulder and back filling the near foreground beside Jesus — a second,
   unlocked figure in cream, which the CAST-CLOSURE lock names as failing the picture. That
   is a COMPOSITION defect, and `--redo` would have attached the defective frame as a
   rough-draft ref and preserved it. Fixed by deleting the file and restating the near
   foreground POSITIVELY ("the camera floats low on the lake itself … nothing between it and
   the hull but a hand's depth of clear shallow water and the pale stony bottom … nobody
   stands, wades, kneels or passes between the camera and the boat"). One pass.

7. **STAGING checked across the library.** The frame story sits in the moored boat off a
   bright daylit shingle beach exactly where Matthew 13:1-2 puts it. Daylight and flat water
   separate it from row 11's night gale and row 19's dawn shore with the charcoal fire, and
   it repeats none of the Luke 15 teaching settings of rows 2, 8 and 21, row 16's lamplit
   interior, row 22's basalt doorstep or row 23's terraced hillside.

8. **Delivered and verified.** verify-mp4 OK 167.555 s / 21,681,837 bytes; captions checked
   on 17 rendered frames (white narrator, light-blue scripture on s3, red Jesus KJV, bottom
   band only, never over the art) and the closing card carries its words. Reviewer card
   repointed with a unique anchor, diffed to prove only row 24 moved (rows 12 and 17
   untouched), carries `data-review-wave="realistic-v2"`, deployed, and confirmed live with
   the raw GitHub URL serving the matching byte size. Firebase deployed first try — the
   quota pruned on 2026-08-02 is still holding.

---

## Row 25 — Wheat and Tares (Matthew 13) — realistic V2 rebuild

**Shipped 2026-08-02 (Machine A, Dev — Claude worker 19).** 33 pictures, ≈$4.69, reroll rate 5.7% (2 of 35).
Cut: `media-production-v2/build-25-wheat-and-tares/matthew-13_wheat-and-tares.mp4` (166.833 s / 21,494,181 bytes).

1. **THE NEW TRAP: A STALE V1 FINAL MP4, AND THE AUDIO LOCK COPIES IT BLIND.** Every prior row's
   sourcing trap was about the SCRIPT disagreeing with the audio. This one is about the finished
   V1 VIDEO disagreeing with the audio, which no earlier row had hit. Established from file
   metadata and transcripts, never from prose:
   - `matthew-13_wheat-and-tares.mp4` — rendered 2026-07-22 02:03, runs 229.033 s.
   - `audio-eleven.log` — the ElevenLabs re-voice ran 2026-07-23 04:26, i.e. AFTER the MP4. That
     MP4 therefore carries PRE-REDO-ALL voices and must never be shipped.
   - The echo-delete sweep re-cut the mp3s again 2026-07-29 09:47, DELETING `n1` and trimming one
     sentence out of `n9`. Both were genuine echoes: n1 repeats j24's own KJV line, and n9's
     "So let them both grow." repeats j1's "Let both grow together until the harvest."
   - faster-whisper on the MP4 puts n1 back on screen at 14-23 s. `n1.mp3` does not exist; only an
     orphan `n1.mp3.words.json` does. extract_beats already skips it as an echo-delete orphan.
   So the mp3 set is the current narration at 166.818 s and the MP4 is an older render at 229.033 s.
   `v2_assemble`'s ±1.0 s guard would have refused to build at all, and forcing it would have shipped
   the old voice, restored the deleted echoes and mistimed every caption by 60+ s.

2. **The fix is a SHARED opt-in, and V1 stays read-only.** `v2_assemble.py` now honours a
   build-declared `AUDIO_FROM_V1_SEGMENTS = True`. When set, the finished narration track is rendered
   from the V1 build's OWN mp3s, each delayed to exactly the `audio_start` extract_beats computes from
   that build's own constants, summed with `amix(normalize=0)`, padded to the full runtime and
   loudness-trimmed toward -15 LUFS — the same stage V1's `build.py` performs. Nothing is re-voiced,
   re-timed or gained per segment, and nothing is ever written into the V1 folder (hard protection #1).
   Rebuilding the V1 video instead was rejected: its `build.py` still lists the deleted `n1` in BEATS,
   so running it would have meant editing V1.
   **Whoever sweeps this next:** `AUDIO-AUDIT.md` already lists row 25 with a +64.37 s delta between
   the V1 final and the expected timeline and still marks it "clean" — "clean" there only means the
   mp3s are ElevenLabs. THE DELTA COLUMN IS THE REAL SIGNAL, and seven other rows carry one.

3. **Sourcing trap checked and cleared on the script side.** `make_narration.py.pre-echo` and
   `.pre-speaker` both disagree with the live script. `n9`, `s24`, `n2`, `n14` and `card` were
   transcribed with faster-whisper and every one matches the LIVE script word for word;
   `n9.timing.json` agrees. No `TEXT_OVERRIDES` were needed.

4. **Windows rebuilt from scratch.** The inherited 2026-07-29 map was discarded. Every window
   recomputed from the fixed extract_beats and split on each segment's own phrase timings, with no
   split falling mid-phrase: contiguous 0.280 s → 160.858 s, zero gaps, zero overlaps, 4.87 s/picture,
   longest hold 8.44 s. All 20 segment speech ONSETS were re-measured with silencedetect — leading
   silence included, not just the nominal `audio_start` — and every one lands inside the window written
   for it. No segment is left without a picture. This build computes `vdur = LEAD + audio_dur + gap`
   from the RAW mp3 duration and its `PEAK = {"j1"}` is already a Jesus segment, so extract's speaker
   test reproduces V1's `is_scripture(...) or name in PEAK` exactly.

5. **Anchor-first casting held the rate to 5.7% (2 of 35)** — three face-showing anchors (the farmer,
   the enemy, the head servant) generated in their own run, then wired into REFS. BOTH rerolls were on
   the anchors themselves and both were COMPOSITION-level, so both were fixed by delete-file + fresh
   generation, never `--redo`:
   - the ENEMY looked straight into the lens. Cured by the standing lens-gaze fix that has now held on
     eight rows: give the gaze a NAMED TARGET INSIDE THE FRAME (the seed falling from his own hand at
     the lower left) and move the camera side-on for a three-quarter profile.
   - the SERVANT had a large out-of-focus PALE shoulder filling the near left foreground — the exact
     row-24 defect, a second unlocked figure in cream. Cured by stating the near foreground POSITIVELY
     (standing crop and the top of the low wall, nobody between camera and subject).
   Both cures were then applied preventively to the other close beats, which is why the remaining 30
   came back clean in one pass.

6. **Continuity rule applied, not re-derived.** This parable spans a growing season, so the row-24 rule
   governs: pin the TERRAIN as the invariant (one dry-laid wall, one gap for the cart track, one lone
   carob tree, one limestone rise) and let each beat state only its own GROWTH STAGE. A DARNEL lock was
   added so the weed is genuinely indistinguishable before heading and unmistakable after — that
   distinction is the parable, and without it the servants' question makes no sense.

7. **STAGING checked across the library.** The frame story sits on a THRESHING FLOOR at the head of the
   grain plain in warm late-afternoon light — the one place in the story world that exists only because
   of harvest, which is what this parable is about. It repeats none of rows 2/8/21 (Luke 15), 16
   (lamplit interior), 22 (basalt doorstep), 23 (terraced hillside), 24 (moored boat off a beach), 11
   (night gale) or 19 (dawn shore with the charcoal fire).

8. **Delivered and verified.** verify-mp4 OK 166.833 s / 21,494,181 bytes; captions checked on 20
   rendered frames (white narrator, light-blue scripture on s24, red Jesus KJV, bottom band only, never
   over the art) and the closing card carries its words. Reviewer card repointed on a unique anchor and
   diffed to a three-line change proving only row 25 moved (rows 12 and 17 byte-identical), carries
   `data-review-wave="realistic-v2"`, deployed first try (no 429), and confirmed live with the raw
   GitHub URL serving the matching byte size.

---

## Session — 2026-08-02 · URGENT AUDIT: is stale V1 audio locked into any shipped V2 cut? · Claude worker 20

**Status: DONE. Result: all 23 shipped realistic-V2 rows are CLEAN. Zero rows rebuilt,
zero pictures generated, $0 spend.** Full measured table:
[`STALE-AUDIO-AUDIT.md`](./STALE-AUDIO-AUDIT.md).

### What was suspected

Row 25 proved the AUDIO LOCK copies the V1 MP4's AAC stream blind, and that a V1 MP4
can predate the 2026-07-23/24 ElevenLabs re-voice or the echo-delete sweep. The fear
was that other shipped cuts had quietly inherited pre-REDO-ALL voices, restored deleted
echoes, or a caption timeline a minute adrift — with `AUDIO-AUDIT.md` calling them
"clean" because it only ever tested the mp3s, never the MP4 those cuts were locked to.

### What was measured (artefacts only — no prose, no prior verdicts)

Per row: git CONTENT date of the V1 MP4 vs every mp3 the build actually places;
`ffprobe` durations of the V1 MP4, the summed `extract_beats` timeline and the shipped
V2 cut; `ffmpeg -f md5` of both audio streams to see whether the AUDIO LOCK was even
the path taken; sample rate of every placed mp3 (24 kHz = old edge-tts voice, 44.1 kHz
= ElevenLabs); `silencedetect` onsets against the beat offsets; and faster-whisper on
the TAIL beats of the four widest-delta rows, because drift accumulates and the tail is
where a stale track cannot hide.

### Findings

1. **0 STALE-AUDIO, 0 OLD-VOICE, 23 CLEAN.** Every placed mp3 in every shipped row is
   44.1 kHz ElevenLabs. Every shipped cut's onsets track its beat offsets with a median
   deviation of 0.04–0.10 s. Nothing needed fixing, so nothing was rebuilt.

2. **Rows 10, 13 and 25 are the only shipped rows whose V1 MP4 predates its own mp3s —
   and they are exactly the three whose V2 audio is NOT bit-identical to that MP4.**
   Each was caught at build time by the existing ±1.0 s runtime check (67.7 s vs
   294.3 s; 259.0 s vs 298.3 s; 229.0 s vs 166.8 s) and rebuilt from the V1 segment
   mp3s. Row 01 also differs from V1, for the separately documented Jesus-line denoise.

3. **MTIME IS WORTHLESS IN THIS REPO — do not audit with it.** Four machines clone and
   pull, so a checkout stamps a 2026-07-22 render as "2026-07-29 09:46". Every mp3 in
   the library shares one such timestamp. The commit that last changed a file's bytes
   is the only honest render date; mtime carries information only for untracked or
   dirty files. Any future audit that ranks renders by mtime will get this backwards.

4. **The defect is dormant, not absent: 54 V1 builds** have a finished MP4 older than
   at least one mp3 in their `audio/` folder. Any of them rebuilt through the AUDIO
   LOCK before today would have shipped a stale stream. Reproducible scan in
   `STALE-AUDIO-AUDIT.md`.

5. **Rows 12 and 17 — reported, not touched.** Both still sit on their V1 cut
   (`data-newvoice="1"`, not `realistic-v2`). Row 12 has an unshipped V2 cut on disk.
   Row 17's V1 final is genuinely **120.33 s short** of its own timeline (`n11` voiced
   and never placed) — a real outstanding defect, but not this defect.

### Shared-tool fix

`v2_assemble.py` gained `content_time()` and `assert_v1_final_is_current()`, called
before the AUDIO LOCK copies anything. Two independent tripwires:

- **Recency** — any PLACED mp3 newer than the V1 MP4 ⇒ refuse. This is the one that
  matters: a re-voice or a text trim that leaves the runtime almost unchanged is
  invisible to every duration check ever written.
- **Runtime excess** — V1 stream more than 0.75 s longer than the summed timeline ⇒
  refuse. Shortfalls keep the looser 1.0 s tolerance, because V1 finals routinely land
  a couple of tenths under the recomputed timeline through trailing-silence trimming.

Both errors name the fix: `AUDIO_FROM_V1_SEGMENTS = True`. V1 is never edited and
nothing is ever re-voiced. Verified against all 23 shipped rows — passes the 20 that
legitimately used the lock, blocks exactly 10, 13 and 25. Zero false positives.

### Lesson for the next worker

**A "clean" verdict is only clean for what it actually tested.** `AUDIO-AUDIT.md` swept
210 builds and said REDO-ALL was satisfied library-wide — true, and it still could not
have caught row 25, because it never looked at the MP4 the V2 cut was locked to. Its
own table listed row 25 with a `+64.37` delta and the word "clean" on the same line.
That file now carries a banner at the top saying exactly what it does and does not
prove. Write that banner on your own audits too.

---

## Row 26 — The Mustard Seed (Matthew 13:31-32 / Luke 13:19) — realistic V2, 2026-08-02
**Claude worker 21, Machine A `Dev`.** Commit `5cd6564105a4` (cut), card repointed in the
following commit. 24 pictures, 87.0 s, 20.3 MB. Spend **$4.15** (31 images at $0.134),
meter $115.642 → $119.80. Reroll rate **7/31 = 23%**.

### The inherited beat map was wrong, and this is how it was proved
`beats_v2.py` arrived with fourteen beats whose windows ran `audio_start` → `spoken_end`
instead of segment boundary to segment boundary. That leaves a DEAD GAP at every segment
join — 3.44→4.01, 8.93→9.47, 12.91→13.45, 17.91→18.47, 27.85→29.39, 40.07→41.52,
46.53→47.11, 54.31→54.84, 59.44→60.00, 63.16→63.65, 71.96→72.51, 79.15→79.42, twelve gaps
totalling ~5.9 s with no picture assigned at all. It also gave the whole of `j1` (9.4 s)
and the whole of `j1b` (10.7 s) one picture each, and staged the frame at the seaside,
which would have been the third row running on rows 24/25's beach and boat.

### WORD TIMINGS, not the timing sidecars — new, and it will recur
The row-25 rule was "split inside a segment on that segment's own `.timing.json` phrase
boundaries." On this row that rule cannot be followed: NINE of the twelve sidecars contain
exactly ONE phrase spanning the entire segment, so there is no interior boundary to split
on. Word-level timings from `faster_whisper` with `word_timestamps=True` are free, take
under a minute for a 87 s video, and put every split on a real comma or clause head.
**When a sidecar has one phrase and the segment is longer than ~5 s, transcribe for word
timings — do not fall back to splitting blind.**

### Audio
Clean. `matthew-13_mustard-seed.mp4` and every `audio/*.mp3` last changed bytes in the
SAME commit (git content date 2026-07-28 16:30:55), and the MP4 runs 87.067 s against the
summed timeline's 87.015 s — 0.052 s, far inside the 0.75 s tripwire. `n0 j1 j1b n5 n8 n9
card` were all transcribed and match the live `make_narration.py` word for word, so no
`TEXT_OVERRIDES` and `AUDIO_FROM_V1_SEGMENTS = False`. Normal packet-copy AUDIO LOCK PASS,
SHA256 `40826b7a8052…`.

### NEW SHARED LESSON — every new setting invents its own anachronism, and a garden's is IRRIGATION
Rows 16/18 paid for interior lighting, row 19 for boat fittings, row 22 for city skylines.
A walled kitchen garden's version is **modern black drip-irrigation hose**: thin dark
tubing lying along the beds, present in **4 of the first 24 frames** (b10, b11, b17, b21)
and invisible until you crop in. Nothing in the existing PERIOD-MATERIALS lock covers it,
because it is not a lamp, a fitting or a garment — it is a LINE ON THE GROUND.
The cure, stated POSITIVELY per the row-10 geometry lesson, went into this build's GARDEN
lock and killed it in ONE pass on all four:

> HAND-IRRIGATION LOCK: ALL the water in this garden moves by hand and by gravity alone.
> The ONLY things that carry water are shallow open channels scraped into the bare earth
> between the beds, the stone-lined cistern, and fired-clay jars carried by hand. Along
> every bed and every path the ground is BARE SOIL, unbroken, with nothing lying on it or
> running across it. There is NO tube, hose, pipe, line, cord, wire, cable, tape, stake or
> fitting of any kind lying along or across any bed, path or channel, in focus or out of
> focus, in the foreground or the background; nothing black, dark grey or glossy runs in a
> straight line anywhere on the ground; and there is no drip irrigation, no sprinkler, no
> spigot, no valve and no pump anywhere in the picture.

**Whoever stages the next garden, orchard, vineyard or irrigated field: paste that block
in before the first paid image.** It generalises to any cultivated ground.

### The other three rerolls
* **b01** — lens gaze, the classic. Jesus AND four listeners had their pupils on the lens.
  Fixed by the eight-for-eight cure: put the camera SIDE-ON to the whole group so the
  entire conversation runs horizontally across frame, Jesus at one edge and the listeners
  at the other, every eyeline exiting through a named side edge.
* **b06** — the row-24/row-25 defect again: the out-of-focus near-foreground listener came
  back in pale grey-taupe. Naming the head cloth indigo was not enough; what worked was
  "his ENTIRE back, shoulder, sleeve and head cloth are DEEP INDIGO — a single dark navy
  mass … with NOTHING pale, grey, beige, taupe, cream or off-white anywhere on him."
* **b11** — the model ignored the beat entirely and returned a hand pressing a seed into
  soil (a composition from earlier in the same build). Fixed by leading `must_show` with
  "THE SUBJECT OF THIS PICTURE IS BIRDS IN FLIGHT" and adding to `must_not_show`: "no
  seed, no planting, no ground-level macro of any kind — the camera is looking UP at the
  sky, not down at the earth." **When a render comes back as a DIFFERENT beat from the
  same build, the fix is to name the subject first and forbid the other beat's geometry.**

### Staging
A small walled kitchen garden on the edge of a village — mud-brick walls just above head
height, narrow raised beds, hand-cut watering channels, a stone-lined cistern, a plank
gate. Luke 13:19 ("cast into his garden") is the warrant and V1's own narration says "the
largest plant in the whole garden," so the audio itself asks for it. Enclosed and
human-scale, the visual opposite of row 25's grain plain and row 24's beach. **The mustard
grows in the SAME corner bed in every frame**, so the teaching and the parable share one
continuous place and the closing wide shot puts Jesus and the grown plant in one picture
without inventing anything. Terrain is the invariant; only growth stage and light move.

---

## ROW 27 — THE LEAVEN (Matthew 13:33), realistic V2 — shipped 2026-08-02 (Claude worker 19)

29 pictures at native 2K against V1's EIGHT. 104.47 s / 20.3 MB. Reroll rate **27.6 % (8 of 29)**.
Spend ≈ **$5.09**. AUDIO LOCK PASS, SHA256 `3c20c13a…`.

### The timing trap on this row: BOTH sidecar sources are unusable
`.timing.json` carries ONE phrase spanning the whole segment for n1, s33, j1 and n4 — four of the
ten story segments — so it cannot supply an interior split at all. And the `.mp3.words.json` files
that already sit in the V1 `audio/` folder are **wrong**: n1's last word ends at 8.52 s inside a
6.295 s file, j1's at 8.92 s inside an 8.072 s file, at *different* ratios, so they are not a
rescalable artefact of the real audio either. Every window came from faster-whisper
`word_timestamps=True` run on the mp3s themselves. **Do not trust a build's `.mp3.words.json`
without checking its last word against the file duration first — it costs one ffprobe.**

### NEW SHARED LESSON — a tight shot's anachronism is the FABRIC, and a macro's is the WHOLE ROOM
Rows 16/18 paid for interior lighting, 19 for boat fittings, 22 for city skylines, 26 for garden
irrigation. This row's family was different because half its pictures are macro:

* **Two sleeves came back as MODERN KNITWEAR** — b12 as a ribbed sweater cuff, b23 as brushed polar
  fleece. `GARMENT-CONSTRUCTION` forbids modern *shapes* (collars, plackets, cuffs) but said nothing
  about how the cloth is *made*, so a correctly-shaped indigo sleeve rendered in jersey knit passed
  every check. Cure, now a **shared `WOVEN-CLOTH LOCK` in `v2_prompt.py`**:

  > every piece of cloth in the frame is WOVEN ON A LOOM and shows it — a visible over-and-under grid
  > of warp and weft threads, slightly irregular, with a flat matte surface. NO CLOTH IS KNITTED OR
  > MACHINE-MADE: no knit stitch, purl, rib, cable, jersey, seed stitch, stretchy cuff or collar band,
  > no felted, fleeced, brushed, napped or looped pile, and no sweater, jumper or sweatshirt texture
  > anywhere, including at a rolled sleeve, a wrist, a hem or a blurred edge. A close macro shot of a
  > sleeve must still read as coarse hand-woven wool or linen, never as knitwear.

  It fixed b12 in one pass. b23 needed a second pass and is the sharper lesson: on an extreme macro
  where the cloth fills a third of the frame, the shared lock alone was not enough — the beat text
  had to restate the sleeve itself as coarse flat hand-woven wool with a frayed cut edge.
* **Two macro food shots came back as PRESENT-DAY PHOTOGRAPHY** — b14 as a smartphone snapshot of a
  proving basket on a garden deck with a white railing, b25 as studio food photography of artisan
  boules on a bamboo mat against a bright white kitchen. Nothing in the frame was a "prop" the locks
  could catch; the whole *room* was modern. The cure is to state where the camera is standing in the
  world, not just what it is pointed at: **"THE WHOLE PICTURE IS OUTDOORS INSIDE THE FIRST-CENTURY
  BAKING YARD, ON BARE SWEPT EARTH BESIDE A ROUGH TAN MUD-BRICK WALL"**, plus a tilt that puts a band
  of that earth and wall in frame so the model has to render it. Both fixed in one pass.
  **Whoever shoots the next tight macro: an object lock protects the object, not the room. Say where
  the camera is standing.**

### The other four
* **b04** — lens gaze on the KJV wide, the classic. Fixed by the eight-for-eight cure: camera fully
  SIDE-ON to the group so the whole conversation runs horizontally, Jesus at one edge in clean profile
  and the listeners at the other, every eyeline exiting through a named side edge.
* **b06** — the rows 24/25/26 defect again: the out-of-focus near-foreground listener beside Jesus in
  cream. Naming a garment was not enough; what worked was pinning the ENTIRE figure — "back, shoulder,
  arm, sleeve, lap, knee and head cloth are DEEP INDIGO, ONE SINGLE UNBROKEN DARK NAVY MASS".
* **b11** — a corrugated SHEET-METAL roof edge above the yard wall, invisible until you crop the top
  right corner. `PERIOD-MATERIALS` forbids sheet metal but the skyline is where it hides. Cure stated
  positively: "ABOVE THE WALLS THERE IS NOTHING BUT OPEN SKY AND THE ROUNDED WEATHERED TOP OF THE MUD
  BRICK ITSELF".
* **b27** — two large WHITE woven-plastic feed sacks behind the oven. Cure: every sack in the picture,
  sharp or blurred, near or far, is coarse dark brown-black goat-hair cloth tied with flax cord.

### Also promoted this session
The **HAND-IRRIGATION LOCK** row 26 left "ready to paste" in this ledger is now a named shared SETTING
lock in `v2_prompt.py` (`SHARED_SETTING_LOCKS`), opted into by naming `HAND-IRRIGATION` in a beat's
`locks` list. It is not appended to every prompt — a boat scene has no irrigation — but the next
garden, orchard, vineyard or irrigated field no longer has to re-learn it.

### Staging
Two places, neither used by any other row. THE FRAME: the long stone bench built along the sunlit
outer wall of a village synagogue, flat bright mid-afternoon, listeners on the bench and the worn
steps — Matthew 13:33 opens "ANOTHER parable spake he unto them", so he is mid-sequence with a settled
audience, which the bench gives without borrowing row 24's boat for a fourth consecutive row (the
inherited scaffold wanted exactly that and called it "the sixth composition"). THE STORY: a small
walled baking yard — a beehive clay oven, a hollowed olive-wood kneading trough on a stone stand,
goat-hair meal sacks, a covered clay starter jar. **The clock is the plot and it is on the screen**,
because the parable is about hidden time passing: low afternoon sun as she mixes, dusk as she covers
the trough, full night lit by one clay lamp with nothing happening, first grey dawn with the cloth
domed from beneath, then bright morning as she bakes and hands the loaves out at her gate.


---

## ROW 28 — HIDDEN TREASURE (Matthew 13:44), realistic V2 — shipped 2026-08-02 (Claude worker 22)

29 pictures at native 2K against V1's SEVEN. 98.8 s, 20.9 MB, AUDIO LOCK PASS
byte-identical (SHA256 e11dfb5a…). Reroll rate **25.6% (10 of 39)**, ≈$5.22.
Commit `42b855efe`. Live on the reviewer, raw URL serving 20,879,508 bytes.

### What V1 was
Seven stills for ninety seconds. `s7.jpeg` held from 67.75 s to 90.36 s — twenty-two
and a half seconds across n9, n10 AND n11, which is the ENTIRE application of the
parable: "once you truly see who Jesus is, nothing else even compares" and the whole
closing turn about joy, on one picture. `s5.jpeg` held 12.9 s, `s6.jpeg` held 11.8 s.

### The inherited scaffold was discarded, and this is why
Measured, not assumed. (1) It planned 16 pictures at 5.6 s each and called that "the
library density" — rows 24-27 shipped at 3.1-4.9 s/picture. (2) It staged the frame in
a HOUSE INTERIOR off Matthew 13:36, arguing row 25 had used a wide interior so a close
one was "no repeat". Row 16 is already the wave's lamplit interior and the frame beats
recur FIVE times across this video; a second interior is the repeat, not the cure.
(3) Its TREASURE lock described "a small iron-banded wooden chest, its lid split with
age" — a hinged, iron-banded strongbox is mediaeval and breaks the shared
PERIOD-MATERIALS lock outright (no machined fitting, no hinge). A first-century Judean
hoard is a sealed fired-clay jar in the ground, which is also what makes the parable's
own law work: the find belonged to the OWNER OF THE LAND, which is precisely why a
labourer buys the ground rather than pocketing the pot.

### Audio and timing
Every `audio/*.mp3` and the V1 MP4 last changed bytes at ONE commit
(2026-07-27T22:44:25 git CONTENT date), so neither of `assert_v1_final_is_current()`'s
tripwires had anything to refuse and the packet-copy AUDIO LOCK applied.
SOURCING TRAP CHECKED AND CLEARED: all FIFTEEN segments transcribed with faster-whisper
match the LIVE `make_narration.py` word for word, and the `.pre-speaker` sibling differs
only in its docstring and voice constants — no `TEXT_OVERRIDES`. Note whisper put a
hallucinated repeat of n2's own first clause on its tail after the real speech ends at
13.71 s; the mp3 is fine, the transcript is not, and that is worth expecting.
Windows recomputed from `extract_beats` and split on measured WORD timings — the
`.timing.json` sidecars were not trusted and this row carries no `.mp3.words.json` at
all. Contiguous 0.280 s → 90.360 s, zero gaps, zero overlaps, 3.11 s/picture, shortest
1.46 s, longest 5.27 s; all 14 speech onsets re-measured with silencedetect and verified
inside their own segment's window, with no segment left without a picture.

### Staging — three places, none used anywhere in the wave
* **OLIVE GROVE** (frame). Matthew 13:36 has him leave the crowd and speak to the
  disciples alone, and 13:44 opens "AGAIN", so this is a small closed circle
  mid-sequence. Ancient trunks, knuckled roots as seats, silver-green canopy breaking
  the light into DAPPLE. No other row in the wave has a canopy or dappled light.
* **A SMALL ENCLOSED STONY FIELD** on a narrow valley floor, walled on all four sides,
  a white chalk bank, one dead terebinth stump, one tumbled gap in the near wall.
  Deliberately NOT row 25's open plain and NOT rows 24/26's crop ground: rough fallow
  is why a landowner hires a man to swing a mattock at it, and the walls are why it is
  one saleable parcel a poor man could buy.
* **A POOR MUD-BRICK DOORYARD** on a dirt slope — distinct from row 22's dressed BLACK
  BASALT doorstep and paved street in material, colour and scale.
TERRAIN IS THE INVARIANT: walls, gap, chalk bank, stump and ridge house never move;
only the light and the state of the dug ground change. The clock only runs forward —
hard midday for the digging, low late afternoon for the selling, clean early morning
for the buying, flat overcast for the "ordinary field", bright morning for the joy.

### NEW SHARED LESSON — a working scene's anachronism is THE TOOL IN THE HAND
Rows 16/18 paid for interior lighting, 19 for boat fittings, 22 for city skylines, 26
for irrigation hose, 27 for knitted fabric. This row's hinge is "his spade struck
something hard", and PERIOD-MATERIALS does NOT reach it: it says tools are "hand-forged
iron or bronze showing hammer marks", which a modern steel garden spade with a D-handle
and a foot tread satisfies perfectly while still being an object from a garden centre.
It is also the largest and sharpest thing in a digging frame. Promoted to a named shared
setting lock, **HAND-TOOLS**, in `v2_prompt.py` SHARED_SETTING_LOCKS, opt-in by name for
any build where somebody digs, chops, reaps, hoes or carries.

### The ten rerolls, and what actually fixed each
1-3. **Both anchors, lens gaze.** Giving the gaze a NAMED TARGET INSIDE THE FRAME — the
   cure that had not failed in ten rows — was NOT enough here on a near-frontal portrait.
   What fixed it was moving the camera fully SIDE-ON *and* turning the HEAD off the
   camera axis explicitly: "his face is seen in clean three-quarter profile, the line of
   his nose pointing toward the RIGHT EDGE, so the camera sees his cheek, his jaw and
   the outer corner of his far eye rather than the front of his face." Worth porting.
4. **Owner in a waffle-knit henley with a button placket**, and **no head cloth**, and a
   **THIRD HAND** lying on the wall with no arm. Fixed with a positive hand inventory
   ("EXACTLY TWO HANDS ARE VISIBLE ANYWHERE IN THIS PICTURE… each arm visibly joined to
   its shoulder"), a restated head covering, and a plain-slit neck clause.
5-7. **PALE CLOTH ON NON-JESUS FIGURES — AND THE LEAK WAS THE SCARF, NOT THE TUNIC.**
   The DISCIPLES lock pinned every tunic to a dark colour and the model obediently
   draped CREAM AND BUFF STOLES round their necks instead, in three frames sitting
   beside Jesus. A garment-colour lock that does not enumerate accessories leaves the
   accessory free. Cured by naming EVERY SEPARATE PIECE of cloth — "tunic, sleeves,
   sash, head cloth, and ANY scarf, stole, shawl, wrap or mantle draped round a neck or
   over a shoulder" — as a dark saturated colour. **Port this into any lock that pins a
   group's clothing.**
8. **A wide beat collapsed into a portrait** and grew a pale foreground mass. Fixed by
   restating the wideness as a countable fact ("the camera far enough back that Jesus
   AND at least six seated disciples are all in the frame, head to sandals; Jesus
   occupies only a modest part of the picture and is never framed from the chest up").
9. **Identity drift on a tight two-shot** plus a roof edge on the skyline. Fixed with
   "the SAME man as the attached reference photograph — the identical face" and tilting
   the camera DOWN so the mud-brick wall fills the background edge to edge, which
   removes the skyline as a place for an anachronism to live (the row-27 lesson).
10. **A broad bright sheet-steel cleaver blade** that survived TWO explicit prohibitions
   naming it. It died only when the OBJECT'S GEOMETRY was changed rather than its
   description: the tool turned EDGE-ON to the camera so its iron reads as a narrow dark
   line and no flat face of metal is ever presented. **When a prohibition fails twice,
   stop describing the object and re-stage it.**

### ⚠️ A SHARED-LOCK REFINEMENT THE NEXT WORKER SHOULD MAKE
Two of the ten rerolls were spent fighting a coin, and they should not have been.
PERIOD-MATERIALS says "no writing, lettering or numerals on any object" — and for a
first-century COIN that is simply wrong. A denarius of that century legitimately carries
a rim legend and an emperor's portrait head, and Jesus himself points at one and asks
"Whose is this image and superscription?" (Matthew 22:20). The generator was returning
the historically CORRECT object and the beat kept rejecting it. Carve out an explicit
coin exception in PERIOD-MATERIALS rather than re-learning this. (The final s25 keeps
the legend and the head, and it is right.)

## Row 29 — The Pearl of Great Price (Matthew 13:45-46) — Claude worker 23, Machine A `Dev`, 2026-08-02

✅ **SHIPPED 2026-08-02.** Commits `77e1bcfa0` (build) and `d9d877430` (card).
36 pictures at native 2K over 108.99 s of story = **3.03 s/picture**, against V1's
SIX. V1's `s1-merchant.jpeg` covered n1, j1 AND n2 (0.28→19.36 s); `s4-sells-all`
covered n5, j2 AND n6 (22.6 s); `s5-buys-it` covered n7 and n8 (24.5 s); and
`s6-pearl-radiant` covered n9 AND n10 — 85.48→109.27, **23.5 seconds, the entire
closing turn the video exists to deliver**, on one held frame.

**THE INHERITED SCAFFOLD WAS DISCARDED** (saved to scratch first), for reasons
measured rather than assumed: 18 pictures at 5.8 s each called "library density"
when rows 24-28 shipped at 3.1-4.9; the frame staged in a HOUSE INTERIOR, which
row 16 owns and row 28 had already examined and rejected on this exact argument,
with the frame beats recurring ELEVEN times here; "each searching beat may pick
its own hour", discarding the clock rows 23-28 proved is the wave's strongest
tool; a MERCHANT lock that made gold rings a deliberate VARIABLE, the exact drift
a lock exists to prevent; and a PEARL lock reading "flawless, perfectly round",
which is a machined CGI sphere.

**AUDIO** — LOCK PASS, byte-identical, SHA256 `f240ba9f…`, 115.8 s / 21,451,026 B.
The V1 MP4 and every mp3 share ONE git content date (2026-07-27T22:46:55), so
neither staleness tripwire fired. SOURCING TRAP CLEARED: all 13 segments
transcribed with faster-whisper against the LIVE `make_narration.py`. Two apparent
mismatches were chased and are **whisper's, not the audio's** — it renders the KJV
"like unto" as "likened to" in j1 on BOTH base.en and small.en, and contracts
"here is"→"here's" in n7. The CARD was re-run on small.en because base.en gave
"you ARE the pearl" against the script's "you WERE the pearl"; small.en returns
the script exactly. **No TEXT_OVERRIDES; `AUDIO_FROM_V1_SEGMENTS` stayed off.**

**WINDOWS** recomputed from `extract_beats` and split on word timings measured
from each mp3 (sidecars not trusted; this build has no `.mp3.words.json`).
Segment-boundary contiguous 0.280 → 109.270 s, zero gaps, zero overlaps, shortest
1.36 s, longest 4.74 s. All 13 segment onsets and the intra-segment splits
re-measured with silencedetect and verified inside their own windows.

**STAGING — four places, none used in the wave.** A BARE LIMESTONE SHELF above a
dry wadi for the frame (open rock, no tree, no canopy, no wall — deliberately the
opposite of row 28's olive grove, which is *defined* by canopy and dapple); a
CARAVAN ROAD; a stone-flagged QUAYSIDE MARKET; and the merchant's own DRESSED-
LIMESTONE COURTYARD. That last was checked deliberately against row 28, which also
has a man selling everything: 28's is a POOR MUD-BRICK hut on a dirt slope with a
thorn pen and a village crowd; this is a PROSPEROUS DRESSED-STONE town house being
STRIPPED — different material, class, and emotional direction (28 gains, 29
empties). The clock carries the argument: hard white midday on the road, cold blue
first light for the years of searching, bright morning for the finding, hard noon
for the selling and the stripping, and the first warm gold of dawn for the
gladness. The n9/n10 turn stays inside the frame story and "his own life, gladly"
is carried by Jesus's **upturned empty palms**, never by any depiction of the cross.

**REROLL RATE 14.3% (6 of 42), ≈$5.63.** Two were the anchors; four were beats.

> ⚠️ **THE SHARPEST LESSON HERE IS A TOOLING ONE AND IT COST AN IMAGE.** After
> editing the ring out of the prompts I verified with `grep "iron ring"`, got
> ZERO, and believed it. The phrase was **split across a Python line break**
> (`"…dark iron "` / `"ring on…"`), so one beat kept the text and rendered a
> glossy machined black band. **Never verify a prompt-text edit with a grep for a
> multi-word phrase in a file of wrapped string literals — grep the distinctive
> SINGLE word, or assemble the prompt and search the assembled output.**

Other defect families and their cures, all by delete-file + fresh generation,
never `--redo`:
  * **The ring** — cured by DELETING the object from the MERCHANT lock and stating
    the hands are BARE, per the row-28 rule that a twice-failed prohibition must be
    re-staged rather than restated.
  * **Pale canvas awnings and pale-clad background figures** in the market — cured
    in the MARKET lock by pinning every awning to VERY DARK BROWN-BLACK goat hair
    and every person in the market to dark saturated colour.
  * **The merchant rendering BARE-HEADED** in two frames although the head cloth
    was named — cured by making the head cloth *do something in the composition*
    (its long loose end hanging down over the shoulder), so it cannot be dropped.
  * **Painted blue-and-white boat hulls** in the harbour — cured by RE-STAGING: the
    MARKET lock now states the sea is empty to the horizon, and the beat turns the
    camera inland so no water is in the frame at all.
  * **Pitched terracotta tile roofs** on the skyline above the courtyard — cured by
    tilting the camera down so there is no skyline in the frame to put a roof on.

**TWO NEW SHARED SETTING LOCKS** promoted into `v2_prompt.py`:
  * **ANCIENT-ROAD** — a road's own anachronism is THE SURFACE AND WHAT LINES IT
    (tarmac, kerbs, painted lines, tyre ruts, poles, wire, guardrails, signposts).
    PERIOD-MATERIALS cannot reach it, because a road surface is not an *object* —
    it is the ground. Roads recur constantly across the 200 (rows 09 and 20 both
    live on one), so this belongs in the shared file, not a ninth build-local copy.
  * **MARKET-TOWN** — a market's own anachronism is THE STALL (trestles, metal
    poles, striped or printed awnings, plastic crates, price boards), with row 22's
    city-skyline lesson (minaret, bell tower, tiled roof) folded in so no future
    town has to re-learn it.

Captions verified on extracted frames — red Jesus KJV on j1/j2, white narrator,
bottom band only, never over the art; the closing card carries its words. LIVE on
the reviewer with `data-review-wave="realistic-v2"`, raw URL serving 21,451,026
bytes, matching the local file exactly.

## Row 30 — The Net / Dragnet (Matthew 13:47-50) — Claude worker 24, Machine A `Dev`, 2026-08-02

✅ **SHIPPED 2026-08-02.** V1 `matthew-13_the-net.mp4` runs 154.933 s
on SEVEN stills (`s1-cast` … `s6-shore-close`) for 17 narration segments — n1, j1
(13:47), n2-n4, j48 (13:48), n5-n7, j2 (13:49), j50 (13:50), n8-n11, card. Full
realistic V2 rebuild in progress: audio locked, windows recomputed from
`extract_beats` and measured word timings, anchor-first casting, staged so it repeats
no setting already used in the wave.

40 pictures rebuilt at native 2K against V1's SIX PLACED stills (a seventh, `s5b-cast-away.jpeg`, sits in assets/ and was never on the timeline at all). V1's holds were the worst in the wave so far: `s5-cast-bad.jpeg` covered n7, j2, j50 AND n8 — 79.991 s to 115.780 s, THIRTY-FIVE AND THREE QUARTER SECONDS on ONE picture, i.e. the entire end-of-the-world turn including both red-letter verses AND the “the angels do it, God does it, it was never handed to us” line the whole passage aims at; `s6-shore-close.jpeg` covered n9, n10 AND n11 — THIRTY-ONE AND NINE-TENTHS SECONDS, the ENTIRE closing application, “it was cast for you”, the reason the video exists; `s1-cast.jpeg` covered n1, j1 and n2 (TWENTY-THREE AND A HALF). THE INHERITED SCAFFOLD WAS DISCARDED for measured reasons: it planned 25 pictures at 5.7 s each and called that the library density (rows 24-29 shipped at 3.1-4.9), and it staged the frame in a HOUSE INTERIOR arguing from Matthew 13:36 — row 16 already owns this wave's interior and rows 28 and 29 each examined and rejected that exact argument; the frame beats recur NINE times here. AUDIO LOCK PASS byte-identical (SHA256 9c6b79ce…), 154.9 s / 21,515,856 bytes — the V1 MP4 and all sixteen mp3s share ONE git content date (2026-07-27T22:50:25), so neither staleness tripwire fired. SOURCING TRAP CHECKED AND CLEARED: all SIXTEEN segments transcribed with faster-whisper match the LIVE make_narration.py word for word; three apparent differences are whisper's and all one family, a dropped final consonant (fishermen→fisherman, the bad away→the bat away, the angels→the angel), so no TEXT_OVERRIDES. WINDOWS REBUILT FROM SCRATCH from extract_beats and split on measured word timings — every one of the sixteen `.timing.json` sidecars holds exactly ONE phrase spanning its whole segment and could not have supplied an interior split at all. Contiguous 0.280 → 147.672 s, zero gaps, zero overlaps, shortest 2.10 s, longest 4.97 s, 3.68 s/picture, every segment has its own pictures and every speech onset was re-measured with silencedetect against the finished V1 MP4 and lands inside its window. STAGING — three places, none used anywhere in the wave, and rows 11 and 24 were checked deliberately because this is the wave's other water story: a low BOULDER BREAKWATER running out from a harbour with water on THREE sides for the frame (not a beach, not a boat, not dry rock); OPEN DEEP WATER with TWO boats and a dragnet strung between them (row 11 is one boat at night in a gale, row 24 one boat moored off shingle); and a flat SAND-AND-MUD STRAND at a stream mouth with reed beds (not row 19's stony beach, not row 24's shingle). The clock is the plot: the parable runs one working day, bright morning → high midday → gold afternoon → grave blue dusk, and the closing grace beats deliberately RETURN to the morning water; the nine frame beats never leave bright early afternoon. THE ANGELS, HEAVEN AND HELL ARE NOT PAINTED (row-21 precedent): v49/v50 stay inside the parable's own fish-and-shore imagery and the furnace is the set-aside catch carried away at dusk toward one SMALL DISTANT shore fire, thin smoke, no close flames and no creature or person in fire. REROLL RATE 1 of 41 = 2.4%, the lowest in the wave. The single defect was Jesus looking straight into the lens on s23, and describing the prohibition again was not the cure — RE-STAGING was: the beat was rewritten as a STRICT SIDE-ON PROFILE with the far cheek and far eye hidden behind his own head, which makes a lens gaze geometrically impossible, and it came back right in ONE pass. ≈$5.36 spend (41 images). No new shared lock was needed: the net and boat anachronisms are already reached by PERIOD-MATERIALS (row 19), and the row's own traps — the fisherman's undyed homespun tunic reading as a second Jesus, and “every kind” inviting an aquarium — were handled with build-local NET, CATCH and per-figure cloth-enumeration locks. Prior approval is VOID under REDO-ALL; LIVE on the reviewer, verified with `data-review-wave="realistic-v2"` and the raw URL serving 21,515,856 bytes.
