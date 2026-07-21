#!/usr/bin/env python3
"""Narration for build-131-scribe-near-the-kingdom — Mark 12.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

STAYED RED: j1 'Thou art not far from the kingdom of God' is Mark 12:34, Jesus in
the flesh, red-letter. Correct as it stood. The KJV frame - 'And when Jesus saw
that he answered discreetly, he said unto him' - is not in the segment, and n3
already does that framing in the storyteller's modern voice, so no split was
needed.

THE FIX THIS BUILD EXISTED FOR - the exchange was never an exchange. Every word
of it, both men's, was narrator paraphrase in white. The video is a conversation
between two people and neither of them spoke. Three lifts, all verbatim:
  s28   Mark 12:28  'Which is the first commandment of all?'  SCRIPTURE. The
        scribe's actual question; n0b keeps its text and retells it.
  jv29  Mark 12:29-31  'The first of all the commandments is, Hear, O Israel...'
        JESUS, RED. Note carefully: he is quoting Deuteronomy 6 and Leviticus 19,
        and it STAYS RED - the test is who is talking, and it is him. n1 keeps its
        text and becomes the retelling.
  s32   Mark 12:32-33  'Well, Master, thou hast said the truth...'  SCRIPTURE.
        This is the hinge of the whole video and it was a one-line paraphrase.
        The scribe is not conceding a debate; he is agreeing out loud and then
        going further than he was asked to. n2 keeps its text and retells it.

Nothing was rewritten. Every narrator beat kept its original words; they simply
moved from standing in for the speakers to explaining them afterward.

ADDED: nothing new. The seven original beats plus three lifted verses.

WOMEN: Mark 12:28-34 records no woman speaking. The widow with her two mites is
only nine verses later in the same chapter and she says nothing - Mark records no
words from her at all. Nothing added, nothing invented.

WHY-LAW: the man was not tricked into being close to the kingdom and he was not
flattered into it. He thought honestly out loud, and Jesus told him the truth
about where that put him. Milk framing - honest thinking gets you nearer than you
expect.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0a", NARRATOR, "A teacher of the law came to Jesus with a real question, not a trap —"),
    # Mark 12:28
    ("s28", SCRIPTURE, "Which is the first commandment of all?"),
    ("n0b", NARRATOR, "which commandment matters most of all?"),
    # Mark 12:29-31
    ("jv29", JESUS, "The first of all the commandments is, Hear, O Israel; The Lord our God is one Lord: And thou shalt love the Lord thy God with all thy heart, and with all thy soul, and with all thy mind, and with all thy strength: this is the first commandment. And the second is like, namely this, Thou shalt love thy neighbour as thyself. There is none other commandment greater than these."),
    ("n1", NARRATOR, "Jesus answered without hesitation. Love God with everything you are. And love your neighbor as yourself. Everything else hangs on those two."),
    # Mark 12:32-33
    ("s32", SCRIPTURE, "Well, Master, thou hast said the truth: for there is one God; and there is none other but he: And to love him with all the heart, and with all the understanding, and with all the soul, and with all the strength, and to love his neighbour as himself, is more than all whole burnt offerings and sacrifices."),
    ("n2", NARRATOR, "The scribe agreed — and added something honest: to love God and neighbor is worth more than any burnt offering."),
    ("n3", NARRATOR, "Jesus looked at him and saw a man thinking clearly, with an open heart."),
    # Mark 12:34
    ("j1", JESUS, "Thou art not far from the kingdom of God."),
    ("n4", NARRATOR, "Not far. The man was close — a step from the door. And no one dared question Jesus after that."),
    ("card", NARRATOR, "You may be closer than you think. Love God, love your neighbor — and step through the door."),
]

# Homographs this build decides for itself (never auto-replaced globally).
SPOKEN = {}


async def main():
    os.makedirs("audio", exist_ok=True)
    for name, speaker, text in SEGMENTS:
        flagged = [w for w in audit(text) if w not in SPOKEN]
        if flagged:
            print(f"  ! {name}: undecided homograph(s) {flagged}")
        await save_speaker_narration(spoken_text(text, SPOKEN), speaker,
                                     f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3  [{speaker}]")


if __name__ == "__main__":
    asyncio.run(main())
