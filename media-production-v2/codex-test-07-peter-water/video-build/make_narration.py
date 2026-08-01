#!/usr/bin/env python3
"""Narration for build-07-peter-water — Matthew 14.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

Matthew 14:22-33. j1, j2 and j3 are Jesus in the flesh and a red-letter KJV
inks all three, so they stay RED. What was missing is everyone else in the boat:
three verbatim lines were buried in narrator paraphrase and are now SCRIPTURE (blue):
  s28  Matthew 14:28  Peter: 'Lord, if it be thou, bid me come unto thee on the water.'
  s30  Matthew 14:30  Peter: 'Lord, save me.'
  s33  Matthew 14:33  the disciples: 'Of a truth thou art the Son of God.'
Four narrator segments (n4, n5, n9, n10) were single audio files spread across two
DIFFERENT stills by the old template. Template A is one beat per still, so each is
split at the exact caption boundary the old build already used - same words, same
pictures, same edit. The added halves are n4b, n5b, n9b, n10b.
n11 is the closing card and keeps its id.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, 'Jesus had just fed more than five thousand people with a few loaves of bread and two small fish. And when it was done, he told his disciples to take the boat and cross the lake ahead of him. He sent the crowds home. And then he climbed a mountain, alone, to pray. That is where the night found him. Not in the boat. On the mountain, talking with his Father.'),
    ("n1", NARRATOR, 'Out on the water, the wind turned against the boat. The waves rose. The disciples — several of them fishermen who had worked this lake their whole lives — rowed against it for hours. Matthew tells us it was the fourth watch of the night when help came. That means between three and six in the morning. They had been fighting that sea nearly all night.'),
    ("n2", NARRATOR, 'And then, through the spray and the dark, they saw something that made grown fishermen scream. A figure. Walking toward them. On top of the water. They cried out that it was a ghost — because nobody walks on the sea. But the voice that came back across the water was one they knew.'),
    ("j1", JESUS, 'Be of good cheer; it is I; be not afraid.'),
    ("n3", NARRATOR, 'Think about what Peter was asking for. Not for the storm to stop. To come out into it — to where Jesus stood.'),
    ("s28", SCRIPTURE, 'Lord, if it be thou, bid me come unto thee on the water.'),
    ("j2", JESUS, 'Come.'),
    ("n4", NARRATOR, 'One word. And Peter put his leg over the side of that pitching boat, and stood up on the sea.'),
    ("n4b", NARRATOR, 'And he was doing it. Step after step on the moving water, his eyes fixed on Jesus. For a moment, an ordinary fisherman walked where only God can walk.'),
    ("n5", NARRATOR, 'Then he noticed the wind tearing at him. He looked down at the waves instead of ahead at Jesus.'),
    ("n5b", NARRATOR, 'And the moment his eyes moved, the water stopped holding him. He dropped to his waist, mid-stride, and cried out the shortest prayer in the Bible.'),
    ("s30", SCRIPTURE, 'Lord, save me.'),
    ("n6", NARRATOR, 'And Jesus caught him. Immediately.'),
    ("n7", NARRATOR, 'Matthew uses that exact word. There was no pause. No lesson first. No letting him go under to teach him something. The hand was there before the prayer was finished. And from that grip — holding him above the water — Jesus asked him one question.'),
    ("j3", JESUS, 'O thou of little faith, wherefore didst thou doubt?'),
    ("n8", NARRATOR, "Why did you doubt? Hear how he asked it. Not from the shore. Not after pulling him into the boat. From the hand already holding him. It isn't a scolding. It's a real question, from someone who had already caught him — as if to say: you were doing it. What made you stop trusting me?"),
    ("n9", NARRATOR, 'The two of them came back to the boat across the water together. And the moment they climbed in, the wind stopped.'),
    ("n9b", NARRATOR, 'Not slowly. Not eventually. The sea that had fought them all night simply lay down flat under the stars.'),
    ("n10", NARRATOR, 'And the men in that boat — the same men who minutes earlier had screamed that he was a ghost — knelt down where they sat, soaked and shaking, and worshipped him.'),
    ("s33", SCRIPTURE, 'Of a truth thou art the Son of God.'),
    ("n10b", NARRATOR, 'The storm had taught them who he was. And notice what the story remembers about Peter. Not that he sank. That he walked. And that when he fell, he was caught.'),
    ("n11", NARRATOR, 'When your storm gets loud and your faith slips, look back up — the same hand is already reaching for you. Keep your eyes on him.'),
]

# Homographs this build decides for itself (never auto-replaced globally).
# "Immediately" -> "imediately": won the in-context A/B 2026-08-01 (see the
# authoritative V1 make_narration.py in media-production/build-07-peter-water/
# for the measurements). Fixes Cameron's COMPLAINTS row 7 pronunciation denial.
SPOKEN = {"Immediately": "imediately"}


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
