#!/usr/bin/env python3
"""Generate narration audio for MEMBER Verse Video #189 — "To Him That
Overcometh" (Revelation 3:20-21). From DRAFTS/row-189.md, validated against
the laws.
Narrator: modern, warm, low, unhurried (American). Plain US model only.
Jesus voice: AMERICAN, never British. Jesus speaks ONLY exact KJV:
Revelation 3:20 and 3:21 (both verified against the passage) — the 3:21
promise is the centerpiece.
Closing card carries the Gospel Library pointer:
"Learn more — Gospel Library: Exaltation" (THE-200 → GL).
CONTENT-CARE: hope without gloom; the knock is gentle, never ominous.
HOMOGRAPH LAW: ear-checked — no bow/wound/wind/tears/lead/sow/live/read/dove/
bass/minute/use(d)/close in any segment (card included). No SPOKEN overrides
needed.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0", NARRATOR, "-20%", "-4Hz",
     "To a church that had grown comfortable and half-asleep, "
     "Jesus sent a knock at the door — not a storm, just a knock."),
    # Exact KJV Rev 3:20.
    ("j1", JESUS, "-22%", "-2Hz",
     "Behold, I stand at the door, and knock: if any man hear my "
     "voice, and open the door, I will come in to him, and will "
     "sup with him, and he with me."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "He does not break the door. He waits to be invited in."),
    # sacred-silence beat follows n1.
    ("n2", NARRATOR, "-20%", "-4Hz",
     "And to the one who opens, who keeps opening, he promises a "
     "seat no empire can give."),
    # Exact KJV Rev 3:21 — THE CENTERPIECE, SILENCE around it.
    ("j2", JESUS, "-22%", "-2Hz",
     "To him that overcometh will I grant to sit with me in my "
     "throne, even as I also overcame, and am set down with my "
     "Father in his throne."),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "The one who overcomes doesn't earn a throne by being "
     "flawless. He shares the one Christ already won."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "He is knocking right now. Open, and you will eat with him — "
     "and reign with him."),
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
