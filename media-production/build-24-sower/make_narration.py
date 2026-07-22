#!/usr/bin/env python3
"""Narration for build-24-sower — Matthew 13.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

STAYED RED: all three existing red beats are Jesus in the flesh telling and
explaining a parable, and a red-letter KJV prints all three.
  j1  Matthew 13:3   'Behold, a sower went forth to sow;'
  j3  Matthew 13:23  'But he that received seed into the good ground...'
  j2  Matthew 13:9   'Who hath ears to hear, let him hear.'

THE FRAMING SPLIT. Matthew 13:3 reads in full: 'And he spake many things unto
them in parables, saying, Behold, a sower went forth to sow;'. Everything before
'Behold' is Matthew writing, and a red-letter KJV leaves it black. The build had
that frame only as modern paraphrase in n2, so the verse is now split properly,
BOTH HALVES ON THE SAME STILL S2 -- no new artwork, and the edit the viewer sees
is unchanged:
  s3  Matthew 13:3  'And he spake many things unto them in parables, saying,'
      SCRIPTURE, light blue -- narration inside the Gospels is never red.
  j1  Matthew 13:3  'Behold, a sower went forth to sow;'  JESUS, red, unchanged.
n3 was already the retelling and is untouched.

ADDED RED, INSIDE THE PARABLE. Two of the four soils were told only in
paraphrase. Both are Jesus's own words:
  j4  Matthew 13:4  'And when he sowed, some seeds fell by the way side, and the
      fowls came and devoured them up:'   -- n4 keeps its text and now retells it.
  j8  Matthew 13:8  'But other fell into good ground, and brought forth fruit,
      some an hundredfold, some sixtyfold, some thirtyfold.'
      -- n9 keeps its text and now retells it, and j3's explanation lands right
      after on the same still.
The stony ground and the thorns are left in the storyteller's voice on purpose:
putting all four soils in Old English back to back would turn the middle of the
video into a recitation. Two verbatim, two retold, alternating.

WOMEN: Matthew 13:1-23 records no woman speaking. Nothing added; nothing invented.

NO GREEN: no voice from heaven in Matthew 13.

PRONUNCIATION: 'sow' and 'sowed' are on the SPEAKER-LAW homograph list -- the
seed-scattering word rhymes with 'so', not with 'cow'. Respelled in `spoken`;
the captions keep the true spelling. 'sower' is left alone -- it already reads
correctly and a bad respelling is worse than none.

WHY-LAW: the farmer did not skip the hard path or the rocks. He threw seed
everywhere, hoping. And ground can change.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "So many people crowded the shore to hear Jesus that he pushed a small boat out onto the water and taught them from there, the whole hillside listening."),
    ("n2", NARRATOR, "And he told them a story about a farmer, and four kinds of ground."),
    # Matthew 13:3
    ("s3", SCRIPTURE, "And he spake many things unto them in parables, saying,"),
    # Matthew 13:3
    ("j1", JESUS, "Behold, a sower went forth to sow;"),
    ("n3", NARRATOR, "A farmer went out to scatter his seed. He did not measure it out grain by grain. He flung it wide, across every kind of ground, hoping all of it would grow."),
    # Matthew 13:4
    ("j4", JESUS, "And when he sowed, some seeds fell by the way side, and the fowls came and devoured them up:"),
    ("n4", NARRATOR, "Some fell on the hard path, packed down by every foot that had ever walked it. It never sank in, and the birds came and ate it."),
    ("n5", NARRATOR, "That, he said, is a heart so hardened that the word never gets below the surface before it is snatched away."),
    ("n6", NARRATOR, "Some fell on thin soil over rock. It sprang up fast, green and hopeful, but it had no root, and when the sun grew hot it withered."),
    ("n7", NARRATOR, "That is the heart that says yes with joy, but has nothing underneath to hold it when things get hard."),
    ("n8", NARRATOR, "Some fell among thorns. The seed grew, but so did the weeds, and the worries and wants of this life crowded in and choked it before it could bear anything."),
    # Matthew 13:8
    ("j8", JESUS, "But other fell into good ground, and brought forth fruit, some an hundredfold, some sixtyfold, some thirtyfold."),
    ("n9", NARRATOR, "But some fell on good ground, open and soft and ready. It took root, and grew, and gave back a harvest many times over."),
    # Matthew 13:23
    ("j3", JESUS, "But he that received seed into the good ground is he that heareth the word, and understandeth it; which also beareth fruit, and bringeth forth, some an hundredfold, some sixty, some thirty."),
    ("n10", NARRATOR, "The good ground is simply the heart that hears him, takes it in, and holds on. And it gives back far more than was ever put in."),
    ("n11", NARRATOR, "Notice the farmer did not skip the hard path or the rocky places. He threw seed everywhere, on every heart, hoping. That is how generous God is with his word."),
    # Matthew 13:9
    ("j2", JESUS, "Who hath ears to hear, let him hear."),
    ("n12", NARRATOR, "And ground can change. A hard path can be broken up. Rocky soil can be cleared. That is how good he is. He keeps sowing, and he never stops hoping your heart will be the good ground."),
    ("card", NARRATOR, "None of these soils are fixed forever. What is the soil of your heart today?"),
]

# Homographs this build decides for itself (never auto-replaced globally).
SPOKEN = {
    "sow": "soh",
    "sowed": "sohd",
}


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
