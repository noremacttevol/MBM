#!/usr/bin/env python3
"""Generate narration audio for Story Video #46 — The Seed Growing Secretly (Mark 4:26-29).

Narrator: en-US-AndrewNeural — plain American, never a Multilingual model.
Jesus voice: en-US-ChristopherNeural — American, never British.

Jesus speaks ONLY exact KJV. Four lines (the whole parable is his direct speech):
  jv26 = Mark 4:26   the kingdom is like a man who casts seed into the ground
  jv27 = Mark 4:27   he sleeps and rises, and it grows "he knoweth not how" — SILENCE 1
  jv28 = Mark 4:28   the earth of herself: blade, then ear, then full corn
  jv29 = Mark 4:29   the harvest is come; he putteth in the sickle — SILENCE 2

CAPTIONS ARE VERBATIM (Cameron, 2026-07-11): build.py imports these SEGMENTS and
word-wraps each text as the on-screen caption. KJV (Jesus) lines render cream italic.

CARE FLAGS: none — GREEN, plain milk. Nothing violent, nothing frightening. This is the
most RESTFUL parable in the set, and the whole job is to let it rest: the one part of the
process (the growing) is never on the farmer's shoulders. The comfort is Mark 4:27 (the
verse card): it grows "he knoweth not how." You plant; God gives the increase.

MILK / WHY-LAW: the misread is that the kingdom (and your own growth) has to be forced into
the world by effort and worry. The point is the opposite: hidden is not dead, slow is not
stopped, and the harvest always comes. The closing card is an INVITATION to stop carrying
what was never yours to carry — never a fear-question.

TRANSLATION LAW: after every KJV line the narrator gives only the plain modern meaning and
never re-quotes the KJV wording — n5 says "he does not even grasp the miracle" instead of
echoing "he knoweth not how", n6 says "shoots / heads of grain / heavy and golden" instead
of "blade / ear / full corn".
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text) — text is BOTH spoken and captioned.
    # --- s1: the frame — the most restful thing he said ---
    ("n1", NARRATOR, "-20%", "-4Hz",
     "This might be the most restful thing he ever said. It is about a farmer, and "
     "a field, and the one part of the whole process that is never, not for one "
     "second, up to you."),
    # --- s2: v26 — a man casts seed ---
    ("jv26", JESUS, "-26%", "-6Hz",
     "So is the kingdom of God, as if a man should cast seed into the ground;"),
    ("n2", NARRATOR, "-22%", "-4Hz",
     "A man walks out and scatters seed across his field. That is his job. He does "
     "it well, he does it by hand, and then, and this is the part that matters, he "
     "goes home."),
    # --- s3: v27 — he sleeps and rises; it grows. SILENCE 1. ---
    ("jv27", JESUS, "-28%", "-6Hz",
     "And should sleep, and rise night and day, and the seed should spring and grow "
     "up, he knoweth not how."),
    ("n3", NARRATOR, "-22%", "-4Hz",
     "And then he lives his life. He sleeps at night and gets up in the morning. "
     "Ordinary weeks go by. And the whole time, down in the dark soil where he "
     "cannot see and cannot help, the seed is doing the one thing he could never "
     "make it do. It is growing."),
    # --- s4: what he is NOT doing ---
    ("n4", NARRATOR, "-22%", "-4Hz",
     "Notice what he is not doing. He is not out there at midnight pulling on the "
     "shoots to stretch them longer. He is not standing over the dirt, worried it "
     "forgot how. He planted. Now he trusts. The growing was never his job."),
    # --- s5: the gentlest words in the story ---
    ("n5", NARRATOR, "-22%", "-4Hz",
     "And the gentlest words in the whole story are about that. He does not even "
     "grasp the miracle he is leaning on. He does not have to. It works whether he "
     "understands it or not."),
    # --- s6: v28 — the earth of herself: blade, ear, full corn ---
    ("jv28", JESUS, "-26%", "-6Hz",
     "For the earth bringeth forth fruit of herself; first the blade, then the ear, "
     "after that the full corn in the ear."),
    ("n6", NARRATOR, "-22%", "-4Hz",
     "And it comes in its own order, on its own clock. The first tender shoots. "
     "Then the heads of grain. Then the whole field heavy and golden and ready, all "
     "in its time, none of it rushed, none of it forced."),
    # --- s7: you cannot hurry a field ---
    ("n7", NARRATOR, "-22%", "-4Hz",
     "You cannot hurry a field. You cannot argue a seed into sprouting faster. "
     "Everything good that has ever grown in your life grew like this, quietly, "
     "underground, on a timetable you did not set."),
    # --- s8: hidden is not dead ---
    ("n8", NARRATOR, "-22%", "-4Hz",
     "So if you planted something good and you still cannot see it, this is the "
     "story for you. Hidden is not the same as dead. Slow is not the same as "
     "stopped. Under the surface, where you cannot watch it, it is already on its "
     "way up."),
    # --- s9: v29 — the harvest is come. SILENCE 2. ---
    ("jv29", JESUS, "-26%", "-6Hz",
     "But when the fruit is brought forth, immediately he putteth in the sickle, "
     "because the harvest is come."),
    ("n9", NARRATOR, "-22%", "-4Hz",
     "And then one morning it is ready, and the waiting is over, and there is "
     "nothing left to do but go out with joy and bring it in. The harvest comes. "
     "That was never the part in doubt."),
    # --- s10: the rest he is offering ---
    ("n10", NARRATOR, "-22%", "-4Hz",
     "Here is the rest he is holding out to you. The kingdom of God is not a thing "
     "you have to force into the world by sheer effort. You do your small, faithful "
     "part. You plant. And God does the part you were never strong enough to do "
     "anyway. He makes it grow."),
    # --- s11: you can sleep tonight — the invitation ---
    ("n11", NARRATOR, "-24%", "-4Hz",
     "So you can actually sleep tonight. The seed is not waiting on your worry. It "
     "is doing, down in the dark, exactly what he promised it would."),
    # --- closing card, read gently (Readable-Card Law). An INVITATION. ---
    ("card", NARRATOR, "-26%", "-4Hz",
     "He told a whole crowd that the growing was never on their shoulders. That the "
     "harvest was already coming, whether they understood it or not. What could you "
     "finally set down, if you believed him?"),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
