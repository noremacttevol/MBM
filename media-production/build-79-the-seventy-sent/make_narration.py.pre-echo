#!/usr/bin/env python3
"""Narration for build-79-the-seventy-sent — Luke 10.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

STAYED RED -- all three existing red beats are Jesus in the flesh, verbatim,
and a red-letter KJV prints all three:
  j1  Luke 10:2   'The harvest truly is great, but the labourers are few: pray ye
      therefore the Lord of the harvest, that he would send forth labourers into
      his harvest.'
  j2  Luke 10:9   'The kingdom of God is come nigh unto you.'
  j3  Luke 10:20  'Notwithstanding in this rejoice not, that the spirits are
      subject unto you; but rather rejoice, because your names are written in
      heaven.'
None carried Luke's framing inside it, so none needed splitting.

THE SEVENTY NOW SPEAK. n3 said 'They came back amazed — even the dark things had
listened when they spoke in his name' -- a paraphrase of the one line these
seventy men actually get in scripture, and the viewer never heard it. Lifted
verbatim as `scripture` (men in the story, not Deity):
  s17  Luke 10:17  'Lord, even the devils are subject unto us through thy name.'
  n3 is trimmed to the frame, n3b carries the retelling and hands off to j3. All
  on ST6. This is worth having because j3 is Jesus CORRECTING what they just
  said, and the video previously played the correction without the viewer having
  heard the thing being corrected.

RETELLINGS ADDED -- this build had three Old English beats and not one plain
modern retelling after any of them, which is the single biggest gap in the cut:
  n1b  after j1, on ST3.
  n2b  after j2, on ST5.
  n3c  after j3, on ST8.

ST8 -- 's8-written-in-heaven.jpeg' was in still_vars and on disk but NO BEAT
POINTED AT IT. The still the build is named for was never on screen. n3c now
carries it, and it is the closing image of the video.

NO GREEN: nothing in Luke 10:1-20 is the Father or a voice from heaven. Jesus
speaks about the Lord of the harvest and about heaven; neither speaks here.

WOMEN: Luke 10:1-20 records no woman speaking. Martha and Mary are verses 38-42,
after this passage and a different story. Nothing added; nothing invented.

WHY-LAW: they came back thrilled about power, and he redirected them to
something quieter and far bigger. Milk: the joy that lasts is that your name is
already written down.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "Jesus picked seventy of his followers and sent them out two by two, ahead of him, into every town he was about to visit."),
    ("n1", NARRATOR, "He didn't send them with much — no extra bag, no spare sandals, no backup plan. Just each other, and a message."),
    # Luke 10:2
    ("j1", JESUS, "The harvest truly is great, but the labourers are few: pray ye therefore the Lord of the harvest, that he would send forth labourers into his harvest."),
    ("n1b", NARRATOR, "There is so much to bring in, he told them, and hardly anyone to do it — so ask the owner of the harvest to send out more workers. Notice what he did not say. He did not say the fields were empty. He said the fields were full, and the crew was short."),
    ("n2", NARRATOR, "Wherever they were welcomed, they were to heal the sick and say the same simple thing."),
    # Luke 10:9
    ("j2", JESUS, "The kingdom of God is come nigh unto you."),
    ("n2b", NARRATOR, "God's kingdom has come close to you. That was the whole message. Not a warning, not a threat — an announcement that the thing everyone had been waiting for had just walked into their town."),
    ("n3", NARRATOR, "And they came back with joy, amazed at what had happened when they used his name:"),
    # Luke 10:17
    ("s17", SCRIPTURE, "Lord, even the devils are subject unto us through thy name."),
    ("n3b", NARRATOR, "Lord, even the evil spirits obey us when we use your name. They were thrilled, and they had every right to be. And then Jesus told them what to actually celebrate."),
    # Luke 10:20
    ("j3", JESUS, "Notwithstanding in this rejoice not, that the spirits are subject unto you; but rather rejoice, because your names are written in heaven."),
    ("n3c", NARRATOR, "Don't be glad about that, he said. Don't let the power be the thing that thrills you. Be glad about this instead: your names are written down in heaven. The power was temporary and it was never really theirs. The name in the book was permanent, and it was theirs before they ever left on the trip."),
    ("card", NARRATOR, "Your name, written in heaven — that's the joy he wanted them to keep. It's meant for you as well."),
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
