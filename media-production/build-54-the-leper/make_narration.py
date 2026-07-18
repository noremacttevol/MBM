#!/usr/bin/env python3
"""Generate narration audio for Video #54 — The Leper Made Clean (Mark 1:40-45).

Narrator: en-US-AndrewNeural — plain American, never a Multilingual model.
Jesus voice: en-US-ChristopherNeural — American, never British.

Jesus speaks ONLY exact KJV. One line — his whole speech in this passage:
  jv41 = Mark 1:41  "I will; be thou clean."   (SACRED SILENCE — the touch)

TRANSLATION LAW: after the KJV line the narrator gives plain meaning and never re-quotes
it. The leper's own plea ("If thou wilt, thou canst make me clean") is NOT red-letter —
the narrator reports it plainly; it is captioned in the narrator's plain white style.

HOMOGRAPH LAW: no TTS homographs in this text (no live/bow/wound/read/tear/wind/lead/sow).
SPOKEN is empty.

CARE — R (RESTRAINT): leprosy is shown gently — pale greyish skin, wrapped hands, an
outcast's loneliness — never graphic sores, never gruesome. The heart of it is the touch:
the untouchable man is touched before he is even healed. Hope-beat is the clean, restored
man who can go home. Ends on an open invitation, never fear.

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
    # --- s1: the outcast ---
    ("n1", NARRATOR, "-20%", "-4Hz",
     "In those days there was no lonelier life than a leper's. The disease wasted his "
     "skin, and the law kept him apart from everyone he loved — no home, no temple, no "
     "touch, made to cry out 'unclean' if anyone drew near. He had not felt a kind hand "
     "in years."),
    # --- s2: if thou wilt ---
    ("n2", NARRATOR, "-22%", "-4Hz",
     "When he heard that Jesus was near, he did the forbidden thing: he came close. He "
     "fell on his knees and begged him — if you are willing, he said, you can make me "
     "clean. He never doubted the power; he only wondered about the will."),
    # --- s3: moved with compassion ---
    ("n3", NARRATOR, "-22%", "-4Hz",
     "And Jesus was moved with compassion. He did not step back from the man everyone "
     "else stepped back from. He reached out his hand toward the very thing no one would "
     "touch."),
    # --- s4: jv41 — I will; be thou clean. SACRED SILENCE. ---
    ("jv41", JESUS, "-26%", "-6Hz",
     "I will; be thou clean."),
    # --- s5: the leprosy departed ---
    ("n4", NARRATOR, "-22%", "-4Hz",
     "And he touched him. Before the healing had even come, the untouchable man was "
     "touched; and then, at once, the leprosy left him, and his skin was made new."),
    # --- s6: made whole ---
    ("n5", NARRATOR, "-22%", "-4Hz",
     "The sores were gone. The pale, wasted skin was warm and whole again, like the skin "
     "of a young child. In a moment he was clean, and more than clean; he was a man who "
     "could go home."),
    # --- s7: see thou tell no man ---
    ("n6", NARRATOR, "-22%", "-4Hz",
     "Jesus told him to say nothing, but to go and show himself to the priest, and be "
     "given back, quietly, the whole life that had been taken from him."),
    # --- s8: he published it abroad ---
    ("n7", NARRATOR, "-22%", "-4Hz",
     "But the man could not hold it in. He went out and told everyone, freely, "
     "everywhere; how could he not? The mercy was far too great to keep to himself."),
    # --- s9: they came to him from every quarter ---
    ("n8", NARRATOR, "-24%", "-4Hz",
     "And so the news ran ahead of him, until he could hardly walk into a town in the "
     "open, and people came to him from every direction, out of every corner of the "
     "land."),
    # --- closing card, read gently (Readable-Card Law) ---
    ("card", NARRATOR, "-26%", "-4Hz",
     "He is still willing. There is no part of you so unclean, so far gone, so long "
     "untouched, that he will draw back his hand from it. He reaches for the very thing "
     "you are most ashamed of and says, I will. What would you ask him to make clean?"),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        spoken = SPOKEN.get(name, text)
        await save_narration(spoken, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")


if __name__ == "__main__":
    asyncio.run(main())
