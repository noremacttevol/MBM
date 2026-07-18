#!/usr/bin/env python3
"""Narration for build-158-two-sticks — Ezekiel 37.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

Both red beats become GREEN. Every quoted line in this build is the LORD speaking directly to Ezekiel in first person or direct command — 'take thee one stick', 'I will take the stick of Joseph'. That is Jehovah, the premortal Christ, so green. Not red: a red-letter KJV prints no Old Testament in red, because Christ had not yet come in the flesh.

  kv16  Ezekiel 37:16  god (was red)
  kv19  Ezekiel 37:19  god (was red)

kv19 is NOT split. It opens 'Say unto them, Thus saith the Lord GOD;' — but that is God telling Ezekiel what to say, still God's own speech, not Ezekiel narrating. The whole segment is one speaker and stays whole.

ADDED — kv17, Ezekiel 37:17, lifted out of the narrator paraphrase in n4 ('Bring the two sticks together, God said, and join them'). It is the hinge of the whole object lesson and the viewer should hear God say it. Sits on S4 with kv16 and n4, so no new artwork. n4 now reads as the retelling that follows it.

Considered and NOT added: Ezekiel 37:18, the people's question 'Wilt thou not shew us what thou meanest by these?' It is quoted INSIDE God's speech — God predicting the question — so it would have to be spoken green while the picture shows the people asking. That reads wrong. n6 keeps it as narrator paraphrase instead.

WHY-LAW: notice whose hand does the joining. God gathers what was scattered — the records and the people both. Milk framing: this is a promise about a family being brought back together, and the video lets a viewer arrive at the rest of it on their own.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import GOD, NARRATOR

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "Among the exiles by the river, the prophet Ezekiel received an unusual assignment from God — not a sermon to preach, but an object lesson to act out, so plain that anyone watching could understand it."),
    ("n2", NARRATOR, "Take a stick, God told him — a flat wooden writing-rod — and mark it with a name: for Judah, and for the people gathered with him. One record, belonging to one part of God's scattered family."),
    ("n3", NARRATOR, "Then take a second stick, God said, and mark it with another name: for Joseph. A separate record, belonging to another branch of the same family, long divided from the first."),
    # Ezekiel 37:16
    ("kv16", GOD, "Moreover, thou son of man, take thee one stick, and write upon it, For Judah, and for the children of Israel his companions: then take another stick, and write upon it, For Joseph, the stick of Ephraim, and for all the house of Israel his companions:"),
    # Ezekiel 37:17
    ("kv17", GOD, "And join them one to another into one stick; and they shall become one in thine hand."),
    ("n4", NARRATOR, "Now here is the part that made people stop and stare. Bring the two sticks together, God said, and join them — until the two become a single stick, one solid piece, held together in your hand."),
    ("n5", NARRATOR, "Two separate records, from two separated peoples, brought together and made one. Not one erasing the other, but the two joined, each completing the other, speaking now with a single united voice."),
    ("n6", NARRATOR, "And of course the people came asking, what do you mean by this? Why two sticks made one? What are you trying to show us? God had built the question right into the lesson."),
    # Ezekiel 37:19
    ("kv19", GOD, "Say unto them, Thus saith the Lord GOD; Behold, I will take the stick of Joseph, which is in the hand of Ephraim, and the tribes of Israel his fellows, and will put them with him, even the stick of Judah, and make them one stick, and they shall be one in mine hand."),
    ("n7", NARRATOR, "Notice whose hand does the joining. God says, they shall be one in mine hand. He is the one who gathers the scattered records, and the scattered people, and binds them together into one."),
    ("n8", NARRATOR, "So this strange little sign is really a promise of gathering. God does not leave his family, or his words to them, broken into separate pieces forever. He brings them back together. So the only question is a hopeful one. When the two are made one in his hand, will you take them both up and read?"),
    ("card", NARRATOR, "God had Ezekiel join two records into one stick — two witnesses made one in his hand. He gathers what was scattered, and binds his words together. When the two are one, will you take them both up and read?"),
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
