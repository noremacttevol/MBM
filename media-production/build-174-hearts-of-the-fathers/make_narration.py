#!/usr/bin/env python3
"""Generate narration audio for Story Video #174 — Elijah, and the Hearts of
the Fathers (Malachi 4:5-6; cf. Luke 1:17). From DRAFTS/row-174.md.
Jesus does NOT appear (prophecy of Elijah/John). Narrator en-US-AndrewNeural;
the exact-KJV centerpiece (Malachi 4:5-6) is carried by the SCRIPTURE voice
(en-US-ChristopherNeural, build-161 precedent), cream-italic, split at the
colon into two flowing pieces so it spans the two stills the storyboard built
for it (s1a on s2 resolve-and-mercy, s1b on s3 the-turn-beginning).
HOMOGRAPH LAW: no flagged words. Clean. Ear-check anyway.

SEGMENTATION (ASSEMBLY-C, 2026-07-17): the KJV verse is split at its colon
(s1a/s1b, flowing as one utterance); n2 is split at its dash so the last two
stills each carry a beat (CAPTION LAW). Beat order places the family finale
(s7) last: n0 s1, s1a s2, s1b s3, n1 s4, n3 s6 (John), n2a s5 (Elijah pointing
to the coming Lord), n2b s7 (the whole family — "whole"). Words unchanged from
the pack; only n2b's leading word is capitalized to stand alone.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"        # plain American — never a Multilingual model
SCRIPTURE = "en-US-ChristopherNeural"  # the scripture voice. Exact KJV only.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0", NARRATOR, "-20%", "-4Hz",
     "Before the great day, a messenger would come first — Elijah, "
     "the prophet, sent ahead."),
    # Exact KJV Malachi 4:5-6, split at the colon, one continuous utterance.
    ("s1a", SCRIPTURE, "-24%", "-2Hz",
     "Behold, I will send you Elijah the prophet before the coming "
     "of the great and dreadful day of the LORD:"),
    ("s1b", SCRIPTURE, "-24%", "-2Hz",
     "And he shall turn the heart of the fathers to the children, "
     "and the heart of the children to their fathers, lest I come "
     "and smite the earth with a curse."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "His work was not to thunder, but to mend. To turn the hearts "
     "of fathers back to their children, and children back to "
     "their fathers."),
    # sacred-silence beat follows n1.
    ("n3", NARRATOR, "-20%", "-4Hz",
     "The same spirit would later rest on John, preparing the "
     "way."),
    ("n2a", NARRATOR, "-20%", "-4Hz",
     "So that when the Lord came, families would be ready."),
    ("n2b", NARRATOR, "-20%", "-4Hz",
     "Not divided, but whole."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "He cares about your family. Let the healing start with your "
     "own heart."),
]

SPOKEN = {}


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts_text = SPOKEN.get(name, text)
        tts = edge_tts.Communicate(tts_text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
