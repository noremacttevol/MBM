# STORY COVERAGE LAW — pictures serve the STORY, never a quota

**Locked by Cameron, 2026-07-19.** Companion to PRODUCTION-BIBLE.md §5 and
CAPTION-LAW.md. This law governs HOW MANY pictures a video gets and WHERE they go.

---

## The law, in Cameron's words

> "It was never actually tailored to the story... it's obvious, made like where
> there's only eight-ten pictures or whatever, and that shouldn't be the rule. It
> should be that the AI can understand where multiple pictures need to be placed
> and can make them perfectly so they can be put where in the story we see fit."

**There is NO fixed picture count.** The old habit of ~7–10 stills per video was a
convenience, not a law. The number of stills is decided by the story's BEATS —
every distinct moment a listener would picture in their head gets its own picture.

## The test for a missing picture

While the narration describes a NEW visual moment — someone moves, reacts,
realizes, jumps, turns, arrives — and the SAME still is on screen, that is a
MISSING PICTURE. If the narrator says it happened, the viewer should SEE it happen.

**The canonical failure (Cameron, John 21 / build-19-shore):** the whole drama —
the stranger calling from the shore at dawn, the tired empty-net fishermen, the
cast on the right side, the net suddenly FULL, John's realization "It is the
Lord," Peter grabbing his coat and LEAPING out of the boat, Peter swimming hard
while the boat follows — was told over ONE picture of Peter swimming. Six or
seven beats, one still. Every beat listed there deserved its own frame.

## How to plan coverage (per video)

1. Read the narration script segment by segment.
2. List every distinct visual beat the words describe (action, reaction,
   realization, arrival, exchange). A beat = something a camera would cut for.
3. One still per beat. Two segments may share a still ONLY if nothing visually
   changes between them. A long segment that moves through several moments gets
   SEVERAL stills, switched mid-segment at the timestamps where the words turn.
4. Emotional turns are beats too: surprise → recognition → joy are THREE faces,
   not one.

## Pictures must AGREE with the words (the second half of this law)

A picture that contradicts its narration is worse than a missing one.
**Canonical failure (Cameron, Road to Emmaus / build-18):** the narration says
Jesus "drew near and went WITH them" — fell into step alongside — but the picture
shows him ahead of them, everyone's backs to camera, nobody walking together. And
another still didn't look like Jesus at all (lock not applied).

Before accepting any still, read the exact narration line it will sit under and
ask: **does this picture show what these words say, at the moment they say it?**
- "fell in step with them" → walking BESIDE them, same direction, same pace
- "called out to them" → distance between caller and hearers, faces turning
- "jumped out of the boat" → mid-leap, boat and water both visible
- "did not recognize him" → they can see him, but faces show no recognition
Direction, position, scale and emotion in the picture must match the sentence.

## Craft rules that carry over (measured, this repo)

- Anti-panel clause on EVERY prompt (see PROMPTS.md conventions) — without it the
  model returns stacked panels/triptychs.
- Enumerate people positionally ("(1) a man in indigo; (2) a woman in green...")
  — models cannot count "four men and four women".
- Character locks byte-identical in every prompt the character appears in, and
  VERIFY the assembled prompt has no unexpanded [TOKEN] before generating.
- Every new/replaced still re-runs the video's build.py and passes
  admin/verify-mp4.sh before delivery.

## Retrofit

This law applies to every NEW build immediately, and retroactively to any video
Cameron denies for storytelling/picture reasons. build-19-shore (John 21) and
build-18-emmaus are the first two retrofits.
