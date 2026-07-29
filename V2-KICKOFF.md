# V2-KICKOFF — Full V2 picture production, one machine, starting at row 1

> **Cameron's order (2026-07-28): V2 production is GO.** Work through THE-200 in row
> order starting at #1 and DO NOT STOP between videos — finish one, log it, start the
> next, until Cameron messages you or the session runs out of room. This file is the
> complete job spec and it is RE-RUNNABLE: a fresh session pointed at this file resumes
> exactly where the ledger says the last one stopped. Standing Laws A–F in
> PRODUCTION-BIBLE.md §0 apply (announce Chrome bursts, never ask permission you already
> have, run to completion). Any message from Cameron stops the browser instantly.

## What V2 is (read first, once)

Every picture in all 200 videos is being replaced. The stories, the ElevenLabs
narration audio, the timing, and the caption text are PRESERVED. The pictures, the
old painted style, and the old Jesus depiction are RETIRED for V2.

**For V2 builds ONLY, Cameron's V2 order SUPERSEDES these V1 laws:**
- The painted "hand-painted 2D animation / Not photorealistic" Master Style Block → replaced by STYLE-V2 below.
- JESUS LOCK v3 (brown eyes, painted) and jesus_face_gate.py v3 → replaced by JESUS LOCK v4 below. Do NOT run the v3 gate on V2 prompt sheets; enforce the v4 checklist below instead.
- Everything else still binds: two-voice, story-coverage (one picture per beat), caption law (bottom band, synced splits), no music bed, content-care flags, action-logic, time-of-day, anatomy counts, only-Jesus-cream, no halo/glow, scripture-named files, ministry gate.

**HARD PROTECTIONS — never violate:**
1. **V1 is read-only.** Never modify, delete, move, or overwrite ANYTHING in `media-production/build-*`. You READ from V1 (audio, timing, scripts, beat maps); you WRITE only inside `media-production-v2/`.
2. **The app, site/, firebase — untouched.** Nothing deploys. Nothing replaces a live video. Cameron approves V2 cuts later, per video.
3. **Git:** `git add` ONLY small text files (ledger, prompt sheets, MINISTRY-GATE, build scripts). NEVER add images/audio/mp4s from media-production-v2 (put `*.jpeg`, `*.jpg`, `*.png`, `*.mp4`, `*.mp3` in `media-production-v2/.gitignore` first thing). Commit locally with clear messages. Try `git push` at most ONCE per video with a 2-minute timeout; if it fails or hangs, note "push skipped" in the ledger and move on — this machine's push is known-broken until a separate repair (12.7 GB backlog). Never retry pushes in a loop.
4. **MONEY IS NOT A CONSTRAINT (Cameron, 2026-07-28 — this REVERSED the old "paid
   Gemini API is BANNED" line).** His words: *"ignore the money law… I already paid for
   it… there shouldn't be any limitations on the money. Make it how it's supposed to
   be."* Never refuse a model, a tier, or a resolution to save money. Flow via
   `media-production/flow_driver.py` is still the proven path and stays the default
   because it works, not because it is cheap. A paid API additionally needs a KEY from
   Cameron — that is a missing credential, not a budget rule. See FACTORY-ORDERS.md
   MONEY RULE #1.

## STYLE-V2 — the V2 master style block (byte-identical opener of EVERY image prompt)

```
Cinematic biblical realism: a lifelike scene from first-century Judea, like a still
frame from a reverent, masterfully photographed biblical film. Natural cinematic
lighting, true depth of field, real physical scale. Realistic faces, eyes, hands and
anatomy; real fabric weave, wood grain, stone, dust and skin texture. Historically
credible clothing of rough-woven wool and linen in earth tones; authentic
architecture and landscape. Emotionally warm, reverent, and spiritually serious.
Not cartoon, not comic, not anime, not plastic CGI, not a painted illustration, not
a copy of any painting or artist's style. No text, captions, borders, panels,
watermarks, or modern objects anywhere in the image.
```

(9:16 vertical is set in Flow, not in the prompt text. Add nothing to this block;
scene content comes after it.)

## JESUS LOCK v4 — paste byte-identical into every prompt where Jesus appears

```
JESUS LOCK v4: the SAME man as the attached JESUS-V2-REF image — identical face,
hair and beard in every picture: a Middle Eastern Jewish man of about thirty-three,
warm olive-brown skin, strong kind weathered features, shoulder-length dark
brown-black wavy hair, a full dark beard, striking natural GREEN eyes, one plain
undyed off-white cream wool robe with a simple mantle and cloth sash (only he wears
cream), leather sandals. No halo, no glow, no rim-light. Never Caucasian, never
pale, never blue-eyed, never blond.
```

Plus, in every Jesus shot: `REF: media-production-v2/JESUS-V2-REF/jesus-v2-face.jpeg`
attached via `--ref`. In every WIDE or multi-figure shot with a ref attached, the
prompt MUST open (after STYLE-V2) with the forced-wide defense line: "WIDE
FULL-LENGTH SCENE with MULTIPLE PEOPLE — never a portrait, never a close-up of one
face; the camera far enough back that the named figures are visible head to sandals."
(The ref-echo failure is documented in FLOW-BUILD-PLAYBOOK.md — a ref can make the
model copy the portrait instead of composing the scene. QC's first question on any
ref-attached still: did it compose the scene or copy the ref?)

Other characters: dress them in earth colors, NEVER cream/off-white; state their
colors positively in every prompt where Jesus appears. Recurring cast wardrobe
colors come from CAST-REF/CAST-BIBLE.md (it wins over CHARACTER-LAW.md where they
disagree). V2 cast reference images do not exist yet — hold cast consistency
within each video by locking each character's description text (hairline, hair,
beard, age, build, garment: length, sleeves, fastening) byte-identical across all
of that video's prompts.

## ONE-TIME BOOTSTRAP — COMPLETE 2026-07-28 (face APPROVED by Cameron; never regenerate it) (only if media-production-v2/ does not exist yet)

1. `python3 media-production/flow_driver.py check` — must print logged_in. If not,
   STOP and tell Cameron in one line; do no browser retries beyond two.
2. Create `media-production-v2/` with the .gitignore described above, plus
   `PRODUCTION-LEDGER.md` (header + session table) and `JESUS-V2-REF/`.
3. **Jesus V2 face:** generate THREE candidate front bust portraits (Flow, model
   **Nano Banana Pro** — spend the credits; this face carries 200 videos): prompt =
   STYLE-V2 + the v4 identity text (no ref). Compare at full res: realism, warmth,
   green-eye impact, historical plausibility, zero resemblance to any known painting.
   Pick the best ONE → save as `JESUS-V2-REF/jesus-v2-face.jpeg` (keep the two
   losers as candidates-2/3 for Cameron). Then, attaching the winner as --ref,
   generate: three-quarter, profile, and full-body standing → save alongside.
   Record in the ledger: "JESUS V2 FACE = CANDIDATE, locked for this run, pending
   Cameron's approval of video #1."
4. Ledger note the bootstrap wall-time and every credit figure flow_driver prints.

## PER-VIDEO LOOP (repeat for row = lowest row with no DONE entry in the ledger, starting at 1)

**A. Ledger open:** append the row's entry with `date` start timestamp.

**B. Extract the beat truth (terminal, free):** From the CANONICAL V1 build folder
(use media-production/corpus.py's CANONICAL_BUILD_SLUGS for duplicate numbers):
read `make_narration.py` (SEGMENTS), `build.py` (BEATS + LEAD/GAP/KJV_GAP/HOLD
constants — they vary per build, use THAT build's values), and `audio/*.timing.json`.
Compute each segment's absolute audio window the same way that build.py does.
COPY (never move) the audio dir into `media-production-v2/build-NN-slug/audio/`.

**C. V2 beat map:** one picture per story BEAT per STORY-COVERAGE-LAW.md — every
action, reaction, realization, arrival in the narration gets its own picture; a
picture may span two segments only if nothing visually changes; long segments with
multiple visual moments get word-anchored sub-beats (the marker_time pattern from
build-10/18/19). **Coverage law (Cameron, 2026-07-28): aim ~15 pictures per story, range 10–20,
scaled by runtime** — the narration decides, never a forced count; a 2.5-minute
story may exceed 20 only when the beats genuinely demand it. **Burst sequences get
burst coverage** (Cameron's example, John 21: not knowing it's Jesus → told →
realizing → leaping from the boat → swimming — each micro-beat its OWN frame via
word-anchored markers). Write `media-production-v2/build-NN-slug/PROMPTS-V2.md`: per
beat — beat id (v2-rNNN-bBB), the exact narration text it covers, its audio window,
MUST SHOW / MUST NOT SHOW from the scripture, characters, camera/composition,
time of day, then the full prompt (STYLE-V2 + defense line if wide + scene + locks).
Check CONTENT-CARE.md flags for this row FIRST and obey them.

**D. v4 checklist on the sheet (replaces the v3 gate):** every Jesus shot has the
byte-identical LOCK v4 + REF line; no drift words (Caucasian, pale, blue-eyed,
blond, halo, glow, rim-light); nobody but Jesus in cream; every hand in two-figure
contact shots assigned a job; counts stated positively; no NEGATIVE-PROMPT lists.

**E. Generate (announce the Chrome burst first, then start immediately):**
`python3 media-production/flow_driver.py gen --prompt "<full prompt>" --out
media-production-v2/build-NN-slug/assets/sBB-slug.jpeg --size 2K [--ref ...]`
(the `--size 2K` download = 1536×2752 from the viewer menu, found 2026-07-28 —
the old gallery fetch was silently 1K/768×1376; never ship 1K again) — **Nano Banana
Pro for every shot containing Jesus, any close face, or a crowd; Nano Banana 2
allowed only for empty landscapes/objects.** One gen at a time (the profile lock
enforces it). Log every credit figure the driver prints. If Flow throttles
(~20 gens/hr is the measured ceiling), slow to 1 gen per 2 min — never evade, never
touch a CAPTCHA: if one appears, stop the browser and tell Cameron in one line.

**F. QC every still (Read the jpeg at full resolution) against the V2 rubric:**
HARD FAILS → regenerate with a prompt fix (log the defect code): embedded
text/border/panel/watermark · Jesus face doesn't match jesus-v2-face.jpeg (compare
side by side) · anyone else in cream · wrong headcount/object count · anatomy
count wrong (2 arms, 2 hands, 5 fingers where legible, 2 legs, 2 feet, 1 head, limbs
attached; count EVERY figure) · duplicated named character in one frame · action
contradicts the narration at a glance · wrong direction/time-of-day/setting ·
modern object · cartoon/plastic/painted look · fake teardrops · blur/softness ·
scale wrong. Then score 1–5 on: story-moment accuracy, composition, lighting
realism, emotion/reverence, faces/eyes, hands, fabric/material, period accuracy,
sharpness, consistency with this video's other stills — accept only ≥4 average with
nothing below 3. Three failed rerolls on one beat → note it in the ledger, make the
best available choice, and move on (never stall the line on one image).

**G. Assemble the V2 cut:** write `media-production-v2/build-NN-slug/build.py`
adapted from the V1 build's (same SEGMENTS import path trick, same constants, same
caption pipeline — captions are burned in, so they re-render with the new stills;
caption law: bottom band only, split long captions in sync). NO music bed. Output
`<book>-<chapter>_<slug>.mp4` in the V2 folder. Run `admin/verify-mp4.sh` on it,
silence-scan (no >2.5s gap in the spoken body), and frame-strip spot checks
(captions on right scenes, brightest + darkest frame legibility).

**H. Ministry gate:** write `MINISTRY-GATE.md` in the V2 build folder — the four
answers from PRODUCTION-BIBLE §5, honestly.

**I. Ledger close + commit:** end timestamp, elapsed, beats, gens attempted,
accepted, rerolls by defect code, credits logged, mp4 duration/size, notes. Commit
text files only. One push attempt max (2-min timeout), then move on.

**J. Next row. Do not wait, do not ask.** Give Cameron a one-line progress note
between videos and keep working.

## LEDGER FORMAT (media-production-v2/PRODUCTION-LEDGER.md)

Session header per session: session #, model, `date` start, machine.
Per video: `| row | slug | start | end | mins | beats | gens | accepted | rerolls | credits-noted | status | notes |`
Status values: DONE / IN-PROGRESS (with last completed step A–I) / BLOCKED(reason).
A fresh session resumes: read this file top to bottom, then the ledger, then continue
at the first row not DONE — finishing any IN-PROGRESS row from its last completed step.

## SESSION HYGIENE

- The repo is the memory; the ledger is the state. Never rely on chat scrollback.
- No screenshots for browser navigation (token law from PROTOCOL-V4).
- When your context gets tight: FINISH the current video through step I, update the
  ledger, print exactly: `SESSION FULL — open a new session and say: Read
  V2-KICKOFF.md and continue.` Then stop.
- Two browser attempts max on any failure, then log BLOCKED and move to terminal
  work on the next row's prep (steps B–D need no browser and can be batched ahead
  as background tasks while generations run).
