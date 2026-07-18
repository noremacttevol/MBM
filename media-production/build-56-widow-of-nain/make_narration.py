#!/usr/bin/env python3
"""Generate narration audio for Video #56 — The Widow of Nain's Son (Luke 7:11-17).

Narrator: en-US-AndrewNeural — plain American, never a Multilingual model.
Jesus voice: en-US-ChristopherNeural — American, never British.

Jesus speaks ONLY exact KJV. Two lines — his whole speech in this passage:
  jv13 = Luke 7:13  "Weep not."                          (SACRED SILENCE 1 — compassion)
  jv14 = Luke 7:14  "Young man, I say unto thee, Arise." (SACRED SILENCE 2 — the raising)

TRANSLATION LAW: after each KJV line the narrator gives plain meaning and never re-quotes
it. The crowd's praise is reported plainly, captioned in the narrator's plain white style.

HOMOGRAPH LAW: deliberately AVOIDED "tears" (crying /teerz/ vs rips /tairz/) by writing
"her sorrow" / "by grief". No other TTS homographs remain; SPOKEN is empty.

CARE — R (RESTRAINT): a funeral and a dead body, shown with dignity and never gruesome —
the young man wrapped in pale burial linen, peaceful as if asleep, no decay, no gore. The
widow's grief is real but never melodramatic. The heart is compassion; the hope-beat is the
son restored to his mother. Ends on an open invitation.

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
    # --- s1: nearing Nain ---
    ("n1", NARRATOR, "-20%", "-4Hz",
     "As Jesus came near the town of Nain, a great crowd walked along with him. It was an "
     "ordinary day on an ordinary road, until they reached the town gate and met something "
     "coming the other way."),
    # --- s2: the funeral ---
    ("n2", NARRATOR, "-22%", "-4Hz",
     "Out of the gate came a funeral. A young man had died, carried out on an open bier, "
     "and behind him walked his mother, a widow, grieving. He was her only son, and now "
     "she had no one. A large crowd from the town walked with her in her sorrow."),
    # --- s3: he saw her ---
    ("n3", NARRATOR, "-22%", "-4Hz",
     "When the Lord saw her, he did not see a crowd or a custom; he saw a mother who had "
     "lost everything. And his heart broke for her. No one there asked him to do a single "
     "thing. He simply could not walk past her sorrow."),
    # --- s4: jv13 — weep not. SACRED SILENCE 1. ---
    ("jv13", JESUS, "-26%", "-6Hz",
     "Weep not."),
    # --- s5: he touched the bier ---
    ("n4", NARRATOR, "-22%", "-4Hz",
     "Then he did something no one does at a funeral. He walked up and touched the bier, "
     "and the men carrying it stood still. The whole procession held its breath. And he "
     "spoke to the dead as though the young man were only asleep."),
    # --- s6: jv14 — arise. SACRED SILENCE 2. ---
    ("jv14", JESUS, "-26%", "-6Hz",
     "Young man, I say unto thee, Arise."),
    # --- s7: he sat up ---
    ("n5", NARRATOR, "-22%", "-4Hz",
     "And the young man who had been dead sat up, and began to speak. Life poured back "
     "into him at the sound of that voice, as simply as morning comes. Death let go of "
     "him, because it had no choice."),
    # --- s8: gave him to his mother ---
    ("n6", NARRATOR, "-22%", "-4Hz",
     "And Jesus took him by the hand and gave him back to his mother. He did not keep him "
     "or make a spectacle of him; he simply returned a son to the arms of the woman who "
     "thought she had buried him."),
    # --- s9: they glorified God ---
    ("n7", NARRATOR, "-24%", "-4Hz",
     "A holy fear fell on everyone there, and they praised God, saying a great prophet has "
     "risen among us, and God has visited his people. And the news of it went out through "
     "all the country round about."),
    # --- closing card, read gently (Readable-Card Law) ---
    ("card", NARRATOR, "-26%", "-4Hz",
     "He still meets us at the gate, on the worst day, in the middle of a grief no one "
     "can fix. He is not put off by death, or by sorrow, or by a thing everyone else has "
     "given up on. He sees you, his heart breaks, and he speaks life. What have you "
     "already buried that he is asking to raise?"),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        spoken = SPOKEN.get(name, text)
        await save_narration(spoken, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")


if __name__ == "__main__":
    asyncio.run(main())
