#!/usr/bin/env python3
"""Narration audio for Video #111 — Lilies and Sparrows (Matthew 6:25-34).

Narrator: en-US-AndrewNeural. Jesus: en-US-ChristopherNeural (exact KJV only).

Jesus's KJV lines (Christopher, cream italic):
  jv26    Matt 6:26     "Behold the fowls of the air... yet your heavenly Father
                         feedeth them. Are ye not much better than they?" — silence 1
  jv2829  Matt 6:28-29  "Consider the lilies of the field... even Solomon in all his
                         glory was not arrayed like one of these."
  jv33    Matt 6:33     "But seek ye first the kingdom of God, and his righteousness;
                         and all these things shall be added unto you." — silence 2

WHY-LAW: worry is not solved by an argument; Jesus solves it by pointing outdoors. Look
at the birds — no barns, no savings, and the Father feeds them. Look at the wildflowers —
they do nothing, and God dresses them better than a king. You matter more to him than a
sparrow or a lily. So stop bracing for tomorrow alone; seek him first, and trust him for
the rest. Milk framing: your Father knows what you need and is already caring for you. An
invitation to rest, never a threat.

HOMOGRAPH EAR-CHECK: 'sow' /soh/ (not /sow/ the pig), 'arrayed' plain. Verify 'sow'.
NUMBER-STRESS LAW obeyed.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"
JESUS = "en-US-ChristopherNeural"

SEGMENTS = [
    ("n1", NARRATOR, "-20%", "-4Hz",
     "He was talking to people who knew what it was to worry. Where the next meal would "
     "come from. Whether there would be enough. And instead of an argument, Jesus simply "
     "pointed at the world around them.", None),
    # jv26 — behold the fowls — silence 1
    ("jv26", JESUS, "-26%", "-6Hz",
     "Behold the fowls of the air: for they sow not, neither do they reap, nor gather "
     "into barns; yet your heavenly Father feedeth them. Are ye not much better than "
     "they?", None),
    ("n2", NARRATOR, "-22%", "-4Hz",
     "Look at the little sparrows, he says. No barns. No savings. No plans for next "
     "winter. And not one of them goes uncared for, because the Father feeds them. And "
     "you — you are worth so much more to him than a sparrow.", None),
    ("n3", NARRATOR, "-22%", "-4Hz",
     "Then he reaches down to the wildflowers scattered through the grass at their feet.", None),
    # jv2829 — consider the lilies
    ("jv2829", JESUS, "-24%", "-6Hz",
     "Consider the lilies of the field, how they grow; they toil not, neither do they "
     "spin: And yet I say unto you, That even Solomon in all his glory was not arrayed "
     "like one of these.", None),
    ("n4", NARRATOR, "-22%", "-4Hz",
     "These flowers do not work a single day. They just grow where they are planted. And "
     "yet the richest king who ever lived, in all his robes, was never dressed as "
     "beautifully as one ordinary wildflower that God simply decided to clothe.", None),
    ("n5", NARRATOR, "-22%", "-4Hz",
     "Here is his point, gentle and steady: if God feeds the birds and dresses the grass "
     "that is here today and gone tomorrow, how much more will he take care of you? Your "
     "anxious tomorrow is not something you have to carry alone.", None),
    ("n6", NARRATOR, "-22%", "-4Hz",
     "He is not scolding the worry. He knows life is hard and needs are real. He is "
     "gently loosening your grip, one finger at a time, and offering to carry it with "
     "you, as a Father who already knows exactly what you need.", None),
    # jv33 — seek first — silence 2
    ("jv33", JESUS, "-26%", "-6Hz",
     "But seek ye first the kingdom of God, and his righteousness; and all these things "
     "shall be added unto you.", None),
    ("n7", NARRATOR, "-24%", "-4Hz",
     "Put him first, he says, and stop bracing against tomorrow all by yourself. The same "
     "Father who has not forgotten a single sparrow has certainly not forgotten you. You "
     "can breathe. You are cared for.", None),
    ("card", NARRATOR, "-26%", "-4Hz",
     "God feeds the birds and clothes the wildflowers, and Jesus says you matter far more "
     "to your Father than these. What worry could you set down today, and trust him with "
     "instead?", None),
]


async def main():
    for name, voice, rate, pitch, text, cap in SEGMENTS:
        tts = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")


if __name__ == "__main__":
    import os
    os.makedirs("audio", exist_ok=True)
    asyncio.run(main())
