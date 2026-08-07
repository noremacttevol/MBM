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
