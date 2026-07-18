#!/usr/bin/env python3
"""Narration audio for Video #122 — The Mote and the Beam (Matthew 7:1-5).

Narrator: en-US-AndrewNeural. Jesus's voice: en-US-ChristopherNeural (exact KJV only).
Jesus is never shown, but these are HIS words, so they are in the scripture voice and render
cream-italic; the narrator frames the illustration.

Jesus's KJV lines (Christopher, cream italic):
  jvA  Matt 7:1-2  "Judge not, that ye be not judged. For with what judgment ye judge, ye
                    shall be judged." — sacred silence 1
  jvB  Matt 7:5    "Thou hypocrite, first cast out the beam out of thine own eye; and then
                    shalt thou see clearly to cast out the mote out of thy brother's eye."
                    — sacred silence 2

CARE FLAGS: none (GREEN). The beam is a stylized metaphor, never gore.

WHY-LAW: Jesus is not banning discernment — he is ordering it. Deal with the plank in your own
eye BEFORE the speck in your brother's, and then you can help him gently instead of condemning
him. Milk framing: the measure you use is the measure you get, so choose mercy; honest
self-examination turns judgment into kindness. An invitation to humility, never a scolding.

HOMOGRAPH EAR-CHECK: 'mote' (speck) reads clearly, not 'moat'. NUMBER-STRESS LAW: no numbers.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"
JESUS = "en-US-ChristopherNeural"

SEGMENTS = [
    ("n1", NARRATOR, "-20%", "-4Hz",
     "Of all the things Jesus taught on that hillside, one of them cuts straight to how we "
     "treat each other — and it starts with a warning we would rather skip.", None),
    # jvA — Judge not, that ye be not judged — sacred silence 1
    ("jvA", JESUS, "-26%", "-6Hz",
     "Judge not, that ye be not judged. For with what judgment ye judge, ye shall be "
     "judged.", None),
    ("n2", NARRATOR, "-22%", "-4Hz",
     "We are experts at spotting the small faults in someone else. A tiny speck, a mote, in "
     "our brother's eye — and we cannot wait to point it out.", None),
    ("n3", NARRATOR, "-22%", "-4Hz",
     "But Jesus drew a picture so absurd it makes you laugh. A man fussing over a speck of "
     "sawdust in someone else's eye — while an entire wooden beam is sticking straight out "
     "of his own.", None),
    ("n4", NARRATOR, "-22%", "-4Hz",
     "He cannot even see straight. The beam is in the way of everything he does. And yet he "
     "is completely sure that he is the one who ought to be fixing other people.", None),
    ("n5", NARRATOR, "-22%", "-4Hz",
     "And then, if we are honest, the moment finally comes when we catch sight of the beam. "
     "Not his. Ours. The one we had been carrying the whole time.", None),
    # jvB — Thou hypocrite, first cast out the beam — sacred silence 2
    ("jvB", JESUS, "-26%", "-6Hz",
     "Thou hypocrite, first cast out the beam out of thine own eye; and then shalt thou see "
     "clearly to cast out the mote out of thy brother's eye.", None),
    ("n6", NARRATOR, "-22%", "-4Hz",
     "Notice he does not say ignore your brother's speck. He says deal with your own beam "
     "first — and then you will actually be able to help him, gently, instead of just "
     "condemning him.", None),
    ("n7", NARRATOR, "-22%", "-4Hz",
     "The goal was never to stop caring about each other. It was to come to each other "
     "humble instead of superior — as one flawed person helping another, not a judge passing "
     "a sentence.", None),
    ("n8", NARRATOR, "-24%", "-4Hz",
     "The measure you use is the measure you will get back. So Jesus offers a better one: "
     "mercy. Deal honestly with yourself, and you will be amazed how much patience you "
     "suddenly have for everyone else.", None),
    ("card", NARRATOR, "-26%", "-4Hz",
     "Jesus was not telling us to stop seeing clearly — he was telling us where to start: "
     "with the beam in our own eye. Deal with that, and our eyes for other people fill with "
     "mercy instead of judgment. Whose speck have you been watching, while a beam waited in "
     "your own eye?", None),
]


async def main():
    for name, voice, rate, pitch, text, cap in SEGMENTS:
        await save_narration(text, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")


if __name__ == "__main__":
    import os
    os.makedirs("audio", exist_ok=True)
    asyncio.run(main())
