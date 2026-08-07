# QC / RUNNER HANDOFF — build-49-water-to-wine (John 2:1-11)

Lesson-12 + complaint-corpus pass done 2026-08-05 (Machine A). `--check`
PASSES, zero WARNs. 40 beats, ~230 s. Audio OK. Open complaint on this
row (row 50 card mentions Cana pronunciation — that one is row 50's; row
49 itself carries the "Cana = Kane-a" pronunciation family): VERIFY the
narration audio says KANE-a everywhere before assembly (the audio is
locked V1 audio — if it fails, mark NEEDS-AUDIO, do not re-voice).

## ⚠ THREE-MARYS LAW (identity trap — read before generating)

This row's MARY is the MOTHER of Jesus (~50, serene, per her lock). She
is NOT build-16/17's Mary of Bethany and NOT Mary Magdalene. There is no
CAST-V2-REF sheet for any Mary. Story-cast her fresh for this row, and
when she passes QC, note her canonical frame HERE — future mother-Mary
rows (84 manger, 86 wise men, 87 boy in temple, 94-96 the cross) must
REFS-anchor to it. Never reuse a Bethany-Mary or Magdalene frame for
the mother.

## Coverage shape

Five true wides with stated geometry: b02 (court establish), b04 (the
dance — full-body ensemble action), b25 (the bucket brigade in profile),
b32 (the public toast from behind the tables), b37 (the restored feast —
the transformed echo of b04). Eight flips: Mary's walks (direction
anchored to in-frame targets), the quiet order at the jars, the careful
cup-carry, the couple two-shot.

## Place plates — promote-first (no stash match)

| Token | Promote from | Then covers |
|---|---|---|
| COURT | b02 `assets/s02-...jpeg` | all courtyard beats |
| JARS | b21 `assets/s21-...jpeg` (the six-jar row) | all jar beats |

SERVANTS is a CAST lock the tool misread as a place — do NOT promote a
plate for it (three distinct servants: face-board them instead).

## Complaint-corpus checks

- **COUNT LAW (row-135) — the row's biggest:** SIX stone jars, exactly,
  in every jars frame — countable, separated (COUNT-AS-GEOMETRY lock).
  THREE servants, exactly, throughout.
- **The miracle is UNDEPICTED mid-change:** water goes in (b25), wine
  comes out at the drawing/tasting — never show a glowing
  transformation moment; the first RED appears at the draw, and the
  drawn cup's contents read as wine, not blood (dark red, in a cup, at
  a feast).
- **Identity (32/62/91/102):** steward, bridegroom, the three servants,
  mother-Mary — face-board all; the tall servant who carries the cup
  (b28) is the SAME servant who draws it.
- **Direction (row-83):** b08 Mary crosses TO Jesus (he is in frame);
  b19 she walks AWAY without looking back while the servants' gazes
  stay ON her order's target.
- **Jars are STONE (John 2:6), waist-high — never clay amphorae, never
  glass (row-7 class).** Water poured TO THE BRIM (b25) — visibly full.
- Wedding joy is lamplit night from b04 on; golden afternoon before.
  One direction only.
- Only Jesus wears cream anywhere.

---

## C-FIX (Machine A `Dev`, 2026-08-07) — Cameron's picture complaint, ALL fixed

**Complaint (`v2_outline.py 49`, against the live shipped cut `b7f622627`):**
> "2:42 the water turning into wine does not need a cadle flame in it. That is
> weird. And mother mary standing so close to Jesus in those couple of pics is
> weird @ 0:50 & 0:57"

Picture-domain, not audio. Mapped each timestamp to its still by extracting the
frame from the shipped mp4 and matching content (Ken Burns pan → still):

**COMPLAINT LEDGER (this re-cut, touch-once — all three offenders re-rolled):**
- **2:42 "candle flame in the wine" → `s29` (b29) FIXED.** The old scene text
  literally asked for "the strung lamps' small flames riding its moving surface,"
  so the model painted a lit flame floating IN the cup. Rewrote b29 to smooth
  dark-red wine under a soft even lamplight with an explicit must_not_show: "NO
  flame, candle, wick, ember or bright point of light on or inside the liquid."
  Re-rolled → the cup now shows plain dark-red wine, the oil lamp only in the
  far background. No flame in the cup.
- **0:50 "Mary too close to Jesus" → `s09` (b09) FIXED.** Old scene text: "Mary's
  lifted face a hand's breadth from her son's" — produced a forehead-to-forehead,
  lover-like framing. Rewrote to "a natural, respectful arm's-length beside her
  grown son, half-turned to speak … their faces apart" + must_not_show "foreheads
  never touch, no intimate or romantic framing." Re-rolled → they now stand a
  normal conversational distance apart in the lamplit hall.
- **0:57 "Mary too close to Jesus" → `s11` (b11) FIXED.** Old scene text: "the two
  faces stay close … one hand risen lightly toward her shoulder" — produced a
  near-embrace. Rewrote to "a natural step … his hands quietly at his sides — no
  reaching, no touch" + must_not_show "he does NOT reach for, touch, or embrace
  her — no hand to her shoulder, no intimate or romantic framing." Re-rolled →
  mother and son face each other at arm's-length, no contact.

**Identity/law checks on the three re-rolls:** Mary stays the canonical mother
(indigo mantle, madder-rose dress, ~50, silvering hair, serene) — consistent with
s16 canonical frame. Jesus canonical (cream robe, dark wavy hair, full beard,
only-Jesus-in-cream) — no second cream figure in the s09 crowd. No halo/glare/
rim-light. `--check` v4 checklist PASS. Audio untouched — re-assemble AUDIO LOCK
PASS, narration byte-identical to the shipped cut.

**Reroll ledger (COST LAW):** 3 rerolls / 40 beats = **7.5%** (budget 15%). Spend
this session ≈ 3 × $0.134 = **$0.40**, all image cost, $0 audio. Touch-once: all
three open picture defects batched into ONE re-cut.

**Root-cause lesson for the pipeline:** on a Jesus+family two-shot, "a hand's
breadth" / "faces stay close" / "hand toward her shoulder" reads as ROMANTIC, not
maternal — mother-son beats must state a respectful arm's-length. And "lamp flames
riding the [liquid] surface" paints a flame INSIDE a cup/vessel. Logged to
RUNNER-LESSONS.

---

## RUNNER QC + SHIP (A-auto Machine A, 2026-08-06)

**COMPLAINT LEDGER: none open (at first ship).** `v2_outline.py 49` shows no filed complaint on
row 49. The row-adjacent pronunciation family ("Cana = Kane-a", row 50 card) is
an AUDIO matter, and the audio here is the locked V1 stream (AUDIO LOCK PASS on
assemble) — not re-voiced, per REDO-ALL/SPEAKER law. Row 50/51 are correctly
parked NEEDS-AUDIO on the board.

**Row-specific laws verified (all PASS):**
- COUNT LAW (row-135, "the row's biggest"): SIX stone jars, countable and
  separated, in every jars frame — verified by cropping s21 (plate) and s36 to
  count exactly 6 rims. Jars read as pale STONE (not clay amphorae, not glass),
  waist-to-chest height (scripturally large, 20-30 gal). Water poured TO THE
  BRIM at fill; wine appears at the rims post-miracle (s36).
- THREE-SERVANTS: a consistent man/woman/boy trio across s23/s25 (and drawing
  servant s26). Action-logic: water is poured INTO the jars (fill), reads right.
- MIRACLE UNDEPICTED: no glowing transformation moment; first RED appears only
  at the draw (s29 cup = dark-red WINE, not blood, in a cup at a feast; s36 rims).
- THREE-MARYS: MARY = the MOTHER (blue mantle, serene, ~50). Consistent across
  s03/s08/s09/s15/s16. **Canonical mother-Mary frame for future rows (84/86/87/
  94-96): build-49 s16-and-his-mother-who-knew.jpeg** (per author instruction).
  b08 direction law: Mary crosses TO Jesus (he is in frame). PASS.
- JESUS: one locked face (V2 master-ref — warm Middle-Eastern, dark wavy
  shoulder-length hair, full dark beard; eyes are the V2 reference green, held
  CONSISTENT across s03/s04/s08/s09/s12/s15/s23/s26/s27/s37/s38/s40 — not drift).
  Cream robe every scene; ONLY Jesus wears cream anywhere. No halo/glow. Face
  gate exits 0.
- STEWARD (purple/gold, towel, grey curly beard) and BRIDEGROOM (young, olive
  wreath, maroon) consistent across s30/s32/s33/s34. Stone jars in wide framing.

**Reroll ledger (COST LAW):** 1 reroll of 40 beats = **2.5%** (budget 15%).
- b02 COURT establish: first take was a 3-panel COLLAGE (RUNNER-LESSONS pattern);
  rerolled once → single coherent courtyard wide, then promoted as COURT plate.
Place plates promote-first (no stash match): COURT (s02, 19 beats), JARS (s21,
7 beats). Portraits: STEWARD, BRIDEGROOM ($0.27). No blond-drift on incidental
children observed (RUNNER-LESSONS row-47 pattern) — dark hair throughout.

**FIX-WAVE (residual, minor — NOT garbage, kept best take):**
- s03 ("he was there as a guest") reads night-lamplit; author's note wanted
  golden-afternoon before the b04 dance (wedding joy is lamplit from b04 on).
  Time-of-day progression slightly early to night. Not a scripture-stated time;
  minor continuity, deferred to fix wave.
- s37 and s38 are near-duplicate COURT restored-feast wides. Both valid; minor
  repetition.

Row spend this session ≈ portraits $0.27 + 2 anchors $0.27 + 1 reroll $0.13 +
full run $5.09 ≈ **$5.76**, under the $6.10/row running average. Trend holds.
