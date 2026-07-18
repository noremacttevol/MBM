#!/usr/bin/env python3
"""Narration for build-114-abraham-sodom — Genesis 18.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

Both scripture lines were painted JESUS-RED and neither is Jesus in the flesh.
Genesis 18 is Jehovah — the premortal Christ — so both are GREEN.

Two of Abraham's own lines were buried inside narrator paraphrase and are now
lifted out as SCRIPTURE so the viewer hears the man actually plead:
  s23  Gen 18:23  'Wilt thou also destroy the righteous with the wicked?'
  s32  Gen 18:32a 'Oh let not the Lord be angry...'

Gen 18:32 is a genuinely mixed verse — Abraham's plea AND God's reply in one
breath — so it is split: s32 (blue) then jv32 (green). Both halves stay on the
same still, so the picture the viewer sees is unchanged.

WHY-LAW: Abraham is not wearing God down. He is discovering how merciful God
already was. Milk framing — God welcomes the bold intercessor.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import GOD, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "In the heat of the day, three travelers appeared at Abraham's tent. He did not know at first who they were. He only knew they were strangers, and tired, and that hospitality was sacred."),
    ("n2", NARRATOR, "He washed their feet, baked fresh bread, set out the best he had, and waited on them himself under the oak. And as they ate, they brought him astonishing news — and a heavy word about Sodom."),
    ("n3", NARRATOR, "For those cities had grown very dark, and judgment was near. Two of the travelers went on ahead. But Abraham stayed behind, standing before the warm presence of the Lord — and he began to plead."),
    ("n4", NARRATOR, "Not for himself. For strangers — for the good people who might still be down in that doomed city."),
    # Genesis 18:23
    ("s23", SCRIPTURE, "Wilt thou also destroy the righteous with the wicked? Shall not the Judge of all the earth do right?"),
    # Genesis 18:26
    ("jv26", GOD, "If I find in Sodom fifty righteous within the city, then I will spare all the place for their sakes."),
    ("n5", NARRATOR, "Yes, God said. For fifty, I will spare them all. And you can almost feel Abraham's courage grow. What about forty-five? What about forty? Thirty? Each time, gently, the answer came back — yes. Yes. I will spare it."),
    ("n6", NARRATOR, "He is not wearing God down. He is discovering how merciful God already is — how much God would rather spare than destroy. So Abraham dares one last step."),
    # Genesis 18:32
    ("s32", SCRIPTURE, "Oh let not the Lord be angry, and I will speak yet but this once: Peradventure ten shall be found there."),
    # Genesis 18:32
    ("jv32", GOD, "I will not destroy it for ten's sake."),
    ("n6b", NARRATOR, "Let me speak just once more, Abraham said. What if there are only ten? And the answer came back the same as every time before — for ten, I will not destroy it."),
    ("n7", NARRATOR, "For the sake of ten good people, the whole place would be spared. That is the God Abraham found at the top of that hill. Not one straining to condemn — one who could be talked, again and again, toward mercy."),
    ("n8", NARRATOR, "Abraham went home in the dusk, amazed. He had dared to plead for strangers, and found God kinder than he had hoped. God let a man argue with him — and kept saying yes."),
    ("card", NARRATOR, "God let one old man plead for strangers, and answered mercy every time. He is not looking for reasons to condemn — he welcomes the bold and the interceding. What would you dare ask him for?"),
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
