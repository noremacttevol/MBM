# RUNNER-LESSONS — the shared defect memory (every build session reads AND feeds this)

Created 2026-08-06 after Cameron: "it will probably still suck and make mistakes
becasue your not doing anythign for making it do it better learning from
previous mistakes or using previously made pictures."

**The law:** before Light QC on any row, read every pattern below and check the
frames against them. When you find a defect class NOT listed here — even one
you rerolled successfully — ADD it as one line before your session ends and
commit it. This file is how one session's $0.13 mistake stops being every
session's $0.13 mistake. Keep entries deduped and one line each.

## FLEET / COLLISION — read this at CLAIM time (step 1), before you pick a row

- **AUDIO-PRONUNCIATION complaints are OUT of runner scope — park the row, do
  NOT ship over them (2026-08-06, rows 50/51; row 46 shipped WRONG).** Run
  `v2_outline.py <row>` at claim time: if the OPEN complaint is a mispronunciation
  ("Cana → Kane-a", "tear → tare", "put-uth", "Lieth → lie-eth"), the fix is a
  re-voice (respell/spoken-override + regenerate narration), which the runner is
  forbidden to do (audio-immutability). Mark the row **NEEDS-AUDIO** on the board,
  write a RUNNER PARK note in QC.md with the resume, and take the next row. Do
  NOT ship a picture-rebuild over an open audio complaint — the audio is unchanged,
  so the complaint repeats (the worst failure). Row 46 was shipped this way with
  its "put-uth" complaint still open because its QC.md wrongly claimed "no open
  complaint"; always trust `v2_outline.py`, not the QC header, for open complaints.
  Rendering complaints (question-card "squares") are DIFFERENT — the V2 card
  renderer already fixed that class, so just verify the rendered end card is clean
  and ship.
- **FIRST check ALREADY-SHIPPED, before you check LIVE (2026-08-06, row-45
  second pile-on, ~$5 wasted).** A row can be fully DONE — mp4 committed, review
  card live — with NO live `v2_gen_api` process, because the lane that built it
  already exited. The "no live sibling → safe to resume" check below will then
  WRONGLY greenlight a full rebuild. So before generating ANY `RUNNING`/`A-auto`
  row, run `git log --oneline -1 -- media-production-v2/<build>/*.mp4` AND
  `grep 'id="v<NN>".*realistic-v2' site/review.html`: if either is non-empty the
  row is SHIPPED — do NOT regenerate, tick it BUILT on the AUTHOR-BOARD if it is
  not already, and take the next AUTHORED row. (The `assets/` count alone does
  not tell you shipped-vs-mid-build; the committed mp4 does.)
- **Art lives in `<build>/assets/*.jpeg`, NOT `<build>/frames/*.png`.** The
  `frames/` dir is essentially always empty. Judging "this claimed row crashed"
  by an empty `frames/` is WRONG and is what made 3+ lanes all pile onto row 45
  and burn redundant Gemini money (2026-08-06). Count `assets/*.jpeg` instead.
- **A `RUNNING` + `A-auto` row is NOT automatically stranded.** The autopilot
  runs up to 6 parallel lanes and every lane signs claims `A-auto`, so that
  signature CANNOT tell a live sibling from a crashed self. Before resuming any
  `RUNNING`/`A-auto` row, run `ps aux | grep v2_gen_api | grep -v grep`: if a
  `v2_gen_api.py <that-build>` process is alive, or its `assets/` is still
  growing, a LIVE sibling owns it — do NOT touch it, take the next clean row.
  Only resume a `RUNNING` row when NO sibling gen is live (mirror
  `autopilot.sh` next_stranded, which resumes only when LIVE==0).
- **Claim uniquely so the next lane can tell:** put asset count + "LIVE" in the
  AUTHOR-BOARD claim cell of a row you are actively building, and mark it BUILT
  the instant it ships so `next_ready` (state must be AUTHORED) skips it.
- **Never `git add -A` while siblings generate** — you will sweep another
  lane's in-flight `assets/` and `api-spend.jsonl` into your commit. Add only
  your row's paths + the boards/SESSION-LOG explicitly. Pull with
  `--rebase --autostash`.

## Known defect patterns (check every frame)

- **Modern objects sneak in**: hurricane/kerosene lamps (b41 war tent), modern
  chairs (b41), school slates chalked with ARABIC NUMERALS (b41 — period
  writing only, or blank), wristwatches, buttons, stitched tailoring.
- **Wrong aspect inside the canvas**: a 16:9 image letterboxed inside the 9:16
  frame (b41) — reroll on sight, never crop-rescue.
- **Second cream-robed figure**: ONLY Jesus wears cream; any other cream robe
  fails the frame.
- **Lens-staring**: any figure looking into the camera fails.
- **Fair-haired INCIDENTAL children/extras** (row 47 b15 family-in-the-house):
  even non-locked background people default to blond/light hair — a first-century
  Judean scene wants dark hair on everyone. Check kids in domestic/crowd frames,
  not just the locked cast. One reroll usually darkens them; a slightly-light
  child is FIX-WAVE, not garbage.
- **Headless/extra-limbed figures** (b16 headless at b07): count heads, arms,
  legs at full resolution, especially in crowds.
- **Beards appear/disappear/recolor between frames** (rubric lesson 13 — rows
  9/62/91/102): run the beard-only pass per person.
- **Giant/shrunken figures** (rubric lesson 14 — rows 56/69/107/112): height-
  check every multi-figure frame against a shared reference; Jesus is
  ordinary-sized, children stay child-sized.
- **Empty sandals with toes / lamps burning off the wick** (b17): objects obey
  physics; flames sit ON wicks only.
- **Fair-haired / blue-eyed drift on locked cast** (BUILDER in a FIX-WAVE
  note): locks say dark hair/eyes — check every named person against their
  lock even when the face "looks fine".
- **PLATE frames propagate their defects** (b41 lamp was IN the plate): QC the
  plate/anchor frame FIRST and hardest — every later beat of that place
  inherits its mistakes.
- **DO NOT reroll Jesus's green/hazel eyes** (row 54 b13 "I will" close-up): the
  locked V2 reference `JESUS-V2-REF/jesus-v2-face.jpeg` is itself green/hazel-eyed,
  so every Jesus frame echoes it and it is CONSISTENT across all shipped V2 rows
  (45/46/47/52/53). A reroll cannot change it (it re-echoes the ref) and only
  burns meter; editing the ref is a hard-rail violation. If Cameron files it, it
  is a whole-wave reference swap, not a per-row fix — log the observation in QC.md
  and move on. (Memory: `v2_rebuild_plan` "green-eyed Jesus".)
- **Place wired as a person** (WARTENT queued as a portrait, b41 session): a
  place must never carry a character lock.
- **Wrong story on the board** (row 44 two-debtors vs the QUEUE's Pentecost
  swap): cross-check the row against media-production/QUEUE.md BEFORE spending.
- **Footwear drift on a lone recurring figure** (row 46 farmer: sandals in
  b02/b06/b15 but tall boots in b12/b25): a one-person, many-frame story lets
  footwear (and other small worn items) swap between shots — glance at feet on
  the beard/identity pass. Minor: FIX-WAVE it, do not burn a reroll unless the
  frame is otherwise flawed.
- **Thin wire / power-line across open sky** (row 53 b13 courtyard exterior):
  a taut wire-straight line crossing the sky between rooftops/walls reads as a
  modern utility cable — a modern-object fail. It PROPAGATES from a courtyard
  PLATE (row 53's s03 plate carried it faintly), so QC the plate's sky first;
  one reroll of the affected beat usually clears it. Glance at the sky on every
  exterior/courtyard frame, not just the ground.
- **A single CARTOON / CGI-render frame in an otherwise-realistic row** (row 56
  b22 the-news-went-out came back as a smooth 3D-illustration/plasticky render
  while all 21 other frames were photographic). It reads as a totally different
  medium and, under Law 14 (realistic-only), a MIX fails the whole cut — worse
  than all-cartoon. It tends to hit the LAST/wide "epilogue" beat (news-goes-out,
  aftermath) where the prompt is a generic landscape with small figures. Check
  the STYLE of every frame, not just its content; one reroll usually lands a
  photographic take. Not subtle drift — this is a mandatory reroll on sight.
- **Green/hazel-eyed Jesus in extreme close-ups** (row 56 b09): the JESUS-MASTER-REF
  face carries a hazel/green cast that only reads clearly in a tight close-up
  (wides read brown). It is SYSTEMIC (all 200, baked into the reference) and a
  plan-level item awaiting Cameron — NOT a per-row regression. One reroll will
  NOT clear a baked-in reference trait, so do not burn rerolls chasing it; log
  FIX-WAVE and keep the best take. Fix belongs at the master-ref level.
- **Multi-panel COLLAGE inside one 9:16 frame** (row 42 barren-fig; row 45 b10
  twice — a 4-up then a 3-up grid of separate shots stacked in one frame):
  triggered by beats that ask for MANY workers doing MANY tasks at once
  ("tenants working the lease"). Reroll on sight — the model eventually lands a
  single coherent wide. Never crop-rescue a panel out of it.
- **False "tiled/collage" frame from ffmpeg INPUT-seek (`-ss` BEFORE `-i`)**
  (row 55 caption QC): extracting a caption frame with `ffmpeg -ss <t> -i mp4`
  can land on a non-keyframe and decode a garbled/striped image that looks like
  2-3 stacked panels — it is a DECODE ARTIFACT, not a real collage in the video.
  Before rerolling/re-cutting, re-extract with OUTPUT seek (`ffmpeg -i mp4 -ss <t>
  -frames:v 1`): if the accurate-seek frame is a single clean image, the mp4 is
  fine. Always confirm a suspected assembly defect with an accurate-seek frame.

## Reuse before regenerate (Cameron's core order — rubric lesson 11 + COST LAW)

- Plates: `v2_stash.py --wire` before generating; promote-first for new places.
- **After every ship: run `python3 media-production-v2/v2_stash.py --scan` and
  commit STASH-INDEX.json** so the row's passing stills instantly become
  reusable plates for every later row. A place generated twice because the
  index was stale is a COST LAW violation.
- Portraits/cast sheets are reused across rows automatically — never re-pay
  for a face that has a sheet.
