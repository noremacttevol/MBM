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

Claimed before any spend. Audio LOCKED (reused unchanged, never re-voiced). Every
picture rebuilt at native 2K to the realistic standard; every window re-timed from
the fixed `extract_beats.py`. Spend and lessons appended below as the row proceeds.
