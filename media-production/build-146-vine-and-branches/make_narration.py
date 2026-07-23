#!/usr/bin/env python3
"""Narration for build-146-vine-and-branches — John 15.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

STAYED RED: both existing red beats are Jesus in the flesh in the upper room and a
red-letter KJV prints both.
  j1a  John 15:5a  'I am the vine, ye are the branches:'
  j1b  John 15:5b  'He that abideth in me, and I in him...'
Neither had Johannine framing welded onto it, so neither needed splitting.

ADDED: John 15:4, the verse the whole picture rests on, which the build did not
have in any form -- not even as paraphrase. `j0`, JESUS red, verbatim, on the
SAME still S2 the build already used for the living branch. n0d is its retelling.

RETELLING RULE: j1a and j1b ran back to back with no storyteller between them.
n0c now sits between them on the same still S3, retelling 'I am the vine, ye are
the branches' in plain English before the harder half lands. n1 was already
doing the retelling work for j1b and is untouched.

WOMEN: John 15 records no woman speaking. Nothing added; nothing invented.

WHY-LAW: fruit is not the price of the connection, it is the evidence of it. The
branch does not strain -- it stays joined. Milk framing, no argument on screen.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0a", NARRATOR, "Jesus used a picture His friends would know —"),
    ("n0b", NARRATOR, "a vine, and the branches that grow from it."),
    # John 15:4
    ("j0", JESUS, "Abide in me, and I in you. As the branch cannot bear fruit of itself, except it abide in the vine; no more can ye, except ye abide in me."),
    ("n0d", NARRATOR, "Stay in me, he said, and I will stay in you. It has never once done it. All it does is stay attached, and the life of the vine does the rest."),
    # John 15:5
    ("j1a", JESUS, "I am the vine, ye are the branches:"),
    ("n0c", NARRATOR, "I am the vine, he said. You are the branches. Not visitors. Not hired hands. Branches — part of the same living thing."),
    # John 15:5
    ("j1b", JESUS, "He that abideth in me, and I in him, the same bringeth forth much fruit: for without me ye can do nothing."),
    ("n1", NARRATOR, "A branch cut off from the vine doesn't dry up because it's weak. It dries up because it's disconnected."),
    ("n2", NARRATOR, "Stay joined to Him, and the life flows. Try to bear fruit on your own, and there's nothing there."),
    ("n3a", NARRATOR, "He wasn't asking for effort."),
    ("n3b", NARRATOR, "He was offering connection."),
    ("card", NARRATOR, "Stay connected to the Vine. Let His life flow through you."),
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
