#!/usr/bin/env python3
"""Narration for build-176-who-shall-ascend — Psalm 24.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

Both scripture beats were painted JESUS-RED and neither is Deity speaking.
Psalm 24 is David at the pen from start to finish, so this build moves red ->
BLUE with no green anywhere:
  s1  Psalm 24:3  'Who shall ascend into the hill of the LORD?...'  RED -> SCRIPTURE
  s2  Psalm 24:4  'He that hath clean hands, and a pure heart...'   RED -> SCRIPTURE

This is the subtle case. The psalm is entirely about the LORD - his hill, his
holy place, the King of glory - but the LORD never opens his mouth in it. A
psalmist asking a question about God and then answering it himself is the man
with the pen, not Deity. Green here would have made David's question sound like
God interrogating the listener.

NO SPLIT on s1/s2. They are a question and its answer, and a red-letter Bible
has no seam to mark. Wedging a narrator retelling between them would break the
one moment the psalm is built around, so they stay consecutive and n1 retells
both. That is the one retelling-rule warning left standing in this build, and it
is deliberate.

LIFTED THREE VERSES out of narrator paraphrase - the biggest change here. The
back half of this video was retelling Psalm 24 in modern English without ever
letting the viewer hear it:
  s3  Psalm 24:5  'He shall receive the blessing from the LORD...'   NEW, scripture
  s4  Psalm 24:7  'Lift up your heads, O ye gates...'                NEW, scripture
  s5  Psalm 24:8  'Who is this King of glory? The LORD strong...'    NEW, scripture
Each one is placed immediately BEFORE the narrator beat that was already
paraphrasing it, so n2, n3a/n3b and n4a/n4b now do the retelling job instead of
standing in for the verse. All three are verbatim Psalm 24 and each sits on the
same still as its narrator beat, so no new artwork is needed.

Verse ordering note: s3 is Psalm 24:5 but lands last in this video, because the
original running order already put n2 (the blessing) at the end on S9. The
arrangement is the original build's, not a change of mine.

Nothing left as paraphrase from uncertainty.

WHY-LAW: milk. The gate opens on clean hands and a pure heart - not bloodline,
not rank, not a resume. That is the most hopeful reading of the psalm and it is
the one the video keeps.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "A question was put to Israel long ago — who gets to climb the hill of the LORD and stand in his holy place?"),
    # Psalm 24:3
    ("s1", SCRIPTURE, "Who shall ascend into the hill of the LORD? or who shall stand in his holy place?"),
    # Psalm 24:4
    ("s2", SCRIPTURE, "He that hath clean hands, and a pure heart; who hath not lifted up his soul unto vanity, nor sworn deceitfully."),
    ("n1", NARRATOR, "The answer was not about bloodline or rank."),
    # Psalm 24:7
    ("s4", SCRIPTURE, "Lift up your heads, O ye gates; and be ye lift up, ye everlasting doors; and the King of glory shall come in."),
    ("n3a", NARRATOR, "Then the call goes out to the gates themselves — lift up your heads, you ancient doors,"),
    # Psalm 24:8
    ("s5", SCRIPTURE, "Who is this King of glory? The LORD strong and mighty, the LORD mighty in battle."),
    ("n4b", NARRATOR, "He is the one who comes in."),
    # Psalm 24:5
    ("s3", SCRIPTURE, "He shall receive the blessing from the LORD, and righteousness from the God of his salvation."),
    ("n2", NARRATOR, "Such a one receives blessing from the LORD, and righteousness from the God of their salvation."),
    ("card", NARRATOR, "The door is open to the one with a clean heart. Come and stand in his presence."),
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
