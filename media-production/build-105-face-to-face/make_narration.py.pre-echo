#!/usr/bin/env python3
"""Narration for build-105-face-to-face — Exodus 33.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

THE MISSED 200th. Every other row got a speaker plan on 2026-07-18; this one
never did, so run_batch never saw it and the video Cameron has been watching
still carries the pre-SPEAKER-LAW narration. The speaker assignments below were
already applied by hand to make_narration.py -- this file records them so the
build is reproducible and can never be skipped again.

GREEN, not red: Exodus is Old Testament, so every line the Lord speaks here is
premortal Jehovah -- GOD, green. A red-letter Bible prints none of Exodus 33 in
red, and the doctrine section of SPEAKER-LAW.md is explicit that green is how
these videos carry premortal Christ.
  g14  Exodus 33:14  'My presence shall go with thee...'
  g19  Exodus 33:19  'I will make all my goodness pass before thee...'
  g20  Exodus 33:20  'Thou canst not see my face...'

BLUE: s18 is Moses asking, so it is a man quoted from the KJV -- SCRIPTURE.
sface is Exodus 33:11 quoted as narration of the text rather than someone
speaking, and it stays SCRIPTURE for the same reason.

NO WOMEN: Exodus 33 records no woman speaking.

WHY-LAW: God talks with a man the way a man talks with his friend, then hides
him in a rock to keep him safe from too much glory. Milk framing -- nearness first, majesty second.

IDS: the original build.py beats are nface/jv14/jv19/jv20 and the music beds
and start_of[] lookups key off them, so they keep their names even though
nface is now blue and the jv* beats are now green. A hand pass had renamed them
to sface/g14/g19/g20 and migrate refused the plan outright.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import GOD, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "Moses pitched a tent a little way outside the camp and called it the Tent of Meeting. It was the place he went to be with God — set apart, quiet, away from everything else."),
    ("n2", NARRATOR, "Whenever Moses walked out to that tent, something happened that had never happened for anyone."),
    ("n3", NARRATOR, "All the people would rise and stand, each at the door of their own tent, and watch him go, and worship — because they knew where he was going, and who was waiting for him there."),
    ("n4", NARRATOR, "As Moses reached the tent, a great pillar of cloud would come down and stand at the door — the presence of God himself, come down to meet one man."),
    # Exodus 33:11
    ("nface", SCRIPTURE, "And the LORD spake unto Moses face to face, as a man speaketh unto his friend."),
    ("n5", NARRATOR, "Face to face. As a man speaks with his friend. Not a master barking at a servant. Not a king across a vast throne room — easy, honest, close. God wanted Moses. Not just his obedience. His friendship."),
    # Exodus 33:14
    ("jv14", GOD, "My presence shall go with thee, and I will give thee rest."),
    ("n5b", NARRATOR, "I will go with you myself, and I will give you rest. Not send someone ahead. Not watch from somewhere far off. Go with you."),
    ("n6", NARRATOR, "And that friendship made Moses bold. He asked for the one thing no one had ever dared to ask."),
    # Exodus 33:18
    ("s18", SCRIPTURE, "I beseech thee, shew me thy glory."),
    # Exodus 33:19
    ("jv19", GOD, "I will make all my goodness pass before thee, and I will proclaim the name of the LORD before thee."),
    ("n6b", NARRATOR, "Show me your glory, Moses asked. And God answered — I will make all my goodness pass in front of you. Not his power. Not his greatness. His goodness. Of everything he could have shown a friend, that is what he chose."),
    # Exodus 33:20
    ("jv20", GOD, "Thou canst not see my face: for there shall no man see me, and live."),
    ("n6c", NARRATOR, "You cannot see my face and live. That was not a refusal. It was care — the way you would not hand a child something far too heavy to hold."),
    ("n7", NARRATOR, "So God did the gentlest thing. He tucked Moses into a cleft in the rock, and covered him with his own hand, and let all his goodness pass by — near enough to feel, too much to look on. He protected his friend even from the weight of his own glory."),
    ("n8", NARRATOR, "And when Moses came back down, his face was shining. He did not even know it."),
    ("n9", NARRATOR, "That is what happens to someone who spends time close to God — you start, quietly, to glow with a little of him. It began with a friendship, at a tent, outside the camp."),
    ("card", NARRATOR, "God spoke with a man as with a friend, and hid him in a rock to keep him safe from too much glory. He still wants to be known like that — not feared from far off, but known up close. Would you let him be that kind of friend to you?"),
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
