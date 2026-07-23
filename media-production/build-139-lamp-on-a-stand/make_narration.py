#!/usr/bin/env python3
"""Generate narration audio for Story Video #139 — The Lamp on a Stand
(Matthew 5:14-16). From DRAFTS/row-139.md, validated against the laws.
Narrator: modern, warm, low, unhurried (American). Plain US model only.
Jesus voice: AMERICAN, never British. Jesus speaks ONLY exact KJV:
Matthew 5:14, 5:15, 5:16 (all three verified against the passage).
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
     "Jesus was teaching a crowd on a mountainside. He told them "
     "who they were before He told them what to do."),
    # Exact KJV Matt 5:14.
    ("j1", JESUS, "-20%", "-2Hz",
     "Ye are the light of the world. A city that is set on an hill "
     "cannot be hid."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "Nobody lights a lamp and then hides it under a bowl. You put "
     "it up where it can light the whole room."),
    # Exact KJV Matt 5:15.
    ("j2", JESUS, "-20%", "-2Hz",
     "Neither do men light a candle, and put it under a bushel, "
     "but on a candlestick; and it giveth light unto all that are "
     "in the house."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "Not to be noticed — he was never after applause. The point was "
     "that people would see something good in a life and be drawn to the "
     "God behind it."),
    # sacred-silence beat follows n2. Exact KJV Matt 5:16.
    ("j3", JESUS, "-22%", "-2Hz",
     "Let your light so shine before men, that they may see your "
     "good works, and glorify your Father which is in heaven."),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "You were lit on purpose. You were put on the stand on "
     "purpose."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "You were made to be seen for good. Let it shine."),
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
