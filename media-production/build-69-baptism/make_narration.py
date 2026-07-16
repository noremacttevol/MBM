#!/usr/bin/env python3
"""Generate narration audio for Story Video #69 — The Baptism of Jesus (Matt 3:13-17).
Narrator: modern, warm, low, unhurried (American). Plain US model only.
Jesus voice: AMERICAN, never British. Jesus speaks ONLY exact KJV: Matt 3:15b.
The Father's words are NEVER voiced as a character: the scripture voice reads
the FULL verse Matt 3:17 with its narrative wrapper (build-169 precedent), so
Christopher reads scripture rather than playing the Father.
GREEN story. HOMOGRAPH LAW: "dove" (the bird) gets a SPOKEN respelling "duv"
so TTS never says /dohv/; captions stay exact.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.
SCRIPTURE = JESUS                   # the scripture-reading voice (build-169 pattern)

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0", NARRATOR, "-20%", "-4Hz",
     "Down at the Jordan river, John was baptizing. He was rough as "
     "the desert he came from — a coat of camel's hair, a leather "
     "belt, a voice like a trumpet — and the whole countryside was "
     "walking out to him to confess and start over in that muddy "
     "water. Every day, sinners lined the bank. And then one day, "
     "somebody joined the line who had nothing to confess."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "Jesus walked from Galilee — days on foot — specifically to be "
     "baptized by John. And John, the wild man who was afraid of "
     "nobody, took one look and refused. It should be the other way "
     "around, he said. I need what YOU have. You coming to ME makes "
     "no sense."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "And John was right — it did not make sense. Baptism was for "
     "washing sins away, and Jesus had none. So listen carefully to "
     "the reason Jesus gives, because it tells you why he did almost "
     "everything:"),
    # Exact KJV Matt 3:15b — SILENCE around it.
    ("j1", JESUS, "-20%", "-2Hz",
     "Suffer it to be so now: for thus it becometh us to fulfil all "
     "righteousness."),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "Let it happen, John — this is how we do everything right, "
     "together. He was not washing anything away. He was stepping "
     "into line with us. If baptism is the doorway God asks people "
     "to walk through, then Jesus would walk through it first — not "
     "because he needed it, but so that no one who followed him "
     "would ever be asked to do something he had not done himself. "
     "He never leads from behind."),
    ("n4", NARRATOR, "-20%", "-4Hz",
     "So John baptized him — lowered him under the water of the "
     "Jordan, and raised him up again. And as Jesus came straight up "
     "out of the water, the sky itself broke open."),
    ("n5", NARRATOR, "-20%", "-4Hz",
     "The Spirit of God came down through the opened heavens like a "
     "dove, gentle as falling light, and rested on him. And then a "
     "voice came out of heaven — not John's voice, not any voice on "
     "the riverbank. A Father's voice."),
    # Exact KJV Matt 3:17, full verse with wrapper — SACRED SILENCE.
    ("jv1", SCRIPTURE, "-26%", "-6Hz",
     "And lo a voice from heaven, saying, This is my beloved Son, in "
     "whom I am well pleased."),
    ("n6", NARRATOR, "-20%", "-4Hz",
     "Stand on that riverbank for a second. The Son is standing in "
     "the water. The Spirit is descending upon him. The Father is "
     "speaking from heaven. Three — each one distinct, each one "
     "present, all in one moment — and what the Father chose to say, "
     "before Jesus had preached one sermon or healed one person, was: "
     "this is my Son, and I love him, and I am pleased with him. "
     "Identity first. Approval before achievement."),
    ("n7", NARRATOR, "-20%", "-4Hz",
     "Jesus began everything from that sentence. Not working TOWARD "
     "being loved — working FROM it. And the doorway he walked "
     "through that day, he left standing open behind him."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "He walked through the door first, so you would never face one "
     "he hadn't. The way in is still open."),
]

# HOMOGRAPH LAW — "dove" respelled for TTS (/duv/); caption stays exact KJV-true text.
SPOKEN = {
    "n5": ("The Spirit of God came down through the opened heavens like a "
           "duv, gentle as falling light, and rested on him. And then a "
           "voice came out of heaven — not John's voice, not any voice on "
           "the riverbank. A Father's voice."),
}


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts_text = SPOKEN.get(name, text)
        tts = edge_tts.Communicate(tts_text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
