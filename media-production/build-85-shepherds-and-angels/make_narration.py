#!/usr/bin/env python3
"""Generate narration audio for Story Video #85 — Shepherds and Angels
(Luke 2:8-20). Written by ASSEMBLY-B from PROMPTS.md (no draft existed).
GREEN story. No adult Christ; the babe is the newborn only.
Narrator: modern, warm, low, unhurried (American). Plain US model only.
The ANGEL / heavenly-host KJV words are read by the SCRIPTURE VOICE
(Christopher) — the Jesus voice is reserved for Jesus's own words, and Jesus
does not speak here; the scripture voice carries the angelic KJV (build-161
precedent). KJV verified: Luke 2:10-11 (j1), Luke 2:14 (j2).
HOMOGRAPH LAW: ear-checked — no bow/wound/wind/tears/lead/sow/live/read/dove/
bass/minute/use(d)/close in any segment. No SPOKEN overrides needed.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"       # plain American — never a Multilingual model
SCRIPTURE = "en-US-ChristopherNeural"  # the scripture voice. Exact KJV only.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0", NARRATOR, "-20%", "-4Hz",
     "Outside Bethlehem, shepherds were keeping watch over their "
     "flocks by night — ordinary men working the late shift, about "
     "the lowest job there was."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "Suddenly an angel of the Lord stood before them, and the glory "
     "of the Lord blazed all around. They were terrified."),
    # Exact KJV Luke 2:10-11 — scripture voice, SILENCE around it.
    ("j1", SCRIPTURE, "-22%", "-2Hz",
     "Fear not: for, behold, I bring you good tidings of great joy, "
     "which shall be to all people. For unto you is born this day in "
     "the city of David a Saviour, which is Christ the Lord."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "And in a moment the one angel became a vast multitude of the "
     "heavenly host, filling the whole sky."),
    # Exact KJV Luke 2:14 — scripture voice.
    ("j2", SCRIPTURE, "-22%", "-2Hz",
     "Glory to God in the highest, and on earth peace, good will "
     "toward men."),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "When the angels had gone, the shepherds said to each other, "
     "let us go and see this thing. And they came with haste into "
     "the town."),
    # sacred-silence beat follows n3 (the stable threshold).
    ("n4", NARRATOR, "-20%", "-4Hz",
     "They found Mary and Joseph, and the baby lying in the manger — "
     "exactly as they had been told."),
    ("n5", NARRATOR, "-20%", "-4Hz",
     "There he was: the Saviour of the world, a tiny newborn asleep "
     "in a feed trough, wrapped in strips of cloth."),
    ("n6", NARRATOR, "-20%", "-4Hz",
     "The shepherds could not keep it in. They went out glorifying "
     "and praising God, telling everyone they met what they had seen "
     "and heard."),
    ("n7", NARRATOR, "-20%", "-4Hz",
     "But Mary kept all these things, and pondered them in her "
     "heart."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "The first birth announcement in history went to night-shift "
     "workers on a hillside. Good news of great joy, for all people. "
     "Including you."),
]

# HOMOGRAPH LAW — every segment ear-checked against the flag list; none
# present. Captions stay exact.
SPOKEN = {}


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts_text = SPOKEN.get(name, text)
        tts = edge_tts.Communicate(tts_text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
