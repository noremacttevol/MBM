#!/usr/bin/env python3
"""Narration for build-56-widow-of-nain — Luke 7.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

THE WIDOW DOES NOT SPEAK, AND I DID NOT INVENT A LINE FOR HER. Luke 7:11-17 is the
one raising in the gospels where the grieving parent says nothing at all -- no
request, no plea, not one recorded word. She is the reason the miracle happens and
she never asks for it. That silence is the point of the story and it is now said out
loud in the narration (n3) instead of being an accident. NO `woman` beat in this
build. Checked Luke 7 twice; there is nothing there to lift.

STAYED RED, both of them:
  jv13  Luke 7:13  "Weep not."
  jv14  Luke 7:14  "Young man, I say unto thee, Arise."
Both kept their ids.

NARRATION FRAMING SPLIT OFF BOTH. Luke welds his own writing onto each red line, and
both frames were sitting in white paraphrase:
  s13a  Luke 7:13  "And when the Lord saw her, he had compassion on her, and said
        unto her,"  -- new [scripture] beat on S4, same still as jv13.
  s14a  Luke 7:14  "And he came and touched the bier: and they that bare him stood
        still. And he said,"  -- new [scripture] beat on S6, same still as jv14.
        n4 is trimmed to its setup; n4b carries the retelling.

THE TOWN SPEAKS, AND IT WAS IN WHITE. n7 paraphrased Luke 7:16. Lifted verbatim as
s16 [scripture] on S9: "That a great prophet is risen up among us; and, That God
hath visited his people." n7 keeps its id, trimmed to the frame; n7b retells it.

NO GREEN: the crowd says God has visited his people, but God does not speak in this
passage. Nothing green.

WHY-LAW: nobody asked him. He met a funeral coming out of a gate, saw one woman at
the back of it, and could not walk past. Milk: he is not waiting to be asked.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "As Jesus came near the town of Nain, a great crowd walked along with him. It was an ordinary day on an ordinary road, until they reached the town gate and met something coming the other way."),
    ("n2", NARRATOR, "Out of the gate came a funeral. A young man had died, carried out on an open bier, and behind him walked his mother, a widow, grieving. He was her only son, and now she had no one. A large crowd from the town walked with her in her sorrow."),
    ("n3", NARRATOR, "Here is what Luke does not record: a single word from her. She never asks him for anything. She does not know who he is. She is simply walking behind her son's body. And when the Lord saw her, he did not see a crowd or a custom; he saw a mother who had lost everything."),
    # Luke 7:13
    ("s13a", SCRIPTURE, "And when the Lord saw her, he had compassion on her, and said unto her,"),
    # Luke 7:13
    ("jv13", JESUS, "Weep not."),
    ("n3b", NARRATOR, "Don't cry. Two words, to the one woman in that whole procession nobody could comfort. No one there had asked him to do a single thing. He simply could not walk past her sorrow."),
    ("n4", NARRATOR, "Then he did something no one does at a funeral."),
    # Luke 7:14
    ("s14a", SCRIPTURE, "And he came and touched the bier: and they that bare him stood still. And he said,"),
    # Luke 7:14
    ("jv14", JESUS, "Young man, I say unto thee, Arise."),
    ("n4b", NARRATOR, "He walked up and put his hand on the open bier, and the men carrying it stopped dead. The whole procession held its breath. And he spoke to the dead boy the way you would wake a sleeping child — young man, I say to you, get up."),
    ("n5", NARRATOR, "And the young man who had been dead sat up, and began to speak. Life poured back into him at the sound of that voice, as simply as morning comes. Death let go of him, because it had no choice."),
    ("n6", NARRATOR, "And Jesus took him by the hand and gave him back to his mother. He did not keep him or make a spectacle of him; he simply returned a son to the arms of the woman who thought she had buried him."),
    ("n7", NARRATOR, "A holy fear fell on everyone there, and they praised God, saying:"),
    # Luke 7:16
    ("s16", SCRIPTURE, "That a great prophet is risen up among us; and, That God hath visited his people."),
    ("n7b", NARRATOR, "A great prophet has risen among us, they said. God has come to his own people. And the news of it went out through all the country round about."),
    ("card", NARRATOR, "He still meets us at the gate, on the worst day, in the middle of a grief no one can fix. He is not put off by death, or by sorrow, or by a thing everyone else has given up on. He sees you, his heart breaks, and he speaks life. What have you already buried that he is asking to raise?"),
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
