#!/usr/bin/env python3
"""Generate narration audio for MEMBER Verse Video #187 — "Ye Are Gods;
Children of the Most High" (Psalm 82:6, quoted by Jesus in John 10:34).
From DRAFTS/row-187.md, validated against the laws.
Narrator: modern, warm, low, unhurried (American). Plain US model only.
Jesus voice: AMERICAN, never British. Jesus speaks ONLY exact KJV: the full
Psalm 82:6 he stands on in John 10:34 — "I have said, Ye are gods; and all of
you are children of the most High." (word-exact against the psalm).
Closing card carries the Gospel Library pointer:
"Learn more — Gospel Library: Divine Potential" (THE-200 → GL).
CONTENT-CARE: confrontation without violence; accusers composed, never
grotesque.
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
     "The religious leaders were circling Jesus, demanding he say "
     "plainly who he claimed to be."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "Instead of backing down, he reached into their own "
     "scriptures — to a psalm where God calls mere men gods."),
    # Exact KJV Psalm 82:6 (the verse Jesus quotes, John 10:34) — CENTERPIECE.
    ("j1", JESUS, "-22%", "-2Hz",
     "I have said, Ye are gods; and all of you are children of the "
     "most High."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "His point was sharp: if scripture called men gods because "
     "God's word came to them, how could they condemn the one the "
     "Father set apart?"),
    # sacred-silence beat follows n2.
    ("n3", NARRATOR, "-20%", "-4Hz",
     "He was not making himself a second God. He was showing them "
     "their own book exposed their logic."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "He stood on the scriptures they claimed to love. Come know "
     "him as he truly is."),
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
