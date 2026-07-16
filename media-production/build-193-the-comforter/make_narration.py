#!/usr/bin/env python3
"""Generate narration audio for MEMBER Verse Video #193 — "The Comforter...
Shall Teach You All Things" (John 14:26). From DRAFTS/row-193.md, validated
against the laws.
Narrator: modern, warm, low, unhurried (American). Plain US model only.
Jesus voice: AMERICAN, never British. Jesus speaks ONLY exact KJV:
John 14:26 (verified against the passage) — the centerpiece.
Closing card carries the Gospel Library pointer:
"Learn more — Gospel Library: Holy Ghost" (THE-200 → GL).
CONTENT-CARE: comfort; the Holy Ghost shown only as gentle light, never a
face or figure.
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
     "On the night before He died, Jesus sat with His disciples "
     "and told them they would not be left alone."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "He promised another Helper would come — the Holy Ghost, sent "
     "by the Father in His name."),
    # sacred-silence beat follows n1.
    ("n2", NARRATOR, "-20%", "-4Hz",
     "This Helper would do two things: teach them everything, and "
     "bring every word Jesus had spoken back to their minds."),
    # Exact KJV John 14:26 — THE CENTERPIECE, SILENCE around it.
    ("j1", JESUS, "-22%", "-2Hz",
     "But the Comforter, which is the Holy Ghost, whom the Father "
     "will send in my name, he shall teach you all things, and "
     "bring all things to your remembrance, whatsoever I have said "
     "unto you."),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "The promise still stands — the Spirit who taught them then "
     "teaches everyone who listens now."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "You are not left to remember alone. The Comforter is here — "
     "let Him teach you."),
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
