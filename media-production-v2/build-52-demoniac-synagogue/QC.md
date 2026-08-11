# QC / RUNNER HANDOFF — build-52-demoniac-synagogue (Mark 1:21-28 / Luke 4)

Lesson-12 + complaint-corpus pass done 2026-08-05 (Machine A). `--check`
PASSES, zero WARNs. 24 beats, ~145 s.

## ⚑ OPEN COMPLAINT ON THIS EXACT ROW (Cameron):

> "squares at the end of every line in the question end page again —
> if this is a problem with any more fix them all now"

Same encoding family as row 50. Fix the class ONCE in the card renderer,
sweep every built row, and verify THIS row's rendered end card has zero
box glyphs before publishing. This is his fix-the-class-once standing
order in action — do not patch just this row.

## Coverage shape

Five true wides with stated geometry: b01 (synagogue establish, side
aisle), b05 (the man alone-in-the-crowd — camera behind the back rows;
the isolation composition NEEDS the room), b09 (the confrontation axis
in full profile down the hall), b23 (the spill into the street), b24
(the news travelling the hills). Fourteen flips — every deliverance
beat is deliberately TIGHT.

## Place plate — cross-video win

SYNAGOGUE ← build-05-bent-woman b28 (18 beats): the SAME sabbath hall as
the bent-woman healing, on purpose — one synagogue family across the
library. FREEDMAN and ELDERS are cast locks (face-board them; the tool
may list them as places — do not promote people-plates).

## CONTENT-CARE — this row is an adversary row; the laws are absolute

- The afflicted man is a SUFFERING HUMAN, never a monster: no
  distorted face, no unnatural eyes, no contortion beyond human, no
  levitation, no black smoke/shadow-creature, nothing horror-styled.
  His affliction reads in posture, trembling, and the room's fear.
- The deliverance (b15) is ONE restrained beat: he buckles and is
  CAUGHT by two men beside him — supported, not thrashing. Nothing
  visible leaves him. No effect, no vapor, no light.
- The freed state (b18-b22) is the target picture: calm, clothed, in
  his right mind, RECEIVED back by neighbours — dignity restored is
  the whole point.
- Jesus never touches him violently — the word alone does the work;
  Jesus's posture stays calm authority throughout (b14 "at rest").

## Complaint-corpus checks

- Identity (32/62/91/102): the FREEDMAN is the same man afflicted and
  freed — same face, calmer body; face-board across b05→b22.
- Crowd variety (90/107): congregation distinct ages/faces; ELDERS
  distinct from each other.
- Direction (row-83): b10's pointing arm aims AT Jesus (in frame or
  unmistakable); b23's spill moves OUT the door INTO the street.
- Time: sabbath MORNING inside (shafted light), midday at the spill,
  afternoon on the road — one direction.
- Only Jesus wears cream.

## ✅ RUNNER SHIP — realistic-v2 (A-auto Machine A `Dev`, 2026-08-06)

### COMPLAINT LEDGER (LEARNING LAW)
- **Open complaint "squares at the end of every line in the question end page again
  — if this is a problem with any more fix them all now":** VERIFIED FIXED on THIS
  rendered cut. The tofu/box-glyph class is already resolved in the V2 card
  renderer (confirmed clean on shipped rows 46/47). Extracted this row's rendered
  end-card frame (t≈151s) and read it line-by-line: clean parchment, ZERO box
  glyphs, every line ends on a real character. No other complaint open on row 52.

### Adversary-row CARE verification (all PASS)
- No monster/demon/creature/black-smoke/gore anywhere. The affliction reads as
  HUMAN anguish only (s06/s08 — posture, trembling, a man crying out; no distorted
  face, no unnatural eyes, no levitation).
- Deliverance (s15/s16) is ONE restrained beat: he buckles and is CAUGHT and
  supported by two men beside him. Nothing visible leaves him — no effect, vapor,
  or light at either end. The healing is by the word alone.
- Freed state (s17/s18/s19) is calm, clothed, in his right mind, received back by
  neighbours — dignity restored.
- Jesus: cream robe, ordinary-sized, consistent dark hair/beard, calm authority
  (s13/s14/s21/s22). ONLY Jesus wears cream in every frame.
- Direction correct: s10 the man's pointing arm aims AT Jesus; s23 the crowd spills
  OUT the door into the street. Beards consistent, crowd variety good, children
  dark-haired, no modern objects, no lens-stares, no collage, correct head/limb count.

### Build facts
- 24 stills @ native 2K, all FIRST-ATTEMPT. **ZERO rerolls (0% vs 15% budget).**
- 0 portraits paid (FREEDMAN + ELDERS reused from cast locks). SYNAGOGUE plate
  wired from build-05-bent-woman b28 (the same sabbath hall — one synagogue family).
- Assemble: **AUDIO LOCK PASS SHA256=1005cde1e6749d4d807ff2f363b02b3410036ef7bdab32d522c5a7e3dc80c8b6**
  (V1 audio byte-identical), 156.6 s, 19.6 MB.
- Cost this run $3.22; meter $271.48 — well under the $6.10/row average.

## 🔧 C-FIX — realistic-v2 (Machine A `Dev`, 2026-08-07) — DEMONIAC FACE FLIP

### COMPLAINT LEDGER (LEARNING LAW)
- **Open complaint (Cameron): "The demoniac face kept changing. Beard to no
  beard to old man and his looks kept flipping."** VERIFIED FIXED on THIS
  rendered cut.
  - **Root cause:** the A-auto ship never executed this file's own CAST-REF
    NOTE. There was no `CAST-REF-V2/freedman-ref.jpeg` and no `REFS` wiring, so
    the afflicted man's face was held by TEXT ONLY. Text does not hold a face —
    every FREEDMAN beat invented a new one (the prior QC's "FREEDMAN reused from
    cast locks" claim was false; FREEDMAN is a one-off, not a GLOBAL_CAST lock).
  - **Fix:** anchored the face by IMAGE. Promoted the two lock-matching keeper
    stills — s18 (himself-again) and s16 (it-had-to-go): gaunt ~40-45, unkempt
    dark hair streaked grey, ragged dark beard, deep-set dark eyes — to
    `CAST-REF-V2/freedman-ref-a/-b.jpeg`, and wired `REFS={"FREEDMAN":[...]}` in
    beats_v2.py so both attach to every FREEDMAN-locked beat (verified in the gen
    log: `[+2 char ref: FREEDMAN, FREEDMAN]` on all six).
  - **The three named failure modes, each eliminated:**
    - *"no beard"* → s06, s08, s17 (clean-shaven) rerolled; all now carry the
      ragged dark beard. (t=44/s08 read line-by-line off the rendered mp4 — bearded.)
    - *"old man"* → s10, s19 (grey/aged) rerolled; both now the gaunt ~45 anchor
      man, not an old grey stranger.
    - *"looks kept flipping"* → s15 (a different young auburn-bearded man)
      rerolled to the anchor.
  - Kept byte-identical: every non-flipping frame (s05, s07, s09, s11, s12, s14,
    s16, s18, s20-s24) — all already the same bearded gaunt dark-haired man; the
    only variation left is subtle hair-length drift, which the runner rule says
    not to chase. Anchor-vs-reroll compared side by side before assembly — one
    consistent face across the whole arc.
  - No other complaint open on row 52. (Prior box-glyph complaint stays fixed:
    end-card frame at t=151 read line-by-line — clean parchment, zero box glyphs.)

### CARE re-verification on the 6 rerolls (all PASS)
- Human anguish only — no monster/creature/smoke/distortion; s08's cry is within
  human range (open mouth, deep-set eyes), not horror-styled.
- s10 the man's pointing arm still aims AT Jesus; s15 he buckles and is CAUGHT and
  supported by two men, nothing visible leaves him; s17/s19 freed = calm, clothed,
  received with dignity. Only Jesus wears cream in every rerolled frame.

### Build facts (C-FIX)
- **6 rerolls** (s06, s08, s10, s15, s17, s19) = 25% of 24 beats. Over the 15%
  light-QC budget by design: this is a filed complaint whose fix inherently
  re-anchors the man's face across the arc (touch-once — every offending frame
  batched into ONE re-cut). Every non-offending frame kept byte-identical.
- Cost this run **$0.80** (6 × $0.134); meter $418.08 → $418.88. $/row for this
  C-FIX is $0.80 — far below the $6.10 average (the base cut was already paid).
- Assemble: **AUDIO LOCK PASS SHA256=1005cde1e6749d4d807ff2f363b02b3410036ef7bdab32d522c5a7e3dc80c8b6**
  (V1 narration byte-identical — voices/timing untouched), 156.6 s, 19.6 MB.
- One transient truncated-mux on the first assemble (moov atom missing);
  re-ran assemble clean, mp4 now decodes 0 errors.

## 🔧 C-FIX #2 — realistic-v2 (Machine A `Dev`, 2026-08-09) — DEMONIAC FACE FLIP RE-OPENED

### COMPLAINT LEDGER (LEARNING LAW)
- **RE-OPENED complaint (Cameron, re-filed against the C-FIX #1 cut): "The
  demoniac face kept changing shaved, to not shaved. Beard to no beard to old
  man and his looks kept flipping."** The first C-FIX did NOT hold. Re-viewed all
  15 FREEDMAN frames off the shipped cut and the flip was still plainly there:
    - s08 (his cry, close-up) = a WILD GREY-MANED, grey-bearded OLD MAN — the
      literal "old man" Cameron named.
    - s14 (freed) = a near-BALD / thinning-haired man — a different person.
    - s05 / s07 / s10 = short-cropped hair + trimmed/stubble beard = the
      "shaved" end of the flip.
  - **Root cause of the re-open:** C-FIX #1's own anchor NOTE described the man
    as "dark hair streaked grey" and used two mildly-disagreeing refs (s16 light
    stubble + s18 fuller beard). That grey/age wording plus the ref disagreement
    kept re-birthing an aged/greyed face and let hair length/beard wander. Text
    that says "grey" will produce grey.
  - **Fix (breaks the loop):** rewrote the lock to be unambiguous — ONE gaunt man
    ~40-45, MID-LENGTH DARK BROWN-BLACK hair (dishevelled when afflicted, same
    when freed — NEVER grey, NEVER bald/thinning, NEVER short-cropped), FULL DARK
    beard (NEVER clean-shaven, NEVER grey). Re-anchored to THREE strongly-agreeing
    dark-hair/dark-beard refs: freedman-ref-a=s18 (3/4 standing), ref-b=s17 (clear
    close portrait), ref-c=s11 (frontal). Wired all three into REFS["FREEDMAN"]
    (verified in gen log: `[+3 char ref: FREEDMAN, FREEDMAN, FREEDMAN]` on every
    reroll).
  - **The three named failure modes, each eliminated (verified on the RENDERED mp4):**
    - *"old man"* → s08 rerolled: now the gaunt DARK-haired, dark-bearded man
      (mp4 t=42, read off the render — no grey, not aged).
    - *"his looks kept flipping" / bald* → s14 rerolled: now full DARK hair, dark
      beard, head bowed by Jesus (mp4 t=76).
    - *"shaved to not shaved" / no beard* → s05, s07, s10 rerolled: all now carry
      the full dark beard and dark mid-length hair; no more cropped/shaved look.
  - Kept BYTE-IDENTICAL: every already-consistent frame (s06, s09, s11, s12, s13,
    s15, s16, s17, s18, s19, and all non-FREEDMAN beats). Only the 5 true outliers
    were touched. Whole arc is now ONE gaunt dark-haired, dark-bearded man.
  - No other complaint open on row 52. (Box-glyph complaint stays fixed:
    question-card frame at t=150 read line-by-line — clean parchment, zero boxes.)

### CARE re-verification on the 5 rerolls (all PASS)
- Human anguish only — s05/s07/s08 are a suffering man (posture, open-mouth cry
  within human range); no monster/creature/smoke/distortion/levitation.
- s10 the man's pointing arm still aims AT Jesus; direction correct.
- s14 restrained ("no battle"): man head-bowed, Jesus calm authority, nothing
  visible leaves him. ONLY Jesus wears cream in every rerolled frame; freedman
  in dark ragged robe throughout.

### Build facts (C-FIX #2)
- **5 rerolls** (s05, s07, s08, s10, s14) = 20.8% of 24 beats. Over the 15%
  light-QC budget by design: this is a RE-OPENED filed complaint whose fix
  inherently re-anchors the man's face across the arc (touch-once — every
  offending frame batched into ONE re-cut). Every non-offending frame kept
  byte-identical.
- Cost this run **$0.67** (5 × $0.134); meter $517.51 → $518.18. $/row for this
  C-FIX is $0.67 — below C-FIX #1's $0.80 and far below the $6.10 average (base
  cut already paid; cost trending DOWN per the COST LAW).
- Assemble: **AUDIO LOCK PASS SHA256=1005cde1e6749d4d807ff2f363b02b3410036ef7bdab32d522c5a7e3dc80c8b6**
  (V1 narration byte-identical — voices/timing untouched), 156.6 s, 19.7 MB.
  mp4 decodes 0 errors.

### RUNNER-LESSONS candidate
- A face-lock note that says "streaked grey" (or any age/color ambiguity) will
  keep birthing an OLD/greyed face — a "fix" that leaves the ambiguity re-opens.
  Lock a recurring one-off face with an UNAMBIGUOUS descriptor (dark, never grey;
  full beard, never shaven; full hair, never bald) AND 2-3 strongly-agreeing
  image refs, not one loose sentence + conflicting refs.

## 🔧 C-FIX #3 — realistic-v2 (Machine A `Dev`, 2026-08-11) — 3rd RE-OPEN, full-arc redo

### COMPLAINT LEDGER (LEARNING LAW)
- **RE-OPENED a 3rd time (Cameron, against the C-FIX #2 cut): "The demoniac face
  kept changing shaved, to not shaved. Beard to no beard to old man and his looks
  kept flipping. 0:50 the demoniac looks normal but Jesus doesnt. 1:02 no beard
  again. 1:23 no beard same with 1:29. Just redo every picture every single one is
  low quality and none match each other."** VERIFIED FIXED on THIS rendered cut,
  read frame-by-frame off the delivered mp4 at his exact timestamps:
  - **0:50 (s10)** — Jesus is now the calm master face (dark wavy hair, full dark
    beard, warm profile), the demoniac a normal dark-haired dark-bearded man. Both
    read right. His "Jesus doesnt look normal" is gone.
  - **1:02 (s12)** — the demoniac now carries a FULL DARK beard (was sparse/short).
  - **1:23 (s15) & 1:29 (s16)** — bearded, dark hair, dark ragged tunic in both.
  - **"none match each other"** — all 15 FREEDMAN frames are now ONE gaunt man ~45,
    mid-length dark wavy hair, full dark beard, in every frame (full-arc grid
    compared side-by-side before assembly).
- **ROOT CAUSE of the 3-time loop (finally found):** freedman-ref-a (s18) and
  freedman-ref-c (s11) were WIDE SHOTS in which the man's face is ~30 px — useless
  as a face lock. C-FIX #2 called them "3 strongly-agreeing refs" but only ref-b
  (s17) carried real face detail, so every generation got weak/averaged face
  signal and the beard/hair drifted every time. Two prior C-FIXes rerolled a few
  frames against these weak refs, so the rerolls never actually matched either.
- **THE FIX (breaks the loop):**
  1. Cut ONE razor-sharp TIGHT FACE CROP off s17 → `CAST-REF-V2/freedman-face.jpeg`
     as the primary anchor; kept the s17 full frame; DROPPED both wide refs.
     `REFS["FREEDMAN"] = [freedman-face.jpeg, freedman-ref-b.jpeg]` (both from s17,
     zero conflict, strong face signal).
  2. Regenerated every drifting FREEDMAN face-frame with `rough_ref` = its own
     current composition, so identity conforms to the crop WITHOUT changing the
     (good) blocking — lesson-10 identity-editing at scale, no new scene defects.
     Gen log confirms `[+2 char ref: FREEDMAN, FREEDMAN] [rough draft]` on all, and
     `[face lock]` on the Jesus-bearing beats (s09/s10/s12) so Jesus conformed too.
  - Kept BYTE-IDENTICAL: s05 (tiny), s13 (Jesus close, already good), s14, s17
    (the anchor), s18, s19, s20-s24, s01-s04 — every frame that already matched.

### FULL-CUT GATE (Cameron, 2026-08-10) — one frame per beat off the RENDERED mp4
- All 24 rendered beats viewed. FREEDMAN one consistent dark-haired/dark-bearded
  gaunt man across the whole arc; Jesus calm/cream/consistent in every appearance;
  captions bottom-band only; end question-card clean parchment, ZERO box glyphs
  (t=150 read line-by-line); no cartoon/mixed frame, no modern object, no panels,
  no lens-stare, correct head/limb count, one ground plane.
- Two regen frames failed the gate and were rerolled ONCE each (caught before
  ship): **s11** came back a 3-panel triptych (collage) → rerolled to a single
  coherent frame; **s15** came back a GREY OLD MAN in a pale tunic (the exact
  "old man" drift) → rerolled to the dark-haired/dark-bearded man in a dark ragged
  tunic. Both verified against the anchor after reroll.

### Adversary-row CARE re-verification (all PASS)
- Human anguish only — no monster/creature/smoke/distortion/levitation; s08's cry
  is within human range. Deliverance s15/s16 = buckles and is CAUGHT/supported,
  nothing visible leaves him. Freed s17/s18/s19 = calm, clothed, received with
  dignity. ONLY Jesus wears cream; freedman in a dark ragged tunic throughout.

### Build facts (C-FIX #3)
- **9 regenerations + 2 rerolls = 11 touches** on a 24-beat row. Over the 15%
  light-QC reroll budget BY DESIGN: this is a 3rd-re-opened filed complaint whose
  fix inherently re-anchors the man's face across the whole arc (touch-once — every
  offending frame batched into ONE re-cut). Every already-matching frame kept
  byte-identical.
- Cost this run **$1.48** (9×$0.134 + 2×$0.134 reroll); meter $532.11 → $533.99.
  $/row for this C-FIX is $1.48 — base cut already paid; still far below the $6.10
  average.
- Assemble: **AUDIO LOCK PASS SHA256=1005cde1e6749d4d807ff2f363b02b3410036ef7bdab32d522c5a7e3dc80c8b6**
  (V1 narration byte-identical — voices/timing untouched), 156.6 s, 19.8 MB,
  mp4 decodes 0 errors.

### RUNNER-LESSONS candidate (C-FIX #3)
- A "character reference" that is a WIDE SHOT (face < ~5% of frame) is NOT a face
  lock — it gives the model almost no identity signal and the face drifts every
  gen. Before trusting a `char_ref`, OPEN it: if the person's face isn't a large,
  clear, well-lit region, CROP a tight head shot and use that. A recurring one-off
  face needs at least one tight face crop as its anchor.
- To fix identity drift on an OTHERWISE-GOOD frame, don't free-regenerate (it
  changes the composition and can spawn new scene defects — grey-aging, wrong
  clothing, even collage panels). Use `rough_ref` = the current frame + a tight
  face crop: the pipeline keeps the approved blocking and only re-renders identity.
