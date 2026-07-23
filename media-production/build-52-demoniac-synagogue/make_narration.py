#!/usr/bin/env python3
"""Narration for build-52-demoniac-synagogue — Mark 1.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

THE UNCLEAN SPIRIT WAS BURIED IN THE NARRATOR. All of Mark 1:24 was sitting
inside n4, spoken in white in modern English -- the storyteller doing the voice.
Lifted out verbatim as SCRIPTURE, light blue:
  s24  Mark 1:24  'Let us alone; what have we to do with thee, thou Jesus of
       Nazareth? art thou come to destroy us? I know thee who thou art, the Holy
       One of God.'
Light blue, not red and not green: it is a being in the story, one of the people
Mark records speaking, and it is emphatically not Deity. n4 keeps its id, trimmed
to the frame only -- 'The voice that broke from him was not his own.' -- and a new
n4b carries the retelling. Both stay on S4, the still already named
s4-the-unclean-cry, which is exactly what it is now showing.

ADDED IN BLUE -- THE CONGREGATION. Mark 1:27, the crowd's reaction, was
paraphrased inside n7. Lifted out verbatim as SCRIPTURE:
  s27  Mark 1:27  'What thing is this? what new doctrine is this? for with
       authority commandeth he even the unclean spirits, and they do obey him.'
  n7 trimmed to its frame, new n7b retells it.

STAYED RED. jv25 (Mark 1:25, 'Hold thy peace, and come out of him') is Jesus in
the flesh and a red-letter KJV inks it. Mark's framing -- 'And Jesus rebuked him,
saying' -- was already stripped, so no split was needed. It sits between s24 and
n5 as the answer to what the spirit just said, which is how Mark orders it.

NO GREEN. Nothing in Mark 1:21-28 is the Father speaking.

WOMEN: Mark 1:21-28 records no woman speaking. Nothing added; nothing invented.

LEFT AS PARAPHRASE ON PURPOSE: n2 describes Mark 1:22 ('he taught them as one
that had authority, and not as the scribes') without quoting it. I left it in the
storyteller's voice because the same sentence, in Matthew's wording, is now a blue
beat in build-47, and because s27 later in this build already says the authority
line verbatim. Quoting it twice inside one video would flatten the ending.

RETELLING RULE: s24 by n4b, jv25 by n5, s27 by n7b. No two Old English blocks run
back to back.

WHY-LAW: no long battle, no struggle of equals -- the darkness knew exactly who he
was and had to go at a word. Milk: nothing holding you has to stay when he speaks.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "On the sabbath day, Jesus went into the synagogue at Capernaum and stood up to teach. The people had gathered as they always did, to hear the scriptures taught and explained by the teachers they knew."),
    ("n2", NARRATOR, "But this was different. He taught them as one who had authority of his own, not leaning on teacher after teacher the way the scribes did. His words carried a quiet weight, and the whole room felt it, and was astonished."),
    ("n3", NARRATOR, "There in the congregation was a man held by an unclean spirit. Something dark had bound him for a long time, and the nearness of Jesus stirred it. Unable to stay silent any longer, he suddenly cried out."),
    ("n4", NARRATOR, "And the voice that broke out of him was not his own."),
    # Mark 1:24
    ("s24", SCRIPTURE, "Let us alone; what have we to do with thee, thou Jesus of Nazareth? art thou come to destroy us? I know thee who thou art, the Holy One of God."),
    ("n4b", NARRATOR, "Leave us alone. What do you want with us, Jesus of Nazareth? Have you come to destroy us? And then, almost trembling: I know who you are. The Holy One of God. Sit with that for a second. In a room full of religious people, the first one to say out loud exactly who he was, was the darkness."),
    # Mark 1:25
    ("jv25", JESUS, "Hold thy peace, and come out of him."),
    ("n5", NARRATOR, "Be quiet, and come out of him. Just a few short words. There was no long battle, no struggle of equals. At his word the spirit shook the man one last time, cried out with a loud voice, and came out of him. The thing that had held him for so long simply had to go."),
    ("n6", NARRATOR, "And the man was free. The torment had drained from his face, and he stood there quiet and whole, himself again, like someone waking gently from a long and terrible dream."),
    ("n7", NARRATOR, "The people were amazed, and they turned to one another asking:"),
    # Mark 1:27
    ("s27", SCRIPTURE, "What thing is this? what new doctrine is this? for with authority commandeth he even the unclean spirits, and they do obey him."),
    ("n7b", NARRATOR, "What is this? A new teaching, and it comes with authority behind it. He gives an order to the unclean spirits, and they obey him. They had come to synagogue that morning expecting an ordinary sabbath."),
    ("n8", NARRATOR, "And right away the news of him went out everywhere, through all the country round about Galilee. Wherever the story was carried, people heard that one had come whose word even the darkness could not resist."),
    ("card", NARRATOR, "The same voice that spoke into that man's torment still speaks today. There is no darkness in you so deep that his word cannot reach it, and nothing holding you that has to stay when he says come out. What is he asking you to let him set free?"),
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
