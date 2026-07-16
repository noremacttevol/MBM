#!/usr/bin/env python3
"""Generate narration audio for Story Video #136 — The Blind Man Healed in Two
Touches (Mark 8:22-26). From DRAFTS/row-136.md, validated against the laws.
Narrator: modern, warm, low, unhurried (American). Plain US model only.
Jesus voice: AMERICAN, never British. Jesus speaks ONLY exact KJV:
Mark 8:26 (his spoken words, verified against the passage).
CONTENT-CARE: healing shown gently, never the body in focus; the man's eyes
are never graphic.
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
     "Friends brought a blind man to Jesus in Bethsaida and begged "
     "Him just to touch him."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "Jesus took the man by the hand and walked him outside the "
     "village. He spit on the man's eyes and laid His hands on "
     "him, then asked if he could see anything yet."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "The man looked up and said the strangest thing — he could "
     "see, but only halfway. People looked like trees walking "
     "around."),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "So Jesus put His hands on the man's eyes a second time and "
     "told him to look up again."),
    # sacred-silence beat around the second touch. Exact KJV Mark 8:26.
    ("j1", JESUS, "-22%", "-2Hz",
     "Neither go into the town, nor tell it to any in the town."),
    ("n4", NARRATOR, "-20%", "-4Hz",
     "And this time he saw everything clearly — every face, every "
     "leaf. The second touch finished what the first had started."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "Maybe your faith came in stages too. He is patient enough to "
     "touch you twice."),
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
