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
# portraits + CITY plate (b04) already DONE — do NOT regen them.
python3 media-production-v2/v2_gen_api.py build-116-graven-on-his-palms --ceiling <meter+20*0.201+25>
# generates the 20 remaining beats (b01-b03, b05-b21); CITY already wired to b04, WOMAN portrait set.
# then QC, assemble, ship per PROMPT-OPUS-RUNNER.md
```

## RUNNER PARK — 2026-08-06 (A-auto Machine A) — BILLING STILL DEPLETED (2nd probe, $0 spent)

Re-probed post-topup this session. Portraits (WOMAN) and CITY plate (b04, s04)
already existed — QC'd b04 as a clean plate (first-century Judean dusk town,
stars, many solitaries each faced away, no lens-stare, no cream, no modern
object, anatomy fine — PASS). Ran `v2_gen_api ... --ceiling 438.66` to generate
the 20 remaining beats; it returned `429 RESOURCE_EXHAUSTED — "Your prepayment
credits are depleted"` on beat b01, the very first call. Retried once after 62 s
per the brief — IDENTICAL depleted 429. This is the HARD billing wall (RUNNER-
LESSONS INFRA/BILLING), GLOBAL to the Gemini key: every row is blocked, there is
NO next-ready row to fall to. **$0 spent** (429 fired before any image made).

**ACTION FOR CAMERON:** top up Google AI Studio prepayment billing at
https://ai.studio/projects (billing → prepay). Until then NO row can generate.
After topup, any session re-running the RESUME above ships this row.

---

## 🅿️ RUNNER PARK #2 — A-auto Machine A, 2026-08-06 (BILLING DEPLETED AGAIN, GLOBAL)

**BLOCKER (GLOBAL, not row-specific):** Gemini API returned
`429 RESOURCE_EXHAUSTED — "Your prepayment credits are depleted"` after the
WOMAN portrait + the b04 CITY anchor were generated. Retried twice (per brief);
identical error. This is depleted PREPAYMENT credit, not an auto-reloading rate
limit — it blocks EVERY row and EVERY lane until Cameron tops up at
https://ai.studio/projects (Google AI Studio → billing → prepay). The earlier
row-1 spend this session ($409.64 meter) exhausted the prepaid balance mid-row.

**Art state (preserved, reusable — do NOT regen):** WOMAN portrait made
(`CAST-REF-V2/woman.jpeg`); CITY plate promoted from b04
(`assets/s04-that-is-exactly-how-people.jpeg`, QC-PASS: dusk city of solitaries,
period props, no modern objects). Remaining 20 beats NOT generated.
COMPLAINT LEDGER: none open.

Claim reverted to AUTHORED / Ready ✅ / empty claim so the next session
(post-topup) takes it clean; the promoted CITY plate + WOMAN portrait are
committed and will be reused.

**RESUME (after Cameron tops up Gemini billing):**
```
cd media-production-v2
python3 v2_gen_api.py build-116-graven-on-his-palms --ceiling <meter+21*0.134*1.5+25>
# b04 already present + CITY wired; QC all frames, assemble (audio CLEAN,
# |Δ|=0.024s — will pass AUDIO LOCK), ship per PROMPT-OPUS-RUNNER.md step 7.
```
