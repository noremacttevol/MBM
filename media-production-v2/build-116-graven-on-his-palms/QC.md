# QC / RUNNER HANDOFF — build-116-graven-on-his-palms (Isaiah 49:14-16)

Lesson-12 + complaint-corpus pass done 2026-08-05 (Machine A). `--check`
PASSES, zero WARNs. 21 beats, ~116 s.

## THE PALMS (the row's central image — handle exactly)

"Graven upon the palms of my hands": the engraver vignettes cut a name
INTO enduring material (the craftsman's beats) — permanent, costly,
not written-on but cut-in. The gospel echo (nail-marked palms) is
IMPLIED by the word graven and the closing gaze only — never depicted
as wounds in this row (the passion imagery belongs to rows 94-96 and
stays at their merciful distance).

## The forgotten woman (dignity law)

Her loneliness (Zion's "the LORD hath forsaken me") is real and
dignified — the row-44/74/75 women's class. Her arc: dusk-doorway
alone → the promise heard → stepping into full morning. Face-board.

## The nursing-mother comparison (b-early beats)

"Can a woman forget her sucking child?" — the MOTHER lock's frames
are warm and safe (child content-care); the may-forget/I-will-not
contrast lives between her human frailty and the graven permanence.

## Coverage shape

Two true wides with stated geometry: b04 (the dusk city's many
solitaries, each faced away from the lens into their own window) and
b16 (thy-walls-continually — the whole waking city from the wall's
height). Four flips.

- Dusk → first gold → full morning: the light IS the promise's arc.
- ENGRAVER/MOTHER are cast tokens — no plates; CITY promote-first
  from b04.

---

## RUNNER PARK — 2026-08-06 (A-auto Machine A) — BILLING DEPLETED ($0 spent)

**BLOCKER (GLOBAL, not row-specific):** the Gemini API returns
`429 RESOURCE_EXHAUSTED — "Your prepayment credits are depleted"` on the very
first portrait call. Retried once after 65 s per the brief; identical error.
This is NOT a rate limit that auto-reloads — it is depleted PREPAYMENT credit
and blocks EVERY row until Cameron tops up billing at
https://ai.studio/projects (Google AI Studio → billing → prepay).

- $0 spent this session (429 fired before any image generated; nothing to reuse/regen).
- Row 116 is untouched: claim reverted to AUTHORED / Ready ✅ / empty claim so
  the next session (post-topup) can take it clean.
- COMPLAINT LEDGER: none open (v2_outline.py 116 shows no complaints).
- Author QC intact: CITY plate promote-first from b04; ENGRAVER/MOTHER cast tokens.

**RESUME (after Cameron tops up Gemini billing):**
```
python3 media-production-v2/v2_story_cast.py build-116-graven-on-his-palms --ceiling <meter+~0.6>
python3 media-production-v2/v2_gen_api.py build-116-graven-on-his-palms --ceiling <meter+(21 beats+1 portrait)*0.134*1.5+25>
# then promote CITY from b04, QC, assemble, ship per PROMPT-OPUS-RUNNER.md
```
