#!/usr/bin/env python3
"""Narration for build-126-by-their-fruits — Matthew 7.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

STAYED RED, ALL OF IT. This is the Sermon on the Mount - Jesus preaching in the
flesh - and a red-letter KJV inks every one of these verses. Nothing moved to
another speaker. There is no evangelist framing welded onto any of these
segments (no 'and Jesus said unto them'), so nothing needed splitting for colour.

THE PROBLEM THAT WAS REAL: j1a and j1b were two red beats back to back with no
storyteller between them, and j1b was the second half of j1a's sentence, so it
could not simply be separated. j1b is now the NARRATOR'S retelling of Matthew
7:15, and j1a carries the whole verse verbatim. Same id, same still (ST3, the
sheep's-clothing image), and the retelling fits that picture better than half a
sentence did.

LIFTED: Matthew 7:18 was buried inside n2's modern paraphrase - 'the good and the
rotten cannot switch places' IS verse 18. It is now jv18, red, in Jesus's own
words, sitting on ST5 (the corrupt tree) where the picture already argues it.
n2 was rewritten to retell 7:16-17 (which it now follows) and n2b carries n2's
original 'cannot switch places' point as the retelling of 7:18.

ADDED: n3, a closing narrator retelling of 7:19-20 so j3 does not run straight
into the card unexplained.

WOMEN: Matthew 7:15-20 records no woman speaking. Nothing added, nothing invented.

WHY-LAW: the test he gave is not a test of doctrine or of eloquence, it is a test
of fruit - and it is one an ordinary person can actually run. Milk framing: look
at what grows.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "Jesus taught how to tell what is true — look at what grows from it."),
    # Matthew 7:15
    ("j1a", JESUS, "Beware of false prophets, which come to you in sheep's clothing, but inwardly they are ravening wolves."),
    ("j1b", NARRATOR, "Watch out, he said. Some of them will come to you looking like part of the flock — gentle, harmless, one of your own. Inside, they are wolves."),
    ("n1", NARRATOR, "A tree shows what it is by what it bears. You don't guess at a tree by its bark."),
    # Matthew 7:16-17
    ("j2", JESUS, "Ye shall know them by their fruits. Do men gather grapes of thorns, or figs of thistles? Even so every good tree bringeth forth good fruit; but a corrupt tree bringeth forth evil fruit."),
    ("n2", NARRATOR, "Nobody picks grapes off a thorn bush. Nobody gathers figs off a thistle. You already know how this works — a good tree gives good fruit, and a bad one gives bad fruit."),
    # Matthew 7:18
    ("jv18", JESUS, "A good tree cannot bring forth evil fruit, neither can a corrupt tree bring forth good fruit."),
    ("n2b", NARRATOR, "Cannot. Not will not — cannot. The good and the rotten cannot switch places. What is inside comes out in the open, given long enough."),
    # Matthew 7:19-20
    ("j3", JESUS, "Every tree that bringeth not forth good fruit is hewn down, and cast into the fire. Wherefore by their fruits ye shall know them."),
    ("n3", NARRATOR, "A tree that never gives anything worth eating gets cut down. So watch the fruit. Not the clothes, not the confidence, not the words — the fruit. That is the whole test, and anybody can run it."),
    ("card", NARRATOR, "What grows from a life with him is good fruit — love, kindness, truth. Abide in him, and let it show."),
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
