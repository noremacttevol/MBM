#!/usr/bin/env python3
"""Narration for build-197-sons-and-daughters-prophesy — Joel 2.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

Joel 2:28-29. Both red beats move to GREEN.

  s1  Joel 2:28  'And it shall come to pass afterward, that I will pour out...'  RED -> GOD
  s2  Joel 2:29  'And also upon the servants and upon the handmaids...'          RED -> GOD

Both are the LORD in the first person - 'I will pour out my spirit' twice over.
That is Jehovah, the premortal Christ, so both are green. Joel is Old Testament,
so `jesus` is not available and would be wrong: a red-letter KJV prints this
black because Christ had not yet come in the flesh.

No splits. Neither segment mixes speakers. 'And it shall come to pass afterward'
is inside the oracle, not Joel's frame around it - the frame is verse 28's
opening in the wider chapter and the video never quotes it. Joel's own narration
is handled entirely by n0, which is already its own white beat.

TWO GREEN BEATS BACK TO BACK, on purpose. s1 runs straight into s2 with no
narrator between them, which the validator flags. They are one continuous
sentence of divine speech that the KJV happens to break across two verse numbers
- 'upon all flesh' in 28 and 'and ALSO upon the servants and upon the handmaids'
in 29. Cutting a retelling into the middle of that would break the one thing the
verse is doing, which is piling group onto group until nobody is left out. n1
retells both immediately after: 'not stopped by age or status - every kind of
person, filled with the same Spirit.' The retelling rule is met, just once for
the pair instead of twice.

Verbatim: s1 and s2 are Joel 2:28-29 word for word, including the colon at the
end of s1 and 'handmaids' rather than any modernisation. Neither was smoothed.

Nothing lifted from paraphrase. n2 recounts the day of Pentecost and Peter
standing up, which is Acts 2 - I am leaving it as narrator. Peter's speech there
is mostly him quoting this same Joel passage back, so lifting it would put the
video's own verse on screen twice, in green and then blue. n3 is the storyteller's
close, not a quotation.

Ids and beats unchanged. The card is 'card' and stays out of beats, as the
original had it.

WHY-LAW: milk. Sons AND daughters. Servants AND handmaids. The promise names the
people a listener would assume were left out, which is the whole point and needs
no commentary.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import GOD, NARRATOR

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "The prophet Joel looked down the long corridor of time and described a day the LORD promised — not for a few insiders, but for all."),
    # Joel 2:28
    ("s1", GOD, "And it shall come to pass afterward, that I will pour out my spirit upon all flesh; and your sons and your daughters shall prophesy, your old men shall dream dreams, your young men shall see visions:"),
    # Joel 2:29
    ("s2", GOD, "And also upon the servants and upon the handmaids in those days will I pour out my spirit."),
    ("n1", NARRATOR, "Not stopped by age or status — every kind of person, filled with the same Spirit."),
    ("n2", NARRATOR, "Decades later, on the day of Pentecost, the apostle Peter stood and said this promise had arrived. The Spirit fell, and ordinary people told of the mighty works of God."),
    ("n3", NARRATOR, "The promise was never meant to be locked in one building or one office. It was poured out — freely, widely, for whoever calls on the name of the LORD."),
    ("card", NARRATOR, "The promise was all flesh. That includes you. The Spirit is offered — receive Him."),
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
