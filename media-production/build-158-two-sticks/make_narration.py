#!/usr/bin/env python3
"""Generate narration audio for Story Video #158 — "The stick of Judah and the stick
of Joseph" (Ezekiel 37:15-19). MEMBER shelf verse-video.
→ Gospel Library topic: Book of Mormon.

Narrator: en-US-AndrewNeural — plain American, modern paraphrase, never a
Multilingual model, never echoes the KJV wording.
Scripture voice: en-US-ChristopherNeural — speaks the KJV text EXACTLY.
(Ezekiel is Old-Testament prophecy; the scripture voice carries the verse. Christ is
NOT depicted; God is shown only as light. Keep entirely in ancient imagery — two wooden
writing-rods joined; the Gospel Library pointer on the card carries the connection.)

KJV lines (exact):
  kv16 = Ezek 37:16  take one stick for Judah... another for Joseph (SACRED SILENCE 1)
  kv19 = Ezek 37:19  make them one stick... one in mine hand (NAMED VERSE — SACRED SILENCE 2)

WHY-LAW: hope of gathering — God binds what was scattered, records and people, into one.
STUDY GEMS: an object lesson anyone could grasp (n1); two records from two divided
branches of one family (n2-n3); joined, each completing the other, not erasing (n5); the
joining is done in GOD'S hand (n7).

TRANSLATION LAW: the narrator never re-quotes a KJV line. n4 says "bring the two sticks
together and join them," delivered as paraphrase; the exact KJV lands only in kv16/kv19.

MILK FRAMING: an invitation. The closing card ends on an open question and a one-line
pointer to the Gospel Library topic (Book of Mormon). No shame, no mocking any group.
CHRIST IS NEVER DEPICTED; God is shown only as warm light.

NUMBER-STRESS LAW: no sentence opens with a bare number.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"
SCRIPTURE = "en-US-ChristopherNeural"

SEGMENTS = [
    ("n1", NARRATOR, "-20%", "-4Hz",
     "Among the exiles by the river, the prophet Ezekiel received an unusual assignment "
     "from God — not a sermon to preach, but an object lesson to act out, so plain that "
     "anyone watching could understand it."),
    ("n2", NARRATOR, "-22%", "-4Hz",
     "Take a stick, God told him — a flat wooden writing-rod — and mark it with a name: "
     "for Judah, and for the people gathered with him. One record, belonging to one part "
     "of God's scattered family."),
    ("n3", NARRATOR, "-22%", "-4Hz",
     "Then take a second stick, God said, and mark it with another name: for Joseph. A "
     "separate record, belonging to another branch of the same family, long divided from "
     "the first."),
    # kv16 — SACRED SILENCE 1
    ("kv16", SCRIPTURE, "-26%", "-6Hz",
     "Moreover, thou son of man, take thee one stick, and write upon it, For Judah, and "
     "for the children of Israel his companions: then take another stick, and write upon "
     "it, For Joseph, the stick of Ephraim, and for all the house of Israel his "
     "companions:"),
    ("n4", NARRATOR, "-22%", "-4Hz",
     "Now here is the part that made people stop and stare. Bring the two sticks "
     "together, God said, and join them — until the two become a single stick, one solid "
     "piece, held together in your hand."),
    ("n5", NARRATOR, "-22%", "-4Hz",
     "Two separate records, from two separated peoples, brought together and made one. "
     "Not one erasing the other, but the two joined, each completing the other, speaking "
     "now with a single united voice."),
    ("n6", NARRATOR, "-22%", "-4Hz",
     "And of course the people came asking, what do you mean by this? Why two sticks "
     "made one? What are you trying to show us? God had built the question right into the "
     "lesson."),
    # kv19 — NAMED VERSE, SACRED SILENCE 2
    ("kv19", SCRIPTURE, "-26%", "-6Hz",
     "Say unto them, Thus saith the Lord GOD; Behold, I will take the stick of Joseph, "
     "which is in the hand of Ephraim, and the tribes of Israel his fellows, and will put "
     "them with him, even the stick of Judah, and make them one stick, and they shall be "
     "one in mine hand."),
    ("n7", NARRATOR, "-22%", "-4Hz",
     "Notice whose hand does the joining. God says, they shall be one in mine hand. He is "
     "the one who gathers the scattered records, and the scattered people, and binds them "
     "together into one."),
    ("n8", NARRATOR, "-24%", "-4Hz",
     "So this strange little sign is really a promise of gathering. God does not leave his "
     "family, or his words to them, broken into separate pieces forever. He brings them "
     "back together. So the only question is a hopeful one. When the two are made one in "
     "his hand, will you take them both up and read?"),
    ("card", NARRATOR, "-26%", "-4Hz",
     "God had Ezekiel join two records into one stick — two witnesses made one in his "
     "hand. He gathers what was scattered, and binds his words together. When the two are "
     "one, will you take them both up and read?"),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        await save_narration(text, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
