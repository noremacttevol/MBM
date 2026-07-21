#!/usr/bin/env python3
"""Narration for build-125-i-never-knew-you — Matthew 7.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

ALL THREE RED BEATS STAY RED. j1 (Matthew 7:21), j2 (7:22) and j3 (7:23) are
one unbroken stretch of Jesus speaking on the mount. Nothing moved out of red.

j2 IS THE ONE TO GET RIGHT. 'Lord, Lord, have we not prophesied in thy name?'
is Jesus quoting what people will say — speech inside his own speech, exactly
like the dialogue inside a parable. A red-letter KJV inks the whole of
Matthew 7:22 red, including the quoted crowd. It stays JESUS. It is not
scripture-blue and it is never split off from the verse around it.

NO MIXED SEGMENTS. There is no narration frame in Matthew 7:21-23 — Matthew
does not interrupt — so nothing needed splitting. n0 is the storyteller's own
modern-English framing and correctly stays narrator.

THE REAL PROBLEM HERE WAS THE RETELLINGS. This build is short, three red
blocks in a row with only a single thin sentence between each, and the Old
English was landing unexplained. n1, n2 and n3 have all been rewritten so
each one now retells the verse before it in plain modern English first, then
carries the point:
  n1 retells 7:21 — not everyone who calls me Lord, only the one who does
     what my Father wants — before setting up the day of accounting.
  n2 retells 7:22 line by line and points out what is missing from the list.
  n3 retells 7:23 — I never knew you — and keeps the original closing
     invitation word for word at the end.
No new segments, no new stills, no id changes, no beat reordering. The
storyteller now stands between every pair of red blocks doing real work
instead of nodding.

NOTHING LEFT AS PARAPHRASE FROM UNCERTAINTY. All three quoted beats were
checked word for word against the KJV and were already exact.

WHY-LAW: this passage is easy to preach as a threat. It is not one. He is not
weighing the size of the resume, he is asking whether we ever actually walked
with him — and the answer to that is an open door, not a closed one. Milk
framing all the way through, and the card stays exactly as it is.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "Jesus warned that saying the right words is not the same as knowing him. The door is not opened by a name we repeat."),
    # Matthew 7:21
    ("j1", JESUS, "Not every one that saith unto me, Lord, Lord, shall enter into the kingdom of heaven; but he that doeth the will of my Father which is in heaven."),
    ("n1", NARRATOR, "Not everyone who calls me Lord will come into the kingdom, he said — only the one who actually does what my Father wants. Words are cheap. A life is not. And then he described a day when many will point to everything they did in his name."),
    # Matthew 7:22
    ("j2", JESUS, "Many will say to me in that day, Lord, Lord, have we not prophesied in thy name? and in thy name have cast out devils? and in thy name done many wonderful works?"),
    ("n2", NARRATOR, "Lord, they will say, didn't we prophesy in your name? Didn't we drive out devils in your name? Didn't we do all kinds of wonderful works in your name? Listen to what is missing from that list. Every single sentence is about what they did. Not one of them is about him."),
    # Matthew 7:23
    ("j3", JESUS, "And then will I profess unto them, I never knew you: depart from me, ye that work iniquity."),
    ("n3", NARRATOR, "I never knew you. Not, I never heard of your works — I never knew you. He is not weighing the size of anyone's list. He is asking whether we ever really walked with him. And this is not a threat to scare you. It is an invitation to be known — to walk with him, not just speak his name."),
    ("card", NARRATOR, "He wants to know you, not just be named by you. Come close, and let him know you."),
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
