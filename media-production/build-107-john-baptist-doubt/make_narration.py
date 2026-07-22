#!/usr/bin/env python3
"""Narration for build-107-john-baptist-doubt — Matthew 11.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

This video is a CONVERSATION, and only half of it was voiced. Both red beats
are genuinely red and stay red. The work here was making John's side actually
present, and pulling the evangelist's framing out of red.

STAYED RED (jesus):
  jv4  Matt 11:4-5  'Go and shew John again those things which ye do hear and see...'
  jv6  Matt 11:6    'And blessed is he, whosoever shall not be offended in me.'

THE OTHER VOICE - nq WAS NARRATOR, NOW SCRIPTURE (light blue):
  nq   Matt 11:3    'Art thou he that should come, or do we look for another?'
The segment already carried the verbatim KJV word for word, but it was painted
white and spoken by the storyteller, so the viewer heard Jesus answer a question
nobody had audibly asked. It is John's two disciples speaking, so it is
`scripture`. The blue question against the red answer IS this video.

SPLIT - the narration frame is not red:
  s4a  Matt 11:4a   'Jesus answered and said unto them,'  SCRIPTURE
That clause is Matthew writing, not Jesus speaking, and a red-letter KJV leaves
it black. It is a new beat on S4, the still where the messengers reach him, and
hands straight to jv4 on S5. No new artwork, and the cut the viewer sees is the
same.

WOMEN: Matthew 11 records no woman speaking. There is nothing here to lift, so
nothing was added rather than reaching for a line from another chapter.

NOT CHANGED: n1 through n7b stay narrator. They describe the prison, the doubt
and the answer in modern English rather than quoting, which is correct. n3 is
already the retelling of nq, and n4/n6 already retell jv4 and jv6, so no new
retelling beats were needed.

WHY-LAW: Jesus was not offended by an honest question from a friend in the dark,
and answered it with evidence of mercy rather than a rebuke. Milk framing - you
are allowed to ask.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "John the Baptist had spent his whole life preparing the way. He had pointed to Jesus and said, behold, the Lamb of God. And now he sat in a prison cell, waiting to die, and the doubts crept in."),
    ("n2", NARRATOR, "If Jesus really was the promised one, why was John still in chains? Where was the rescue? So he did something honest and brave. He sent two of his followers to ask Jesus directly."),
    # Matthew 11:3
    ("nq", SCRIPTURE, "Art thou he that should come, or do we look for another?"),
    ("n3", NARRATOR, "It is one of the most human questions in the whole Bible. Are you really who I hoped you were? And notice — Jesus was not offended. He did not scold John for asking."),
    # Matthew 11:4
    ("s4a", SCRIPTURE, "Jesus answered and said unto them,"),
    # Matthew 11:4-5
    ("jv4", JESUS, "Go and shew John again those things which ye do hear and see: The blind receive their sight, and the lame walk, the lepers are cleansed, and the deaf hear, the dead are raised up, and the poor have the gospel preached to them."),
    ("n4", NARRATOR, "He did not send back an argument. He sent back a scene. Go and tell John what you see happening — right here, right now. The blind seeing. The broken mended. The poorest people being treated like they matter. This is what I am doing."),
    ("n5", NARRATOR, "Not overthrowing an empire. Not breaking open a prison. But healing, one by one, the people everyone else stepped over. That was the answer to give a doubting man. Look at the love. Look at what it is actually doing."),
    # Matthew 11:6
    ("jv6", JESUS, "And blessed is he, whosoever shall not be offended in me."),
    ("n6", NARRATOR, "It was tender, not sharp. Blessed is the one who does not give up on me when I do not look the way he expected. And then, the moment the messengers left, Jesus turned to the crowd and praised John — defending his doubting friend to his face."),
    ("n7", NARRATOR, "The answer came back to the cell, and John was at peace. Not rescued — but no longer alone in the dark, and no longer afraid that he had been wrong."),
    ("n7b", NARRATOR, "Sometimes the answer to our doubt is not the thing we asked for. It is simply, quietly: look at the love. It is real, and it is for you. Do not be offended — only trust, and be at peace."),
    ("card", NARRATOR, "Even the strongest believer sometimes sits in the dark and wonders. Jesus did not shame John for asking; he answered gently, with evidence of grace. If you have your own honest question, would you dare to bring it to him too?"),
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
