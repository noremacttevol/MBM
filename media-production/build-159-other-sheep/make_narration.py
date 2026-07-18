#!/usr/bin/env python3
"""Generate narration audio for Story Video #159 — "Other sheep I have" (John 10:14,16).
MEMBER shelf verse-video. → Gospel Library topic: Book of Mormon.

Narrator: en-US-AndrewNeural — plain American, modern paraphrase, never a
Multilingual model, never echoes the KJV wording.
Scripture voice: en-US-ChristopherNeural — these are the LORD'S OWN WORDS (red-letter,
John 10), spoken in the reverent scripture voice, EXACT KJV only.

Jesus IS depicted in this video (the Good Shepherd) — his face shown, locked to the
JESUS-MASTER-REF master face; only Jesus wears cream.

KJV lines (exact, red-letter):
  kv14 = John 10:14  I am the good shepherd, and know my sheep (SACRED SILENCE 1)
  kv16 = John 10:16  other sheep I have... one fold, one shepherd (NAMED VERSE — SACRED SILENCE 2)

WHY-LAW: belonging — the Shepherd has sheep the crowd never counted, and he will gather
them all. STUDY GEMS: he KNOWS his own, each by name and voice (n2); there are others in
far places, not of this fold (n4); they too shall hear his voice (n5); one fold, one
shepherd — none forgotten (n6); if you ever felt an outsider, he counted you in (n7).

TRANSLATION LAW: the narrator never re-quotes a KJV line. n1 says "I am the good shepherd"
ONLY as the KJV line kv14; the paraphrase around it uses other words.

MILK FRAMING: an invitation. The closing card ends on an open question and a one-line
pointer to the Gospel Library topic (Book of Mormon). No shame, no fear.

NUMBER-STRESS LAW: no sentence opens with a bare number.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"
SCRIPTURE = "en-US-ChristopherNeural"

SEGMENTS = [
    ("n1", NARRATOR, "-20%", "-4Hz",
     "On a hillside, surrounded by his listeners, Jesus reached for the most familiar "
     "picture they had — a shepherd and his flock. He was the shepherd, he told them, "
     "the good one, and the sheep were his very own."),
    ("n2", NARRATOR, "-22%", "-4Hz",
     "It is a tender thing to be known like that. Not counted as part of a crowd, but "
     "known — each one, by name, by voice, by the particular way it strays and the "
     "particular way it finds its way home."),
    ("n3", NARRATOR, "-22%", "-4Hz",
     "And the knowing runs both ways. His own know him too — the sound of his voice, the "
     "shape of his care — the way sheep will lift their heads at one familiar step and "
     "follow no stranger."),
    # kv14 — SACRED SILENCE 1
    ("kv14", SCRIPTURE, "-26%", "-6Hz",
     "I am the good shepherd, and know my sheep, and am known of mine."),
    ("n4", NARRATOR, "-22%", "-4Hz",
     "But then Jesus said something that must have stopped them cold. This flock, right "
     "here in front of me, he told them — you are not all the sheep I have. There are "
     "others, in other places, not of this fold."),
    ("n5", NARRATOR, "-22%", "-4Hz",
     "People they had never met, in lands they had never seen, who also belonged to him "
     "and were waiting to be brought in. And about them he made a quiet, sweeping "
     "promise: they too shall hear my voice."),
    ("n6", NARRATOR, "-22%", "-4Hz",
     "Not two rival flocks. Not one favoured and one forgotten. In the end, one fold and "
     "one shepherd — every scattered sheep gathered home under the same gentle hand."),
    # kv16 — NAMED VERSE, SACRED SILENCE 2
    ("kv16", SCRIPTURE, "-26%", "-6Hz",
     "And other sheep I have, which are not of this fold: them also I must bring, and "
     "they shall hear my voice; and there shall be one fold, and one shepherd."),
    ("n7", NARRATOR, "-22%", "-4Hz",
     "So if you have ever felt like an outsider — like one of the other sheep, far from "
     "where the story seemed to be happening — hear this. He counted you in from the "
     "beginning. He always meant to come for you too."),
    ("n8", NARRATOR, "-24%", "-4Hz",
     "That is the wide, patient heart of the Good Shepherd. He has sheep the crowd never "
     "counted, and he will not rest until they hear him and come. So the only question is "
     "a gentle one. When you hear his voice, will you know it, and follow?"),
    ("card", NARRATOR, "-26%", "-4Hz",
     "Jesus said he has other sheep, not of this fold — and they too will hear his voice, "
     "until there is one fold and one shepherd. Wherever you are, he counted you in. When "
     "you hear his voice, will you follow?"),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        await save_narration(text, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
