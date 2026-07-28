#!/usr/bin/env python3
"""Narration for build-128-heart-far-from-me — Mark 7:6-13 (SPEAKER-LAW).

Row 128 corrected 2026-07-23: the folder build-128-famine-of-hearing held the old
Amos "famine of hearing" narration, which duplicated #156. This is the real Mark 7
story its QUEUE row was swapped to. See DRAFTS/row-128-heart-far-from-me.md.

Jesus's quoted words are JESUS (exact KJV red-letter). Narrator is modern and never
restates the adjacent KJV line (echo_scan clean).
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR

SEGMENTS = [
    ("n1", NARRATOR, "Some of the religious leaders came to Jesus with a complaint. They had seen his disciples eating with unwashed hands — breaking not God's law, but a tradition the elders had added on top of it. To them, that was a scandal."),
    ("n2", NARRATOR, "Jesus was not impressed by the show. He answered them with words the prophet Isaiah had written long before."),
    # Mark 7:6-7
    ("j1", JESUS, "This people honoureth me with their lips, but their heart is far from me. Howbeit in vain do they worship me, teaching for doctrines the commandments of men."),
    ("n3", NARRATOR, "You can say every right word and keep every custom and still be a thousand miles away on the inside. He was never counting the handwashing. He was looking for what stood behind it."),
    # Mark 7:8
    ("j2", JESUS, "For laying aside the commandment of God, ye hold the tradition of men."),
    ("n4", NARRATOR, "Then he gave them an example that exposed the whole game. God had said, Honour thy father and thy mother. But their custom let a man label his money a gift promised to the temple — and use that label as an excuse to give nothing to his own aging parents."),
    # Mark 7:13
    ("j3", JESUS, "Making the word of God of none effect through your tradition, which ye have delivered."),
    ("n5", NARRATOR, "They had used a rule about God to cancel a command from God — turning devotion into a loophole. That was his warning: never let the outside of religion grow so loud that it drowns out the heart of it. He would always rather have an honest heart than a flawless performance. Come to him with the real one."),
]

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
