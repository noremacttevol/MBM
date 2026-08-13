# QC / RUNNER HANDOFF — build-140-naaman-washes (2 Kings 5:1-14)

## ✅ AUTHOR-REFRAMED — Option B taken (2026-08-13, Machine A `Dev`, Fable-5 author lane, $0 stills)

The story-rejection complaint has been fixed at the AUTHOR level and the row is
Ready ✅ for the runner to build its 16 stills. The park is CLEARED.

Cameron's complaint (`v2_outline.py 140`, was OPEN):
> "What the f*** is this? Did we just run out of stories that were good about
> Jesus to tell? And now you are using somebody else's gospel to redo the same
> exact story we told earlier of the prodigal son… you shouldn't use 2 different
> people telling the same story about Jesus… did we seriously run out of Jesus
> stories…"

**Root cause (confirmed):** the story is NOT the problem — 2 Kings 5 (Naaman) is
a genuinely distinct Bible account. The problem was that the authored `n5` MORAL
had been grafted onto the prodigal "coming home" lesson Cameron already has at
row 2 — *"It was the way back… if you've been away… come back again."* That
duplication is exactly what he rejected.

**The reframe (Option B — keep the story, change the moral to Naaman's OWN
lesson):**
- **n5 re-authored** from the prodigal "way back / come back again" framing to
  Naaman's actual lesson — humble obedience, and the pride that almost forfeits a
  FREE gift:
  *"The instruction wasn't beneath him. His pride nearly cost him everything.
  God's mercy isn't impressed by rank or gold — it asks only that we humble
  ourselves and obey. Whatever simple thing He is asking of you, don't be too
  proud to do it."* (Both V1 `media-production/build-140/make_narration.py` and
  the V2 copy carry the new text; captions flow from V1 SEGMENTS via extract_beats.)
- **n5 re-voiced** in ElevenLabs **Brian** (narrator, engine-parity with n0–n4),
  written to `media-production/build-140-naaman-washes/audio/n5.mp3` (15.60 s).
  `AUDIO_FROM_V1_SEGMENTS = True` set in beats_v2.py so the V2 cut rebuilds its
  track from the re-voiced V1 mp3s (the stale V1 mp4 is NOT stream-copied).
- **beats.json rebuilt** (`extract_beats 140`) → new n5 timing + shifted card +
  total 99.34 s. All 16 beat **windows re-derived** to the new timeline.
- **b15 image reframed** ("the way back" → *what pride nearly cost*: Naaman clean
  in the shallows looking back at his heaped, abandoned armor + chests of gold).
- **b16 image reframed** (a modern person "kneeling again… come back again" → the
  mighty captain HIMSELF kneeling humbled in the Jordan; locked to NAAMAN + JORDAN,
  in-world, no modern room). This kills the prodigal "return" motif in the picture
  as well as the words.
- The closing **card** ("He almost rode away from his healing because it sounded
  too simple. Do the simple thing.") was already Naaman-specific — pride nearly
  forfeiting a free healing — and is KEPT unchanged (byte-identical audio).

`v2_prompt.py --check` PASS (16 beats). `audio_audit --rows 140` clean (0
old-voice, new ElevenLabs n5 recognized). Cost: $0 image spend; one short
ElevenLabs segment re-voice.

### COMPLAINT LEDGER (runner: copy the review-card line, verify before ship)
- **OPEN — "using somebody else's gospel to redo the same exact prodigal-son
  story / did we run out of Jesus stories":** FIXED by re-authoring the n5 moral
  from the prodigal "way back / come back again" lesson (a duplicate of row 2) to
  Naaman's own distinct lesson — humble obedience and the pride that nearly
  forfeits a free healing — in both the narration (re-voiced) AND the closing
  images (b15 abandoned pride, b16 the great man kneeling humbled). The story is
  kept; only the duplicated moral is gone.
- **Review-card flag for Cameron:** *"Reframed Naaman off the prodigal 'coming
  home' moral you flagged — it now teaches humble obedience (pride nearly cost him
  a free healing), which no other story tells. Same account, its own lesson."*

**Resume (runner):** `python3 media-production-v2/v2_prompt.py
build-140-naaman-washes --check` then the normal runner loop — build the 16
stills, assemble (AUDIO_FROM_V1_SEGMENTS rebuild), ship.

---

AUTHORED FROM SCRATCH, 2026-08-05 (Machine A). `--check` PASSES, zero
WARNs. 16 beats, ~91 s. **(Authored BEFORE the story-rejection complaint was
addressed — see park block above; the mechanics below are sound but the moral
is unresolved.)**

## Leprosy with total dignity (row-15 class, strictly)

The affliction exists ONLY as linen wrappings at wrist/neck + his
guarded privacy (b02). NEVER lesions, skin close-ups, or grotesque
detail, in any frame. b14's restoration = WHOLENESS and WONDER
(clean warm forearm, wrappings loose in his fist) — no before-gore
contrast. Automatic reject on violation.

## Wrapping state machine (prop-board)

Wrist + neck wrappings present b01-b12 (dark with river water in
b12) → GONE from b14 on. If a wrapping appears after the seventh
dip, reject.

## The seven-dips count (counts law)

b12 = early dips (once, twice), armor visibly LEFT on the bank.
b13 = the SEVENTH, no shortcut. The count discipline is the story.

## Character laws

- NAAMAN: proud hurt, never villainy — great in every register
  (pride, rage, humility, wonder). Face-board across 11 frames.
- THE MAID: a captive child with full dignity and warmth — earnest,
  unafraid; her certainty (b04) is the story's engine.
- The servants (b10/b11): humble AND brave — reasoning up at the
  rage on open palms.

## The plain-vs-great engine

b05: glittering column + open silver chests before the lovingly
PLAIN little house (never shabby). b06: the half-open door + calm
messenger — the slight is architectural. b09: the column wheels
AWAY (direction law), the house unmoved behind the dust.

## Coverage shape

One true wide with stated geometry: b01 (camera down the parade
line past the spearmen's backs). No Jesus beats (Old Testament
row). b16's lamplit kneeling application is period-neutral, no
modern objects (row-7). File order = story order.

- Plates: HOUSE --take from build-16 REJECTED (the Bethany dusk
  lane again — 11+ prior declines; Elisha's house is its own
  place). HOUSE promote-first from b05, JORDAN from b12.


## 🔁 NEW STORY SPEC (2026-08-13) — this row is no longer Naaman

Cameron rejected the Naaman story itself (duplicate of #2 Prodigal Son's come-home moral).
Row 140 is now **THE BRONZE SERPENT — Numbers 21:4-9 + John 3:14-15**, chosen via an
external-AI gap review of the full 200 lineup and handed back by Cameron 2026-08-13.

- **Moral (plain words):** look in faith to God's provision and live — simple, desperate
  looking that saves. This is the event Jesus HIMSELF used to explain his cross:
  "as Moses lifted up the serpent in the wilderness, even so must the Son of man be
  lifted up" (John 3:14, KJV — close the video on this verse card).
- **Not a dupe:** #4 Nicodemus at Night is the John 3 *conversation*; this is the
  historical *type* it points to. Verified: no serpent/Numbers-21 story exists anywhere
  in the 200.
- **Era:** Old Testament — NO Jesus in frame, nobody wears cream; Moses per CAST rules.
- **CARE:** real venomous snakes in a real wilderness camp — dread, not horror-gore;
  the bronze serpent lifted on the pole is the visual anchor (cross foreshadow),
  people across the camp turning their faces toward it to live.
- **Author fresh in `build-140-bronze-serpent/`** (this folder is the archived Naaman
  package — do not delete, do not reuse its beats).
- Alternates (future gap-fills only, do not build): Passover Lamb (Ex 12:1-13),
  David Spares Saul (1 Sam 24).
