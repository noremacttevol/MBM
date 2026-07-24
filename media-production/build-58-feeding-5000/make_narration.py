#!/usr/bin/env python3
"""Narration for build-58-feeding-5000 — John 6.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

STAYED RED, and two more added.
  jv12  John 6:12  "Gather up the fragments that remain, that nothing be lost."
        Kept its id. n6 already retells it, so nothing new was needed after it.
  j5    John 6:5   "Whence shall we buy bread, that these may eat?"  -- MISSING;
        n2 paraphrased it in white. Lifted onto S2. n2 trimmed to the frame, n2b
        retells.
  j10   John 6:10  "Make the men sit down."  -- MISSING; n4 paraphrased it. Lifted
        onto S4. n4 trimmed to the frame, n4b retells.

THE DISCIPLES WERE NEVER HEARD -- AND WHICH GOSPEL MATTERS HERE.
"We have here but five loaves, and two fishes" is Matthew 14:17. This build is John
6, and John gives the line to Andrew, by name, with more in it:
  s9  John 6:9  "There is a lad here, which hath five barley loaves, and two small
      fishes: but what are they among so many?"
That is the sentence n3 was paraphrasing almost word for word, so John's is the one
that belongs in a John video -- a viewer looking up John 6:9 finds it exactly.
Lifted as [scripture] on S3; n3 trimmed to the frame, n3b retells. The Matthew
wording is exact too, and is here in the notes if a later pass wants the synoptic
version instead.

THE CROWD WAS NEVER HEARD. n7 paraphrased John 6:14. Lifted as s14 [scripture] on
S9: "This is of a truth that prophet that should come into the world." n7 keeps its
id, trimmed to the frame; n7b retells.

CONSIDERED AND LEFT OUT: Philip's answer, John 6:7 -- "Two hundred pennyworth of
bread is not sufficient for them, that every one of them may take a little." It is
exact and it is good, but the video already carries Andrew's not-enough line on the
very next still, and two men saying the same thing in a row plays as a stutter. Left
out on judgment, not on uncertainty; the verse is above if a later pass wants it.

NO GREEN: John 6:1-14 has no voice from heaven. WOMEN: John 6:1-14 records no woman
speaking -- women are counted in the crowd but none is quoted. Nothing invented.

WHY-LAW: the smallest lunch in the field was barley bread, the poor man's loaf, and
it was the only thing anybody offered. Milk: he does not ask you for enough. He asks
you for what you have.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "A huge crowd had followed Jesus to a lonely green hillside beside the lake, hungry to hear him and to be healed. He taught them and cared for them all day, until the sun began to sink and they were a long way from any town or food."),
    ("n2", NARRATOR, "His disciples grew anxious as the light went. But Jesus turned it back on them. He looked up at the crowd coming toward him and asked Philip:"),
    # John 6:5
    ("j5", JESUS, "Whence shall we buy bread, that these may eat?"),
    ("n2b", NARRATOR, "He was not worried. John tells us plainly that he already knew exactly what he was going to do — he asked to see what Philip would say."),
    ("n3", NARRATOR, "There was only one lunch in the whole crowd. Andrew, Simon Peter's brother, brought a boy to Jesus, almost embarrassed to mention it."),
    # John 6:9
    ("s9", SCRIPTURE, "There is a lad here, which hath five barley loaves, and two small fishes: but what are they among so many?"),
    ("n3b", NARRATOR, "Barley was the poor man's bread. It was the smallest, cheapest lunch on that whole hillside, and it was the only thing anybody offered."),
    ("n4", NARRATOR, "Jesus was not troubled by how little there was. He said simply:"),
    # John 6:10
    ("j10", JESUS, "Make the men sit down."),
    ("n4b", NARRATOR, "Have everyone sit down. And they settled in groups on the green grass, five thousand men, besides women and children, waiting to see what he would do."),
    ("nbless", NARRATOR, "Then he took the five loaves and the two fish, and looking up to heaven, he gave thanks, and broke the bread."),
    ("n5", NARRATOR, "And the food did not run out. The disciples carried it through the crowd, and it kept coming, bread and fish, more and more, until every single person there had eaten as much as they wanted, and was full."),
    # John 6:12
    ("jv12", JESUS, "Gather up the fragments that remain, that nothing be lost."),
    ("n6", NARRATOR, "Pick up every scrap that's left, he said. Let nothing go to waste. So they went through the crowd and gathered what was left, and filled twelve baskets with the broken pieces. They ended with far more than they had started with. The little lunch, placed in his hands, had become a feast."),
    ("n7", NARRATOR, "When the people saw the sign, they were amazed, and began to say:"),
    # John 6:14
    ("s14", SCRIPTURE, "This is of a truth that prophet that should come into the world."),
    ("n7b", NARRATOR, "He had taken almost nothing, given thanks for it, and fed them all."),
    ("card", NARRATOR, "He still takes the little you have, the not-enough, the barely-anything, the lunch you are embarrassed to offer, and gives thanks for it, and breaks it, and somehow it becomes enough, with baskets to spare. What small thing is he asking you to place in his hands?"),
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
