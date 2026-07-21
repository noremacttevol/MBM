#!/usr/bin/env python3
"""Narration for build-72-calling-matthew — Matthew 9.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

STAYED RED -- both existing red beats are Jesus in the flesh and a red-letter
KJV prints both:
  j1  Matthew 9:9    'Follow me.'
  j2  Matthew 9:12-13  'They that be whole need not a physician, but they that
      are sick. But go ye and learn what that meaneth, I will have mercy, and not
      sacrifice: for I am not come to call the righteous, but sinners to
      repentance.'  Verbatim across two verses, unchanged.
Neither carried Matthew's framing inside it, so neither needed splitting.

THE PHARISEES NOW SPEAK. n8 ended with 'asked his disciples the question that
gave the whole thing away' -- and then paraphrased the question instead of asking
it. That is the hinge of the whole story and the viewer never heard it. Lifted
verbatim as `scripture` (men in the story, not Deity):
  s11  Matthew 9:11  'Why eateth your Master with publicans and sinners?'
  n8 is trimmed to the frame, n8b carries the retelling. Both on S8.

MATTHEW'S OWN FIVE WORDS. The turn of this man's entire life is one clause and it
was in white paraphrase:
  s9   Matthew 9:9  'And he arose, and followed him.'  `scripture` -- Matthew
       writing about himself. Placed on S5, the still already built for it, with
       the existing n5 immediately after as its retelling.

NO GREEN: nothing in Matthew 9:9-13 is the Father or a voice from heaven.

WOMEN: Matthew 9:9-13 records no woman speaking. n6 mentions 'the men and women
the rest of the town had quietly given up on' -- true to the scene, but Matthew
records no words from any of them, so nothing was put in anyone's mouth.

WHY-LAW: the one thing that kept anybody away from that table was being sure they
were already fine. Milk: the door is not shut on the people who assume they would
never be let in.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "There was one job in every Galilee town that made you a traitor to your own people. Tax collector. You worked for Rome, the empire occupying your homeland, and you got rich taking money from your neighbors, most of it more than Rome even asked. Matthew had that job."),
    ("n2", NARRATOR, "So Matthew had money, and Matthew had no one. The devout would not touch him. His old friends were long gone. He sat at his booth by the road every day, counting silver, while the whole town walked a little wider around him. Rich, and completely alone."),
    ("n3", NARRATOR, "And this is the man Jesus walked up to. Not around. Up to. Past everyone who would have been a safer, more respectable choice, straight to the booth nobody else wanted to stand near."),
    # Matthew 9:9
    ("j1", JESUS, "Follow me."),
    ("n4", NARRATOR, "Two words. And notice what is missing from them. No pay it all back first. No prove you have changed. No list of conditions to clear before he was allowed to come. Just, come."),
    # Matthew 9:9
    ("s9", SCRIPTURE, "And he arose, and followed him."),
    ("n5", NARRATOR, "He got up, and he left it. The coins, the scales, the ledgers, the whole profitable, lonely life, sitting right there on the table. Matthew tells his own story in five words and does not give himself a single one of them for hesitating. He walked away from all of it that afternoon, and followed him."),
    ("n6", NARRATOR, "And then something even stranger. Jesus went to Matthew's house for dinner. And the room filled up with Matthew's kind of people. Other tax collectors. Outcasts. The men and women the rest of the town had quietly given up on. And he sat down in the middle of them and ate."),
    ("n7", NARRATOR, "Look at who is at that table. Not the respectable. Not the qualified. The people who were used to being turned away at every door, finding themselves, for once, welcome. You can see it on their faces."),
    ("n8", NARRATOR, "The religious men could not stand it. They stood at the door, too clean to come in, and asked his disciples the question that gave the whole thing away:"),
    # Matthew 9:11
    ("s11", SCRIPTURE, "Why eateth your Master with publicans and sinners?"),
    ("n8b", NARRATOR, "Why does your teacher eat with tax collectors and sinners? They did not ask it to learn anything. They asked it because they could not imagine why anyone good would want to be in that room."),
    # Matthew 9:12-13
    ("j2", JESUS, "They that be whole need not a physician, but they that are sick. But go ye and learn what that meaneth, I will have mercy, and not sacrifice: for I am not come to call the righteous, but sinners to repentance."),
    ("n9", NARRATOR, "A doctor does not spend his day with the healthy. He goes where the sickness is. Go and learn what this means, he told them — I want mercy, not sacrifice. That was his whole answer. He did not come for the people who had it all together. He came for the ones who knew that they did not."),
    ("n10", NARRATOR, "And that is the quiet turn in the story. The outcasts were close to him because they knew they needed him. The religious men stood outside, arms folded, because they were sure they did not. The only thing that kept anyone from that table was believing they were already fine."),
    ("n11", NARRATOR, "As for Matthew, the man who had spent his life writing down what other people owed became a writer of a very different kind: one of the four accounts of Jesus's life we still read today came from his pen, the Gospel of the tax collector nobody wanted. That is what the call did to him."),
    ("n12", NARRATOR, "And the table he sat at is still set. The same door is still open, the same welcome still held out to exactly the people who assume they would never be let in. He is not waiting for you to qualify. He is asking you to come and eat."),
    ("card", NARRATOR, "He walked past every respectable man in town to sit down with the one nobody else would. If the door was open that wide for the man the whole town had written off, what makes you think it is closed to you?"),
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
