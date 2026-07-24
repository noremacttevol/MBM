#!/usr/bin/env python3
"""Narration for build-165-laying-on-hands — Acts 8.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

Both red segments were misattributions. Acts 8 is Luke writing the history of
the Church — Jesus does not speak anywhere in this passage. kv14 and kv17 both
move JESUS-RED -> SCRIPTURE (light blue). Two lines out of red.

Two verses were buried inside narrator paraphrase and are now lifted so the
viewer hears Luke state the pattern himself instead of being told about it:
  s15  Acts 8:15  'Who, when they were come down, prayed for them...'
  s16  Acts 8:16  'For as yet he was fallen upon none of them...'
Both are Luke narrating, so both are SCRIPTURE. Each is followed immediately by
the existing narrator beat that already retells it (n3 retells s15, n4 retells
s16), so no new narration was needed.

No mixed segments here — every quoted line is Luke start to finish, so nothing
was split.

All original ids kept (n1, n2, kv14, n3, n4, n5, kv17, n6, n7, card). New ids
are s15 and s16 only. New beats reuse S4 and S5; no new artwork.

MILK: the doctrine — the Holy Ghost conferred by the laying on of hands under
authority — is carried entirely by Acts 8:16 and 8:17 sitting next to each
other. Nothing on screen argues it. The verse and the picture agree and the
viewer draws the conclusion.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "A wave of faith had swept through Samaria. Whole crowds had heard the good news, believed it with glad hearts, and been baptized in water. Something real and joyful was happening among them."),
    ("n2", NARRATOR, "Word of it reached the apostles back in Jerusalem. And notice their response: they did not simply send a letter of congratulations. They sent two of their own number, Peter and John, to go down in person."),
    # Acts 8:14
    ("kv14", SCRIPTURE, "Now when the apostles which were at Jerusalem heard that Samaria had received the word of God, they sent unto them Peter and John:"),
    # Acts 8:15
    ("s15", SCRIPTURE, "Who, when they were come down, prayed for them, that they might receive the Holy Ghost:"),
    ("n3", NARRATOR, "And here is the surprising part: even though these people already believed, and had already been baptized, the gift had not yet come to a single one of them."),
    # Acts 8:16
    ("s16", SCRIPTURE, "For as yet he was fallen upon none of them: only they were baptized in the name of the Lord Jesus."),
    ("n4", NARRATOR, "So the water alone had not been enough. Their faith was sincere and their baptism was real, yet the promised gift of the Spirit still waited on something more — on the hands of those God had given authority."),
    ("n5", NARRATOR, "Then Peter and John did the simple, deliberate thing Luke records so plainly. They laid their hands on each believer. And in that moment, under that authority, the gift finally came."),
    # Acts 8:17
    ("kv17", SCRIPTURE, "Then laid they their hands on them, and they received the Holy Ghost."),
    ("n6", NARRATOR, "Here is the quiet study gem. The gift of the Holy Ghost did not arrive by sincerity alone, or by baptism alone. It travelled by authority — conferred through the laying on of hands by those God had sent. Order and gift belong together."),
    ("n7", NARRATOR, "And that same gift is still offered to you, by that same pattern. Faith and baptism open the door, and then, by the hands of those with authority, the Comforter is given to be with you. When that gift is offered to you, will you receive it?"),
    ("card", NARRATOR, "Samaria believed and was baptized, but the Holy Ghost came only when the apostles laid their hands on them. The gift travels by authority. When that gift is offered to you, will you receive it?"),
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
