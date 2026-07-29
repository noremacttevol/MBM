#!/usr/bin/env python3
"""Narration for build-155-falling-away — 2 Thessalonians 2.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

STAYED RED: nothing. This is an epistle — Paul writing to the saints at
Thessalonica — and a red-letter King James Bible prints no red anywhere in
2 Thessalonians 2. Both red beats move:
  kv2  2 Thessalonians 2:2  'That ye be not soon shaken in mind...'   RED -> SCRIPTURE
  kv3  2 Thessalonians 2:3  'Let no man deceive you by any means...'  RED -> SCRIPTURE
Painting Paul's warning red made the letter read as words of Christ in the
flesh, which is the exact error this pass exists to fix. Light blue is Paul.

NO SPLITS. Neither verse welds a narrator frame onto quoted speech — both are
the writer's own sentences start to finish, so each is one colour all the way
through.

BOTH VERSES VERIFIED VERBATIM against the King James text and left exactly as
the build already had them. Nothing lifted from paraphrase: n2 already retells
verse 2 and n4 through n7 already carry verse 3 into modern English, so the
retelling rule is satisfied without adding a beat.

WHY-LAW: milk. The falling away is told as a promise, not an accusation — a
night foretold means a morning was always planned. No church is named, nothing
is argued, and the closing question stays hopeful.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "The young believers in Thessalonica were rattled. Rumors were flying that the great Day of the Lord had already come, and they were frightened and confused. So Paul sat down to write them a steadying letter."),
    ("n2", NARRATOR, "His first word to them was calm. Do not let yourselves be shaken or alarmed, he said, by every excited rumor and secondhand report, or stampeded into fear by things you cannot even trace to their source."),
    ("n3", NARRATOR, "He wanted them anchored, not tossed around by the loudest voice in the room. Feelings and hearsay are not the same as truth, and a frightened crowd is rarely a wise one."),
    # 2 Thessalonians 2:2
    ("kv2", SCRIPTURE, "That ye be not soon shaken in mind, or be troubled, neither by spirit, nor by word, nor by letter as from us, as that the day of Christ is at hand."),
    ("n4", NARRATOR, "Then Paul told them plainly what to watch for. That day, he said, would not arrive until something else happened first — and it was sobering. Before the end, there would come a falling away."),
    ("n5", NARRATOR, "A drifting from the truth. A dimming of the light that had been lit. Many hearts, over time, turning away from what the apostles had actually given them, until much of it was lost from view."),
    ("n6", NARRATOR, "But here is the part that turns dread into hope. Paul is telling them ahead of time. A falling away would not mean God had failed, or his plan had broken. It would mean the very thing he predicted was coming to pass."),
    # 2 Thessalonians 2:3
    ("kv3", SCRIPTURE, "Let no man deceive you by any means: for that day shall not come, except there come a falling away first, and that man of sin be revealed, the son of perdition;"),
    ("n7", NARRATOR, "And you do not warn people about a night unless a morning is meant to follow. A falling away only makes sense if there is something to fall back to — a truth that can be restored, brought back, and lit again."),
    ("n8", NARRATOR, "So this hard little verse is really a quiet promise. The dimming was foretold, which means the returning was always part of the plan. So the only question is a hopeful one. When the light is offered again, will you know it, and take hold?"),
    ("card", NARRATOR, "Paul warned that a falling away would come first — not because God failed, but because he foretold it. And what is foretold can be restored. When the light returns, will you take hold of it?"),
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
