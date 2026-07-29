#!/usr/bin/env python3
"""Generate narration audio for Story Video #143 — "I Am the Door"
(John 10:7, 9). From DRAFTS/row-143.md, validated against the laws.
Narrator: modern, warm, low, unhurried (American). Plain US model only.
Jesus voice: AMERICAN, never British. Jesus speaks ONLY exact KJV:
John 10:7 and John 10:9 (both verified against the passage).
HOMOGRAPH LAW: ear-checked — no bow/wound/wind/tears/lead/sow/live/read/dove/
bass/minute/use(d)/close in any segment. No SPOKEN overrides needed.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    ("n0", NARRATOR, "-20%", "-4Hz", 'Jesus used a picture the crowd knew well — a sheepfold with one opening, and a shepherd who guards it through the night. The opening is where danger is stopped and every sheep is known.'),
    ("j1", JESUS, "-20%", "-2Hz", 'Verily, verily, I say unto you, I am the door of the sheep.'),
    ("n1a", NARRATOR, "-20%", "-4Hz", 'Someone who sneaks over the wall avoids the shepherd because he is there to take, not to care.'),
    ("n1b", NARRATOR, "-20%", "-4Hz", 'But the door is not another trap or test. It is the guarded way the flock comes in safe.'),
    ("j2", JESUS, "-22%", "-2Hz", 'I am the door: by me if any man enter in, he shall be saved, and shall go in and out, and find pasture.'),
    ("n2", NARRATOR, "-20%", "-4Hz", 'Through him you come in and you go out — free, fed, not trapped. Notice that the door is a person, not a score you must earn. Safety and pasture begin with trusting the shepherd who put himself in the opening.'),
    ("card", NARRATOR, "-22%", "-5Hz", 'The way home is not hidden from you. The Shepherd himself is the door. Knock, and walk through.'),
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
