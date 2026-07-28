#!/usr/bin/env python3
"""Narration for build-174-hearts-of-the-fathers — Malachi 4.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

Both scripture beats were painted JESUS-RED. Malachi is Old Testament, so
neither can be red - and both are the LORD speaking in first person, which makes
them GREEN, not blue:
  s1a  Malachi 4:5  'Behold, I will send you Elijah the prophet...'   RED -> GOD
  s1b  Malachi 4:6  'And he shall turn the heart of the fathers...'   RED -> GOD

NO SPLIT on s1a. It carries first person all the way through ('I will send you
Elijah'), and 4:6 keeps it ('lest I come and smite the earth'). Malachi is
reporting the LORD's own words unbroken across both verses, so there is no
narrator clause to peel off. Splitting 'Behold,' out would be mechanical and
would read worse.

ADDED n0b - a narrator retelling between the two green beats. s1a landed on a
promise ('the great and dreadful day of the LORD') with no plain-English landing
before 4:6 started, so the Old English was stacking two verses deep before the
viewer got any help. n0b sits on S2, the same still as s1a, so the picture is
unchanged.

Nothing lifted from paraphrase and nothing left uncertain - both verses are
verbatim Malachi 4:5-6 as a viewer would find them.

WHY-LAW: milk. Elijah's errand is repair, not thunder. Hearts turning toward
family is the whole promise, and the video lets it stay that simple.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import GOD, NARRATOR

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, 'Before the great day, a messenger would come first — Elijah, the prophet, sent ahead.'),
    ("s1a", GOD, 'Behold, I will send you Elijah the prophet before the coming of the great and dreadful day of the LORD:'),
    ("n0b", NARRATOR, 'Listen to who is talking there. That is God himself, making a promise out loud: before the last great day arrives, I am sending Elijah back. Not an army. Not a warning shot.'),
    ("s1b", GOD, 'And he shall turn the heart of the fathers to the children, and the heart of the children to their fathers, lest I come and smite the earth with a curse.'),
    ("n1", NARRATOR, 'His work was not to thunder, but to mend.'),
    ("n3", NARRATOR, 'The same spirit would later rest on John, preparing the way.'),
    ("n2a", NARRATOR, 'So that when the Lord came, families would be ready.'),
    ("n2b", NARRATOR, 'Not divided, but whole.'),
    ("card", NARRATOR, 'He cares about your family. Let the healing start with your own heart.'),
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
