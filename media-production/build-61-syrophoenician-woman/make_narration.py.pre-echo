#!/usr/bin/env python3
"""Narration for build-61-syrophoenician-woman — Mark 7.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

THIS BUILD IS HERS AND SHE NEVER SPOKE IN IT. The whole video turns on one sentence
a Gentile mother says to Jesus, and that sentence was sitting inside n5 as modern
paraphrase in white. It is now w28 [woman, pink], verbatim, on the SAME still (S5):

  w28  Mark 7:28  "Yes, Lord: yet the dogs under the table eat of the children's
       crumbs."

  WHICH GOSPEL, AND WHY IT MATTERS. Matthew 15:27 has her saying "Truth, Lord: yet
  the dogs eat of the crumbs which fall from their masters' table," and that is
  every bit as bold and every bit as exact. But this build is Mark 7 -- j1 is Mark
  7:27 and j2 is Mark 7:29 -- and Mark's own wording is what n5 was already
  paraphrasing ("even the pups under the table get what the children drop").
  Putting Matthew's version of her reply between Mark's version of his two lines
  would give a viewer a page that does not match what they are hearing. Used Mark
  7:28. The Matthew wording is recorded here, exact, if a later pass would rather
  have it.

  HER EARLIER CRY -- CHECKED, AND IT IS NOT IN THIS GOSPEL. "Have mercy on me, O
  Lord, thou son of David; my daughter is grievously vexed with a devil" is Matthew
  15:22. Mark has no such cry; Mark 7:26 only reports, in the evangelist's own
  voice, that "she besought him that he would cast forth the devil out of her
  daughter" -- indirect speech, not a quotation. So n2 stays narrator paraphrase.
  Left out because Mark does not record it, not because I am unsure of the wording.

STAYED RED, both, and both kept their ids:
  j1  Mark 7:27  "Let the children first be filled: for it is not meet to take the
      children's bread, and to cast it unto the dogs."
  j2  Mark 7:29  "For this saying go thy way; the devil is gone out of thy daughter."
Neither had Mark's framing welded onto it, so neither needed splitting. n4 already
does the work of explaining j1 before she answers it, and it is left alone.

n5 keeps its id, trimmed to the frame; n5b carries the retelling it used to carry.

NO GREEN. WHY-LAW: he did not praise her manners. He praised her saying -- "for this
saying." She heard a door where everyone else would have heard a no, and walked
through it. Milk: there is room for you at his table, and he is glad when you insist
on it.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, WOMAN

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "Jesus went north — out of Jewish land entirely, up to the coast around Tyre. Gentile country. He slipped into a house and wanted no one to know he was there. But Mark says it plainly: he could not be hidden. Word about him had crossed the border long before he did."),
    ("n1", NARRATOR, "And one woman heard it. A Greek, born in that country — a Syrophoenician, which is Mark's way of saying: not one of us. Wrong nation, wrong religion, no claim at all on a Jewish rabbi. But her little girl was sick with something dark that no one could fix. And a mother with a sick child does not care about borders."),
    ("n2", NARRATOR, "She found the house. She came in uninvited, fell down at his feet, and begged him — cast this thing out of my daughter. Every social rule in the room said she had no right to ask. She asked anyway."),
    ("n3", NARRATOR, "What Jesus said next sounds harsh — until you hear it the way she heard it."),
    # Mark 7:27
    ("j1", JESUS, "Let the children first be filled: for it is not meet to take the children's bread, and to cast it unto the dogs."),
    ("n4", NARRATOR, "Here is the why. Let the children be fed first — that was his mission order: Israel first, then the whole world. And the word he chose was not the word for street dogs. It was the word for the little pups a family keeps under its own table. He had not slammed a door. He had painted a picture of a household — and left her a place in it, if she could see it. She saw it instantly."),
    ("n5", NARRATOR, "She did not argue with him. She stepped right into the picture he had painted, and answered him:"),
    # Mark 7:28
    ("w28", WOMAN, "Yes, Lord: yet the dogs under the table eat of the children's crumbs."),
    ("n5b", NARRATOR, "Yes, Lord — but even the pups under the table get what the children drop. She did not ask him to change the order. She just pointed out that there is food under a table too. Bible students love this moment: it is the only time in the gospels anyone wins an exchange with Jesus. And you can almost hear how glad he was to lose it."),
    ("n6", NARRATOR, "He answered her:"),
    # Mark 7:29
    ("j2", JESUS, "For this saying go thy way; the devil is gone out of thy daughter."),
    ("n7", NARRATOR, "Because you said that — go on home. It is already done. Notice what he did not do. He did not walk to her house. He did not touch the girl. He simply said it was finished, across the distance, on his word alone. And she believed him enough to just... go home. That walk home, holding nothing but his word, was the faith he praised."),
    ("n8", NARRATOR, "She came to her door and found her daughter lying on the bed, resting — quiet, and whole. The dark thing was gone. It had left at the exact moment he spoke."),
    ("n9", NARRATOR, "The first outsider in Mark's gospel to be told yes was a Gentile mother with no credentials, no standing, and no appointment — just a stubborn, clear-eyed faith that would not leave without the crumbs. He gave her the whole loaf."),
    ("card", NARRATOR, "She refused to believe there was no room for her at his table. There is room for you."),
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
