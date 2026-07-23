#!/usr/bin/env python3
"""Narration for build-193-the-comforter — John 14.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

John 14. The red beat STAYS RED, and a second red line is lifted out.

  j1  John 14:26  'But the Comforter, which is the Holy Ghost...'  RED -> stays JESUS
  j0  John 14:18  NEW - lifted out of narrator paraphrase          -> JESUS
  n0b NEW - narrator retelling of j0

This is the Gospel of John, the upper room on the night of the betrayal, and
John 14:26 is Christ speaking in mortality. A red-letter King James Bible prints
it red. It stays red. Checked for evangelist framing welded onto the front - the
kind of 'And Jesus answering said unto him' seam that has to be split off into
blue - and there is none. j1 opens on 'But the Comforter' and is Christ's own
words end to end. No split.

LIFT. n0 said the disciples 'would not be left alone', which is a modern
paraphrase of John 14:18, sitting eight verses upstream of the line the video is
built on, and one of the tenderest sentences Christ ever spoke. It is now `j0`,
verbatim and red, on ST1 - the still is literally called 'not left alone', so the
artwork was already there waiting for it. Because the retelling rule is
mandatory, `n0b` is new narration that says it again in plain modern English
before n1 picks up the argument. That is the only new narrator line in the build.

Verbatim: j0 is John 14:18 word for word - 'I will not leave you comfortless: I
will come to you.' j1 is John 14:26 word for word, including 'whatsoever I have
said unto you'. Neither was smoothed.

n1, n2a and n2b stay narrator. They describe the Helper in modern English and
already do the retelling work for j1 in advance, which is why j1 needed no new
narration behind it - n3a and n3b close it out.

Ids: every original id kept. j0 and n0b are new. The card is 'card' and stays out
of beats, as the original had it.

WHY-LAW: milk. The Holy Ghost is a comfort and a teacher, not a doctrine to
argue. The promise was made to men in a room and it is still open.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "On the night before He died, Jesus sat with His disciples and told them they would not be left alone."),
    # John 14:18
    ("j0", JESUS, "I will not leave you comfortless: I will come to you."),
    ("n0b", NARRATOR, "He was hours from the cross, and He was the one doing the comforting — promising that whatever else they lost that week, they would not be left on their own."),
    ("n1", NARRATOR, "He promised another Helper would come — the Holy Ghost, sent by the Father in His name."),
    ("n2a", NARRATOR, "This Helper would do two things: teach them everything,"),
    ("n2b", NARRATOR, "and bring every word Jesus had spoken back to their minds."),
    # John 14:26
    ("j1", JESUS, "But the Comforter, which is the Holy Ghost, whom the Father will send in my name, he shall teach you all things, and bring all things to your remembrance, whatsoever I have said unto you."),
    ("n3a", NARRATOR, "The promise still stands."),
    ("n3b", NARRATOR, "The Spirit who taught them then teaches everyone who listens now."),
    ("card", NARRATOR, "You are not left to remember alone. The Comforter is here — let Him teach you."),
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
