#!/usr/bin/env python3
"""Narration for build-71-calling-the-fishermen — Matthew 4.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

STAYED RED: j1, Matthew 4:19, 'Follow me, and I will make you fishers of men.'
Jesus in the flesh, red-lettered, verbatim. Unchanged, id kept. It is the only
spoken line in the passage and it is correctly red.

LIFTED OUT OF PARAPHRASE -- MATTHEW'S TWO HAMMER SENTENCES. The point of this
build is how FAST they went, and Matthew makes that point twice with two of the
shortest, hardest sentences in the Gospels. Both were only ever paraphrased in
white. They are now `scripture` (light blue -- Matthew writing, not Jesus
speaking), each on the still the paraphrase already used:
  s20  Matthew 4:20  'And they straightway left their nets, and followed him.'
       on S6, with the existing n6 immediately after as its retelling.
  s22  Matthew 4:22  'And they immediately left the ship and their father, and
       followed him.'  on S9, with the existing n9 after as its retelling. Note
       Matthew says they left the FATHER, not just the boat -- n9 already reckons
       with Zebedee, and now the verse says it out loud.
No narrator text had to be rewritten for either: n6 and n9 already open by saying
in modern English exactly what the verses say in Old English, so the retelling
rule is satisfied by segments that were already there.

NO GREEN: no Father, no voice from heaven, in Matthew 4:18-22.

WOMEN: Matthew 4:18-22 records no woman speaking. Zebedee is present and silent;
so is everyone else. Nothing added; nothing invented.

WHY-LAW: he did not go to a temple to find the qualified. He walked a working
shoreline in the middle of an ordinary workday and looked for the willing. Milk:
he takes what you already are and makes it into something that saves people.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "It is early morning on the Sea of Galilee. Not a temple, not a synagogue, not a hall full of scholars. Just a working lake at the start of an ordinary day, and the men whose whole lives were spent on it."),
    ("n2", NARRATOR, "Two brothers are out in the shallows, Simon and Andrew, throwing a net the way they had a thousand mornings before. Their hands are rough, their sleeves are wet. This is not where anyone would think to begin a kingdom."),
    ("n3", NARRATOR, "And this is where he comes. Not waiting in a holy place for the right people to find him. Walking the shoreline, in the middle of their workday, straight up to two men with a net in their hands."),
    # Matthew 4:19
    ("j1", JESUS, "Follow me, and I will make you fishers of men."),
    ("n4", NARRATOR, "Notice what he does not say. He does not tell them to become someone else first. He does not ask them to be scholars or priests. He takes the very thing they already are, and says he will make it into something that saves people. He meets them exactly as they are."),
    ("n5", NARRATOR, "Think about what it would take to make a man like Simon put his net down. He was not a boy with nothing to lose. He had a trade, a boat, a life he was good at. And one sentence from a stranger on the shore was enough."),
    # Matthew 4:20
    ("s20", SCRIPTURE, "And they straightway left their nets, and followed him."),
    ("n6", NARRATOR, "And they went at once. Not next season, not once they had saved a little more. That very morning, with the net still wet, they left it on the sand and followed him, and did not look back."),
    ("n7", NARRATOR, "A little further along, two more brothers, James and John, sat in a boat mending the day's torn nets beside Zebedee, their father. The family trade, three lives on the same water."),
    ("n8", NARRATOR, "And he called them too. The same voice, the same invitation, held out to two more ordinary men doing ordinary work."),
    # Matthew 4:22
    ("s22", SCRIPTURE, "And they immediately left the ship and their father, and followed him."),
    ("n9", NARRATOR, "And they did the same thing. Right then they climbed out of the boat, left the half-mended nets in the hull, and went. Matthew does not soften it — they left the boat AND they left their father. You can see old Zebedee there, watching his two sons walk away. The cost was real. But he does not call them back, and they do not turn around."),
    ("n10", NARRATOR, "So the ones who followed him down the shore that morning were four fishermen. No titles, no training, no credentials. The men he chose first to carry the whole thing were the men everyone else would have walked right past."),
    ("n11", NARRATOR, "That is the good news hiding in this small story. He did not go looking for the qualified. He went looking for the willing. He left the empty boats on the sand and took the men, because it was never about how impressive they were. It was only about whether they would come."),
    ("n12", NARRATOR, "And the strange thing is, that shoreline is not closed. The same voice that walked up to men at their nets still walks up to ordinary people in the middle of ordinary days. He is not asking you to clean up first. He is asking you to come."),
    ("card", NARRATOR, "He walked up to four working men on a normal morning and made them part of the greatest story ever told, exactly as they were. If he would walk up to a fishing boat and call the men there by name, what makes you think he would walk past you?"),
]

# Homographs this build decides for itself (never auto-replaced globally).
SPOKEN = {}


SPOKEN.update({'zebedee': 'zebbuhdee'})  # round2 in-context A/B winners 2026-07-20 (SWEEP/round2-state.json)

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
