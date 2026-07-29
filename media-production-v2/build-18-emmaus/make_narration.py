#!/usr/bin/env python3
"""Narration for build-18-emmaus — Luke 24.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

Luke 24:13-35. j1 is the risen Christ speaking and a red-letter KJV inks it,
so it stays RED. The two disciples on the road are men in the story, not Jesus, so
their four verbatim lines are SCRIPTURE (blue). All four were narrator paraphrase:
  s18  Luke 24:18  Cleopas: 'Art thou only a stranger in Jerusalem...'
  s21  Luke 24:21  'But we trusted that it had been he which should have redeemed Israel.'
  s29  Luke 24:29  'Abide with us: for it is toward evening, and the day is far spent.'
  s32  Luke 24:32  'Did not our heart burn within us, while he talked with us by the
       way, and while he opened to us the scriptures?' - the line the whole video is
       built around, and it was not in it.
n11 is the closing card and keeps its id. still_vars S1..S8 introduced.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "It was the same Sunday. The tomb was empty, the rumors were flying, and two of Jesus's followers had given up and left. They were walking the seven miles from Jerusalem to a village called Emmaus, heads down, going over it all again — the arrest, the cross, the end of everything they had hoped for."),
    ("n1", NARRATOR, "As they walked and argued and grieved, a stranger came up alongside them and fell into step. And Luke tells us something strange and deliberate: their eyes were held, so that they did not recognize him. It was Jesus himself — walking right beside them — and they had no idea."),
    ("n2", NARRATOR, "He asked them what they were talking about that had them so heavy. They stopped in the road, faces stricken. One of them, Cleopas, said: are you the only visitor to Jerusalem who doesn't know what has happened these last few days?"),
    # Luke 24:18
    ("s18", SCRIPTURE, "Art thou only a stranger in Jerusalem, and hast not known the things which are come to pass there in these days?"),
    ("n3", NARRATOR, "And it all poured out. Jesus of Nazareth — a prophet mighty in word and deed — handed over and crucified. And then the line that holds all their heartbreak: we had hoped that he was the one who would rescue Israel. Now some women were saying the tomb was empty and angels said he was alive. But nobody had seen him."),
    # Luke 24:21
    ("s21", SCRIPTURE, "But we trusted that it had been he which should have redeemed Israel."),
    ("n4a", NARRATOR, "The stranger listened to all of it. And then he answered them:"),
    # Luke 24:25-26
    ("j1", JESUS, "O fools, and slow of heart to believe all that the prophets have spoken: Ought not Christ to have suffered these things, and to enter into his glory?"),
    ("n4b", NARRATOR, "And then, starting all the way back at Moses, walking through prophet after prophet, he opened the scriptures to them — showing them every place the whole story had been pointing to a rescuer who had to be broken before he could be crowned. The cross was not the collapse of the plan. It was the plan."),
    ("n5", NARRATOR, "They reached Emmaus as the sun was going down, and the stranger acted as if he would keep walking on into the night. But they couldn't let him go. Stay with us, they said — it's nearly evening, the day is almost gone. So he went in to stay."),
    # Luke 24:29
    ("s29", SCRIPTURE, "Abide with us: for it is toward evening, and the day is far spent."),
    ("n6", NARRATOR, "They sat down to the table. And then their guest did the one thing only the host of the house should do. He took the bread. He blessed it. He broke it. And he held it out to them."),
    ("n7", NARRATOR, "And in that motion — the taking, the blessing, the breaking of the bread — their eyes were opened, and they knew him. It was Jesus. And in the very instant they recognized him, he was gone — vanished from the table, the bread still warm in their hands."),
    ("n8", NARRATOR, "They turned to each other, stunned. Weren't our hearts burning inside us, they said, the whole time he was talking to us on the road, while he opened the scriptures to us? He had been with them the entire way, and they had almost missed him."),
    # Luke 24:32
    ("s32", SCRIPTURE, "Did not our heart burn within us, while he talked with us by the way, and while he opened to us the scriptures?"),
    ("n9", NARRATOR, "They did not wait for morning. That same hour they got up and ran the seven dark miles back to Jerusalem, found the eleven, and said the words the whole world had been aching to hear: the Lord is risen. It's true. We have seen him."),
    ("n10", NARRATOR, "Notice how the risen Jesus spent that first afternoon. Not with kings. Not with crowds. On a dusty road, with two heartbroken people who had already quit — walking at their pace, patiently opening the scriptures, until the moment they could see. He is still in the habit of walking with the ones who have lost hope."),
    ("n11", NARRATOR, "He walked with them a long way before they knew who he was. Is it possible he has been walking with you — in a season you thought you were walking alone?"),
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
