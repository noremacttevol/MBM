#!/usr/bin/env python3
"""Generate narration audio for Story Video #96 — "It Is Finished"; the Veil Torn
(John 19:28-30 / Matt 27:50-51). From DRAFTS/row-096.md, validated against the laws.
Narrator: modern, warm, low, unhurried (American). Plain US model only.
Jesus voice: AMERICAN, never British. Jesus speaks ONLY exact KJV:
John 19:30 "It is finished." (verified against the passage).
CONTENT-CARE: reverent distance — no gore, no wounds; the veil-tearing is awe,
not horror.
HOMOGRAPH LAW — 🛑 BUILDER MUST EAR-CHECK n2 ("he BOWED his head"): "bow" is on
the flag list. It must read /BOWD/ as in "bough"/"plow" (bending down), never
/BOHD/ as in "ribbon". Context usually saves it, but LISTEN before assembly.
If misread, add SPOKEN override: n2 -> "And he boughed his head and gave up
the spirit — on his own terms, not theirs." (caption stays "bowed").
No other flagged words in any segment.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0", NARRATOR, "-20%", "-4Hz",
     "At the very end, Jesus knew everything had now been "
     "accomplished. He wasn't a victim losing a fight — he was "
     "finishing a work."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "With his last breath he spoke three words that weren't a cry "
     "of defeat, but a declaration of completion."),
    # sacred-silence beat follows n1. Exact KJV John 19:30 — SILENCE around it.
    ("j1", JESUS, "-24%", "-2Hz",
     "It is finished."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "And he bowed his head and gave up the spirit — on his own "
     "terms, not theirs."),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "At that moment, in the temple across the city, the great "
     "veil that walled off the holiest place was torn in two, from "
     "the top down — as if torn by a hand from above."),
    ("n4", NARRATOR, "-20%", "-4Hz",
     "That curtain had kept people out of God's presence for "
     "centuries. The instant he died, it was ripped open. The way "
     "in was thrown wide — for everyone."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "The curtain that kept you out was torn open the moment he "
     "died. The way to God is open. Walk in."),
]

# HOMOGRAPH LAW — see the docstring: ear-check n2 "bowed" before assembly.
# If (and only if) TTS misreads it, uncomment the override below.
SPOKEN = {
    # "n2": ("And he boughed his head and gave up the spirit — on his "
    #        "own terms, not theirs."),
}


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts_text = SPOKEN.get(name, text)
        tts = edge_tts.Communicate(tts_text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
