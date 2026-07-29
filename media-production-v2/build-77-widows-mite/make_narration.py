#!/usr/bin/env python3
"""Narration for build-77-widows-mite — Mark 12.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

STAYED RED: j1, Mark 12:43-44, 'Verily I say unto you, That this poor widow
hath cast more in, than all they which have cast into the treasury: for all they
did cast in of their abundance; but she of her want did cast in all that she had,
even all her living.' Verbatim across two verses, Jesus in the flesh,
red-lettered. Unchanged, id kept. It is the only spoken line in the passage.

THE WIDOW DOES NOT SPEAK. This is the honest answer and it is worth stating
plainly, because a build about a woman is exactly where the temptation to invent
lives. Mark 12:41-44 records not one word from her. She walks in, she puts in two
mites, she walks out, and she never learns that anyone noticed. NOTHING was put
in her mouth. No pink in this build, and that is correct. The silence is part of
what the story is about -- n4a and n4b are built on it.

LIFTED OUT OF PARAPHRASE -- MARK'S TWO SETUP VERSES, now `scripture` (light blue,
Mark writing), each on the still the paraphrase already used:
  s41  Mark 12:41  'And Jesus sat over against the treasury, and beheld how the
       people cast money into the treasury: and many that were rich cast in much.'
       on ST1, with n1a immediately after as its retelling. Note what the verse
       says he was doing: he SAT and he BEHELD. He set out to watch people give.
       That is the frame the whole video hangs on.
  s42  Mark 12:42  'And there came a certain poor widow, and she threw in two
       mites, which make a farthing.'  on ST5, with the existing n2b immediately
       after as its retelling -- n2b already says 'two tiny copper coins, together
       worth less than a penny', which is exactly what a farthing is.
Neither required rewriting a narrator segment: n1a and n2b were already the plain
modern retellings of the verses they now follow.

NO GREEN: nothing in Mark 12:41-44 is the Father or a voice from heaven.

WHY-LAW: the one gift nobody in the building saw was the only one heaven was
counting. Milk: he is already looking at the thing about you that no one else
noticed.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "Jesus sat down across from the temple treasury and just watched people give."),
    # Mark 12:41
    ("s41", SCRIPTURE, "And Jesus sat over against the treasury, and beheld how the people cast money into the treasury: and many that were rich cast in much."),
    ("n1a", NARRATOR, "He sat down facing the collection boxes and watched how people put their money in. And the rich came through and put in large amounts."),
    ("n1b", NARRATOR, "You could hear the coins land, and everyone noticed."),
    ("n2a", NARRATOR, "Then a poor widow came, small and unnoticed."),
    # Mark 12:42
    ("s42", SCRIPTURE, "And there came a certain poor widow, and she threw in two mites, which make a farthing."),
    ("n2b", NARRATOR, "She put in two tiny copper coins — together worth less than a penny. That is the whole of what Mark records about her. She does not say a word, and nobody in that courtyard looks up."),
    ("n3", NARRATOR, "Jesus called his disciples over, like he had just seen the most important thing all day."),
    # Mark 12:43-44
    ("j1", JESUS, "Verily I say unto you, That this poor widow hath cast more in, than all they which have cast into the treasury: for all they did cast in of their abundance; but she of her want did cast in all that she had, even all her living."),
    ("n4a", NARRATOR, "I'm telling you the truth, he said — this poor widow has put in more than every one of them. They gave out of what they had spare. She gave out of what she did not have. Everyone else gave from what they had left over. She gave from what she needed."),
    ("n4b", NARRATOR, "Heaven does the math differently than we do."),
    ("card", NARRATOR, "He noticed the gift no one else did. What might he already see in you that others overlook?"),
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
