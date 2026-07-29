#!/usr/bin/env python3
"""Narration for build-168-born-water-spirit — John 3.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

TWO SPLITS, and they are the whole point of this plan. Both original segments
opened with John's narration welded onto Christ's words and were painted red end
to end, which put the evangelist's reporting into the Lord's mouth and his voice.

SPLIT 1 — John 3:3
  kv3   (scripture, blue)  'Jesus answered and said unto him,'
  kv3b  (jesus, RED)       'Verily, verily, I say unto thee, Except a man be born
                            again, he cannot see the kingdom of God.'
SPLIT 2 — John 3:5
  kv5   (scripture, blue)  'Jesus answered,'
  kv5b  (jesus, RED)       'Verily, verily, I say unto thee, Except a man be born
                            of water and of the Spirit, he cannot enter into the
                            kingdom of God.'
A red-letter King James Bible starts the red at 'Verily' in both verses. kv3 and
kv5 keep their original ids so nothing that references them by name is orphaned;
kv3b and kv5b are the new ones. BOTH HALVES OF EACH SPLIT STAY ON THE SAME STILL
— kv3/kv3b on S3, kv5/kv5b on S7 — so no new artwork and the edit the viewer sees
is identical. kv5 is only two words; that is correct, it is a short blue beat and
it hands straight off to the red.

LIFTED FROM PARAPHRASE:
  s4  John 3:4  'How can a man be born when he is old? can he enter the second
      time into his mother's womb, and be born?'   SCRIPTURE, blue
Nicodemus was the other man in this conversation and he never got to speak — n3
was reporting his bewilderment for him. He asks it himself now, in his own words.
The KJV frame 'Nicodemus saith unto him,' is left off so s4 is his speech only.
This matches build-04-nicodemus, which gives him the same four lines in blue.

kv3b -> s4 is a DELIBERATE statement-and-question pair: the Lord says it, and the
ruler's honest confusion comes straight back at him with no narrator in between.
That is the exception the retelling rule allows, and n3 retells both immediately
after. The validator warns about it; the warning is expected.

WHY-LAW: milk. Baptism and the gift of the Holy Ghost are shown as one gate open
to everybody, framed by a good and learned man who still had to walk through it.
Nothing on screen argues about who may perform it.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "Nicodemus was a ruler and a respected teacher, a man near the top of his world. And yet, one night, he slipped quietly through the dark streets to ask his questions in private, humble enough to come and learn."),
    ("n2", NARRATOR, "He came to the light and listened. And what he heard turned his careful world upside down. It was not a small adjustment or one more rule to keep. It was a whole new beginning — a person must be born all over again."),
    # John 3:3
    ("kv3", SCRIPTURE, "Jesus answered and said unto him,"),
    # John 3:3
    ("kv3b", JESUS, "Verily, verily, I say unto thee, Except a man be born again, he cannot see the kingdom of God."),
    # John 3:4
    ("s4", SCRIPTURE, "How can a man be born when he is old? can he enter the second time into his mother's womb, and be born?"),
    ("n3", NARRATOR, "Nicodemus took it literally, and was baffled. He could not picture it. Surely no one could climb back and start his life over from the beginning."),
    ("n4", NARRATOR, "But the new birth was never meant to be physical. To be born again is first to be born of water — to go down into the water of baptism and come up new, the old life washed away and left behind."),
    ("n5", NARRATOR, "And there was a second half to it, not water only. To be born of the Spirit is to receive the gift of the Holy Ghost — a birth from above, life breathed into the soul by heaven itself."),
    # John 3:5
    ("kv5", SCRIPTURE, "Jesus answered,"),
    # John 3:5
    ("kv5b", JESUS, "Verily, verily, I say unto thee, Except a man be born of water and of the Spirit, he cannot enter into the kingdom of God."),
    ("n6", NARRATOR, "Here is the quiet study gem. Notice he did not say this was one good option among many. He said a person cannot enter without it. The gate is the gate — the same for everyone, even a learned and upright ruler like Nicodemus."),
    ("n7", NARRATOR, "And that same single gate still stands open before you: born of water, and born of the Spirit. The door is not hidden and it is not narrow with pride — it is simply the way in. When you stand before it, will you go through?"),
    ("card", NARRATOR, "To enter the kingdom, a person must be born again — born of water in baptism, and of the Spirit from above. The gate is the gate, the same for everyone. When you stand before it, will you go through?"),
]

# Homographs this build decides for itself (never auto-replaced globally).
SPOKEN = {}


async def main():
    os.makedirs("audio", exist_ok=True)
    for name, speaker, text in SEGMENTS:
        flagged = [w for w in audit(text) if w not in SPOKEN]
        if flagged:
            print(f"  ! {name}: undecided homograph(s) {flagged}")
        await save_speaker_narration(spoken_text(text, SPOKEN, speaker), speaker,
                                     f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3  [{speaker}]")


if __name__ == "__main__":
    asyncio.run(main())
