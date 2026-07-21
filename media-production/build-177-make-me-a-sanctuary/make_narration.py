#!/usr/bin/env python3
"""Narration for build-177-make-me-a-sanctuary — Exodus 25.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

The one scripture beat was painted JESUS-RED. Exodus is Old Testament, so it
cannot be red - and it is the LORD speaking in first person, which makes it
GREEN, not blue:
  s1  Exodus 25:8  'And let them make me a sanctuary; that I may dwell
                    among them.'                                   RED -> GOD
'Make ME a sanctuary, that I may dwell among them' - that is Jehovah, the
premortal Christ, talking about himself. Straightforward green.

NO SPLIT on s1. The whole segment is Deity's own words with no narrator clause
attached; Moses's 'And the LORD spake unto Moses, saying' is not in this
segment, so there is nothing to peel off.

LIFTED ONE VERSE out of narrator paraphrase:
  g22  Exodus 25:22  'And there I will meet with thee, and I will commune
                      with thee from above the mercy seat...'      NEW, god
n2a already listed the ark and the table and the lampstand, and n2b already said
'every detail meant to say: I am near' - but the viewer never heard God actually
say it. Exodus 25:22 is that sentence, in his own first person, and it is the
warmest line in the chapter. Quoted through 'the ark of the testimony' - a clean
clause boundary mid-verse, verbatim to that point, the same way the reference
plan handles Genesis 18:32a. g22 sits on S3 with n2a so no artwork changes.

ADDED two narrator retellings, both required by the retelling rule:
  n0b  retells Exodus 25:8 immediately after it, on S2 with s1.
  n2r  retells Exodus 25:22 immediately after it, on S4 with n2b.
Before this, s1's Old English had to wait until n1a/n1b - four beats later - for
any plain-English landing.

Nothing left as paraphrase from uncertainty.

WHY-LAW: milk. God asked for a tent, not a fortress, and he asked for it in the
middle of the camp. The whole point is nearness - he wanted to live where his
people lived. Nothing on screen argues about temples; the tent says it.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import GOD, NARRATOR

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "While Israel camped in the wilderness, the LORD gave Moses a strange instruction — have the people build me a sanctuary."),
    # Exodus 25:8
    ("s1", GOD, "And let them make me a sanctuary; that I may dwell among them."),
    ("n0b", NARRATOR, "Build me a place, God said, so that I can live right there with you. Not a palace on a far-off hill. A tent, pitched in the middle of the camp, with everybody else's tents circled around it."),
    ("n2a", NARRATOR, "He told them exactly how — the ark, the table, the lampstand —"),
    # Exodus 25:22
    ("g22", GOD, "And there I will meet with thee, and I will commune with thee from above the mercy seat, from between the two cherubims which are upon the ark of the testimony."),
    ("n2r", NARRATOR, "That is what all the measurements were for. There, God said — right there, above that lid, between those two carved angels — that is where I will meet you and talk with you. He gave them an address."),
    ("n2b", NARRATOR, "every detail meant to say: I am near."),
    ("n1a", NARRATOR, "Not for his sake. For theirs."),
    ("n1b", NARRATOR, "So that he could dwell among them in the middle of their ordinary days."),
    ("n3a", NARRATOR, "The pattern was carried by a people on the move,"),
    ("n3b", NARRATOR, "yet the promise was fixed — God with his people."),
    ("n4", NARRATOR, "Centuries later that promise would take a face. But here it begins as a tent in the desert, God pitching his tent beside them."),
    ("card", NARRATOR, "He wanted to live among his people then. He wants to live among you now."),
]

# Homographs this build decides for itself (never auto-replaced globally).
SPOKEN = {}


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
