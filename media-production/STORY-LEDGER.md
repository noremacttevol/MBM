# STORY LEDGER — the shared law for WHICH stories exist and WHY (Cameron, 2026-07-23)

> **Every Claude Code session on every machine reads THIS file before touching story
> content.** It is the agreement so all sessions converge. If you change the plan,
> change it HERE and push, then tell Cameron. Do not fork the story set in your head.

## The decision (Cameron + Claude, 2026-07-23)

Cameron rejected the duplicate-story problem (complaint #140: a SECOND Prodigal Son,
`build-140-road-runs-both-ways`, "fatted calf"). Root cause: the story-picker treated
**a Bible passage** as the unit and, to hit a hard count of 200, reached for the same
*plot* from a different passage — telling one story twice. The fix is a change of law,
made the way the LDS Jesus would want it:

### THE STORY LAWS (new — bind every session)
1. **Chase TRUE, not a number.** Jesus never padded to hit a quota. Quota-over-truth is
   dead. A story earns a slot ONLY if it feeds a heart something new. A near-repeat
   feeds no one and is cut. The count (200) is a shelf size, not a mandate to invent
   filler — and the Bible has far more than 200 genuine distinct moments, so cutting
   duplicates never forces a retread; we refill freed slots with genuinely NEW stories.
2. **ONE EVENT = ONE VIDEO.** Never "one gospel passage = one video." If an event
   appears in more than one gospel, it is told ONCE.
3. **Four witnesses, one Christ (the law of witnesses — "in the mouth of two or three
   witnesses").** When an event is in multiple gospels, BLEND them into one telling:
   fullest account as the spine; each other writer's UNIQUE detail woven in (Mark's
   vivid touch, Luke's compassion, John's meaning, Matthew's fulfillment) — one
   brushstroke each; the KJV card quotes ONE writer (the strongest wording), not all
   four. This is "justice to each person's differences": every witness contributes to
   ONE painting, never four near-identical ones.
4. **Keep the milk→meat arc** (comfort / being-seen first → goodness of Jesus →
   Restoration through their own scripture). Story first, never a survey or lecture.
5. **Less in-video repetition** (tightening + ElevenLabs): if the narrator says a thing
   in plain modern words and the KJV line right after says the same understandable
   thing, DROP the echo. Narrator sets it up; scripture lands the point ONCE.

## THE LEDGER — KEEP / MERGE / REPLACE (Claude fills this; Cameron approves REPLACE)
Before any story is built, check it here. Status meanings:
- **KEEP** — unique event, earns its slot → build/keep.
- **MERGE→#N** — same event as #N → fold new detail into #N, do NOT ship a 2nd video.
- **REPLACE** — true duplicate/filler → drop; Claude proposes a NEW subject; Cameron
  approves the swap BEFORE any stills are made.

### Confirmed so far (2026-07-23)
| item | status | note |
|---|---|---|
| build-140-road-runs-both-ways | **REPLACE (done)** | dead 2nd Prodigal; already swapped for #140 Naaman. Delete the folder. |
| #44 The two debtors (Luke 7) | **MERGE→#74** | parable is spoken INSIDE the foot-washing scene |
| #74 Woman washed his feet (Luke 7) | KEEP (host of the merge) | |
| #58 Five thousand / #59 Four thousand | KEEP both | genuinely 2 different miracles; video must say "a second time" so it doesn't read as a repeat |
| #134 "Today...paradise" | KEEP | reuses ONE thief line for a different purpose (spirit world); don't re-narrate the whole #95 scene |
| #2 / #8 / #21 (Luke 15 trio) | KEEP all | deliberately 3 angles of one sermon, not duplicates |
| Sermon-on-the-Mount cluster (#47,109–112,121–127,139,188) | KEEP | separate teachings, not duplicates |

_(full 200-row audit in progress — Claude adds rows here and pushes as it goes.)_

## Workflow discipline (multi-machine)
- Push every change here immediately; other sessions are working the same problem and
  must agree. `git pull --rebase --autostash origin main` before push.
- This box (Machine C) has no node → source fixes + pushes here; board/site deploy runs
  on a node machine. See [[shared-git-tree-multisession-hazard]].
