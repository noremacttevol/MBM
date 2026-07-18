#!/usr/bin/env python3
"""Narration audio for Video #115 — The Ram in the Thicket (Genesis 22).

Narrator: en-US-AndrewNeural. The divine voice: en-US-ChristopherNeural (exact KJV only).
Abraham's 'God will provide himself a lamb' and 'Jehovah-jireh' are voiced by the NARRATOR;
God's own KJV (the staying voice and the blessing) renders cream-italic.

God's KJV lines (Christopher, cream italic):
  jv12  Gen 22:12  "Lay not thine hand upon the lad, neither do thou any thing unto him:
                    for now I know that thou fearest God..." — the rescue (sacred silence 1)
  jv17  Gen 22:17  "in blessing I will bless thee... and thy seed shall possess the gate
                    of his enemies" — the promise (sacred silence 2)

WHY-LAW (CONTENT-CARE §C / #166): the child is NEVER in the rendered image and the narration
NEVER lingers on the threat. The point of the whole story is the PROVISION — "God himself
provides the lamb." GOD NEVER WANTED THE CHILD. He stopped Abraham, and gave a ram in the
thicket, and the boy went home safe. This is the God who provides what we cannot, and who
one day would provide the true Lamb himself. Milk framing: God is not a taker of what you
love — he is the Provider who steps in. An invitation to trust, never a threat.

HOMOGRAPH EAR-CHECK: no high-risk homographs. NUMBER-STRESS LAW obeyed.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"
GOD = "en-US-ChristopherNeural"

SEGMENTS = [
    ("n1", NARRATOR, "-20%", "-4Hz",
     "It is one of the hardest stories in the Bible, and one of the most misread. God asks "
     "Abraham for the thing he loves most in all the world — his son. And Abraham, "
     "trusting God completely, sets out.", None),
    ("n2", NARRATOR, "-22%", "-4Hz",
     "Now watch closely, because everything the story means is in how it ends. Abraham "
     "believed, somehow, that God was good — that whatever this was, God could be trusted "
     "with his boy. So he walked, and he trusted, and he did not let go of that.", None),
    ("n3", NARRATOR, "-22%", "-4Hz",
     "Father and son climbed the mountain together, the boy carrying the wood, the old man "
     "carrying the fire and a heart full of faith and ache. And as they climbed, the child "
     "asked the question that hangs over the whole story.", None),
    ("n4", NARRATOR, "-22%", "-4Hz",
     "Father, he said — here is the wood and the fire, but where is the lamb? And Abraham "
     "answered with the line that turns out to be the whole point: my son, God will provide "
     "himself a lamb.", None),
    ("n5", NARRATOR, "-22%", "-4Hz",
     "God will provide. Abraham did not fully understand how. He only trusted that the God "
     "he loved would not, in the end, ask him to lose his son. And at the very last "
     "moment, at the edge of everything, heaven broke open.", None),
    # jv12 — the rescue — silence 1
    ("jv12", GOD, "-26%", "-6Hz",
     "Lay not thine hand upon the lad, neither do thou any thing unto him: for now I know "
     "that thou fearest God.", None),
    ("n6", NARRATOR, "-22%", "-4Hz",
     "Stop. God never wanted the child. He never did. He stopped Abraham's hand, and right "
     "there, caught in a thicket, was a ram — God's own provision, ready all along. The "
     "boy was safe. He was always going to be safe.", None),
    ("n7", NARRATOR, "-22%", "-4Hz",
     "And the old father gathered his living son into his arms and held him, and wept, and "
     "would not let go. God had provided. Abraham named that place The Lord Will Provide, "
     "and the name has echoed down every generation since.", None),
    # jv17 — the promise — silence 2
    ("jv17", GOD, "-26%", "-6Hz",
     "In blessing I will bless thee, and in multiplying I will multiply thy seed as the "
     "stars of the heaven, and as the sand which is upon the sea shore.", None),
    ("n8", NARRATOR, "-24%", "-4Hz",
     "This was never a story about a God who takes. It is about a God who provides — who "
     "steps in at the last moment with what we could never provide ourselves. Centuries "
     "later, on another hill nearby, God would provide a Lamb again — this time, his own. "
     "The Lord will provide. He always has.", None),
    ("card", NARRATOR, "-26%", "-4Hz",
     "God never wanted the child; he wanted to show he provides. He stopped the hand and "
     "gave the ram, and the boy went home safe. Where do you most need to trust that the "
     "Lord will provide?", None),
]


async def main():
    for name, voice, rate, pitch, text, cap in SEGMENTS:
        await save_narration(text, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")


if __name__ == "__main__":
    import os
    os.makedirs("audio", exist_ok=True)
    asyncio.run(main())
