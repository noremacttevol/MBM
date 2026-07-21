#!/usr/bin/env python3
"""Narration for build-57-jairus-daughter — Mark 5.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

STAYED RED, and two more added.
  jv36  Mark 5:36  "Be not afraid, only believe."  -- kept its id.
  jv41  Mark 5:41  "Damsel, I say unto thee, arise."  -- kept its id, and now sits
        where it actually belongs in the verse (see the Talitha split below).
  j39   Mark 5:39  "Why make ye this ado, and weep? the damsel is not dead, but
        sleepeth."  -- MISSING ENTIRELY; n4 paraphrased it in white. Lifted verbatim
        onto the same still (S5). n4 keeps its id, trimmed to the frame; n4b retells.

THE TALITHA SPLIT. Mark 5:41 reads "And he took the damsel by the hand, and said
unto her, Talitha cumi; which is, being interpreted, Damsel, I say unto thee,
arise." A red-letter KJV inks the Aramaic AND the translation of it, and leaves
"which is, being interpreted" black -- that is Mark explaining to his Roman readers.
So S7 now carries three consecutive beats over the one image:
  jtal  [jesus]     "Talitha cumi."
  s41i  [scripture] "which is, being interpreted,"
  jv41  [jesus]     "Damsel, I say unto thee, arise."
The video was throwing away the two words Jesus actually said out loud in that room.
"Talitha" is already in the global pronunciation map, so `spoken` is left empty.

JAIRUS WAS NEVER HEARD. Mark 5:23 is a father's own words and it was white
paraphrase inside n1. Lifted verbatim as s23 [scripture -- he is a man in the story,
not Deity] on S1: "My little daughter lieth at the point of death: I pray thee, come
and lay thy hands on her, that she may be healed; and she shall live." n1 trimmed to
the frame, n1b retells.

THE MESSENGERS WERE NEVER HEARD EITHER. Mark 5:35 -- "Thy daughter is dead: why
troublest thou the Master any further?" -- lifted as s35 on S3, the sentence jv36 is
answering. Without it, "Be not afraid, only believe" is answering nothing. n3 trimmed
to the frame, n3b retells, and a new n3c retells jv36 on S4.

NO GREEN. WOMEN: the mother is present in Mark 5:40 but Mark records no words from
her, and the girl says nothing. Nothing added; nothing invented.

WHY-LAW: the message came that said stop bothering him, it's over. He answered it
before Jairus could. Milk: he is never too late, and after raising her from the dead
his very next thought was that a twelve-year-old would be hungry.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "A man named Jairus, a leader of the synagogue, pushed through the crowd and fell down at Jesus' feet, and begged him:"),
    # Mark 5:23
    ("s23", SCRIPTURE, "My little daughter lieth at the point of death: I pray thee, come and lay thy hands on her, that she may be healed; and she shall live."),
    ("n1b", NARRATOR, "My little girl is dying, he said. Please come and lay your hands on her, so she'll be healed and live. His only daughter, twelve years old, slipping away at home while he stood in the road begging."),
    ("n2", NARRATOR, "So Jesus went with him. A great crowd pressed in on every side as they hurried toward the house, the desperate father leading the way, praying there was still time."),
    ("n3", NARRATOR, "But before they arrived, messengers came from the house with the worst news a father can hear."),
    # Mark 5:35
    ("s35", SCRIPTURE, "Thy daughter is dead: why troublest thou the Master any further?"),
    ("n3b", NARRATOR, "Your daughter is dead, they said. Why bother the Teacher any further? And Jairus' heart broke in the middle of the road. But Jesus heard it too, and he spoke before the father could say anything at all."),
    # Mark 5:36
    ("jv36", JESUS, "Be not afraid, only believe."),
    ("n3c", NARRATOR, "Don't be afraid. Just keep believing. The worst thing had already happened, and Jesus told him to keep believing anyway — not that it would be undone, but that he should not stop trusting him now."),
    ("n4", NARRATOR, "At the house the mourning had already begun, people weeping and wailing loudly for the little girl. And Jesus said to them:"),
    # Mark 5:39
    ("j39", JESUS, "Why make ye this ado, and weep? the damsel is not dead, but sleepeth."),
    ("n4b", NARRATOR, "Why all this noise and crying, he asked. The child is not dead. She's asleep. And they laughed at him, certain that she was gone."),
    ("n5", NARRATOR, "He put them all outside. Then he took the girl's father and mother, and three of his closest friends, and went in quietly to where the child was lying, small and still."),
    # Mark 5:41
    ("jtal", JESUS, "Talitha cumi."),
    # Mark 5:41
    ("s41i", SCRIPTURE, "which is, being interpreted,"),
    # Mark 5:41
    ("jv41", JESUS, "Damsel, I say unto thee, arise."),
    ("n6", NARRATOR, "Two words in his own everyday Aramaic — little girl, get up. It is the kind of thing a parent says on a school morning. He took her by the hand, and immediately she got up, and began to walk. She was twelve years old. Her parents were beside themselves with wonder, holding the daughter they had already grieved as lost."),
    ("n7", NARRATOR, "And then Jesus said the most tender, ordinary thing: give her something to eat. He had just raised her from death, and his very next thought was that a growing girl would be hungry. The small things mattered to him too."),
    ("card", NARRATOR, "He is never too late, even when everyone says he is. He walks into the room the world has already given up on, takes the hand no one else could reach, and speaks life. And then he thinks of your smallest needs, too. What have you decided is finally too far gone for him?"),
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
