#!/usr/bin/env python3
"""Narration audio for Video #107 — John the Baptist's Doubt (Matthew 11:2-11).

Narrator: en-US-AndrewNeural. Jesus: en-US-ChristopherNeural (exact KJV only). John's
question is voiced by the narrator (white caption); Jesus's answer renders cream-italic.

Jesus's KJV lines (Christopher, cream italic):
  jv4  Matt 11:4-5  "Go and shew John again those things which ye do hear and see..."
                    — the answer of evidence (sacred silence 1)
  jv6  Matt 11:6    "And blessed is he, whosoever shall not be offended in me." — silence 2

WHY-LAW: even John — the greatest of the prophets, the fearless one who pointed Jesus
out — sat in a prison cell and doubted. And Jesus did not scold him or shame him. He
sent back gentleness and evidence: look at what love is actually doing — the blind see,
the poor are lifted. Milk framing: honest doubt is safe with Jesus; he answers it with
kindness, not condemnation. An invitation, never a threat.

HOMOGRAPH EAR-CHECK: no high-risk homographs. NUMBER-STRESS LAW obeyed.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"
JESUS = "en-US-ChristopherNeural"

SEGMENTS = [
    ("n1", NARRATOR, "-20%", "-4Hz",
     "John the Baptist had spent his whole life preparing the way. He had pointed to "
     "Jesus and said, behold, the Lamb of God. And now he sat in a prison cell, waiting "
     "to die, and the doubts crept in.", None),
    ("n2", NARRATOR, "-22%", "-4Hz",
     "If Jesus really was the promised one, why was John still in chains? Where was the "
     "rescue? So he did something honest and brave. He sent two of his followers to ask "
     "Jesus directly.", None),
    # John's question — narrator voice, white caption
    ("nq", NARRATOR, "-22%", "-2Hz",
     "Art thou he that should come, or do we look for another?", None),
    ("n3", NARRATOR, "-22%", "-4Hz",
     "It is one of the most human questions in the whole Bible. Are you really who I "
     "hoped you were? And notice — Jesus was not offended. He did not scold John for "
     "asking.", None),
    # jv4 — the answer of evidence, silence 1
    ("jv4", JESUS, "-26%", "-6Hz",
     "Go and shew John again those things which ye do hear and see: The blind receive "
     "their sight, and the lame walk, the lepers are cleansed, and the deaf hear, the "
     "dead are raised up, and the poor have the gospel preached to them.", None),
    ("n4", NARRATOR, "-22%", "-4Hz",
     "He did not send back an argument. He sent back a scene. Go and tell John what you "
     "see happening — right here, right now. The blind seeing. The broken mended. The "
     "poorest people being treated like they matter. This is what I am doing.", None),
    ("n5", NARRATOR, "-22%", "-4Hz",
     "Not overthrowing an empire. Not breaking open a prison. But healing, one by one, "
     "the people everyone else stepped over. That was the answer to give a doubting man. "
     "Look at the love. Look at what it is actually doing.", None),
    # jv6 — blessed is he, silence 2
    ("jv6", JESUS, "-26%", "-6Hz",
     "And blessed is he, whosoever shall not be offended in me.", None),
    ("n6", NARRATOR, "-22%", "-4Hz",
     "It was tender, not sharp. Blessed is the one who does not give up on me when I do "
     "not look the way he expected. And then, the moment the messengers left, Jesus "
     "turned to the crowd and praised John — defending his doubting friend to his face.", None),
    ("n7", NARRATOR, "-24%", "-4Hz",
     "The answer came back to the cell, and John was at peace. Not rescued — but no "
     "longer alone in the dark, and no longer afraid that he had been wrong.", None),
    ("n7b", NARRATOR, "-24%", "-4Hz",
     "Sometimes the answer to our doubt is not the thing we asked for. It is simply, "
     "quietly: look at the love. It is real, and it is for you. Do not be offended — "
     "only trust, and be at peace.", None),
    ("card", NARRATOR, "-26%", "-4Hz",
     "Even the strongest believer sometimes sits in the dark and wonders. Jesus did not "
     "shame John for asking; he answered gently, with evidence of grace. If you have your "
     "own honest question, would you dare to bring it to him too?", None),
]


async def main():
    for name, voice, rate, pitch, text, cap in SEGMENTS:
        await save_narration(text, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")


if __name__ == "__main__":
    import os
    os.makedirs("audio", exist_ok=True)
    asyncio.run(main())
