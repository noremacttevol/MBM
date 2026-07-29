#!/usr/bin/env python3
"""Narration for build-134 — Today shalt thou be with me in paradise
(Luke 23:42-43 + John 20:17).

ROW 134 (canonical, per THE-200 v2 repeat-purge 2026-07-20 — replaces the archived
other-sheep dupe). BRIDGE shelf. Wound answered: "one heaven, one chance, one size" —
mercy has more geography and more time than you were told. Bible only; Church not named.

SPEAKER-LAW: Jesus's words EXACT KJV, red. The dying thief is a man — his line is
SCRIPTURE, light-blue, NOT red. Narrator is plain modern English, white, never KJV.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

SEGMENTS = [
    ("n0", NARRATOR, "You may have been told there are only two doors when you die — one heaven, one hell — and the moment your heart stops, one of them slams shut forever. Two sentences from Jesus quietly open that picture wider."),
    ("n1", NARRATOR, "The first he said while he was dying. Next to him hung a criminal, a man who had earned his cross and knew it. And in his last hour, that man turned his head and asked Jesus to remember him."),
    # Luke 23:42 — the thief, a man: SCRIPTURE blue, not red
    ("s1", SCRIPTURE, "Lord, remember me when thou comest into thy kingdom."),
    # Luke 23:43
    ("j1", JESUS, "Verily I say unto thee, To day shalt thou be with me in paradise."),
    ("n2", NARRATOR, "Today. Not after a lifetime of good behavior, not after religion had its say — today. Mercy reached a dying thief at the very last minute. Most people know that verse. Here is the one almost nobody sets beside it."),
    ("n3", NARRATOR, "Three days later, on Easter morning, Mary reaches for the risen Jesus, and he stops her with something strange:"),
    # John 20:17
    ("j2", JESUS, "Touch me not; for I am not yet ascended to my Father:"),
    ("n4", NARRATOR, "Read those two slowly, side by side. On Friday he told the thief they would be together in paradise that same day. On Sunday he says he has not yet gone up to his Father. Which means the paradise he promised the thief was not yet the final home with the Father. It was somewhere in between — real, and good, and not the end of the road."),
    ("n5", NARRATOR, "That should change how you grieve. The people you love who died without every box checked did not fall through a trapdoor. Mercy has more room than you were told, and more time. There is a place still called paradise, a place of waiting, and the Shepherd is there too."),
    ("card", NARRATOR, "If mercy could reach a thief in his last sixty seconds, and if the road past death is longer and kinder than you were taught — who have you already given up on that God has not?"),
]

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
