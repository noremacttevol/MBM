#!/usr/bin/env python3
"""Narration for build-185-many-mansions-member — John 14.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

STAYED RED: both, unchanged.
  j1  John 14:2  'In my Father's house are many mansions: if it were not so, I
      would have told you. I go to prepare a place for you.'
  j2  John 14:3  'And if I go and prepare a place for you, I will come again, and
      receive you unto myself; that where I am, there ye may be also.'
Gospel, Jesus in the flesh in the upper room, red-letter both, and both already
verbatim. No evangelist frame welded on either one, so NO SPLITS.

LIFTED FROM PARAPHRASE:
  jv1  John 14:1  'Let not your heart be troubled: ye believe in God, believe also
       in me.'   JESUS, RED
n0 was giving the most comforting sentence in the chapter second-hand — 'told
them not to let their hearts be troubled' — while the verse itself never got
spoken. It is his line and it is red. jv1 sits on ST2 with n1, a still the build
already has, so no new artwork.

Companion to build-133-many-mansions, which covers the same passage. That plan
folds John 14:1 into the front of its j1 beat; this build keeps j1 at verse 2
only, so verse 1 is added as its own beat here instead. The speaker calls agree
across both plans — 14:1, 14:2 and 14:3 are all red in each.

Treated independently of 133 otherwise: different segments, different stills, and
the Thomas exchange in 133 (John 14:5-6) is NOT imported here. This build is the
short comfort piece and adding a second voice would change what it is.

The closing card is not a beat in this build and has been left out of BEATS,
exactly as the original had it.

WHY-LAW: milk. A prepared place and a promise to come back. Nothing about
degrees, nothing about who qualifies — just room enough, and he is coming.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "On the night before everything changed, Jesus sat with his disciples and told them not to let their hearts be troubled."),
    # John 14:1
    ("jv1", JESUS, "Let not your heart be troubled: ye believe in God, believe also in me."),
    ("n1", NARRATOR, "He was going somewhere — but not to leave them behind. He was going to get a place ready."),
    # John 14:2
    ("j1", JESUS, "In my Father's house are many mansions: if it were not so, I would have told you. I go to prepare a place for you."),
    ("n2", NARRATOR, "A house with room for everyone. He said it plainly — if it were not true, he would have told them."),
    # John 14:3
    ("j2", JESUS, "And if I go and prepare a place for you, I will come again, and receive you unto myself; that where I am, there ye may be also."),
    ("n3a", NARRATOR, "He was not describing a far-off maybe."),
    ("n3b", NARRATOR, "He was promising to come back and carry them home himself."),
    ("card", NARRATOR, "He went to prepare a place — and he's coming back for you. You are not forgotten."),
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
