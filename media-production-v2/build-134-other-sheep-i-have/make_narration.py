#!/usr/bin/env python3
"""Narration for build-134-other-sheep-i-have — John 10.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

STAYED RED: j1 is John 10:16, Jesus in the flesh, red-letter, already verbatim.
No framing welded on, so no split needed.

LIFTED: jv14 John 10:14 'I am the good shepherd, and know my sheep, and am known
of mine.' JESUS, RED. n0 was asserting it in the storyteller's voice - 'He was the
good Shepherd, and they were His flock' - which is the claim of the chapter
reported second-hand. He says it himself now, and n0b (new) is the retelling.
Verse 14 was chosen over verse 11 because 'know my sheep, and am known of mine' is
what makes verse 16 land: the other sheep are not strangers to him either.

RESEQUENCED: n1a, n1b and n2 all paraphrased j1 BEFORE j1 arrived, so the viewer
heard 'there were other sheep, not of that pen' in modern English three times and
then finally got the King James. j1 now comes fifth instead of last-but-three, and
n1b and n2 keep their exact original words as retellings afterward. n1a was
trimmed by two words so it reads as a setup rather than a summary.

WOMEN: John 10:1-18 records no woman speaking - this is Jesus teaching, with only
the crowd's division reported in verses 19-21 and no quoted woman anywhere.
Nothing added, nothing invented.

NOTE ON THE STILLS: ST10 stays unused, exactly as the original build had it. The
artwork is untouched and no beat was invented to fill it.

WHY-LAW: this is the verse a Latter-day Saint hears differently, and it needs no
argument on screen at all. The video says only what the verse says - there are
sheep he already has, elsewhere, and he is going to bring them. Milk. A viewer who
later learns where those other sheep were will find the video was right all along.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "Jesus used a picture His listeners knew well — a shepherd and his sheep, out on the open hill."),
    # John 10:14
    ("jv14", JESUS, "I am the good shepherd, and know my sheep, and am known of mine."),
    ("n0b", NARRATOR, "Not a hired hand counting a herd — a shepherd who knows them one at a time, and is known back."),
    ("n1a", NARRATOR, "But the flock was bigger than the people standing in front of Him."),
    # John 10:16
    ("j1", JESUS, "And other sheep I have, which are not of this fold: them also I must bring, and they shall hear my voice; and there shall be one fold, and one shepherd."),
    ("n2", NARRATOR, "And the result would be one flock, one Shepherd."),
    ("n3", NARRATOR, "Not divided by nation or wall. One voice, one care, one Shepherd over all who listen."),
    ("n4", NARRATOR, "Whoever hears Him belongs — wherever they're from."),
    ("card", NARRATOR, "His voice reaches further than you think. Hear Him, and you're in the fold."),
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
