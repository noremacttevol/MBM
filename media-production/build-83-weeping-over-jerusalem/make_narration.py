#!/usr/bin/env python3
"""Narration for build-83-weeping-over-jerusalem — Luke 19.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

STAYED RED: j1, Luke 19:42, 'If thou hadst known, even thou, at least in this
thy day, the things which belong unto thy peace! but now they are hid from thine
eyes.' Verbatim, Jesus in the flesh, red-lettered. Unchanged, id kept. It is the
only spoken line in the passage.

LIFTED OUT OF PARAPHRASE -- LUKE'S OWN SENTENCE, now `scripture` (light blue,
Luke writing, not Jesus speaking):
  s41  Luke 19:41  'And when he was come near, he beheld the city, and wept over
       it.'  This is the sentence the entire video is named for and the viewer
       never heard it. n1a is trimmed to the frame and n1b carries the retelling.
       Both on S2 and S3 -- the stills already built for exactly this moment.

RETELLING ADDED: n2b after j1, on S5. The build's one Old English beat had no
plain-modern landing at all, and 'the things which belong unto thy peace' is not
a phrase a listener today parses on the fly.

LEFT AS NARRATOR PARAPHRASE ON PURPOSE. n3a says 'He could see what was coming
for the city he loved — armies and ruin, a generation away.' That is Luke
19:43-44, and I know the wording, but it is graphic -- trenches, the city laid
level with the ground, children dashed down, not one stone left on another. This
is a milk-before-meat library and the build's whole tone is tenderness. Putting
that verse in verbatim would turn a video about his tears into a video about the
siege. It stays as the storyteller's summary, deliberately, and this note is the
record of that choice rather than an accident. The one clause of 19:44 that IS
the emotional point -- 'because thou knewest not the time of thy visitation' --
is already carried by n2 and n3b in the storyteller's voice.

NO GREEN: nothing in Luke 19:41-44 is the Father or a voice from heaven.

WOMEN: Luke 19:41-44 records no woman speaking. There is no dialogue in the
passage besides Jesus. Nothing added; nothing invented.

WHY-LAW: God cried over people who could not see him, and the crying was not
anger. Milk: his grief over you is love that can see exactly what could have
been.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "As Jesus came over the hill and the whole city of Jerusalem opened up in front of him, he did something the crowds didn't expect."),
    ("n1a", NARRATOR, "He stopped. Luke writes it in one plain sentence:"),
    # Luke 19:41
    ("s41", SCRIPTURE, "And when he was come near, he beheld the city, and wept over it."),
    ("n1b", NARRATOR, "He came close, he looked at the city, and he cried over it. Not for himself. For them."),
    ("n2", NARRATOR, "The peace they had been aching for had walked right up to their gates — and the city was too busy to see it."),
    # Luke 19:42
    ("j1", JESUS, "If thou hadst known, even thou, at least in this thy day, the things which belong unto thy peace! but now they are hid from thine eyes."),
    ("n2b", NARRATOR, "If only you had known — even you, even today — what would have brought you peace. But now it's hidden from your eyes. He is not scolding the city. He is talking to it the way you talk to someone you love who is about to walk past the one thing that would have saved them."),
    ("n3a", NARRATOR, "He could see what was coming for the city he loved — armies and ruin, a generation away."),
    ("n3b", NARRATOR, "His tears weren't anger. They were the grief of love that sees exactly what could have been."),
    ("card", NARRATOR, "He wept because he loved the city that couldn't see him. He sees you clearly. Don't look away."),
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
