#!/usr/bin/env python3
"""Narration for Story Video #21 — The Lost Sheep (Luke 15:1-7).

PROVENANCE: the shipped luke-15_lost-sheep.mp4 was assembled by Machine C
(Cameron Lovett MS) on the shared prep, from the 7 s*-named stills in assets/.
This file is the narration script RECONCILED to that delivered cut (recovered
from the finished audio and cleaned to exact KJV), so the repo is honest and the
narration is regenerable + ear-checkable. Regenerating here reproduces the same
spoken script; the approved mp4 itself is kept as the deliverable.

Narrator: en-US-AndrewNeural — plain American, never a Multilingual model.
Jesus voice: en-US-ChristopherNeural — American, never British.
Jesus speaks ONLY exact KJV: Luke 15:4 (j1), 15:5 (j2), 15:6 (j3), 15:7 (j4).
CAPTIONS ARE VERBATIM. After each KJV line the narrator gives only the plain
modern meaning and never re-quotes the KJV words (Translation Law).
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text) — text is BOTH spoken and captioned.
    # --- s1-gathering: the murmur (Luke 15:1-2) ---
    ("n1", NARRATOR, "-20%", "-4Hz",
     "The people everyone else had written off — the cheats, the outcasts, the "
     "ones with a past — kept crowding in close to hear Jesus."),
    ("n2", NARRATOR, "-22%", "-4Hz",
     "And the religious men muttered about it. This man welcomes sinners, they "
     "said, and even eats with them."),
    ("n3", NARRATOR, "-22%", "-4Hz",
     "So Jesus told them a story about how heaven really feels about one lost "
     "person."),
    # --- s2-flock-dusk: the parable's core (KJV j1 = Luke 15:4) ---
    ("j1", JESUS, "-26%", "-6Hz",
     "What man of you, having an hundred sheep, if he lose one of them, doth not "
     "leave the ninety and nine in the wilderness, and go after that which is "
     "lost, until he find it?"),
    ("n4", NARRATOR, "-22%", "-4Hz",
     "Which of you, he asks, with a hundred sheep, would not leave the "
     "ninety-nine behind to go after the one that wandered off, and keep "
     "searching until you found it?"),
    # --- s3-leaves: he leaves the ninety-nine ---
    ("n5", NARRATOR, "-22%", "-4Hz",
     "He does not stand there counting what he still has. He leaves the "
     "ninety-nine behind to go out after the one that is gone."),
    # --- s4-searches-night: through the night ---
    ("n6", NARRATOR, "-22%", "-4Hz",
     "He searches through the night, over the rocks and the ravines, calling "
     "into the dark, because to him that one is not a loss he can shrug off. "
     "That one is his."),
    # --- s5-finds: found it (KJV j2 = Luke 15:5), reverent pause after ---
    ("n7", NARRATOR, "-24%", "-5Hz",
     "And when he finds it — frightened, tangled in the thorns, too worn out to "
     "walk — he does not scold it, and he does not leave it there."),
    ("j2", JESUS, "-26%", "-6Hz",
     "And when he hath found it, he layeth it on his shoulders, rejoicing."),
    # --- s6-shoulders: carries it home ---
    ("n8", NARRATOR, "-22%", "-4Hz",
     "He lifts it up, lays it across his own shoulders, and carries it the whole "
     "way home, rejoicing. Not relieved. Not annoyed at the trouble. Rejoicing."),
    # --- s7-rejoicing: the homecoming (KJV j3 = 15:6, j4 = 15:7) ---
    ("n9", NARRATOR, "-22%", "-4Hz",
     "Then he calls everyone together — friends, neighbors, the whole village — "
     "and throws a celebration."),
    ("j3", JESUS, "-25%", "-6Hz",
     "Rejoice with me; for I have found my sheep which was lost."),
    ("j4", JESUS, "-26%", "-6Hz",
     "I say unto you, that likewise joy shall be in heaven over one sinner that "
     "repenteth, more than over ninety and nine just persons, which need no "
     "repentance."),
    ("n10", NARRATOR, "-23%", "-4Hz",
     "That is how good he is. Heaven throws a party over one person turning back. "
     "Not a lecture. Not a grudge. Joy."),
    # --- closing card, read gently (Readable-Card Law) ---
    ("card", NARRATOR, "-26%", "-4Hz",
     "To him, you were never one of a crowd. Have you ever felt like the one who "
     "wandered too far to be worth coming after?"),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
