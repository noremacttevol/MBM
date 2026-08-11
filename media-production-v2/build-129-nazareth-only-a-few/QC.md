# QC / RUNNER HANDOFF — build-129-nazareth-only-a-few (Mark 6:1-6)

AUTHORED FROM SCRATCH (prepped + scaffolded + written this session),
2026-08-05 (Machine A). `--check` PASSES, zero WARNs. 14 beats, ~78 s.

## Mary and the family are NEVER depicted

b02/b03 NAME the mother, brothers and sisters — spoken only. No
render may show Mary or any sibling (keeps the three-Marys law
untriggered). The murmuring TOWNSFOLK carry both beats. Automatic
reject if a Mary-like figure appears.

## The townsfolk (villain law)

Familiar ordinary neighbours whose failure is FAMILIARITY — folded
arms, turned shoulders, shuttered faces (b04's quiet human wall).
Never jeering, never a mob. b06 must show a few faces genuinely
ASTONISHED first (Mark 6:2) — the doubt arrives one breath later.

## The few sick folk = THREE (counts law)

Same three across b10-b13: old fevered woman (dark shawl), gaunt
young man (pallet), stooped elder (bound knee). Sequence readable in
b12: one healed-upright, one under his hands, one awaiting. Illness
with dignity (row-15 class): warm living skin, no gore. Face-board
the three.

## The door rhyme (the row's frame)

b09: EVERY door shut, every shutter closed (person-free lane). b14:
ONE door open with lamplight and an eager family. The rhyme must be
the same lane. Early-evening lamplight in b14 is BY DESIGN.

## Jesus beats

b01, b05, b06, b08, b10, b11, b12, b13, b14 (9 of 14) — locked face,
no halo. b05 calm-sad (no bitterness), b08 idle hands in the
incurious noon lane, b11 the marvel = wonder-with-sadness (never
contempt), b13 extreme-close full-palm touch.

## Coverage shape

One true wide with stated geometry: b01 (camera following behind him
up into the town — direction law: INTO Nazareth). File order ≠ story
order (b06 at 3.48s) — build by WINDOW.

- Plates: SYNAGOGUE auto-match from build-05 REJECTED per the
  standing row-73 precedent (Nazareth's synagogue is its own place;
  build-05's wires to 52/55 only). SYNAGOGUE promote-first from b06,
  NAZARETH from b01.
- Clone-crowd check on bench rows (rows 90/107).

---

## RUNNER NOTES (Opus runner, Machine A `Dev`, 2026-08-11)

- Audio pre-flight PASS: V1 mp4 85.767s vs timeline 85.387s (excess +0.380 ≤0.75,
  newer_mp3s=0) → default AUDIO LOCK path, byte-identical V1 narration. BUILDABLE.
- **FORCED NO-PROMOTE on NAZARETH + SYNAGOGUE (row-51 precedent).** The author QC
  named b01→NAZARETH and b06→SYNAGOGUE as promote anchors, but BOTH are Jesus beats
  (jesus=1). `v2_stash --promote` copies the whole frame incl. Jesus-in-cream, and
  wiring that to the other place beats would spawn a second cream figure. NAZARETH's
  only non-Jesus frame (b09) is the SHUT-DOOR lane — too specific a state to be a
  general plate (b14 needs the door OPEN). So both places stay on their TEXT locks;
  PLACE-WIRING.json left `{}`; place uniformity QC'd by eye in the full-cut gate.

---

## ✅ SHIPPED — realistic-v2 (Opus runner, Machine A `Dev`, 2026-08-11)

**COMPLAINT LEDGER: none open** (`v2_outline.py 129` shows no complaint block — fresh
V2 build; the 2026-07-17 ASSEMBLY-B cut predates the review board).

**Cost:** 14 stills @ $1.88 + 1 reroll @ $0.13 = **$2.01**, **1 reroll / 14 = 7.1%**
(budget 15%; well under the $6.10/row + 19%-reroll running average — cost-down trend held).

**Generate:** `v2_gen_api build-129 --ceiling 583.11` — 14/14 clean, no 429s.
**AUDIO LOCK PASS** SHA256 e444040ceb2ed886721d088247aa7728ccdf75f6f4238d91cd0056887ed45c11
(default path — byte-identical V1 narration; excess +0.380 ≤0.75). mp4 19.4 MB / 85.8s.

**Light QC + FULL-CUT GATE (all 14 source stills + one frame/beat from the RENDERED mp4
+ 3 caption frames + card): PASS.**
- Reroll: **s04** came back ROTATED 90° (row-110/51/82 rotation-garbage class) →
  `--only b04 --redo` landed it upright (synagogue, folded-arms townsfolk). Confirmed
  upright in the rendered mp4.
- Jesus (9 beats): ONE locked face, cream-only, no halo, calm eyes, ordinary scale —
  consistent across all. Green/hazel iris = the systemic ref trait (do-not-reroll, lesson).
- Content-care held: NO fire / darkness / wrath-face in any frame; b11 marvel =
  wonder-with-sadness (not contempt); row ENDS on the door OPEN + welcome (b14).
- Mary & the family NEVER depicted (b02/b03 name them, render only townsfolk). Verified.
- Three sick folk (counts law) consistent across b10-b13 (old woman dark shawl / gaunt
  young man pallet / stooped elder bound knee). Illness with dignity, no gore.
- Door-rhyme: b09 every door shut (person-free lane) → b14 one door open, lamplit,
  eager family. Same lane look.
- Direction law: b01 Jesus walking INTO Nazareth (camera behind).
- Captions: white narrator / light-blue scripture (Mark 6:3 townsfolk quote, 6:4 is
  Jesus RED, 6:5 scripture blue) / bottom-band only, synced, art uncovered. Card clean.

**FIX-WAVE (kept, not blocking — background/minor):**
- s03/s04: a distant, small, unlocked cream Jesus at the synagogue reading desk on the
  jesus=0 murmur beats (face reads consistent; too small to lock/reroll cheaply).
- s14: a small background wall-bracket lamp reads slightly modern; the emotional-payoff
  closing frame is otherwise perfect and the foreground clay oil lamp is correct — not
  worth risking the composition on a re-roll.
