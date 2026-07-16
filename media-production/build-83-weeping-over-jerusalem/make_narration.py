#!/usr/bin/env python3
"""Generate narration audio for Story Video #83 — Weeping Over Jerusalem
(Luke 19:41-44). Narrator: modern, warm, low, unhurried (American). Plain US only.
Jesus voice: AMERICAN, never British. Jesus speaks ONLY exact KJV:
Luke 19:42 (fetched, not hand-typed). vv43-44 are narrator-paraphrased in ONE
restrained line — no fear-mongering; his weeping IS the mercy, and the narrator says
his tears were love (mercy-in-judgment law).
HOMOGRAPH LAW: "tears" in n3 gets a SPOKEN respelling ("teers"); caption stays
exact. Ear-check "wept" too. No music bed: narration + intentional silence only.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0", NARRATOR, "-20%", "-4Hz",
     "As Jesus came over the hill and the whole city of Jerusalem "
     "opened up in front of him, he did something the crowds didn't "
     "expect."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "He stopped, and he wept over it — not for himself. For them."),
    # Exact KJV Luke 19:42 — SILENCE around it.
    ("j1", JESUS, "-20%", "-2Hz",
     "If thou hadst known, even thou, at least in this thy day, the "
     "things which belong unto thy peace! but now they are hid from "
     "thine eyes."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "The peace they had been aching for had walked right up to their "
     "gates — and the city was too busy to see it."),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "He could see what was coming for the city he loved — armies and "
     "ruin, a generation away. His tears weren't anger. They were the "
     "grief of love that sees exactly what could have been."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "He wept because he loved the city that couldn't see him. He sees "
     "you clearly. Don't look away."),
]

# HOMOGRAPH LAW — n3 contains "tears" (must say /teerz/, never /tairz/):
# SPOKEN respelling for audio only; the caption keeps the true word "tears".
SPOKEN = {
    "n3": ("He could see what was coming for the city he loved — armies and "
           "ruin, a generation away. His teers weren't anger. They were the "
           "grief of love that sees exactly what could have been."),
}


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts_text = SPOKEN.get(name, text)
        tts = edge_tts.Communicate(tts_text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
