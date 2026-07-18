#!/usr/bin/env python3
"""Generate narration audio for Story Video #156 — "A famine of hearing the words of
the LORD" (Amos 8:11-12). MEMBER shelf verse-video. → Gospel Library topic: Apostasy.

Narrator: en-US-AndrewNeural — plain American, modern paraphrase, never a
Multilingual model, never echoes the KJV wording.
Scripture voice: en-US-ChristopherNeural — speaks the KJV text EXACTLY.
(Amos is Old-Testament prophecy; the scripture voice carries the verse. Christ is NOT
depicted; the famine is shown only as spiritual hunger and searching — no accusation,
no villain, no specific church.)

KJV lines (exact):
  kv11 = Amos 8:11  a famine... of hearing the words of the LORD (NAMED VERSE — SACRED SILENCE 1)
  kv12 = Amos 8:12  wander from sea to sea... shall not find it (SACRED SILENCE 2)

WHY-LAW: the ache is a promise — you only starve for what is real; a famine is the hunger
right before the harvest. STUDY GEMS: not a famine of bread but of the word (n2); you can
be full and still hollow (n3); the very hunger proves the word exists and is meant to be
found (n7); God does not leave his people hungry forever (n8).

TRANSLATION LAW: the narrator never re-quotes a KJV line. n2 says "a hunger for the word
of God," delivered as paraphrase; the exact KJV lands only in kv11/kv12.

MILK FRAMING: an invitation. The closing card ends on an open question and a one-line
pointer to the Gospel Library topic (Apostasy). No shame, no fear, no accusing any group.
CHRIST IS NEVER DEPICTED; the word/hope is shown only as warm light or bread.

NUMBER-STRESS LAW: no sentence opens with a bare number.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"
SCRIPTURE = "en-US-ChristopherNeural"

SEGMENTS = [
    ("n1", NARRATOR, "-20%", "-4Hz",
     "The prophet Amos gave his people a strange warning. A famine is coming, he said. "
     "But not the kind you are picturing. There would be bread on the tables and water "
     "in the wells, and still the land would starve."),
    ("n2", NARRATOR, "-22%", "-4Hz",
     "It would be a famine of a different kind — a hunger for the word of God. A time "
     "when the living voice from heaven grew scarce, and people ached for it without "
     "always knowing what the ache even was."),
    ("n3", NARRATOR, "-22%", "-4Hz",
     "You could go about your days, eat your fill, and still feel a hollow place inside "
     "that no meal could reach — a quiet starving of the soul for something true and "
     "living from God."),
    # kv11 — NAMED VERSE, SACRED SILENCE 1
    ("kv11", SCRIPTURE, "-26%", "-6Hz",
     "Behold, the days come, saith the Lord GOD, that I will send a famine in the land, "
     "not a famine of bread, nor a thirst for water, but of hearing the words of the "
     "LORD:"),
    ("n4", NARRATOR, "-22%", "-4Hz",
     "And when people feel that kind of hunger, they do what hungry people do. They go "
     "looking. They search high and low, near and far, hoping to stumble on the thing "
     "that will finally fill them."),
    ("n5", NARRATOR, "-22%", "-4Hz",
     "Amos saw them wandering from one end of the world to the other, running here and "
     "there, chasing every rumor of where the word of God might still be found."),
    ("n6", NARRATOR, "-22%", "-4Hz",
     "But in a famine of the word, the seeking alone does not satisfy. They looked, and "
     "looked, and could not lay hold of it — because what they were hungry for had grown "
     "rare in the land."),
    # kv12 — SACRED SILENCE 2
    ("kv12", SCRIPTURE, "-26%", "-6Hz",
     "And they shall wander from sea to sea, and from the north even to the east, they "
     "shall run to and fro to seek the word of the LORD, and shall not find it."),
    ("n7", NARRATOR, "-22%", "-4Hz",
     "But think about what that hunger really means. You do not ache for what was never "
     "real. The very fact that a soul can starve for God's word is proof that such a "
     "word exists, and that it was always meant to be found."),
    ("n8", NARRATOR, "-24%", "-4Hz",
     "So a famine is never the end of the story; it is the ache that comes right before "
     "the harvest. God does not leave his people hungry forever. So the only question is "
     "a hopeful one. When the word is set before you again, will you sit down and eat?"),
    ("card", NARRATOR, "-26%", "-4Hz",
     "Amos foretold a famine — not of bread, but of hearing the word of God. Yet a "
     "hunger like that is a promise: you only starve for what is real. When the word is "
     "offered again, will you feed on it?"),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        await save_narration(text, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
