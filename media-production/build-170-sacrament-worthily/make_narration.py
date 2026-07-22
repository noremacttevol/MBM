#!/usr/bin/env python3
"""Narration for build-170-sacrament-worthily — 1 Corinthians 11.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

kv24 and kv25 both move JESUS-RED -> SCRIPTURE (light blue). Two lines out of
red.

This is the hardest call in my set and worth stating plainly. 1 Corinthians
11:24-25 is Paul quoting what the Lord said at the last supper, and some
red-letter editions do ink the quoted clauses red. But the governing rule for
this pass is that the epistles are the writer speaking — this is Paul's letter,
recounting what he received, not Jesus speaking in the flesh in the narrative.
SPEAKER-LAW's epistle rule and validate_plan.py both make `jesus` invalid in 1
Corinthians, and Cameron's complaint was exactly this class of case. So: light
blue, whole verse. Flagging it as the one judgement call in my set worth a look.

Because both halves of each verse land on the same speaker, neither verse was
split. Splitting 'And when he had given thanks, he brake it, and said,' from
'Take, eat: this is my body' would produce two segments of the identical colour
and gain nothing while risking the music beds. Left whole.

Two verses lifted out of narrator paraphrase, both Paul, both SCRIPTURE:
  s26  1 Cor 11:26  'For as often as ye eat this bread...'
  s28  1 Cor 11:28  'But let a man examine himself...'
Each sits immediately before the existing narrator beat that retells it — s26
before n4 (the looking-back-and-forward beat), s28 before n5 (Paul's gentle ask).
s28 is the verse the whole build is named for, and it belongs on screen in
Paul's own words rather than in summary.

All original ids kept. New ids are s26 and s28 only. New beats reuse S5 and S6;
no new artwork.

MILK: verse 28 is quoted and then softened, never sharpened. The narration says
plainly that the examination is not to keep anyone away. Nothing about
worthiness is argued — the invitation stays open and the verse stands on its
own.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "Paul was handing on something sacred that he had received himself: on the very night he was betrayed, at supper with his friends, the Master took a simple loaf of bread into his hands and gave thanks over it."),
    # 1 Corinthians 11:24
    ("kv24", SCRIPTURE, "And when he had given thanks, he brake it, and said, Take, eat: this is my body, which is broken for you: this do in remembrance of me."),
    ("n2", NARRATOR, "Then he lifted the cup. This one, he said, was the sign of a new covenant — a solemn promise sealed between God and his people, and offered freely to them."),
    # 1 Corinthians 11:25
    ("kv25", SCRIPTURE, "After the same manner also he took the cup, when he had supped, saying, This cup is the new testament in my blood: this do ye, as oft as ye drink it, in remembrance of me."),
    ("n3", NARRATOR, "Ever since, his people have taken that same bread and that same cup together, quietly, reverently — a small, holy act of remembering the One who gave everything for them."),
    # 1 Corinthians 11:26
    ("s26", SCRIPTURE, "For as often as ye eat this bread, and drink this cup, ye do shew the Lord's death till he come."),
    ("n4", NARRATOR, "And it looks in two directions at once. Every time we take it, we are remembering a sacrifice already made, and we are looking forward, in hope, to the day he returns."),
    # 1 Corinthians 11:28
    ("s28", SCRIPTURE, "But let a man examine himself, and so let him eat of that bread, and drink of that cup."),
    ("n5", NARRATOR, "Paul asked for just one thing beforehand, and he asked it gently: that each person pause and look honestly into his own heart, and come sincerely. Not to keep anyone away, but so the moment stays real and tender."),
    ("n6", NARRATOR, "Here is the quiet study gem. This is why it is done again and again, and never just once. It is a covenant renewed — week after week, a fresh chance to be made clean, to set down the past and begin again."),
    ("n7", NARRATOR, "And a place at that table is kept for you. Not for the perfect, but for the sincere — for anyone willing to come and remember. When the bread and the cup are offered to you, will you come to the table?"),
    ("card", NARRATOR, "The bread and the cup are taken in remembrance — a covenant renewed again and again, a fresh chance to be made clean. Not for the perfect, but for the sincere. When they are offered to you, will you come to the table?"),
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
