#!/usr/bin/env python3
"""Generate narration audio for Story Video #27 — The Leaven (Matthew 13:33).

Narrator: en-US-AndrewNeural — plain American, never a Multilingual model.
Jesus voice: en-US-ChristopherNeural — American, never British.
Jesus speaks ONLY exact KJV: Matthew 13:33 (j1) — the whole one-verse parable.

CAPTIONS ARE VERBATIM (Cameron, 2026-07-11): build.py imports these SEGMENTS
and word-wraps each text as the on-screen caption, so every word spoken is on
the screen. After the KJV line the narrator gives ONLY the plain modern meaning
and never re-quotes the KJV words (Translation Law).

A parable told BY Jesus with NO Jesus figure on screen — only his narrating
voice; the whole picture is an ordinary woman baking bread (STILLS-ONLY, Law E;
face gate trivial — no Jesus figure at all).

THE POINT (how GOOD he is): the kingdom does not come by force or spectacle. It
works quietly, hidden, from the inside, in ordinary hands, and it never stops
until the WHOLE is changed. That is how gently and completely God works in a
person.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text) — text is BOTH spoken and captioned.
    # --- s1: a woman takes the leaven ---
    ("n1", NARRATOR, "-20%", "-4Hz",
     "Jesus said the kingdom of God is like something a woman does every week, "
     "in her own kitchen, with her own hands."),
    ("j1", JESUS, "-26%", "-6Hz",
     "The kingdom of heaven is like unto leaven, which a woman took, and hid in "
     "three measures of meal, till the whole was leavened."),
    ("n2", NARRATOR, "-22%", "-4Hz",
     "Leaven is just a little piece of old, living dough, what we would call a "
     "sourdough starter. Small. Plain. Easy to overlook."),
    # --- s2: three measures of meal (the scale) ---
    ("n3", NARRATOR, "-22%", "-4Hz",
     "And three measures of meal is not a small bowl. It is an enormous amount "
     "of flour, enough bread to feed a hundred people."),
    # --- s3: she hides it in ---
    ("n4", NARRATOR, "-22%", "-4Hz",
     "She takes that tiny bit of leaven and works it down deep into the whole "
     "mass, hiding it, until you cannot even see where it went."),
    # --- s4: covered, waiting ---
    ("n5", NARRATOR, "-22%", "-4Hz",
     "Then she covers it and waits. Nothing looks like it is happening. No "
     "noise, no show, no spectacle. Just quiet, hidden time."),
    # --- s5: the risen dough (the peak) ---
    ("n6", NARRATOR, "-24%", "-5Hz",
     "But inside, the leaven is spreading through every part of the dough. And "
     "by morning the whole heavy mass has risen, alive, changed all the way "
     "through."),
    # --- s6: the baked bread ---
    ("n7", NARRATOR, "-22%", "-4Hz",
     "That, Jesus said, is how the kingdom of God works. Not by force. Not by "
     "noise. It starts small and hidden, and it quietly changes everything it "
     "touches, from the inside out."),
    # --- s7: bread carried to the table (transformation shared) ---
    ("n8", NARRATOR, "-24%", "-4Hz",
     "That is how good he is. He does not overpower you. He works gently, "
     "patiently, from within, until the whole of you is warmed and changed and "
     "made into something that can feed other people."),
    # --- closing card, read gently (Readable-Card Law) ---
    ("card", NARRATOR, "-26%", "-4Hz",
     "God is often working quietest right where you cannot see it yet. Where "
     "might he already be at work inside you?"),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        await save_narration(text, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
