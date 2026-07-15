#!/usr/bin/env python3
"""Narration audio for Video #102 — Jacob's Ladder (Genesis 28:10-22).

Narrator: en-US-AndrewNeural. The Lord's voice: en-US-ChristopherNeural (exact KJV
only). Jacob's own words are given by the narrator in plain paraphrase (two-voice law).

The Lord's KJV lines (Christopher, cream italic):
  jv13  Gen 28:13  "I am the LORD God of Abraham thy father... to thee will I give it"
  jv15  Gen 28:15  "I am with thee, and will keep thee in all places..." — THE promise

WHY-LAW: the misread is that God only meets the deserving. The point is the opposite —
God met Jacob at his lowest: a runaway who had lied to his father and cheated his
brother, alone in the dark with a rock for a pillow. No altar, no ceremony. And there
God gave him an unearned promise of presence: I am with thee, and will keep thee.
Milk framing: comfort for the guilty, the runaway, the lonely. An invitation, never a
threat. Nobody is harmed.

HOMOGRAPH EAR-CHECK: none of the high-risk words (bow/wind/live/tears/lead) appear in
the KJV lines here. "whither" and "Bethel" are read plainly.

NUMBER-STRESS LAW: no sentence opens with a bare number.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"
LORD = "en-US-ChristopherNeural"

SEGMENTS = [
    ("n1", NARRATOR, "-20%", "-4Hz",
     "Jacob was running. He had lied to his blind father and cheated his own brother, "
     "and now he was fleeing for his life, alone, with everything he knew behind him.", None),
    ("n2", NARRATOR, "-22%", "-4Hz",
     "When the sun went down he was in the middle of nowhere. No home, no bed, no "
     "welcome. He took a stone, put it under his head for a pillow, and lay down in the "
     "dark to sleep.", None),
    ("n3", NARRATOR, "-22%", "-4Hz",
     "And there, in the last place he would have expected it, God came to him in a "
     "dream. He saw a great stairway rising from the very ground where he lay, all the "
     "way up into an opening in heaven.", None),
    ("n4", NARRATOR, "-22%", "-4Hz",
     "And on it the angels of God were going up and coming down, moving between heaven "
     "and this lonely patch of dirt where a runaway lay sleeping. Heaven was not far off. "
     "It was open, right above him.", None),
    # --- jv13: the covenant ---
    ("jv13", LORD, "-24%", "-6Hz",
     "I am the LORD God of Abraham thy father, and the God of Isaac: the land whereon "
     "thou liest, to thee will I give it, and to thy seed.", None),
    ("n5", NARRATOR, "-22%", "-4Hz",
     "God did not scold him for what he had done. He stood above the stairway and made "
     "him a promise — the same promise he had made to his grandfather Abraham. This "
     "wanderer with nothing would become a family as many as the dust of the earth.", None),
    # --- jv15: THE promise — sacred silence ---
    ("jv15", LORD, "-26%", "-6Hz",
     "And, behold, I am with thee, and will keep thee in all places whither thou goest, "
     "and will bring thee again into this land; for I will not leave thee, until I have "
     "done that which I have spoken to thee of.", None),
    ("n6", NARRATOR, "-22%", "-4Hz",
     "I am with thee. I will keep thee. I will not leave thee. To a man who had just "
     "thrown his whole life away and run, God promised to go with him, everywhere, and "
     "never let go. He had done nothing to earn it.", None),
    # --- Jacob wakes ---
    ("n7", NARRATOR, "-22%", "-4Hz",
     "Jacob woke with a start, shaken to his core. Surely the Lord is in this place, he "
     "said, and I did not even know it. This is nothing less than the house of God. This "
     "is the gate of heaven — and I nearly slept through it.", None),
    ("n8", NARRATOR, "-22%", "-4Hz",
     "So he took the stone that had been his pillow and stood it up on end as a pillar, "
     "a marker of the place where heaven had opened over him.", None),
    ("n8b", NARRATOR, "-22%", "-4Hz",
     "And he poured oil over the top of it to set it apart as holy, and he called that "
     "place Bethel — the house of God.", None),
    # --- closing frame ---
    ("n9", NARRATOR, "-24%", "-4Hz",
     "Then he went on his way — the same road, the same troubles waiting ahead, but a "
     "different man. Not because he had fixed himself, but because he finally knew he was "
     "not walking alone. That is how God still meets people: not at their best, but "
     "wherever they happen to lie down in the dark.", None),
    # --- closing card ---
    ("card", NARRATOR, "-26%", "-4Hz",
     "God met a runaway with a rock for a pillow, and promised to go with him and never "
     "leave. If heaven is that near even to the one who ran, what might God be wanting to "
     "say to you, right where you are?", None),
]


async def main():
    for name, voice, rate, pitch, text, cap in SEGMENTS:
        tts = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")


if __name__ == "__main__":
    import os
    os.makedirs("audio", exist_ok=True)
    asyncio.run(main())
