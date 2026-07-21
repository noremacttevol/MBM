#!/usr/bin/env python3
"""Narration for build-112-beatitudes — Matthew 5.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

ALL FOUR RED BEATS STAY RED. jv3, jv456, jv78, jv910 are the Beatitudes
themselves, Matthew 5:3-10, spoken by Jesus in the flesh. A red-letter KJV
prints every word of them red. Nothing moved out of red in this build.

THE FIX IS FRAMING. Matthew 5:1-2 — 'And seeing the multitudes, he went up
into a mountain... And he opened his mouth, and taught them, saying' — is
Matthew writing, not Jesus speaking. It was not in the build at all; it was
only paraphrased inside n1. It is now lifted out as s1f, SCRIPTURE (light
blue), and it sits on S1 with n1, so the picture is unchanged.

EDITS TO EXISTING NARRATOR TEXT: n1 lost its closing clause ('Jesus sat down,
and turned the whole thing upside down') because s1f now says that verbatim
and the new n1b retells it. n1 now hands into the frame instead of doing the
frame's job. Nothing else in n1 changed.

RETELLING COVERAGE: already good and left alone. n2 retells jv3, n3 retells
jv456, n4 retells jv78, n5 retells jv910. No two red blocks run back to back
anywhere in this build.

WHY-LAW: the first words of the sermon are not a demand, they are a list of
who is already blessed. Milk framing — the kingdom starts with the overlooked.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "The crowds came up the mountain expecting, maybe, the usual — that God blesses the strong, the rich, the winners. Matthew was there on the grass that day, and this is how he wrote down the beginning of it."),
    # Matthew 5:1-2
    ("s1f", SCRIPTURE, "And seeing the multitudes, he went up into a mountain: and when he was set, his disciples came unto him: And he opened his mouth, and taught them, saying,"),
    ("n1b", NARRATOR, "He saw the crowd coming, climbed the hillside, and sat down. His friends gathered in close around him. And then he opened his mouth and began to teach — and turned the whole thing upside down."),
    # Matthew 5:3
    ("jv3", JESUS, "Blessed are the poor in spirit: for theirs is the kingdom of heaven."),
    ("n2", NARRATOR, "He starts with the very people the world walks past. Not the self-made and self-assured — the ones who know they have nothing to offer God but empty hands. The kingdom, he says, belongs to them first."),
    # Matthew 5:4-6
    ("jv456", JESUS, "Blessed are they that mourn: for they shall be comforted. Blessed are the meek: for they shall inherit the earth. Blessed are they which do hunger and thirst after righteousness: for they shall be filled."),
    ("n3", NARRATOR, "The grieving will be comforted. The gentle, who never push to the front, will inherit everything. Those aching to be made good will be filled. Every blessing goes to exactly the person the world would call a loser."),
    # Matthew 5:7-8
    ("jv78", JESUS, "Blessed are the merciful: for they shall obtain mercy. Blessed are the pure in heart: for they shall see God."),
    ("n4", NARRATOR, "The merciful will be shown mercy. The pure in heart — the simple, honest, unguarded ones — will actually see God. Not the clever or the powerful. The clean of heart."),
    # Matthew 5:9-10
    ("jv910", JESUS, "Blessed are the peacemakers: for they shall be called the children of God. Blessed are they which are persecuted for righteousness' sake: for theirs is the kingdom of heaven."),
    ("n5", NARRATOR, "The ones who make peace instead of winning fights are called God's own children. And even those pushed aside for doing right are not forgotten — the kingdom is theirs, too. Every last person the world overlooks, God is reaching for."),
    ("n6", NARRATOR, "So if you have ever felt small, unseen, worn thin, or passed over — listen closely. In his kingdom, you are not at the back of the line. You are exactly the one he came for. That is how upside down, and how good, his kingdom really is."),
    ("card", NARRATOR, "The world blesses the winners; Jesus blesses the overlooked — the poor, the grieving, the gentle, the merciful. Which of these blessings sounds like it was written for you?"),
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
