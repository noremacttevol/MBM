#!/usr/bin/env python3
"""Narration for build-94-father-forgive-them — Luke 23.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

STAYED RED, and it is exact:
  j1  Luke 23:34  'Father, forgive them; for they know not what they do.'
  Id kept. Nothing else in this video is Jesus speaking, so nothing else is red.

THE FRAMING IS NOT RED, AND IT WAS IN WHITE ANYWAY -- SO IT WAS LIFTED TO BLUE.
n0 paraphrased Luke 23:33 in modern English. That verse is Luke writing, not
Jesus speaking, so it is SCRIPTURE (light blue), never red:
  s33  Luke 23:33  'And when they were come to the place, which is called
       Calvary, there they crucified him, and the malefactors, one on the right
       hand, and the other on the left.'
  n0 keeps its id and now retells it. This is the case the law calls out by name:
  narration inside the Gospels is the writer, and it belongs in blue.

ALSO LIFTED, on the still already named 's3-casting-lots':
  s34b Luke 23:34  'And they parted his raiment, and cast lots.'
       -- the second half of the same verse, and also Luke writing. n2b retells
       it. It is what makes the prayer land: while he was praying for them, they
       were gambling for his clothes at the foot of the cross.

RETELLING: n3 already retells the prayer in plain words ('Not, forgive them
later, if they're sorry. Forgive them now') and was left exactly as it was.

NO GREEN: the Father is prayed TO in this video, and he does not answer out loud.
Luke 23 records no words from him. Nothing added.

WOMEN: Luke 23:33-34 records no woman speaking. Luke 23:28, 'Daughters of
Jerusalem, weep not for me,' is on the road to Calvary and is red, but the women
there are wept over, not quoted. Nothing added, nothing invented.

WHY-LAW: the first thing out of his mouth on the cross was mercy for the men
holding the hammer, and he said it while it was still happening. Milk: if his
mercy reached them mid-crime, it reaches you.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    # Luke 23:33
    ("s33", SCRIPTURE, "And when they were come to the place, which is called Calvary, there they crucified him, and the malefactors, one on the right hand, and the other on the left."),
    ("n0", NARRATOR, "They brought him to a place called Calvary, and there they crucified him — between two criminals, at the hands of soldiers just following orders."),
    ("n1", NARRATOR, "He had every reason to curse them. Every right to call down judgment."),
    # Luke 23:34
    ("s34b", SCRIPTURE, "And they parted his raiment, and cast lots."),
    ("n2b", NARRATOR, "While he hung there, the soldiers divided up his clothes and threw dice for them, right at the foot of the cross. That is what was going on underneath him."),
    ("n2", NARRATOR, "And instead of a curse, the first words out of his mouth on the cross were a prayer — for the very people driving the nails."),
    # Luke 23:34
    ("j1", JESUS, "Father, forgive them; for they know not what they do."),
    ("n3", NARRATOR, "Not, forgive them later, if they're sorry. Forgive them now — while it's still happening."),
    ("n4a", NARRATOR, "That is how far his mercy reaches. If it covered the ones killing him,"),
    ("n4b", NARRATOR, "there is no one, and nothing you've done, it can't cover."),
    ("card", NARRATOR, "His first words on the cross were mercy for the ones who put him there. That mercy has your name in it too."),
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
