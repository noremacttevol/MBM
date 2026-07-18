#!/usr/bin/env python3
"""Narration audio for Video #105 — Face to Face, as a Friend (Exodus 33).

SPEAKER-LAW rebuild (2026-07-18). This is the proof video for the five-speaker
system, and it is the clearest case in the library of the defect Cameron named:
all three of its scripture lines were painted JESUS-RED, and not one of them is
Jesus speaking in the flesh. Exodus 33 is Jehovah — the premortal Christ — so
every one of them is GREEN.

WHAT CHANGED
  * g14 / g19 / g20  RED -> GREEN. A red-letter KJV prints none of Exodus in red;
    Christ had not yet come in the flesh. Green carries the truth that it is still
    Deity speaking.
  * sface was the narrator paraphrasing Exodus 33:11 in a white caption. It is
    verbatim KJV written by Moses, so it is SCRIPTURE (light blue), and the
    narrator now retells it plainly afterwards.
  * s18 is NEW. Moses's own words — "I beseech thee, shew me thy glory" (Ex 33:18)
    — were buried inside a narrator paraphrase ("Show me your glory"). Lifted out
    as SCRIPTURE so the viewer hears the man actually ask.
  * Every Old English line is now followed by the narrator saying it again in
    plain modern English (the retelling rule). n5, n5b, n6b and n6c are those.

WHY-LAW (unchanged): the wonder here is not thunder and law — it is FRIENDSHIP.
God spoke with a man the way you speak with a trusted friend, and when that was
not enough for Moses's hungry heart, he did not rebuke him for wanting more. He
hid him in a rock and let his goodness pass by. Milk framing: God WANTS to be
known. Never a threat.

PRONUNCIATION: "shew" -> "show" comes from the global map in mbm_pronounce.
No homographs present (audited at render time).
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import GOD, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR,
     "Moses pitched a tent a little way outside the camp and called it the Tent of "
     "Meeting. It was the place he went to be with God — set apart, quiet, away from "
     "everything else."),
    ("n2", NARRATOR,
     "Whenever Moses walked out to that tent, something happened that had never "
     "happened for anyone."),
    ("n3", NARRATOR,
     "All the people would rise and stand, each at the door of their own tent, and "
     "watch him go, and worship — because they knew where he was going, and who was "
     "waiting for him there."),
    ("n4", NARRATOR,
     "As Moses reached the tent, a great pillar of cloud would come down and stand at "
     "the door — the presence of God himself, come down to meet one man."),

    # Exodus 33:11 — Moses wrote it; verbatim KJV, so it is scripture, not narration.
    ("sface", SCRIPTURE,
     "And the LORD spake unto Moses face to face, as a man speaketh unto his friend."),
    ("n5", NARRATOR,
     "Face to face. As a man speaks with his friend. Not a master barking at a "
     "servant. Not a king across a vast throne room — easy, honest, close. God "
     "wanted Moses. Not just his obedience. His friendship."),

    # Exodus 33:14 — Jehovah. Sacred silence 1.
    ("g14", GOD,
     "My presence shall go with thee, and I will give thee rest."),
    ("n5b", NARRATOR,
     "I will go with you myself, and I will give you rest. Not send someone ahead. "
     "Not watch from somewhere far off. Go with you."),

    ("n6", NARRATOR,
     "And that friendship made Moses bold. He asked for the one thing no one had "
     "ever dared to ask."),
    # Exodus 33:18 — Moses's own words, previously buried in the paraphrase above.
    ("s18", SCRIPTURE,
     "I beseech thee, shew me thy glory."),

    # Exodus 33:19 — Jehovah.
    ("g19", GOD,
     "I will make all my goodness pass before thee, and I will proclaim the name of "
     "the LORD before thee."),
    ("n6b", NARRATOR,
     "Show me your glory, Moses asked. And God answered — I will make all my goodness "
     "pass in front of you. Not his power. Not his greatness. His goodness. Of "
     "everything he could have shown a friend, that is what he chose."),

    # Exodus 33:20 — Jehovah. Sacred silence 2.
    ("g20", GOD,
     "Thou canst not see my face: for there shall no man see me, and live."),
    ("n6c", NARRATOR,
     "You cannot see my face and live. That was not a refusal. It was care — the way "
     "you would not hand a child something far too heavy to hold."),

    ("n7", NARRATOR,
     "So God did the gentlest thing. He tucked Moses into a cleft in the rock, and "
     "covered him with his own hand, and let all his goodness pass by — near enough "
     "to feel, too much to look on. He protected his friend even from the weight of "
     "his own glory."),
    ("n8", NARRATOR,
     "And when Moses came back down, his face was shining. He did not even know it."),
    ("n9", NARRATOR,
     "That is what happens to someone who spends time close to God — you start, "
     "quietly, to glow with a little of him. It began with a friendship, at a tent, "
     "outside the camp."),

    ("card", NARRATOR,
     "God spoke with a man as with a friend, and hid him in a rock to keep him safe "
     "from too much glory. He still wants to be known like that — not feared from far "
     "off, but known up close. Would you let him be that kind of friend to you?"),
]

# Homographs this build decides for itself. None present — kept for the audit trail.
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
