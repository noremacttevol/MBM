#!/usr/bin/env python3
"""Narration for build-78-who-is-my-mother — Mark 3.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

STAYED RED -- all three existing red beats are Jesus in the flesh and a
red-letter KJV prints all three, verbatim:
  j1  Mark 3:33  'Who is my mother, or my brethren?'
  j2  Mark 3:34  'Behold my mother and my brethren!'
  j3  Mark 3:35  'For whosoever shall do the will of God, the same is my brother,
      and my sister, and mother.'
None carried Mark's framing inside it, so none needed splitting. j2 and j3 are
one continuous saying and are deliberately left back to back, with n3 retelling
both together.

THE MESSENGER NOW SPEAKS. n1b said 'The people near him passed it forward: your
family is here — they want you' -- modern English, in white, standing in for a
verse the viewer never heard. Lifted verbatim as `scripture` (the crowd in the
story, not Deity):
  s32  Mark 3:32  'Behold, thy mother and thy brethren without seek for thee.'
  n1b is trimmed to the frame, n1c carries the retelling. Both on ST3, no new
  artwork. This matters because Jesus's red-letter question in j1 is a direct
  answer to those exact words -- and until now the video asked the answer to a
  question it had never actually asked.

DELIBERATE QUESTION-AND-ANSWER SHAPE -- NO RETELLING WEDGED IN. j1 is Jesus's
question, and j2/j3 are Jesus answering his own question. n2 sits between them
and is the storyteller describing him looking around the room, which is Mark 3:34
narration and belongs in white. No plain-English retelling is put between j1 and
n2, because retelling a four-word rhetorical question back to the viewer before
he has answered it would kill the beat. n3 retells the whole exchange after j3.
This is the same call the law makes for build-98's 'Mary.' / 'Rabboni.'

MARY IS PRESENT AND SILENT. Mark 3:31-35 has his mother standing outside and
sending in for him -- and Mark records not one word from her. NOTHING was put in
her mouth. The message that comes in is spoken by the crowd sitting around him,
not by her, so s32 is `scripture` and not `woman`. No pink in this build, and
that is the honest reading.

NO GREEN: nothing in Mark 3:31-35 is the Father or a voice from heaven. Jesus
speaks ABOUT the will of God here; God does not speak.

WHY-LAW: he was not shutting his family out, he was drawing the circle wider.
Milk: the family line got redrawn around whoever would come.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, 'Jesus was inside a packed house, teaching, when word came in from the edge of the crowd.'),
    ("n1a", NARRATOR, 'His mother and his brothers were standing outside, asking for him.'),
    ("n1b", NARRATOR, 'The people sitting around him passed it forward, and Mark writes down exactly what they said:'),
    ("s32", SCRIPTURE, 'Behold, thy mother and thy brethren without seek for thee.'),
    ("n1c", NARRATOR, "Look — your mother and your brothers are outside, and they're asking for you. Everyone in that room knew what happens next. You stop teaching, and you go out to your family."),
    ("j1", JESUS, 'Who is my mother, or my brethren?'),
    ("n2", NARRATOR, 'Nobody expected that. Then he looked slowly around at the ordinary people sitting in a circle right in front of him — farmers, fishermen, mothers, a child — and answered his own question.'),
    ("j2", JESUS, 'Behold my mother and my brethren!'),
    ("j3", JESUS, 'For whosoever shall do the will of God, the same is my brother, and my sister, and mother.'),
    ("n3", NARRATOR, "He wasn't pushing his family away. He was opening the circle — telling a room full of nobodies they could belong to him like blood."),
    ("card", NARRATOR, 'He drew the family line around whoever would come. That door is open to you too.'),
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
