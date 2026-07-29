#!/usr/bin/env python3
"""Narration for build-95-thief-on-the-cross — Luke 23.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

STAYED RED, and it is exact:
  j1  Luke 23:43  'Verily I say unto thee, To day shalt thou be with me in
      paradise.'
  Id kept. It carried no framing welded on, so it needed no split.

THE THIEF IS BLUE, NOT RED -- and he is the reason this video exists. Every word
he says was sitting in narrator paraphrase, in white. He is a man in the story,
not Deity, so all three of his lines are SCRIPTURE (light blue):
  s39  Luke 23:39  'If thou be Christ, save thyself and us.'
       -- the one who railed on him. n0b keeps its id and now retells it.
  s40  Luke 23:40-41  'Dost not thou fear God, seeing thou art in the same
       condemnation? And we indeed justly; for we receive the due reward of our
       deeds: but this man hath done nothing amiss.'
       -- the other one answering him. n1 already retells this almost word for
       word and was left exactly as it was.
  s42  Luke 23:42  'Lord, remember me when thou comest into thy kingdom.'
       -- THE line. n3 said it in modern English and the Old English was nowhere
       in the video. It now sits on ST4, the still already named
       's4-remember-me'. n2 is trimmed to the frame and n3 keeps its id as the
       retelling.

NO GREEN: the Father does not speak in Luke 23:39-43.

WOMEN: Luke 23:39-43 records no woman speaking. Nothing added, nothing invented.

WHY-LAW: a condemned criminal with nothing left to offer asked to be remembered,
and got paradise the same day. Milk: it is never too late, and there is nothing
to bring but the asking.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0a", NARRATOR, 'Two criminals were crucified with Jesus, one on each side.'),
    ("s39", SCRIPTURE, 'If thou be Christ, save thyself and us.'),
    ("n0b", NARRATOR, 'That was one of them, sneering at him from the next cross over.'),
    ("s40", SCRIPTURE, 'Dost not thou fear God, seeing thou art in the same condemnation? And we indeed justly; for we receive the due reward of our deeds: but this man hath done nothing amiss.'),
    ("n1", NARRATOR, "But the other one stopped him. We're getting what we deserve, he said."),
    ("n2", NARRATOR, 'Then he turned his head toward Jesus and asked for the smallest thing he could think of.'),
    ("s42", SCRIPTURE, 'Lord, remember me when thou comest into thy kingdom.'),
    ("n3", NARRATOR, 'No good deeds to offer. No time left to fix his life. Just a dying man asking.'),
    ("j1", JESUS, 'Verily I say unto thee, To day shalt thou be with me in paradise.'),
    ("n4", NARRATOR, "Today. Not someday, not after you've earned it. Today. The last-minute faith of a criminal was enough."),
    ("card", NARRATOR, "He saved a man who had nothing to give but a request. It's never too late to ask."),
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
