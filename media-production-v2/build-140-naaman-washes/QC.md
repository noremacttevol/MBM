# QC / RUNNER HANDOFF — build-140-naaman-washes (2 Kings 5:1-14)

## 🅿️ PARKED-STORY — RUNNER WILL NOT BUILD (2026-08-11, Machine A `Dev`, Opus runner, $0/0 stills)

**Row 140 is BLOCKED by an OPEN reviewer complaint that rejects the STORY, not
the pictures — so a picture build cannot fix it and would ship the exact
rejected cut (the worst failure this pipeline can produce). Ready ✅ CLEARED →
this row is AUTHOR-LANE work + a Cameron story decision.**

Cameron's own words (`v2_outline.py 140`, tagged OPEN — MUST BE FIXED):
> "What the f*** is this? Did we just run out of stories that were good about
> Jesus to tell? And now you are using somebody else's gospel to redo the same
> exact story we told earlier of the prodigal son… you shouldn't use 2 different
> people telling the same story about Jesus… did we seriously run out of Jesus
> stories…"

**Why a rebuild does NOT fix it (root cause):** the complaint is about STORY
SELECTION + MORAL DUPLICATION, not any frame. The authored narration still
carries the prodigal "coming home" moral grafted onto an Old-Testament figure —
`n5`: *"The instruction wasn't beneath him. It was the way back… If you've been
away, the way back may look almost too simple — pray again, read again, come
back again. Do the simple thing."* That IS the Prodigal-Son lesson Cameron
already has (row 2). Generating 15 realistic Naaman stills over this same moral
= re-shipping the story he rejected. There is no COMPLAINT LEDGER line the
runner can honestly write ("what in this cut fixes it") because nothing in a
picture build changes the moral he objected to.

**Why the runner cannot fix it here:** hard-rail #1 forbids editing scene text,
locks, or any beat's moral. The fix is a STORY DECISION above runner scope:
  - **Option A — CUT Naaman from the 200** (Cameron: "find some other way to get
    into things that would be good for people"). Purge the row like the prior
    prodigal dupe it replaced.
  - **Option B — AUTHOR-REFRAME** the moral away from the prodigal "way back /
    come back again" framing to a distinct lesson (e.g. *the pride that almost
    forfeits a free healing* / *God's power reaching a foreigner outside
    Israel*), so it no longer duplicates row 2. Then re-set Ready ✅.
Either way it goes back to the FABLE-5 AUTHOR lane, not the runner.

**THE ONE QUESTION FOR CAMERON:** cut Naaman entirely, or keep it with a
non-prodigal moral? (This is a which-story-to-cut / doctrine fork — yours alone.)

**Resume (only after the author reframes AND re-sets Ready ✅):**
`python3 media-production-v2/v2_prompt.py build-140-naaman-washes --check` then
the normal runner loop. Until Ready ✅ returns, no session builds this row.

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
