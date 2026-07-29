#!/usr/bin/env python3
"""Narration for build-132-forbid-him-not — Mark 9.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

STAYED RED: j1 is Mark 9:39-40, Jesus in the flesh, red-letter, and verbatim as it
already stood. The KJV frame 'But Jesus said,' was already left off the segment,
so there was no welded framing to split.

THE FIX - John's complaint is the hinge of the video and John never said it.
  s38  Mark 9:38  'Master, we saw one casting out devils in thy name, and he
       followeth not us: and we forbad him, because he followeth not us.'
       SCRIPTURE, light blue. John is an apostle, not Deity. n0 keeps its
       original text word for word and now works as the retelling right after it.
       Hearing him say 'because he followeth not us' TWICE in one breath - the
       KJV really does repeat it - is the whole point of the video, and a
       paraphrase flattened it.

LIFTED: jv41 Mark 9:41 'For whosoever shall give you a cup of water to drink in
my name, because ye belong to Christ, verily I say unto you, he shall not lose
his reward.' JESUS, RED. n3a was paraphrasing it; n3a keeps its text and is now
the retelling. ST8 is literally named 'a-cup-of-water' and the cup-of-water verse
was never spoken in the video.

REWRITTEN: n2 gave away j1's words before j1 arrived ('Don't stop him. Anyone
doing good in My name isn't against you' is just verse 39 in modern English,
delivered early). It is now a short setup, and the retelling work moved to n2b,
AFTER the verse, where the law wants it.

ADDED: n2b, the retelling of 9:39-40. ST10 now carries n3b, so all eight bound
stills are in the running order.

WOMEN: Mark 9:38-41 records no woman speaking. Nothing added, nothing invented.

WHY-LAW: John drew the circle at the edge of his own group and expected to be
thanked for it. Milk framing - the name is doing the work, not the membership,
and there is room for far more people than the inner circle assumed.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    # Mark 9:38
    ("s38", SCRIPTURE, "Master, we saw one casting out devils in thy name, and he followeth not us: and we forbad him, because he followeth not us."),
    ("n0", NARRATOR, "John came to Jesus with a complaint. They'd seen someone driving out demons using Jesus's name — and the man wasn't one of their group. So they told him to stop."),
    ("n1", NARRATOR, "John thought he was protecting the cause. The man wasn't with them, so he shouldn't be using the name."),
    ("n2", NARRATOR, "Jesus didn't take John's side. He went after the instinct underneath the complaint."),
    # Mark 9:39-40
    ("j1", JESUS, "Forbid him not: for there is no man which shall do a miracle in my name, that can lightly speak evil of me. For he that is not against us is on our part."),
    ("n2b", NARRATOR, "Don't stop him, He said. Nobody works a miracle in My name and then turns around and speaks against Me. Whoever isn't against us is on our side."),
    # Mark 9:41
    ("jv41", JESUS, "For whosoever shall give you a cup of water to drink in my name, because ye belong to Christ, verily I say unto you, he shall not lose his reward."),
    ("n3a", NARRATOR, "Whoever gives a cup of water in His name won't lose his reward."),
    ("n3b", NARRATOR, "The work isn't about belonging to a team — it's about Him."),
    ("n4", NARRATOR, "John learned a lesson that day: the kingdom is bigger than the inner circle."),
    ("card", NARRATOR, "Don't draw the circle too small. Whoever works in His name is on your side."),
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
