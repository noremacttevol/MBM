#!/usr/bin/env python3
"""Narration for build-37-rich-man-lazarus — Luke 16.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

Luke 16:19-31. A parable, so a red-letter KJV inks the whole of it - including
Abraham and the rich man, because those are Jesus's own words. j1 and j2 stay RED and
three more parable lines the video only paraphrased join them:
  j3  Luke 16:24  the rich man: 'Father Abraham, have mercy on me...'
  j4  Luke 16:26  '...between us and you there is a great gulf fixed...'
  j5  Luke 16:29  'They have Moses and the prophets; let them hear them.'
Note this Lazarus is the beggar in the parable, not the Lazarus of John 11.
still_vars S1..S8 introduced.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, 'Jesus once told a story about two men who lived side by side, yet worlds apart.'),
    ("n1", NARRATOR, 'One was rich. He wore the finest purple and linen, and every day of his life was a feast.'),
    ("n2", NARRATOR, 'Just outside his house, at his own gate, lay a poor beggar named Lazarus.'),
    ("n3", NARRATOR, "He was covered in sores, and so hungry he only wished for the scraps that fell from the rich man's table. Even the stray dogs came and licked his wounds."),
    ("n4", NARRATOR, 'The rich man walked past that gate every single day. And every day he stepped around the suffering man lying there, and did nothing.'),
    ("n5", NARRATOR, "Then the day came that comes for us all. Lazarus died — and the angels carried him home, to Abraham's side, into light and comfort at last."),
    ("n6", NARRATOR, 'The rich man died too, and was buried. But he opened his eyes in a place of torment: a dark and thirsty place, far from the light.'),
    ("j3", JESUS, 'Father Abraham, have mercy on me, and send Lazarus, that he may dip the tip of his finger in water, and cool my tongue; for I am tormented in this flame.'),
    ("n7", NARRATOR, 'Across a vast divide he could see Abraham in the distance, with Lazarus resting beside him. And he cried out, begging for just a drop of water to cool his tongue.'),
    ("j1", JESUS, 'Son, remember that thou in thy lifetime receivedst thy good things, and likewise Lazarus evil things: but now he is comforted, and thou art tormented.'),
    ("j4", JESUS, 'Between us and you there is a great gulf fixed: so that they which would pass from hence to you cannot; neither can they pass to us, that would come from thence.'),
    ("n8", NARRATOR, 'And between them, Abraham said, a great gulf had been fixed — one that no one could ever cross.'),
    ("n9", NARRATOR, 'So the rich man begged again: then send someone to my five brothers, to warn them, so they never come to this place.'),
    ("j5", JESUS, 'They have Moses and the prophets; let them hear them.'),
    ("n10", NARRATOR, 'They already have the writings of Moses and the prophets, Abraham replied. Let them listen. But the man pleaded — no, if only someone came back from the dead, then they would turn.'),
    ("n11", NARRATOR, 'And Abraham gave his final answer.'),
    ("j2", JESUS, 'If they hear not Moses and the prophets, neither will they be persuaded, though one rose from the dead.'),
    ("n12", NARRATOR, 'Jesus told this to people who had everything, and walked right past the ones who had nothing. It was a warning — but underneath it, a mercy.'),
    ("n13", NARRATOR, 'Because the day is still yours — for now.'),
    ("card", NARRATOR, 'There is a gate before you today, and someone waiting at it. Who are you walking past — and will you stop while there is still time?'),
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
