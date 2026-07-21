#!/usr/bin/env python3
"""Narration for build-180-before-i-formed-thee — Jeremiah 1.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

Both scripture beats were painted JESUS-RED. Jeremiah is Old Testament, so
neither can be red - and both are the LORD speaking in first person, which makes
them GREEN:
  s1  Jeremiah 1:5  'Before I formed thee in the belly I knew thee...'  RED -> GOD
  s2  Jeremiah 1:8  'Be not afraid of their faces: for I am with thee to
                     deliver thee, saith the LORD.'                     RED -> GOD

NO SPLIT on s2, and that is a judgement call worth stating. It ends with 'saith
the LORD' - technically Jeremiah's attribution wrapper, technically blue. But
peeling three words off the end of a nine-word promise would leave a stub beat
that the ear reads as a stumble, and the attribution is doing the opposite of
what a narrator clause usually does: it is pointing AT the speaker, not away
from him. Kept whole as green, which is how a listener hears it anyway.

LIFTED TWO VERSES out of narrator paraphrase - the real upgrade here. n3a and
n3b were retelling the actual exchange between Jeremiah and God in modern
English, so the viewer never got to hear the boy answer back:
  s1b  Jeremiah 1:6  'Ah, Lord GOD! behold, I cannot speak: for I am a
                      child.'                                   NEW, scripture
  g7   Jeremiah 1:7  'Say not, I am a child: for thou shalt go to all that I
                      shall send thee, and whatsoever I command thee thou
                      shalt speak.'                             NEW, god
Note the colours: Jeremiah's protest is blue, because Jeremiah is a man; God's
answer is green. That back-and-forth of blue and green IS the story, and it was
invisible before. s1b sits on ST2 with n3a and g7 sits on ST7 with n3b, so both
reuse existing artwork and n3a/n3b become the retellings they should have been.

g7 is quoted from 'Say not' onward - Jeremiah's 'But the LORD said unto me,'
wrapper is left off rather than made its own three-word beat, since n3a's setup
already tells the viewer who answers.

ADDED n1r - a narrator retelling of Jeremiah 1:5 immediately after it. Before
this, God's longest and most tender line went straight into Jeremiah's protest
with no plain-English landing at all. n1r sits on ST5 with s1.

Nothing left as paraphrase from uncertainty; all four quoted lines are verbatim
Jeremiah 1:5-8.

WHY-LAW: milk. He was known before he was born and he was scared anyway, and
God did not scold him for it - he just promised to come along. The comfort is
the point, not the calling.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import GOD, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "A young man named Jeremiah felt far too small for the job. God was calling him to speak to nations, and he was certain he could not do it."),
    ("n1", NARRATOR, "But the call did not begin the day he heard it. Long before he was born, before he ever drew a breath, the plan was already set."),
    ("n2", NARRATOR, "The God who made him had already chosen him — and blessing, not pressure, was the shape of it."),
    # Jeremiah 1:5
    ("s1", GOD, "Before I formed thee in the belly I knew thee; and before thou camest forth out of the womb I sanctified thee, and I ordained thee a prophet unto the nations."),
    ("n1r", NARRATOR, "Read that again slowly. Before I made your body, I knew you. Before you were ever born, I set you apart, and I gave you this work. God is telling a frightened young man that they had already met — long before anybody in Jerusalem knew his name."),
    # Jeremiah 1:6
    ("s1b", SCRIPTURE, "Ah, Lord GOD! behold, I cannot speak: for I am a child."),
    ("n3a", NARRATOR, "Jeremiah answered that he was only a child."),
    # Jeremiah 1:7
    ("g7", GOD, "Say not, I am a child: for thou shalt go to all that I shall send thee, and whatsoever I command thee thou shalt speak."),
    ("n3b", NARRATOR, "The LORD replied — go where I send you, speak what I command, and do not be afraid, for I am with you to deliver you."),
    # Jeremiah 1:8
    ("s2", GOD, "Be not afraid of their faces: for I am with thee to deliver thee, saith the LORD."),
    ("n4", NARRATOR, "The same God who knew you before you were born is the one who walks with you now. The calling is His; the courage is His gift."),
    ("card", NARRATOR, "You were known before you were born. You are not too small for what He has for you."),
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
