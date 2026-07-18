#!/usr/bin/env python3
"""Narration audio for Video #109 — Ask, Seek, Knock (Matthew 7:7-11).

Narrator: en-US-AndrewNeural. Jesus: en-US-ChristopherNeural (exact KJV only).

Jesus's KJV lines (Christopher, cream italic):
  jv7   Matt 7:7   "Ask, and it shall be given you; seek, and ye shall find; knock,
                    and it shall be opened unto you:" — sacred silence 1
  jv8   Matt 7:8   "For every one that asketh receiveth..."
  jv11  Matt 7:11  "If ye then, being evil, know how to give good gifts unto your
                    children, how much more shall your Father which is in heaven give
                    good things to them that ask him?" — sacred silence 2

WHY-LAW: prayer is not prying open the hand of a reluctant God. Jesus says: ask, seek,
knock — words that get more personal and more persistent — and then he compares God to a
loving human father who would never hand his hungry child a stone. If flawed human
parents give good gifts, HOW MUCH MORE your Father in heaven. Milk framing: you are
invited to ask, simply and boldly, because the One you ask is good and glad to give. An
invitation, never a threat.

HOMOGRAPH EAR-CHECK: no high-risk homographs. NUMBER-STRESS LAW obeyed.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"
JESUS = "en-US-ChristopherNeural"

SEGMENTS = [
    ("n1", NARRATOR, "-20%", "-4Hz",
     "People have always wondered how prayer really works. Do you have to say it just "
     "right? Wear God down? Jesus, teaching on a hillside, made it startlingly simple.", None),
    # jv7 — ask, seek, knock — silence 1
    ("jv7", JESUS, "-26%", "-6Hz",
     "Ask, and it shall be given you; seek, and ye shall find; knock, and it shall be "
     "opened unto you:", None),
    ("n2", NARRATOR, "-22%", "-4Hz",
     "Three words, and each one is warmer and more personal than the last. Ask — like a "
     "child who simply puts out its hands, trusting, expecting good.", None),
    ("n3", NARRATOR, "-22%", "-4Hz",
     "Seek — more than a word now; it is getting up and searching, patient and hopeful, "
     "sure that what you are looking for is really there to be found.", None),
    # jv8 — every one that asketh receiveth
    ("jv8", JESUS, "-24%", "-6Hz",
     "For every one that asketh receiveth; and he that seeketh findeth; and to him that "
     "knocketh it shall be opened.", None),
    ("n4", NARRATOR, "-22%", "-4Hz",
     "Knock — and keep knocking — on a door you cannot yet see behind. And the promise "
     "is that the door does open. Not maybe. Not for the specially worthy. Every one who "
     "asks, receives.", None),
    ("n5", NARRATOR, "-22%", "-4Hz",
     "Then Jesus makes it personal with a picture from any home. A child asks its father "
     "for bread. What kind of father hands his hungry child a stone instead? Or a snake "
     "when he asks for a fish? No father you would trust.", None),
    # jv11 — how much more — silence 2
    ("jv11", JESUS, "-26%", "-6Hz",
     "If ye then, being evil, know how to give good gifts unto your children, how much "
     "more shall your Father which is in heaven give good things to them that ask him?", None),
    ("n6", NARRATOR, "-22%", "-4Hz",
     "How much more. If flawed, tired, imperfect parents still love to give their kids "
     "good things — how much more does a perfect Father delight to give to you? Prayer is "
     "not twisting God's arm. It is a child asking a good Father who is glad to be asked.", None),
    ("n7", NARRATOR, "-24%", "-4Hz",
     "So the invitation is just this: ask. Not perfectly. Not impressively. Simply, "
     "honestly, like a child. The Father is not reluctant. He is leaning in, glad to "
     "hear your voice.", None),
    ("card", NARRATOR, "-26%", "-4Hz",
     "Ask, seek, knock. Jesus says your Father in heaven is far kinder than the best "
     "parent you can imagine, and glad to be asked. Is there something you have been "
     "afraid to ask him for?", None),
]


# SPOKEN-OVERRIDE (Cameron denial #109, 2026-07-18): "kinder" was read the German
# way (KIN-der, as in kindergarten). It is the English comparative of "kind" — "She
# is kinder than him" — so it must be KYNE-der. Respell ONLY the spoken word to
# "kynder". The caption still reads the exact word "kinder" (build.py takes caption
# text from SEGMENTS, never from SPOKEN).
SPOKEN = {
    "card": ("Ask, seek, knock. Jesus says your Father in heaven is far kynder than the best "
             "parent you can imagine, and glad to be asked. Is there something you have been "
             "afraid to ask him for?"),
}


async def main():
    for name, voice, rate, pitch, text, cap in SEGMENTS:
        tts_text = SPOKEN.get(name, text)
        await save_narration(tts_text, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")


if __name__ == "__main__":
    import os
    os.makedirs("audio", exist_ok=True)
    asyncio.run(main())
