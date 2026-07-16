#!/usr/bin/env python3
"""Generate narration audio for Story Video #130 — "Ye Know Not What Manner of
Spirit Ye Are Of" (Luke 9:51-56). From DRAFTS/row-130.md, validated against
the laws.
Narrator: modern, warm, low, unhurried (American). Plain US model only.
Jesus voice: AMERICAN, never British. Jesus speaks ONLY exact KJV:
Luke 9:55-56 (his spoken words, verified against the passage).
HOMOGRAPH LAW — 🛑 BUILDER MUST EAR-CHECK j1 ("destroy men's LIVES"): "lives"
is on the flag list. Here it is the NOUN and must read /LYVZ/ (rhymes with
"hives"), never /LIVZ/. The natural TTS reading is usually right for the
noun, but LISTEN before assembly. If misread, add SPOKEN override respelling
it "lyves" (caption keeps the exact KJV word).
No other flagged words in any segment.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0", NARRATOR, "-20%", "-4Hz",
     "As Jesus traveled toward Jerusalem, a Samaritan village "
     "refused to welcome Him. The disciples James and John were "
     "hot with anger."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "They asked if they should call down fire from heaven to burn "
     "the place. They wanted judgment."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "Jesus turned and rebuked them — not the village, but His own "
     "disciples' hearts."),
    # Exact KJV Luke 9:55-56 — SILENCE around it.
    ("j1", JESUS, "-20%", "-2Hz",
     "Ye know not what manner of spirit ye are of. For the Son of "
     "man is not come to destroy men's lives, but to save them."),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "He didn't come to burn. He came to rescue. The fire in the "
     "disciples' hearts was the wrong kind."),
    # sacred-silence beat follows n3.
    ("n4", NARRATOR, "-20%", "-4Hz",
     "Anger that wants to destroy isn't from Him. The spirit He "
     "brings saves."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "He came to save, not to burn. Let His Spirit — the saving "
     "one — shape yours."),
]

# HOMOGRAPH LAW — see the docstring: ear-check "lives" in j1 before assembly.
# If (and only if) TTS misreads it as /LIVZ/, uncomment the override.
SPOKEN = {
    # "j1": ("Ye know not what manner of spirit ye are of. For the Son of "
    #        "man is not come to destroy men's lyves, but to save them."),
}


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts_text = SPOKEN.get(name, text)
        tts = edge_tts.Communicate(tts_text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
