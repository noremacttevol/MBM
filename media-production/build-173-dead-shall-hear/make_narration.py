#!/usr/bin/env python3
"""Generate narration audio for Story Video #173 — "The dead shall hear the
voice of the Son of God" (John 5:25). From DRAFTS/row-173.md.
Jesus FACE-SHOWN (master-locked). Narrator: modern, warm, low, unhurried
(American). Jesus voice: AMERICAN, never British. Jesus speaks ONLY exact KJV
(John 5:25, verified against the passage).
HOMOGRAPH LAW: "live" (the #1 TTS offender, verb) appears in the KJV verse
("they that hear shall live") and n2 ("To hear him is to live") — both
SPOKEN-respelled /LIV/; the captions keep the true spelling. Ear-check.

SEGMENTATION (ASSEMBLY-C, 2026-07-17): the KJV verse is delivered in three
flowing pieces so it can span the three stills the storyboard built for it
(s2 verily-verily, s4 light-summoned, s5 calling-hand) — split at its natural
comma/colon breaks, played as one continuous utterance (small gaps between
the pieces, the sacred pause coming BEFORE the verse, after n1). n2 is split
so the last two stills each carry a beat (CAPTION LAW). Words unchanged from
the pack; captions keep the exact KJV. Beat order: n0 s1, n1 s3, j1a s2,
j1b s4, j1c s5, n2a s6, n2b s7.
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
    # sacred-silence beat follows n1. Exact KJV John 5:25, in three flowing
    # pieces (one continuous utterance across s2/s4/s5).
    ("j1a", JESUS, "-24%", "-2Hz",
     "Verily, verily, I say unto you, The hour is coming, and now "
     "is,"),
    ("j1b", JESUS, "-24%", "-2Hz",
     "when the dead shall hear the voice of the Son of God:"),
    ("j1c", JESUS, "-24%", "-2Hz",
     "and they that hear shall live."),
    ("n2a", NARRATOR, "-20%", "-4Hz",
     "The One who made life is the One who calls it back."),
    ("n2b", NARRATOR, "-20%", "-4Hz",
     "To hear him is to live."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "He speaks, and death loses its grip. Lean in and listen — "
     "and live."),
]

# HOMOGRAPH LAW — "live" respelled /LIV/ in the audio; captions keep "live".
SPOKEN = {
    "j1c": "and they that hear shall liv.",
    "n2b": "To hear him is to liv.",
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
