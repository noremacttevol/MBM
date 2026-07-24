#!/usr/bin/env python3
"""Narration for build-171-baptized-for-the-dead — 1 Corinthians 15.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

s1 moves JESUS-RED -> SCRIPTURE (light blue). One line out of red. 1
Corinthians 15:29 is Paul asking the Corinthians a question in his own letter;
Jesus is not speaking and a red-letter KJV prints none of it red.

No mixed segments in this build — s1 is Paul from the first word to the last, so
nothing was split.

This build was almost entirely narrator paraphrase carrying Paul's argument, so
two of his verses are lifted back in, both SCRIPTURE:
  s20  1 Cor 15:20  'But now is Christ risen from the dead, and become the
       firstfruits of them that slept.'
  s22  1 Cor 15:22  'For as in Adam all die, even so in Christ shall all be made
       alive.'
These matter here more than in most builds. Verse 29 only makes sense because of
verse 20 — Paul's question about baptism for the dead rests on the resurrection
he has just finished proving. Putting v20 back on screen lets the viewer see the
argument stand up instead of being told it does. s20 is followed by n4a
('Christ rose.') which retells it, and s22 by n5a.

All original ids kept (n0, s1, n1, n2, n3, n4a, n4b, n5a, n5b, card). New ids
are s20 and s22 only. Beats reuse ST5 and ST6; no new artwork. n5a and n5b swap
stills so the new beat sits cleanly — ST6 then ST7 — and both stills are still
used exactly once.

MILK: the doctrine is left entirely to Paul. The video never explains temple
work, never names an ordinance the viewer has not met, and never argues the
practice. It quotes the question Paul asked and lets it sit. A viewer who later
learns what the question implies will find the video was right all along.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    # 1 Corinthians 15:29
    ("s1", SCRIPTURE, "Else what shall they do which are baptized for the dead, if the dead rise not at all? why are they then baptized for the dead?"),
    ("n1", NARRATOR, "The only reason to do such a thing is the quiet hope that the dead are not gone forever."),
    ("n2", NARRATOR, "Baptism stands for new life — a beginning, not an end."),
    ("n3", NARRATOR, "So the work done for those who've passed is built on one promise: that death is not the last word."),
    # 1 Corinthians 15:20
    ("s20", SCRIPTURE, "But now is Christ risen from the dead, and become the firstfruits of them that slept."),
    ("n4a", NARRATOR, "Christ rose."),
    ("n4b", NARRATOR, "And because He rose, the grave loses its grip — for Him first, and then for all who belong to Him."),
    # 1 Corinthians 15:22
    ("s22", SCRIPTURE, "For as in Adam all die, even so in Christ shall all be made alive."),
    ("n5a", NARRATOR, "The ordinance done in love reaches across the veil."),
    ("n5b", NARRATOR, "Offering every soul the chance to choose."),
    ("card", NARRATOR, "Death separates for a while, not forever. Because He livez, there is hope for every name on the other side of the veil."),
]

# Homographs this build decides for itself (never auto-replaced globally).
SPOKEN = {}
SPOKEN.update({'slept': 'slehpt'})  # 2026-07-21: Steffan reliably reads plain "slept" as "SUCKED" in 1 Cor 15:20 (2/2 takes). 'slehpt' round-trips "slept" clean (A/B in Steffan). Caption keeps KJV "slept".


async def main():
    os.makedirs("audio", exist_ok=True)
    for name, speaker, text in SEGMENTS:
        flagged = [w for w in audit(text) if w not in SPOKEN]
        if flagged:
            print(f"  ! {name}: undecided homograph(s) {flagged}")
        await save_speaker_narration(spoken_text(text, SPOKEN, speaker), speaker,
                                     f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3  [{speaker}]")


if __name__ == "__main__":
    asyncio.run(main())
