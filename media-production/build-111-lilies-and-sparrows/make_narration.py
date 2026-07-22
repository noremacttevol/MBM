#!/usr/bin/env python3
"""Narration for build-111-lilies-and-sparrows — Matthew 6.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

All three existing red beats are correctly red and were left alone. This is the
Sermon on the Mount, Jesus speaking in the flesh, and none of the segments had an
evangelist framing clause welded on, so there was nothing to split and nothing to
move out of red.

STAYED RED (jesus), verified verbatim:
  jv26    Matt 6:26     'Behold the fowls of the air...'
  jv2829  Matt 6:28-29  'Consider the lilies of the field...'
  jv33    Matt 6:33     'But seek ye first the kingdom of God...'

LIFTED FROM PARAPHRASE - also Jesus, so also RED:
  jv30  Matt 6:30  'Wherefore, if God so clothe the grass of the field, which to
                    day is, and to morrow is cast into the oven, shall he not much
                    more clothe you, O ye of little faith?'
  jv34  Matt 6:34  'Take therefore no thought for the morrow: for the morrow shall
                    take thought for the things of itself. Sufficient unto the day
                    is the evil thereof.'
n5 was already delivering both of these in modern English - 'if God feeds the
birds and dresses the grass that is here today and gone tomorrow, how much more
will he take care of you' is Matthew 6:30 almost word for word, and 'your anxious
tomorrow' is 6:34. The video was making Jesus's argument without ever letting him
make it. Now the verses speak and n5 retells them, which is the right order.

EDIT TO EXISTING NARRATOR TEXT: n5 is unchanged in substance but split at its own
seam so each half retells the verse it now follows. n5 keeps the 'how much more
will he take care of you' half after jv30; the 'anxious tomorrow' half becomes
n5b after jv34. No wording was invented.

LEFT AS PARAPHRASE ON PURPOSE: n6 ends with 'a Father who already knows exactly
what you need', which is Matthew 6:32. It is not lifted out, because n6 is doing
pastoral work in the narrator's own warm voice and a fourth red beat in a row
would flatten the pacing. Flagging it as a deliberate choice rather than an
oversight - it is available if a later pass wants it.

WOMEN: Matthew 6 records no woman speaking. Nothing was added rather than
importing a line from another passage.

WHY-LAW: he does not scold the worry. He points at a bird. Milk framing - you are
already being cared for by someone who has never once forgotten a sparrow.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "He was talking to people who knew what it was to worry. Where the next meal would come from. Whether there would be enough. And instead of an argument, Jesus simply pointed at the world around them."),
    # Matthew 6:26
    ("jv26", JESUS, "Behold the fowls of the air: for they sow not, neither do they reap, nor gather into barns; yet your heavenly Father feedeth them. Are ye not much better than they?"),
    ("n2", NARRATOR, "Look at the little sparrows, he says. No barns. No savings. No plans for next winter. And not one of them goes uncared for, because the Father feeds them. And you — you are worth so much more to him than a sparrow."),
    ("n3", NARRATOR, "Then he reaches down to the wildflowers scattered through the grass at their feet."),
    # Matthew 6:28-29
    ("jv2829", JESUS, "Consider the lilies of the field, how they grow; they toil not, neither do they spin: And yet I say unto you, That even Solomon in all his glory was not arrayed like one of these."),
    ("n4", NARRATOR, "These flowers do not work a single day. They just grow where they are planted. And yet the richest king who ever lived, in all his robes, was never dressed as beautifully as one ordinary wildflower that God simply decided to clothe."),
    # Matthew 6:30
    ("jv30", JESUS, "Wherefore, if God so clothe the grass of the field, which to day is, and to morrow is cast into the oven, shall he not much more clothe you, O ye of little faith?"),
    ("n5", NARRATOR, "Here is his point, gentle and steady: if God feeds the birds and dresses the grass that is here today and gone tomorrow, how much more will he take care of you?"),
    # Matthew 6:34
    ("jv34", JESUS, "Take therefore no thought for the morrow: for the morrow shall take thought for the things of itself. Sufficient unto the day is the evil thereof."),
    ("n5b", NARRATOR, "Don't go out to meet tomorrow. Tomorrow will look after itself, and today has enough in it already. Your anxious tomorrow is not something you have to carry alone."),
    ("n6", NARRATOR, "He is not scolding the worry. He knows life is hard and needs are real. He is gently loosening your grip, one finger at a time, and offering to carry it with you, as a Father who already knows exactly what you need."),
    # Matthew 6:33
    ("jv33", JESUS, "But seek ye first the kingdom of God, and his righteousness; and all these things shall be added unto you."),
    ("n7", NARRATOR, "Put him first, he says, and stop bracing against tomorrow all by yourself. The same Father who has not forgotten a single sparrow has certainly not forgotten you. You can breathe. You are cared for."),
    ("card", NARRATOR, "God feeds the birds and clothes the wildflowers, and Jesus says you matter far more to your Father than these. What worry could you set down today, and trust him with instead?"),
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
