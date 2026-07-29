#!/usr/bin/env python3
"""Generate narration audio for Story Video #137 — "One, as we are one"
(John 17:20-23). From DRAFTS/row-137-one-as-we-are-one.md (v2 — the swapped
story that REPLACED the purged Stephen dupe, 2026-07-20 repeat audit).

The whole video is Jesus's own prayer the night before he died: he prays that
his followers become one THE SAME WAY he and the Father are one — perfect
unity between DISTINCT persons, the Godhead from Jesus's own lips. No church
named (row spec).

Jesus lines are EXACT KJV red-letter (John 17:20-21, 22-23a), Jesus voice.
The Father is addressed, not seen — no divine figure is depicted in this
build (no vision occurs in John 17).

HOMOGRAPH LAW: scanned — "perfect" (PER-fect, safe), "loved" (safe); no
bow/wound/wind/tears/lead/sow/live/read/dove/close voiced. Ear-check anyway.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR

# (id, speaker, caption_text). The caption always shows this exact text; only
# the string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR,
     "The night before he died, Jesus stopped to pray. And in that prayer, "
     "he prayed for someone you might not expect — for everyone who would "
     "ever believe. That includes you."),
    # Exact KJV John 17:20-21 — sacred silence around it.
    ("j1", JESUS,
     "Neither pray I for these alone, but for them also which shall believe "
     "on me through their word; that they all may be one; as thou, Father, "
     "art in me, and I in thee, that they also may be one in us."),
    ("n1", NARRATOR,
     "Listen to how he asks. He prays that his followers will be one — the "
     "same way he and his Father are one."),
    ("n2", NARRATOR,
     "If that oneness meant one single being, this prayer would be asking "
     "millions of believers to melt into one person. It doesn't ask that. "
     "It asks for perfect unity between distinct persons."),
    # Exact KJV John 17:22-23a — sacred silence around it.
    ("j2", JESUS,
     "And the glory which thou gavest me I have given them; that they may "
     "be one, even as we are one: I in them, and thou in me, that they may "
     "be made perfect in one."),
    ("n3", NARRATOR,
     "The Father and the Son are perfectly one — one in purpose, one in "
     "love, one in glory. Two persons, one heart. And Jesus prayed that you "
     "would be brought into that same oneness."),
    ("card", NARRATOR,
     "The night before he died, he prayed for you — that you would be one "
     "with them, as they are one with each other."),
]

# Homographs this build decides for itself (never auto-replaced globally).
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
