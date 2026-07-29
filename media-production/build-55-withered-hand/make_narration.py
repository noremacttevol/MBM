#!/usr/bin/env python3
"""Narration for build-55-withered-hand — Mark 3.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

STAYED RED, both of them, and a third added.
  jv4  Mark 3:4  "Is it lawful to do good on the sabbath days, or to do evil? to
       save life, or to kill?"  -- already correctly stopping short of "But they
       held their peace," which is Mark writing. Left exactly as it was.
  jv5  Mark 3:5  "Stretch forth thine hand."  -- kept its id.
  j3   Mark 3:3  "Stand forth."  -- MISSING ENTIRELY. n3 paraphrased it in white
       ("stand up, and come out here into the midst"). Lifted verbatim as its own
       red beat on the SAME still (S3). n3 keeps its id, trimmed to the frame, and
       n3b carries the retelling.

NARRATION FRAMING SPLIT OFF THE SECOND RED LINE. Mark 3:5 reads "And when he had
looked round about on them with anger, being grieved for the hardness of their
hearts, he saith unto the man, Stretch forth thine hand." The anger and the grief
are Mark writing, not Jesus speaking -- and they were sitting in white paraphrase at
the tail of n4. Lifted as s5a [scripture, light blue] on S6, immediately before jv5
on the same still. n4 is trimmed to end at their silence; n4b retells both halves.

NO GREEN: nothing in Mark 3:1-6 is the Father or a voice from heaven.

WOMEN: Mark 3:1-6 records no woman speaking. Nothing added; nothing invented.

WHY-LAW: the room was full of people watching a man's suffering as an opportunity.
Jesus put him in the middle of the floor where nobody could pretend not to see him.
Milk: mercy was never a breaking of the sabbath. It was the whole reason for it.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "On another sabbath Jesus went into the synagogue to teach, and there in the crowd was a man whose hand was withered, shrunken and useless, a hand that could not work or grip or hold. He had carried it, and the shame of it, for years."),
    ("n2", NARRATOR, "But others in the room were watching — not the man, but Jesus. Some of the religious leaders felt sure he would try to heal on the sabbath, and they waited, hoping to catch him breaking the law, so they could accuse him."),
    ("n3", NARRATOR, "Jesus knew exactly what was in their hearts. He did not hide the moment away in a corner. He said to the man with the withered hand:"),
    # Mark 3:3
    ("j3", JESUS, "Stand forth."),
    ("n3b", NARRATOR, "Stand up. Come out here, into the middle, where everyone can see you. The man everybody in that room had learned to look past was moved to the center of the floor."),
    # Mark 3:4
    ("jv4", JESUS, "Is it lawful to do good on the sabbath days, or to do evil? to save life, or to kill?"),
    ("n4", NARRATOR, "It was a simple question, and it left them no answer. They had no real love for the law, or for the man; they only wanted a reason to condemn him. So they said nothing at all."),
    # Mark 3:5
    ("s5a", SCRIPTURE, "And when he had looked round about on them with anger, being grieved for the hardness of their hearts, he saith unto the man,"),
    # Mark 3:5
    ("jv5", JESUS, "Stretch forth thine hand."),
    ("n4b", NARRATOR, "He looked around at every one of them, angry, and grieved to the heart at how hard they had let themselves become. And then he turned away from them, to the man, and said:"),
    ("n5", NARRATOR, "And the man stretched out the hand he could not use — and as he reached, it was made whole, restored, strong and alive again, exactly like his other hand. The thing that had been dead came back to life at a single word."),
    ("n6", NARRATOR, "But the leaders were not amazed; they were furious. They walked out and began, that very day, to plot together how they might destroy him. He had done nothing but good, and it only hardened them."),
    ("n7", NARRATOR, "Faced with a rule on one side and a suffering man on the other, Jesus never wavered. He will always move toward the person. Mercy, to him, was never a breaking of the sabbath; it was the whole reason for it."),
    ("card", NARRATOR, "There will always be people upset that he loves you without conditions. Let them be. He looks past every rule that was ever used to shut you out, and he calls you to stand up, out in the open, and be made whole. Will you stretch out the very thing you thought was beyond help?"),
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
