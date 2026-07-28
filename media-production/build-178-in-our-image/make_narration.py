#!/usr/bin/env python3
"""Narration for build-178-in-our-image — Genesis 1.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

Both scripture beats were painted JESUS-RED. Genesis is Old Testament so
neither can be red - but they do NOT both go the same way, and this build is the
clearest example in the set of the distinction the pass exists to fix.

SPLIT - Genesis 1:26 is genuinely two speakers in one breath:
  s1   (scripture, blue)  'And God said,'
                          - that is MOSES writing. Three words of narration.
  g26  (god, green)       'Let us make man in our image, after our likeness:
                           and let them have dominion over the fish of the sea...'
                          - that is DEITY, first person plural, his own voice.
The whole verse was one red segment, which made Moses's attribution read as part
of God's speech. s1 keeps its original id and g26 is new; BOTH stay on S2, so
the viewer sees the identical edit - two consecutive beats over one image. The
three-word blue beat is short, and it is worth it: this is the exact seam the
law is written around, and the colour flip on screen is the teaching.

NO SPLIT on s2, but it changes colour completely:
  s2  Genesis 1:27  'So God created man in his own image, in the image of God
                     created he him; male and female created he them.'
                                                         RED -> SCRIPTURE (blue)
This one is about God from end to end and never once IS God. 'So God created' -
third person, past tense, Moses narrating what he was shown. It is the second
half of the same thought as 1:26 and it was painted the same colour, but the
speaker changed at the verse break and the colour has to change with it. Green
here would have had God narrating his own work in the third person.

LIFTED ONE VERSE out of narrator paraphrase:
  s3  Genesis 2:7  'And the LORD God formed man of the dust of the ground, and
                    breathed into his nostrils the breath of life; and man
                    became a living soul.'                        NEW, scripture
n3 was already retelling this verse almost word for word in modern English -
dust, breath, came alive - without ever letting the viewer hear it. Moses
narrating again, so blue. It sits on S4 with n3, which now does the retelling
job. Noted for the record that this is Genesis 2, one chapter past the build's
stated reference; it is the verse n3 was paraphrasing and the story needs it.

ADDED two narrator retellings, both required by the retelling rule:
  n0b  retells Genesis 1:26 after the split, on S3.
  n0c  retells Genesis 1:27, on S4.
Without them, four verses of Old English ran with only the split between them,
and n1a/n1b - which do retell 1:27 - sit five beats downstream on S6.

Nothing left as paraphrase from uncertainty.

WHY-LAW: milk. Made in his image, given the earth to look after. Dignity first,
stewardship second, and no argument about either.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import GOD, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, 'At the start of all things, before any person drew breath, a counsel happened in the Godhead — let us make man in our image.'),
    ("s1", SCRIPTURE, 'And God said,'),
    ("g26", GOD, 'Let us make man in our image, after our likeness: and let them have dominion over the fish of the sea, and over the fowl of the air, and over the cattle, and over all the earth, and over every creeping thing that creepeth upon the earth.'),
    ("n0b", NARRATOR, 'Hear the word us. God is not talking to himself there — he is talking with someone, and what they decide together is to make a creature that looks like them. Then he hands that creature the whole living world to take care of.'),
    ("s2", SCRIPTURE, 'So God created man in his own image, in the image of God created he him; male and female created he them.'),
    ("n0c", NARRATOR, 'And then he did it. Not one of them closer to God than the other. Both of them bearing the likeness.'),
    ("s3", SCRIPTURE, 'And the LORD God formed man of the dust of the ground, and breathed into his nostrils the breath of life; and man became a living soul.'),
    ("n3", NARRATOR, 'Then the act:'),
    ("n2", NARRATOR, 'The plan included dominion — over fish, birds, cattle, and all the earth. Stewards, not owners.'),
    ("n1a", NARRATOR, 'Not in the shape of any creature, but bearing something of God himself:'),
    ("n1b", NARRATOR, 'the capacity to know him, to choose him, to reflect him.'),
    ("n4", NARRATOR, 'Every person since carries that original dignity — made in the image, loved into being.'),
    ("card", NARRATOR, 'You are made in his image. That is worth more than you know.'),
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
