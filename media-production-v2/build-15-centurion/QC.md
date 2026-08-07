# QC / RUNNER HANDOFF — build-15-centurion

Complaint-gate addendum, 2026-08-05 (Machine A).

## OPEN CAMERON COMPLAINT — gates before rebuild

"the sick boy's age keeps changing and he looks too grey to be a
human and partially alive like he shouldnt be that grey and his age
should stay the same."
The SERVANT lock was REWRITTEN this session: exactly eighteen in
apparent age in every frame (never a boy in one shot and a man in
another), and PALE-BUT-ALIVE — warm living undertone always, NEVER
grey/waxy/ashen (the old lock literally ordered 'grey and waxy';
that wording is dead). Face-board the servant across every beat for
AGE and for LIVING SKIN before assembly; one grey-corpse frame or
one age-shifted frame = reject.

## C-FIX 2026-08-07 (Machine A Dev) — SHIPPED

**COMPLAINT LEDGER — the ONE open complaint on this row:**

> "the sick boy's age keeps changing and he looks too grey to be a human
> and partially alive like he shouldnt be that grey and his age should stay
> the same."

ROOT CAUSE (why a prior rebuild didn't fix it): the SERVANT *lock* had
already been rewritten to "eighteen, PALE-BUT-ALIVE, never grey," but the
per-beat scene text of four servant frames still literally ordered the
defect — b05 said "He is very young … dark curls … soft grey," b06 said
"the boy … the boy's grey face," b39/b41 said "the boy." The beat text
overrode the lock, so every re-gen reproduced a curly grey corpse in s05
and a 13-year-old boy in s06/s39/s41 while the healthy/healed frames
(s04, s36, s37, s38) showed a ~20-year-old man. THAT is the age swing and
the grey he saw.

FIX (touch-once, this one re-cut):
- Scrubbed the "boy / very young / dark curls / grey face" wording out of
  the FOUR offending beats (b05, b06, b39, b41) so the scene text now
  agrees with the SERVANT lock: one ~18–20 young man, short dark hair,
  PALE-BUT-ALIVE, never grey.
- Regenerated ONLY those four frames (char-ref anchored to the kept
  healed-servant frame s04). Every other frame is byte-identical.
- Result, face-boarded against s04/s36/s37/s38:
  - **s05** — grey curly "corpse" → living young man, warm skin, short dark
    hair, sweat of fever but alive. GREY LOOK GONE.
  - **s06** — 13-yr-old boy → same ~18–20 young man on the bed.
  - **s39** — boy in doorway → same young man standing, colour in his face.
  - **s41** — small boy in the embrace → same young man.
  - His apparent age is now the SAME across all eight servant frames; no
    frame is grey/ashen. Both prongs of the complaint answered.

Rerolls: 4 of 41 beats = 9.8% (under the 15% budget). Spend this fix:
~$0.54. Audio untouched — AUDIO LOCK must pass on re-assemble.
