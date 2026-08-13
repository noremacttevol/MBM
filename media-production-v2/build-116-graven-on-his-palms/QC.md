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

---

## ✅ SHIPPED — REALISTIC-V2 FIRST CUT (Opus runner, Machine A `Dev`, headless) 2026-08-13

Billing restored overnight (row 118 shipped this morning cleared the depletion wall).
Resumed the two 2026-08-06 billing parks: WOMAN portrait + CITY plate (b04) were
already done & committed — reused, NOT regenerated. Generated the 20 remaining beats
in ONE pass, 0 429s.

**COMPLAINT LEDGER: none open.** `v2_outline.py 116` shows no filed complaint on
this row. Cross-checked QUEUE.md row 116 = "Graven on his palms, Isa 49" — a
realistic-V2 redo, NOT a swapped/replaced story. Built to spec, no complaint to answer.

- **Build:** 21 realistic stills @ native 2K. Reused: WOMAN portrait (CAST-REF-V2/woman.jpeg),
  CITY plate (assets/s04, PLACE-WIRING manual). NEW gen: b01-b03,b05-b21. ENGRAVER + MOTHER
  are text-lock-only cast tokens (no portraits) — QC'd hardest for drift; each read consistent
  within its few frames (MOTHER b07/b09/b11 warm nursing content-care; ENGRAVER b12/b14/b15/b21
  one grey craftsman).
- **Rerolls: 2 (9.5%, under the 15% budget), both on b21.** AUTOPSY = ALLOWED (nothing in the
  beat banned eyewear): the closing engraver twice rendered wearing modern wire-rim EYEGLASSES
  (anachronism / modern object) + a lens-stare — the generator associates "old man examining
  fine engraving" with reading glasses. Reroll #2 cleared both (glasses-free, eyes on the tablet,
  three-quarter). Hit the 2-reroll cap; did NOT drift-chase further.
- **FULL-CUT GATE on the RENDERED mp4 — 21/21 beats + card PASS** (one frame per beat extracted
  from the mp4 and viewed in PLAY order, + caption/speaker pixel check): realistic photography
  throughout (no cartoon/mix, Law 14). **GOD NEVER EMBODIED (default OT gate — no complaint asks
  to depict him)** — no divine figure/hand-from-sky/beam/light-disc; the God-voice beats (jv15
  b09/b10, jv16 b14/b16) are carried by the forgotten woman, the nursing mother, and the ENGRAVER
  carving a NAME into enduring bronze. **THE PALMS handled per author law: "graven" = a name cut
  deep into metal (b14/b15 Hebrew, b19 insert), the gospel echo IMPLIED only — NEVER depicted as
  nail-wounds** (passion imagery stays at rows 94-96's distance). WOMAN one consistent olive
  middle-aged face in dark-blue veil across all her beats; MOTHER warm/modest; ENGRAVER consistent.
  Distinct faces, ordinary scale, clean hands/anatomy, no owl-neck, no modern object (glasses gone),
  first-century materials, warm living skin. Light arc holds: dusk-alone → first gold → full morning
  (b18 the woman steps into full morning light — the promise's payoff). Captions bottom-band only;
  **SPEAKER LAW pixel-verified: narrator WHITE, Zion's lament "The LORD hath forsaken me" BLUE
  (scripture), God-voice jv15/jv16 GREEN, NO RED anywhere** (correct — OT, no embodied/Jesus voice).
  Clean question card, good margins, no tofu. DROP-CHECK: concat_base = 21 clips == 21 BEATS
  (no dropped beat); mp4 133.67s; AUDIO LOCK PASS SHA256 e5bb3a2e.
- **Judgment logged (not a defect):** b21's closing bronze plate carries a legible engraved
  Greek name reading "IHΣOYΣ" (Jesus). This is a graven NAME — the literal subject of the row
  ("Behold, I have graven thee") — and b15/b19 likewise show engraved Hebrew letters BY DESIGN;
  it reads as the intended gospel echo, is not a watermark/caption/modern-object defect, and is
  not any Cameron-complaint class. Kept rather than exceed the 2-reroll cap chasing a Hebrew
  variant. Flag for the later fix-wave if he ever wants Hebrew-only graven text.
- **Cost:** ~$2.94 this session (20 beats + 2 rerolls), 9.5% rerolls — both well under the
  $6.10/row & 15% COST-LAW ceilings; downward trend holds.

---

## QC-VERIFY — 2026-08-13 (Opus runner, Machine A `Dev`, headless) — FULL-CUT GATE, CLEAN, NOT re-cut

Independent full-cut gate (PROMPT-OPUS-RUNNER 6b) of the BUILT/unapproved cut
sitting in Cameron's Unwatched queue, before his eyes reach it.

**UNTOUCHABLE-CHECK FIRST:** read `.approvals.json` row 116 myself — `approved:false`,
`approvedHash:null`. Row is NOT approved → QC-VERIFY is in-scope (not an untouchable
release decision; the 2026-07-18 approvedAt is a void pre-redo timestamp).

**Live-verified Cameron is being served THIS cut (not assumed):**
- review.html card `data-hash` = `3bb9a5df17f9947cd391325b33ef7e890d5bbca6`; live
  Firebase page (milk-b4-meat.web.app) serves the same hash.
- Ship commit `3bb9a5df1`; the mp4 in that commit blob = local = **19,313,597 bytes**.
- Served raw mp4 HTTP 200, content-length **19,313,597** == local.

**FULL-CUT GATE:** extracted one mid-window frame per beat (21 beats, play order
b01–b21) + the question card from the RENDERED mp4; viewed EVERY frame against the
defect checklist + CONTENT-CARE (the PALMS law) + speaker law.

- **CLEAN 21/21 + card.** No re-cut. $0 / 0 rerolls.
- God NEVER embodied — the "graven" image is an ENGRAVER cutting a NAME into metal
  (b12 JERUSALEM brass, b14 Hebrew bronze, b19 macro, b21 Greek IHΣOYΣ closing echo);
  never nail-wounds. Content-care (PALMS law) held exactly.
- Speaker law verified in-frame: white narrator; **blue** Zion-scripture (b03 "But Zion
  said, The LORD hath forsaken me…"); **green** God-voice (b09 "…the son of her womb?",
  b10 "yea, they may forget, yet will I not forget thee").
- Cast consistency: WOMAN (older, blue-gray robe/shawl, gray-streaked dark hair) held
  across b01/02/03/05/06/08/10/13/17/18; MOTHER (young, braided, red robe) b07/09/11;
  ENGRAVER (grey-bearded, leather apron) b12/14/21. No drift.
- Time-of-day arc intentional & correct: blue dusk (loneliness) → warm lamplight
  (mother/engraver) → morning gold (the promise). No modern objects, no glow/halo/
  rim-light, anatomy/hands clean on every checked frame, no giant-scale, no white-tears,
  no eyes-turned-to-light.
- Captions bottom-band only; question card clean (no code-squares/typos, text fits).
- COMPLAINT LEDGER: none open (v2_outline.py 116 — no complaints; `.approvals.json`
  complaint=null). Nothing to regress.

Left BUILT/Ready for Cameron; claim marked QC-OK.
