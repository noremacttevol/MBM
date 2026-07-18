#!/usr/bin/env python3
"""Generate narration audio for Story Video #66 — "Malchus's Ear" (Luke 22:47-51).
Narrator: modern, warm, low, unhurried (American). Plain US model only.
Jesus voice: AMERICAN, never British. Jesus speaks ONLY exact KJV: Luke 22:51a.
CONTENT-CARE: DEEP — the arrest night, but the story is the HEALING of an enemy;
violence is never described in gory terms, only that a sword was drawn and a man hurt,
then healed.
HOMOGRAPH LAW: no offenders. "wound" is NOT used (avoided to dodge the homograph and
to keep CARE gentle). SPOKEN empty; ear-check every segment anyway.
No music bed: narration + intentional silence only.
Authored 2026-07-17 by W1-STILLS (no Hermes draft existed for this row).
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0", NARRATOR, "-20%", "-4Hz",
     "It was night in the garden. A crowd came up the path with torches "
     "and lanterns to arrest Jesus."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "One of his friends panicked, drew a sword, and struck the high "
     "priest's servant, cutting off his ear."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "Jesus stopped everything. Even here, even now, he would not answer "
     "violence with violence."),
    # Exact KJV Luke 22:51a — Jesus, SILENCE around it.
    ("j1", JESUS, "-18%", "-2Hz",
     "Suffer ye thus far."),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "And he reached out and touched the man's ear, and healed him — the "
     "enemy who had come to seize him, made whole by his hand."),
    ("n4", NARRATOR, "-20%", "-4Hz",
     "It was one of the last free things he did before they led him "
     "away: a miracle of mercy for someone who never asked for it."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "Even as they came to take him, he healed the man sent to seize "
     "him. That's the mercy held out to you."),
]

# HOMOGRAPH LAW — no offenders; SPOKEN stays empty. Ear-check every segment anyway.
SPOKEN = {}


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts_text = SPOKEN.get(name, text)
        tts = edge_tts.Communicate(tts_text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")


if __name__ == "__main__":
    asyncio.run(main())
