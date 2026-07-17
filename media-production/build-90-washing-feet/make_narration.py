#!/usr/bin/env python3
"""Generate narration audio for Story Video #90 — Washing the Disciples' Feet
(John 13:1-17). From DRAFTS/row-090.md, validated against the laws.
Narrator: modern, warm, low, unhurried (American). Plain US model only.
Jesus voice: AMERICAN, never British. Jesus speaks ONLY exact KJV:
John 13:8, 13:14 (verified against the passage, not hand-typed from memory).
HOMOGRAPH LAW: ear-checked — no bow/wound/wind/tears/lead/sow/live/read/dove/
bass/minute/use(d)/close in any segment. No SPOKEN overrides needed.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0", NARRATOR, "-20%", "-4Hz",
     "At that last supper, knowing he was about to leave the world, "
     "Jesus did something no master would ever do for his servants."),
    # n1 split: pouring the water (s2) then washing their feet (s3).
    ("n1a", NARRATOR, "-20%", "-4Hz",
     "He got up from the table, wrapped a towel around his waist, "
     "and poured water into a basin."),
    ("n1b", NARRATOR, "-20%", "-4Hz",
     "And he began to wash his disciples' feet — one by one."),
    # sacred-silence beat follows n1: the still holds on the washing.
    ("n2", NARRATOR, "-20%", "-4Hz",
     "When he came to Peter, Peter pulled back — Lord, you will "
     "never wash MY feet. Jesus answered him gently but firmly."),
    # Exact KJV John 13:8 — SILENCE around it.
    ("j1", JESUS, "-20%", "-2Hz",
     "If I wash thee not, thou hast no part with me."),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "When he had finished, he dried their feet with the towel at "
     "his waist, sat back down, and asked if they understood what "
     "he had just done."),
    # Exact KJV John 13:14.
    ("j2", JESUS, "-20%", "-2Hz",
     "If I then, your Lord and Master, have washed your feet; ye "
     "also ought to wash one another's feet."),
    ("n4", NARRATOR, "-20%", "-4Hz",
     "The greatest one in the room knelt at the dirtiest job in "
     "the house. That is the kind of king he is."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "He kneels to serve the ones he loves. Will you let him near "
     "enough to do it for you?"),
]

# HOMOGRAPH LAW — every segment ear-checked against the flag list
# (bow, wound, wind, tears, lead, sow, live/lives, read, dove, bass,
# minute, use/used, close): none present. Captions stay exact.
SPOKEN = {}


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts_text = SPOKEN.get(name, text)
        tts = edge_tts.Communicate(tts_text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
