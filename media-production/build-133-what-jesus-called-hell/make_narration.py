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
    ("n0", NARRATOR, 'Many of the pictures people carry of hell came through centuries of art and tradition. Jesus did give severe warnings. But to hear one of his most famous warnings clearly, start with the history inside the word Gehenna.'),
    ("n1", NARRATOR, "Gehenna is the Greek form of the name Valley of Hinnom, a real ravine along the southern side of Jerusalem. Long before Jesus, that name had become a memory of one of Judah's darkest apostasies."),
    ("n2", NARRATOR, 'The prophets condemned a place there called Topheth, where children had been passed through fire. Jeremiah said it would be called the Valley of Slaughter. The name carried shame, ruin, and judgment.'),
    ("n3", NARRATOR, "By the time Mark recorded Jesus' warning, Gehenna was a place-name charged with that biblical history. Jesus used it, along with the closing image from Isaiah of fire and the worm, to make the danger of sin impossible to ignore:"),
    ("j1", JESUS, 'And if thy hand offend thee, cut it off: it is better for thee to enter into life maimed, than having two hands to go into hell, into the fire that never shall be quenched:'),
    ("j2", JESUS, 'And if thine eye offend thee, pluck it out: it is better for thee to enter into the kingdom of God with one eye, than having two eyes to be cast into hell fire:'),
    ("j3", JESUS, 'Where their worm dieth not, and the fire is not quenched.'),
    ("n4", NARRATOR, "The images are deliberately severe. Hand and eye name things as precious as parts of your own body, yet no cherished sin is worth surrendering life in God's kingdom. Love does not make the warning smaller. Love tells the truth about what destroys us."),
    ("n5", NARRATOR, 'Later art supplied pitchforks, elaborate torture chambers, and maps of the underworld. Scripture itself uses several warning images: death, destruction, darkness, exclusion, and fire. The images are meant to call you back, not satisfy curiosity about every detail beyond death.'),
    ("n6", NARRATOR, 'Read the warning beside the whole life of the speaker: the shepherd who searches for the lost, the father who runs down the road, the Savior who enters death to bring people home. He warns because sin destroys and because he came to save.'),
    ("card", NARRATOR, 'The warning is real. So is the rescue. What would you leave behind if you trusted that the one warning you is also the one searching for you?'),
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
