# QC / RUNNER HANDOFF — build-54-the-leper (Mark 1:40-45)

## C-FIX 2026-08-07 (Machine A `Dev`) — "leprosy on Jesus's hand" complaint CLOSED

> Cameron (reviewer complaint on the shipped cut): *"1:01 looks like Jesus had
> lepracy on his hand. That is wrong."*

**COMPLAINT LEDGER (one line per open complaint, what THIS cut does):**

| time | beat / file | defect | fix in this cut |
|---|---|---|---|
| 1:01 | b14 `s14-touched-before-healed` | Jesus's own hand + forearm on the leper's shoulder carried pale, ashen, scaly leprosy-like patches — read as Jesus having leprosy | targeted image-EDIT pass: ONLY Jesus's hand/wrist/forearm repainted as healthy warm olive-brown skin; leper keeps his marks; faces, cream robe, doorway, lighting, crop byte-identical |
| 0:52 | b12 `s12-and-touched-him` | SAME root cause one beat earlier — Jesus's hand on the leper's neck showed the ashen bleed | same targeted edit — Jesus's hand now clean healthy skin, leper's face-marks kept |

**Root cause (swept touch-once):** the model painted the leper's "ashen scaled
skin" texture onto whatever skin sits at the point of contact — so it bled onto
Jesus's hand ONLY in the two frames where his hand rests on the leper's marked
skin (b12 neck, b14 shoulder). Swept every touch frame: **b11** (hand mid-reach
in open air) clean, **b13** (close on Jesus, hand at bottom) clean, **b15** (leper's
healed arms out) clean — only b12 + b14 carried it, both fixed. The disease now
lives only on the leper, never on Jesus, in every frame of the video.

**Method:** row-39 targeted image-edit pass (attach finished frame → gemini-3-pro-image
→ change ONLY the named skin, keep every other pixel), candidate QC'd full-frame
(FACE-BOARD: no new figure, no crop/light drift), promoted over the original.
**AUDIO LOCK PASS** SHA256=8691209c…39ef — narration byte-identical, NOT a re-voice.
**Cost:** 2 edits × $0.134 = **$0.27**, 0 discarded takes → **0% rerolls** (well under
the ≤15% budget and the $6.10/row average).

---


Lesson-12 + complaint-corpus pass done 2026-08-05 (Machine A). `--check`
PASSES, zero WARNs. 24 beats, ~137 s.

## Coverage shape — DISTANCE IS THE STORY

Three true wides with stated geometry, each a distance-thesis frame:
b02 (the enforced apartness — road and rocks in one profile), b10 (the
geometry of compassion — crowd at maximum distance, Jesus at minimum),
b24 (the closing convergence — streams of people converging ON the one
figure). Eleven flips including b01 and b23, both SINGLE figures in
empty country (phantom-people trap; b23 is Jesus alone in the desert —
an injected crowd would reverse the verse's meaning).

## CONTENT-CARE — leprosy with dignity

- The disease reads as PATCHED, ashen-marked skin on forearms/hands and
  the covered lower face (Lev 13:45 clothing law: torn clothes, covered
  lip) — never gore, never missing features, never horror makeup.
- The cleansing (b15) is bared forearms CLEAR — warm whole skin where
  the marks were. Before/after must be the SAME man's arms (row-15
  class: no grey corpse tones in the sick state; ashen-marked but
  alive).
- THE TOUCH (b11-b14 family) is the story's center: Jesus's hand lands
  on him BEFORE the healing — the crowd's horror at the touch is the
  point. No glow, no effect at the contact.

## Complaint-corpus checks

- **Direction (row-83):** b05 he descends TOWARD the distant crowd
  (crowd in frame); b20 Jesus points him toward the town and the man
  turns THAT way; b21 he strides toward the gate (gate in frame); b24
  the streams converge inward. Every vector anchored.
- **Identity (32/62/91/102):** the LEPER is the same man ragged and
  restored — face-board across the arc; his healed frames show the
  same face, cleaner.
- **Plates:** ROADSIDE←38, VILLAGE←38 wired + committed. WILDS
  promote-first from b01 (`assets/s01-...jpeg`, single-figure broken
  country — the plate carries the rocks, not the man).
- The crowd RECOILS in b06-b11 — varied real recoil, no uniform
  choreography (rows 90/107).
- Only Jesus wears cream.

---

## RUNNER QC — A-auto (Machine A `Dev`) 2026-08-06

**COMPLAINT LEDGER: none open.** `v2_outline.py 54` surfaced no filed
complaint for this row. Nothing to answer; nothing regressed.

**Build:** 24 beats + 1 LEPER portrait. WILDS promoted from b01 (single-figure
broken country, no man in the plate); ROADSIDE<-38, VILLAGE<-38 wired.
`--check` PASS. AUDIO LOCK PASS (SHA256 8691209c...39ef). 19.7 MB / 154 s.

**Reroll count: 0 of 24 beats (0%).** Well under the 15% COST LAW budget.
Every frame passed light QC on the first take.

**Cost:** portrait $0.13 + b01 anchor $0.13 + main gen $3.08 = ~$3.34/row,
well under the $6.10 running average -- trend DOWN per the COST LAW.

**Light-QC pass (all 24 viewed once):**
- Realistic biblical photography throughout -- no cartoon, no mixed styles.
- Leprosy shown with dignity: covered lower lip (Lev 13:45), ashen patched
  skin on face/forearms, wrapped hands -- never gore. Cleansed frames
  (s15/s16/s17) show the SAME man, skin clear.
- Only Jesus wears cream; crowd/leper figures in brown/olive/grey.
- Scale gate PASS -- Jesus ordinary-sized in every multi-figure frame; no giant.
- Directions anchored -- s05 toward crowd, s20 points to gate (gate in frame),
  s24 streams converge inward on the one figure.
- Beard/identity consistent for leper and Jesus across the arc.
- No modern objects, no lens-staring, dark hair on all crowd/children.
- Captions bottom-band only; closing question card clean margins.

**OBSERVATION (not a reroll -- reference-level, logged for the wave):** Jesus's
eyes read green/hazel, most visible in the s13 "I will" close-up. FAITHFUL to
the locked V2 reference JESUS-V2-REF/jesus-v2-face.jpeg, which is itself
green/hazel-eyed, and matches every shipped V2 row (45/46/47/52/53). A reroll
cannot fix it (echoes the ref or breaks face-consistency); editing the reference
is a runner hard-rail violation. If Cameron wants brown eyes, that is a
whole-wave reference change above the runner's scope -- flagged so it is not
silently lost. See MEMORY v2_rebuild_plan "green-eyed Jesus."
