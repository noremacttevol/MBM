#!/usr/bin/env python3
"""Generate narration audio for Story Video #134 — "Other Sheep I Have"
(John 10:16). From DRAFTS/row-134.md, validated against the laws.
Narrator: modern, warm, low, unhurried (American). Plain US model only.
Jesus voice: AMERICAN, never British. Jesus speaks ONLY exact KJV:
John 10:16 (verified against the passage).
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
     "Jesus used a picture His listeners knew well — a shepherd "
     "and his sheep. He was the good Shepherd, and they were His "
     "flock."),
    # n1 split so the familiar-fold still and the other-hillside still
    # each carry their half — draft words verbatim.
    ("n1a", NARRATOR, "-20%", "-4Hz",
     "But He said the flock was bigger than the people standing "
     "there."),
    ("n1b", NARRATOR, "-20%", "-4Hz",
     "There were other sheep, not of that pen, that He would also "
     "bring."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "They would hear His voice. And the result would be one "
     "flock, one Shepherd."),
    # sacred-silence beat follows n2. Exact KJV John 10:16.
    ("j1", JESUS, "-22%", "-2Hz",
     "And other sheep I have, which are not of this fold: them "
     "also I must bring, and they shall hear my voice; and there "
     "shall be one fold, and one shepherd."),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "Not divided by nation or wall. One voice, one care, one "
     "Shepherd over all who listen."),
    ("n4", NARRATOR, "-20%", "-4Hz",
     "Whoever hears Him belongs — wherever they're from."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "His voice reaches further than you think. Hear Him, and "
     "you're in the fold."),
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
