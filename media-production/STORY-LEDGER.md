# STORY LEDGER — supporting notes (SUBORDINATE to the authoritative docs)

> ⚠️ **THIS FILE IS NOT THE SOURCE OF TRUTH. Read these first, in order:**
> 1. **`AUDITS/2026-07-20-repeat-audit.md`** — the authoritative dedup (Cameron-ordered).
>    It already found & replaced SIX repeats (#71,128,133,134,137,140). Dedup is DONE.
> 2. **`STORY-INTEGRITY-LAW.md`** — the reconciled standing law (rules + Pentecost + bench).
>
> This ledger was written 2026-07-23 by a parallel session BEFORE it read the Jul-20
> audit, so two of its early calls were WRONG and are RETRACTED below. Kept only for the
> one-event/blend-witnesses rule statement, which matches the authoritative docs.

> ### RETRACTIONS (do not act on the old versions of these)
> - ❌ "Only ONE true duplicate" — WRONG. There were SIX; five were already swapped in
>   the Jul-20 audit, so the current queue only still showed #140. Dedup already complete.
> - ❌ "MERGE #44 two-debtors → #74" — WRONG. Both audits rule **KEEP #44** (it's an
>   APPROVED video; the parable vs. the woman it was told for is an allowed add-on).
> - The #74/#82 anointing "doctrine call" is not raised by either audit — drop it unless
>   Cameron asks.

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

### FULL 200 AUDIT RESULT (2026-07-23) — the library is NOT riddled with duplicates
Swept all 200 by event vs scripture ref. **Only ONE true story-duplicate exists, and
it's already fixed.** Cameron's fear ("did we run out of stories?") is unfounded — ~199
of the 200 are genuinely distinct. Action list is tiny:

| # | title(s) | verdict | action |
|---|---|---|---|
| — | build-140-road-runs-both-ways | **TRUE DUP — REPLACE (done)** | dead 2nd Prodigal; #140 is now Naaman. **Delete the folder.** |
| #44 ↔ #74 | Two debtors (Luke 7) inside Woman washed his feet (Luke 7) | **MERGE→#74** | one scene; fold the parable into #74, retire #44's slot for a NEW story |
| #74 ↔ #82 | Foot-washing (Luke 7) vs Anointing at Bethany (Mark 14) | **CAMERON'S DOCTRINE CALL** | scholars split: same anointing or two? If one → merge; if two → keep both distinct. Flagged, not guessed. |
| #121 ↔ #139 | Salt & light (Matt 5) vs Lamp on a stand (Mark 4) | **REVIEW — likely KEEP** | different sermons, same "light" image; keep unless they play as a repeat |

**Same event, DIFFERENT doctrinal purpose — all KEEP (do NOT re-narrate the scene;
use the ONE line for the member-shelf point):**
- #69 Baptism of Jesus (Matt 3) ↔ #169 "to fulfil all righteousness" (proper authority)
- #103 Peter's confession (Matt 16) ↔ #162 keys of the kingdom (priesthood keys)
- #95 Thief on the cross ↔ #134 "Today...paradise" (spirit world)
These are legitimate: they teach doctrine from a scene, they don't re-tell the story.

**Net for Cameron:** you need ~1–2 NEW replacement stories at most (the #44 slot, plus
#140's slot which Naaman already fills), NOT dozens. Claude will propose the #44 swap
for approval. Everything else is KEEP.

## Workflow discipline (multi-machine)
- Push every change here immediately; other sessions are working the same problem and
  must agree. `git pull --rebase --autostash origin main` before push.
- This box (Machine C) has no node → source fixes + pushes here; board/site deploy runs
  on a node machine. See [[shared-git-tree-multisession-hazard]].
