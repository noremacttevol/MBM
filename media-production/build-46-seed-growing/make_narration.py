#!/usr/bin/env python3
"""Narration for build-46-seed-growing — Mark 4.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

STAYED RED, ALL FOUR, UNCHANGED. Mark 4:26-29 is a parable spoken by Jesus in
the flesh and a red-letter KJV inks the whole of it, including the farmer's
doings inside the story. jv26 (4:26), jv27 (4:27), jv28 (4:28), jv29 (4:29) are
each verbatim and each already stripped of Mark's framing -- 4:26 opens "And he
said, So is the kingdom of God..." and the segment starts at "So is the kingdom
of God", so no split was needed anywhere in this build.

NO SPLITS. Not one segment welded narration to speech.

NO GREEN, NO BLUE. Nobody but Jesus speaks in Mark 4:26-29. The farmer never
opens his mouth -- he sleeps, rises, and puts in the sickle. There is no second
voice to lift.

WOMEN: Mark 4:26-29 records no woman speaking. Nothing added; nothing invented.

RETELLING RULE ALREADY SATISFIED. Every red beat was already followed by the
storyteller saying it again in plain English -- jv26 by n2, jv27 by n3, jv28 by
n6, jv29 by n9. Nothing needed to be inserted. This build was already built the
way the law asks for; the only change is that the colour and the voice now come
from one declaration instead of two.

WHY-LAW: the growing was never his job. Milk -- you plant, God grows it, and you
are allowed to sleep tonight.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "This might be the most restful thing he ever said. It is about a farmer, and a field, and the one part of the whole process that is never, not for one second, up to you."),
    # Mark 4:26
    ("jv26", JESUS, "So is the kingdom of God, as if a man should cast seed into the ground;"),
    ("n2", NARRATOR, "A man walks out and scatters seed across his field. That is his job. He does it well, he does it by hand, and then, and this is the part that matters, he goes home."),
    # Mark 4:27
    ("jv27", JESUS, "And should sleep, and rise night and day, and the seed should spring and grow up, he knoweth not how."),
    ("n3", NARRATOR, "And then he lives his life. He sleeps at night and gets up in the morning. Ordinary weeks go by. And the whole time, down in the dark soil where he cannot see and cannot help, the seed is doing the one thing he could never make it do. It is growing."),
    ("n4", NARRATOR, "Notice what he is not doing. He is not out there at midnight pulling on the shoots to stretch them longer. He is not standing over the dirt, worried it forgot how. He planted. Now he trusts. The growing was never his job."),
    ("n5", NARRATOR, "And the gentlest words in the whole story are about that. He does not even grasp the miracle he is leaning on. He does not have to. It works whether he understands it or not."),
    # Mark 4:28
    ("jv28", JESUS, "For the earth bringeth forth fruit of herself; first the blade, then the ear, after that the full corn in the ear."),
    ("n6", NARRATOR, "And it comes in its own order, on its own clock. The first tender shoots. Then the heads of grain. Then the whole field heavy and golden and ready, all in its time, none of it rushed, none of it forced."),
    ("n7", NARRATOR, "You cannot hurry a field. You cannot argue a seed into sprouting faster. Everything good that has ever grown in your life grew like this, quietly, underground, on a timetable you did not set."),
    ("n8", NARRATOR, "So if you planted something good and you still cannot see it, this is the story for you. Hidden is not the same as dead. Slow is not the same as stopped. Under the surface, where you cannot watch it, it is already on its way up."),
    # Mark 4:29
    ("jv29", JESUS, "But when the fruit is brought forth, immediately he putteth in the sickle, because the harvest is come."),
    ("n9", NARRATOR, "And then one morning it is ready, and the waiting is over, and there is nothing left to do but go out with joy and bring it in. The harvest comes. That was never the part in doubt."),
    ("n10", NARRATOR, "Here is the rest he is holding out to you. The kingdom of God is not a thing you have to force into the world by sheer effort. You do your small, faithful part. You plant. And God does the part you were never strong enough to do anyway. He makes it grow."),
    ("n11", NARRATOR, "So you can actually sleep tonight. The seed is not waiting on your worry. It is doing, down in the dark, exactly what he promised it would."),
    ("card", NARRATOR, "He told a whole crowd that the growing was never on their shoulders. That the harvest was already coming, whether they understood it or not. What could you finally set down, if you believed him?"),
]

# Homographs this build decides for itself (never auto-replaced globally).
SPOKEN = {}


async def main():
    os.makedirs("audio", exist_ok=True)
    for name, speaker, text in SEGMENTS:
        flagged = [w for w in audit(text) if w not in SPOKEN]
        if flagged:
            print(f"  ! {name}: undecided homograph(s) {flagged}")
        await save_speaker_narration(spoken_text(text, SPOKEN), speaker,
                                     f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3  [{speaker}]")


if __name__ == "__main__":
    asyncio.run(main())
