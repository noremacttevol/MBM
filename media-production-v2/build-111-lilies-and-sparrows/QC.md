# QC / RUNNER HANDOFF — build-111-lilies-and-sparrows (Matthew 6:25-33)

## ✅ C-FIX SHIPPED — 2026-08-07 (Machine A `Dev`)

**COMPLAINT LEDGER (open at claim):**
- `0:09 picture everything is out o scale and weird.` → **FIXED.** At 0:09 the
  still on screen is beat `v2-r111-b11` / `s11-and-instead-of-an-argument.jpeg`.
  Root cause: the sparrows were rendered grossly OVERSIZED — the birds beside
  Jesus's hand and next to the baby were larger than the infant's head, so the
  whole frame read out-of-scale. Fixed by ONE `--only v2-r111-b11 --redo`
  reroll: the new take renders the sparrows at true small size (proper
  sparrow-to-person proportion), people correctly sized, Jesus ordinary-sized,
  cream robe / locked face / no halo, realistic photographic. Verified in the
  RENDERED mp4 at 0:09. Only this ONE frame was touched — every other still is
  byte-identical, audio is byte-identical (AUDIO LOCK PASS, same SHA256).

**Result:** 1 reroll (1/29 = 3.4% of beats — under the 15% COST-LAW budget).
Spend this row this session ≈ $0.13 (one still, 0 portraits). AUDIO LOCK PASS
SHA256=51aba66bab0cb54d1f1ff6688893d836b5f05becbc02c12f069dbbf625b6cd8a
(byte-identical to the shipped audio), 174.3s, 21.0 MB. Deployed + live-verified.

**New defect class fed to RUNNER-LESSONS:** oversized birds/animals — a beat
whose scene names small wildlife working the foreground ("sparrows working the
seed") can render the birds giant, bigger than a nearby child's head; height-
check animals against the people in every nature frame, not just figures.

---


Lesson-12 + complaint-corpus pass done 2026-08-05 (Machine A). `--check`
PASSES, zero WARNs. 29 beats, ~162 s.

## The living exhibits (nature-frame laws)

- SPARROWS: real small brown birds, busy and unposed — never
  songbird-pretty; countable where small groups show (b07 is
  PERSON-FREE — birds only, protected from phantom people).
- THE ANEMONE (b10, the "lily"): one red anemone lifted gently in his
  fingers — the region's actual flower, TIGHT frame; "Solomon in all
  his glory" is spoken, never depicted (no palace insert).
- The dry-grass handful (b16): today-alive, tomorrow-oven — the
  contrast held in one hand.
- No worry is cartooned: the ring's knotted hands and tired faces are
  ordinary working people's (90/107 variety; row-15 dignity).

## Coverage shape

Three true wides with stated geometry: b01 (the worried ring), b03
(BEHOLD — the directing arm and turning gazes in profile: the
gaze-redirect is the sermon's method, row-83 law as teaching), b18
(the whole classroom at rest from the side). Eight flips including
two person-free nature frames.

- MEADOW promote-first from b07's bird frame or b28's cared-for gold;
  RING is cast — no plate.
- Seek-ye-FIRST (b26): the hand lifts skyward FIRST, then the open
  palm to the ordinary things — the ORDER of the two gestures is the
  verse; if reversed, reroll.
- Warm day into gold; only Jesus wears cream.

---

## RUNNER SHIP — A-auto Machine A, 2026-08-06 (REALISTIC V2)

**COMPLAINT LEDGER: none open.** `v2_outline.py 111` shows no filed complaints
on this row. (Prior V1 was a 10-still Flow cut, Machine C 2026-07-15 — replaced
entirely by this 29-still realistic rebuild.)

**Result:** 29 realistic stills @ 2K, AUDIO LOCK PASS
(SHA256=51aba66bab0cb54d1f1ff6688893d836b5f05becbc02c12f069dbbf625b6cd8a),
174.3s, 20.9 MB. **0 rerolls (0% — well under the 15% COST-LAW budget).**
Spend this row ≈ $3.88 (29 stills × $0.134, 0 portraits, 0 rerolls) — under the
$6.10 running average. MEADOW promote-first from b07's bird frame (person-free,
Sea-of-Galilee wildflower meadow); RING was cast (no plate) per author QC.

**Light-QC pass (every frame viewed once vs must_show / RUNNER-LESSONS):**
- All 29 frames realistic photographic — NO cartoon, NO mixed-style frame
  (Law 14 clean). Only Jesus wears cream in every frame; Jesus's locked
  face/dark-wavy-hair/full-beard consistent throughout.
- Sparrows real, brown, busy and unposed; countable in the count frames
  (s04/s06/s07/s15/s24/s28). Anemone (s10) is the region's red anemone;
  Solomon's glory spoken not depicted (s14 uses a purple market cloth as the
  "king's robes" contrast — no palace insert, per author QC).
- s26 (seek-ye-first): skyward hand raised FIRST + open palm to the people —
  gesture ORDER correct per author QC.
- No modern objects, no lens-stare, no burned-in text, no collage, no sky-wires,
  good anatomy/scale, no beard drift. Jesus's green/hazel eyes are the known
  baked-in V2-reference trait (RUNNER-LESSONS) — NOT rerolled.

**FIX-WAVE (minor, non-garbage — kept per COST LAW, no reroll):**
- s09: mother wears a plain metal band ring — reads faintly modern; rings are
  period-plausible so borderline, not a clear anachronism.
- s23: tight Jesus portrait against a plain earthen wall vs the meadow setting —
  ambiguous (could be outside a house); minor continuity.
- s08: warm golden-hour light on the tender "you are worth more" close-up vs the
  midday wides — reads intentional, not jarring.
