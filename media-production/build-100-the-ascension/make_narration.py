#!/usr/bin/env python3
"""Narration for build-100-the-ascension — Acts 1.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

Acts is Luke writing, so almost everything here is `scripture` — but this build is
the exception the law names: the speaker in Acts 1:7-8 is the RISEN CHRIST, talking
to the eleven on the day he ascends. A red-letter King James Bible inks those verses.
So the one red beat STAYS red, and it grows:

  j1  Acts 1:8  RED -> RED (jesus), but rewritten to the full verbatim verse. The
      old line dropped 'both in Jerusalem, and in all Judaea, and in Samaria' out of
      the middle, which made it a paraphrase wearing Old English clothes. It is now
      exactly what a viewer finds in Acts 1:8.
  j0  Acts 1:7  NEW (jesus). n0 already told the viewer the disciples asked about
      restoring the kingdom; his actual answer was never on screen. It is now, in his
      own words, immediately before verse 8. Same still as j1 — two consecutive beats
      over ST2, no new artwork.

LIFTED FROM PARAPHRASE — the two men in white:
  s11 Acts 1:11  NEW (scripture, light blue). n3 said 'two figures in white stood
      beside them with a promise' and then n4 gave the promise in modern English,
      which meant the single most quotable line in the chapter never got spoken as
      scripture. s11 now says it verbatim and n4 retells it, unchanged, right after.
      These are angels/messengers, not Christ — light blue, not red and not green.
      s11 and n4 share ST7.

Nothing left as paraphrase from uncertainty. Acts 1:7, 1:8 and 1:11 are all quoted
in full from the King James text.

WHY-LAW: milk. He did not leave them staring at the sky. He left them a job, a
companion, and a promise to come back — and all three are on screen in the words
they were actually said in.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "In his last moments with them, the disciples asked Jesus if he was going to restore the kingdom right then. He turned them toward something bigger."),
    # Acts 1:7
    ("j0", JESUS, "It is not for you to know the times or the seasons, which the Father hath put in his own power."),
    # Acts 1:8
    ("j1", JESUS, "But ye shall receive power, after that the Holy Ghost is come upon you: and ye shall be witnesses unto me both in Jerusalem, and in all Judaea, and in Samaria, and unto the uttermost part of the earth."),
    ("n1", NARRATOR, "That is not a no. It is a redirection. The timing belongs to the Father, he told them, and it is not yours to work out — but the power is yours, and so is the work. He was handing them the mission. Go tell everyone, everywhere, starting right where you're standing. And then something happened they would never forget."),
    ("n2a", NARRATOR, "While they watched, he was lifted up,"),
    ("n2b", NARRATOR, "and a cloud received him out of their sight. They stood there staring into the sky, stunned."),
    ("n3", NARRATOR, "Then two figures in white stood beside them with a promise:"),
    # Acts 1:11
    ("s11", SCRIPTURE, "Ye men of Galilee, why stand ye gazing up into heaven? this same Jesus, which is taken up from you into heaven, shall so come in like manner as ye have seen him go into heaven."),
    ("n5", NARRATOR, "He did not abandon them. He left them a mission, a promise, and the sure word that he's coming again."),
    ("card", NARRATOR, "He's coming back the same way he left. Until then, you're not alone — and you're not without purpose."),
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
