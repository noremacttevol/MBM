#!/usr/bin/env python3
"""Narration for build-169-fulfil-righteousness — Matthew 3.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

THIS IS THE WORKED EXAMPLE IN SPEAKER-LAW section 4, and it is done exactly as
the law prints it.

SPLIT 1 — Matthew 3:15, three speakers in one breath, previously all red:
  kv15   (scripture, blue)  'And Jesus answering said unto him,'
  kv15b  (jesus, RED)       'Suffer it to be so now: for thus it becometh us to
                             fulfil all righteousness.'
  kv15c  (scripture, blue)  'Then he suffered him.'
A red-letter King James Bible prints only the middle clause red — the other two
are Matthew narrating. kv15 keeps the original id rather than being renamed
kv15a, because renaming would orphan anything referencing it by name; kv15b and
kv15c are new. All three stay on S3.

SPLIT 2 — Matthew 3:17, and this one is the doctrinal catch. It was painted red
end to end, which made the FATHER'S voice from heaven read as the Son's own:
  kv17  (scripture, blue)  'And lo a voice from heaven, saying,'
  gv17  (god, GREEN)       'This is my beloved Son, in whom I am well pleased.'
Green is the Father speaking. Red here would have had Christ announcing himself
as his own beloved Son, which is exactly the class of error this pass exists to
catch. Both stay on S6.

LIFTED FROM PARAPHRASE:
  s14  Matthew 3:14  'I have need to be baptized of thee, and comest thou to me?'
       SCRIPTURE, blue. John the Baptist. n2 was reporting his protest for him;
       he makes it himself now. The KJV frame 'But John forbad him, saying,' is
       left off so s14 is his speech only.

s14 -> kv15 -> kv15b is a DELIBERATE question-and-answer pair with the narrative
frame in the middle: John objects, Matthew reports, the Lord answers. That is the
exception the retelling rule allows, and n3 retells the whole exchange right
after. The validator warns; the warning is expected.

WHY-LAW: milk. Baptism is shown as the way in that even the Sinless One walked,
and the Godhead is shown standing plain in one frame — three distinct persons,
each doing his own part — without a word of argument about it. The colour does
the teaching: red in the river, green from heaven.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import GOD, JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "Something startling happens at the very start of it all. Jesus, who had no sin to wash away, walks down to the river Jordan and asks John to baptize him — the sinless One, lining up for the sinner's ordinance."),
    ("n2", NARRATOR, "John was stunned, and tried to stop him. He felt the whole thing backwards: surely he was the one who needed to be baptized by Jesus, not Jesus by him. Who was he to baptize the Lord?"),
    # Matthew 3:14
    ("s14", SCRIPTURE, "I have need to be baptized of thee, and comest thou to me?"),
    # Matthew 3:15
    ("kv15", SCRIPTURE, "And Jesus answering said unto him,"),
    # Matthew 3:15
    ("kv15b", JESUS, "Suffer it to be so now: for thus it becometh us to fulfil all righteousness."),
    # Matthew 3:15
    ("kv15c", SCRIPTURE, "Then he suffered him."),
    ("n3", NARRATOR, "So even the perfect One went down into the water. Not because he needed cleansing, but to fulfil all righteousness — to walk the path himself, and leave us an example that this gate is the way in, for everyone."),
    ("n4", NARRATOR, "And as he came up out of the water, heaven itself answered. The skies opened, and the Spirit of God came down gently, like a dove, and rested upon him in the warm light."),
    # Matthew 3:17
    ("kv17", SCRIPTURE, "And lo a voice from heaven, saying,"),
    # Matthew 3:17
    ("gv17", GOD, "This is my beloved Son, in whom I am well pleased."),
    ("n5", NARRATOR, "Look closely at that one moment, because it opens a window into who God is. Three were there at once, and each was distinct: the Son standing in the river, the Spirit resting as the dove, and the Father speaking from the opened heaven."),
    ("n6", NARRATOR, "Here is the quiet study gem. This was not one person changing costumes. It was three distinct persons, together, each doing his own part — the Godhead, standing plain to see. And notice: even He was baptized."),
    ("n7", NARRATOR, "And that settles it for the rest of us. If the one man who never needed it still went down into the water to fulfil all righteousness, then the way is surely open, and good, for you. When you come to that same water, will you go down into it?"),
    ("card", NARRATOR, "Even the Sinless One was baptized, to fulfil all righteousness — and there the Godhead stood revealed: the Son, the Spirit, and the Father, three and distinct. When you come to that same water, will you go down into it?"),
]

# Homographs this build decides for itself (never auto-replaced globally).
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
