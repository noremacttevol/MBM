#!/usr/bin/env python3
"""Generate narration audio for Story Video #155 — "A falling away first"
(2 Thessalonians 2:1-3). MEMBER shelf verse-video. → Gospel Library topic: Apostasy.

Narrator: en-US-AndrewNeural — plain American, modern paraphrase, never a
Multilingual model, never echoes the KJV wording.
Scripture voice: en-US-ChristopherNeural — speaks the KJV text EXACTLY.
(Paul's epistle; the scripture voice carries the verse. Christ is NOT depicted;
the falling away is shown only as fading light — never a villain, never a specific
church, never anyone shamed.)

KJV lines (exact):
  kv2 = 2 Thes 2:2  be not soon shaken in mind (SACRED SILENCE 1)
  kv3 = 2 Thes 2:3  a falling away first (NAMED VERSE — SACRED SILENCE 2)

WHY-LAW: dread turned to hope — a falling away was FORETOLD, so it never meant God
failed; and what is foretold as lost can be restored. STUDY GEMS: don't be stampeded by
rumor (n2-n3); the dimming was predicted, not a surprise (n6); you don't warn of a night
unless a morning follows (n7); the returning was always part of the plan (n8).

TRANSLATION LAW: the narrator never re-quotes a KJV line. n2 says "do not let yourselves
be shaken or alarmed," delivered as paraphrase; the exact KJV lands only in kv2/kv3.

MILK FRAMING: an invitation. The closing card ends on an open question and a one-line
pointer to the Gospel Library topic (Apostasy). No shame, no fear, no accusing any group.
CHRIST IS NEVER DEPICTED; the apostasy is shown only as gently fading light.

NUMBER-STRESS LAW: no sentence opens with a bare number.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"
SCRIPTURE = "en-US-ChristopherNeural"

SEGMENTS = [
    ("n1", NARRATOR, "-20%", "-4Hz",
     "The young believers in Thessalonica were rattled. Rumors were flying that the "
     "great Day of the Lord had already come, and they were frightened and confused. So "
     "Paul sat down to write them a steadying letter."),
    ("n2", NARRATOR, "-22%", "-4Hz",
     "His first word to them was calm. Do not let yourselves be shaken or alarmed, he "
     "said, by every excited rumor and secondhand report, or stampeded into fear by "
     "things you cannot even trace to their source."),
    ("n3", NARRATOR, "-22%", "-4Hz",
     "He wanted them anchored, not tossed around by the loudest voice in the room. "
     "Feelings and hearsay are not the same as truth, and a frightened crowd is rarely "
     "a wise one."),
    # kv2 — SACRED SILENCE 1
    ("kv2", SCRIPTURE, "-26%", "-6Hz",
     "That ye be not soon shaken in mind, or be troubled, neither by spirit, nor by "
     "word, nor by letter as from us, as that the day of Christ is at hand."),
    ("n4", NARRATOR, "-22%", "-4Hz",
     "Then Paul told them plainly what to watch for. That day, he said, would not "
     "arrive until something else happened first — and it was sobering. Before the end, "
     "there would come a falling away."),
    ("n5", NARRATOR, "-22%", "-4Hz",
     "A drifting from the truth. A dimming of the light that had been lit. Many hearts, "
     "over time, turning away from what the apostles had actually given them, until much "
     "of it was lost from view."),
    ("n6", NARRATOR, "-22%", "-4Hz",
     "But here is the part that turns dread into hope. Paul is telling them ahead of "
     "time. A falling away would not mean God had failed, or his plan had broken. It "
     "would mean the very thing he predicted was coming to pass."),
    # kv3 — NAMED VERSE, SACRED SILENCE 2
    ("kv3", SCRIPTURE, "-26%", "-6Hz",
     "Let no man deceive you by any means: for that day shall not come, except there "
     "come a falling away first, and that man of sin be revealed, the son of "
     "perdition;"),
    ("n7", NARRATOR, "-22%", "-4Hz",
     "And you do not warn people about a night unless a morning is meant to follow. A "
     "falling away only makes sense if there is something to fall back to — a truth that "
     "can be restored, brought back, and lit again."),
    ("n8", NARRATOR, "-24%", "-4Hz",
     "So this hard little verse is really a quiet promise. The dimming was foretold, "
     "which means the returning was always part of the plan. So the only question is a "
     "hopeful one. When the light is offered again, will you know it, and take hold?"),
    ("card", NARRATOR, "-26%", "-4Hz",
     "Paul warned that a falling away would come first — not because God failed, but "
     "because he foretold it. And what is foretold can be restored. When the light "
     "returns, will you take hold of it?"),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        await save_narration(text, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
