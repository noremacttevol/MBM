#!/usr/bin/env python3
"""Narration for build-44-pentecost — Acts 2 (SPEAKER-LAW).

Row 44 swapped 2026-07-23 from "The two debtors" (a double-telling of #74's Luke 7
scene) to Pentecost — the approved new story. See DRAFTS/row-044-pentecost.md.

Peter's quoted words are SCRIPTURE (verbatim KJV, light-blue) — he is an apostle,
not Jesus, so NOT red. Jesus does not speak here (post-Ascension); he is proclaimed.
Narrator is modern and never restates the adjacent KJV line (echo_scan clean).
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import NARRATOR, SCRIPTURE

SEGMENTS = [
    ("n1", NARRATOR, "Before Jesus went back to heaven, he told his followers to wait in Jerusalem — he was going to send them help. They did not fully understand what he meant. So they waited, and they prayed. Then one morning it came."),
    # Acts 2:2-3
    ("s1", SCRIPTURE, "And suddenly there came a sound from heaven as of a rushing mighty wind, and it filled all the house where they were sitting. And there appeared unto them cloven tongues like as of fire, and it sat upon each of them."),
    ("n2", NARRATOR, "The Holy Ghost filled every one of them. Ordinary people from Galilee began to speak in languages they had never learned. Jerusalem was packed that day with travelers from every nation — and each one heard the wonders of God in his own tongue."),
    ("n3", NARRATOR, "A crowd gathered, amazed and confused. Some mocked and said they were drunk. So Peter — the same man who had denied Jesus only weeks before — stood up in front of everyone, unafraid now, and told them the truth."),
    # Acts 2:23-24
    ("s2", SCRIPTURE, "Him, being delivered by the determinate counsel and foreknowledge of God, ye have taken, and by wicked hands have crucified and slain: whom God hath raised up, having loosed the pains of death."),
    ("n4", NARRATOR, "His message was not about himself, and not about the wind or the fire. It was about the man they had rejected — living again, exactly as he had promised. And Peter said the apostles had all seen him with their own eyes."),
    # Acts 2:36
    ("s3", SCRIPTURE, "Therefore let all the house of Israel know assuredly, that God hath made that same Jesus, whom ye have crucified, both Lord and Christ."),
    ("n5", NARRATOR, "The words went straight through them. They had helped condemn him — and God had lifted him up anyway, and given him a throne over everything. Cut to the very heart, they asked the only question left to ask."),
    # Acts 2:37
    ("s4", SCRIPTURE, "Men and brethren, what shall we do?"),
    # Acts 2:38
    ("s5", SCRIPTURE, "Repent, and be baptized every one of you in the name of Jesus Christ for the remission of sins, and ye shall receive the gift of the Holy Ghost."),
    ("n6", NARRATOR, "About three thousand people were baptized that same day. The church of Jesus Christ began — not with an army or a building, but with the Spirit poured out and a crowd who had finally understood who he really was. That same invitation is still open to you."),
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
