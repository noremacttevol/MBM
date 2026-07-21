#!/usr/bin/env python3
"""Narration for build-159-other-sheep — John 10.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

STAYED RED: both of them, and nothing moved.
  kv14  John 10:14  'I am the good shepherd, and know my sheep, and am known of mine.'
  kv16  John 10:16  'And other sheep I have, which are not of this fold...'
This is a Gospel, Jesus speaking in the flesh on the hillside, and a red-letter
King James Bible prints both verses red end to end. Both were already verbatim.

NO SPLITS. Neither segment has John's narration welded onto it — there is no
'Jesus saith unto them' frame on either one — so both stay single beats and the
edit the viewer sees is unchanged.

Nothing lifted from paraphrase. n1 through n3 set verse 14 up and n4 through n6
carry verse 16 into plain English before and after it lands, so the retelling
rule is already met by the narrator the build has.

Companion to build-134-other-sheep-i-have, which covers the same two verses;
the speaker calls here match that plan exactly.

WHY-LAW: milk. The other sheep are named as a promise to the outsider, not as
an argument about which fold is which. One shepherd, one voice, everybody
counted.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "On a hillside, surrounded by his listeners, Jesus reached for the most familiar picture they had — a shepherd and his flock. He was the shepherd, he told them, the good one, and the sheep were his very own."),
    ("n2", NARRATOR, "It is a tender thing to be known like that. Not counted as part of a crowd, but known — each one, by name, by voice, by the particular way it strays and the particular way it finds its way home."),
    ("n3", NARRATOR, "And the knowing runs both ways. His own know him too — the sound of his voice, the shape of his care — the way sheep will lift their heads at one familiar step and follow no stranger."),
    # John 10:14
    ("kv14", JESUS, "I am the good shepherd, and know my sheep, and am known of mine."),
    ("n4", NARRATOR, "But then Jesus said something that must have stopped them cold. This flock, right here in front of me, he told them — you are not all the sheep I have. There are others, in other places, not of this fold."),
    ("n5", NARRATOR, "People they had never met, in lands they had never seen, who also belonged to him and were waiting to be brought in. And about them he made a quiet, sweeping promise: they too shall hear my voice."),
    ("n6", NARRATOR, "Not two rival flocks. Not one favoured and one forgotten. In the end, one fold and one shepherd — every scattered sheep gathered home under the same gentle hand."),
    # John 10:16
    ("kv16", JESUS, "And other sheep I have, which are not of this fold: them also I must bring, and they shall hear my voice; and there shall be one fold, and one shepherd."),
    ("n7", NARRATOR, "So if you have ever felt like an outsider — like one of the other sheep, far from where the story seemed to be happening — hear this. He counted you in from the beginning. He always meant to come for you too."),
    ("n8", NARRATOR, "That is the wide, patient heart of the Good Shepherd. He has sheep the crowd never counted, and he will not rest until they hear him and come. So the only question is a gentle one. When you hear his voice, will you know it, and follow?"),
    ("card", NARRATOR, "Jesus said he has other sheep, not of this fold — and they too will hear his voice, until there is one fold and one shepherd. Wherever you are, he counted you in. When you hear his voice, will you follow?"),
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
