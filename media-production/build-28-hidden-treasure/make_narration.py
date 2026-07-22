#!/usr/bin/env python3
"""Narration for build-28-hidden-treasure — Matthew 13.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

Matthew 13:44. A one-verse parable - a red-letter KJV inks all of it, so j1
stays RED. Nobody speaks inside it, so nothing moved and nothing new was lifted.
Structural only: the old template played the single j1 audio across two different
stills. j1 keeps its id and the first half of the verse; j1b carries the rest. Same
words, same two pictures, same edit. still_vars S1..S7 introduced.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "Jesus once told a very short story — about a man, and a field."),
    ("n1", NARRATOR, "He was a hired worker, out digging in a field that wasn't even his own."),
    ("n2", NARRATOR, "And on one ordinary day, his spade struck something hard, buried in the ground."),
    ("n3", NARRATOR, "He cleared away the dirt — and there it was. A treasure. Hidden, forgotten, and worth more than he had ever seen in his life."),
    ("n4", NARRATOR, "His heart pounded. Quickly, quietly, he covered it back over — and told no one."),
    # Matthew 13:44
    ("j1", JESUS, "Again, the kingdom of heaven is like unto treasure hid in a field; the which when a man hath found, he hideth,"),
    # Matthew 13:44
    ("j1b", JESUS, "and for joy thereof goeth and selleth all that he hath, and buyeth that field."),
    ("n5", NARRATOR, "Did you catch what he did? He went home and sold everything he owned."),
    ("n6", NARRATOR, "His house. His tools. All of it — gladly, without a second thought."),
    ("n7", NARRATOR, "And with every coin he had, he bought that one field for himself."),
    ("n8", NARRATOR, "Because he knew what was waiting under the soil. That field was worth more than everything else he owned, put together."),
    ("n9", NARRATOR, "That, Jesus said, is what God's kingdom is like."),
    ("n10", NARRATOR, "At first it can look like an ordinary field. But once you catch sight of the treasure in it — once you truly see who Jesus is — nothing else even compares."),
    ("n11", NARRATOR, "And you don't give everything up sadly. You do it out of pure joy — because you've found the one thing worth having everything else."),
    ("card", NARRATOR, "The man sold all he had — and called it the best trade of his life. If you have found the treasure, what is he worth to you?"),
]

# Homographs this build decides for itself (never auto-replaced globally).
SPOKEN = {}


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
