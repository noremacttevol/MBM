#!/usr/bin/env python3
"""Narration for build-137-stephen-sees-him-standing — Acts 7.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

One red beat, and it was a misattribution. Jesus does not speak anywhere in this
story — he is SEEN, standing, and says nothing. The words on screen are Stephen's:

  s1  Acts 7:56  'Behold, I see the heavens opened, and the Son of man standing on
      the right hand of God.'  RED -> SCRIPTURE

That is the whole colour change: one line out of red into light blue. Painting it red
had Christ announcing his own appearance in the third person, which is backwards —
the power of the moment is that a dying man says it while the stones are coming.
Light blue is where every other witness in Acts sits, and Stephen belongs there.

No splits needed; the segment is a single clean speaker. Nothing lifted from
paraphrase — n0a, n0b and n1 are Luke's narration retold in modern English and are
correctly narrator, and n2 already does the retelling job right after s1. Acts 7:56
is quoted verbatim from the King James text. Nothing left uncertain.

WHY-LAW: milk. Standing, not sitting. Heaven is not indifferent to what is happening
to you — and the video does not have to argue that, because Stephen already said it. 2026-07-21: added n2b (narrator, same still ST5) — the cut fell to 57.1s, under the 60s floor, after the dead-air trim; the added line is the two-distinct-beings observation straight from Acts 7:55-56.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0a", NARRATOR, "The council was furious. They dragged Stephen out and hurled stones."),
    ("n0b", NARRATOR, "But Stephen was looking somewhere else entirely."),
    ("n1", NARRATOR, "Full of the Holy Ghost, he gazed up into heaven — and saw the glory of God."),
    # Acts 7:56
    ("s1", SCRIPTURE, "Behold, I see the heavens opened, and the Son of man standing on the right hand of God."),
    ("n2", NARRATOR, "Not sitting. Standing. As if ready to receive the one they were killing."),
    ("n2b", NARRATOR, "Notice what Stephen actually saw: the glory of God, and the Son of man standing beside it, at his right hand. Two of them. Distinct. And the Son was on his feet for him."),
    ("n3", NARRATOR, "The vision held him steady while the stones fell. He saw his Savior standing for him."),
    ("card", NARRATOR, "He stands for you too. Whatever falls on you today, you are not alone."),
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
