#!/usr/bin/env python3
"""Narration for build-161-called-of-god — Hebrews 5.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

Hebrews is an epistle. The writer — Paul, by the traditional attribution — is
explaining the priesthood, not quoting Jesus. A red-letter King James Bible
prints no red in Hebrews 5. All three red beats move:
  kv1  Hebrews 5:1  'For every high priest taken from among men...'  RED -> SCRIPTURE
  kv4  Hebrews 5:4  'And no man taketh this honour unto himself...'  RED -> SCRIPTURE
  kv5  Hebrews 5:5  split, see below                                 RED -> SCRIPTURE + GOD

SPLIT — this is the mixed segment in the set. Hebrews 5:5 is two speakers in
one breath:
  kv5  (scripture, blue)  'So also Christ glorified not himself to be made an
                           high priest; but he that said unto him,'
                          — that is the writer, describing.
  gv5  (god, green)       'Thou art my Son, to day have I begotten thee.'
                          — that is the FATHER speaking, quoted from Psalm 2:7.
It was painted entirely red, which made the Father's words to the Son read as
the Son's own words. Green is the correct colour for the quoted half. kv5 keeps
its original id and gv5 is new, and BOTH stay on S7, so the edit the viewer
sees is unchanged — two consecutive beats over one image, no new artwork.

Nothing lifted from paraphrase; n4 through n7 already retell every quoted line.

WHY-LAW: milk. Authority is received, never seized — Aaron was called, and even
Christ was called. The laying-on of hands is shown, not argued.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import GOD, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "In ancient Israel, one man stood between the people and God. The high priest carried their gifts and their sins to the altar, and carried God's holiness back to them. It was the most sacred office a person could hold."),
    # Hebrews 5:1
    ("kv1", SCRIPTURE, "For every high priest taken from among men is ordained for men in things pertaining to God, that he may offer both gifts and sacrifices for sins."),
    ("n2", NARRATOR, "And here is a tender thing. The high priest was not a distant, perfect being. He was a weak man himself, who knew his own failings, and so he could be gentle with everyone else's. He was one of the people, not above them."),
    ("n3", NARRATOR, "But an office that holy could not simply be claimed. However sincere a man was, however gifted, he could not reach out and take it for himself. You cannot hand this to yourself. It has to be given."),
    # Hebrews 5:4
    ("kv4", SCRIPTURE, "And no man taketh this honour unto himself, but he that is called of God, as was Aaron."),
    ("n4", NARRATOR, "Think of how Aaron became high priest. He did not campaign for it or seize it. God named him, and Moses brought him before the people and set him apart. The honour came down to him; it was never something he grasped."),
    ("n5", NARRATOR, "And notice how it was done. Not with a ceremony he arranged for himself, but with another man's hands laid on his head, ordaining him. The authority passed by touch and blessing, from someone who already held it."),
    ("n6", NARRATOR, "Then the holy oil was poured over him, running down, and Aaron was consecrated, set apart, given. Everything about that day says the same thing: this was received, not taken."),
    # Hebrews 5:5
    ("kv5", SCRIPTURE, "So also Christ glorified not himself to be made an high priest; but he that said unto him,"),
    # Hebrews 5:5 (Psalm 2:7)
    ("gv5", GOD, "Thou art my Son, to day have I begotten thee."),
    ("n7", NARRATOR, "And this is the astonishing part. Even the Lord himself did not make himself a high priest. The Father gave him the office and called him to it. If the Son of God received his authority instead of seizing it, then no one else gets to appoint themselves either."),
    ("n8", NARRATOR, "And that is the quiet good news in this verse. The right to speak and act for God has always come the same way: a real call, and hands laid on a bowed head. It is not earned by being impressive. It is given. So the only question left is a hopeful one. Where might God be calling you?"),
    ("card", NARRATOR, "No one hands themselves the things of God. Aaron was called, and even Christ was called. That same authority is still given today, by a call and the laying-on of hands. Where is God calling you?"),
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
