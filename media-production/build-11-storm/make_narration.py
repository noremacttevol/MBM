#!/usr/bin/env python3
"""Generate narration audio for Story Video #11 — Calming the Storm
(Mark 4:35-41).
Narrator: en-US-AndrewNeural — plain American, never Multilingual.
Jesus voice: en-US-ChristopherNeural — American, never British.
Jesus speaks ONLY exact KJV: Mark 4:35 (j0), 4:39 (j1), 4:40 (j2) —
fetched from bible-api.com (qc/mark4-kjv.txt), never hand-typed.
Pre-flighted on paper per PRODUCTION-BIBLE §4b — see PREFLIGHT.md.
Translation Law: no narrator line echoes KJV Jesus wording; the narrator
may quote the DISCIPLES modernly (v38, v41 are their words, not his).
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    # n0 — evening shore (s1). v35 setup: worn out from teaching all day.
    ("n0", NARRATOR, "-20%", "-4Hz",
     "Evening, on the Sea of Galilee. Jesus had been teaching crowds on "
     "the shore all day — story after story, until the light was going "
     "and his voice was nearly gone with it. He was worn through. And "
     "when the last story was told, he said to his friends:"),
    # J0 — exact KJV Mark 4:35.
    ("j0", JESUS, "-27%", "-6Hz",
     "Let us pass over unto the other side."),
    # n1 — even as he was; other little ships (s2). v36 gems.
    ("n1", NARRATOR, "-20%", "-4Hz",
     "So they took him, Mark says, even as he was — no rest, no supper, "
     "straight from the last word into the boat. Other little boats "
     "followed them out. And here is something worth knowing about the "
     "men at the oars: at least four of them were professional "
     "fishermen. This lake was their workplace. They had crossed it at "
     "night their whole lives. Nothing about dark water scared them."),
    # n2 — THE STORM (s3 still + clip). v37 + the WHY-gem about the lake.
    ("n2", NARRATOR, "-22%", "-4Hz",
     "Then the lake turned on them. The Sea of Galilee lies seven "
     "hundred feet below sea level, in a bowl of hills — when cold wind "
     "spills down those slopes, calm water can turn violent in minutes. "
     "This storm was savage even by that lake's standard. Waves broke "
     "over the side faster than the men could bail. The boat was "
     "filling. And the fishermen who had survived a hundred storms "
     "looked at this one — and believed it was going to be their last."),
    # n3 — asleep on the cushion (s4). v38a.
    ("n3", NARRATOR, "-24%", "-4Hz",
     "And Jesus was asleep. In the stern, on the steersman's cushion, "
     "soaked with spray, rising and falling with the pitching deck — "
     "asleep. Not because he didn't know what was happening. Because "
     "he wasn't afraid of it."),
    # n4 — don't you care? (s5). v38b — they doubted his heart, not his power.
    ("n4", NARRATOR, "-22%", "-4Hz",
     "So they woke him. Rough hands on his shoulder, screaming over the "
     "wind the question people have been asking in storms ever since: "
     "Teacher — don't you care that we are going down? Listen to what "
     "they were really saying. They never doubted his power. They "
     "doubted his heart."),
    # n5 — he stood up (s6 still). Setup for the KJV line; music dies here.
    ("n5", NARRATOR, "-24%", "-4Hz",
     "He got up. He stood in the stern of a sinking boat, in the middle "
     "of the worst storm those fishermen had ever seen. And he did not "
     "speak to the men. He spoke to the storm."),
    # J1 — exact KJV Mark 4:39. Spoken into TRUE SILENCE; the calm clip
    # plays under and after it. ALL sound is out before this line ends.
    ("j1", JESUS, "-30%", "-6Hz",
     "Peace, be still."),
    # n6 — the great calm (s7). v39b + the swell gem. Quiet, slow.
    ("n6", NARRATOR, "-26%", "-4Hz",
     "And the wind quit. The sea fell flat — glass flat — with stars "
     "where the storm had been, and the only sound left was water "
     "dripping off the ropes. Sailors will tell you the waves keep "
     "rolling for hours after a wind dies. These didn't. The lake did "
     "not calm down. It obeyed."),
    # n7 — he turned to them (s8 setup). v40 lead-in.
    ("n7", NARRATOR, "-24%", "-4Hz",
     "Then he turned to his friends — soaked, shaking, still gripping "
     "the ropes — and he asked them, gently:"),
    # J2 — exact KJV Mark 4:40.
    ("j2", JESUS, "-27%", "-6Hz",
     "Why are ye so fearful? how is it that ye have no faith?"),
    # n8 — translation bridge (Translation Law: modern meaning only) + Seed.
    ("n8", NARRATOR, "-24%", "-4Hz",
     "Hear where he asked that from. Standing in their boat, on the sea "
     "he had just flattened to save them. He didn't ask it from the "
     "shore. He came through the storm with them — and then he asked "
     "why the fear had gotten so much bigger than their trust. He never "
     "said the storm wasn't real. He never scolded them for waking him. "
     "He was simply bigger than it."),
    # n9 — what manner of man (s9). v41 + the psalm gem.
    ("n9", NARRATOR, "-24%", "-4Hz",
     "And then a strange thing happened: the fear didn't leave the "
     "boat — it changed direction. Mark says they feared exceedingly — "
     "more awe after the calm than in the storm — and they asked each "
     "other: what kind of man is this, that even the wind and the sea "
     "do what he says? These men knew their scriptures. They knew the "
     "old psalm that says it is God who stills the storm to a whisper. "
     "And now they were staring at a man in dripping clothes who had "
     "just done it."),
    # n10 — the closing card, read aloud gently (Readable-Card Law).
    # INVITATION, not a fear-question (closing-card law, Cameron 2026-07-15).
    ("n10", NARRATOR, "-26%", "-4Hz",
     "Whatever storm you are in tonight, hear this: the same Jesus is "
     "still in the boat with you. He has not left you alone in it. Bring "
     "him your fear, and let him speak his peace over your storm."),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        await save_narration(text, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
