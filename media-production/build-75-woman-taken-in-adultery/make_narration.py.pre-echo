#!/usr/bin/env python3
"""Narration for build-75-woman-taken-in-adultery — John 8.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

ALL FOUR VOICES ARE IN THIS ONE. White, blue, red, pink - and the pink is the
line the whole video was missing.

SHE SPEAKS NOW. John 8:11 records her, and it is three words:
  w11  John 8:11  'No man, Lord.'  WOMAN, pink. It was buried in n5 as 'No one,
       sir, she said' - a modern paraphrase of the only sentence the Bible gives
       her. She is the person this is happening to and she was the only one in
       the video with no voice. n5 keeps its id and now retells the exchange.

STAYED RED, all three, and none of them needed splitting because none had John's
framing welded on:
  j1  John 8:7   'He that is without sin among you, let him first cast a stone
      at her.'
  j2  John 8:10  'Woman, where are those thine accusers? hath no man condemned
      thee?'
  j3  John 8:11  'Neither do I condemn thee: go, and sin no more.'

THE ACCUSERS ARE LIGHT BLUE, NOT RED. The scribes and Pharisees are people in
the story, so they are SCRIPTURE like anyone else quoted from the KJV:
  s4  John 8:4-5  'Master, this woman was taken in adultery, in the very act.
      Now Moses in the law commanded us, that such should be stoned: but what
      sayest thou?'  n1 was carrying this as paraphrase; n1 keeps its id and its
      two-still span and was rewritten to set the verse up instead of replacing
      it. n2, 'it was a trap', is the retelling and did not have to move.
  s9  John 8:9   'And they which heard it, being convicted by their own
      conscience, went out one by one, beginning at the eldest, even unto the
      last: and Jesus was left alone, and the woman standing in the midst.'
      John narrating - never red. n4 keeps its id and text and now retells it.
  n4a new narrator beat on S6 so j1 is retold before the crowd empties out.

NOTE ON THE SPAN: n1 is one audio segment running across TWO stills, S2 and S3,
cutting at a caption boundary. Untouched - same picture cut as the delivered
video.

NO GREEN: the Father does not speak in John 8:1-11.

THE HUSH IS UNTOUCHED. 'Neither do I condemn thee' runs straight into the silent
still on S10 with no retelling. That was right and it stays.

WHY-LAW: everybody in that courtyard had something to say about her except her,
and the only man there with the right to throw anything put it down.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE, WOMAN

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "Early morning at the temple, Jesus was teaching a crowd, when a knot of religious leaders shoved their way through — dragging a woman with them."),
    ("n1", NARRATOR, "They stood her in the middle of everyone, where no one could look away. They had caught her, they said, in the act itself. And then they turned to Jesus, put the law of Moses on the table between them, and made him answer for it."),
    # John 8:4-5
    ("s4", SCRIPTURE, "Master, this woman was taken in adultery, in the very act. Now Moses in the law commanded us, that such should be stoned: but what sayest thou?"),
    ("n2", NARRATOR, "It was a trap. Say let her go, and he breaks the law. Say stone her, and he's just another man with a rock."),
    ("n3", NARRATOR, "Jesus said nothing at first. He bent down and wrote in the dust with his finger. Then he straightened up."),
    # John 8:7
    ("j1", JESUS, "He that is without sin among you, let him first cast a stone at her."),
    ("n4a", NARRATOR, "Whichever one of you has never sinned, he said — you go first. He did not argue the law with them. He just handed the first stone to anybody who had earned the right to throw it."),
    # John 8:9
    ("s9", SCRIPTURE, "And they which heard it, being convicted by their own conscience, went out one by one, beginning at the eldest, even unto the last: and Jesus was left alone, and the woman standing in the midst."),
    ("n4", NARRATOR, "And he bent down and wrote again. They dropped their stones and walked away, one by one — the oldest first — until it was only the two of them."),
    # John 8:10
    ("j2", JESUS, "Woman, where are those thine accusers? hath no man condemned thee?"),
    # John 8:11
    ("w11", WOMAN, "No man, Lord."),
    ("n5", NARRATOR, "Where are the ones accusing you, he asked her. Has no one condemned you? No man, Lord, she said. Three words — the only three the Bible gives her, and she got to say them standing up, in an empty courtyard, to the one person who had not walked away."),
    # John 8:11
    ("j3", JESUS, "Neither do I condemn thee: go, and sin no more."),
    ("card", NARRATOR, "The only one with the right to condemn her, wouldn't. What would it change to hear him say that to you?"),
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
