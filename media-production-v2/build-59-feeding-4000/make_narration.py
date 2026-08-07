#!/usr/bin/env python3
"""Narration for build-59-feeding-4000 — Mark 8.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

STAYED RED, and two more added.
  jv2  Mark 8:2  "I have compassion on the multitude, because they have now been
       with me three days, and have nothing to eat."  -- already exact. Kept its id.
  j3   Mark 8:3  "And if I send them away fasting to their own houses, they will
       faint by the way: for divers of them came from far."  -- MISSING; n2
       paraphrased it in white. It is the second half of the same continuous
       sentence as jv2, so it sits immediately after it on the SAME still (S2), and
       n1b retells both halves together.
  j5   Mark 8:5  "How many loaves have ye?"  -- MISSING; n3 paraphrased it. Lifted
       onto S4.

THE DISCIPLES WERE NEVER HEARD, TWICE.
  s4  Mark 8:4  "From whence can a man satisfy these men with bread here in the
      wilderness?"  -- [scripture] on S3. n2 keeps its id, trimmed to the frame;
      n2b retells.
  s5  Mark 8:5  "Seven."  -- one word, and it is theirs. [scripture] on S4.

DELIBERATE QUESTION-AND-ANSWER PAIR: j5 asks "How many loaves have ye?" and s5
answers "Seven." Red straight into blue with no narrator wedged between them is
intentional -- a retelling in the middle of a two-word exchange would kill it. n3b
retells both immediately after. Every other Old English block in this build is
followed by the narrator saying it again.

SECOND-FEEDING SCHOLARSHIP (Cameron complaint, 2026-08-06 — reportedAgainst
3005df5d1da3). This IS the second time Jesus fed a multitude, at a different time
and place from the five thousand, and the narration must SAY so and defend it, not
retell the first story with new numbers. The proof is recorded in Jesus's OWN
words: Matt 16:9-10 / Mark 8:19-21, where he makes the disciples count BOTH — "the
five loaves of the five thousand, and how many baskets... the seven loaves of the
four thousand, and how many baskets" — twelve then, seven now. Two crowds, two
wildernesses, two rescues; he wanted both remembered. The two are deliberately
CONTRASTED here (n2b, n5): five loaves and two fishes → twelve baskets on the green
Jewish hillside (Matt 14) vs seven loaves and a few small fishes → seven baskets in
the Gentile Decapolis (Mark 8), after three days. The differing counts are the
evidence the events are distinct. This REVERSES the old "keep the two feedings from
bleeding" note: the contrast is now the point, not a leak to be prevented.
THE DISCIPLES' OWN line in THIS story stays Mark 8:4 above (s4).

NO GREEN. WOMEN: Mark 8:1-9 records no woman speaking. Nothing invented.

WHY-LAW: he had already fed five thousand and the disciples still could not see it.
He did not scold them; he just asked what they had. Milk: he noticed they were tired
and a long way from home. He cared about their souls and he cared that they would
collapse on the road.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "Another huge crowd had come to Jesus, this time in a remote and rugged place far from any town. They had been with him three whole days, listening and being healed, and now their food was completely gone, and they were a long way from home. And Jesus called his disciples over and said:"),
    # Mark 8:2
    ("jv2", JESUS, "I have compassion on the multitude, because they have now been with me three days, and have nothing to eat."),
    # Mark 8:3
    ("j3", JESUS, "And if I send them away fasting to their own houses, they will faint by the way: for divers of them came from far."),
    ("n1b", NARRATOR, "I feel for these people, he said. They have been with me three days and they have nothing left to eat. And if I send them home hungry they will collapse on the way — some of them have come a very long distance. Nobody had raised it with him. He was the one who noticed."),
    ("n2", NARRATOR, "He would not just send them off. So he turned to his disciples; but they were baffled."),
    # Mark 8:4
    ("s4", SCRIPTURE, "From whence can a man satisfy these men with bread here in the wilderness?"),
    ("n2b", NARRATOR, "Where out here, they said, could anybody get enough bread to fill a crowd this size? They were standing in a wilderness doing the arithmetic, with the man who had already fed five thousand standing right in front of them. And here they were, working the very same sums a second time, as if that first miracle had never happened."),
    ("n3", NARRATOR, "Jesus did not scold them for it. He just asked them what they already had."),
    # Mark 8:5
    ("j5", JESUS, "How many loaves have ye?"),
    # Mark 8:5
    ("s5", SCRIPTURE, "Seven."),
    ("n3b", NARRATOR, "How many loaves do you have, he asked. Seven, they said — and a few small fish. It was almost nothing against so great a need. But he took it gladly; in his hands, it was more than enough."),
    ("nbless", NARRATOR, "He had the people sit down on the ground. Then he took the seven loaves, and gave thanks, and broke them, and gave them to his disciples to set before the crowd."),
    ("n4", NARRATOR, "And once again the food did not run out. The disciples carried bread and fish through the whole multitude, and everyone ate until they were completely satisfied, thousands of people, fed from almost nothing."),
    ("n5", NARRATOR, "When they gathered up what was left over, they filled seven large baskets with the broken pieces. There was far more at the end than there had been at the start. And the numbers were the proof this was no retelling: five loaves had left twelve baskets the first time; seven loaves left seven this time. Later Jesus made the disciples count both feedings — twelve baskets, then seven — so they could never blur the two into one. He wanted both of them remembered."),
    ("n6", NARRATOR, "About four thousand people were there that day, and every single one of them went home full. Then he sent them away, cared for, in body and in soul."),
    ("n7", NARRATOR, "He did not owe them a meal. But he saw tired, hungry people a long way from home, and he could not bear to send them away empty. That is simply who he is."),
    ("card", NARRATOR, "He notices what everyone else overlooks, that you are tired, that you are running on empty, that you have come a long way. He cares about your soul, and he also cares that you would faint on the road. What ordinary need are you afraid is too small to bring to him?"),
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
