#!/usr/bin/env python3
"""Narration for build-27-leaven — Matthew 13.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

STAYED RED: the one existing red beat is Jesus in the flesh telling a parable, and
a red-letter KJV prints it.
  j1  Matthew 13:33  'The kingdom of heaven is like unto leaven, which a woman took,
      and hid in three measures of meal, till the whole was leavened.'
Checked word for word against the KJV -- it is exactly verbatim, and it stays red.

THE FRAMING SPLIT -- the only change this build needed. Matthew 13:33 reads in full:
'Another parable spake he unto them; The kingdom of heaven is like unto leaven...'.
The clause before 'The kingdom' is Matthew writing, and a red-letter KJV leaves it
black. It is now its own beat, ON THE SAME STILL S1 as j1 -- no new artwork, and the
edit the viewer sees is unchanged:
  s33  Matthew 13:33  'Another parable spake he unto them;'  SCRIPTURE, light blue.
n1 keeps its id and its place as the on-ramp before the frame, and n2 onward is
already the retelling, so nothing else moved.

NOTHING ELSE LIFTED. This parable is one verse long. Every other segment in the
build is the storyteller explaining what leaven and three measures of meal actually
were, and that is honest narrator work -- there is no further KJV buried in it to
lift out. Matthew 13:34-35 (Matthew's own comment, quoting Psalm 78:2) would be
`scripture` if it were wanted, but it is not in this build and adding it would
displace the warm personal ending the video already lands on. Left alone on purpose.

NO GREEN: no voice from heaven in Matthew 13.

WOMEN: there IS a woman at the centre of this parable, and she is the reason the
video exists -- but Matthew records nothing she SAYS. She is described, never
quoted. So there is no `woman` beat here; inventing one would be inventing
scripture. Nothing added.

PRONUNCIATION: nothing on the homograph list appears in the KJV line. 'leaven',
'leavened' and 'meal' all read correctly as written; no respellings, because a bad
respelling is worse than none.

WHY-LAW: he does not overpower you. He works small, hidden and patient, from the
inside, until the whole of you is changed and can feed somebody else.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "Jesus said the kingdom of God is like something a woman does every week, in her own kitchen, with her own hands."),
    # Matthew 13:33
    ("s33", SCRIPTURE, "Another parable spake he unto them;"),
    # Matthew 13:33
    ("j1", JESUS, "The kingdom of heaven is like unto leaven, which a woman took, and hid in three measures of meal, till the whole was leavened."),
    ("n2", NARRATOR, "Leaven is just a little piece of old, living dough, what we would call a sourdough starter. Small. Plain. Easy to overlook."),
    ("n3", NARRATOR, "And three measures of meal is not a small bowl. It is an enormous amount of flour, enough bread to feed a hundred people."),
    ("n4", NARRATOR, "She takes that tiny bit of leaven and works it down deep into the whole mass, hiding it, until you cannot even see where it went."),
    ("n5", NARRATOR, "Then she covers it and waits. Nothing looks like it is happening. No noise, no show, no spectacle. Just quiet, hidden time."),
    ("n6", NARRATOR, "But inside, the leaven is spreading through every part of the dough. And by morning the whole heavy mass has risen, alive, changed all the way through."),
    ("n7", NARRATOR, "That, Jesus said, is how the kingdom of God works. Not by force. Not by noise. It starts small and hidden, and it quietly changes everything it touches, from the inside out."),
    ("n8", NARRATOR, "That is how good he is. He does not overpower you. He works gently, patiently, from within, until the whole of you is warmed and changed and made into something that can feed other people."),
    ("card", NARRATOR, "God is often working quietest right where you cannot see it yet. Where might he already be at work inside you?"),
]

# Homographs this build decides for itself (never auto-replaced globally).
SPOKEN = {}


SPOKEN.update({'dough': 'doh'})  # round2 in-context A/B winners 2026-07-20 (SWEEP/round2-state.json)

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
