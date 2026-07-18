#!/usr/bin/env python3
"""Generate narration audio for Video #58 — Feeding the Five Thousand (John 6:1-14).

Narrator: en-US-AndrewNeural — plain American, never a Multilingual model.
Jesus voice: en-US-ChristopherNeural — American, never British.

Jesus speaks ONLY exact KJV. One red-letter line is used here, plus one non-verbal sacred
beat:
  (nbless) John 6:11 — the BLESSING of the loaves (narrator-told) = SACRED SILENCE 1.
  jv12 = John 6:12  "Gather up the fragments that remain, that nothing be lost."
                     = SACRED SILENCE 2 (cream-italic KJV).

TRANSLATION LAW: the narrator paraphrases everything else (including Jesus' testing question
in v5) and never re-quotes the red-letter line.

HOMOGRAPH LAW: no TTS homographs in this text (avoided archaic "brake" by writing "broke";
no live/bow/wound/read/tear/wind/lead/sow). SPOKEN is empty.

CARE — GREEN: a joyful miracle of provision. Nothing fearful; a boy's small lunch becomes a
feast for thousands. The fish are shown as simple food, never gory. Ends on an open
invitation.

NUMBER-STRESS LAW: no sentence opens with a bare number.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"
JESUS = "en-US-ChristopherNeural"

SPOKEN = {}

SEGMENTS = [
    # (filename, voice, rate, pitch, text) — text is BOTH spoken and captioned.
    # --- s1: the crowd follows ---
    ("n1", NARRATOR, "-20%", "-4Hz",
     "A huge crowd had followed Jesus to a lonely green hillside beside the lake, hungry "
     "to hear him and to be healed. He taught them and cared for them all day, until the "
     "sun began to sink and they were a long way from any town or food."),
    # --- s2: far from bread ---
    ("n2", NARRATOR, "-22%", "-4Hz",
     "His disciples grew anxious. Send the people away, they said, so they can go and buy "
     "themselves something to eat. But Jesus turned it back on them: where, he asked, "
     "could they ever buy enough bread to feed a crowd like this? He already knew what he "
     "would do."),
    # --- s3: a boy's lunch ---
    ("n3", NARRATOR, "-22%", "-4Hz",
     "There was only one lunch in the whole crowd. A boy had five small barley loaves and "
     "two little fish, and Andrew brought him to Jesus, almost embarrassed. But what is "
     "that, he said, among so many?"),
    # --- s4: sit down on the grass ---
    ("n4", NARRATOR, "-22%", "-4Hz",
     "Jesus was not troubled by how little there was. He simply told the disciples to have "
     "everyone sit down, and they settled in groups on the green grass, five thousand men, "
     "besides women and children, waiting to see what he would do."),
    # --- s5: he blessed and broke. SACRED SILENCE 1. ---
    ("nbless", NARRATOR, "-24%", "-5Hz",
     "Then he took the five loaves and the two fish, and looking up to heaven, he gave "
     "thanks, and broke the bread."),
    # --- s6: all were filled ---
    ("n5", NARRATOR, "-22%", "-4Hz",
     "And the food did not run out. The disciples carried it through the crowd, and it "
     "kept coming, bread and fish, more and more, until every single person there had "
     "eaten as much as they wanted, and was full."),
    # --- s7: jv12 — gather the fragments. SACRED SILENCE 2. ---
    ("jv12", JESUS, "-26%", "-6Hz",
     "Gather up the fragments that remain, that nothing be lost."),
    # --- s8: twelve baskets ---
    ("n6", NARRATOR, "-22%", "-4Hz",
     "So they went through the crowd and gathered what was left, and filled twelve baskets "
     "with the broken pieces. They ended with far more than they had started with. The "
     "little lunch, placed in his hands, had become a feast."),
    # --- s9: that prophet ---
    ("n7", NARRATOR, "-24%", "-4Hz",
     "When the people saw the sign, they were amazed, and began to say, this is truly the "
     "Prophet who was to come into the world. He had taken almost nothing, given thanks, "
     "and fed them all."),
    # --- closing card, read gently (Readable-Card Law) ---
    ("card", NARRATOR, "-26%", "-4Hz",
     "He still takes the little you have, the not-enough, the barely-anything, the lunch "
     "you are embarrassed to offer, and gives thanks for it, and breaks it, and somehow it "
     "becomes enough, with baskets to spare. What small thing is he asking you to place in "
     "his hands?"),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        spoken = SPOKEN.get(name, text)
        await save_narration(spoken, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")


if __name__ == "__main__":
    asyncio.run(main())
