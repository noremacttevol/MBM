#!/usr/bin/env python3
"""Narration for build-181-morning-stars-sang — Job 38.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

The one scripture beat was painted JESUS-RED. Job is Old Testament, so it
cannot be red - and it is the LORD himself speaking out of the whirlwind, in
first person, which makes it GREEN, not blue:
  s1  Job 38:7  'When the morning stars sang together, and all the sons of
                 God shouted for joy?'                            RED -> GOD

Worth being careful here, because on its own s1 does not LOOK like Deity
speaking - there is no 'I' in it. But it is the tail of a question God started
in verse 4, and the question mark at the end of the segment is the giveaway: it
is still God's sentence. Blue would have made it read as Job's commentary, or
the narrator's, when in fact God is the one asking.

LIFTED ONE VERSE out of narrator paraphrase, and it is what makes s1 make sense:
  g4  Job 38:4  'Where wast thou when I laid the foundations of the earth?
                 declare, if thou hast understanding.'            NEW, god
n1a and n1b were paraphrasing this verse without quoting it, which left s1
dangling as a question nobody had asked. With g4 in place, the viewer hears God
start the question and then finish it three beats later, exactly as Job heard
it. g4 sits on ST4 with n1b, so no new artwork.

Placement note: g4 goes AFTER n1b rather than between n1a and n1b. n1a and n1b
are two halves of one sentence - 'Before there were people to suffer or to
doubt, / the foundations of the earth were being laid' - and wedging a verse
into the middle of it would break the line the editor built.

ADDED n1r - a narrator retelling of Job 38:4 immediately after it, on ST6 ahead
of n2. Required by the retelling rule and it also sets up the shape of God's
answer: he replies to a hard question with a harder one, and somehow that is
comforting rather than cruel.

NO SPLIT anywhere in this build. Both quoted lines are unbroken Deity speech.

Nothing left as paraphrase from uncertainty; both are verbatim Job 38:4 and 38:7.

WHY-LAW: milk. Job asked why and God answered by showing him the first morning,
when the stars sang. The answer is not an explanation - it is a reminder of who
is holding the thing. Warm, not crushing.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import GOD, NARRATOR

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "Job had asked God hard questions. And God answered — not with explanations, but by taking Job back to the very first morning."),
    ("n1a", NARRATOR, "Before there were people to suffer or to doubt,"),
    ("n1b", NARRATOR, "the foundations of the earth were being laid."),
    # Job 38:4
    ("g4", GOD, "Where wast thou when I laid the foundations of the earth? declare, if thou hast understanding."),
    ("n1r", NARRATOR, "Where were you, God asked him, when I laid the foundations of the earth? Tell me, if you know. It sounds severe until you notice what it really does — it lifts Job's eyes off his own wreckage and sets them on something older and steadier than his pain."),
    ("n2", NARRATOR, "And when that happened, something astonishing broke out in the sky."),
    # Job 38:7
    ("s1", GOD, "When the morning stars sang together, and all the sons of God shouted for joy?"),
    ("n3", NARRATOR, "The stars themselves broke into song. Creation was not a cold accident — it was a celebration."),
    ("n4", NARRATOR, "The God who sang the world into being is the same one listening to your questions today."),
    ("card", NARRATOR, "The stars sang when the world began. Your story is still being written by the same hand."),
]

# Homographs this build decides for itself (never auto-replaced globally).
SPOKEN = {}


async def main():
    os.makedirs("audio", exist_ok=True)
    for name, speaker, text in SEGMENTS:
        flagged = [w for w in audit(text) if w not in SPOKEN]
        if flagged:
            print(f"  ! {name}: undecided homograph(s) {flagged}")
        await save_speaker_narration(spoken_text(text, SPOKEN), speaker,
                                     f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3  [{speaker}]")


if __name__ == "__main__":
    asyncio.run(main())
