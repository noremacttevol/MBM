#!/usr/bin/env python3
"""Generate narration audio for Story Video #146 — The Vine and the Branches
(John 15:5). From DRAFTS/row-146.md, validated against the laws.
Narrator: modern, warm, low, unhurried (American). Plain US model only.
Jesus voice: AMERICAN, never British. Jesus speaks ONLY exact KJV:
John 15:5 (verified against the passage).
HOMOGRAPH LAW: ear-checked — no bow/wound/wind/tears/lead/sow/live/read/dove/
bass/minute/use(d)/close in any segment. No SPOKEN overrides needed.

SEGMENTATION (ASSEMBLY-C, 2026-07-17): the verse is delivered in two exact-KJV
pieces split at its first colon, back to back — the prompt sheet built s3
("i-am-the-vine") and s6 ("abide-in-me") for those pieces. n0 and n3 split at
natural breaks so all 8 stills carry a beat synced to what is being said
(CAPTION LAW). Words unchanged from the draft.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0a", NARRATOR, "-20%", "-4Hz",
     "Jesus used a picture His friends would know —"),
    ("n0b", NARRATOR, "-20%", "-4Hz",
     "a vine, and the branches that grow from it."),
    # Exact KJV John 15:5, first clause.
    ("j1a", JESUS, "-20%", "-2Hz",
     "I am the vine, ye are the branches:"),
    # Exact KJV John 15:5, rest of the verse.
    ("j1b", JESUS, "-20%", "-2Hz",
     "He that abideth in me, and I in him, the same bringeth forth "
     "much fruit: for without me ye can do nothing."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "A branch cut off from the vine doesn't dry up because it's "
     "weak. It dries up because it's disconnected."),
    # sacred-silence beat follows n1.
    ("n2", NARRATOR, "-20%", "-4Hz",
     "Stay joined to Him, and the life flows. Try to bear fruit on "
     "your own, and there's nothing there."),
    ("n3a", NARRATOR, "-20%", "-4Hz",
     "He wasn't asking for effort."),
    ("n3b", NARRATOR, "-20%", "-4Hz",
     "He was offering connection."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "Stay connected to the Vine. Let His life flow through you."),
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
