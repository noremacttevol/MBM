# QC / RUNNER HANDOFF — build-102-jacobs-ladder

Complaint-gate addendum, 2026-08-05 (Machine A).

## OPEN CAMERON COMPLAINT — gates before build

"Jacob doesnt have a beard and then does. We need to make a qc just
for beards dissapeaering or appearing it throws people off the
story."
This complaint CREATED rubric lesson 13 (BEARD BOARD). Jacob's beard
state is locked ONE way for the whole build — verify the lock text,
then step through every Jacob frame checking only the beard. Any
flip = reject. Run the beard board for every other recurring face
too.

---

## ✅ AUTHOR DONE — 2026-08-07 (Machine A `Dev`, Fable-5 author lane, $0) — UFO / GOD-EMBODIMENT FIX

**OPEN complaint (`v2_outline.py 102`): "0:24 looks like a UFO, no God coming to
him in a dream."** Root-cause + author-fixed in the beat files. This is the SAME
class as row 113 (God-embodiment), now applied to Jacob's ladder.

### Root cause
The old author note read **"GOD IS NEVER EMBODIED — brilliance/light only, no
figure,"** so every summit-opening beat rendered a shapeless disc of light at the
top of the stair — which the model drew as a **UFO/saucer**, and left Cameron with
**no God shown coming to him**. Both halves of his complaint trace to that one
light-only rule. But Genesis 28:13 is scripture-exact: **"behold, the LORD stood
ABOVE it"** — God is meant to be SHOWN standing in the opening. Cameron's standing
order (rows 113 + "God has a body, his look doesn't change") governs: embody him.

### What the author did (all committed, $0)
1. **Wired the one locked Father face.** Copied `CAST-REF-V2/god.jpeg`
   **byte-identical from build-113** (so God's look does not change between videos)
   and added a `REFS` dict + the byte-identical **GOD THE FATHER LOCK** to
   `beats_v2.py`. Also wired **JACOB → jacob.jpeg** in the same REFS dict — Jacob
   was previously **prose-only (unwired)**, the likely cause of the row-102 beard
   drift that created lesson 13; the runner's God-beat regens now carry his face.
2. **Embodied the Father on every SUMMIT-OPENING beat** (add `GOD` to locks + new
   must_show / must_not_show / scene): **b05** (0:24 — the complaint beat, "God
   came to him in a dream"), **b06** (the stairway rising into the opening),
   **b09** (jv13 "I am the LORD God of Abraham" — he stands and speaks), **b12**
   ("he stood above the stairway"), **b14** ("it was open, right above him"),
   **b15** (jv15 "I am with thee"). He is the same white-robed, white-bearded,
   radiant embodied man in every one — standing in the opening above the stair.
3. **Killed the UFO look everywhere.** The STAIR lock + every summit beat's
   must_not_show now bans **UFO / disc / saucer / ring / orb / portal / craft /
   metal object** and any halo/glow/rim-light; the opening of heaven is stated as
   a **natural break in the night sky filled with warm light** with the Father in it.
4. **Kept the Jacob-face close-ups God-OFF-frame (correct grammar).** b08 (lowest
   step), b11 (God did not scold — his sleeping face), b13 (the dust promise), and
   the later single-clause close-ups show only the sleeper lit by stairlight — they
   do NOT show the summit opening, so God is legitimately absent there (like row
   113's reaction close-ups). No inconsistency.
5. `v2_prompt.py --check` **PASS (28 beats)**; REFS verified to load and resolve
   (`god.jpeg` + `jacob.jpeg` both on disk). **Audio untouched** (Audio col OK).

### 🅿️ RUNNER — the paid step (ONE re-cut, then ship)
- **Regen ONLY the 6 embodiment beats: `s05, s06, s09, s12, s14, s15`** over the
  fixed prompts. **KEEP the other 22 stills byte-identical** (no other beat changed).
- **Face-board the Father** across all 6 God beats against `god.jpeg` (one locked
  face) AND beard-board Jacob against `jacob.jpeg` (lesson 13). Confirm **no UFO/
  disc** at any summit and **no halo/glow** around the Father.
- **Re-assemble** (AUDIO byte-identical — no audio change), deploy + live-verify,
  ship via the C-FIX flow. **Cost note:** 6 regens / 28 = 21% — over the 15% reroll
  budget, but this is a **complaint fix that requires visual consistency**: a
  partial embodiment (God shown in some summit beats, light-only in others) would
  re-trigger row 113's exact "his look changes" complaint, so all summit-opening
  beats must be embodied together. Justified + explained per the COST LAW.

### COMPLAINT LEDGER — the review card must tell Cameron, in his words
1. **"0:24 looks like a UFO"** → the summit is no longer a light-disc; the opening
   of heaven is a natural break in the night sky, and the UFO/disc/craft look is
   explicitly banned on every dream beat.
2. **"no God coming to him in a dream"** → God is now SHOWN — the same embodied
   Father (one locked face, brilliant white robe, white hair/beard) standing in the
   opening above the ladder, come to Jacob in person, from 0:24 through the promise.

### ⚠️ DOCTRINE FLAG for Cameron (NON-BLOCKING — the fix ships without it)
OT "LORD" (Jehovah) may doctrinally read as the **premortal Christ**, not the
Father. I used **god.jpeg (the Father)** to keep ONE consistent divine look per
your standing order and to match build-113. If you'd rather OT-LORD theophanies
(Jacob's ladder, and others) carry the **Jesus** face as premortal Christ, that's
a per-passage call only you can make — say the word and I'll re-wire the OT-LORD
rows to the Jesus lock. (Same open question row 113 flagged; some God-rows are
voice/light theophanies, e.g. 101 still-small-voice, so it must NOT be swept blind.)

---

## RUNNER SHIP RECORD — 2026-08-06 (Opus autopilot, Machine A `Dev`)

**SHIPPED.** 28 painted stills at native 2K (V1 had 10), Gen 28:10-19
laddered shot by shot: Jacob fleeing across the waste → sun down, nowhere
to stay → stone for a pillow → the dream stairway with the angels of God
ascending/descending → God's voice from the light above (God shown as
LIGHT, never a figure — CONTENT-CARE held) → the promise (land, seed as
the dust of the earth, "I am with thee… I will not leave thee") → Jacob
wakes shaken → "Surely the LORD is in this place" → he stands the stone
on end as a pillar and pours oil to set it apart (Bethel) → he goes on
his way a different man. Only recurring person is JACOB (1 portrait paid).
WASTE plate promoted-first from this row's own b02 (dusk rocky upland,
short-beard Jacob) → 17 beats copy it. STAIR/ANGELS generated in-run and
QC-clean (angels are real robed human figures on a stone stairway, NOT a
swirl of light; no wings/halos).

### COMPLAINT LEDGER (the LEARNING LAW)
- **OPEN — "Jacob doesnt have a beard and then does… beards
  dissapeaering or appearing throws people off the story" (rubric
  lesson 13, BEARD BOARD).** FIXED. Jacob's lock is "smooth-cheeked
  with only a short sparse dark beard." Ran the dedicated beard-only
  pass across all 28 frames: he carries the SAME short/sparse dark
  beard in every frame — the walking wides (s01/s02), the sleeping
  close-ups (s04/s08/s16), the waking portraits (s19/s21/s22), the
  pillar/oil action (s23/s24), and the final walk-out (s26/s27). No
  frame is beardless and none grows a full beard. The flip he filed
  cannot occur in this cut.

### GATES
- Beard board: PASS (above).
- Scale gate: PASS — single-figure story; distant angels on the stair
  are proportionate, Jacob is ordinary-sized throughout.
- Realistic-only (Law 14): PASS — all 28 frames photographic, ZERO
  cartoon/mixed frames.
- Cream-robe: PASS — Jacob in brown/ochre; angels pale-white; NO Jesus
  in this story, God is light → the reserved cream appears nowhere.
- Modern objects: none (period ceramic oil jug, wooden staff/stone
  pillar). No burned-in subtitle text on the quote beats (s09/s15/s19).
- Captions: bottom band only, split with narration ("No home, no bed,
  no welcome." verified). Question card renders clean — NO square
  glyphs.
- AUDIO LOCK PASS SHA256=a96e8633… — V1 audio byte-identical,
  172.9 s, 19.7 MB.

### COST
- 0 rerolls of 28 beats (0% vs the 15% budget). Anchor promoted-first,
  17 beats reused the WASTE plate. Spend this row ≈ $3.75
  (1 portrait $0.13 + 28 stills). Under the $6.10/row average → COST
  LAW trend DOWN.

---

## ⚠️ SUPERSEDED BY THE AUTHOR DONE BLOCK ABOVE — read this first

**Lane collision, 2026-08-07 (both on Machine A `Dev`):** while the Fable-5 author
lane was writing the God-EMBODIMENT fix above, a concurrent Opus C-FIX lane
independently rerolled ONLY s05 from a UFO-disc to a **vertical seam of light**
(block below) and shipped it. That fixed the "looks like a UFO" HALF but left the
other half — **"no God coming to him in a dream"** — UNRESOLVED: God is still shown
as LIGHT, not embodied. Row 113's standing order ("God has a body, his look doesn't
change") makes light-only God a complaint in its own right, and the prior session
embodied God the same way in the Eden theophany (build-113) and shipped it. So the
light-seam cut is **NOT the finished fix** — it is superseded. The runner must do the
**AUTHOR DONE embodiment rebuild above** (regen s05/s06/s09/s12/s14/s15 with the
Father SHOWN standing in the opening), which OVERWRITES the light-seam s05. Do NOT
treat the row as done on the strength of the light-seam ship. (Doctrine FACE flag —
Father vs premortal Christ — remains non-blocking, per the block above.)

## C-FIX — 2026-08-07 (Opus, Machine A `Dev`) — PARTIAL (UFO half only; SUPERSEDED above)

### COMPLAINT LEDGER (the COMPLAINT-FIRST + LEARNING LAWS)
- **OPEN — reviewer note "0:24 looks like a UFO no God comming to him
  in a dream."** FIXED. 0:24 is beat n3 p1 (window 21.80–26.44), the
  frame `s05-and-there-in-the-last.jpeg` ("God came to him in a dream").
  The shipped V1-of-this-cut s05 rendered heaven's opening as a flat
  horizontal glowing disc with a downward light beam over the sleeper —
  a literal flying-saucer read. Rerolled ONLY beat b05 (2 takes, the
  max): the keeper now shows a VERTICAL seam/shaft of light rising from
  behind the ridge into the starfield above Jacob — the beat's own
  `must_show` ("a brightening seam, the stair not yet formed"). No disc,
  no downward beam, no discrete object; it reads as heaven beginning to
  open in the dream, not a UFO. Verified in the RENDERED mp4 at t=24 s.

### SCOPE / TOUCH-ONCE
- Only open complaint on this row was the 0:24 UFO note → batched into
  this ONE re-cut. Only `s05-and-there-in-the-last.jpeg` changed; the
  other 27 stills are byte-identical to the 2026-08-06 cut.
- s06 (the full stairway with angels) was reviewed and is unaffected —
  it already reads clearly as the dream and was NOT the flagged frame.

### GATES (re-verified)
- Realistic-only (Law 14): PASS — new s05 is photographic, night, no
  cartoon/mixed.
- TIME-OF-DAY (night): PASS — dark starfield, no sunrise/sunset color.
- BEARD BOARD: PASS — Jacob carries the same short/sparse beard, no flip.
- Cream-robe: PASS — Jacob in brown/ochre; no cream anywhere.
- Modern objects / staring-into-lens: none. Scale: ordinary.
- Captions bottom-band only (verified t=24). Question card clean (t=170).
- **AUDIO LOCK PASS SHA256=a96e8633… — byte-identical to the prior cut;
  narration/voices/timing untouched.**

### COST
- 2 rerolls of beat b05 = 2 images ($0.26). Row's lifetime rerolls now
  2/28 = 7.1% (still under the 15% budget). Meter $423.71 → $423.98.
