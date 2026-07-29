#!/usr/bin/env python3
"""Narration for build-87-boy-in-the-temple — Luke 2.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

MARY SPEAKS -- IN PINK -- AND SHE WAS NOT IN THE VIDEO AT ALL. This is the fix
this build existed for. n2 said 'His mother, relieved and worried, asked why he'd
done this to them' -- a modern paraphrase, in white, standing in for one of the
most human sentences any mother says in scripture. Lifted verbatim as `woman`:
  w48  Luke 2:48  'Son, why hast thou thus dealt with us? behold, thy father and
       I have sought thee sorrowing.'
  n2 is trimmed to the frame and n2b carries the retelling. Both on ST6, no new
  artwork. Hear what she actually says: not 'where were you' but 'we have been
  looking for you, SORROWING'. Three days of it. That is a mother telling her son
  what it cost, and the video was throwing the line away in a subordinate clause.

STAYED RED: j1, Luke 2:49, 'How is it that ye sought me? wist ye not that I must
be about my Father's business?' Jesus in the flesh, red-lettered, verbatim -- and
these are the first recorded words of his life. Unchanged, id kept.

RETELLING ADDED: n2c after j1, on ST7. The one red line in the build had no plain
modern landing, and 'wist ye not' and 'my Father's business' are both phrases a
listener today will not parse on the fly.

THE MOTHER-AND-SON EXCHANGE IS DELIBERATELY BACK TO BACK. w48 (pink) runs
straight into j1 (red) with n2b's retelling in between, which is where it has to
go -- her line and his answer are a real question and a real answer, and n2b hands
off into the reply rather than breaking the exchange. This is the shape the law
sets out for build-98's 'Mary.' / 'Rabboni.', adapted for the fact that here the
retelling belongs to her line and not to his.

PRONUNCIATION: 'wist' is already in the global SPOKEN map, so nothing is added to
this build's `spoken` -- a duplicate local entry is exactly how the audited-bad
respellings got in.

NO GREEN: Jesus talks ABOUT his Father here; the Father does not speak. Nothing in
Luke 2:41-52 is a voice from heaven.

WHY-LAW: at twelve years old he already knew whose he was and where he belonged,
and then he went home and obeyed his parents anyway. Milk: knowing who your Father
is does not make you too important for ordinary life.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, WOMAN

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0a", NARRATOR, "Every year Jesus's family went to Jerusalem for the Passover. When he was twelve, they made the trip as usual."),
    ("n0b", NARRATOR, "On the way home, they realized he wasn't with them."),
    ("n1a", NARRATOR, 'They turned back, searching for three days.'),
    ("n1b", NARRATOR, 'And they found him in the temple, sitting among the teachers, listening,'),
    ("n1c", NARRATOR, 'and asking questions that amazed everyone.'),
    ("n2", NARRATOR, 'His mother was the one who spoke. Relieved, and frightened, and hurt, Mary said this:'),
    ("w48", WOMAN, 'Son, why hast thou thus dealt with us? behold, thy father and I have sought thee sorrowing.'),
    ("n2b", NARRATOR, 'she said. Your father and I have been looking for you, sick with worry. Listen to the word Luke gives her — sorrowing. Not annoyed. Grieving. Three days of a mother assuming the worst. And he answered her with a question of his own.'),
    ("j1", JESUS, "How is it that ye sought me? wist ye not that I must be about my Father's business?"),
    ("n2c", NARRATOR, "Why were you out looking for me? he said. Didn't you know I had to be in my Father's house, about my Father's work? He was twelve years old. He was not being smart with his mother. He genuinely could not imagine where else they thought he would be."),
    ("n3", NARRATOR, "They didn't fully understand. But he went home with them and obeyed them — and he kept growing in wisdom, in stature, and in favor with God and people."),
    ("card", NARRATOR, "Even as a boy he knew where he belonged. You were made for the Father's house too — come find your place."),
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
