#!/usr/bin/env python3
"""Generate narration audio for MEMBER Verse Video #200 — "This Gospel of the
Kingdom Shall Be Preached in All the World" (Matthew 24:14). The catalog's
final row. From DRAFTS/row-200.md, validated against the laws.
Narrator: modern, warm, low, unhurried (American). Plain US model only.
Jesus voice: AMERICAN, never British. Jesus speaks ONLY exact KJV:
Matthew 24:14 (verified against the passage) — the centerpiece.
Closing card carries the Gospel Library pointer:
"Learn more — Gospel Library: Second Coming" (THE-200 → GL).
CONTENT-CARE: calm teaching prophecy — forward-looking, no distress imagery.
HOMOGRAPH LAW: n3 contains "live it" — the #1 TTS offender, verb, must read
/LIV/. SPOKEN respelling applied (the draft's flag line missed it); the
caption keeps the true spelling. Ear-check n3 anyway. No other flagged words
in any segment (card checked).
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0", NARRATOR, "-20%", "-4Hz",
     "Jesus sat with his disciples on the Mount of Olives, telling "
     "them what the long road ahead would hold — wars, rumors, "
     "hardship, and patience under strain."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "Then he turned to the one thing that would outlast all of "
     "it: a message carried to every corner of the earth."),
    # sacred-silence beat follows n1.
    ("n2", NARRATOR, "-20%", "-4Hz",
     "Not a secret kept for a few. A witness given to all "
     "nations — the good news of the kingdom going out until the "
     "very end."),
    # Exact KJV Matthew 24:14 — THE CENTERPIECE, SILENCE around it.
    ("j1", JESUS, "-22%", "-2Hz",
     "And this gospel of the kingdom shall be preached in all the "
     "world for a witness unto all nations; and then shall the end "
     "come."),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "The task he gave is still the task we carry: tell it, show "
     "it, live it — until the promise is fulfilled."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "The good news was meant for the whole world — and for you. "
     "Come, hear it, and carry it on."),
]

# HOMOGRAPH LAW — every segment ear-checked against the flag list
# (bow, wound, wind, tears, lead, sow, live/lives, read, dove, bass,
# minute, use/used, close): n3 contains "live it" — the VERB, must read
# /LIV/; SPOKEN respelling applied below. Captions stay exact.
SPOKEN = {
    "n3": ("The task he gave is still the task we carry: tell it, show "
           "it, liv it — until the promise is fulfilled."),
}


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts_text = SPOKEN.get(name, text)
        tts = edge_tts.Communicate(tts_text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
