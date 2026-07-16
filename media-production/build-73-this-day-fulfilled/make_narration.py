#!/usr/bin/env python3
"""Generate narration audio for Story Video #73 — This Day Fulfilled (Luke 4:16-21).
Narrator: modern, warm, low, unhurried (American). Plain US model only.
Jesus voice: AMERICAN, never British. Jesus speaks ONLY exact KJV:
Luke 4:18-19 (the Isaiah reading) and the words of Luke 4:21 (fetched, not hand-typed).
CONTENT-CARE: GREEN — this build ends at v21 (the fulfillment); the cliff/rejection
at Nazareth is row 105's story and is NOT told here.
HOMOGRAPH LAW: "read" (past tense) in n1 gets a SPOKEN respelling ("red");
the caption stays exact. Card's "reads" is present tense (/reedz/) — ear-check it
anyway before assembly. No music bed (HUM PURGE): narration + silence only.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0", NARRATOR, "-20%", "-4Hz",
     "He came back to Nazareth — the town that raised him — and on the "
     "Sabbath he walked into the synagogue like he always had."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "They handed him the scroll of Isaiah. He found the place, and read "
     "it out loud."),
    # Exact KJV Luke 4:18-19 — sacred pause around it.
    ("j1", JESUS, "-20%", "-2Hz",
     "The Spirit of the Lord is upon me, because he hath anointed me to "
     "preach the gospel to the poor; he hath sent me to heal the "
     "brokenhearted, to preach deliverance to the captives, and "
     "recovering of sight to the blind, to set at liberty them that are "
     "bruised, to preach the acceptable year of the Lord."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "Then he rolled the scroll up, handed it back, and sat down. Every "
     "eye in the room was fixed on him — this was the boy who grew up on "
     "their street. And the room held its breath."),
    # Exact KJV Luke 4:21 (his words) — SILENCE around it.
    ("j2", JESUS, "-18%", "-2Hz",
     "This day is this scripture fulfilled in your ears."),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "The promise Israel had waited on for centuries — the healing, the "
     "freedom, the good news for the poor — he said it was standing "
     "right in front of them. Not someday. Today."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "He still reads it as today. What would it mean if that promise "
     "were meant for you, right now?"),
]

# HOMOGRAPH LAW — n1 contains "read" (past tense, must say /red/): SPOKEN
# respelling for audio only; the caption keeps the true word "read".
SPOKEN = {
    "n1": ("They handed him the scroll of Isaiah. He found the place, and "
           "red it out loud."),
}


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts_text = SPOKEN.get(name, text)
        tts = edge_tts.Communicate(tts_text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
