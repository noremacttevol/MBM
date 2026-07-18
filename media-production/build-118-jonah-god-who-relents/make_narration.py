#!/usr/bin/env python3
"""Narration audio for Video #118 — Jonah and the God Who Relents (Book of Jonah).

Narrator: en-US-AndrewNeural. God's voice: en-US-ChristopherNeural (exact KJV only).
Jonah's own warning ("yet forty days...") is voiced by the NARRATOR (white caption); God's
own KJV lines render cream-italic in the scripture voice.

God's KJV lines (Christopher, cream italic):
  jvA  Jonah 3:2   "Arise, go unto Nineveh, that great city, and preach unto it the
                    preaching that I bid thee." — sacred silence 1 (the second chance)
  jvB  Jonah 4:11  "And should not I spare Nineveh, that great city, wherein are more than
                    sixscore thousand persons... and also much cattle?" — sacred silence 2

CARE FLAG J (Jonah): the MERCY is the story. God relents; Nineveh is SPARED on screen and in
the card. Judgment is spoken ("yet forty days") but the destruction never falls and is never
depicted. The fish is God's rescue, not a punishment.

WHY-LAW: Jonah runs because he is afraid God is TOO forgiving toward people he thinks deserve
ruin. Every surprise in the book bends toward mercy — the fish saves instead of drowns; the
violent city repents; God relents and spares a hundred thousand strangers. Milk framing: God
is not eager to destroy; he is eager to spare, and he will chase down a running prophet just
to rescue a city that turns. An invitation to trust that mercy, never a threat.

HOMOGRAPH EAR-CHECK: 'sixscore' reads six-score plainly; no high-risk homographs.
NUMBER-STRESS LAW obeyed ("forty days", "three days and three nights").
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"
GOD = "en-US-ChristopherNeural"

SEGMENTS = [
    ("n1", NARRATOR, "-20%", "-4Hz",
     "God had a hard errand for a man named Jonah. He was to go to Nineveh — a huge, "
     "violent, foreign city — and warn them, because God would far rather warn a wicked "
     "city than lose it.", None),
    ("n2", NARRATOR, "-22%", "-4Hz",
     "But Jonah did not want mercy for people like that. So he ran. He found a ship going "
     "the exact opposite way and sailed off, trying to put an ocean between himself and a "
     "God he thought was far too forgiving.", None),
    ("n3", NARRATOR, "-22%", "-4Hz",
     "A great storm caught the ship, so fierce the sailors were sure they would all drown. "
     "Jonah knew the storm was because of him. So at last they did the only thing left, and "
     "cast him into the raging sea.", None),
    ("n4", NARRATOR, "-22%", "-4Hz",
     "And here is the first surprise of this story. The sea should have been the end of "
     "him. Instead, God sent a great fish — not to punish Jonah, but to catch him, and "
     "carry him, and keep him alive in the deep.", None),
    ("n5", NARRATOR, "-22%", "-4Hz",
     "For three days and three nights, in the dark, Jonah finally stopped running. From the "
     "belly of the fish he prayed, and his hard, resentful heart began at last to turn back "
     "toward the God who would not let him drown.", None),
    # jvA — Arise, go unto Nineveh (the second chance) — sacred silence 1
    ("jvA", GOD, "-26%", "-6Hz",
     "Arise, go unto Nineveh, that great city, and preach unto it the preaching that I bid "
     "thee.", None),
    ("n6", NARRATOR, "-22%", "-4Hz",
     "The fish set him safe on dry land, and God gave him the errand again. This time Jonah "
     "went. He walked into the great city and cried out his warning: yet forty days, and "
     "Nineveh shall be overthrown.", None),
    ("n7", NARRATOR, "-22%", "-4Hz",
     "And the second surprise is bigger than the first. They listened. From the king on his "
     "throne down to the poorest beggar, the whole city turned — sackcloth, fasting, and "
     "honest sorrow — begging God for mercy they knew they did not deserve.", None),
    ("n8", NARRATOR, "-22%", "-4Hz",
     "And God, who had been looking for a reason to spare them all along, saw that they "
     "turned from their evil — and he relented. He did not destroy the city. He forgave it. "
     "The judgment never fell.", None),
    # jvB — And should not I spare Nineveh — sacred silence 2 (the mercy climax)
    ("jvB", GOD, "-26%", "-6Hz",
     "And should not I spare Nineveh, that great city, wherein are more than sixscore "
     "thousand persons that cannot discern between their right hand and their left hand; and "
     "also much cattle?", None),
    ("card", NARRATOR, "-26%", "-4Hz",
     "The whole book of Jonah exists to answer one question: is God eager to destroy, or "
     "eager to spare? He spared a city of a hundred thousand strangers the moment they "
     "turned. What would it change to believe God is that quick to forgive?", None),
]


async def main():
    for name, voice, rate, pitch, text, cap in SEGMENTS:
        await save_narration(text, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")


if __name__ == "__main__":
    import os
    os.makedirs("audio", exist_ok=True)
    asyncio.run(main())
