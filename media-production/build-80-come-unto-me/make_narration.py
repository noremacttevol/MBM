#!/usr/bin/env python3
"""Narration for build-80-come-unto-me — Matthew 11.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

ALL THREE STAY RED, AND THAT IS THE RIGHT ANSWER. Matthew 11:28-30 is Jesus
speaking in the flesh from start to finish and a red-letter KJV prints every word
of it red. There was nothing here to move. Every line was checked anyway rather
than assumed, because this build is the one that would look most like a bulk
re-paint if it came back untouched:
  j1  Matthew 11:28  'Come unto me, all ye that labour and are heavy laden, and I
      will give you rest.'
  j2  Matthew 11:29  'Take my yoke upon you, and learn of me; for I am meek and
      lowly in heart: and ye shall find rest unto your souls.'
  j3  Matthew 11:30  'For my yoke is easy, and my burden is light.'
All three verbatim, all three ids kept, no splits needed -- none of them carries
Matthew's framing inside it. j2 and j3 are one continuous sentence in the KJV and
are deliberately left back to back, with one retelling covering both after j3.

RETELLINGS ADDED -- the whole build was Old English with almost no plain-English
landing, which for the gentlest offer in the Gospels is the worst place to leave
it untranslated:
  n0c  after j1, on S3.
  n1b  after j3, on S6, covering j2 and j3 together.
n1's explanation of what a yoke actually is was already doing part of this job
and was left exactly as it was.

NO GREEN: the Father is spoken about elsewhere in Matthew 11 but does not speak
in verses 28 to 30.

WOMEN: Matthew 11:28-30 records no woman speaking. There is no dialogue in the
passage at all besides Jesus. Nothing added; nothing invented.

WHY-LAW: a yoke is built for two, and he is offering to take the other side.
Milk: he never promised you an empty back — he promised you would not carry it
by yourself.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0a", NARRATOR, "To a crowd of people worn down by work, by rules, by just getting through the day,"),
    ("n0b", NARRATOR, "Jesus made one of the gentlest offers ever spoken."),
    # Matthew 11:28
    ("j1", JESUS, "Come unto me, all ye that labour and are heavy laden, and I will give you rest."),
    ("n0c", NARRATOR, "Come to me, all of you who are worn out and carrying too much — and I will give you rest. He does not say come once you have it handled. He says come while you are still under it."),
    ("n1", NARRATOR, "A yoke was the wooden beam that let two oxen pull a load together, so no single animal carried it alone."),
    # Matthew 11:29
    ("j2", JESUS, "Take my yoke upon you, and learn of me; for I am meek and lowly in heart: and ye shall find rest unto your souls."),
    # Matthew 11:30
    ("j3", JESUS, "For my yoke is easy, and my burden is light."),
    ("n1b", NARRATOR, "Take my yoke on you, he said, and learn from me, because I am gentle and I am humble — and you will find rest for your soul. He is not handing you a heavier beam. He is stepping into the empty side of the one you are already pulling."),
    ("n2a", NARRATOR, "He wasn't promising a life with nothing to carry."),
    ("n2b", NARRATOR, "He was promising to get under the load with you, so it never has to be carried alone again."),
    ("card", NARRATOR, "Whatever you've been carrying by yourself — he's offering to take the other side of it. Come."),
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
