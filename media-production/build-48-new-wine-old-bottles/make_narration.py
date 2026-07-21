#!/usr/bin/env python3
"""Narration for build-48-new-wine-old-bottles — Mark 2.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

STAYED RED, ALL FOUR. Mark 2:19-22 is Jesus answering in the flesh and a
red-letter KJV inks all of it, including both little parables -- the patch and
the wineskins. jv19 (2:19), jv20 (2:20), jv21 (2:21), jv22 (2:22) are verbatim
and none carried Mark's framing; 2:19 opens 'And Jesus said unto them,' and the
segment already begins at 'Can the children of the bridechamber'. No splits.

ADDED IN BLUE -- THE QUESTION THE WHOLE VIDEO ANSWERS. S1 is literally named
s1-the-question.jpeg, and the question itself was sitting inside n1 as modern
paraphrase in white. Lifted out verbatim as SCRIPTURE (light blue -- these are
men in the story, not Deity):
  s18  Mark 2:18  'Why do the disciples of John and of the Pharisees fast, but
       thy disciples fast not?'
  n1 keeps its id and is trimmed to the frame only -- 'Some very sincere, very
  religious men came to him with an honest question.' A new n1b carries the
  retelling n1 used to carry. Same shape as the centurion split; all three beats
  stay on S1, so no new artwork.

RETELLING GAP FIXED. jv21, the patch on the old garment, ran straight into n6,
which is about wine -- the garment was never said again in plain English. New
n5b now retells it on S6, the still already named s6-the-rent-made-worse, which
the original build gave no words of its own.

NO GREEN. Nothing here is the Father or a voice from heaven.

WOMEN: Mark 2:18-22 records no woman speaking. The bride is not even mentioned --
only the bridegroom and the children of the bridechamber. Nothing added; nothing
invented.

WHY-LAW: they came asking about a rule and he answered with a wedding. Milk --
God is not patching the old thing, he is pouring out a new one, and all he asks
is a heart soft enough to stretch.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "Some very sincere, very religious men came to him with an honest question."),
    # Mark 2:18
    ("s18", SCRIPTURE, "Why do the disciples of John and of the Pharisees fast, but thy disciples fast not?"),
    ("n1b", NARRATOR, "John's followers fasted. The Pharisees fasted. So why, they asked, did his own disciples not fast like everyone else? It was a fair question, asked plainly."),
    ("n2", NARRATOR, "Fasting was how you showed God you were serious. These were good men, going hungry to draw close to him. And here were his disciples, not fasting at all. It looked careless. His answer was not what they expected."),
    # Mark 2:19
    ("jv19", JESUS, "Can the children of the bridechamber fast, while the bridegroom is with them? as long as they have the bridegroom with them, they cannot fast."),
    ("n3", NARRATOR, "He points them at a wedding. Nobody starves themselves at a wedding feast. While the groom is right there in the room, the only fitting thing to do is celebrate. And that was the quiet, staggering claim underneath it. The groom is here. He was talking about himself."),
    # Mark 2:20
    ("jv20", JESUS, "But the days will come, when the bridegroom shall be taken away from them, and then shall they fast in those days."),
    ("n4", NARRATOR, "Then he says something that must have landed strangely. A day is coming when the groom will be gone. He is looking straight past this moment to the cross. There will be a time to mourn, and a time to fast. But not now, not while he is standing in front of them."),
    ("n5", NARRATOR, "Then he gives them two small pictures from everyday life. The first one is about mending clothes. You do not sew a stiff, brand-new scrap onto a soft, worn-out old coat."),
    # Mark 2:21
    ("jv21", JESUS, "No man also seweth a piece of new cloth on an old garment: else the new piece that filled it up taketh away from the old, and the rent is made worse."),
    ("n5b", NARRATOR, "Put a stiff new patch on a worn-out coat and the new cloth pulls against the old, and it tears the hole wider than it was before you started. You end up worse off for having tried to fix it that way."),
    ("n6", NARRATOR, "The second picture is about wine. In that world you kept your wine in bottles made of leather, of whole animal skins. A fresh skin was soft and it could stretch. But an old skin had gone hard and brittle, and new wine, still working and giving off gas, needs room to swell."),
    # Mark 2:22
    ("jv22", JESUS, "And no man putteth new wine into old bottles: else the new wine doth burst the bottles, and the wine is spilled, and the bottles will be marred: but new wine must be put into new bottles."),
    ("n7", NARRATOR, "So you never pour fresh, living wine into a stiff old skin. The wine keeps growing, the hard leather cannot give, and the whole thing tears open and everything is lost. Fresh wine belongs in a fresh skin, one that can stretch along with it. That is what he is telling them. God is doing something so new and so alive that the old rigid forms simply cannot hold it. Not a patch on the old religion. A whole new thing."),
    ("n8", NARRATOR, "That is the good news hiding inside a question about fasting. God was not tinkering with the old rules. He was pouring out something brand new, full of life and joy, and he was standing right there to give it. The only thing he asks is a heart soft enough to hold it."),
    ("card", NARRATOR, "They came asking about a rule, and he answered with a wedding. God is doing a new thing, and it is full of joy. Where is he offering you something new, if you will only make room for it?"),
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
