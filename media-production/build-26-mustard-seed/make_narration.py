#!/usr/bin/env python3
"""Narration for build-26-mustard-seed — Matthew 13.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

Matthew 13:31-32. A parable - a red-letter KJV inks the whole thing, so j1
stays RED. Nobody else speaks in it, so nothing moved out of red and no new
scripture was lifted.
The one structural change: the old template played ONE audio file (j1) across TWO
different stills. Template A is one beat per still, so j1 is split at the exact
caption boundary the old build already used - j1 keeps its id and carries Matthew
13:31, j1b carries 13:32. Same words, same two pictures, same edit.
still_vars S1..S6 introduced.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "Jesus told a story about the smallest seed a farmer knew."),
    ("n1", NARRATOR, "It was a mustard seed — so tiny it could be lost in the palm of your hand."),
    ("n2", NARRATOR, "A man took that one little seed and planted it in his field."),
    ("n3", NARRATOR, "Of all the seeds he could have sown, it was just about the smallest of them all."),
    # Matthew 13:31
    ("j1", JESUS, "The kingdom of heaven is like to a grain of mustard seed, which a man took, and sowed in his field: which indeed is the least of all seeds:"),
    # Matthew 13:32
    ("j1b", JESUS, "but when it is grown, it is the greatest among herbs, and becometh a tree, so that the birds of the air come and lodge in the branches thereof."),
    ("n4", NARRATOR, "But that tiny seed did not stay small. Quietly, slowly, it began to grow."),
    ("n5", NARRATOR, "Up out of the ground, higher and higher, until it became the largest plant in the whole garden — a tall, spreading tree."),
    ("n6", NARRATOR, "And the wild birds came and built their nests in its broad, sheltering branches."),
    ("n7", NARRATOR, "That, Jesus said, is what God's kingdom is like."),
    ("n8", NARRATOR, "It almost never begins big. It begins small — a whispered prayer, a single kind act, one quiet change of heart."),
    ("n9", NARRATOR, "But God takes that smallest beginning and grows it into something far greater than anyone could have imagined."),
    ("card", NARRATOR, "God does enormous things from the smallest of starts. What small seed is he asking you to plant today?"),
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
