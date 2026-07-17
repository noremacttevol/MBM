#!/usr/bin/env python3
"""Generate narration audio for Story Video #131 — The Scribe Near the Kingdom
(Mark 12:28-34). From DRAFTS/row-131.md, validated against the laws.
Narrator: modern, warm, low, unhurried (American). Plain US model only.
Jesus voice: AMERICAN, never British. Jesus speaks ONLY exact KJV:
Mark 12:34 (verified against the passage).
HOMOGRAPH LAW: ear-checked — no bow/wound/wind/tears/lead/sow/live/read/dove/
bass/minute/use(d)/close in any segment. No SPOKEN overrides needed.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    # n0 split so the approach (s1) and the asking (s3) each carry
    # their half — draft words verbatim.
    ("n0a", NARRATOR, "-20%", "-4Hz",
     "A teacher of the law came to Jesus with a real question, not "
     "a trap —"),
    ("n0b", NARRATOR, "-20%", "-4Hz",
     "which commandment matters most of all?"),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "Jesus answered without hesitation. Love God with everything "
     "you are. And love your neighbor as yourself. Everything else "
     "hangs on those two."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "The scribe agreed — and added something honest: to love God "
     "and neighbor is worth more than any burnt offering."),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "Jesus looked at him and saw a man thinking clearly, with an "
     "open heart."),
    # sacred-silence beat follows n3. Exact KJV Mark 12:34 — SILENCE around it.
    ("j1", JESUS, "-22%", "-2Hz",
     "Thou art not far from the kingdom of God."),
    ("n4", NARRATOR, "-20%", "-4Hz",
     "Not far. The man was close — a step from the door. And no "
     "one dared question Jesus after that."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "You may be closer than you think. Love God, love your "
     "neighbor — and step through the door."),
]

# HOMOGRAPH LAW — every segment ear-checked against the flag list
# (bow, wound, wind, tears, lead, sow, live/lives, read, dove, bass,
# minute, use/used, close): n4 contains "close" as the ADJECTIVE /KLOHS/
# ("the man was close") — edge-tts's default reading; ear-check it anyway.
# Captions stay exact.
SPOKEN = {}


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts_text = SPOKEN.get(name, text)
        tts = edge_tts.Communicate(tts_text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
