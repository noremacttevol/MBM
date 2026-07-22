#!/usr/bin/env python3
"""Narration for build-54-the-leper — Mark 1.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

STAYED RED: jv41 "I will; be thou clean." (Mark 1:41) is Jesus in the flesh and a
red-letter KJV inks exactly those four words -- and only those. Kept its id.

NARRATION FRAMING SPLIT OFF IT. Mark 1:41 reads "And Jesus, moved with compassion,
put forth his hand, and touched him, and saith unto him, I will; be thou clean."
Everything before the comma is Mark writing, not Jesus speaking, so it is now s41a
[scripture, light blue] sitting on the SAME still (S4) immediately before jv41. No
new artwork, and the edit the viewer sees is unchanged.

THE LEPER WAS NEVER HEARD. His one line -- the whole hinge of the story -- was
sitting inside n2 as modern paraphrase in white. Lifted verbatim as s40 [scripture],
same still (S2): "If thou wilt, thou canst make me clean." (Mark 1:40)
  WORDING NOTE: the brief you may have in mind, "Lord, if thou wilt, thou canst make
  me clean," is Matthew 8:2 / Luke 5:12. This build is Mark 1, and Mark 1:40 has no
  "Lord." Used the Mark form so a viewer who looks up Mark 1:40 finds it word for
  word. Both are exact; only one belongs in a Mark video.
  n2 is trimmed to the frame only and a new n2b carries the retelling it used to
  carry.

JESUS'S SECOND RED LINE WAS MISSING ENTIRELY. n6 paraphrased Mark 1:44 in white.
Lifted as j44 [jesus] on S7: "See thou say nothing to any man: but go thy way, shew
thyself to the priest, and offer for thy cleansing those things which Moses
commanded, for a testimony unto them." n6 keeps its id, trimmed to the frame; n6b
retells it.

NO GREEN: nothing in Mark 1:40-45 is the Father or a voice from heaven.

WOMEN: Mark 1:40-45 records no woman speaking. Nothing added; nothing invented.

WHY-LAW: he never doubted the power, only the will -- and the answer was two words
long. Milk: the reaching hand came before the healing did. The untouchable man was
touched first.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "In those days there was no lonelier life than a leper's. The disease wasted his skin, and the law kept him apart from everyone he loved — no home, no temple, no touch, made to cry out 'unclean' if anyone drew near. He had not felt a kind hand in years."),
    ("n2", NARRATOR, "When he heard that Jesus was near, he did the forbidden thing: he came close. He fell on his knees and begged him."),
    # Mark 1:40
    ("s40", SCRIPTURE, "If thou wilt, thou canst make me clean."),
    ("n2b", NARRATOR, "If you are willing, he said, you can make me clean. He never doubted the power. He only wondered about the will — whether a man like him was someone Jesus would want to bother with."),
    ("n3", NARRATOR, "And Jesus was moved with compassion. He did not step back from the man everyone else stepped back from. He reached out his hand toward the very thing no one would touch."),
    # Mark 1:41
    ("s41a", SCRIPTURE, "And Jesus, moved with compassion, put forth his hand, and touched him, and saith unto him,"),
    # Mark 1:41
    ("jv41", JESUS, "I will; be thou clean."),
    ("n4", NARRATOR, "I will. Two words, and the wondering was over. And he touched him. Before the healing had even come, the untouchable man was touched; and then, at once, the leprosy left him, and his skin was made new."),
    ("n5", NARRATOR, "The sores were gone. The pale, wasted skin was warm and whole again, like the skin of a young child. In a moment he was clean, and more than clean; he was a man who could go home."),
    ("n6", NARRATOR, "Then Jesus sent him away with strict instructions."),
    # Mark 1:44
    ("j44", JESUS, "See thou say nothing to any man: but go thy way, shew thyself to the priest, and offer for thy cleansing those things which Moses commanded, for a testimony unto them."),
    ("n6b", NARRATOR, "Say nothing to anyone, he told him. Just go and show yourself to the priest, and make the offering Moses commanded — and be given back, quietly and legally, the whole life that had been taken from you."),
    ("n7", NARRATOR, "But the man could not hold it in. He went out and told everyone, freely, everywhere; how could he not? The mercy was far too great to keep to himself."),
    ("n8", NARRATOR, "And so the news ran ahead of him, until he could hardly walk into a town in the open, and people came to him from every direction, out of every corner of the land."),
    ("card", NARRATOR, "He is still willing. There is no part of you so unclean, so far gone, so long untouched, that he will draw back his hand from it. He reaches for the very thing you are most ashamed of and says, I will. What would you ask him to make clean?"),
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
