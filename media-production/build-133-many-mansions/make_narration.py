#!/usr/bin/env python3
"""Narration for build-133-many-mansions — John 14.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

STAYED RED: j1 is John 14:1-2, Jesus in the flesh in the upper room, red-letter,
and already verbatim. No evangelist framing welded on, so no split needed.

THE FIX - this is a conversation and only one side of it was in the video.
  s5   John 14:5  'Lord, we know not whither thou goest; and how can we know the
       way?'  SCRIPTURE, light blue. Thomas. The whole reason John 14:6 exists is
       that Thomas admitted out loud that he was lost, and he was not in the build
       at all - not even paraphrased. Added.
  jv6  John 14:6  'I am the way, the truth, and the life: no man cometh unto the
       Father, but by me.'  JESUS, RED. The KJV frame 'Jesus saith unto him,' is
       deliberately left off so the segment is his words only.
  s5 -> jv6 is a DELIBERATE question-and-answer pair and the only place in these
  eight builds where two non-narrator blocks touch. n4 retells both halves.

LIFTED: jv3 John 14:3 'And if I go and prepare a place for you, I will come again,
and receive you unto myself; that where I am, there ye may be also.' JESUS, RED.
n3 was paraphrasing it ('I'm coming back. I'll bring you to Myself'); n3 keeps its
text and is now the retelling.

REWRITTEN: n1 said 'Don't let your heart be troubled, He said. Trust God. Trust
Me' BEFORE j1 - that is verse 1 in modern English, delivered ahead of verse 1. It
is now a short setup, and n2 (unchanged) does the retelling after j1, which it was
always well suited to.

WOMEN: John 14:1-6 records no woman speaking - the upper room discourse is Jesus
with the Twelve, and the only named speakers in the chapter are Thomas, Philip and
Judas (not Iscariot). Nothing added, nothing invented.

WHY-LAW: Thomas said the honest thing - we don't know where you're going. The
answer was not a map. It was a person. Milk framing: the place is prepared, and
the way to it is Him.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0a", NARRATOR, "Jesus was preparing His disciples for a hard goodbye."),
    ("n0b", NARRATOR, "His words could have brought fear — instead they brought comfort."),
    ("n1", NARRATOR, "He could see it on their faces. So the very first thing He did was tell them not to be afraid."),
    # John 14:1-2
    ("j1", JESUS, "Let not your heart be troubled: ye believe in God, believe also in me. In my Father's house are many mansions: if it were not so, I would have told you. I go to prepare a place for you."),
    ("n2", NARRATOR, "He described a home they couldn't see yet — a place He was going to make ready for them, room for each one."),
    # John 14:3
    ("jv3", JESUS, "And if I go and prepare a place for you, I will come again, and receive you unto myself; that where I am, there ye may be also."),
    ("n3", NARRATOR, "And then the promise that undoes every fear: I'm coming back."),
    # John 14:5
    ("s5", SCRIPTURE, "Lord, we know not whither thou goest; and how can we know the way?"),
    # John 14:6
    ("jv6", JESUS, "I am the way, the truth, and the life: no man cometh unto the Father, but by me."),
    ("n4", NARRATOR, "We don't even know where you're going, Thomas said. How can we know the way? And Jesus told him: I am the way. Not a map. Not a method. Him. Not a vague hope — a prepared place, a return, a reunion."),
    ("card", NARRATOR, "He's preparing a place — and He's coming back for you. Don't let your heart be troubled."),
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
