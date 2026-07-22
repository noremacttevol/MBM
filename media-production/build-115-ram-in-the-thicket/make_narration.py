#!/usr/bin/env python3
"""Narration for build-115-ram-in-the-thicket — Genesis 22.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

Two segments were painted JESUS-RED. Both are Jehovah speaking in Genesis 22 — the
premortal Christ, before he came in the flesh — so a red-letter KJV leaves them black
and this pass makes them GOD (green). Ids kept exactly:
  jv12  Genesis 22:12
  jv17  Genesis 22:17
Note verse 12 is spoken by 'the angel of the LORD' but in the first person — 'thou hast
not withheld thy son... from me' — so it is Deity, and green is right.

Added four lifted lines that were buried in narrator paraphrase, all verbatim KJV:
  s7   Gen 22:7   Isaac  — 'Behold the fire and the wood: but where is the lamb...'   SCRIPTURE
  s8   Gen 22:8   Abraham— 'My son, God will provide himself a lamb...'               SCRIPTURE
  jv11 Gen 22:11  the LORD — 'Abraham, Abraham.'                                      GOD
  s11  Gen 22:11  Abraham— 'Here am I.'                                               SCRIPTURE
Isaac and Abraham are men in the story, so light blue, never red. n4 keeps its id and
is rewritten from paraphrase-of-the-dialogue into the retelling that follows it.

Added n7b as the retelling for jv17, which previously had none — n8 changes subject
instead of restating the blessing.

LEFT AS NARRATOR: Genesis 22:14, the naming of the place Jehovahjireh. I know the
verse, but the KJV wording ('In the mount of the LORD it shall be seen') needs its own
explanation and n7 already carries the naming in plain English. Also left as narrator:
God's opening command in 22:2. Nothing is approximated — every coloured line above is
exact King James text a viewer can look up.

WHY-LAW: the point is God PROVIDES, not God takes. Every added beat pushes that way —
the boy's question and the father's answer are the thesis of the story, and the video
was only paraphrasing them.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import GOD, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "It is one of the hardest stories in the Bible, and one of the most misread. God asks Abraham for the thing he loves most in all the world — his son. And Abraham, trusting God completely, sets out."),
    ("n2", NARRATOR, "Now watch closely, because everything the story means is in how it ends. Abraham believed, somehow, that God was good — that whatever this was, God could be trusted with his boy. So he walked, and he trusted, and he did not let go of that."),
    ("n3", NARRATOR, "Father and son climbed the mountain together, the boy carrying the wood, the old man carrying the fire and a heart full of faith and ache. And as they climbed, the child asked the question that hangs over the whole story."),
    # Genesis 22:7
    ("s7", SCRIPTURE, "Behold the fire and the wood: but where is the lamb for a burnt offering?"),
    # Genesis 22:8
    ("s8", SCRIPTURE, "My son, God will provide himself a lamb for a burnt offering."),
    ("n4", NARRATOR, "Father, the boy said — we've got the fire and we've got the wood, but where's the lamb? And Abraham answered with the line that turns out to be the whole point of the story: my son, God will provide the lamb himself."),
    ("n5", NARRATOR, "God will provide. Abraham did not fully understand how. He only trusted that the God he loved would not, in the end, ask him to lose his son. And at the very last moment, at the edge of everything, heaven broke open."),
    # Genesis 22:11
    ("jv11", GOD, "Abraham, Abraham."),
    # Genesis 22:11
    ("s11", SCRIPTURE, "Here am I."),
    ("n5b", NARRATOR, "His name, twice, out of the sky. And the old man answered the way he always had — here I am. Then came the words that ended it."),
    # Genesis 22:12
    ("jv12", GOD, "Lay not thine hand upon the lad, neither do thou any thing unto him: for now I know that thou fearest God."),
    ("n6", NARRATOR, "Don't lay a hand on the boy. Don't do anything to him at all. Stop. God never wanted the child. He never did. He stopped Abraham's hand, and right there, caught in a thicket, was a ram — God's own provision, ready all along. The boy was safe. He was always going to be safe."),
    ("n7", NARRATOR, "And the old father gathered his living son into his arms and held him, and wept, and would not let go. God had provided. Abraham named that place The Lord Will Provide, and the name has echoed down every generation since."),
    # Genesis 22:17
    ("jv17", GOD, "In blessing I will bless thee, and in multiplying I will multiply thy seed as the stars of the heaven, and as the sand which is upon the sea shore."),
    ("n7b", NARRATOR, "I will bless you and bless you again, God told him. Your family will outnumber the stars over your head and the sand under your feet. The man who was willing to hand back his only son was promised more children than he could count."),
    ("n8", NARRATOR, "This was never a story about a God who takes. It is about a God who provides — who steps in at the last moment with what we could never provide ourselves. Centuries later, on another hill nearby, God would provide a Lamb again — this time, his own. The Lord will provide. He always has."),
    ("card", NARRATOR, "God never wanted the child; he wanted to show he provides. He stopped the hand and gave the ram, and the boy went home safe. Where do you most need to trust that the Lord will provide?"),
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
