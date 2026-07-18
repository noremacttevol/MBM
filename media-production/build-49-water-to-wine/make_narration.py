#!/usr/bin/env python3
"""Generate narration audio for Story Video #49 — Water to Wine at Cana (John 2:1-11).

Narrator: en-US-AndrewNeural — plain American, never a Multilingual model.
Jesus voice: en-US-ChristopherNeural — American, never British.

Jesus speaks ONLY exact KJV. Three lines (the rest of the dialogue is Mary and the
governor of the feast, carried by the narrator, never in the Jesus voice):
  jv4  = John 2:4   "Woman, what have I to do with thee? mine hour is not yet come."
  jv7  = John 2:7   "Fill the waterpots with water."            — SACRED SILENCE 1
  jv8  = John 2:8   "Draw out now, and bear unto the governor of the feast." — SILENCE 2

CAPTIONS ARE VERBATIM (Cameron, 2026-07-11): build.py imports these SEGMENTS and
word-wraps each text as the on-screen caption. KJV (Jesus) lines render cream italic.

CARE FLAGS: none — GREEN, plain milk. Framed around JOY, generosity and abundance, NOT
around drink: the wine is the sign of gladness and of God saving the best for last (the
verse card, John 2:10). "Well drunk" (v10) is softened to "once everyone had been served
a while" — the point is the quality and the lavishness, never intoxication.

WHY-LAW: two lines do damage if delivered flat. (1) "Woman, what have I to do with thee"
(v4) sounds cold in English but was not: "Woman" was a term of respect, and the phrase is
a gentle Semitic idiom ("is this ours to fix, and is it the time?"). n5 says this out loud;
without it this video misreads him as rude to his mother. (2) the miracle has NO show — no
lightning, no words over the jars — and n9 keeps it that quiet, because the restraint is
the point: he turned a family's worst moment into more joy than they started with, and
almost no one even knew.

TRANSLATION LAW: the narrator gives the plain meaning and does not re-quote KJV wording —
n9 says "dip a cup and carry it to the man in charge" instead of echoing "draw out / bear
unto the governor". CLOSING CARD IS AN INVITATION, never a fear-question.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text) — text is BOTH spoken and captioned.
    # --- s1: the first miracle was a wedding ---
    ("n1", NARRATOR, "-20%", "-4Hz",
     "The very first miracle he ever did was not what you would guess. Not a "
     "healing. Not calming a storm. He saved a village wedding from falling apart."),
    # --- s2: he was there as a guest, in ordinary joy ---
    ("n2", NARRATOR, "-22%", "-4Hz",
     "He was there as a guest, with his mother and his friends. A wedding in a "
     "small town like Cana ran for days, and the whole village came. It was pure, "
     "ordinary joy, and he was right in the middle of it."),
    # --- s3: the wine runs out ---
    ("n3", NARRATOR, "-22%", "-4Hz",
     "And then, quietly, disaster. The wine ran out. To us that sounds small. To "
     "that family it was a public shame they would carry for years. The feast, and "
     "their good name, were about to collapse."),
    # --- s4: his mother goes straight to him ---
    ("n4", NARRATOR, "-22%", "-4Hz",
     "His mother noticed before anyone else did. And she did not go to the host, or "
     "the kitchen. She went straight to her son and told him the plain truth. They "
     "have no wine."),
    # --- s5: v4 — his reply, and what it really means ---
    ("jv4", JESUS, "-26%", "-6Hz",
     "Woman, what have I to do with thee? mine hour is not yet come."),
    ("n5", NARRATOR, "-22%", "-4Hz",
     "That sounds sharp in English, but it was not. Woman was a word of respect, "
     "and the phrase was a gentle old idiom, something like, is this really "
     "ours to fix, and is now the time? He was not brushing her off. He was "
     "wondering out loud whether this was the moment to begin."),
    # --- s6: his mother to the servants — the best advice in the Bible ---
    ("n6", NARRATOR, "-22%", "-4Hz",
     "And his mother, who knew him better than anyone alive, did not argue. She "
     "just turned to the servants and gave them the best advice in the whole Bible. "
     "Whatever he tells you, do it. Then she stepped back and left it with him."),
    # --- s7: the six stone waterpots ---
    ("n7", NARRATOR, "-22%", "-4Hz",
     "Standing nearby were six big stone jars, the kind kept for the washing "
     "rituals, each one holding twenty or thirty gallons. Empty jars, meant for "
     "making things clean. Not a wine cup in sight."),
    # --- s8: v7 — fill them with water. SACRED SILENCE 1. ---
    ("jv7", JESUS, "-28%", "-6Hz",
     "Fill the waterpots with water."),
    ("n8", NARRATOR, "-22%", "-4Hz",
     "Not wine. Water. The plainest thing there is, from the nearest well. The "
     "servants filled all six to the very top, hauling bucket after bucket, surely "
     "wondering what plain water had to do with the problem."),
    # --- s9: v8 — draw out now. SACRED SILENCE 2. The quiet miracle. ---
    ("jv8", JESUS, "-28%", "-6Hz",
     "Draw out now, and bear unto the governor of the feast."),
    ("n9", NARRATOR, "-22%", "-4Hz",
     "No lightning. No words spoken over the jars. No show at all. He simply told "
     "them to dip a cup and carry it to the man in charge of the feast. And "
     "somewhere between the jar and the cup, the water quietly became something "
     "else."),
    # --- s10: the governor tastes — the best wine ---
    ("n10", NARRATOR, "-22%", "-4Hz",
     "The steward tasted it and had no idea where it came from. He pulled the "
     "bridegroom aside, half laughing. Everyone serves the good wine first, he "
     "said, and the cheap stuff once the guests have stopped paying attention. You "
     "saved the best for last."),
    # --- s11: he saved the best for last — lavish abundance ---
    ("n11", NARRATOR, "-22%", "-4Hz",
     "And that is the line to hold on to. He saved the best for last. Not a bare "
     "rescue, not just barely enough to get by. Something like a hundred and fifty "
     "gallons of the finest wine at the party, poured out on ordinary people who "
     "would never even know who paid for it."),
    # --- s12: the glory manifested, and they believed ---
    ("n12", NARRATOR, "-24%", "-4Hz",
     "That is the God this story is showing you. His first move in the whole world "
     "was not to frighten anyone or settle a score. It was to walk into a family's "
     "worst moment of the day and quietly turn it into more joy than they started "
     "with. His friends saw it, and they believed him."),
    # --- closing card, read gently (Readable-Card Law). An INVITATION. ---
    ("card", NARRATOR, "-26%", "-4Hz",
     "His very first miracle was making a good day even better, for people who "
     "never asked and never knew. If that is how he begins, what do you think he is "
     "like? What would you bring a God who saves the best for last?"),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        await save_narration(text, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
