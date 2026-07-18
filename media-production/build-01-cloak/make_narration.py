#!/usr/bin/env python3
"""Generate narration audio for Story Video #1 — Woman Who Touched His Cloak. v2.
Narrator: modern, warm, low, unhurried (American).
Jesus voice: AMERICAN, never British (Cameron's permanent law, 2026-07-07).
Jesus speaks ONLY exact KJV: Mark 5:30 "Who touched my clothes?" and Mark 5:34.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"     # plain American — never the Multilingual model (law)
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n1", NARRATOR, "-20%", "-4Hz",
     "There was a woman who had been suffering for twelve years."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "She had spent everything on doctors. Nothing helped. She was exhausted, "
     "desperate — and by the rules of her time, considered untouchable."),
    ("n2b", NARRATOR, "-20%", "-4Hz",
     "That day, Jesus was already on his way to save someone else — a ruler's "
     "daughter, twelve years old, and dying. The crowd pressed around him on "
     "every side. Almost no one would have noticed one more sick woman at its edge."),
    ("n3a", NARRATOR, "-20%", "-4Hz",
     "She heard Jesus was nearby. She did not ask permission. She did not make a speech."),
    ("n3b", NARRATOR, "-20%", "-4Hz",
     "She pressed through the crowd and reached out to touch the edge of his cloak."),
    ("n4a", NARRATOR, "-22%", "-4Hz",
     "He stopped. He had felt it — power had gone out of him. "
     "The healing was already hers, given the moment she touched him."),
    ("j0", JESUS, "-25%", "-6Hz",
     "Who touched my clothes?"),
    ("n4c", NARRATOR, "-20%", "-4Hz",
     "His disciples thought the question made no sense. The whole crowd was "
     "pressing against him — who hadn't touched him? He ignored them. He was "
     "already needed somewhere else, and he stopped anyway."),
    ("n4b", NARRATOR, "-22%", "-4Hz",
     "He looked for her until he found her."),
    ("j1", JESUS, "-25%", "-6Hz",
     "Daughter, thy faith hath made thee whole; go in peace, and be whole of thy plague."),
    ("n5", NARRATOR, "-20%", "-4Hz",
     "Be whole of thy plague — be free of what has been hurting you. "
     "Twelve years of it. Over, in a sentence. "
     "And the first word he chose was daughter."),
    # closing card — an invitation, read gently
    ("card", NARRATOR, "-22%", "-4Hz",
     "Whatever you have carried for years — reach for him. "
     "He stops for the one. He calls you his own."),
]

async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        await save_narration(text, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
