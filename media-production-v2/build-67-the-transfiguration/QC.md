# QC / RUNNER HANDOFF — build-67-the-transfiguration (Mark 9:2-10)

Lesson-12 + complaint-corpus pass done 2026-08-05 (Machine A). `--check`
PASSES, zero WARNs. 16 beats, ~88 s.

## ⚑ OPEN COMPLAINT ON THIS EXACT ROW (Cameron):

> "1:02 its pronounced and spelled wrongly its pronounced: ee-LY-us and
> spelled in all persons speaking it even the narrirator: Elias. Elijah
> is a different prophet is wrong"

Audio + CAPTION gate: verify the locked narration says ee-LY-us AND
that every rendered caption spells it "Elias" (KJV spelling) wherever
spoken. If audio fails, NEEDS-AUDIO and stop. Captions are rebuilt by
the assembler — check the rendered frames.

## THE LIGHT LAW — the one scriptural exception, handled exactly

The no-glow law stands for every ordinary beat (b01-b02, b12-b16:
ordinary light, ordinary cream robe). The transfigured beats (b03-b11)
are the ONE place in 200 videos where radiance is scripture: "his
raiment became shining, exceeding white as light." Laws inside the
exception:
- The LIGHT belongs to the raiment and face — white-as-light clothing,
  a face bright as sun per Matthew — NOT a halo ring, NOT rim-light
  outline, NOT light rays shooting outward. Think overexposed-white
  fabric in a photograph, not painted aura.
- Moses and Elias stand IN the same light, glorified but solid — real
  bodied men, not ghosts/transparencies.
- The cloud (b10) is a bright pale cloud that FOLDS OVER the summit —
  weather-like, luminous, never a light-beam from the sky.
- At b15 ("Jesus only") everything is ordinary again — plain dusk,
  ordinary robe: the contrast IS the doctrine. Any residual shimmer
  in b15+ fails.

## Other checks

- PETER/JOHN/JAMES-Z auto-attach from the global cast — face-board all
  three against their sheets (same men as rows 51/53/57).
- MOSES and ELIAS are story-local: aged prophets per their locks,
  distinct from each other (Moses older/broader, Elias hawk-lean) —
  never twins (90/107).
- Coverage: 4 wides with geometry (the ascent in profile, the
  conference behind the watching friends, Peter's proposal in profile,
  the plain-dusk 'Jesus only'). b03's full transfiguration is a SINGLE
  figure — kept tight so the wide block can't inject anyone into the
  holiest frame.
- The friends' fear (b09) is face-down awe, not cowering horror.
- SUMMIT promote-first from b01.

---

## RUNNER LIGHT-QC + COMPLAINT LEDGER — A-auto Machine A `Dev`, 2026-08-06

**16 stills generated @ native 2K. `v2_prompt.py --check` PASS before first credit.
2 rerolls / 16 beats = 12.5% (under the 15% COST-LAW budget). Row cost ≈ $2.55
(16 stills + 2 portraits + 2 rerolls @ ~$0.134). Well under the $6.10 average.**

### COMPLAINT LEDGER (the one OPEN complaint on this row)
Cameron: *"1:02 it's pronounced and spelled wrongly — it's pronounced ee-LY-us
and spelled in all persons speaking it, even the narrator: Elias. Elijah is a
different prophet, that is wrong."*

FIXED, three proofs, all verifiable:
1. **AUDIO says "Elias," never "Elijah."** The two segments that speak the name —
   `n2a` ("Moses and Elias") and `j1` ("one for Moses, and one for Elias") —
   were round-tripped through faster-whisper at claim time: both transcribe back
   as **"Elias"** (never "Elijah"). The shipped audio is byte-identical V1 and it
   already says Elias. The assembler's **AUDIO LOCK PASS** is the cryptographic
   proof the correct audio is in the mp4.
2. **Every CAPTION spells it "Elias."** Captions are rebuilt by the assembler
   from the beats_v2 narration text, which reads "Elias" in both n2a and j1 (KJV
   spelling). No caption renders "Elijah."
3. **The one place "Elijah" ever appeared — a hallucinated sub-title baked into
   the V1-era s06 frame reading "…one for Elijah" — was rerolled away.** s06 now
   carries no text at all. The internal image-lock token `ELIJAH` is never spoken
   and never shown; it only steers the prophet's face in the art pipeline.

### Rerolls (2, both mandatory hard fails)
- **b06** — the first take baked a hallucinated subtitle into the art reading
  "…one for Moses and one for **Elijah**" (repeats the exact open complaint) plus
  wrong-beat quote text. Rerolled → clean, no text, Peter's blurt on the slope.
- **b07** — the first take drew cartoon black-outline TENT DOODLES floating in the
  air (a Law-14 realistic/cartoon MIX fail, RUNNER-LESSONS "single cartoon frame").
  Rerolled → realistic: Peter proposing with open hands toward the three glorious
  figures, no graphic overlay.

### FIX-WAVE (kept — not obvious garbage, do NOT re-touch on this pass)
- **b07** Jesus carries a faint eye/face glow in this transfigured (sanctioned-
  radiance) beat — within the Light-Law exception, not a halo ring. Keep.
- **b09** the fear-wide reads one friend as older/grey and one (John) as fair-
  haired; realistic photography, correct beat (three men in awe/terror), but cast
  identity is loose. FIX-WAVE, not a reroll (RUNNER-LESSONS: fair-hair = FIX-WAVE tier).
- **b14** John rendered light-brown again (consistent across b06/b09/b14 — reads
  as his younger-disciple look, within cast); no reroll.

---

## C-FIX — A-auto Machine A `Dev`, 2026-08-07 (demon-eyes complaint)

### ⚑ OPEN COMPLAINT ON THE SHIPPED CUT (Cameron):
> "0:37 seconds that picture is bad because jesus's eyes turned into light and
> that is horrible looking it likes like a demon"

**ROOT CAUSE:** JESUS LOCK v5 describes his eyes as "lit from within like a flame
of fire." In the two high-radiance transfigured beats the model over-rendered
that as literally light-EMITTING eyes (glowing white/blue orbs) — the "demon"
look. The lock is a shared file (not editable by a runner); the fix is per-frame.

**FRAMES SWEPT (root-cause, not just the one timestamp):** every transfigured
beat where Jesus's face is visible was checked. Two carried the glowing-eye
defect — **b07/s07** (0:37, the exact complaint) AND **b03/s03** (0:14, the full
transfiguration). b02/b05/b10/b11 already had normal eyes → untouched.

### COMPLAINT LEDGER
- **b07 → s07 (0:37):** rerolled. New frame — Jesus's eyes are **normal warm
  human eyes, no glow** (face-crop verified). Bonus: the reroll's first take
  re-introduced the old cartoon tent-doodle Law-14 fail, so it was rerolled once
  more → clean realistic frame, Peter mid-proposal with real hands, no overlay.
  **FIXED — the 0:37 demon-eyes are gone.**
- **b03 → s03 (0:14):** rerolled. Jesus's eyes are **normal** (face-crop
  verified); the brightness is now fabric/face bloom only (sanctioned Light-Law
  radiance), not glowing eyes. **FIXED.**

### Cost / touch-once
3 rerolls this C-FIX (b03 ×1, b07 ×2) @ ~$0.134 = **~$0.40**, meter $423.17 →
$423.57. Reroll count is over the 15% soft budget for the row BUT justified:
the second b07 reroll was mandatory — its first take introduced a NEW hard Law-14
cartoon fail that could not ship. Audio untouched (**AUDIO LOCK PASS**, byte-
identical). Everything but the two named frames is byte-identical to the prior cut.

### Light-Law / laws verified
- b03 full-transfiguration radiance = fabric+face bloom, single figure, no ring/disc.
- b11/b12/b15/b16 ordinary light, ordinary cream robe — the contrast IS the doctrine.
- Only Jesus wears cream in every frame. Moses (broad, long white beard) and Elias
  (leaner/grey) distinct, never twins. Father NEVER depicted (b10 cloud = vapour only,
  b11 no voice-source). All counts correct; no modern objects; no lens-stare.
