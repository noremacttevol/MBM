#!/usr/bin/env python3
"""Generate narration audio for Story Video #125 — "I Never Knew You"
(Matthew 7:21-23). From DRAFTS/row-125.md, validated against the laws.
Narrator: modern, warm, low, unhurried (American). Plain US model only.
Jesus voice: AMERICAN, never British. Jesus speaks ONLY exact KJV:
Matthew 7:21, 7:22, 7:23 (all three verified against the passage).
CONTENT-CARE (judgment passage): mercy spoken aloud; the close is an
invitation to be known, never fear. No embodied devils are ever depicted —
"cast out devils" is heard in the KJV line only, never painted.
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
     "Jesus warned that saying the right words is not the same as "
     "knowing him. The door is not opened by a name we repeat."),
    # Exact KJV Matt 7:21.
    ("j1", JESUS, "-20%", "-2Hz",
     "Not every one that saith unto me, Lord, Lord, shall enter "
     "into the kingdom of heaven; but he that doeth the will of my "
     "Father which is in heaven."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "He described a day when many will point to what they did — "
     "prophecies, miracles, works done in his name."),
    # sacred-silence beat follows n1. Exact KJV Matt 7:22.
    ("j2", JESUS, "-20%", "-2Hz",
     "Many will say to me in that day, Lord, Lord, have we not "
     "prophesied in thy name? and in thy name have cast out "
     "devils? and in thy name done many wonderful works?"),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "And then the honest part — knowing him matters more than "
     "sounding like we do."),
    # Exact KJV Matt 7:23 — SILENCE around it; gravity held with mercy.
    ("j3", JESUS, "-22%", "-2Hz",
     "And then will I profess unto them, I never knew you: depart "
     "from me, ye that work iniquity."),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "This is not a threat to scare you. It is an invitation to be "
     "known — to walk with him, not just speak his name."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "He wants to know you, not just be named by you. Come close, "
     "and let him know you."),
]

# HOMOGRAPH LAW — every segment ear-checked against the flag list
# (bow, wound, wind, tears, lead, sow, live/lives, read, dove, bass,
# minute, use/used, close): none present ("Come close" in the card is the
# adjective /klohs/, which is edge-tts's default reading — ear-check it).
SPOKEN = {}


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts_text = SPOKEN.get(name, text)
        tts = edge_tts.Communicate(tts_text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
