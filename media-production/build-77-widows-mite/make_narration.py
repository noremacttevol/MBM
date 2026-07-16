#!/usr/bin/env python3
"""Generate narration audio for Story Video #77 — The Widow's Mite (Mark 12:41-44).
Narrator: modern, warm, low, unhurried (American). Plain US model only.
Jesus voice: AMERICAN, never British. Jesus speaks ONLY exact KJV:
Mark 12:43-44 in full, including "Verily I say unto you, That" (fetched, not
hand-typed). CONTENT-CARE: GREEN — dignity for the widow, no pity-spectacle; the
contrast with the rich is gentle, never mocking.
HOMOGRAPH LAW: EAR-CHECK "living" in j1 ("all her living" — the liv- root); if TTS
says /LYE-ving/, add SPOKEN override "livving" for j1 (caption stays exact KJV).
No music bed: narration + intentional silence only.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0", NARRATOR, "-20%", "-4Hz",
     "Jesus sat down across from the temple treasury and just watched "
     "people give."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "The rich came through and put in large amounts — you could hear "
     "the coins land, and everyone noticed."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "Then a poor widow came. She put in two tiny copper coins — "
     "together worth less than a penny."),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "Jesus called his disciples over, like he had just seen the most "
     "important thing all day."),
    # Exact KJV Mark 12:43-44, in full — SILENCE around it. EAR-CHECK "living".
    ("j1", JESUS, "-20%", "-2Hz",
     "Verily I say unto you, That this poor widow hath cast more in, "
     "than all they which have cast into the treasury: for all they did "
     "cast in of their abundance; but she of her want did cast in all "
     "that she had, even all her living."),
    ("n4", NARRATOR, "-20%", "-4Hz",
     "Everyone else gave from what they had left over. She gave from "
     "what she needed. Heaven does the math differently than we do."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "He noticed the gift no one else did. What might he already see in "
     "you that others overlook?"),
]

# HOMOGRAPH LAW — ear-check j1's "living" (/LIV-ing/, never /LYE-ving/) before
# assembly; if misread, activate:  SPOKEN = {"j1": "... even all her livving."}
# (caption text stays exact KJV). No other flagged words in these segments.
SPOKEN = {}


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts_text = SPOKEN.get(name, text)
        tts = edge_tts.Communicate(tts_text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
