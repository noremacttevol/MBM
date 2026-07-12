#!/usr/bin/env python3
"""Generate narration audio for Story Video #24 — The Sower
(Matthew 13:1-9, 18-23).

Narrator: en-US-AndrewNeural — plain American, never a Multilingual model.
Jesus voice: en-US-ChristopherNeural — American, never British.
Jesus speaks ONLY exact KJV: Matthew 13:3 (j1), 13:9 (j2), 13:23 (j3).

CAPTIONS ARE VERBATIM (Cameron, 2026-07-11): build.py imports these SEGMENTS
and word-wraps each text as the on-screen caption, so every word spoken is on
the screen. After each KJV Jesus line the narrator gives ONLY the plain modern
meaning and never re-quotes the KJV words (Translation Law).

A parable told BY Jesus from the boat: he is the narrating voice and appears
only in the bookend shots (s1, s7) as a seated teacher seen from behind, his
face never shown (STILLS-ONLY, Law E; Jesus face-never, #18). The farmer and
the four soils are shown fully.

THE POINT (how GOOD he is): the farmer flings seed on EVERY kind of ground —
even the hard path, even the rock, even the thorns — not only the good. God is
that generous with his word, and no soil is fixed forever.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text) — text is BOTH spoken and captioned.
    # --- s1: Jesus teaches from the boat ---
    ("n1", NARRATOR, "-20%", "-4Hz",
     "So many people crowded the shore to hear Jesus that he pushed a small "
     "boat out onto the water and taught them from there, the whole hillside "
     "listening."),
    ("n2", NARRATOR, "-22%", "-4Hz",
     "And he told them a story about a farmer, and four kinds of ground."),
    # --- s2: the sower goes out (KJV j1 = Matthew 13:3) ---
    ("j1", JESUS, "-26%", "-6Hz",
     "Behold, a sower went forth to sow;"),
    ("n3", NARRATOR, "-22%", "-4Hz",
     "A farmer went out to scatter his seed. He did not measure it out grain by "
     "grain. He flung it wide, across every kind of ground, hoping all of it "
     "would grow."),
    # --- s3: the wayside ---
    ("n4", NARRATOR, "-22%", "-4Hz",
     "Some fell on the hard path, packed down by every foot that had ever "
     "walked it. It never sank in, and the birds came and ate it."),
    ("n5", NARRATOR, "-22%", "-4Hz",
     "That, he said, is a heart so hardened that the word never gets below the "
     "surface before it is snatched away."),
    # --- s4: stony ground ---
    ("n6", NARRATOR, "-22%", "-4Hz",
     "Some fell on thin soil over rock. It sprang up fast, green and hopeful, "
     "but it had no root, and when the sun grew hot it withered."),
    ("n7", NARRATOR, "-22%", "-4Hz",
     "That is the heart that says yes with joy, but has nothing underneath to "
     "hold it when things get hard."),
    # --- s5: thorns ---
    ("n8", NARRATOR, "-22%", "-4Hz",
     "Some fell among thorns. The seed grew, but so did the weeds, and the "
     "worries and wants of this life crowded in and choked it before it could "
     "bear anything."),
    # --- s6: good ground (KJV j3 = 13:23), the peak ---
    ("n9", NARRATOR, "-24%", "-5Hz",
     "But some fell on good ground, open and soft and ready. It took root, and "
     "grew, and gave back a harvest many times over."),
    ("j3", JESUS, "-26%", "-6Hz",
     "But he that received seed into the good ground is he that heareth the "
     "word, and understandeth it; which also beareth fruit, and bringeth "
     "forth, some an hundredfold, some sixty, some thirty."),
    ("n10", NARRATOR, "-22%", "-4Hz",
     "The good ground is simply the heart that hears him, takes it in, and "
     "holds on. And it gives back far more than was ever put in."),
    # --- s7: the generous farmer, the call (KJV j2 = 13:9) ---
    ("n11", NARRATOR, "-22%", "-4Hz",
     "Notice the farmer did not skip the hard path or the rocky places. He "
     "threw seed everywhere, on every heart, hoping. That is how generous God "
     "is with his word."),
    ("j2", JESUS, "-26%", "-6Hz",
     "Who hath ears to hear, let him hear."),
    ("n12", NARRATOR, "-24%", "-4Hz",
     "And ground can change. A hard path can be broken up. Rocky soil can be "
     "cleared. That is how good he is. He keeps sowing, and he never stops "
     "hoping your heart will be the good ground."),
    # --- closing card, read gently (Readable-Card Law) ---
    ("card", NARRATOR, "-26%", "-4Hz",
     "None of these soils are fixed forever. What is the soil of your heart "
     "today?"),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
