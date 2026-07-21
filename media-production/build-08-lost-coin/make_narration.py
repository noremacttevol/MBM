#!/usr/bin/env python3
"""Narration for build-08-lost-coin — Luke 15.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

Luke 15:8-10. A parable, so a red-letter KJV inks the whole thing - including
the woman's own line inside it and Jesus's frame around her. j1 and j2 stay RED,
and two more verses of the same parable that the video only paraphrased are lifted
out and join them in red:
  jv8   Luke 15:8   'Either what woman having ten pieces of silver...'
  jv9a  Luke 15:9a  'And when she hath found it, she calleth her friends and her
        neighbours together, saying,' - Jesus's own frame inside the parable, and
        it sits on the beat immediately before j1, the line it introduces.
NOTE: the woman in this parable is NOT a `woman` beat. She is a character Jesus
invented inside a story he is telling; the words are his, and a red-letter Bible
prints them red. Pink is for women the Bible records actually speaking.
This build had NO closing-card narration - the card was silent text on cream. A
`card` segment is added carrying the card's existing words, so the card is spoken
like every other build in the library and TAIL can be derived from it.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "When Jesus wanted to show how God feels about one lost soul, he didn't talk about crowds. He told this story."),
    # Luke 15:8
    ("jv8", JESUS, "Either what woman having ten pieces of silver, if she lose one piece, doth not light a candle, and sweep the house, and seek diligently till she find it?"),
    ("n1", NARRATOR, "A woman has ten coins. She loses one."),
    ("n2a", NARRATOR, "She lights a lamp. She sweeps the whole house."),
    ("n2b", NARRATOR, "She searches carefully — not casually, carefully — until she finds it."),
    # Luke 15:9
    ("jv9a", JESUS, "And when she hath found it, she calleth her friends and her neighbours together, saying,"),
    # Luke 15:9
    ("j1", JESUS, "Rejoice with me; for I have found the piece which I had lost."),
    ("n3", NARRATOR, "Then she calls her neighbors and friends to celebrate."),
    ("n4", NARRATOR, "One coin. Out of ten. The joy is disproportionate to the value of the coin."),
    # Luke 15:10
    ("j2", JESUS, "Likewise, I say unto you, there is joy in the presence of the angels of God over one sinner that repenteth."),
    ("n5", NARRATOR, "Over one. Not a crowd. One."),
    ("card", NARRATOR, "Have you ever felt like the thing that got lost, rather than the one doing the searching?"),
]

# Homographs this build decides for itself (never auto-replaced globally).
# calleth (Cameron complaint #8, 2026-07-21, second denial): plain "calleth" in
# the jesus voice (EricNeural -22%) round-trips isolated as "Kalloth" — the
# suffix vowel goes wrong. A/B 2026-07-21: "kawleth" is the only candidate that
# both keeps the in-sentence round-trip at 100% ("calleth") and fixes the
# isolated reading ("Colith" = KAW-lith). One word, no hyphens, per the law.
SPOKEN = {"calleth": "kawleth"}


async def main():
    os.makedirs("audio", exist_ok=True)
    for name, speaker, text in SEGMENTS:
        flagged = [w for w in audit(text) if w not in SPOKEN]
        if flagged:
            print(f"  ! {name}: undecided homograph(s) {flagged}")
        await save_speaker_narration(spoken_text(text, SPOKEN), speaker,
                                     f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3  [{speaker}]")


if __name__ == "__main__":
    asyncio.run(main())
