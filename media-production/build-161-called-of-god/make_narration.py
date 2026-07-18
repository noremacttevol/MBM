#!/usr/bin/env python3
"""Generate narration audio for Story Video #161 — Called of God, as was Aaron
(Hebrews 5:1-6). MEMBER shelf verse-video. → Gospel Library topic: Priesthood.

Narrator: en-US-AndrewNeural — plain American, modern paraphrase, never a
Multilingual model, never echoes the KJV wording.
Scripture voice: en-US-ChristopherNeural — speaks the KJV text EXACTLY, the same
reverent voice the project uses for scripture. (Hebrews is apostolic text, not
red-letter words of Jesus; here the scripture voice carries the verse itself.)

KJV lines (exact):
  kv1 = Heb 5:1   every high priest is ordained for men in things pertaining to God
  kv4 = Heb 5:4   no man taketh this honour unto himself (VERSE CARD — SACRED SILENCE 1)
  kv5 = Heb 5:5   so also Christ glorified not himself (SACRED SILENCE 2)

The two sacred silences land on kv4 (the named verse) and kv5 (even Christ was
called, not self-made).

WHY-LAW: the point is reassurance, not gatekeeping — the right to act for God is
GIVEN, through a call and the laying-on of hands, the same gentle way it came to
Aaron. STUDY GEMS: a high priest was himself a weak man, able to feel for weak
people (n2); Aaron did not choose himself — God named him and Moses ordained and
anointed him (n4-n6); even Christ did not make himself high priest — the Father
called him (n7).

TRANSLATION LAW: the narrator never re-quotes a KJV line. n3 says "you cannot hand
this to yourself," never "no man taketh this honour"; n7 says "the Father gave him
the office," never "glorified not himself."

MILK FRAMING: an invitation. The closing card ends on an open question and a
one-line pointer to the Gospel Library topic (Priesthood). No shame, no gatekeeping.

NUMBER-STRESS LAW: no sentence opens with a bare number.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"
SCRIPTURE = "en-US-ChristopherNeural"

SEGMENTS = [
    # (filename, voice, rate, pitch, text) — text is BOTH spoken and captioned.
    # --- s1: the office ---
    ("n1", NARRATOR, "-20%", "-4Hz",
     "In ancient Israel, one man stood between the people and God. The high priest "
     "carried their gifts and their sins to the altar, and carried God's holiness "
     "back to them. It was the most sacred office a person could hold."),
    ("kv1", SCRIPTURE, "-24%", "-6Hz",
     "For every high priest taken from among men is ordained for men in things "
     "pertaining to God, that he may offer both gifts and sacrifices for sins."),
    # --- s2: compassion ---
    ("n2", NARRATOR, "-22%", "-4Hz",
     "And here is a tender thing. The high priest was not a distant, perfect being. "
     "He was a weak man himself, who knew his own failings, and so he could be gentle "
     "with everyone else's. He was one of the people, not above them."),
    # --- s3: no man takes it ---
    ("n3", NARRATOR, "-22%", "-4Hz",
     "But an office that holy could not simply be claimed. However sincere a man was, "
     "however gifted, he could not reach out and take it for himself. You cannot hand "
     "this to yourself. It has to be given."),
    # --- s4: kv4 — VERSE CARD, SACRED SILENCE 1 ---
    ("kv4", SCRIPTURE, "-26%", "-6Hz",
     "And no man taketh this honour unto himself, but he that is called of God, as "
     "was Aaron."),
    ("n4", NARRATOR, "-22%", "-4Hz",
     "Think of how Aaron became high priest. He did not campaign for it or seize it. "
     "God named him, and Moses brought him before the people and set him apart. The "
     "honour came down to him; it was never something he grasped."),
    # --- s5: laying on of hands ---
    ("n5", NARRATOR, "-22%", "-4Hz",
     "And notice how it was done. Not with a ceremony he arranged for himself, but "
     "with another man's hands laid on his head, ordaining him. The authority passed "
     "by touch and blessing, from someone who already held it."),
    # --- s6: anointed ---
    ("n6", NARRATOR, "-22%", "-4Hz",
     "Then the holy oil was poured over him, running down, and Aaron was consecrated, "
     "set apart, given. Everything about that day says the same thing: this was "
     "received, not taken."),
    # --- s7: kv5 — SACRED SILENCE 2 (Christ) ---
    ("kv5", SCRIPTURE, "-26%", "-6Hz",
     "So also Christ glorified not himself to be made an high priest; but he that "
     "said unto him, Thou art my Son, to day have I begotten thee."),
    ("n7", NARRATOR, "-22%", "-4Hz",
     "And this is the astonishing part. Even the Lord himself did not make himself a "
     "high priest. The Father gave him the office and called him to it. If the Son of "
     "God received his authority instead of seizing it, then no one else gets to "
     "appoint themselves either."),
    # --- s8: the pattern still / invitation ---
    ("n8", NARRATOR, "-24%", "-4Hz",
     "And that is the quiet good news in this verse. The right to speak and act for "
     "God has always come the same way: a real call, and hands laid on a bowed head. "
     "It is not earned by being impressive. It is given. So the only question left is "
     "a hopeful one. Where might God be calling you?"),
    # --- closing card, read gently (Readable-Card Law) ---
    ("card", NARRATOR, "-26%", "-4Hz",
     "No one hands themselves the things of God. Aaron was called, and even Christ "
     "was called. That same authority is still given today, by a call and the "
     "laying-on of hands. Where is God calling you?"),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        await save_narration(text, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
