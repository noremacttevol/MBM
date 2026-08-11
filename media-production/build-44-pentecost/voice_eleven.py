#!/usr/bin/env python3
"""Voice build-44-pentecost (Acts 2) with the LOCKED ElevenLabs cast.

Row 44 swapped 2026-07-23 from "two debtors" (a double-telling of #74) to
Pentecost. This is a NEW build with NO V1 audio, so the narration track is
voiced here from scratch (ElevenLabs, not edge-tts) and the V2 assembler is
told AUDIO_FROM_V1_SEGMENTS = True so it renders from these very mp3s.

SPEAKER LAW: narrator = Brian; Peter's quoted KJV / the crowd's question / the
scripture = Roger (SCRIPTURE voice, light-blue captions — Peter is an apostle,
not Jesus, so NOT red). Jesus does not speak here (post-Ascension).
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
MP = os.path.dirname(HERE)                       # media-production
sys.path.insert(0, MP)
sys.path.insert(0, HERE)

import mbm_eleven
from mbm_speakers import NARRATOR, SCRIPTURE

# The 11 spoken segments (make_narration.SEGMENTS, verbatim).
SEGMENTS = [
    ("n1", NARRATOR, "Before Jesus went back to heaven, he told his followers to wait in Jerusalem — he was going to send them help. They did not fully understand what he meant. So they waited, and they prayed. Then one morning it came."),
    ("s1", SCRIPTURE, "And suddenly there came a sound from heaven as of a rushing mighty wind, and it filled all the house where they were sitting. And there appeared unto them cloven tongues like as of fire, and it sat upon each of them."),
    ("n2", NARRATOR, "The Holy Ghost filled every one of them. Ordinary people from Galilee began to speak in languages they had never learned. Jerusalem was packed that day with travelers from every nation — and each one heard the wonders of God in his own tongue."),
    ("n3", NARRATOR, "A crowd gathered, amazed and confused. Some mocked and said they were drunk. So Peter — the same man who had denied Jesus only weeks before — stood up in front of everyone, unafraid now, and told them the truth."),
    ("s2", SCRIPTURE, "Him, being delivered by the determinate counsel and foreknowledge of God, ye have taken, and by wicked hands have crucified and slain: whom God hath raised up, having loosed the pains of death."),
    ("n4", NARRATOR, "His message was not about himself, and not about the wind or the fire. It was about the man they had rejected — living again, exactly as he had promised. And Peter said the apostles had all seen him with their own eyes."),
    ("s3", SCRIPTURE, "Therefore let all the house of Israel know assuredly, that God hath made that same Jesus, whom ye have crucified, both Lord and Christ."),
    ("n5", NARRATOR, "The words went straight through them. They had helped condemn him — and God had lifted him up anyway, and given him a throne over everything. Cut to the very heart, they asked the only question left to ask."),
    ("s4", SCRIPTURE, "Men and brethren, what shall we do?"),
    ("s5", SCRIPTURE, "Repent, and be baptized every one of you in the name of Jesus Christ for the remission of sins, and ye shall receive the gift of the Holy Ghost."),
    ("n6", NARRATOR, "About three thousand people were baptized that same day. The church of Jesus Christ began — not with an army or a building, but with the Spirit poured out and a crowd who had finally understood who he really was. That same invitation is still open to you."),
]

SPOKEN = {}  # no undecided homographs in this passage (draft §HOMOGRAPH FLAGS)


def main():
    os.makedirs(os.path.join(HERE, "audio"), exist_ok=True)
    raw = open(os.path.join(MP, "elevenlabs API KEY.txt")).read()
    key = re.search(r"sk_[A-Za-z0-9]+", raw).group(0)
    for name, speaker, text in SEGMENTS:
        spoken = mbm_eleven.eleven_spoken_text(text, SPOKEN)
        out = os.path.join(HERE, "audio", f"{name}.mp3")
        sents = mbm_eleven.render_segment(spoken, speaker, out, key=key)
        dur = sents[-1]["end"] if sents else 0.0
        print(f"saved audio/{name}.mp3  [{speaker}]  {len(sents)} sent  last_end={dur:.2f}s", flush=True)


if __name__ == "__main__":
    main()
