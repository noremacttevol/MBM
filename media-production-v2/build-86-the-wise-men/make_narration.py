#!/usr/bin/env python3
"""Narration for build-86-the-wise-men — Matthew 2.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

THE FIX: BOTH RED BEATS WERE WRONG, AND NEITHER WAS JESUS. He is a small child
in this story and he does not say a word in it. There is NO RED in this build,
and that is correct, not an oversight. Both are now `scripture` (light blue):
  j1  Matthew 2:2  'Where is he that is born King of the Jews? for we have seen
      his star in the east, and are come to worship him.'  That is THE WISE MEN
      speaking -- foreign scholars standing in Herod's hall. Leaving it red had
      the infant asking where he himself was.
  j2  Matthew 2:11  'And when they were come into the house, they saw the young
      child with Mary his mother, and fell down, and worshipped him: and when they
      had opened their treasures, they presented unto him gifts; gold, and
      frankincense, and myrrh.'  That is MATTHEW NARRATING. Nobody speaks it at
      all. It is the plainest 'narration inside the Gospels is scripture, not
      jesus' case in my whole set.
Both ids kept.

HEROD NOW SPEAKS, AND THE BUILD FINALLY MAKES SENSE. n0 said the wise men were
'asking a dangerous question' and n4a said 'Warned in a dream, they went home
another way' -- but Herod was never in the video, so the danger was never shown
and the dream warning was a non-sequitur the viewer could not follow. Added as
`scripture` (a man in the story, not Deity):
  s8  Matthew 2:8  'Go and search diligently for the young child; and when ye have
      found him, bring me word again, that I may come and worship him also.'
      with a new n1 framing it and a new n1b retelling it, all on S2 -- the still
      is literally called 'herods-hall' and until now nothing in it was about
      Herod. No new artwork.
Kept deliberately restrained: the killing of the children is Matthew 2:16 and is
NOT brought in. This is a milk-before-meat build. Herod's lie is enough to make
the dream warning land without turning a nativity video into a massacre.

RETELLINGS ADDED: n0b after j1, n1b after s8, n3b after j2. The build previously
had two long Old English blocks and no plain modern landing after either.

NO GREEN: an angel warns them in a dream in Matthew 2:12, but Matthew records no
words for it -- 'being warned of God in a dream' is all he gives. There is nothing
verbatim to put in green, so n4a keeps it as the storyteller's summary. Nothing
invented to manufacture a green beat.

WOMEN: Mary is named and present in Matthew 2:11 and records not one word.
NOTHING was put in her mouth; no pink in this build.

WHY-LAW: the people who found him first were foreigners who had no scripture, no
covenant and no invitation -- and they were the ones who came to worship. Milk:
the nations came looking, and the door was open.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "Some time after Jesus was born, travelers came from the east — scholars who had read the skies. They had seen his star, and followed it all the way to Jerusalem, where they walked into the king's hall and asked a dangerous question."),
    ("j1", SCRIPTURE, 'Where is he that is born King of the Jews? for we have seen his star in the east, and are come to worship him.'),
    ("n0b", NARRATOR, 'Understand what they had just done. They asked the sitting king of Jerusalem to point them to the real one.'),
    ("n1", NARRATOR, 'Herod was frightened, and he was clever about it. He sent them on to Bethlehem with an errand of his own:'),
    ("s8", SCRIPTURE, 'Go and search diligently for the young child; and when ye have found him, bring me word again, that I may come and worship him also.'),
    ("n1b", NARRATOR, 'Go and look carefully for the child, he said, and when you find him, come back and tell me, so that I can come and worship him too. Every word of that was a lie. He had no intention of worshipping anybody.'),
    ("n2a", NARRATOR, 'They were led at last to a house in Bethlehem.'),
    ("n2b", NARRATOR, 'And there he was — not in a palace, but with his mother.'),
    ("n3", NARRATOR, 'The wise men knelt before the little child — everything their long journey had been for. Matthew writes it down like this:'),
    ("j2", SCRIPTURE, 'And when they were come into the house, they saw the young child with Mary his mother, and fell down, and worshipped him: and when they had opened their treasures, they presented unto him gifts; gold, and frankincense, and myrrh.'),
    ("n3b", NARRATOR, 'Then they opened up what they had carried across the world and gave it to him — gold, and frankincense, and myrrh. They had crossed a desert to kneel on a dirt floor in a village nobody had heard of.'),
    ("n4a", NARRATOR, 'God warned them in a dream not to go back to Herod. So they went home another way, and the king never got his answer.'),
    ("n4b", NARRATOR, 'The nations had come to bow to the King.'),
    ("card", NARRATOR, "Strangers from far away recognized him first. The door is open — you're invited to worship too."),
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
