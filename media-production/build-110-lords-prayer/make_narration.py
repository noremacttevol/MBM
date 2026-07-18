#!/usr/bin/env python3
"""Narration audio for Video #110 — The Lord's Prayer: "Our Father" (Matthew 6).

Narrator: en-US-AndrewNeural. Jesus: en-US-ChristopherNeural (exact KJV only).

Jesus's KJV lines (Christopher, cream italic):
  jv9   Matt 6:9-10   "Our Father which art in heaven, Hallowed be thy name. Thy
                       kingdom come. Thy will be done in earth, as it is in heaven." — silence 1
  jv11  Matt 6:11-12  "Give us this day our daily bread. And forgive us our debts, as
                       we forgive our debtors."
  jv13  Matt 6:13     "And lead us not into temptation, but deliver us from evil: For
                       thine is the kingdom, and the power, and the glory, for ever.
                       Amen." — silence 2

WHY-LAW: when the disciples asked how to pray, Jesus did not give them a complicated
ritual. He gave them a family word: Father. The whole prayer flows from that one
astonishing permission — that the God of the universe invites you to speak to him the
way a trusted child speaks to a good dad: honestly, simply, about bread and forgiveness
and being kept safe. Milk framing: you do not need fancy words; you need only to begin,
"Our Father." An invitation, never a threat.

HOMOGRAPH EAR-CHECK: 'debts' read /dets/ (silent b — verify). No other high-risk words.
NUMBER-STRESS LAW obeyed.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"
JESUS = "en-US-ChristopherNeural"

SEGMENTS = [
    ("n1", NARRATOR, "-20%", "-4Hz",
     "One day his followers asked him a simple question: teach us how to pray. They "
     "expected, maybe, a technique. A ritual. Instead, Jesus gave them a family word.", None),
    # jv9 — Our Father... — silence 1
    ("jv9", JESUS, "-26%", "-6Hz",
     "Our Father which art in heaven, Hallowed be thy name. Thy kingdom come. Thy will be "
     "done in earth, as it is in heaven.", None),
    ("n2", NARRATOR, "-22%", "-4Hz",
     "Father. Not a distant judge. Not a force. A Father you belong to. And the very "
     "first thing you long for, once you know him, is not for yourself at all — that his "
     "name be honoured, and his good kingdom come, everywhere.", None),
    # jv11 — daily bread, forgive
    ("jv11", JESUS, "-24%", "-6Hz",
     "Give us this day our daily bread. And forgive us our debts, as we forgive our "
     "debtors.", None),
    ("n3", NARRATOR, "-22%", "-4Hz",
     "Then the plain, honest things. Bread — it is fine to ask for the ordinary needs of "
     "the day. And forgiveness — asked for, and passed on. We receive mercy with the same "
     "hands we use to give it away.", None),
    # jv13 — deliver us — silence 2
    ("jv13", JESUS, "-26%", "-6Hz",
     "And lead us not into temptation, but deliver us from evil: For thine is the "
     "kingdom, and the power, and the glory, for ever. Amen.", None),
    ("n4", NARRATOR, "-22%", "-4Hz",
     "Keep me safe. Lead me away from what would harm me. And it ends where it began — "
     "with him: the kingdom, the power, the glory, all his, for ever. Short. Honest. "
     "Nothing showy.", None),
    ("n5", NARRATOR, "-22%", "-4Hz",
     "Because Jesus had just warned them: prayer is not a performance. Not many clever "
     "words, not standing on a corner to be admired. The prayer God loves most may be the "
     "simplest one a child ever whispered.", None),
    ("n6", NARRATOR, "-22%", "-4Hz",
     "That is really all it is. Not a speech to impress heaven. A child, climbing into "
     "the lap of a good Father, and simply talking to him.", None),
    ("n7", NARRATOR, "-24%", "-4Hz",
     "So you do not need the right words. You only need to begin. And the beginning is "
     "just two words, the ones he gave them first of all: Our Father.", None),
    ("card", NARRATOR, "-26%", "-4Hz",
     "Jesus said you can talk to God the way a child talks to a good Father — simply, "
     "honestly, no performance. It starts with two words: Our Father. What would you say "
     "to him, if you began today?", None),
]


async def main():
    for name, voice, rate, pitch, text, cap in SEGMENTS:
        await save_narration(text, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")


if __name__ == "__main__":
    import os
    os.makedirs("audio", exist_ok=True)
    asyncio.run(main())
