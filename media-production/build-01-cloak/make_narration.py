#!/usr/bin/env python3
"""Generate narration audio for Story Video #1 — Woman Who Touched His Cloak.
Narrator: modern, warm, low, unhurried. Jesus voice: EXACT KJV only (Mark 5:34).
Text is taken verbatim from 01-cloak-production-pack.md (do not rewrite).
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewMultilingualNeural"
JESUS = "en-GB-RyanNeural"

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n1", NARRATOR, "-20%", "-4Hz",
     "There was a woman who had been suffering for twelve years."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "She had spent everything on doctors. Nothing helped. She was exhausted, "
     "desperate — and by the rules of her time, considered untouchable."),
    ("n3a", NARRATOR, "-20%", "-4Hz",
     "She heard Jesus was nearby. She did not ask permission. She did not make a speech."),
    ("n3b", NARRATOR, "-20%", "-4Hz",
     "She pressed through the crowd and reached out to touch the edge of his cloak."),
    ("n4a", NARRATOR, "-25%", "-4Hz",
     "He stopped."),
    ("n4b", NARRATOR, "-20%", "-4Hz",
     "He turned. In a crowd of dozens pressing against him, he felt her reach. "
     "He looked for her until he found her."),
    ("j1", JESUS, "-25%", "-8Hz",
     "Daughter, thy faith hath made thee whole; go in peace, and be whole of thy plague."),
    ("n5", NARRATOR, "-20%", "-4Hz",
     "Be whole of thy plague — be free of what has been hurting you. "
     "Twelve years of it. Over, in a sentence. "
     "And the first word he chose was daughter."),
]

async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
