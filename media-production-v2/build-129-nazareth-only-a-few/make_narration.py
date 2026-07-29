#!/usr/bin/env python3
"""Narration for build-129-nazareth-only-a-few — Mark 6.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

MOVED OFF RED - THE MAIN FIX. s1 was painted Jesus-red and Jesus is not speaking
in it at all. 'And he could there do no mighty work, save that he laid his hands
upon a few sick folk, and healed them. And he marvelled because of their
unbelief' is Mark 6:5-6, MARK NARRATING. That is the evangelist writing, so it is
now SCRIPTURE, light blue. Exactly the case PLAN-AUTHORING calls out: narration
inside the Gospels is `scripture`, not `jesus`.

LIFTED - the townspeople, who were the whole problem and never got to speak.
  s3  Mark 6:3  'Is not this the carpenter, the son of Mary, the brother of
      James, and Joses, and of Juda, and Simon? and are not his sisters here with
      us?'  SCRIPTURE. The still ST2 is literally named 'isnt-this-the-carpenter'
      and the line it was named for was never spoken in the video. n1 keeps its
      original text and now works as the retelling right after it.

NEW RED, CORRECTLY. jv4 Mark 6:4 'A prophet is not without honour, but in his own
country, and among his own kin, and in his own house.' The famous line of this
passage was missing entirely. It IS red-letter - Jesus speaking in the flesh. The
KJV frame 'But Jesus said unto them,' is deliberately NOT included, so no split
was needed; the segment is his words only. n1b is its retelling.

ADDED: n3b, so ST6 ('the healed few') gets used, and n4 moves to ST7 ('the door
faith opens') which matches its line about faith opening the door. The original
build left ST7 unused.

WOMEN: Mary is NAMED in Mark 6:3 - 'the son of Mary' - and his sisters are
mentioned, but Mark records none of them speaking anywhere in this passage.
Nothing was added, because there is nothing verbatim to add. Not invented.

WHY-LAW: his power did not run out in Nazareth. Their willingness did. And even
then he healed the few who came anyway - the mercy did not shrink to match the
unbelief.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, 'Jesus went back to Nazareth, the town that watched Him grow up. He taught in the synagogue.'),
    ("s3", SCRIPTURE, 'Is not this the carpenter, the son of Mary, the brother of James, and Joses, and of Juda, and Simon? and are not his sisters here with us?'),
    ("n1", NARRATOR, "But the people who'd known Him as a boy couldn't believe. They took offense at Him — and their unbelief became a wall."),
    ("jv4", JESUS, 'A prophet is not without honour, but in his own country, and among his own kin, and in his own house.'),
    ("n1b", NARRATOR, 'A prophet gets honored everywhere, He said — everywhere except home. Except among his own relatives. Except in his own house.'),
    ("n2", NARRATOR, "He could do only a few mighty works there. Not because His power ran out, but because they wouldn't receive it."),
    ("s1", SCRIPTURE, 'And he could there do no mighty work, save that he laid his hands upon a few sick folk, and healed them. And he marvelled because of their unbelief.'),
    ("n3", NARRATOR, "Even amazement at their doubt didn't stop His mercy."),
    ("n3b", NARRATOR, 'A few sick folk. That is all Nazareth brought Him, and He laid His hands on every one of them. The mercy never shrank down to match the unbelief.'),
    ("n4", NARRATOR, 'Faith opens the door. Where people believed, even a little, He worked.'),
    ("card", NARRATOR, 'He healed the few who reached out. The door is the same today — believe, and let Him work.'),
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
