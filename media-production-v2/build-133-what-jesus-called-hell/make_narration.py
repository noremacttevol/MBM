#!/usr/bin/env python3
"""Narration for build-133 — What Jesus called hell (Mark 9:43-48; Matt 5:22).

ROW 133 (canonical, per THE-200 v2 repeat-purge 2026-07-20 — replaces the archived
many-mansions dupe). BRIDGE shelf. Wound answered: "one heaven, one chance, one size"
/ the inherited torture-chamber picture of hell. Bible only; the Church is not named.

SPEAKER-LAW: Jesus's words are EXACT KJV, red. Everything the narrator says is plain
modern English, white — never KJV. No women, no Deity voice in this cut.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR

SEGMENTS = [
    ("n0", NARRATOR, "You were probably taught that hell is a torture chamber, and that God keeps most of his children there forever. Jesus did warn about hell. But the word he used, and the place he pointed at, are not what tradition made them."),
    ("n1", NARRATOR, "When Jesus said hell, the word in his language was Gehenna — and everyone listening knew exactly what he meant. It was a real place. A valley just outside the wall of Jerusalem."),
    ("n2", NARRATOR, "The valley of Hinnom. Long before, terrible things had happened there, and by Jesus' day it had become the city's burning garbage dump — fires that smoldered day and night, always another load, the smoke never seeming to stop."),
    ("n3", NARRATOR, "So when Jesus said this, he was pointing at a smoking valley his listeners could have walked to that same afternoon:"),
    # Mark 9:43
    ("j1", JESUS, "And if thy hand offend thee, cut it off: it is better for thee to enter into life maimed, than having two hands to go into hell, into the fire that never shall be quenched:"),
    # Mark 9:47
    ("j2", JESUS, "And if thine eye offend thee, pluck it out: it is better for thee to enter into the kingdom of God with one eye, than having two eyes to be cast into hell fire:"),
    # Mark 9:48
    ("j3", JESUS, "Where their worm dieth not, and the fire is not quenched."),
    ("n4", NARRATOR, "He used the most vivid picture his listeners owned — the ever-burning dump — to say something deadly serious: sin is worth cutting loose from, and what you carry into eternity matters. He would not have loved them enough to warn them if it did not."),
    ("n5", NARRATOR, "But notice what he did NOT say. He never described God shoveling his own children into a dungeon to torture them forever for his pleasure. That picture — the pit, the pitchfork, the endless screaming — came later, from tradition and from paintings. It did not come from him."),
    ("n6", NARRATOR, "The God Jesus actually showed was a shepherd who leaves ninety-nine to chase one, a father who runs down the road. That God warns you about the fire the way a parent yanks a child back from a cliff — because he wants you, not because he is hunting for a reason to lose you."),
    ("card", NARRATOR, "What if the God you were afraid of was never the God who warned you — but the God who came to carry you past the fire himself? Who taught you to fear him more than to trust him?"),
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
