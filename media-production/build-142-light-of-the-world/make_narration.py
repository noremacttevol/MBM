#!/usr/bin/env python3
"""Generate narration audio for Story Video #142 — "I Am the Light of the World"
(John 8:12; 9:5). From DRAFTS/row-142.md, validated against the laws.
Narrator: modern, warm, low, unhurried (American). Plain US model only.
Jesus voice: AMERICAN, never British. Jesus speaks ONLY exact KJV:
John 8:12 and John 9:5 (both verified against the passage).
TRANSLATION-LAW FIX: the draft's n2 echoed John 9:5 nearly verbatim in the
narrator's mouth ("while I am in the world, I am the light of the world") —
the echo is removed; only the Jesus voice carries the verse.
HOMOGRAPH LAW: ear-checked — no bow/wound/wind/tears/lead/sow/live/read/dove/
bass/minute/use(d)/close in any segment. No SPOKEN overrides needed.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0", NARRATOR, "-20%", "-4Hz",
     "Jesus stood among the temple courts and spoke into the noise "
     "of the crowd."),
    # Exact KJV John 8:12.
    ("j1", JESUS, "-20%", "-2Hz",
     "I am the light of the world: he that followeth me shall not "
     "walk in darkness, but shall have the light of life."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "Not a lamp that burns out. A light that walks with you, so "
     "you're never feeling your way blind."),
    # sacred-silence beat follows n1.
    ("n2", NARRATOR, "-20%", "-4Hz",
     "Later, as He met a man born blind, He said it again."),
    # Exact KJV John 9:5.
    ("j2", JESUS, "-22%", "-2Hz",
     "As long as I am in the world, I am the light of the world."),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "He didn't just describe light. He opened blind eyes and "
     "proved it."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "Stop groping in the dark. Walk with the Light."),
]

# HOMOGRAPH LAW — every segment ear-checked against the flag list
# (bow, wound, wind, tears, lead, sow, live/lives, read, dove, bass,
# minute, use/used, close): none present. Captions stay exact.
SPOKEN = {}


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts_text = SPOKEN.get(name, text)
        await save_narration(tts_text, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
