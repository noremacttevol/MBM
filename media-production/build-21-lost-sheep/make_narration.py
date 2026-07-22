#!/usr/bin/env python3
"""Narration for build-21-lost-sheep — Luke 15.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

STAYED RED: all four existing red beats are Jesus in the flesh, and a red-letter
KJV prints the whole parable red -- including the shepherd's own call to his
neighbours, which is Jesus's words in a character's mouth.
  j1  Luke 15:4  'What man of you, having an hundred sheep...'
  j2  Luke 15:5  'And when he hath found it, he layeth it on his shoulders, rejoicing.'
  j3  Luke 15:6  'Rejoice with me; for I have found my sheep which was lost.'  <- the
      shepherd inside the parable. STAYS RED. Not blue.
  j4  Luke 15:7  'I say unto you, that likewise joy shall be in heaven...'
Nothing here has Luke's framing welded onto it, so nothing needed splitting.

ADDED BLUE, OUTSIDE THE PARABLE. The Pharisees and scribes who set the whole
thing off were speaking in the storyteller's white voice as paraphrase in n2.
They are men in Luke's narrative frame, not characters in the parable, so they
are SCRIPTURE, light blue:
  s2  Luke 15:2  'This man receiveth sinners, and eateth with them.'
n2 is trimmed to the frame only -- 'And the religious men muttered about it.' --
and n2b carries the retelling that n2 used to carry, word for word. Both stay on
the SAME still S1, so the picture is unchanged.
The complaint is the thing the parable answers, and hearing it in a real voice
makes the answer land.

RETELLING RULE: j3 and j4 ran back to back with no storyteller between them, and
they are not a question-and-answer pair -- j3 is the shepherd in the story and j4
is Jesus stepping out of the story to apply it. n9b now sits between them on the
same still S7, retelling the shepherd's call before the application lands. n10
was already retelling j4 and is untouched.

WOMEN: Luke 15:1-7 records no woman speaking. The woman with the lost coin is
the very next parable, Luke 15:8-10, and is outside this build's passage --
nothing was pulled in from it and nothing was invented.

NO GREEN: no voice from heaven in Luke 15:1-7.

WHY-LAW: he does not stand there counting what he still has. Heaven throws a
party over one person turning back -- not a lecture, not a grudge. Joy.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "The people everyone else had written off — the cheats, the outcasts, the ones with a past — kept crowding in close to hear Jesus."),
    ("n2", NARRATOR, "And the religious men muttered about it."),
    # Luke 15:2
    ("s2", SCRIPTURE, "This man receiveth sinners, and eateth with them."),
    ("n2b", NARRATOR, "This man welcomes sinners, they said, and even eats with them."),
    ("n3", NARRATOR, "So Jesus told them a story about how heaven really feels about one lost person."),
    # Luke 15:4
    ("j1", JESUS, "What man of you, having an hundred sheep, if he lose one of them, doth not leave the ninety and nine in the wilderness, and go after that which is lost, until he find it?"),
    ("n4", NARRATOR, "Which of you, he asks, with a hundred sheep, would not leave the ninety-nine behind to go after the one that wandered off, and keep searching until you found it?"),
    ("n5", NARRATOR, "He does not stand there counting what he still has. He leaves the ninety-nine behind to go out after the one that is gone."),
    ("n6", NARRATOR, "He searches through the night, over the rocks and the ravines, calling into the dark, because to him that one is not a loss he can shrug off. That one is his."),
    ("n7", NARRATOR, "And when he finds it — frightened, tangled in the thorns, too worn out to walk — he does not scold it, and he does not leave it there."),
    # Luke 15:5
    ("j2", JESUS, "And when he hath found it, he layeth it on his shoulders, rejoicing."),
    ("n8", NARRATOR, "He lifts it up, lays it across his own shoulders, and carries it the whole way home, rejoicing. Not relieved. Not annoyed at the trouble. Rejoicing."),
    ("n9", NARRATOR, "Then he calls everyone together — friends, neighbors, the whole village — and throws a celebration."),
    # Luke 15:6
    ("j3", JESUS, "Rejoice with me; for I have found my sheep which was lost."),
    ("n9b", NARRATOR, "Be glad with me, he tells them. I have found my sheep, the one that was lost. Not, I got my property back. My sheep. It was his the whole time it was missing."),
    # Luke 15:7
    ("j4", JESUS, "I say unto you, that likewise joy shall be in heaven over one sinner that repenteth, more than over ninety and nine just persons, which need no repentance."),
    ("n10", NARRATOR, "That is how good he is. Heaven throws a party over one person turning back. Not a lecture. Not a grudge. Joy."),
    ("card", NARRATOR, "To him, you were never one of a crowd. Have you ever felt like the one who wandered too far to be worth coming after?"),
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
