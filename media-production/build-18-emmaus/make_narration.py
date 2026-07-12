#!/usr/bin/env python3
"""Narration for Story Video #18 — The Road to Emmaus (Luke 24:13-35).
Narrator: en-US-AndrewNeural (plain American, never Multilingual).
Jesus: en-US-ChristopherNeural (American). Jesus speaks ONLY exact KJV
Luke 24:25-26 (j1) from qc/luke24-kjv.txt. Translation Law: the narrator
never echoes j1's wording; the disciples' and the eleven's words may be
paraphrased. STILLS-ONLY + Face Law (#18): they never recognize him on the
road, so his face is simply never shown.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"
JESUS = "en-US-ChristopherNeural"

SEGMENTS = [
    ("n0", NARRATOR, "-20%", "-4Hz",
     "It was the same Sunday. The tomb was empty, the rumors were flying, "
     "and two of Jesus's followers had given up and left. They were walking "
     "the seven miles from Jerusalem to a village called Emmaus, heads down, "
     "going over it all again — the arrest, the cross, the end of everything "
     "they had hoped for."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "As they walked and argued and grieved, a stranger came up alongside "
     "them and fell into step. And Luke tells us something strange and "
     "deliberate: their eyes were held, so that they did not recognize him. "
     "It was Jesus himself — walking right beside them — and they had no "
     "idea."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "He asked them what they were talking about that had them so heavy. "
     "They stopped in the road, faces stricken. One of them, Cleopas, said: "
     "are you the only visitor to Jerusalem who doesn't know what has "
     "happened these last few days?"),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "And it all poured out. Jesus of Nazareth — a prophet mighty in word "
     "and deed — handed over and crucified. And then the line that holds "
     "all their heartbreak: we had hoped that he was the one who would "
     "rescue Israel. Now some women were saying the tomb was empty and "
     "angels said he was alive. But nobody had seen him."),
    ("n4a", NARRATOR, "-22%", "-4Hz",
     "The stranger listened to all of it. And then he answered them:"),
    ("j1", JESUS, "-26%", "-6Hz",
     "O fools, and slow of heart to believe all that the prophets have "
     "spoken: Ought not Christ to have suffered these things, and to enter "
     "into his glory?"),
    ("n4b", NARRATOR, "-22%", "-4Hz",
     "And then, starting all the way back at Moses, walking through prophet "
     "after prophet, he opened the scriptures to them — showing them every "
     "place the whole story had been pointing to a rescuer who had to be "
     "broken before he could be crowned. The cross was not the collapse of "
     "the plan. It was the plan."),
    ("n5", NARRATOR, "-20%", "-4Hz",
     "They reached Emmaus as the sun was going down, and the stranger acted "
     "as if he would keep walking on into the night. But they couldn't let "
     "him go. Stay with us, they said — it's nearly evening, the day is "
     "almost gone. So he went in to stay."),
    ("n6", NARRATOR, "-22%", "-4Hz",
     "They sat down to the table. And then their guest did the one thing "
     "only the host of the house should do. He took the bread. He blessed "
     "it. He broke it. And he held it out to them."),
    ("n7", NARRATOR, "-24%", "-4Hz",
     "And in that motion — the taking, the blessing, the breaking of the "
     "bread — their eyes were opened, and they knew him. It was Jesus. And "
     "in the very instant they recognized him, he was gone — vanished from "
     "the table, the bread still warm in their hands."),
    ("n8", NARRATOR, "-22%", "-4Hz",
     "They turned to each other, stunned. Weren't our hearts burning inside "
     "us, they said, the whole time he was talking to us on the road, while "
     "he opened the scriptures to us? He had been with them the entire way, "
     "and they had almost missed him."),
    ("n9", NARRATOR, "-20%", "-4Hz",
     "They did not wait for morning. That same hour they got up and ran the "
     "seven dark miles back to Jerusalem, found the eleven, and said the "
     "words the whole world had been aching to hear: the Lord is risen. "
     "It's true. We have seen him."),
    ("n10", NARRATOR, "-24%", "-4Hz",
     "Notice how the risen Jesus spent that first afternoon. Not with kings. "
     "Not with crowds. On a dusty road, with two heartbroken people who had "
     "already quit — walking at their pace, patiently opening the scriptures, "
     "until the moment they could see. He is still in the habit of walking "
     "with the ones who have lost hope."),
    ("n11", NARRATOR, "-26%", "-4Hz",
     "He walked with them a long way before they knew who he was. Is it "
     "possible he has been walking with you — in a season you thought you "
     "were walking alone?"),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
