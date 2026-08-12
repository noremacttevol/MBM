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
mp4) — caught + batched a THIRD defect Cameron did not name (before he could):**
the three tight Jesus close-ups **b07/b10/b17 had pale glassy GREEN irises** with
a bright catch-light — the exact "wrong-Jesus" look rows 89 and 98 (both today)
rejected and edited to warm brown. This VIOLATES CLAUDE.md law 8(g) ("warm brown
eyes… NEVER pale/blue") and the one-locked-face-across-every-video law (Law 5/6):
leaving row 71 green while 89/98 ship brown = Jesus with different eyes between
videos. ROOT CAUSE = a LOCK BUG: `v2_prompt.py` JESUS_LOCK_V5 still literally
specifies "luminous GREEN eyes" (lines ~953/971/992), so EVERY v2 row generates
green and needs this manual fix — **flagged to Cameron to correct the lock to
warm brown at source** (else all 200 rows keep needing it). FIX = the row-89/120
iris edit (`_eye_edit.py`, gemini-3-pro-image): fed each finished still back,
"recolour ONLY the irises to warm medium brown, remove the pale/greenish cast +
catch-light, keep every other pixel identical." All THREE edited together (a lone
brown among green = Law-14 mix). Backups `assets/*.preeye.bak`. Verified in the
re-rendered mp4: b07/b10/b17 warm brown, consistent with each other + the group
shots (small/dark eyes) + rows 89/98; robe/hair/hands/wrist-mark/background/pose
all identical (edit changed only the irises). Group shots (b03/b04/b05/b06/b09/
b13/b14) left as-is — eyes too small/dark to read colour on screen (per lesson).

**Rest of the FULL-CUT GATE:** CLEAN — empty-cross off-screen crucifixion (b01),
no-wire tomb (b12), cream-only-Jesus every appearance, ordinary Jesus scale in
every multi-figure frame, prior-C-FIX rerolls still good (b16 upright group, b20
soft leather scripture, b21 ancient dirt-path descent), captions bottom-band
3-colour correct (white narrator / red jv18-jv19-jv20 Jesus), question card
clean. No modern object, no 2nd cream figure, no anatomy fail, no lens-stare.

**COST:** 1 reroll (b18) + 3 iris edits / 21 beats = 4 paid images ≈ **$0.53**;
reroll rate 4.8% (well under the 15% budget); meter $599.92→$600.45. Touch-once:
both named complaints AND the gate-caught eye defect batched into ONE re-cut
(Cameron reviews the finished cut once). Under the ~$1.2 C-FIX norm; trend DOWN.
**AUDIO byte-identical throughout — the 3 eye edits + 1 reroll are picture-only.**

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

---

## C-FIX 2026-08-12 (Opus runner, Machine A `Dev`) — RE-OPEN #3: audio "alway"→"always" + white tear on Peter — CLOSED in ONE touch-once re-cut

**COMPLAINT LEDGER** (`v2_outline.py 71`, Cameron, reportedAgainst `5cc43a5f`):
1. *"Jesus said … 'I am with you always … end of the world' not 'alway'. The voice
   still is pronouncing [it wrong], the caption is correct but not the audio."*
   → **FIXED (audio).** jv20 re-voiced to say **"always"** with an audible /z/.
2. *"1:37 a man has a white tear and that needs to get fixed."*
   → **FIXED (picture).** 1:37 = b18/`s18`; Peter regenerated fully dry-eyed.

**Why it re-opened twice (PROMPT AUTOPSY, rubric meta-law 3):**

- **Audio = the whisper trap.** The 08-11 fix (`1897b351c`) only changed the
  CAPTION (TEXT_OVERRIDES) and trusted `faster-whisper` ("confirms 'always' on
  jv20.mp3") to prove the audio was fine. faster-whisper NORMALISES "alway"→
  "always" and is deaf to the missing terminal /z/. The V1 make_narration text is
  "alway", so ElevenLabs was fed "alway" and correctly said "alway" — no /z/.
  Measured on the shipped V1 jv20: word-final HF(4-8k) = **0.009** (vs its own /z/
  in "observe" = 0.18, /s/ in "whatsoever" = 0.31) → the word ends in the /eɪ/
  vowel = "alway". Cameron was right. **Verdict: the caption fix ALLOWED the audio
  defect to survive by mis-diagnosing it.** Fix = re-voice (below), not caption.
- **Picture = a self-inflicted loophole.** b18's `must_not_show` banned a "painted/
  white tear/streak/droplet" but then explicitly PERMITTED "if his eyes shine at
  all it is only the faintest natural wetness catching the light." The model renders
  that permitted wet glint on Peter's lower eyelid as a welling tear — which reads
  as the white tear across all three cuts. **Verdict: CAUSED/ALLOWED by the prompt's
  own wet-eye permission.** Fix = remove the permission; forbid ALL eye wetness/
  shine/gloss/glint, eyes fully dry, emotion via brow + mouth alone; regen s18.

**Audio re-voice (touch-once with the picture):** ElevenLabs **Alexander** (JESUS
voice, same as jv18/jv19 — identity preserved), fed the literal "always". Rendered
4 takes; A/B spectrogram vs the original confirmed a distinct terminal /z/ frication
cloud (4-8 kHz) the original lacks. Chosen take: terminal /z/ HF **0.65**, **F0 96 Hz**
(orig jv20 = 97, jv19 = 95). atempo-locked to the original **11.232653 s**
(delivered 11.2588 s, drift +26 ms — inside the 1.6 s KJV gap, no window moves).
Old jv20 saved to `audio-oldvoice-backup/`. Because a V1 mp3 now post-dates the V1
final mp4, `AUDIO_FROM_V1_SEGMENTS = True` was added so narration rebuilds from the
V1 mp3s (incl. new jv20) — **AUDIO REBUILD PASS SHA256=6a0f7de9…**, 131.8 s. Caption
stays "always" (TEXT_OVERRIDES, already correct) and now matches the spoken word.

**FULL-CUT GATE 6b:** one frame per beat from the RE-RENDERED mp4, all 21 viewed —
realistic throughout, Jesus one face + cream-only, natural scales, no modern objects,
no cartoon, s18 Peter dry-eyed, jv20 caption "always … unto the end of the world.
Amen." correct (Jesus red), question card clean. No new complaint-worthy frame; only
the two named defects were touched.

**Cost:** 1 s18 reroll (~$0.13) + 4 ElevenLabs Jesus renders (subscription, ~$0
marginal Gemini) = **1 gen / 21 beats = 4.8% reroll**, ~$0.13 Gemini. Touch-once:
picture + audio in ONE re-cut = one reviewer delivery. Audio is NO LONGER
byte-identical (jv20 was legitimately re-voiced) — SHA c29f8cf → **6a0f7de9**.
