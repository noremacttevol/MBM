#!/usr/bin/env python3
"""Narration audio for Video #104 — The Boy Samuel (1 Samuel 3:1-19).

Narrator: en-US-AndrewNeural. The Lord's voice: en-US-ChristopherNeural (exact KJV
only). Samuel's own words ("Speak, LORD...") are voiced by the NARRATOR (the Lord's
voice is reserved for the Lord's own words); Samuel's line renders as a plain white
caption, the Lord's call renders cream-italic.

The Lord's KJV line (Christopher, cream italic):
  jv10  1 Sam 3:10  "Samuel, Samuel." — the call by name (sacred silence)

WHY-LAW: 'the word of the LORD was precious in those days; there was no open vision.'
Into that silence God did not summon a priest or a king — he called a child, by name,
in the dark, three times, patiently, until the boy learned to listen. Milk framing: God
still calls gently, by name, and waits for a heart that will say, speak, I am listening.
The hard message about Eli's house is left off-screen; the heart is the call and the
listening. An invitation, never a threat.

HOMOGRAPH EAR-CHECK: none of the high-risk homographs appear. NUMBER-STRESS LAW obeyed.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"
LORD = "en-US-ChristopherNeural"

SEGMENTS = [
    ("n1", NARRATOR, "-20%", "-4Hz",
     "In those days the word of the Lord was rare. People had stopped hearing from God, "
     "and it was a quiet, dim time. But one small lamp still burned in the house of God "
     "at night — and a boy slept nearby.", None),
    ("n2", NARRATOR, "-22%", "-4Hz",
     "Samuel was only a child, given to serve in the tabernacle. He lay asleep on his "
     "mat near the holy place while the old priest Eli, nearly blind with age, slept in "
     "his room.", None),
    ("n3", NARRATOR, "-22%", "-4Hz",
     "And in the dark, a voice called his name. Samuel. He sat straight up. He thought it "
     "was old Eli needing him, so he ran to him and said, here I am; you called me.", None),
    ("n4", NARRATOR, "-22%", "-4Hz",
     "But Eli said, I did not call you. Go back and lie down. So he did. And the voice "
     "came again — Samuel — and again he ran to the old man, and again Eli sent him back. "
     "It happened a third time.", None),
    ("n5", NARRATOR, "-22%", "-4Hz",
     "Then Eli understood. This was no dream, and it was not his voice. It was God "
     "himself, calling the child. So the old priest gently taught the boy what to do.", None),
    ("n6", NARRATOR, "-22%", "-4Hz",
     "If he calls you again, Eli said, do not run to me. Answer him. Say: speak, Lord, "
     "for thy servant heareth. So Samuel went and lay down in his place, and waited in "
     "the dark.", None),
    # jv10 — the call by name, sacred silence
    ("jv10", LORD, "-26%", "-6Hz",
     "Samuel, Samuel.", None),
    # Samuel's answer — narrator voice, white caption
    ("ns", NARRATOR, "-22%", "-2Hz",
     "And the boy answered: Speak; for thy servant heareth.", None),
    ("n7", NARRATOR, "-22%", "-4Hz",
     "Speak — I am listening. That was all God had been waiting for. A heart small "
     "enough and open enough to stop running around and simply listen. And God spoke to "
     "him, and told him true things, and stayed with him.", None),
    ("n8", NARRATOR, "-24%", "-4Hz",
     "Samuel grew, and the Lord was with him, and let none of his words fall to the "
     "ground. The child who learned to listen in the dark became the voice God used to "
     "speak to a whole nation. It began with a boy saying, speak — I am listening.", None),
    ("card", NARRATOR, "-26%", "-4Hz",
     "God called a child by name, in the dark, and waited until he was ready to listen. "
     "He is patient like that still. If a voice were gently calling your name, could you "
     "say it too — speak, I am listening?", None),
]


async def main():
    for name, voice, rate, pitch, text, cap in SEGMENTS:
        tts = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")


if __name__ == "__main__":
    import os
    os.makedirs("audio", exist_ok=True)
    asyncio.run(main())
