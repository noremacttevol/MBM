#!/usr/bin/env python3
"""Generate narration audio for Story Video #138 — "We Are Also His Offspring"
(Acts 17:22-31, Paul at Mars' Hill). From DRAFTS/row-138.md, validated
against the laws.
Narrator: modern, warm, low, unhurried (American). Plain US model only.
Jesus does NOT appear or speak in this story. The exact KJV of Acts 17:28 is
PAUL's sermon line — carried by the SCRIPTURE VOICE (Christopher) per the
build-161 precedent (the narrator never quotes KJV).
HOMOGRAPH LAW: "live" (the #1 TTS offender) appears in BOTH the KJV line (p1)
and the narrator's echo (n2) — must read /LIV/ (to be alive), never /LYVE/.
SPOKEN respelling "liv" applied to both; captions keep the exact spelling.
Ear-check both segments before assembly anyway.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"      # plain American — never a Multilingual model
SCRIPTURE = "en-US-ChristopherNeural"  # the scripture voice. Exact KJV only.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    # n0 split so the Mars-hill still and the unknown-altar still each
    # carry their half — draft words verbatim.
    ("n0a", NARRATOR, "-20%", "-4Hz",
     "Paul stood in the middle of Athens, surrounded by statues to "
     "every god they could think of —"),
    ("n0b", NARRATOR, "-20%", "-4Hz",
     "and one altar that simply said, To the unknown God."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "He told them they were already closer than they knew. The "
     "God they'd left unnamed made the whole world, and He is not "
     "far from any of us."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "In Him, Paul said, we live and move and have our being. He "
     "even quoted their own poets: we are His children."),
    # Exact KJV Acts 17:28 — Paul's line, scripture voice.
    ("p1", SCRIPTURE, "-22%", "-2Hz",
     "For in him we live, and move, and have our being; as certain "
     "also of your own poets have said, For we are also his "
     "offspring."),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "God overlooked the times of ignorance before, Paul said — "
     "but now He commands all men everywhere to repent."),
    # sacred-silence beat follows n3.
    ("n4", NARRATOR, "-20%", "-4Hz",
     "The unknown God was never unknown to Him. He had been near "
     "the whole time."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "You were made to be His. Reach out — He is not far."),
]

# HOMOGRAPH LAW — "live" must read /LIV/ in n2 and p1. SPOKEN respelling
# steers the audio; the captions keep the true spelling. Ear-check both.
SPOKEN = {
    "n2": ("In Him, Paul said, we liv and move and have our being. He "
           "even quoted their own poets: we are His children."),
    "p1": ("For in him we liv, and move, and have our being; as certain "
           "also of your own poets have said, For we are also his "
           "offspring."),
}


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts_text = SPOKEN.get(name, text)
        await save_narration(tts_text, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
