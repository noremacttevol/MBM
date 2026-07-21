#!/usr/bin/env python3
"""Narration for build-140-road-runs-both-ways — Luke 15.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

THIS IS A PARABLE, SO THE WHOLE THING IS RED. Luke 15:11-32 is Jesus telling a
story, and a red-letter KJV inks every word of it - including the lines Jesus puts
in the father's and the sons' mouths, and including his own narration inside the
parable ('But the father said to his servants,'). So nothing here moved to blue.
The test is not 'who is the character', it is 'does a red-letter KJV print this
red' - and here it does.

STAYED RED: j1 'And he said, A certain man had two sons:' (Luke 15:11).

WHAT THIS BUILD WAS MISSING: it was the most famous story Jesus ever told and the
viewer never heard one line of it. Everything after j1 was modern paraphrase. Four
blocks of verbatim KJV are now lifted out, all JESUS red, each one followed by the
narrator retelling it - and each one sitting on the SAME still as the narrator beat
it belongs to, so the artwork and the edit are unchanged:
  j18  Luke 15:18-19  'I will arise and go to my father... make me as one of thy
       hired servants.'          retold by n3a + n3b (unchanged text)
  j20  Luke 15:20     'But when he was yet a great way off, his father saw him,
       and had compassion, and ran, and fell on his neck, and kissed him.'
                                 retold by n4 (unchanged text)
  j22  Luke 15:22-24  'Bring forth the best robe... for this my son was dead, and
       is alive again; he was lost, and is found.'
                                 retold by n5 (unchanged text)
  j31  Luke 15:31-32  'Son, thou art ever with me, and all that I have is thine...'
                                 retold by n7 (NEW)
n7 is the only new narrator beat, and it goes on ST10 (two roads, one door), which
the original build never used - so the older brother finally gets the answer the
title of the video is about.

WOMEN: Luke 15:11-32 records no woman speaking. Nothing added; nothing invented.

WHY-LAW: the father runs while the son is still a great way off, before a word of
the apology gets out. And the same father walks out to the angry son standing in
the yard. Milk framing - the road runs both ways and the door is open at both ends.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "Jesus told a story about a father and two sons. The younger one wanted his share of the inheritance now — and he got it."),
    # Luke 15:11
    ("j1", JESUS, "And he said, A certain man had two sons:"),
    ("n1", NARRATOR, "He left home and went to a country far away. There he spent everything on a life that looked free and felt empty."),
    ("n2", NARRATOR, "A hard season came. He was hungry, alone, and tending pigs — and he came to himself."),
    # Luke 15:18-19
    ("j18", JESUS, "I will arise and go to my father, and will say unto him, Father, I have sinned against heaven, and before thee, And am no more worthy to be called thy son: make me as one of thy hired servants."),
    ("n3a", NARRATOR, "He decided to go back."),
    ("n3b", NARRATOR, "Not as a son claiming rights, but as a servant asking for a place."),
    # Luke 15:20
    ("j20", JESUS, "But when he was yet a great way off, his father saw him, and had compassion, and ran, and fell on his neck, and kissed him."),
    ("n4", NARRATOR, "But while he was still far off, his father saw him and ran. No lecture. No waiting for the apology. He threw his arms around him."),
    # Luke 15:22-24
    ("j22", JESUS, "But the father said to his servants, Bring forth the best robe, and put it on him; and put a ring on his hand, and shoes on his feet: And bring hither the fatted calf, and kill it; and let us eat, and be merry: For this my son was dead, and is alive again; he was lost, and is found."),
    ("n5", NARRATOR, "The father gave him the robe, the ring, the sandals — belonging, not probation. And there was a feast, because what was lost had come home."),
    ("n6", NARRATOR, "But the older brother stood outside, angry that grace looked so easy. The door ran both ways — it was open for him too."),
    # Luke 15:31-32
    ("j31", JESUS, "Son, thou art ever with me, and all that I have is thine. It was meet that we should make merry, and be glad: for this thy brother was dead, and is alive again; and was lost, and is found."),
    ("n7", NARRATOR, "Son, you have always been with me, the father told him, and everything I have is already yours. Then he went right back to the reason for the party — your brother was dead, and he's alive. He was lost, and we found him. The father walked out to both sons."),
    ("card", NARRATOR, "The road home is always open. However far you've gone, turn around — He's already running to meet you."),
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
