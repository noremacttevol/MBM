#!/usr/bin/env python3
"""Generate narration audio for MEMBER Verse Video #173 — "The Dead Shall Hear
the Voice of the Son of God" (John 5:25). From DRAFTS/row-173.md, validated
against the laws.
Narrator: modern, warm, low, unhurried (American). Plain US model only.
Jesus voice: AMERICAN, never British. Jesus speaks ONLY exact KJV:
John 5:25 (verified against the passage) — the verse IS the centerpiece.
Closing card carries the Gospel Library pointer:
"Learn more — Gospel Library: Redemption of the Dead" (THE-200 → GL).
HOMOGRAPH LAW: "live" (the #1 TTS offender, verb) appears in BOTH the KJV
line ("they that hear shall live") and the card ("listen — and live"). SPOKEN
respelling "liv" applied to both; captions keep the true spelling. Ear-check
both before assembly anyway. No other flagged words.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0", NARRATOR, "-20%", "-4Hz",
     "Jesus said a time was coming — and had already begun — when "
     "something impossible would happen."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "The dead would hear a voice. Not a rumor of a voice. His "
     "voice."),
    # sacred-silence beat follows n1. Exact KJV John 5:25 — THE CENTERPIECE.
    ("j1", JESUS, "-24%", "-2Hz",
     "Verily, verily, I say unto you, The hour is coming, and now "
     "is, when the dead shall hear the voice of the Son of God: "
     "and they that hear shall live."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "The One who made life is the One who calls it back. To hear "
     "him is to live."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "He speaks, and death loses its grip. Lean in and listen — "
     "and live."),
]

# HOMOGRAPH LAW — "live" must read /LIV/ in j1, n2 and the card. SPOKEN
# respellings steer the audio; captions keep the true spelling. Ear-check.
SPOKEN = {
    "j1": ("Verily, verily, I say unto you, The hour is coming, and now "
           "is, when the dead shall hear the voice of the Son of God: "
           "and they that hear shall liv."),
    "n2": ("The One who made life is the One who calls it back. To hear "
           "him is to liv."),
    "card": ("He speaks, and death loses its grip. Lean in and listen — "
             "and liv."),
}


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts_text = SPOKEN.get(name, text)
        tts = edge_tts.Communicate(tts_text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
