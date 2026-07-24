#!/usr/bin/env python3
"""Narration for build-147-joseph-forgives — Genesis 45.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

Two segments were painted JESUS-RED and neither is Jesus. Both are Joseph — a man in
the story — so both become SCRIPTURE (light blue):
  s1  Genesis 45:5   'Now therefore be not grieved, nor angry with yourselves...'
  s2  Genesis 50:20  'ye thought evil against me; but God meant it unto good...'
Genesis is Old Testament; a red-letter KJV prints none of it red. Ids kept.

Added one lifted line. n1 ended 'Then he told them' and then just cut away — the
single most famous sentence in the chapter was missing entirely:
  s0  Genesis 45:4   'I am Joseph your brother, whom ye sold into Egypt.'
SCRIPTURE, verbatim, and it sits on ST3, the still literally named 'i-am-joseph'.

Added narrator retellings after s0 and s1 (n1b, n1c) per the retelling rule. n3 was
already doing the retelling job for s2, so it is left alone.

LEFT AS NARRATOR: Genesis 45:3 ('doth my father yet live'), and Genesis 50:19 ('Fear
not: for am I in the place of God?'). Both would be good, but the video is short and
adding them would bury the two lines that matter. Nothing here is paraphrased as
scripture — every coloured line is exact KJV.

WHY-LAW: forgiveness here is not pretending the harm was small. Joseph names the sale
out loud — 'whom ye sold into Egypt' — and forgives anyway. That is the milk.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0a", NARRATOR, "Years before, Joseph's own brothers had sold him into slavery out of jealousy."),
    ("n0b", NARRATOR, "Now he was second only to Pharaoh in all Egypt."),
    ("n1", NARRATOR, "When the brothers came begging for food in the famine, they didn't recognize the brother they'd betrayed. Then he sent every Egyptian out of the room, and told them."),
    # Genesis 45:4
    ("s0", SCRIPTURE, "I am Joseph your brother, whom ye sold into Egypt."),
    ("n1b", NARRATOR, "He didn't soften it and he didn't skip it — he said the worst thing they ever did straight to their faces, and then he kept talking."),
    # Genesis 45:5
    ("s1", SCRIPTURE, "Now therefore be not grieved, nor angry with yourselves, that ye sold me hither: for God did send me before you to preserve life."),
    ("n1c", NARRATOR, "Don't tear yourselves up over it, he said. Don't be angry at yourselves that you sold me here. God sent me ahead of you — to keep people alive. He gave them the one thing they could not give themselves: permission to stop hating themselves."),
    ("n2", NARRATOR, "Much later, when their father died and the brothers feared revenge, Joseph spoke the line that closes the wound."),
    # Genesis 50:20
    ("s2", SCRIPTURE, "But as for you, ye thought evil against me; but God meant it unto good, to bring to pass, as it is this day, to save much people alive."),
    ("n3", NARRATOR, "You meant it for evil, he told them — I'm not going to call it anything else. a whole lot of people are still alive. He didn't pretend it hadn't hurt. He saw God's hand turning their evil into rescue."),
    ("card", NARRATOR, "What others meant for harm, God can mean for good. Let it go."),
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
