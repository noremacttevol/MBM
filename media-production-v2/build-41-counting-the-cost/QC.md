# QC / RUNNER HANDOFF — build-41-counting-the-cost (Luke 14:25-35)

Lesson-12 pass done 2026-08-05 (Machine A). `v2_prompt.py --check` PASSES
with zero WARNs at handoff. 58 beats, 333.1 s. Audio OK on AUTHOR-BOARD.

## Coverage shape (lesson 12 — do not "fix" this back)

This row is a crowd-and-landscape epic, so 15 true wides survive — the
crowd's scale and its thinning ARE the story. Each wide states its camera
position and to-the-backs geometry in scene text: b01 b02 b03 b06 b16 b17
b22 b23 b26 b32 b34 b40 b49 b55 b57. Nine former wides are now tighter
coverage on purpose (b05 b15 b18 b20 b27 b30 b36 b41 b52) — if a render
comes back as a big group scene on one of those, it MISSED the beat.

The crowd ARC is the row's continuity spine: enormous (b01/b22/b26) →
halted (b03) → shocked (b28/b05/b06/b15) → thinning (b40/b41) → remnant
(b48/b49/b52) → quiet column at dusk (b55/b56). The light ages with it:
bright afternoon → long amber → deep dusk. Check both progressions run
ONE direction across the assembled cut; a bright-afternoon frame after
b40 is a continuity failure even if the frame is beautiful.

## b57/b58 — the candid-lock fix (do not regress)

The old scene text ordered Jesus to face and look INTO the camera at the
close. The shared CANDID-FRAME lock forbids lens-gaze on every beat, so
those prompts fought themselves. The rewritten b57/b58 keep the
invitation but rest his eyes and extended hand a breath PAST the lens.
If a render comes back with pupils centred on the camera, it fails.

## Place plates (lesson 11)

Wired and committed (PLACE-REF/, PLACE-WIRING.json):
- ROAD ← build-38-persistent-widow b39 (24 beats). Plate is an empty
  evening road; the beats' own prose sets crowd and hour.
- VINEYARD ← build-23-vineyard b03 (8 beats). Same vineyard family as the
  laborers build — cross-video place identity, exactly the goal.

PROMOTE-FIRST (new places):

| Token | Promote from | Then covers |
|---|---|---|
| WARTENT | b07 `assets/s07-second-picture-higher-stakes.jpeg` | b27 b29 b33 |
| FAMILY-house interior* | b09 `assets/s09-you-said-hate-and-everybody.jpeg` | b12 b14 b43 |

*FAMILY is a CAST token (the stash tool lists it as a "new place" because
it cannot tell the difference) — do NOT promote a people-plate. What IS
worth promoting is the family's lamplit supper-room once b09 passes QC,
under the FAMILY token only if the tooling allows a place-style use;
otherwise skip it and rely on the b09 rough-ref for b12's closer angle.

## Row-specific QC traps

- RESTRAINED-CROSS LAW (content-care): b16's posts are EMPTY — no bodies,
  no occupied crossbeams, ever. b17's beam-carrier is unmarked and
  unbloodied; weight and the town's stillness carry it. Any gore, any
  body on a post = automatic reject, no reroll budget spent arguing.
- Armies never meet: b30 is two fire-fields at night (enemy's visibly
  ~2x wider), b32 is three unarmed envoys with an olive branch on open
  ground. No battle, no weapons drawn anywhere in the row.
- The SITTING posture is the row's repeated motif — b18/b21/b35 (builder
  on his stone stack) and b27 (king dropped onto a camp stool) must rhyme:
  seated, bent over the count. b34 folds both sitters into one dusk
  landscape — it is ONE unified scene; any split-panel look fails.
- b23's mockery: the builder himself is ABSENT; farmers point at stones,
  not at a person. Weeds through the courses date the failure.
- b47's two bowls are NEAR-identical; only the surrounding food tells
  them apart. If the powders look obviously different, reroll.
- b10 (Jacob/Leah idiom): BOTH women dignified, neither demeaned — only
  the man's direction of step tells the idiom. No sneering, no shrinking.
- Salt beats (b42/b44/b45/b46/b47) are still-lifes or single-action
  domestic frames — keep them quiet; no drama styling.
- b48's hollow man is pleasant, decent, empty-eyed — never villainous.
- Only Jesus wears cream anywhere, including the far-off cream point at
  the column's head in b01/b26/b49.
- Person-free frames: b11 b13 b19 b29 b30 b38* b39 b42 b46 b47 b50
  (*b38 is hands only) — do not let the model add figures.

## RUNNER QC LOG — first-attempt V2 cut (Machine A, 2026-08-05)

58/58 at native 2K. Portraits: BUILDER + KING only. **WARTENT was NOT given a
portrait** — the tooling had been queueing it as a person (its lock says "dark
goat-HAIR walls", which matched the body-detector); fixed in v2_story_cast.py
this session so places can never be wired in as CHARACTER locks. WARTENT was
promoted as a PLACE plate from b07, exactly as this QC.md asked. ROAD +
VINEYARD carried in. FAMILY correctly left un-plated (author's instruction).
Row ~$8.4; meter 222.84 → 231.42, under the $234.90 ceiling.

**REROLLED (4 frames, all obvious defects, none subtle drift):**
- b07 (the WARTENT plate itself): first take lit the council tent with MODERN
  glass-chimney hurricane lamps. Reroll gave correct first-century clay oil
  lamps. Caught before it became the plate for b27/b29/b33.
- b12: first take rendered a 16:9 image LETTERBOXED inside the 9:16 frame —
  huge blank bands top and bottom, unusable in a vertical video (also a modern
  knit sweater). Reroll is full-bleed 1536x2752.
- b13: re-shot with the first take's modern-looking chair replaced; the beat
  wants "one carved chair alone in clean light" and now reads as a rough
  hand-hewn seat on flagstones — the un-shareable single seat.
- b35: first take put a MODERN SCHOOL SLATE in the builder's hands, chalked
  with a vertical sum in Arabic numerals ("4 + 5 / 30"). Reroll gives a plain
  wooden tally tablet. NOTE for the fix wave: the beat text itself uses the
  word "slate", which is what pulls the model toward a schoolroom object — if
  it ever returns, the cure is in the beat prose, not another reroll.

**PASSED:** crowd scale and thinning read as the story's argument; the tower
ladder (foundation → half-built → mocked → finished) is legible; the king's
council and the envoy ride hold their light; all violence stays off-screen;
cream on Jesus only; no lens-staring; no giant figures; person-free inserts
(scroll, chair, foundation, salt) stayed empty.

**FIX-WAVE (kept):** BUILDER renders fair-haired and blue-eyed — his lock does
say "sandy-brown beard", so this is authored, but he reads more Northern
European than Levantine next to the rest of the cast; worth an author decision
rather than a runner reroll.
