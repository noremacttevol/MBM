#!/usr/bin/env python3
"""Narration for build-122-mote-and-beam — Matthew 7.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

BOTH RED BEATS STAY RED. jvA (Matthew 7:1-2) and jvB (Matthew 7:5) are Jesus
speaking on the mount. Nothing moved out of red.

jvA WAS CUT SHORT MID-VERSE. It ended at 'ye shall be judged.' where the KJV
has a colon and keeps going. The full second verse is now restored so the
line a viewer looks up matches the line they heard:
  '...and with what measure ye mete, it shall be measured to you again.'
n8 already retells that clause ('the measure you use is the measure you will
get back'), so the retelling was already in the build waiting for the words.

LIFTED FROM PARAPHRASE — two red verses were in this build only as narrator
paraphrase and are now spoken verbatim:
  jv3  Matthew 7:3  'And why beholdest thou the mote that is in thy brother's
                     eye, but considerest not the beam that is in thine own
                     eye?'                                          JESUS
  jv4  Matthew 7:4  'Or how wilt thou say to thy brother, Let me pull out the
                     mote out of thine eye; and, behold, a beam is in thine
                     own eye?'                                      JESUS
This is the heart of the story and it was the one part of it the viewer never
actually heard Jesus say. Both new beats sit on the same stills as the
narrator beats that retell them (jv3 on S3 with n2, jv4 on S4 with n3), so no
new artwork is needed and the edit is unchanged.

NO RED RUNS BACK TO BACK. Order is jvA, n2, jv3, n3, jv4, n4, n5, jvB, n6-n8.
Every Old English block is followed immediately by the storyteller.

NO MIXED SEGMENTS. Matthew 7:1-5 is one unbroken stretch of Jesus speaking;
there is no narration frame welded into any of these beats.

WHY-LAW: he never says stop caring about your brother. He says deal with your
own beam first so you can actually help. Milk framing — mercy, not superiority.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, 'Of all the things Jesus taught on that hillside, one of them cuts straight to how we treat each other — and it starts with a warning we would rather skip.'),
    ("jvA", JESUS, 'Judge not, that ye be not judged. For with what judgment ye judge, ye shall be judged: and with what measure ye mete, it shall be measured to you again.'),
    ("n2", NARRATOR, "Don't set yourself up as the judge, he said, because whatever standard you hold other people to is the one that will be held up to you. And we are experts at spotting the small faults in someone else. A tiny speck, a mote, in our brother's eye — and we cannot wait to point it out. So he asked a question."),
    ("jv3", JESUS, "And why beholdest thou the mote that is in thy brother's eye, but considerest not the beam that is in thine own eye?"),
    ("n3", NARRATOR, "Why do you stare at the speck of sawdust in your brother's eye, he asked, and never once notice the plank in your own? Then he drew the picture out until it was absurd enough to make you laugh."),
    ("jv4", JESUS, 'Or how wilt thou say to thy brother, Let me pull out the mote out of thine eye; and, behold, a beam is in thine own eye?'),
    ("n4", NARRATOR, 'Picture it. A man leaning in, saying hold still, let me get that little speck out for you — with an entire wooden beam sticking straight out of his own head. He cannot even see straight. The beam is in the way of everything he does. And yet he is completely sure that he is the one who ought to be fixing other people.'),
    ("n5", NARRATOR, 'And then, if we are honest, the moment finally comes when we catch sight of the beam. Not his. Ours. The one we had been carrying the whole time.'),
    ("jvB", JESUS, "Thou hypocrite, first cast out the beam out of thine own eye; and then shalt thou see clearly to cast out the mote out of thy brother's eye."),
    ("n6", NARRATOR, "Notice he does not say ignore your brother's speck. He says deal with your own beam first — and then you will actually be able to help him, gently, instead of just condemning him."),
    ("n7", NARRATOR, 'The goal was never to stop caring about each other. It was to come to each other humble instead of superior — as one flawed person helping another, not a judge passing a sentence.'),
    ("n8", NARRATOR, 'The measure you use is the measure you will get back. So Jesus offers a better one: mercy. Deal honestly with yourself, and you will be amazed how much patience you suddenly have for everyone else.'),
    ("card", NARRATOR, 'Jesus was not telling us to stop seeing clearly — he was telling us where to start: with the beam in our own eye. Deal with that, and our eyes for other people fill with mercy instead of judgment. Whose speck have you been watching, while a beam waited in your own eye?'),
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
