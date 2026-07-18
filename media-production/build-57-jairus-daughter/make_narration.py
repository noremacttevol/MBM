#!/usr/bin/env python3
"""Generate narration audio for Video #57 — Jairus's Daughter (Mark 5:21-24, 35-43).

Narrator: en-US-AndrewNeural — plain American, never a Multilingual model.
Jesus voice: en-US-ChristopherNeural — American, never British.

Jesus speaks ONLY exact KJV. Two red-letter lines are used as the sacred silences:
  jv36 = Mark 5:36  "Be not afraid, only believe."     (SACRED SILENCE 1 — to Jairus)
  jv41 = Mark 5:41  "Damsel, I say unto thee, arise."  (SACRED SILENCE 2 — the raising)
(His "not dead, but sleepeth" line is reported by the narrator, not red-lettered here.)

TRANSLATION LAW: after each KJV line the narrator gives plain meaning and never re-quotes
it. The messengers' and mourners' words are reported plainly in the narrator's white style.

HOMOGRAPH LAW: deliberately AVOIDED "live" (verb /liv/ vs adj /laɪv/) by writing "be healed
and made well". No other TTS homographs remain; SPOKEN is empty.

CARE — R (RESTRAINT): a dying, then dead, then raised child, shown with the utmost gentleness
— the girl lying peacefully as if only asleep, never morbid, no gore. The mourners' wailing
is heard of, not made frightening. The hope-beat is the girl up and walking, and the tender
"give her something to eat." Ends on an open invitation.

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
    # --- s1: Jairus falls at his feet ---
    ("n1", NARRATOR, "-20%", "-4Hz",
     "A man named Jairus, a leader of the synagogue, pushed through the crowd and fell "
     "down at Jesus' feet. His little girl, his only daughter, twelve years old, was "
     "dying at home, and he begged Jesus to come and lay his hands on her, so that she "
     "would be healed and made well."),
    # --- s2: Jesus goes with him ---
    ("n2", NARRATOR, "-22%", "-4Hz",
     "So Jesus went with him. A great crowd pressed in on every side as they hurried "
     "toward the house, the desperate father leading the way, praying there was still "
     "time."),
    # --- s3: the worst news ---
    ("n3", NARRATOR, "-22%", "-4Hz",
     "But before they arrived, messengers came from the house with the worst news a "
     "father can hear. Your daughter is dead, they said; why trouble the Teacher any "
     "further? And Jairus' heart broke in the middle of the road."),
    # --- s4: jv36 — be not afraid. SACRED SILENCE 1. ---
    ("jv36", JESUS, "-26%", "-6Hz",
     "Be not afraid, only believe."),
    # --- s5: not dead, but sleeping ---
    ("n4", NARRATOR, "-22%", "-4Hz",
     "At the house the mourning had already begun, people weeping and wailing loudly for "
     "the little girl. Jesus told them the child was not dead, but only asleep. And they "
     "laughed at him, certain that she was gone."),
    # --- s6: he takes the few in ---
    ("n5", NARRATOR, "-22%", "-4Hz",
     "He put them all outside. Then he took the girl's father and mother, and three of "
     "his closest friends, and went in quietly to where the child was lying, small and "
     "still."),
    # --- s7: jv41 — damsel, arise. SACRED SILENCE 2. ---
    ("jv41", JESUS, "-26%", "-6Hz",
     "Damsel, I say unto thee, arise."),
    # --- s8: she arose and walked ---
    ("n6", NARRATOR, "-22%", "-4Hz",
     "He took her by the hand, and immediately she got up, and began to walk. She was "
     "twelve years old. Her parents were beside themselves with wonder, holding the "
     "daughter they had already grieved as lost."),
    # --- s9: give her to eat ---
    ("n7", NARRATOR, "-24%", "-4Hz",
     "And then Jesus said the most tender, ordinary thing: give her something to eat. He "
     "had just raised her from death, and his very next thought was that a growing girl "
     "would be hungry. The small things mattered to him too."),
    # --- closing card, read gently (Readable-Card Law) ---
    ("card", NARRATOR, "-26%", "-4Hz",
     "He is never too late, even when everyone says he is. He walks into the room the "
     "world has already given up on, takes the hand no one else could reach, and speaks "
     "life. And then he thinks of your smallest needs, too. What have you decided is "
     "finally too far gone for him?"),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        spoken = SPOKEN.get(name, text)
        await save_narration(spoken, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")


if __name__ == "__main__":
    asyncio.run(main())
