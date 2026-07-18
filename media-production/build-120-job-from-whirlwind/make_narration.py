#!/usr/bin/env python3
"""Narration audio for Video #120 — Job Answered from the Whirlwind (Job 38-42).

Narrator: en-US-AndrewNeural. God's voice: en-US-ChristopherNeural (exact KJV only).
Job's own answer (Job 42:5) is voiced by the NARRATOR (white caption); God's own KJV lines
from the whirlwind render cream-italic in the scripture voice.

God's KJV lines (Christopher, cream italic):
  jvA  Job 38:4   "Where wast thou when I laid the foundations of the earth? declare, if
                   thou hast understanding." — sacred silence 1
  jvB  Job 38:31  "Canst thou bind the sweet influences of Pleiades, or loose the bands of
                   Orion?" — sacred silence 2 (adjacent to jvA)

CARE FLAGS G, J (Job): the answer was PRESENCE, not an explanation. The narration NEVER makes
God the tormentor-for-glory — it does not dwell on the heavenly wager or frame God as
authoring pain to win a bet. Job's grief is honored, not rushed; his losses are aftermath, not
spectacle. The closing never promises the same restoration — the hope is that God draws near
to the broken.

WHY-LAW: the best man in the world lost everything and demanded to know why. God never gave
the reason. He gave something Job needed more — himself, out of the whirlwind. Milk framing:
when you are in the ashes, the promise is not a tidy explanation but a God who shows up in the
grief. An assurance of nearness, never a threat.

HOMOGRAPH EAR-CHECK: 'wound' (noun, injury) in context; 'Pleiades'/'Orion' are KJV proper
names. NUMBER-STRESS LAW: no risky numbers.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"
GOD = "en-US-ChristopherNeural"

SEGMENTS = [
    ("n1", NARRATOR, "-20%", "-4Hz",
     "Job was a good man — honest, generous, devoted to God — and for most of his life that "
     "goodness and a happy, prosperous home went together.", None),
    ("n2", NARRATOR, "-22%", "-4Hz",
     "And then, in a single devastating stretch, it was all taken. His wealth, his health, "
     "and — most unbearable of all — his children. One of the oldest, hardest questions in "
     "the world landed on the best man in it: why do good people suffer?", None),
    ("n3", NARRATOR, "-22%", "-4Hz",
     "He sat down in the ashes, sick and broken, and he did not pretend to be all right. He "
     "grieved out loud. And scripture never once scolds him for it.", None),
    ("n4", NARRATOR, "-22%", "-4Hz",
     "His friends came, and at first they simply sat with him — which was the best thing "
     "they did. Then they started explaining. You must have sinned, they said. This must be "
     "your fault. Their tidy answers only deepened the wound.", None),
    ("n5", NARRATOR, "-22%", "-4Hz",
     "But Job would not accept easy lies about God or about himself. He did something braver "
     "than pretending. He took his anguish straight to God and demanded an answer. Where are "
     "you? Why is this happening?", None),
    ("n6", NARRATOR, "-22%", "-4Hz",
     "And God answered — though not in the way anyone expected. Out of a great whirlwind, "
     "the Maker of everything finally spoke.", None),
    # jvA — Where wast thou when I laid the foundations — sacred silence 1
    ("jvA", GOD, "-26%", "-6Hz",
     "Where wast thou when I laid the foundations of the earth? declare, if thou hast "
     "understanding.", None),
    # jvB — Canst thou bind the sweet influences of Pleiades — sacred silence 2
    ("jvB", GOD, "-26%", "-6Hz",
     "Canst thou bind the sweet influences of Pleiades, or loose the bands of Orion?", None),
    ("n7", NARRATOR, "-22%", "-4Hz",
     "God never explained why. Instead he showed Job the sea and the stars and the wild "
     "goodness of a world Job could never have made or held — and somehow it was enough. Not "
     "because Job got his answer, but because he got God himself. I have heard of thee by the "
     "hearing of the ear, Job said, but now mine eye seeth thee.", None),
    ("n8", NARRATOR, "-24%", "-4Hz",
     "The suffering was never fully explained — not to Job, and not to us. But Job was no "
     "longer alone in it. The God he thought had abandoned him had come near, and that "
     "nearness was the answer his grief actually needed.", None),
    ("card", NARRATOR, "-26%", "-4Hz",
     "Job's comfort was never a reason for his pain. It was a Person who showed up in it. If "
     "you are in the ashes right now, the promise is not a tidy explanation — it is that God "
     "draws near to the broken. Where do you most need him to show up?", None),
]


async def main():
    for name, voice, rate, pitch, text, cap in SEGMENTS:
        await save_narration(text, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")


if __name__ == "__main__":
    import os
    os.makedirs("audio", exist_ok=True)
    asyncio.run(main())
