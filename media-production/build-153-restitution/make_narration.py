#!/usr/bin/env python3
"""Narration for build-153-restitution — Acts 3.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

Acts 3 is Luke recording Peter preaching on Solomon's porch. Jesus does not
speak anywhere in this chapter, so a red-letter King James Bible prints none
of it red. Both red beats move to SCRIPTURE (light blue):
  kv19  Acts 3:19  'Repent ye therefore, and be converted...'  RED -> SCRIPTURE
  kv21  Acts 3:21  'Whom the heaven must receive...'           RED -> SCRIPTURE

No mixed segments — both verses are Peter start to finish, so nothing is split.

ADDED: s6 lifts Acts 3:6 out of n1's paraphrase. n1 said 'after a lame man was
healed' and skipped past the most quoted line in the chapter — the words Peter
actually spoke at the gate. It stays on S1, the temple still, so no new artwork
is needed, and the new n1b retells it in modern English right after.

WHY-LAW: milk. The restitution of all things is left to say what Peter said —
everything set right, promised by every prophet since the world began. The
video does not name the Restoration or argue for it; it lets the word
'restitution' sit there and be looked up.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "After a lame man was healed at the temple gate, a crowd came running, amazed. And Peter, a fisherman turned preacher, stood up among them to explain what they had really just seen."),
    # Acts 3:6
    ("s6", SCRIPTURE, "Silver and gold have I none; but such as I have give I thee: In the name of Jesus Christ of Nazareth rise up and walk."),
    ("n1b", NARRATOR, "I have no money, Peter told him. But what I do have, I give you. And in the name of Jesus Christ of Nazareth, he told a man who had never walked to stand up. He had nothing in his pockets, and he gave away the only thing he had that was worth anything."),
    ("n2", NARRATOR, "His message was not complicated. Turn back to God, he said. Change your direction, let your wrongs be wiped away, and something good will follow — not someday far off, but seasons of relief, sent from God himself."),
    ("n3", NARRATOR, "Picture that word: refreshing. Like cool rain on cracked ground, like a deep breath after a long, hard road. That is what God longs to pour out on people who simply turn back toward him."),
    # Acts 3:19
    ("kv19", SCRIPTURE, "Repent ye therefore, and be converted, that your sins may be blotted out, when the times of refreshing shall come from the presence of the Lord;"),
    ("n4", NARRATOR, "But Peter pointed to something even larger than one person's fresh start. He spoke of a day when everything that has gone wrong with the world would finally be set right — a healing not only of people, but of all things."),
    ("n5", NARRATOR, "Until that day, he said, heaven itself is keeping the promise safe, the way you hold back the best gift for exactly the right moment. It is coming, but at the appointed time, and not a moment before."),
    ("n6", NARRATOR, "And this was not some new idea Peter dreamed up. Every true prophet, all the way back to the beginning, had promised the very same thing: a great restoring, a putting-right of everything, spoken of since the world began."),
    # Acts 3:21
    ("kv21", SCRIPTURE, "Whom the heaven must receive until the times of restitution of all things, which God hath spoken by the mouth of all his holy prophets since the world began."),
    ("n7", NARRATOR, "Restitution means giving back what was lost, restoring what was broken to the way it was always meant to be. Not patched up, not almost — made whole, made new, every part of it."),
    ("n8", NARRATOR, "So this verse is a promise you can lean your full weight on. The world is not just sliding into ruin; it is heading toward a restoration God has planned from the very start. So the only question is a hopeful one. Will you turn, and be part of the refreshing when it comes?"),
    ("card", NARRATOR, "The world is not ending in ruin. It is heading toward a restoration of all things, promised by every prophet since the beginning. Turn back to God, and be refreshed. Will you be ready for the restoring?"),
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
