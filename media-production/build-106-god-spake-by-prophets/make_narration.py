#!/usr/bin/env python3
"""Narration audio for Video #106 — God Spake by the Prophets (Hebrews 1:1-3).

Narrator: en-US-AndrewNeural. The Son's/Scripture voice: en-US-ChristopherNeural for the
exact KJV of Hebrews 1 (this is the apostolic word about the Son; the scripture voice
carries it in cream italic).

KJV lines (Christopher, cream italic):
  jv1  Heb 1:1-2a  "God, who at sundry times and in divers manners spake in time past
                    unto the fathers by the prophets," — silence 1
  jv2  Heb 1:2b    "Hath in these last days spoken unto us by his Son..." — silence 2
  jv3  Heb 1:3a    "Who being the brightness of his glory, and the express image of his
                    person, and upholding all things by the word of his power..."

WHY-LAW: for ages God spoke in fragments — a burning bush here, a fire on a mountain
there, a scroll, a voice at a city gate — many messengers, many ways, never the whole
picture. Then he said everything at once, in a single, complete, human Word: his Son.
If you want to know what God is finally like, you no longer squint at fragments — you
look at Jesus. Milk framing: God has been trying to reach you the whole time, and his
clearest word is a warm human face. An invitation, never a threat.

HOMOGRAPH EAR-CHECK: 'divers' read as DYE-verz (correct). No other high-risk homographs.
NUMBER-STRESS LAW obeyed.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"
SCRIPTURE = "en-US-ChristopherNeural"

SEGMENTS = [
    ("n1", NARRATOR, "-20%", "-4Hz",
     "For thousands of years, God had been speaking. Never all at once. Never the whole "
     "picture. But always, patiently, reaching toward people who could barely hear him.", None),
    # jv1 — sundry times, divers manners — silence 1
    ("jv1", SCRIPTURE, "-24%", "-6Hz",
     "God, who at sundry times and in divers manners spake in time past unto the fathers "
     "by the prophets,", None),
    ("n2", NARRATOR, "-22%", "-4Hz",
     "In many times, and in many different ways. To one he spoke from a bush that burned "
     "but would not burn up. To another, in fire that fell on a mountain.", None),
    ("n3", NARRATOR, "-22%", "-4Hz",
     "To one he gave words to write on a scroll in the lamplight. Another he sent to cry "
     "out in the city gate to people who mostly would not listen. A fragment here, a "
     "flash there — true, but partial.", None),
    ("n4", NARRATOR, "-22%", "-4Hz",
     "Century after century, messenger after messenger, each one carrying a piece of it. "
     "Never quite the whole. Never a face you could look full into and say, so that is "
     "what God is like.", None),
    ("n5", NARRATOR, "-22%", "-4Hz",
     "And then, after all the fragments, God did something he had never done. He stopped "
     "sending messages about himself — and came in person.", None),
    # jv2 — by his Son — silence 2
    ("jv2", SCRIPTURE, "-26%", "-6Hz",
     "Hath in these last days spoken unto us by his Son.", None),
    ("n6", NARRATOR, "-22%", "-4Hz",
     "Not another prophet with another piece. The Son. God's own last and clearest word, "
     "spoken not in fire on a mountain, but in a real human life you could walk beside.", None),
    # jv3 — express image
    ("jv3", SCRIPTURE, "-24%", "-6Hz",
     "Who being the brightness of his glory, and the express image of his person, and "
     "upholding all things by the word of his power.", None),
    ("n7", NARRATOR, "-22%", "-4Hz",
     "The exact likeness of God, in a face you could actually look at. If you have ever "
     "wondered what God is really like — whether he is angry, or distant, or cold — the "
     "answer is not a guess. Look at Jesus. That is God, saying everything, at last.", None),
    ("card", NARRATOR, "-26%", "-4Hz",
     "For ages God spoke in fragments; then he said it all in a Son. His clearest word "
     "about himself is a warm human face inviting you in. If you want to know what God is "
     "really like, where might you start looking?", None),
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
