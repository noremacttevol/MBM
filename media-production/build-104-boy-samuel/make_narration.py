#!/usr/bin/env python3
"""Narration for build-104-boy-samuel — 1 Samuel 3.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

One red beat, and 1 Samuel is Old Testament, so it cannot be red:
  jv10  1 Samuel 3:10  'Samuel, Samuel.'  — Jehovah calling the boy. GOD, green.

MIXED SEGMENT SPLIT: `ns` read 'And the boy answered: Speak; for thy servant
heareth.' — a narrator frame welded to a verbatim KJV line, so no single colour
was correct. `ns` keeps its id and now carries only Samuel's actual words as
SCRIPTURE (light blue). The dropped frame is picked up by n7, which already
begins with the retelling. Same still, same edit.

LIFTED FROM PARAPHRASE (three lines, all 1 Samuel 3):
  s5a  3:5  Samuel  'Here am I; for thou calledst me.'
  s5b  3:5  Eli     'I called not; lie down again.'
  s9   3:9  Eli     'Go, lie down: and it shall be, if he call thee...'
All three were sitting inside narrator paraphrase. The whole point of this story
is a boy learning what to say, so the viewer should hear the actual words being
taught and then actually used. Eli and Samuel are both people in the story, so
both are SCRIPTURE, never GOD.

EDITS TO EXISTING NARRATOR TEXT: n3 lost its trailing 'and said, here I am; you
called me' because s5a now says it verbatim. n6 was rewritten as a retelling of
s9 instead of a paraphrase that pre-empted it. n4a is a new short retelling so
s5a is not left hanging in Old English. Every other narrator beat is untouched.

NO WOMEN: 1 Samuel 3 records no woman speaking. Hannah's prayer is chapter 1 and
belongs to build 149.

WHY-LAW: God calls a child by name and waits, patiently, through three wrong
answers. Milk framing — revelation is quiet, personal, and does not require you
to be impressive.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import GOD, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "In those days the word of the Lord was rare. People had stopped hearing from God, and it was a quiet, dim time. But one small lamp still burned in the house of God at night — and a boy slept nearby."),
    ("n2", NARRATOR, "Samuel was only a child, given to serve in the tabernacle. He lay asleep on his mat near the holy place while the old priest Eli, nearly blind with age, slept in his room."),
    ("n3", NARRATOR, "And in the dark, a voice called his name. Samuel. He sat straight up. He thought it was old Eli needing him, so he ran to him."),
    # 1 Samuel 3:5
    ("s5a", SCRIPTURE, "Here am I; for thou calledst me."),
    ("n4a", NARRATOR, "Here I am — you called me. A boy standing in the doorway in the middle of the night, ready to work. But the old man had not called him."),
    # 1 Samuel 3:5
    ("s5b", SCRIPTURE, "I called not; lie down again."),
    ("n4", NARRATOR, "But Eli said, I did not call you. Go back and lie down. So he did. And the voice came again — Samuel — and again he ran to the old man, and again Eli sent him back. It happened a third time."),
    ("n5", NARRATOR, "Then Eli understood. This was no dream, and it was not his voice. It was God himself, calling the child. So the old priest gently taught the boy what to do."),
    # 1 Samuel 3:9
    ("s9", SCRIPTURE, "Go, lie down: and it shall be, if he call thee, that thou shalt say, Speak, LORD; for thy servant heareth."),
    ("n6", NARRATOR, "Do not run to me, Eli told him. Go lie back down. And if the voice comes again, answer it yourself — say, speak, Lord, your servant is listening. So Samuel went and lay down in his place, and waited in the dark."),
    # 1 Samuel 3:10
    ("jv10", GOD, "Samuel, Samuel."),
    # 1 Samuel 3:10
    ("ns", SCRIPTURE, "Speak; for thy servant heareth."),
    ("n7", NARRATOR, "Speak — I am listening. That was all God had been waiting for. A heart small enough and open enough to stop running around and simply listen. And God spoke to him, and told him true things, and stayed with him."),
    ("n8", NARRATOR, "Samuel grew, and the Lord was with him, and let none of his words fall to the ground. The child who learned to listen in the dark became the voice God used to speak to a whole nation. It began with a boy saying, speak — I am listening."),
    ("card", NARRATOR, "God called a child by name, in the dark, and waited until he was ready to listen. He is patient like that still. If a voice were gently calling your name, could you say it too — speak, I am listening?"),
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
