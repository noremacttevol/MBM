#!/usr/bin/env python3
"""Narration for build-156-famine-of-hearing — Amos 8.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

Both red beats become GREEN. Amos 8:11-12 is one continuous oracle spoken by the LORD in first person — 'I will send a famine in the land' — so it is Jehovah, the premortal Christ. Old Testament Deity speech is never red; a red-letter KJV leaves it black because Christ had not yet come in the flesh.

  kv11  Amos 8:11  god (was red)
  kv12  Amos 8:12  god (was red)

kv11 is technically mixed — 'saith the Lord GOD' is Amos's attribution wrapped around God's own words. It is NOT split. Splitting three words of attribution out into a separate blue beat would break the line in half for no gain and read worse than it sounds now. The segment as a whole is God speaking; it stays whole and green. This is the judgment call the law leaves open, and it goes the same way in build-128.

kv12 continues the same divine speech ('they shall wander...'), still the LORD describing what he will bring about, not Amos commenting. Green.

Both lines already have narrator retellings after them (n4, n7). Nothing added, nothing lifted — this build's narrator already does the retelling work well.

WHY-LAW: the ache proves the thing you ache for is real. A famine of hearing ends in a harvest.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import GOD, NARRATOR

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "The prophet Amos gave his people a strange warning. A famine is coming, he said. But not the kind you are picturing. There would be bread on the tables and water in the wells, and still the land would starve."),
    ("n2", NARRATOR, "It would be a famine of a different kind — a hunger for the word of God. A time when the living voice from heaven grew scarce, and people ached for it without always knowing what the ache even was."),
    ("n3", NARRATOR, "You could go about your days, eat your fill, and still feel a hollow place inside that no meal could reach — a quiet starving of the soul for something true and living from God."),
    # Amos 8:11
    ("kv11", GOD, "Behold, the days come, saith the Lord GOD, that I will send a famine in the land, not a famine of bread, nor a thirst for water, but of hearing the words of the LORD:"),
    ("n4", NARRATOR, "And when people feel that kind of hunger, they do what hungry people do. They go looking. They search high and low, near and far, hoping to stumble on the thing that will finally fill them."),
    ("n5", NARRATOR, "Amos saw them wandering from one end of the world to the other, running here and there, chasing every rumor of where the word of God might still be found."),
    ("n6", NARRATOR, "But in a famine of the word, the seeking alone does not satisfy. They looked, and looked, and could not lay hold of it — because what they were hungry for had grown rare in the land."),
    # Amos 8:12
    ("kv12", GOD, "And they shall wander from sea to sea, and from the north even to the east, they shall run to and fro to seek the word of the LORD, and shall not find it."),
    ("n7", NARRATOR, "But think about what that hunger really means. You do not ache for what was never real. The very fact that a soul can starve for God's word is proof that such a word exists, and that it was always meant to be found."),
    ("n8", NARRATOR, "So a famine is never the end of the story; it is the ache that comes right before the harvest. God does not leave his people hungry forever. So the only question is a hopeful one. When the word is set before you again, will you sit down and eat?"),
    ("card", NARRATOR, "Amos foretold a famine — not of bread, but of hearing the word of God. Yet a hunger like that is a promise: you only starve for what is real. When the word is offered again, will you feed on it?"),
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
