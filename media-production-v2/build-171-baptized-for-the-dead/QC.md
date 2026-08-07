# QC — row 171, build-171-baptized-for-the-dead (1 Corinthians 15:29 + vv.20-22)

**Authored 2026-08-07, Machine A `Dev`, Fable-5 author lane, $0** (0 pictures
generated, 0 audio touched). `v2_prompt.py --check` PASS (15 beats, no warnings).
Windows contiguous + monotonic 0.400 → 73.427 (card_start), every segment onset
in-window. Audio column OK on AUTHOR-BOARD.

## COMPLAINT LEDGER (LEARNING LAW — one open complaint, ADDRESSED)
- **OPEN:** *"First picture is weird there are no scripture that roll like that on
  2 edges."* — The V1 first still put a SCROLL with rendered scripture text
  CURLING on two edges into the frame; it read as a fake panel / generated-text
  artifact. **FIXED in this map:** the new first picture (**b01**) is PEOPLE —
  Paul debating the Corinthians in a portico — and its `must_not_show` HARD-BANS
  any scroll, any parchment/paper with visible writing, any curling/rolling edge,
  any rendered letters/numerals, and any panel/border/frame along any side. AND
  **every one of the 15 beats** carries "nothing written anywhere / no scroll,
  writing or panel" in its must_not_show, so no frame in the build renders
  scripture text as art (captions are added later, bottom band only). The review
  card should tell Cameron the weird rolling-scroll first picture is gone.

## Speaker law
Paul's epistle — **s1, s20, s22 are all the SCRIPTURE voice → LIGHT-BLUE
captions, never red.** No Jesus-red, no God-voice. Jesus is embodied (risen Lord,
locked face + REF, cream) only on the two resurrection-anchor beats **b09** and
**b11**; the picture shows him because "Christ risen" is the concrete fact, but
the caption stays scripture-blue (s20) / narrator.

## Content-care (row 171 is GREEN, but the subject is the DEAD → restraint)
- The departed are shown with DIGNITY and HOPE — a mourner's remembering face,
  the ordinance done in love; **NEVER a corpse, never gore.**
- "the grave loses its grip" (b11) and "in Christ all made alive" (b13) are DAWN
  LIGHT + an EMPTY tomb + a living risen man + hopeful faces — **NEVER rising
  corpses, opened graves with figures climbing out, or zombies.**
- "reaches across the veil" (b14) is SOFT LIGHT only — **no ghost, spirit-figure
  or apparition** stands in it.
- The person "baptized for the dead" is a LIVING PROXY going into the water on
  behalf of one who died — **never a body in the water.**
- The risen Christ (b09/b11) is warm, solid, real — **not a ghost, not a glare;**
  no wound-gore. Scale gate applies.

## The doctrine made concrete (realistic, not V1's abstract metaphors)
Three real settings: **CORINTH-PORTICO** (Paul teaching, b01-b02), **BAPTISM-
WATER** (the proxy baptism + the remembering family, b03-b08, b14-b15), and
**RISEN-DAWN** (the empty tomb + the risen Christ, the resurrection anchor,
b09-b13).

## Locks
- **PAUL** — BYTE-IDENTICAL to rows 138/155/166 (cross-video same man; face
  carried by the text lock, no face sheet yet — same as those rows).
- **PROXY** (living believer baptized for the dead) and **MOURNER** (the departed's
  family) — build-local person locks, one consistent face each across their beats.
- **CORINTH-PORTICO / BAPTISM-WATER / RISEN-DAWN** — build-local place locks.
- **BACKGROUND-CAST** (shared) on multi-figure beats for distinct faces (lesson 3).
- Jesus: locked V2 face + REF auto-attached by the jesus/ref flags on b09/b11.

## RUNNER — do this (paid picture lane; audio is DONE and untouched)
1. Confirm `--check` PASS on this machine.
2. Generate **b01** (Corinth), QC, `--promote build-171-baptized-for-the-dead
   CORINTH-PORTICO <b01>`; **b03** (water), QC, `--promote … BAPTISM-WATER <b03>`;
   **b10** (empty tomb — NOT b09/b11, which are Jesus frames), QC, `--promote …
   RISEN-DAWN <b10>`; then generate the rest on the existing audio (Audio OK — do
   NOT re-voice; AUDIO LOCK byte-identical to V1).
3. **Face board (lesson 10) + beard board (lesson 13):** Paul one man (b01/b02);
   the PROXY one person across the water beats; the MOURNER one woman across her
   beats; the risen Jesus the locked V2 face (b09/b11).
4. **Restraint gate on every departed/resurrection frame** (b05, b10, b11, b12,
   b13, b14): no corpse, no gore, no rising bodies/opened graves, no ghost — dawn
   light and empty tomb only. **Scale gate** on Jesus (b09/b11) and multi-figure
   frames.
5. **First-picture gate (the complaint):** b01 must contain NO scroll, NO written
   text, NO rolling/curling edge, NO panel — verify in the rendered frame.
6. Assemble (`v2_assemble.py` — AUDIO LOCK PASS), technical gates, caption QC
   (bottom-band; s1/s20/s22 light-blue, narrator default), publish to review.html,
   ship with a card noting the weird rolling-scroll first picture is fixed.
7. **Reroll budget ≤15% of 15 = ~2 beats.** Two failed rerolls → FIX-WAVE, keep
   best, move on. Log $/row + reroll % vs the $6.10 average. Expected cost ~15 ×
   $0.20 ≈ $3.0 (all-new build, short row).
