# QC / RUNNER HANDOFF — build-71-the-great-commission

## ✅ C-FIX SHIPPED — Opus runner, Machine A `Dev`, 2026-08-11

**COMPLAINT LEDGER — Cameron's own words (`v2_outline.py 71`):**
> Jesus said: "and, lo, I am with you always, even unto the end of the world"
> not "alway". 1:37 a man has a white tear and that needs to get fixed.

Two named defects, both PICTURE-domain (audio NEVER touched — AUDIO LOCK PASS,
same SHA256 `c29f8cf…`, byte-identical to the cut Cameron already has). Traced
each against the RENDERED mp4, not beat names:

- **"...always..." not "alway" → the RED jv20 caption (renders at b14 77.7s +
  b15 83.3s, the "Amen" tail).** PROMPT AUTOPSY = **CAUSED.** The caption source
  is the V1 `make_narration.py` SEGMENTS, whose jv20 text carried the archaic
  KJV spelling **"alway"** — the caption engine rendered exactly that word. But
  the shipped ElevenLabs **Chris** audio actually SAYS **"always"**
  (faster-whisper on `audio/jv20.mp3`: *"...I am with you always, even unto the
  end of the world. Amen."*). So Cameron was reading a caption that didn't even
  match what he hears. FIX = declared `TEXT_OVERRIDES = {"jv20": "...always..."}`
  in beats_v2.py (the sanctioned `v2_assemble._text_overrides` path) so the
  caption matches the genuinely-spoken word. **V1 make_narration NEVER edited;
  audio NEVER re-voiced — byte-identical.** VERIFIED in rendered mp4 @83s: red
  bottom-band caption now reads "…I am with you **always**, even unto the end of
  the world. Amen."
- **"1:37 a man has a white tear" → b18 / s18-not-until-you-fail-always.jpeg
  (window 95.94–99.76, renders at 97s = 1:37).** The grey-bearded disciple
  (Peter) receiving the ALWAYS had a bright, opaque **white painted tear-streak**
  down his right cheek — an unnatural artifact (real tears aren't opaque white).
  PROMPT AUTOPSY = **ALLOWED.** b18's scene asked for Peter's "weathered face
  taking the word with the particular gratitude…" (an emotional face) but its
  must_not_show placed **no ban on a tear**; the emotional framing let the model
  add one and it rendered as a white streak. FIX = added an explicit ban to b18
  must_not_show ("ABSOLUTELY NO painted or white tear, no bright white streak,
  drip or opaque droplet on any cheek; emotion carried by eyes and mouth alone")
  and rerolled s18 once. New frame: Peter's cheek clean, Jesus's gaze on him,
  cream-only-Jesus, ordinary scale, green eyes (JESUS_LOCK_V5) consistent,
  realistic. VERIFIED in rendered mp4 @97s — no tear.

**FULL-CUT GATE 6b (all 21 beats + card, one frame per beat from the RENDERED
mp4):** CLEAN. Verified: empty-cross off-screen crucifixion (b01), no-wire tomb
(b12), cream-only-Jesus every appearance, ordinary Jesus scale in every
multi-figure frame, green eyes consistent across all Jesus close-ups (b07/b10/
b17 — this is the intended `JESUS_LOCK_V5` "luminous green" standard, NOT drift,
so untouched per COST LAW), prior-C-FIX rerolls still good (b16 upright group,
b20 soft leather scripture, b21 ancient dirt-path descent), captions bottom-band
3-colour correct (white narrator / red jv18-jv19-jv20 Jesus), question card
clean. No modern object, no 2nd cream figure, no anatomy fail, no lens-stare.

**COST:** 1 reroll / 21 beats = **4.8%** (well under the 15% budget) + 0
portraits = 1 image ≈ **$0.13**; meter $599.92→$600.05. Touch-once: both open
complaint items batched into ONE re-cut. Trends the running average DOWN.

---

## ✅ C-FIX SHIPPED — Opus runner, Machine A `Dev`, 2026-08-07

**COMPLAINT LEDGER — Cameron's own words (`v2_outline.py 71`):**
"1:26 has a person sideways, 1:51 the scroll the guy is passing is stiff and
open scrolls of paper are not stiff, the last picture w t1:57 makes no sense
and leaves people confused."

Three named picture defects, each fixed by rerolling ONLY that frame (audio
untouched, byte-identical — same SHA256 c29f8cf…, AUDIO LOCK PASS):

- **1:26 "a person sideways" → s16/b16 (n5, "Teach them not just to hear it").**
  The old cut had a figure lying horizontal across the top-left frame edge (a
  broken sideways body). Rerolled once → a legible close group of upright
  disciples around a table, every figure vertical with correct anatomy, no
  sideways/floating body. VERIFIED in rendered mp4 @87s.
- **1:51 "the scroll the guy is passing is stiff / open scrolls are not stiff" →
  s20/b20 (n6, "It reached across two thousand years").** The old cut showed a
  rigid, board-flat open scroll. Rerolled once → the handoff is now a small,
  soft, worn leather-wrapped scripture (flap and pages fold naturally — nothing
  stiff, no flat open scroll). Matches the beat's "cover soft with carrying."
  VERIFIED in rendered mp4 @111s.
- **1:57 "the last picture makes no sense and leaves people confused" →
  s21/b21 (n6, "That is how far he was willing to send someone").** The old cut
  was a modern-looking aerial drone shot — paved switchback roads and a straight
  shoreline highway (RUNNER-LESSONS §280 defect), tiny black silhouettes. It
  read modern and confusing. Rerolled twice (1st landed a stray pale/cream lead
  figure — off-spec since only Jesus wears cream; 2nd is clean) → a grounded
  hillside view of the eleven in earth-tone robes walking an ANCIENT DIRT
  FOOTPATH down toward the Sea of Galilee in warm light; no modern road, no
  highway, no cream-robed non-Jesus figure. Reads clearly as "the going out."
  VERIFIED in rendered mp4 @116s.

**Cost:** 4 image gens across 3 beats (b16×1, b20×1, b21×2) @ ~$0.134 ≈ **$0.54**.
Touch-once: all three open complaint items batched into ONE re-cut. Captions
bottom-band only, question card clean (verified @125s). Realistic-only (Law 14)
held on all three rerolls — zero cartoon/mixed frames.

---

Complaint-gate addendum, 2026-08-05 (Machine A).

## OPEN CAMERON COMPLAINT — gates before build

"I cant tell if this were remade with the correct references for the
characters or not. Lets just redo the ones with the important
characters that we have."
CAST-REFERENCE PROOF: every important character (Jesus + each named
disciple) must be generated WITH their canonical reference attached
and then face-boarded against that same anchor — and the face-board
result goes in the build folder so Cameron can SEE it was done with
the right references. Any frame whose character cannot be matched to
their canon anchor gets regenerated with the reference.

---

## ✅ RUNNER BUILD — A-auto Machine A, 2026-08-06 (SHIPPED)

**COMPLAINT LEDGER (open complaints from `v2_outline.py 71`):**

- **"I cant tell if this were remade with the correct references for the
  characters or not. Lets just redo the ones with the important characters
  that we have the reference for now."**
  → FIXED. Every one of Jesus's 11 frames (b03,b04,b05,b06,b07,b09,b10,b13,
  b14,b17,b18) was generated with the locked V2 Jesus face reference attached
  (`v2_gen_api` logged `[face lock]` on each). Face-boarded across all 11: one
  actor — same face, full dark beard (beard board / lesson 13 PASS), shoulder-
  length dark wavy hair, warm olive skin, cream wool robe every frame, and ONLY
  Jesus wears cream. Scale gate (lesson 14) PASS: Jesus is an ordinary-sized man
  in every multi-figure frame (b04/b05/b06/b13/b14/b18) — never a giant.
  Recurring disciples (Peter = older grey-beard, John = young helper) read
  consistent across the group beats. The rebuild WAS done with the locked
  references, and the face-lock log + this ledger are the proof.

**Coverage:** 21 realistic stills, native 2K. Movie coverage (lesson 12): singles
(Jesus close-ups b07/b10/b17), two-shots (b14/b18 shoulder-touch), inserts
(b12 tomb, b20 scroll handed on), one establishing wide (b02 the eleven
climbing), plus the going-out descent (b19/b21). Off-screen law honored: b01
three EMPTY crosses far under storm-dawn, no bodies; the adversary/Father never
depicted. Godhead named plainly in b13 (three fingers). Direction arc closes:
b02 UP the mountain → b19/b21 DOWN toward the sea/world.

**Rerolls:** 1 / 21 beats = **4.8%** (well under the 15% COST-LAW budget). Only
reroll: **b12** carried a thin wire-straight line across the misty sky (modern
utility-cable defect, RUNNER-LESSONS row 53) → redo landed a clean rock-hewn
tomb with the disc stone rolled aside, no wire, no modern object.
FIX-WAVE (kept, not garbage): b21 faint winding roads in the far aerial
landscape (subtle background, don't chase — COST LAW).

**Realistic-only (Law 14):** all 21 frames photographic — zero cartoon/CGI/mixed
frames. **Audio:** byte-identical V1 narration, **AUDIO LOCK PASS**
(SHA256 c29f8cf…). Captions verified in the RENDERED mp4: narrator white / Jesus
red (KJV), bottom band only; question card clean.

**Cost:** 21 stills + 0 portraits (cast sheets reused) + 1 reroll @ ~$0.134
≈ **$2.95** — under the $6.10 running average; trend stays DOWN (portraits free,
one place generated straight, single reroll).
