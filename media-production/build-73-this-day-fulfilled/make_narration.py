#!/usr/bin/env python3
"""Narration for build-73-this-day-fulfilled — Luke 4.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

STAYED RED, both, and this is the whole ruling for this build. j1 is Isaiah
61:1-2 - but Jesus is the one reading it out loud off the scroll in the
synagogue at Nazareth (Luke 4:18-19), so it is RED, not green. Green marks the
Father, the Holy Ghost, or premortal Jehovah SPEAKING. Here the speaker in the
room is Jesus in the flesh; Isaiah is what he is reading, not who is talking. A
red-letter KJV inks Luke 4:18-19 for exactly that reason. Same principle as the
temptations, where his 'It is written' answers stay red even though he is
quoting Deuteronomy. j2 (Luke 4:21) 'This day is this scripture fulfilled in
your ears' is red and untouched.

NOTE ON THE SPAN: j1 is one audio segment that runs across TWO stills, S3 and
S4, cutting at a caption boundary. That is untouched - the picture cut stays
exactly where it was. Same for n3 across S7 and S8.

ADDED AS SCRIPTURE, both of them Luke narrating, both light blue:
  s17  Luke 4:17  'And there was delivered unto him the book of the prophet
       Esaias. And when he had opened the book, he found the place where it was
       written,'  - this is the framing split. Everything before Jesus opens his
       mouth is Luke writing, never red. n1 said the same thing in modern
       English and now retells it, ON THE SAME STILL S2 - no new artwork.
  s20  Luke 4:20  'And he closed the book, and he gave it again to the minister,
       and sat down. And the eyes of all them that were in the synagogue were
       fastened on him.'  n2 keeps its id and text and now retells it. This is
       the held breath before the shortest, largest sentence in the video.
  n1b  new narrator beat on S4, the second half of j1's existing span, so the
       long Isaiah block gets retold in plain English before the scene moves on.
       The retelling rule is mandatory and this was the one place in the build
       where a big stretch of Old English landed unexplained.

CONSIDERED AND LEFT OUT: Luke 4:22, 'Is not this Joseph's son?' It is the
town's doubt, and it is exact if a later pass wants it - but n3 is a single
segment spanning S7 and S8, so there is nowhere to put the verse without either
breaking that span or landing the doubt after the closing thought. Left out on
judgment, not uncertainty. Milk framing wins: the video ends on 'today', not on
the neighbours' shrug.

WOMEN: Luke 4:16-21 records no woman speaking. Nothing added, nothing invented.

PRONUNCIATION: 'Esaias' is the KJV spelling of Isaiah and is a proper noun off
the SPEAKER-LAW list. Respelled in `spoken`; the caption keeps the true KJV
spelling.

WHY-LAW: they had read that scroll for centuries as a promise about someday. He
handed it back and told them someday had walked in and sat down.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "He came back to Nazareth — the town that raised him — and on the Sabbath he walked into the synagogue like he always had."),
    # Luke 4:17
    ("s17", SCRIPTURE, "And there was delivered unto him the book of the prophet Esaias. And when he had opened the book, he found the place where it was written,"),
    ("n1", NARRATOR, "They handed him the scroll of Isaiah. He found the place, and read it out loud."),
    # Luke 4:18-19
    ("j1", JESUS, "The Spirit of the Lord is upon me, because he hath anointed me to preach the gospel to the poor; he hath sent me to heal the brokenhearted, to preach deliverance to the captives, and recovering of sight to the blind, to set at liberty them that are bruised, to preach the acceptable year of the Lord."),
    ("n1b", NARRATOR, "The Spirit of the Lord is on me, he read, because he anointed me — to bring good news to the poor, to bind up the broken-hearted, to tell prisoners they can go free, to give the blind their sight back, to set bruised people loose. Every line of it was a promise about somebody who had not come yet."),
    # Luke 4:20
    ("s20", SCRIPTURE, "And he closed the book, and he gave it again to the minister, and sat down. And the eyes of all them that were in the synagogue were fastened on him."),
    ("n2", NARRATOR, "Then he rolled the scroll up, handed it back, and sat down. Every eye in the room was fixed on him — this was the boy who grew up on their street. And the room held its breath."),
    # Luke 4:21
    ("j2", JESUS, "This day is this scripture fulfilled in your ears."),
    ("n3", NARRATOR, "The promise Israel had waited on for centuries — the healing, the freedom, the good news for the poor — he said it was standing right in front of them. Not someday. Today."),
    # FULLNESS REBUILD (Cameron complaint, 2026-08-07): the old ending only
    # REPORTED the event ("he still reads it the same"). Cameron: teach how He
    # MEANT it, that He has risen and continues the same plan today, framed the
    # way the prophets then and the restored Church now would teach it — WITHOUT
    # naming the Church. Milk; the Two-Voice law is untouched (no new words are
    # put in Jesus's mouth — j1/j2 remain his only lines; the fullness is carried
    # by the narrator opening up what his own words meant).
    ("n4", NARRATOR, "He was not reading someone else's words — that was his own mission, spoken in his own mouth, the Anointed One saying out loud what he had come to do. And he did it: he healed the broken, opened blind eyes, and carried freedom to the very people the world had written off."),
    ("n5", NARRATOR, "They killed him for it — but on the third day he rose, and the work he began in that little room did not end at an empty tomb. He is alive, the same Spirit is still upon him, and the good news he read that morning is going out into the world again in our own day — the year of the Lord's favor has never once closed."),
    ("card", NARRATOR, "He read it as today because, for him, it still is. The risen Lord is keeping every line of that promise even now — and one of them was written with you in mind. What would it mean if he were reading it, today, over your life?"),
]

# Homographs this build decides for itself (never auto-replaced globally).
SPOKEN = {
    "Esaias": "eh-ZAY-us",
}


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
