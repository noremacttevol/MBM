#!/usr/bin/env python3
"""Generate narration audio for Story Video #127 — The Strait Gate
(Matthew 7:13-14). From DRAFTS/row-127.md, validated against the laws.
Narrator: modern, warm, low, unhurried (American). Plain US model only.
Jesus voice: AMERICAN, never British. Jesus speaks ONLY exact KJV:
Matthew 7:13 and 7:14 (both verified against the passage).
PRE-FLIGHT FIX: the draft's closing card opened with a bare number
("Two gates. One choice.") — reworded per the NUMBER-STRESS law so the
counts land stressed, in both audio and caption.
HOMOGRAPH LAW — 🛑 BUILDER MUST EAR-CHECK j1 and j2 ("leadeth", twice):
"lead" is on the flag list. It must read /LEED-eth/ (to guide), never
/LED-eth/ (the metal). If misread, add SPOKEN overrides respelling it
"leedeth" (captions keep the exact KJV spelling "leadeth").
No other flagged words in any segment.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0", NARRATOR, "-20%", "-4Hz",
     "Jesus stood before the crowd and described two roads — two "
     "ways that every person gets to choose."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "One road looks easy. The gate is wide, the path is broad, "
     "and a lot of people walk that way."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "The other road looks harder. The gate is narrow, the path is "
     "tight, and far fewer find it."),
    # Exact KJV Matt 7:13.
    ("j1", JESUS, "-20%", "-2Hz",
     "Enter ye in at the strait gate: for wide is the gate, and "
     "broad is the way, that leadeth to destruction, and many "
     "there be which go in thereat:"),
    # Exact KJV Matt 7:14.
    ("j2", JESUS, "-20%", "-2Hz",
     "Because strait is the gate, and narrow is the way, which "
     "leadeth unto life, and few there be that find it."),
    # n3 is split in two so each closing still (s6 gate-in-light, s7 hand
    # at dawn) carries the half being said — same draft words, verbatim.
    ("n3a", NARRATOR, "-20%", "-4Hz",
     "He wasn't describing geography. He was describing a decision."),
    ("n3b", NARRATOR, "-20%", "-4Hz",
     "A narrow gate that leads to life, found by the few who "
     "choose it."),
    # sacred-silence beat follows n3a on the gate-in-light still.
    ("card", NARRATOR, "-22%", "-5Hz",
     "There are two gates, and one choice. He said the narrow way "
     "is worth finding. Step through."),
]

# HOMOGRAPH LAW — see the docstring: ear-check "leadeth" in j1/j2 before
# assembly. If (and only if) TTS misreads it, uncomment the overrides.
# Ear-check 2026-07-17 (ASSEMBLY-B): j2 read "leadeth" as /LED-eth/
# ("letteth" per whisper). Overrides enabled for BOTH KJV lines —
# captions keep the exact KJV spelling "leadeth".
SPOKEN = {
    "j1": ("Enter ye in at the strait gate: for wide is the gate, and "
           "broad is the way, that leedeth to destruction, and many "
           "there be which go in thereat:"),
    "j2": ("Because strait is the gate, and narrow is the way, which "
           "leedeth unto life, and few there be that find it."),
}


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts_text = SPOKEN.get(name, text)
        tts = edge_tts.Communicate(tts_text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
