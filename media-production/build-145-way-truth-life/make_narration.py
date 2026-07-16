#!/usr/bin/env python3
"""Generate narration audio for Story Video #145 — "I Am the Way, the Truth,
and the Life" (John 14:6). From DRAFTS/row-145.md, validated against the laws.
Narrator: modern, warm, low, unhurried (American). Plain US model only.
Jesus voice: AMERICAN, never British. Jesus speaks ONLY exact KJV:
John 14:6 (verified against the passage).
HOMOGRAPH LAW: ear-checked — no bow/wound/wind/tears/lead/sow/live/read/dove/
bass/minute/use(d)/close in any segment ("life" is the noun, safe).
No SPOKEN overrides needed.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0", NARRATOR, "-20%", "-4Hz",
     "In the upper room, the night before the cross, Jesus told "
     "His disciples He was going to prepare a place for them."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "Thomas spoke up — Lord, we don't know where You're going, so "
     "how can we know the way?"),
    # sacred-silence beat follows n1. Exact KJV John 14:6.
    ("j1", JESUS, "-22%", "-2Hz",
     "I am the way, the truth, and the life: no man cometh unto "
     "the Father, but by me."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "Not one way among many. The way itself. The truth itself. "
     "The life itself — standing right there in the room with "
     "them."),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "The door to the Father isn't a map to find. It's a person to "
     "follow."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "Stop looking for the road. Walk with Him."),
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
