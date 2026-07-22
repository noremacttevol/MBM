#!/usr/bin/env python3
"""Narration for build-35-great-banquet — Luke 14.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

STAYED RED: both existing red beats are the host inside Jesus's parable, which
means they are Jesus's own words, and a red-letter KJV prints the whole parable red.
  j1  Luke 14:21  'Go out quickly into the streets and lanes of the city, and bring in
      hither the poor, and the maimed, and the halt, and the blind.'
  j2  Luke 14:23  'Go out into the highways and hedges, and compel them to come in,
      that my house may be filled.'
Both verified verbatim. Neither turns blue. The householder speaking is not a
character to be demoted to `scripture` -- he is a character Jesus is voicing.

THE FRAMING SPLIT. Luke 14:16 reads in full: 'Then said he unto him, A certain man
made a great supper, and bade many:'. The opening clause is LUKE writing and a
red-letter KJV leaves it black; everything after it is Jesus. The build carried the
frame only as modern paraphrase inside n1, so the verse is split properly, BOTH
HALVES ON THE SAME STILL S1 -- no new artwork:
  s16  Luke 14:16  'Then said he unto him,'   SCRIPTURE, light blue.
  j16  Luke 14:16  'A certain man made a great supper, and bade many:'  JESUS, red.
n1 keeps its id and is trimmed to the retelling only; its old opening 'Jesus told a
story about' was the frame and is now carried by s16.

ADDED RED, ALL INSIDE THE PARABLE. Two more of Jesus's own lines were living only in
paraphrase, and both are dialogue he puts in a character's mouth -- still red:
  j18  Luke 14:18  'I have bought a piece of ground, and I must needs go and see it:
       I pray thee have me excused.'  -- the first invited guest. n3 keeps its text and
       now retells all three excuses behind it.
  j22  Luke 14:22  'Lord, it is done as thou hast commanded, and yet there is room.'
       -- the SERVANT reporting back, and still red for the same reason. Placed on S6
       ahead of n8, so that n8's 'And there was still room' becomes its retelling and
       j2's answer on S7 lands as a genuine reply to something the viewer just heard.

LEFT AS PARAPHRASE ON PURPOSE. Luke 14:17 ('Come; for all things are now ready'), the
oxen excuse at 14:19 and the marriage excuse at 14:20 are all red and all could have
been lifted. They are left in the storyteller's voice deliberately: three verbatim
excuses back to back would be a recitation, and n3 already does the work in one clean
sweep. One excuse verbatim, the rest retold. Red now lands on S1, S3, S5, S6 and S7,
with a narrator retelling behind every one.

NOT ADDED. Luke 14:15, the man at the table who says 'Blessed is he that shall eat
bread in the kingdom of God' -- the remark that PROVOKES the parable -- would be
`scripture`, light blue, spoken outside the parable. It is genuinely tempting and it is
verbatim. It is left out because the build has no still for a dinner table before the
feast, and SPEAKER-LAW forbids inventing artwork. Flagged here in case a later art pass
wants it.

NO GREEN: no voice from heaven in Luke 14.

WOMEN: Luke 14:16-24 records no woman speaking. A wife is mentioned in the third excuse
but she is never quoted. Nothing added; nothing invented.

PRONUNCIATION: `spoken` is left empty. Nothing in the KJV lines is on the homograph
list. 'halt' here means lame, not stop, but it is pronounced identically either way, so
there is nothing for a respelling to fix -- n6's retelling carries the meaning instead.

WHY-LAW: when the ones who should have come turned him down, he did not shrink the
table. He opened the doors wider. The feast was always going to be full.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    # Luke 14:16
    ("s16", SCRIPTURE, "Then said he unto him,"),
    # Luke 14:16
    ("j16", JESUS, "A certain man made a great supper, and bade many:"),
    ("n1", NARRATOR, "A man threw a great feast. He prepared everything, the finest food, the tables set, every place ready, and he sent out his invitations."),
    ("n2", NARRATOR, "When the feast was ready, he sent his servant to tell the invited guests, come, for everything is ready now."),
    # Luke 14:18
    ("j18", JESUS, "I have bought a piece of ground, and I must needs go and see it: I pray thee have me excused."),
    ("n3", NARRATOR, "But one by one, they all made excuses. One had just bought a field and had to go see it. One had bought oxen and had to try them out. One had just married, and simply would not come."),
    ("n4", NARRATOR, "They were not evil people. They were just busy. Their own plans felt more urgent than the joy waiting for them at his table."),
    ("n5", NARRATOR, "The servant came back alone. And here is where you would expect the host to cancel the feast, hurt and offended. He did not."),
    # Luke 14:21
    ("j1", JESUS, "Go out quickly into the streets and lanes of the city, and bring in hither the poor, and the maimed, and the halt, and the blind."),
    ("n6", NARRATOR, "Go out into the streets, he said, and bring in the poor, the crippled, the blind, everyone the respectable guests would never have invited."),
    ("n7", NARRATOR, "So the servant went and found them, the overlooked and the left out, and told them there was a seat with their name on it. You can imagine their faces. Nobody had ever invited them to anything."),
    # Luke 14:22
    ("j22", JESUS, "Lord, it is done as thou hast commanded, and yet there is room."),
    ("n8", NARRATOR, "And there was still room."),
    # Luke 14:23
    ("j2", JESUS, "Go out into the highways and hedges, and compel them to come in, that my house may be filled."),
    ("n9", NARRATOR, "Go further out, he said, to the roads and the edges of town, and do not take no for an answer. Make sure they know they are truly wanted, until my house is full."),
    ("n10", NARRATOR, "That is how good he is. When the ones who should have come turned him down, he did not shrink his table. He opened the doors wider. The feast was always going to be full, and there has always been a place at it for you."),
    ("card", NARRATOR, "The table is set, and there is a seat with your name on it. What excuse have you been giving for not sitting down?"),
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
