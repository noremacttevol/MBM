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
  - **EXCEPTION — a pronunciation complaint whose re-voice is ALREADY DONE and
    baked into the V1 mp4 is NOT a park; SHIP it (2026-08-06, row 57 "lieth →
    lie-eth").** Before parking a pronunciation row, check whether the author
    already fixed it: (1) board Audio column says **OK** (not CHECK); (2)
    `make_narration.py` has the `SPOKEN`/respell override for that word;
    (3) `git log` shows a "verified in final audio" fix commit AND the V1 mp4
    was re-rendered AFTER it. If all three hold, the runner is NOT re-voicing —
    it ships the already-corrected byte-identical audio, and **AUDIO LOCK PASS
    is the cryptographic proof** the fix is in the shipped audio. Rows 50/51
    park because their audio is CHECK and the fix is not yet rendered; row 57
    ships because its audio is OK and the fix is already in the mp4. Put the
    proof in the QC COMPLAINT LEDGER and answer it on the review card.
  Rendering complaints (question-card "squares") are DIFFERENT — the V2 card
  renderer already fixed that class, so just verify the rendered end card is clean
  and ship.
  - **A board that says "AUDIO FIX DONE / Audio OK" is NOT proof the fix ships —
    verify the fix reached the AUTHORITATIVE audio before trusting it (2026-08-07,
    row 50).** `v2_assemble` sources narration from the V1 mp4
    (`media-production/<build>/*.mp4`), or from the V1-dir mp3s only when
    `AUDIO_FROM_V1_SEGMENTS=True`; it EXPLICITLY ignores the V2 build-local
    `audio/` dir. Row 50's Cana→cayna fix ran `make_narration.py` from inside the
    V2 build dir, so the corrected n1/n3 landed in
    `media-production-v2/<build>/audio/` (orphaned) while the V1 mp4 (2026-07-29,
    plain "Cana"=KAH-nuh) was never re-rendered. AUDIO LOCK would deceptively PASS
    (durations match, newer_mp3s=0) yet ship the OLD rejected pronunciation =
    repeat the complaint. DETECT before building any "audio-fixed" pronunciation
    row: (a) `grep AUDIO_FROM_V1_SEGMENTS beats_v2.py`; if absent/False the ship
    audio is the V1 mp4 — check the V1 mp4 mtime is AFTER the fix commit; (b) if
    the flag is True, hash-compare the V1-dir mp3 vs the V2-dir fixed mp3 (`md5sum`)
    — they must MATCH. If the fix is only in the V2 dir, PARK NEEDS-AUDIO (the
    audio authority must copy the fixed mp3s into the V1 dir + re-render the V1
    mp4, or set the flag). A passing AUDIO LOCK proves byte-consistency with the
    V1 mp4, NOT that a pronunciation complaint is fixed.
  - **A MULTI-part pronunciation complaint can be HALF-fixed — one word landed in
    the shipping mp4, the other orphaned (2026-08-07, row 70).** Row 70's "I-S/IF"
    was fixed by the earlier REDO render (shipping mp4 says "if/is" —
    whisper-confirmed), but the SAME-session respell for the 2nd word
    ("proceedeth→proceeduth") was committed AFTER the V1 mp4 (respell 2026-08-06,
    mp4 2026-07-28), so it never reached the shipping audio. ANY unfixed part =
    park. When whisper CAN'T adjudicate the sound (-eth vs -uth both transcribe
    "proceedeth"), decide acoustically: extract the segment window from the
    shipping mp4 and cross-correlate the 16k-mono waveform against BOTH the V1-dir
    mp3 (old) and the V2-dir mp3 (fixed) — the mp4 matches whichever it was
    rendered from (row 70: 0.757 vs OLD, 0.026 vs FIXED, fixed take +1.1s longer).
    High-corr-with-OLD → the fix is orphaned → park.
  - **PACING/"too fast"/"meaningless"/"rushed" complaints are ALSO audio-domain —
    park them the same as a mispronunciation (2026-08-06, row 10).** Cameron's
    row-10 complaint was not a wrong word but the DELIVERY of Jesus's Messiah
    reveal j2 "I that speak unto thee am he" being too fast to land. The fix is a
    re-voice (extend the SPOKEN/PHRASE_SPOKEN pauses + regenerate + re-assemble),
    which the runner may not do. A row can even already carry a partial
    PHRASE_SPOKEN ellipsis (row 10 had one for a slur) and STILL be too fast
    overall — a pre-existing override is not proof the pacing complaint is fixed.
    Park NEEDS-AUDIO, do NOT re-cut pictures.
  - **OVER-CORRECTION swings back to a complaint — a pacing re-voice can go too
    FAR the other way (2026-08-07, row 10 recurrence).** The row-10 audio-fix
    answered "too fast" by stacking `-30%` rate + a leading ellipsis + a mid-line
    ellipsis on one 5-word edge-tts line → 4.92 s, and Cameron came back with "now
    its too slow and sounds horrible like a robot... undo it and make it right." A
    synthetic voice (edge-tts) dragged well below its default with two dead-air
    gaps reads as a robot. Fix ONE slow-down at a time and ear-check toward the
    MIDDLE (deliberate, not stretched); don't pile rate-cut + multiple pauses on a
    short line. Still an audio-domain park for the runner — NEEDS-AUDIO, no re-cut.
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
- **QC the frames in the build's `OUTPUT_ASSET_DIR`, NOT `assets/` (2026-08-07, row 11 storm).** A realistic rebuild sets `OUTPUT_ASSET_DIR = "assets-realistic"` in beats_v2.py — `v2_gen_api` generates INTO it and `v2_assemble` renders FROM it, while the old rejected roughs stay in `assets/`. If you Light-QC `assets/`, you review the STALE rough frames, not what shipped — on row 11 this made me wrongly conclude two rerolls "reproduced identical / no Jesus" (I was comparing old-to-old) when the real `assets-realistic/` frames were correct and my rerolls had actually WORKED. Before QC, run `grep OUTPUT_ASSET_DIR beats_v2.py` (default "assets") and view THAT dir; or extract frames from the rendered mp4 (ground truth). `ls --time-style=full-iso` both dirs — the shipped one is today's date. Confusing the two burns rerolls chasing phantom defects and can ship un-QC'd frames.
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
- **Your `git commit` can "fail" with `no changes added` even though you just
  staged — a sibling lane's concurrent commit absorbed your staged index
  (2026-08-06, row 76).** Concurrent `git` processes share `.git/index`, so if a
  sibling runs `git commit` while your files are staged, ITS commit ships YOUR
  staged mp4/QUEUE/AUTHOR-BOARD and your own commit then finds nothing. This is
  NOT data loss: run `git log -1 --format=%H -- <build>/<mp4>` to find the commit
  that actually contains your mp4 and `git branch -r --contains <hash>` to confirm
  it's on origin/main — then point the review card's `data-hash` at THAT commit,
  not a hash you expected to create. Verify with `git ls-files <mp4>` (tracked)
  before assuming you must re-commit.

## Known defect patterns (check every frame)

- **Modern objects sneak in**: hurricane/kerosene lamps (b41 war tent), modern
  chairs (b41), school slates chalked with ARABIC NUMERALS (b41 — period
  writing only, or blank), wristwatches, buttons, stitched tailoring.
- **Wrong aspect inside the canvas**: a 16:9 image letterboxed inside the 9:16
  frame (b41) — reroll on sight, never crop-rescue.
- **Second cream-robed figure**: ONLY Jesus wears cream; any other cream robe
  fails the frame.
- **Unlocked secondary figure defaults to a Jesus DOUBLE (row 65 C-FIX, b02
  "his own disciples were in the middle of it").** On a `jesus:False` beat whose
  named figures (here two cornered disciples) carry NO locked garment colour and
  NO face lock, the model paints them with Jesus's exact bearded/long-haired
  look AND puts one in cream — the frame reads as "2 jesus" even though no Jesus
  REF is attached. QC EVERY `jesus:False` multi-figure frame for a Jesus double,
  not just for cream. Fix: reroll `--only <beat> --redo` (no lock edit needed —
  the CAST-CLOSURE + no-cream clauses usually resolve it in one take; the two
  disciples came back in brown + dark-red with ordinary faces). Root cause is
  UNSPECIFIED garment/face on the secondary cast, per v2_prompt.py's own note.
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
- **Oversized birds/animals in nature frames** (2026-08-07, row 111 b11/s11,
  Cameron C-FIX "0:09 everything is out of scale and weird"). A beat whose scene
  names small wildlife working the FOREGROUND ("sparrows working the seed") can
  render the birds GIANT — the sparrows beside Jesus's hand and next to a seated
  baby came out bigger than the infant's head, throwing the whole frame out of
  scale. It is the same failure as lesson 14 but for animals, and it hides
  because the PEOPLE are fine. FIX: one `--only <beat> --redo` re-anchors small
  birds at true size ($0.13, one frame). CHECK: in every nature/wildlife frame,
  height-check the animals against the nearest person the same way you check
  figures — a sparrow must read tiny next to a hand, never cat-sized.
- **Empty sandals with toes / lamps burning off the wick** (b17): objects obey
  physics; flames sit ON wicks only.
- **Fair-haired / blue-eyed drift on locked cast** (BUILDER in a FIX-WAVE
  note): locks say dark hair/eyes — check every named person against their
  lock even when the face "looks fine".
- **Warm/golden side-light washes a locked dark-haired figure GINGERY-ORANGE**
  (row 69 b12/s12 — Cameron C-FIX "John's hair changed to orange").** A
  black-haired locked character (John, whose lock even says "sun-shot black
  hair") in a low warm-sun frame can render a light sandy grey-gingery top
  that reads ORANGE next to the same character's black hair in cooler frames.
  It is NOT subtle drift to ignore — Cameron reads it as a character/reference
  break. Check every locked-cast frame's HAIR TONE against the reference,
  weighting warm-lit / backlit / low-sun frames hardest; a lone warm frame
  among cooler ones is the tell. One `--only <beat> --redo` re-anchors to the
  ref and lands the correct dark hair. When only 1 of N frames drifts, reroll
  JUST that frame — the others are already correct (13/14 were fine on row 69).
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
- **"Weird eyes" ≠ eye COLOUR — DO reroll a misaligned/dead-stare gaze** (row 1
  C-FIX, b15, Cameron complaint "1:10 Jesus's eyes looking weird"). The
  no-reroll rule above is about the ref's green/hazel *colour*, which a reroll
  cannot change. A *wall-eye, cross-eye, mismatched pupils, dead stare, or a
  gaze not converging on one point* is a per-frame generation defect and a
  reroll DOES fix it (one reroll gave both eyes open, symmetric, aligned). When
  a beat carries an author "CAMERON GATE ... NO weird eyes" line, that beat is
  cleared to reroll for gaze geometry — inspect the eyes at full resolution
  before accepting the take.
- **Reach/touch lands on the wrong body part** (row 1 C-FIX, b11, Cameron
  complaint "she touches ... the tassels only not his back thigh"). A "touch the
  hem/edge" beat can render the hand up on the back/thigh even when the scene
  text says fingertips at the fringe near the ankles. QC every reaching frame by
  asking WHERE on the body the hand actually lands; if it is not on the named
  target (hem/tassel/foot), reroll — the beat text already specifies the correct
  spot, the model just missed it, and a fresh gen usually obeys.
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
  exterior/courtyard frame, not just the ground. NOT courtyard-only: it also hits
  open-landscape frames (row 71 b12 garden-tomb in an olive orchard had a taut
  line crossing the misty sky between the trees) — check the sky on EVERY exterior,
  orchard and hillside frame; one reroll cleared it.
- **Modern paved roads / shoreline highway in a FAR-AERIAL landscape** (row 71
  b21 "the going-out" descent, and faintly b19): a high wide aerial of the Galilee
  hills can render modern-looking paved switchback roads and a straight shoreline
  highway among the terraces. At extreme distance it is borderline (ancient paths
  and terraces look similar), so it is usually FIX-WAVE, not a mandatory reroll —
  but if a straight, graded, modern-width road reads clearly, reroll the aerial;
  the model can land the same vista with only footpaths. Watch the going-out /
  epilogue landscape beats specifically.
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
- **Collage also fires on a SINGLE-figure ACTION beat, as a repeated-same-pose
  triptych** (row 66 b07 Peter's sword-swing came back as 3 vertically-stacked
  near-identical shots of the same man swinging). Not just many-workers beats —
  any "dramatic motion" beat (a swing, a fall, a run) can stack the motion into
  sequential panels. Mandatory reroll on sight; one redo lands a single coherent
  frame. Never crop-rescue one panel.
- **A beat whose TEXT repeats a COUNTING sequence is a STRUCTURAL collage
  trigger that survives the reroll budget** (row 114 b13 "what about forty,
  thirty each"): the enumerated numbers make the model tile one panel per number
  — TWO rerolls both returned 4-up stacks (unlike the row-66/45 collages that a
  single redo fixes). This is NOT a coin-flip a runner can win: keep the best
  take, FIX-WAVE it, and hand to the AUTHOR to de-repeat the counting in the beat
  text (or add an anti-collage cue). Do not burn more than the row's 2 rerolls
  proving it stays a collage — the fix is beat-text, not another render.
- **False "tiled/collage" frame from ffmpeg INPUT-seek (`-ss` BEFORE `-i`)**
  (row 55 caption QC): extracting a caption frame with `ffmpeg -ss <t> -i mp4`
  can land on a non-keyframe and decode a garbled/striped image that looks like
  2-3 stacked panels — it is a DECODE ARTIFACT, not a real collage in the video.
  Before rerolling/re-cutting, re-extract with OUTPUT seek (`ffmpeg -i mp4 -ss <t>
  -frames:v 1`): if the accurate-seek frame is a single clean image, the mp4 is
  fine. Always confirm a suspected assembly defect with an accurate-seek frame.
- **A person-free "calm establishing WIDE" beat renders figures as a floating
  CUT-OUT composited over a bird's-eye AERIAL mini-view of the same place** (row
  45 C-FIX, b46 `s46-that-is-the-setup`, Cameron "0:50 ... trash and just look
  stupid"): the establishing beat locked a VINEYARD plate and its own text is
  person-free, but the model pasted the story's tenants at eye-level ON TOP of an
  aerial view of the vineyard — two clashing perspectives, a ghosting/haze seam
  around the people, a melting head. It is the collage/double-perspective family
  and a MANDATORY reroll on sight; one `--redo` landed a single coherent
  establishing wide. Check every "whole place laid out / the setup / establishing"
  wide for a pasted-in perspective mismatch, not just multi-worker beats.

## Reuse before regenerate (Cameron's core order — rubric lesson 11 + COST LAW)

- Plates: `v2_stash.py --wire` before generating; promote-first for new places.
- **After every ship: run `python3 media-production-v2/v2_stash.py --scan` and
  commit STASH-INDEX.json** so the row's passing stills instantly become
  reusable plates for every later row. A place generated twice because the
  index was stale is a COST LAW violation.
- Portraits/cast sheets are reused across rows automatically — never re-pay
  for a face that has a sheet.
- **Basket of "fragments/leftovers" renders as pale STONES in dusk/low light**
  (row 58 b21 twelve-baskets): a count beat that should show baskets of BROKEN
  BREAD can come back with grey rounded lumps that read as rocks, especially at
  dusk. Check that basket contents plainly read as bread (golden crust, not grey
  stone); one reroll usually lands clear bread. Distinct from the count itself —
  fix the food-legibility first. Exact object counts (e.g. "twelve baskets")
  rarely land to the exact number in a receding line; that is FIX-WAVE, not a
  reroll, once the contents read correctly.
- **`v2_stash.py --wire` auto-suggests a WRONG-REGION place plate the row's QC
  forbids** (row 59: WILDS auto-wired from build-54 the-leper, but row-59 QC.md
  explicitly bans it — leper's Judean broken country ≠ this Decapolis slope).
  `--wire` matches on TOKEN name only, blind to region/period intent. ALWAYS read
  the row's QC.md place notes before trusting a wired plate: if QC says "do NOT
  take build-XX's <TOKEN>" or "promote-first," clear PLACE-WIRING.json (echo '{}'
  > it), generate the anchor beat, eyeball it, and `--promote` from THIS row's own
  frame. A copied wrong-region plate would propagate the wrong place to every beat.
- **`v2_stash.py --wire` OVERWRITES an already-committed PLACE-WIRING.json entry
  with a different (newer) source build (2026-08-07, row 50 ROAD).** The author had
  committed `ROAD ← build-38-persistent-widow b39`; running `--wire` at build time
  silently rewrote it to `build-79-the-seventy-sent` (a newer ROAD that didn't exist
  at authoring time). Both are valid ROAD plates, but the runner must not override
  the AUTHOR's committed wiring. DETECT: `git diff PLACE-WIRING.json` right after any
  `--wire`; if an EXISTING token's src_build changed, `git checkout PLACE-WIRING.json`
  to restore the committed choice. `--wire` is only for tokens with NO committed entry.
- **DECLINE a place plate when its token spans two different rooms/times-of-day
  (2026-08-07, row 50 HOUSE).** Row 50's HOUSE token covers BOTH a night lamplit
  sickroom (b03-b06) AND a bright daytime colonnaded court (b27). Promoting either
  as the single plate bleeds the wrong time-of-day onto the other (the row-101/103
  plate-composition class), and a reroll can't fix it because the plate re-attaches.
  When the receiving beats are genuinely different scenes, DON'T promote — leave the
  token plate-free so each beat renders its own place/time; the CHARACTER refs
  (NOBLEMAN/BOY) already hold identity, and each beat came out correct (verified b27
  as the day court with sea view). Minor within-room architecture drift is FIX-WAVE.
- **A big "crowd streaming up a real Galilee slope" wide comes back as a MODERN
  PILGRIMAGE PHOTO — the background fills with tourists in ballcaps, sunglasses,
  backpacks, windbreakers and a lanyard** (row 68 b30 `no-names`): asking for a
  large crowd on the actual Sea-of-Galilee hills pulls the model toward
  present-day Holy-Land-tour stock photography, so a period foreground figure
  ends up surrounded by 21st-century hikers. Modern-object fail — mandatory
  reroll on sight; one redo usually lands an all-period crowd. Scan the WHOLE
  crowd of any real-location wide for modern dress/gear, not just the named
  subject. Distinct from a single stray modern prop — here the entire background
  population is modern.
- **A "he does X with the traveling prop" single spawns a near-identical TWIN of
  the lone recurring subject** (row 64 b25 "he stood up, rolled up the mat"): the
  beat's only subject is the healed man rolling/carrying his mat, but the model
  added a SECOND grey-bearded old man ALSO carrying a rolled mat right behind him —
  a confusing duplicate (lesson 3 twins + lesson 12 single-subject). One reroll of
  such a prop-handling single usually drops the extra figure; but beware the reroll
  landing a MULTI-PANEL COLLAGE instead (row 64 b25 reroll #1 came back a 4-up grid),
  so verify the reroll is a single coherent frame, not a montage. Two rerolls cleared
  it. Distinct from crowd variety — this is the STORY'S subject duplicated in a shot
  that should hold only him.
- **Model bakes a hallucinated SUBTITLE into the still** (row 67 b06: a first-take
  frame printed "…one for Moses and one for Elijah" as a caption burned into the
  art). It hits beats whose narration is a spoken quote; the model "helpfully"
  renders the line as an on-image subtitle. Two-fold failure: (a) a text-in-image
  defect that will collide with the assembler's real caption, and (b) it can print
  the EXACT word of an open complaint (here "Elijah"). Scan every frame for any
  burned-in lettering; reroll on sight — the real caption is added at assembly.
- **"Sketching/drawing X in the air" prompts render literal cartoon doodles**
  (row 67 b07: "hands sketching three shelters in the air" came back as black
  line-drawn tent ICONS floating in the frame — a Law-14 realistic/cartoon MIX).
  Any beat whose must_show describes drawing/sketching/imagining a shape is at
  risk of a graphic-overlay doodle. Reroll → the model lands a realistic gesture
  (open hands toward the subject) with no floating graphic.

## ASSEMBLY / AUDIO-LOCK

- **A STALE-V1 row cleared with AUDIO_FROM_V1_SEGMENTS=True can STILL ship a
  broken cut — the audio rebuilds to the live length but the beats_v2 STILL-
  WINDOWS were scaffolded on a LONGER timeline, so the picture track overruns
  the audio and the final mux truncates the tail + the whole question card
  (2026-08-07, row 74).** AUDIO REBUILD PASS only proves the AUDIO is right; it
  does NOT check the VIDEO length. Row 74: audio 184.57s but captioned.mp4 =
  201.5s (windows ran to 206.32s vs live card_start 176.738s, ~30s drift) → last
  ~25s of stills + the beige card chopped, and stills drift vs captions (row-42
  class). ALWAYS after assembling any AUDIO_FROM_V1_SEGMENTS row, check
  `ffprobe segs/captioned.mp4 duration` ≈ `extract_beats card_start` (±0.2s); if
  captioned ≫ that, the windows are stale. FIX (runner, timing-metadata only, no
  re-voice/reroll — §row-42): remap every beats_v2 `window` onto the live
  extract timeline (piecewise-linear on segment onsets, last still→card_start),
  re-assemble; AUDIO REBUILD SHA256 stays identical (audio untouched). This is a
  SYSTEMIC risk for the whole 74/78/80/82/86-100/105/106/108 STALE-V1 batch —
  verify captioned≈card_start on each before shipping.
- **AUDIO LOCK fails with "extracted timeline Ns but authoritative V1 final Ms"
  when the V1 mp4 is STALE (2026-08-06, row 69).** If a build's
  `make_narration.py` (or narration segments) was edited AFTER the V1 mp4 was
  rendered, the V1 mp4's audio is out of date and its duration won't match the
  current beats timeline. The runner CANNOT fix this — the assembler's hint
  ("set AUDIO_FROM_V1_SEGMENTS = True in beats_v2.py") requires editing
  beats_v2.py (outside runner writes) and is an author audio decision under the
  audio-immutability law. Diagnose (compare V1 mp4 mtime vs make_narration.py
  mtime; sum audio/*.mp3), write the root cause + resume into QC.md, mark the
  board row NEEDS-AUDIO with the stills-generated note, clear Ready, push, take
  the next row. The generated stills are valid and reusable — do NOT regenerate
  when the author later fixes the audio.
- **PRE-FLIGHT the AUDIO LOCK for $0 BEFORE generating stills (2026-08-06, rows 74 & 77). TWO independent gates — check BOTH.** Load `v2_assemble` + `extract_beats`, compute `total = data['total']`, `d = duration_of(V1mp4)`, and count placed mp3s whose `content_time` > the mp4's `content_time`+1.0 (`newer_mp3s`). Park NEEDS-AUDIO and generate NOTHING if EITHER fails:
  1. **RECENCY** (`assert_v1_final_is_current`): `newer_mp3s > 0` (mp3s changed after the V1 mp4 render). Row 74 = 19/19 newer, d 12.9s short.
  2. **DURATION** (v2_assemble.py line 531, the one I missed first time): `abs(total - d) > 1.0` — a mismatch in EITHER direction, not just `excess>0.75`. Row 77 tripped at d−total = **−1.74s** (V1 *shorter*) even though newer_mp3s=0, and it cost ~$2.40 to learn because the first version of this lesson only tested the positive-excess direction. BUILDABLE requires `newer_mp3s==0 AND abs(total-d) ≤ 1.0`. Shipped rows read `newer=0, |excess|≈0` (75: −0.47 ✓). From the row 75-100 batch, rows with `abs(excess)>1.0` (77 −1.74, 83 −2.20, 86 −1.06, plus the newer>0 rows 78/80/82/88/92/96/99/100) all fail — do NOT claim/generate them; they need an author `AUDIO_FROM_V1_SEGMENTS=True` edit first. Doing both checks at step 2 turns a ~$3-6 wasted-generate-then-park into a $0 park.
  - **The pre-flight MUST read the mp3s from `extract_beats.extract(row)["v1_dir"]`
    under `media-production/`, NOT the v2 build dir (2026-08-06, row 76 false
    alarm).** `assert_v1_final_is_current` locks to the V1 build's `audio/*.mp3`.
    Those are tracked, so `content_time` returns their git COMMIT time. The
    `media-production-v2/<build>/audio/*.mp3` copies are UNTRACKED, so
    `content_time` falls back to their checkout MTIME — always "newer" than the
    committed mp4 — and a pre-flight pointed there fires a false STALE-V1 on
    EVERY row (I saw 76–90 all "STALE", but with the correct V1 dir rows
    76/77/79/81/83/84/85/86/87 PASS and only 78/80/82/88/89/90 are genuinely
    stale). Resolve `v1dir = os.path.join(ROOT, data["v1_dir"])`, pick the single
    non-backup `*.mp4` in it, and call `assert_v1_final_is_current(row, v1dir,
    locked_final, data, total, duration_of(locked_final))` verbatim — never
    hand it the v2 dir. Batch-pre-flighting a whole authored block this way ($0)
    tells you which rows to build vs park before you touch the meter.

## COVERAGE / SCRIPTURE-DETAIL DRIFT
- **Provision-absence ("no purse, no scrip, no shoes") drifts back into the WIDE
  frames even when the close-ups obey it (2026-08-06, row 79 the-seventy-sent).**
  When a beat's must_show is the explicit ABSENCE (Luke 10:4 — the tracked pair
  set out empty-handed), the tight close-ups (b02/b03) land clean: empty hands,
  no bag on either shoulder. But the SENDING/HARVEST/RETURN wides (b01/b04/b09/
  b13/b16) quietly re-add a small shoulder scrip/satchel to the disciples — the
  model's default "traveller" silhouette. This is SUBTLE drift, not obvious
  garbage: it doesn't repeat a filed complaint and the beats where "no bag" is
  the spoken subject are correct, so under the COST LAW it is a FIX-WAVE note,
  NOT a reroll (rerolling a wide for one small satchel burns budget and the
  ROADS/plate re-seeds the same silhouette anyway). Log it in QC.md FIX-WAVE and
  keep the take; the fix wave can prop-edit the scrips out of the wides later.
- **Single-figure close-up beat renders in DAYTIME/SUNSET, ignoring a night row** (row 85 b04 "and the angel said" came back a rugged man in a dirty tunic against a bright golden daylight/sunset sky while all 22 other frames were deep night). Isolated 1-character beats (a portrait-style "X said/spoke" shot) lose the scene's time-of-day because the surrounding geometry is gone. Check the SKY/lighting on every lone-figure beat against the row's stated time of day, not just the wides; one reroll restored night. Mandatory reroll on a clear time-of-day mismatch.
- **Angel-announcement / tight-composition beats drop below the row's stated crowd COUNT** (row 85 s03/s05: three shepherds instead of the canonical four — the fourth falls outside the tighter angel framing). Subtle count drift in a non-count-named beat is FIX-WAVE, not a reroll; the wides still carry the full count. Glance at head-count on tightly-framed hero beats.
- **Heavenly-host / glory-light color drifts GOLDEN vs a row-canon WHITE** (row 85 s09 "Glory to God" came back amber while s08/s11/s12 read white-from-above). On angel-canon rows whose QC specifies WHITE glory light (never sunset tones), a golden take is borderline — FIX-WAVE it unless it reads as a literal horizon sunset. The host itself should be rank-upon-rank of INDIVIDUAL robed people, never a swirl of light (this held on 85).
- **A beat authored with an INTERIOR must_show renders a DAYLIT INTERIOR ROOM
  that breaks a night/outdoor story's continuity** (row 91 b10 "he did not hide
  it": a bright-windowed mud-brick room among 39 night-olive-garden frames). A
  reroll (`--only bNN --redo`) REPRODUCES the interior because the beat's own
  must_show drives it — it is NOT a generation fluke, so do not burn a 2nd
  reroll chasing it. It also does not hit any runner reroll-garbage criterion
  (subject present, only-Jesus-cream, no modern object, no lens-stare, anatomy
  fine), so the runner keeps the best take and logs it as a FIX-WAVE **author
  beat-text** item (rewrite must_show to the correct place/time, then --redo).
  Distinct from subtle drift: the whole SCENE (place + time-of-day) is wrong,
  but the fix is the author's beat text, not the runner's meter.
- **A promote-first PLACE plate propagates its static anchor composition onto a
  MOVEMENT/journey beat of that place** (row 101 b06 "went forty days ... unto
  Horeb": the HOREB plate was promoted from b12's cave-mouth frame, so b06 —
  which wants the tiny figure crossing vast country toward the far mountain —
  inherited the arrived-at-the-cave composition instead). Expected side-effect of
  place-locking by image; the destination beats look right, only the travel beat
  loses its "journey" wide. NOT garbage and NOT a reroll under the COST LAW
  (rerolling re-attaches the same plate) — FIX-WAVE note it. If a place has a
  distinct travel/approach beat, promote its plate from a WIDE anchor, or leave
  that one movement beat plate-free so it can render the journey.
- **Single-location OUTDOOR story drifts INDOOR on beats that don't lock the place token** (row 103 peters-confession b04/06/12/13/15/17 — the whole story is "the same glade under the pale cliff throughout," yet the 6 beats whose `locks` omit CLIFF rendered a generic house/village interior). The place PLATE attaches ONLY to beats whose `locks` name the place token, and when those beats' scene text carries no outdoor cue the model defaults to an interior. Rerolling does NOT fix it (verified: 2 rerolls of b13 both stayed indoor, and the first even broke Peter's locked face) — it is a coin-flip that burns meter (COST LAW) and can damage a locked face. NOT runner-fixable: log FIX-WAVE + author handoff (author adds the place token to EVERY beat's `locks` in a single-setting story, or adds an outdoor cue to the scene text, then regenerates only those beats). Do not burn more than one probe reroll confirming it stays indoor.
- **A COLLAGE reroll can return a CARTOON/CGI frame — budget for a 2nd attempt**
  (row 104 b06): rerolling a stacked-panel collage beat ("he ran to him" action)
  first landed a smooth stylized 3D/animated-film render (Law-14 mix fail), and
  only the 2nd allowed reroll landed a clean photographic single. Both collage
  AND cartoon are mandatory-reroll on sight, so an action/motion beat can legitimately
  need TWO rerolls; count on it when budgeting, and always re-view a collage reroll
  for STYLE, not just for "is it one panel now."
- **A beat that omits a character's REF drifts that character's costume/identity —
  a reroll will NOT fix it** (row 104 b14): n4 was authored with only the ELI ref,
  no SAMUEL ref, so Samuel's locked navy tunic rendered TAN and re-drifted tan on
  reroll (nothing to lock it). The runner cannot edit the beat (hard rail). Do NOT
  burn rerolls chasing a costume/identity drift on a beat whose `[+N char ref: …]`
  banner is missing that person — log it FIX-WAVE for the author to add the ref.
- **A single still renders ROTATED 90° (whole scene sideways)** (row 110 b07 "his
  name be honoured … kingdom come": a rooftop-figure-hands-lifted-over-the-town
  beat came back with the horizon running vertically down one edge and the figure
  lying sideways — the correct COMPOSITION, just rotated a quarter turn). It is
  outright garbage (nobody can read a sideways frame), distinct from the 16:9-
  letterbox-inside-9:16 defect. Mandatory reroll on sight; one `--redo` landed it
  upright. Tends to hit lone-figure "lifted hands / reaching outward" beats.
- **QC a promote-first plate for UNWANTED PEOPLE before promoting — a crowded
  anchor bleeds a crowd onto later beats of that place (row 114 abraham-sodom
  HEIGHT plate s05).** The HEIGHT anchor b05 ("for those cities had grown dark")
  is authored person-free (locks HEIGHT only, landscape must_show), but the model
  added a ~6-person foreground group. It was promoted anyway on the reasoning
  "the receiving beats' own text dominates" — WRONG: the crowd bled into 3 of the
  solo-plea beats (s10/s15/s20) where Abraham should be ALONE (Gen 18:22), while
  s08/s18/s21/s23 stayed correctly solo/person-free. Lesson: when the place's
  beats are meant to be solo or person-free, the plate anchor MUST be QC'd
  person-free BEFORE `--promote`; if the anchor rendered a crowd, reroll the
  anchor for a clean person-free plate first (one reroll on the plate is far
  cheaper than 3 FIX-WAVE regens downstream). Once promoted, the crowd is a
  FIX-WAVE (re-promote a person-free frame like s21/s23 and regen only the
  crowded beats), NOT a per-beat reroll.
- **`429 RESOURCE_EXHAUSTED "prepayment credits are depleted" is a REAL balance-
  zero, not the auto-reloading rate limit (row 114, 2026-08-06).** Distinguish
  the two: a rate-limit 429 clears on the one-retry-after-60s; a "prepayment
  credits are depleted" 429 persists after the retry and halts EVERY lane until
  Cameron tops up Google AI Studio billing. On the depleted variant, do the one
  retry per law, then park with the resume command in QC.md, push, and stop clean
  — no other row is buildable either (all need generation), so there is no next
  ready row to move to.
- **"Coats of skins" / any leather-garment beat renders as a MODERN tailored
  leather JACKET or trench coat** (row 113 b20 the-coats-found, and faintly
  b21/b24): a Genesis-3 beat asking for "garments of soft dark leather" comes
  back as a present-day leather jacket with a COLLAR, LAPELS and BUTTONS laid on
  a stone — a modern-object fail. One `--redo` landed raw draped animal HIDES
  (correct, untailored). Watch any beat whose prompt names leather/hide/skin
  clothing; the model defaults to modern outerwear. Reroll on sight when buttons/
  lapels/zippers appear; a slightly-modern seamed hide is FIX-WAVE. (For Adam/Eve
  a fur/hide look is CORRECT — the "never fur/fleece" rule is Jesus-only.)

## INFRA / BILLING
- **`429 RESOURCE_EXHAUSTED` with body "Your prepayment credits are depleted" is a HARD billing wall, NOT the transient rate-limit 429 (2026-08-06, rows 115 & 116).** The brief's "retry once after 60 s, billing auto-reloads" applies to the rate-limit 429 only; the *prepayment-depleted* message does NOT clear on a 60 s retry (verified twice). It is GLOBAL to the Gemini key — every concurrent lane hits it, so there is NO other Ready row to fall to (the same dead key blocks all of them). Correct response: retry once to confirm, then PARK the row (QC.md RUNNER PARK + exact resume command; keep any already-generated stills — they are valid, do NOT regen), leave the board/QUEUE noting "Gemini credits depleted — Cameron top up AI Studio billing," add a SESSION-LOG entry flagging the ACTION FOR CAMERON, commit, push, and STOP the session clean. Do not burn turns re-trying or hopping rows on a depleted key.

## C-FIX / COMPLAINT HANDLING
- **"lost his beard at N seconds" is usually a WIDE-SHOT small-face drop, and the
  beat text hard-gating the beard does NOT guarantee it renders (2026-08-06, row 9
  b10).** s10-he-meant-it rendered the rich young man clean-shaven even though its
  own must_show/must_not_show demanded "SHORT DARK BEARD present and identical" with
  a CAMERON GATE — the model just dropped it on a small distant face. Beard-board the
  ACTUAL rendered frame against the character ref, never trust the prompt. Fix =
  `--only <beat> --redo` WITH the character REF wired (row 9's RULER lock pulls the
  bearded ruler-ref) — one reroll restored it. Map "N seconds" to the beat by
  cumulative segment/window duration before touching anything.
- **"the picture at M:SS is dumb / not needed" is a COVERAGE complaint, not a picture
  defect — REMOVE the beat, do NOT reroll it (2026-08-06, row 9 b13).** Rerolling a
  "better" version keeps a picture Cameron said shouldn't exist = complaint stands.
  Delete the beat dict and EXTEND the previous beat's `window` to cover the removed
  span (row 9: b12 67.84-73.49 → 67.84-78.49, b13 deleted). Audio stays byte-identical
  because v2_assemble builds the video track from beat `window` fields while the audio
  track is rebuilt independently from the V1 timeline — AUDIO LOCK still PASSes. This
  also directly answers Cameron's recurring "excessive luxuries / wasting api money"
  theme: fewer pictures = fewer chances for drift, and the removal is $0.
- **"the pictures aren't uniform — different boats / changing crew count / the
  subject wanders" is an AUTHOR boat-lock REBUILD, NOT a runner reroll — PARK it
  $0 (2026-08-06, row 11 storm).** A uniformity complaint (Cameron: "10 pictures of
  4 people in one boat and 10 of 6 in a different boat … some don't have Jesus in the
  boat at all") is NOT fixable by rerolling frames. Root cause is structural: the
  boat and the crew are locked in PROSE only ("the same EIGHT men, same boat") with
  NO reference IMAGE — so every Gemini generation invents a fresh hull and headcount,
  exactly like a face with no REF drifts. Uniformity requires an author to (a)
  generate ONE canonical boat plate, commit it as `PLACE-REF/BOAT.jpeg`, and wire a
  `REF:` line into EVERY hull beat (editing beat content + the lock = HARD-RAIL
  forbidden to the runner), and (b) regenerate ~25 frames (≫ the ≤15% reroll
  budget). Rerolling WITHOUT a wired boat plate just mints 25 MORE different boats
  and ships a cut that repeats the complaint = the worst failure. Correct runner
  move: build a labelled contact sheet, confirm the defect, write a RUNNER PARK +
  AUTHOR REBUILD SPEC in QC.md (boat-lock, EIGHT-man crew = crops never smaller
  crews, subject position-lock, plus any single named-frame identity fix), flip
  AUTHOR-BOARD State→NEEDS-REBUILD with Ready empty, $0. Same shape as the row-10
  audio park: complaint real, but the fix lives one stage upstream.

- **Lock rewritten but per-beat scene text still commands the old defect (row 15
  centurion, 2026-08-07).** Cameron's complaint (sick servant "age keeps changing
  … too grey … partially alive") had already triggered a SERVANT *lock* rewrite
  (eighteen, PALE-BUT-ALIVE, never grey), yet the shipped cut STILL showed a grey
  curly corpse in one frame and a 13-yr-old boy in three others. Root cause: four
  beats' own `scene`/`must_show` text literally said "He is very young … dark curls
  … soft grey" and "the boy … the boy's grey face." **The per-beat scene text
  OVERRIDES the shared lock** — the generator concatenates them, and the concrete
  beat wording wins. A lock fix is not applied until the contradicting beat wording
  is scrubbed too. Runner move on a repeat-complaint of a supposedly-fixed lock:
  grep the offending beats for the exact defect words ("boy", "grey", "curls",
  "child", age words), scrub them to agree with the lock, THEN reroll only those
  frames (char-ref anchored to a good kept frame). 4/41 rerolls, ~$0.54, audio
  byte-identical.

- **"Video stops playing / won't play through the N:NN mark" = a CORRUPT AAC
  PACKET in the mux, and it IS runner-fixable — not a NEEDS-AUDIO park (row 31,
  2026-08-07).** Cameron's complaint "stops playing and will not play through the
  1:59 mark ... i can skip past it and it will play but its not playing correctly"
  is a PLAYBACK/encode defect, NOT a re-voice. Diagnose it, don't guess: run
  `ffmpeg -v error -i <mp4> -f null -`; a corrupt audio packet prints
  `channel element X.Y is not allocated` / `Invalid data found` and stalls the
  browser player exactly where the bad packet sits. Confirm scope: `ffmpeg -v error
  -i <mp4> -map 0:v -f null -` (video clean?) and decode-check every source
  `audio/*.mp3` — if the sources are clean, the corruption is only in the final
  mux. FIX: set `AUDIO_FROM_V1_SEGMENTS = True` and re-assemble — the track is
  rebuilt from the build's own clean mp3s at the extract_beats offsets (byte-
  identical narration content, NOTHING re-voiced), producing a clean AAC encode.
  Proof of fix = the NEW mp4 decodes with ZERO `-v error` output. $0 / 0 rerolls,
  pictures untouched. This is DISTINCT from the audio-park class (pronunciation/
  pacing → re-voice → park); a container/encode corruption is the runner's own
  assembly step, so the runner fixes it.
- **A beat whose `must_not_show` GATE contradicts its own `scene` body is an AUTHOR park, NOT a runner reroll (2026-08-07, row 33 b20 "the nails black").** Row 33's prison-hand beat carried a CAMERON GATE in `must_not_show` forbidding black nails, yet its `scene` body still literally said "the nails black" — so every reroll re-paints them. The runner may not edit locked scene text, so rerolling only burns credits on a self-contradicting prompt. When a reroll target's own scene text PRESCRIBES the very thing an open complaint forbids, PARK NEEDS-REBUILD (author deletes the offending scene phrase, then regenerates that one still), $0. Also: a "Jesus is speaking words not spoken by Jesus" complaint on a righteous/crowd KJV quote is a SPEAKER reassignment (make_narration.py entry JESUS→SCRIPTURE), which fixes the wrong voice AND the wrong red caption in one edit — author/NEEDS-REBUILD, never a runner picture reroll.
- **"Random black spots on hands/fingers/lips" = a localized ink/blemish ARTIFACT, fixed by a targeted image-EDIT pass, not a full reroll (2026-08-07, row 39).** Gemini paints small blue-black ink-like smudges on laborer/tax-collector fingers, nails and occasionally a lip — Cameron reads them as "random black spots." They are cosmetic and localized, so a full `--redo` is the wrong tool (it changes the whole composition and can re-roll the smudge back). FIX: attach the finished frame alone to gemini-3-pro-image with an EDIT-ONLY instruction ("return the SAME photograph, remove ONLY the dark ink smudges on the fingers, keep every other pixel"), write to a `.cand.jpeg`, QC it at zoom AND full-frame (FACE-BOARD: no new figure, no crop/light drift), then promote over the original. ~$0.13/frame, composition and identity preserved, audio untouched → AUDIO LOCK stays byte-identical. Same technique fixes an anatomy read like "2 hands of the same side" — instruct it to correct ONLY the handedness to a natural left/right pair while keeping the pose. Sweep every hand/lip frame of that character in the same pass (touch-once), but only edit the ones that actually carry the defect.
- **"1 guy with 3 hands" / extra-hand anatomy comes from a figure doing TWO hand-actions PLUS holding a prop (2026-08-07, row 40 b26).** When a beat has a person leaning/knocking at a door AND carrying a lamp, Gemini can render a forearm to the forehead + a knocking fist + BOTH hands cupping the lamp = four hands. Cameron reads it as "1 guy with 3 hands." A plain reroll (`--only <beat> --redo`, new seed, same locked char-ref) usually resolves it in one take because the prompt already carries "Every figure has two arms, two hands and one head" — the extra hands were a seed artifact, not a prompt defect. QC the reroll by literally counting arms/hands. ~$0.13, audio untouched. If a reroll keeps re-adding the hand, escalate to a targeted image-EDIT ("keep the SAME photo, give him exactly two arms/two hands: one fist on the door, one holding the lamp").
- **"Floating lamp" = a hand-prop rendered with no support surface when its owner is out of frame (2026-08-07, row 40 b36).** On a person-free door/insert beat that still mentions "the lamp's small light," Gemini often paints the clay lamp hovering in mid-air against the wall/door because nothing in-frame holds it. Cameron reads it as "a floating lamp." A reroll grounds it when the scene has an available surface (a stone doorsill/step at the base of the frame) — the new take rests the lamp on that ledge. QC person-free light-source inserts specifically for "what is holding this object?"; if the answer is "nothing," it's a floating-object defect. ~$0.13, audio untouched.
- **"Captions are messed up / don't match the words" can be a whole-video TIMING drift, NOT a wording defect — and it is runner-fixable in assembly (2026-08-07, row 42).** Cameron: "the captions are messed up multiple times match them up to the words, the correct wordage." The caption TEXT was already correct (each segment's caption == its `timing.json` spoken text). The real bug: `beats_v2.py` still-`window`s had been scaffolded from a STALE `beats.json` written on an OLDER, SHORTER narration timeline (before this row's "REDO: new voice + pacing" re-voice lengthened the audio). The assembler draws CAPTIONS on the LIVE `extract_beats` timeline but places STILLS on `beats_v2.py` windows — so the whole picture-and-caption track ran progressively AHEAD of the voice (0s early → ~12s by the end) and the last still froze ~19s. DETECT: `python3 -c "import extract_beats; d=extract_beats.extract(R); print(d['card']['seg_start'])"` vs the max `beats_v2.py` window-end — good rows agree within ~0.1s; row 42 was off by +12.56s. FIX (assembly-only, no reroll, no re-voice): build a monotonic piecewise-linear A→B time map anchored on the stable per-segment `audio_start`+`spoken_end` pairs (stale beats.json = A, live extract = B), remap every `"window": "a-z"` in `beats_v2.py`, re-assemble → AUDIO LOCK PASS (narration byte-identical). Verify still+caption+word agree at ~7 rendered timestamps + the card. Only the `window` timing metadata changes — never scene text/locks. $0, 0 rerolls.
- **A character's DISEASE/skin texture bleeds onto whoever TOUCHES them at the point of contact (2026-08-07, row 54 b12+b14, the leper).** Cameron: "1:01 looks like Jesus had lepracy on his hand. That is wrong." When a beat's scene text describes the sick person's "ashen scaled skin" AND a healthy figure's hand landing on that skin, Gemini paints the ashen/scaly texture onto BOTH — the healer's hand/forearm picks up the leprosy patches. It ONLY happens in the frames where the healthy hand physically contacts the marked skin (the reach-in-air frame one beat earlier was clean). FIX: targeted image-EDIT pass (row-39 method), repaint ONLY the healer's hand/wrist/forearm as clean healthy skin, keep the patient's marks and every other pixel; a plain reroll risks re-rolling the bleed back and loses the composition. Sweep EVERY contact frame of that healing (touch-once) — count them: reach/hover frames are usually clean, only skin-on-skin contact frames carry it. The disease must live on the patient alone, never on Jesus. ~$0.13/frame, audio byte-identical.
- **A one-off recurring character with `locks` but NO `REFS`/GLOBAL_CAST entry renders TEXT-ONLY, and his face FLIPS shot to shot (2026-08-07, row 52, the synagogue demoniac).** Cameron: "The demoniac face kept changing. Beard to no beard to old man and his looks kept flipping." The beats file even carried a CAST-REF NOTE telling the runner to promote the first accepted face to `CAST-REF-V2/<char>-ref.jpeg` and wire `REFS` — but the A-auto ship skipped it, so every FREEDMAN beat invented a new face (clean-shaven / old-grey / young-stranger). A per-build lock token only auto-attaches an IMAGE if it's in `REFS` (build-local) or `GLOBAL_CAST` (library sheet on disk); a token that is neither is text-only no matter how detailed the LOCK prose — text never holds a face. DETECT before shipping any multi-frame single-character arc: `grep -q 'REFS *=' beats_v2.py` OR the token is in GLOBAL_CAST with a >50KB sheet; if neither, the face is unheld. FIX (C-FIX, no re-voice): pick the 1-2 keeper stills that best match the LOCK, copy them to `CAST-REF-V2/<char>-ref-*.jpeg`, add `REFS={"<TOKEN>":[...]}` (paths relative to the build dir), then reroll ONLY the frames whose face grossly deviates (`--only <beats> --redo`) — the gen log must print `[+N char ref: <TOKEN>]` on each. Keep every non-flipping frame byte-identical; don't chase subtle hair-length drift. The reroll count will exceed the 15% light-QC budget on a heavy single-character story — that's expected for this complaint class (the fix re-anchors a face across many beats); batch them all into ONE re-cut. ~$0.13/frame, audio byte-identical.
- **A complaint asking for ADDED scholarship / references / comparisons / "tell it differently" is an AUTHOR content rebuild, NOT a runner reroll or an audio re-voice (2026-08-07, row 59 feeding-4000 "second feeding").** Cameron's row-59 complaint wanted the narration to establish this as the distinct SECOND feeding, cite that Jesus himself commented on both (Matt 16:9-10 / Mark 8:19-21), and draw the 5-loaves/12-baskets vs 7-loaves/7-baskets comparisons. That is new spoken CONTENT that changes the beat map — the runner may not edit scene text or beat content, and no picture reroll touches it. PARK NEEDS-REBUILD (author rewrites narration, may add 1-2 KJV/comparison beats), Ready empty, $0, pictures + audio byte-identical. Distinct from NEEDS-AUDIO (pronunciation/pacing re-voice of EXISTING words) — this ADDS words, so it is author-domain. Also: a stale "COMPLAINT LEDGER: none open" from an earlier build does NOT mean none open — always re-run `v2_outline.py <row>` at claim time; row 59's complaint was filed AFTER the cut shipped.
- **RECURRENCE of the row-52 face-flip class (2026-08-07, row 55, the withered-hand man) + a profile-arm sub-lesson.** Same root cause as row 52: the beats file carried a CAST-REF NOTE telling the runner to build `CAST-REF-V2/hand-man-ref.jpeg` and wire `REFS`, the A-auto ship skipped it, so the MAN token was text-only and his face flipped across the arc (s03 heavy full-grey beard, s09 elderly long-white beard, s10 a YOUNG dark-haired man — three different people). This is now a CONFIRMED repeat, so make it MECHANICAL: at claim time for ANY row whose story follows one named non-Jesus character across ≥3 legible-face beats, run `grep -q 'REFS *=' beats_v2.py` — if it's absent, the face is unheld and the row WILL flip; build the anchor and wire REFS BEFORE the light-QC pass, not after a complaint. Fix method is identical to row 52 (crop the best keeper to the anchor, wire `REFS={"MAN":...}`, reroll only the wrong-person frames, gen log must show `[+1 char ref: MAN]`, keep matching frames byte-identical, audio byte-identical). SUB-LESSON (the "1:34 mutilated double right arm"): a figure drawn in STRICT side-profile reaching forward can render the near-side arm TWICE — once extended and once fisted at the belt — because both read as the same near shoulder; Cameron reads it as a doubled/mutilated arm. The anchored reroll fixed it in one take (the char-ref stabilizes the body plan); QC any profile reach-frame by counting arms on the near side.

- **Mother/family two-shots read ROMANTIC when the scene text pulls faces together (row 49 C-FIX).** "a hand's breadth from her son's", "the two faces stay close", "one hand risen toward her shoulder" produced a lover-like forehead-to-forehead / near-embrace between Jesus and his mother Mary — Cameron flagged it "weird". For any mother/son (or non-couple) beat, state a NATURAL, RESPECTFUL arm's-length and add must_not_show "faces not close, no touch, no romantic/intimate framing."
- **"Lamp/flame reflected ON a liquid surface" paints a flame INSIDE the cup (row 49 C-FIX).** b29's "the strung lamps' small flames riding its moving surface" rendered a lit candle-flame floating in the wine. For close-ups of liquid in a vessel, describe a soft even ambient light (NOT "glow" — drift-word) and must_not_show "NO flame, candle, wick, ember or bright point of light on or inside the liquid."
- **The V2 green-eyed Jesus lock can render as a flat pale-green STARE on a frontal, well-lit face (row 60 C-FIX).** b28's after-picture had Jesus frontal and lit; the lock's intended "green-amber-gold luminous" iris drifted to a washed-out pale-green that reads like colored contacts / a hunted stare — Cameron: "Jesus eyes do not look good." Do NOT edit the shared lock (v2_prompt.py). Reroll ONLY the offending frame; a downcast or three-quarter Jesus gaze in aftermath/after beats reads as warm depth instead of a stare. Spot-check the other Jesus close-ups first to confirm the drift is isolated to one frame (it was — every other close-up was already warm).
- **The JESUS LOCK v5 "eyes lit from within like a flame of fire" over-renders as GLOWING LIGHT-EMITTING EYES in high-radiance beats — reads as demonic (row 67 C-FIX, the Transfiguration).** Cameron: *"0:37 that picture is bad because jesus's eyes turned into light… looks like a demon."* In ordinary beats the lock's eyes render fine, but on a transfigured / blazing-white / glory beat the model amplifies "flame of fire" into literal glowing white-blue orbs. Do NOT edit the shared lock (v2_prompt.py). At claim time on ANY row with a transfiguration/glory/radiance beat, QC every Jesus face for glowing eyes and reroll the offending frame(s) — the brightness must stay on the RAIMENT and a face bloom, never the eyeballs. Sweep ALL radiance frames, not just the complained timestamp (row 67 had it in TWO frames, 0:14 and 0:37 — only the second was reported). WATCH the reroll: on this row the b07 reroll re-introduced the old cartoon tent-doodle Law-14 fail (its scene text says "hands sketching three tent-shapes in the air"), needing a second reroll — always re-QC a reroll for a NEW defect, don't assume the fix is clean.

- **A COMBINED complaint (picture drift + "the message isn't giving the fullness / teach it differently") is a WHOLE AUTHOR REBUILD, not a picture-only C-FIX — do NOT get lured into rerolling just the faces (2026-08-07, row 73 "this day fulfilled").** Cameron flagged BOTH that the first two Jesus pictures "look one way and then another" AND that the narration only reports the event ("he still reads it the same") instead of teaching the fullness — that Jesus meant every word, has risen, and continues the same plan today, framed the way the prophets/restored Church would teach it (without naming the church). The message half is RUNNER-LESSONS §511 author-content-rebuild; it changes the beat map, so the runner cannot touch it. Rerolling only the two drifting faces would ship a cut that STILL repeats the message complaint — the worst failure. When the dominant thrust is message/teaching, PARK the WHOLE row NEEDS-REBUILD and hand the author BOTH parts (the rebuild regenerates the opening stills, curing the face drift for free), $0, pictures+audio byte-identical. Rule of thumb: if ANY part of a complaint requires new/changed spoken content, the whole row is author-domain even when it also names a picture defect.

- **"This is the OLD pictures version, I don't know why I'm seeing it as fixed" is a REVIEWER DELIVERY / CACHE bug, NOT a picture defect — verify the mp4 before spending a single credit (2026-08-07, row 110 lords-prayer C-FIX).** Cameron filed this AGAINST the realistic-v2 ship's own hash. Extracting frames from the committed mp4 proved it was already fully realistic (olive-grove prayer, locked Jesus, realistic forgiveness scene) — the pictures were never the problem. ROOT CAUSE: every reviewer card streamed video from `https://github.com/noremacttevol/MBM/raw/main/<path>?v=<hash>`. That github.com/raw URL 302-redirects to `raw.githubusercontent.com` and **STRIPS the `?v=` query on the redirect** (`curl -sI` shows the `location:` header with no query). So the cache-buster the generator relied on did nothing — the browser cached the bare-path mp4 from BEFORE the ship and re-served the stale OLD cut every time Cameron reopened the reviewer. DETECT: `curl -sI "<github.com/raw URL>?v=x" | grep -i location` — if the location drops the `?v=`, the buster is dead. FIX ($0, no reroll, no re-voice, sweep ALL rows — it's systemic): point every `data-src` at the DIRECT host `https://raw.githubusercontent.com/noremacttevol/MBM/main/<path>?v=<hash>` (no redirect → `?v=` survives as a real browser+CDN cache key → a new hash always misses cache and fetches the current bytes). Also fix the generator (`media-production/gen_site_index.py` RAW_BASE line 30) so a regen can't reintroduce it. Verified: the direct URL returns HTTP 200, no redirect, exact content-length. This is the one complaint class where the correct action is to VERIFY-then-fix-delivery, never reroll — a reroll would burn credits re-making pictures that were already correct and would NOT fix what Cameron saw.
- **Head/face pressed THROUGH a barred cell grate (row 107 C-FIX, s05 "the two messengers at the cell door's grate").** A beat that puts a prisoner "close to the bars" speaking through the grate can render with the face + both hands jammed INTO the small barred window so the head reads as poking THROUGH the metal bars ("weird" — Cameron). Reroll for a composition where the prisoner is clearly BEHIND/inside the bars, face BESIDE the barred panel, hand on the bars — not through them. Watch the swing-back: a reroll can over-correct and stand the prisoner FREE in the corridor with the visitors (row 107 take 1) — the prisoner must stay visibly imprisoned. Do NOT edit the beat text (the scene already says "close to the bars"); it is a render-composition defect a reroll fixes.
- **A QC-named "person-free" promote-first plate can be authored to CONTAIN a distant figure — verify the beat's SCENE TEXT before promoting, and NEVER promote a Jesus-bearing frame (2026-08-07, row 51 BOATS/LAKE).** Row 51's author QC said "BOATS from b02 (person-free)," but b02's own scene text authors in "the crowd around the distant teacher" — a distant cream Jesus — so the render is NOT person-free, and b01 (the LAKE candidate) is Jesus+crowd. `v2_stash.py --promote` copies the WHOLE frame (distant figure and all) and wires it to every beat of that place, and the auto-`--wire` path explicitly refuses Jesus frames (`if not e["jesus"]`) for exactly this reason — a promoted distant cream figure becomes a spurious second-cream-robed figure across the place's frames. You may not edit scene text to strip the figure (hard rail). So: before promoting, `grep`/read the candidate beat's scene text; if it authors ANY figure (esp. Jesus/cream) into the plate frame, do NOT promote it — leave that place on its text lock and QC uniformity by eye. Log the decision in QC.md; it is not a defect, it is a forced no-promote.
