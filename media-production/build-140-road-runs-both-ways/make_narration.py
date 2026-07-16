#!/usr/bin/env python3
"""Generate narration audio for Story Video #140 — The Road to the Far Country
Runs Both Ways (Luke 15:11-32). From DRAFTS/row-140.md, validated against
the laws.
Narrator: modern, warm, low, unhurried (American). Plain US model only.
Jesus voice: AMERICAN, never British. Jesus speaks ONLY exact KJV:
Luke 15:11 (he tells the parable — his voice is heard, he is never depicted).
CONTENT-CARE: gentle — pigs at dignified distance, no shame framing; the
father's run IS the mercy beat, spoken aloud.
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
     "Jesus told a story about a father and two sons. The younger "
     "one wanted his share of the inheritance now — and he got "
     "it."),
    # Exact KJV Luke 15:11 — the teller's voice; he is never depicted.
    ("j1", JESUS, "-22%", "-2Hz",
     "And he said, A certain man had two sons:"),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "He left home and went to a country far away. There he spent "
     "everything on a life that looked free and felt empty."),
    # sacred-silence beat follows n1.
    ("n2", NARRATOR, "-20%", "-4Hz",
     "A hard season came. He was hungry, alone, and tending pigs — "
     "and he came to himself."),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "He decided to go back. Not as a son claiming rights, but as "
     "a servant asking for a place."),
    ("n4", NARRATOR, "-20%", "-4Hz",
     "But while he was still far off, his father saw him and ran. "
     "No lecture. No waiting for the apology. He threw his arms "
     "around him."),
    ("n5", NARRATOR, "-20%", "-4Hz",
     "The father gave him the robe, the ring, the sandals — "
     "belonging, not probation. And there was a feast, because "
     "what was lost had come home."),
    ("n6", NARRATOR, "-20%", "-4Hz",
     "But the older brother stood outside, angry that grace looked "
     "so easy. The door ran both ways — it was open for him too."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "The road home is always open. However far you've gone, turn "
     "around — He's already running to meet you."),
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
