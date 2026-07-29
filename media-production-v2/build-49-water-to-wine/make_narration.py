#!/usr/bin/env python3
"""Narration for build-49-water-to-wine — John 2.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

MARY SPEAKS. She is the reason this miracle happens and in the original she did
not have a single word of her own -- both her lines were narrator paraphrase in
white. Both are now lifted out verbatim as WOMAN, pink, each on the SAME still
the paraphrase already used:
  w3   John 2:3  'They have no wine.'
       This was the tail of n4. n4 keeps its id, trimmed to the frame -- 'She went
       straight to her son and told him the plain truth.' -- and a new n4b carries
       the retelling.
  w5   John 2:5  'Whatsoever he saith unto you, do it.'
       This was the tail of n6, which called it 'the best advice in the whole
       Bible' and then said it in modern English instead of letting her say it.
       It is one of the most quoted lines any woman speaks in the New Testament.
       n6 keeps its id, trimmed to the frame, and a new n6b retells it.

STAYED RED, ALL THREE. jv4 (2:4), jv7 (2:7), jv8 (2:8) are Jesus in the flesh and
a red-letter KJV inks all three. None carried John's framing -- 2:4 opens 'Jesus
saith unto her,' and the segment already begins at 'Woman, what have I to do with
thee' -- so none needed splitting.

ADDED IN BLUE -- THE GOVERNOR OF THE FEAST. His verdict was paraphrased inside
n10. Lifted out verbatim as SCRIPTURE (light blue -- a man in the story):
  s10  John 2:10  'Every man at the beginning doth set forth good wine; and when
       men have well drunk, then that which is worse: but thou hast kept the good
       wine until now.'
  n10 keeps its id, trimmed to the frame, and n10b retells it. 'Thou hast kept the
  good wine until now' is the sentence n11 then builds the whole ending on, so it
  matters that a viewer hears it in the words they would find in their own Bible.

THE SERVANTS -- CONSIDERED, NOT ADDED. The task asked about them, but John 2
never records a servant saying anything. Verse 9 only tells us 'the servants which
drew the water knew.' There is no line to lift, and I will not invent one. They
stay in the narrator's description, which is where scripture leaves them.

NO GREEN. Nothing in John 2 is the Father speaking.

RETELLING RULE: w3 by n4b, jv4 by n5, w5 by n6b, jv7 by n8, jv8 by n9, s10 by
n10b. No two Old English blocks run back to back anywhere in the build.

WHY-LAW: his first move in the whole world was to walk into a family's worst
moment of the day and quietly leave them with more joy than they started with --
for people who never asked and never found out who paid for it. Milk: that is
what he is like before he is anything else.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE, WOMAN

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "The very first miracle he ever did was not what you would guess. Not a healing. Not calming a storm. He saved a village wedding from falling apart."),
    ("n2", NARRATOR, "He was there as a guest, with his mother and his friends. A wedding in a small town like Cana ran for days, and the whole village came. It was pure, ordinary joy, and he was right in the middle of it."),
    ("n3", NARRATOR, "And then, quietly, disaster. The wine ran out. To us that sounds small. To that family it was a public shame they would carry for years. The feast, and their good name, were about to collapse."),
    ("n4", NARRATOR, "His mother noticed before anyone else did. And she did not go to the host, or the kitchen. She went straight to her son and told him the plain truth."),
    # John 2:3
    ("w3", WOMAN, "They have no wine."),
    ("n4b", NARRATOR, "Four words. They have no wine. She did not tell him what to do about it, and she did not ask him for anything. She simply put it in front of him and left the deciding to him."),
    # John 2:4
    ("jv4", JESUS, "Woman, what have I to do with thee? mine hour is not yet come."),
    ("n5", NARRATOR, "That sounds sharp in English, but it was not. Woman was a word of respect, and the phrase was a gentle old idiom, something like, is this really ours to fix, and is now the time? He was not brushing her off. He was wondering out loud whether this was the moment to begin."),
    ("n6", NARRATOR, "And his mother, who knew him better than anyone alive, did not argue with him. She just turned to the servants and gave them the best advice in the whole Bible."),
    # John 2:5
    ("w5", WOMAN, "Whatsoever he saith unto you, do it."),
    ("n6b", NARRATOR, "Whatever he tells you, do it. That is all of it. She did not explain, and she did not stay to supervise. She handed the servants over to him and stepped back, and trusted her son with the rest."),
    ("n7", NARRATOR, "Standing nearby were six big stone jars, the kind kept for the washing rituals, each one holding twenty or thirty gallons. Empty jars, meant for making things clean. Not a wine cup in sight."),
    # John 2:7
    ("jv7", JESUS, "Fill the waterpots with water."),
    ("n8", NARRATOR, "Not wine. Water. The plainest thing there is, from the nearest well. The servants filled all six to the very top, hauling bucket after bucket, surely wondering what plain water had to do with the problem."),
    # John 2:8
    ("jv8", JESUS, "Draw out now, and bear unto the governor of the feast."),
    ("n9", NARRATOR, "No lightning. No words spoken over the jars. No show at all. He simply told them to dip a cup and carry it to the man in charge of the feast. And somewhere between the jar and the cup, the water quietly became something else."),
    ("n10", NARRATOR, "The steward tasted it and had no idea where it came from. He pulled the bridegroom aside, half laughing."),
    # John 2:10
    ("s10", SCRIPTURE, "Every man at the beginning doth set forth good wine; and when men have well drunk, then that which is worse: but thou hast kept the good wine until now."),
    ("n10b", NARRATOR, "Everybody serves the good wine first, he said, and brings out the cheap stuff once the guests have stopped paying attention. You have done it backwards. You saved the best for last."),
    ("n11", NARRATOR, "And that is the line to hold on to. He saved the best for last. Not a bare rescue, not just barely enough to get by. Something like a hundred and fifty gallons of the finest wine at the party, poured out on ordinary people who would never even know who paid for it."),
    ("n12", NARRATOR, "That is the God this story is showing you. His first move in the whole world was not to frighten anyone or settle a score. It was to walk into a family's worst moment of the day and quietly turn it into more joy than they started with. His friends saw it, and they believed him."),
    ("card", NARRATOR, "His very first miracle was making a good day even better, for people who never asked and never knew. If that is how he begins, what do you think he is like? What would you bring a God who saves the best for last?"),
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
