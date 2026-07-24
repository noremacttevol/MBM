#!/usr/bin/env python3
"""Narration for build-82-anointing-at-bethany — Mark 14.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

THE WOMAN IS SILENT, AND I DID NOT GIVE HER A VOICE. This needs saying first,
because this is a build about a woman and the pressure to find her a line is
real. In Mark 14:3-9 she does not speak. Not one word. She comes in, she breaks
the jar, she pours it out, she is scolded, she is defended, and she never answers
any of it. Mark gives her no name either. NOTHING was put in her mouth, and there
is NO PINK in this build. That is the honest reading of the passage, and it is
also the point: everything said in that room is said about her, over her head,
and the only person who speaks up for her is Jesus. Inventing a line for her
would have cost the story the thing that makes it hurt.
(John 12:1-8 names her as Mary of Bethany and she is silent there too, so there
was no verse to borrow from the parallel account either.)

STAYED RED -- all three existing red beats are Jesus in the flesh, verbatim, and
a red-letter KJV prints all three:
  j1  Mark 14:6  'Let her alone; why trouble ye her? she hath wrought a good work
      on me.'
  j2  Mark 14:8  'She hath done what she could: she is come aforehand to anoint
      my body to the burying.'
  j3  Mark 14:9  'Verily I say unto you, Wheresoever this gospel shall be preached
      throughout the whole world, this also that she hath done shall be spoken of
      for a memorial of her.'
None needed splitting. All three ids kept.

ONE MORE RED LINE ADDED. n4 paraphrased Mark 14:7 -- 'There would always be
chances to do good for the poor' -- and that is one of the most quoted sentences
in the Gospels, sitting in the video in white paraphrase:
  j1b  Mark 14:7  'For ye have the poor with you always, and whensoever ye will
       ye may do them good: but me ye have not always.'  `jesus`, red. n4 is
       trimmed to the frame and n4b carries the retelling.

THE DISCIPLES' INDIGNATION IS `scripture`, NOT RED. n2 paraphrased their
complaint in white. Lifted verbatim as `scripture` (men in the story):
  s4  Mark 14:4-5  'Why was this waste of the ointment made? For it might have
      been sold for more than three hundred pence, and have been given to the
      poor.'  n2 is trimmed to the frame, n2b carries the retelling. All on ST5.

RETELLINGS ADDED: n2b after s4, n3b after j1, n4b after j1b, n4c after j2. n6
already retells j3 and was left alone.

NO GREEN: nothing in Mark 14:3-9 is the Father or a voice from heaven.

WHY-LAW: she gave the most extravagant thing she owned and the room called it
waste; he called it beautiful, and said the world would still be telling her
story. He was right. Milk: what you give him is never wasted, whatever the room
says about it.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0a", NARRATOR, "In a house in Bethany, days before the end, a woman came to Jesus at the table."),
    ("n0b", NARRATOR, "She carried an alabaster jar of pure, costly perfume."),
    ("n1a", NARRATOR, "She broke the jar open,"),
    ("n1b", NARRATOR, "and poured all of it over his head — a year's wages, gone in a moment."),
    ("n2", NARRATOR, "Some of the men at the table were furious. Mark writes down what they said:"),
    # Mark 14:4-5
    ("s4", SCRIPTURE, "Why was this waste of the ointment made? For it might have been sold for more than three hundred pence, and have been given to the poor."),
    ("n2b", NARRATOR, "Why has this been wasted? they said. It could have been sold for more than three hundred silver coins — nearly a year's pay for a working man — and the money given to the poor. And Mark adds one more line: they murmured against her. They said it where she could hear it. She does not answer them. She never says a single word in this whole story."),
    ("n3", NARRATOR, "Jesus stopped them cold, and defended her."),
    # Mark 14:6
    ("j1", JESUS, "Let her alone; why trouble ye her? she hath wrought a good work on me."),
    ("n3b", NARRATOR, "Leave her alone. Why are you giving her a hard time? She has done a beautiful thing for me. Not a wasteful thing. A good one."),
    ("n4", NARRATOR, "And then he answered the argument about the money directly:"),
    # Mark 14:7
    ("j1b", JESUS, "For ye have the poor with you always, and whensoever ye will ye may do them good: but me ye have not always."),
    ("n4b", NARRATOR, "You will always have the poor with you, he said, and any time you want to, you can do good for them. But you will not always have me. He was not brushing the poor aside. He was telling a room full of men that the window on this particular kindness was closing, and only one person in it had noticed."),
    # Mark 14:8
    ("j2", JESUS, "She hath done what she could: she is come aforehand to anoint my body to the burying."),
    ("n4c", NARRATOR, "She did what she was able to do, he said. She has come ahead of time to prepare my body for burial. Nobody else in that house would even let him say the word."),
    ("n5", NARRATOR, "Whether she fully knew it or not, she was the only one in that room who had prepared him for what was coming."),
    # Mark 14:9
    ("j3", JESUS, "Verily I say unto you, Wheresoever this gospel shall be preached throughout the whole world, this also that she hath done shall be spoken of for a memorial of her."),
    ("n6", NARRATOR, "Wherever this good news is told, anywhere in the world, what she did today will be told with it, so she is remembered. She gave the most extravagant thing she owned, and he received it as beautiful. Not wasteful — worship. And he was right about the memorial: all these centuries later, here we are, telling her story."),
    ("card", NARRATOR, "She gave him her best and he called it beautiful. What would it mean to stop holding back from him?"),
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
