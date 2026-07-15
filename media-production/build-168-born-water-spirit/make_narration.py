#!/usr/bin/env python3
"""Generate narration audio for Story Video #168 — "Born of water and of the Spirit"
(John 3:5, with 3:1-8). MEMBER shelf verse-video. → Gospel Library topic: Baptism.

Narrator: en-US-AndrewNeural — plain American, modern paraphrase, never a
Multilingual model, never echoes the KJV wording.
Scripture voice: en-US-ChristopherNeural — speaks the KJV text EXACTLY. (The Lord's words
to Nicodemus; the scripture voice carries them. He is NOT depicted as a figure; the one
Nicodemus comes to, and the Spirit, are shown only as warm light — never a face or dove.)

KJV lines (exact — the parallel pair):
  kv3 = John 3:3  born again -> SEE the kingdom of God (SACRED SILENCE 1)
  kv5 = John 3:5  born of water and of the Spirit -> ENTER the kingdom (NAMED — SACRED SILENCE 2)

WHY-LAW: the gate — to enter the kingdom a person must be born again: born of water (baptism)
and of the Spirit (the gift of the Holy Ghost). STUDY GEM: the gate is the gate — required for
everyone, even a wise and good ruler like Nicodemus (n6); ties the baptism + Holy-Ghost thread
together.

TRANSLATION LAW: the narrator never re-quotes a KJV line. n2/n3 paraphrase v4; n4/n5 explain
water and Spirit as baptism and the gift; the exact KJV lands only in kv3/kv5.

MILK FRAMING: an invitation. The closing card ends on an open question and a one-line
pointer to the Gospel Library topic (Baptism). No shame, no fear.

NUMBER-STRESS LAW: no sentence opens with a bare number.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"
SCRIPTURE = "en-US-ChristopherNeural"

SEGMENTS = [
    ("n1", NARRATOR, "-20%", "-4Hz",
     "Nicodemus was a ruler and a respected teacher, a man near the top of his world. And "
     "yet, one night, he slipped quietly through the dark streets to ask his questions in "
     "private, humble enough to come and learn."),
    ("n2", NARRATOR, "-22%", "-4Hz",
     "He came to the light and listened. And what he heard turned his careful world upside "
     "down. It was not a small adjustment or one more rule to keep. It was a whole new "
     "beginning — a person must be born all over again."),
    # kv3 — SACRED SILENCE 1
    ("kv3", SCRIPTURE, "-26%", "-6Hz",
     "Jesus answered and said unto him, Verily, verily, I say unto thee, Except a man be "
     "born again, he cannot see the kingdom of God."),
    ("n3", NARRATOR, "-22%", "-4Hz",
     "Nicodemus took it literally, and was baffled. How could a grown man possibly be born "
     "a second time? He could not picture it. Surely no one could climb back and start his "
     "life over from the beginning."),
    ("n4", NARRATOR, "-22%", "-4Hz",
     "But the new birth was never meant to be physical. To be born again is first to be born "
     "of water — to go down into the water of baptism and come up new, the old life washed "
     "away and left behind."),
    ("n5", NARRATOR, "-22%", "-4Hz",
     "And there was a second half to it, not water only. To be born of the Spirit is to "
     "receive the gift of the Holy Ghost — a birth from above, life breathed into the soul "
     "by heaven itself."),
    # kv5 — NAMED VERSE, SACRED SILENCE 2
    ("kv5", SCRIPTURE, "-26%", "-6Hz",
     "Jesus answered, Verily, verily, I say unto thee, Except a man be born of water and of "
     "the Spirit, he cannot enter into the kingdom of God."),
    ("n6", NARRATOR, "-22%", "-4Hz",
     "Here is the quiet study gem. Notice he did not say this was one good option among "
     "many. He said a person cannot enter without it. The gate is the gate — the same for "
     "everyone, even a learned and upright ruler like Nicodemus."),
    ("n7", NARRATOR, "-24%", "-4Hz",
     "And that same single gate still stands open before you: born of water, and born of the "
     "Spirit. The door is not hidden and it is not narrow with pride — it is simply the way "
     "in. When you stand before it, will you go through?"),
    ("card", NARRATOR, "-26%", "-4Hz",
     "To enter the kingdom, a person must be born again — born of water in baptism, and of "
     "the Spirit from above. The gate is the gate, the same for everyone. When you stand "
     "before it, will you go through?"),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
