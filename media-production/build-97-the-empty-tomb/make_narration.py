#!/usr/bin/env python3
"""Narration for build-97-the-empty-tomb — Luke 24.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

THIS BUILD HAD NO SCRIPTURE IN IT AT ALL. Eight beats, all white -- and
the angels' announcement, the most important sentence in the Bible, was being
delivered in the storyteller's voice.

THE ANGELS ARE BLUE, NOT RED. n4 paraphrased Luke 24:5-6. Angels are not Deity
and a red-letter KJV inks nothing here, so this is SCRIPTURE (light blue):
  s5  Luke 24:5-6  'Why seek ye the living among the dead? He is not here, but
      is risen:'
  n4 keeps its id and its text is already the exact retelling, so it was left
  alone and now simply follows the verse.
  s6  Luke 24:6-7  'remember how he spake unto you when he was yet in Galilee,
      Saying, The Son of man must be delivered into the hands of sinful men, and
      be crucified, and the third day rise again.'
      n5a keeps its id and now retells it.

A NOTE ON THE INNER QUOTE. s6 has the angels quoting Jesus. A red-letter KJV does
NOT ink that clause -- it is a report of a report, and Luke is the one writing it.
It stays blue with the rest of the angels' speech rather than being split out red.

THE WOMEN NOW SPEAK. Luke 24 does not record the women saying anything at the
tomb -- checked, and nothing was invented to fill the gap. But Mark 16:3 records
these same women, on this same walk, in this same hour:
  w3  Mark 16:3  'Who shall roll us away the stone from the door of the
      sepulchre?'
  Lifted as WOMAN (pink) onto ST1. n0b carries the retelling. It is from Mark
  rather than Luke, and that is stated plainly here; it is the only recorded
  speech these women have in this scene, it is verbatim, and it sets up the
  rolled-away stone that n1 walks into two beats later. Left in on judgment.

NO RED: Jesus does not appear or speak in Luke 24:1-8.

NO GREEN: the Father does not speak.

WHY-LAW: they came carrying burial spices, planning to finish taking care of a
body, and were asked why they were looking for a living man in a graveyard.
Milk: the tomb could not hold him, and the stone they were worried about was
already gone before they got there.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import NARRATOR, SCRIPTURE, WOMAN

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "Very early on the first day of the week, while it was still dark, the women who loved him came to the tomb carrying spices to anoint his body. And the whole way there, one thing worried them."),
    # Mark 16:3
    ("w3", WOMAN, "Who shall roll us away the stone from the door of the sepulchre?"),
    ("n0b", NARRATOR, "It took several men to move it, and there were only a few women walking up that hill in the dark."),
    ("n1", NARRATOR, "But when they arrived, the huge stone that had sealed the tomb was rolled away."),
    ("n2a", NARRATOR, "They stepped inside — and the body was gone."),
    ("n2b", NARRATOR, "They stood there, confused and afraid."),
    ("n3", NARRATOR, "Then two figures in dazzling clothing stood beside them, and asked a question that has echoed for two thousand years:"),
    # Luke 24:5-6
    ("s5", SCRIPTURE, "Why seek ye the living among the dead? He is not here, but is risen:"),
    ("n4", NARRATOR, "He is not here — he is risen."),
    # Luke 24:6-7
    ("s6", SCRIPTURE, "remember how he spake unto you when he was yet in Galilee, Saying, The Son of man must be delivered into the hands of sinful men, and be crucified, and the third day rise again."),
    ("n5a", NARRATOR, "Remember, they said, what he told you back in Galilee — that he would be handed over to sinful men, and crucified, and on the third day rise again. He had said all of it, out loud, before any of it happened."),
    ("n5b", NARRATOR, "And they remembered."),
    ("card", NARRATOR, "The tomb couldn't hold him. Whatever feels dead and sealed shut in your life — he's the God of the rolled-away stone."),
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
