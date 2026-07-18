#!/usr/bin/env python3
"""Generate narration audio for Story Video #164 — The Rainbow Covenant
(Genesis 8:20-9:17).

Narrator: en-US-AndrewNeural — plain American, never a Multilingual model.
Divine voice: en-US-ChristopherNeural — the same voice that carries Jesus's
exact KJV lines project-wide; here it speaks GOD's words, exact KJV only.
God is never depicted in any frame (voice only — see PROMPTS.md).

God speaks ONLY exact KJV. Five lines:
  jv22 = Gen 8:22   seedtime and harvest shall not cease
  jv9  = Gen 9:9    I establish my covenant with you
  jv11 = Gen 9:11   neither shall there any more be a flood
  jv13 = Gen 9:13   I do set my bow in the cloud (verse card — SACRED SILENCE 1)
  jv16 = Gen 9:16   I will look upon it, that I may remember (SACRED SILENCE 2)

The two sacred silences land on the two COVENANT-SIGN beats: jv13 (the bow is
hung in the sky — the verse card) and jv16 (God keeps the reminder in his own
sight — the Seed).

WHY-LAW: the misread is "the rainbow is a nice decoration after a scary story."
The point: God binds HIMSELF, one-way — Noah is not asked to earn or promise
anything — and the sign is aimed at GOD ("I will look upon it, that I may
remember"). STUDY GEMS: to flood survivors every dark cloud meant terror, and
the covenant answers that fear (n5); the Hebrew word is simply BOW — a war-bow
hung up in the clouds, the warrior retiring his weapon (n8); the covenant
includes every living creature that came off the ark (n6).

TRANSLATION LAW: after each KJV line the narrator gives plain meaning and never
re-quotes it. n9 says "the string God tied around his own finger," never "I
will look upon it"; n7 says "never again — unconditional," never "cut off any
more by the waters."

MILK FRAMING: the flood is never shown; every frame is AFTER — a washed new
world. No fear-question: the card is an invitation about a promise-keeping God.

NUMBER-STRESS LAW: no sentence opens with a bare number.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"
GOD = "en-US-ChristopherNeural"

SEGMENTS = [
    # (filename, voice, rate, pitch, text) — text is BOTH spoken and captioned.
    # --- s1: the ark at rest ---
    ("n1", NARRATOR, "-20%", "-4Hz",
     "The rain had stopped. For the better part of a year, one family and a "
     "great wooden boat full of animals had ridden out the end of the world "
     "they knew. Then one morning the ark sat still on a mountainside, and "
     "the earth lay quiet and washed and new."),
    # --- s2: first steps ---
    ("n2", NARRATOR, "-22%", "-4Hz",
     "Noah and his family stepped out onto wet grass under an open sky. "
     "There were eight of them, and everything they had ever known was gone. "
     "The whole human story was starting over, and one heavy question hung "
     "over it. Could anyone trust the sky again?"),
    # --- s3: the altar ---
    ("n3", NARRATOR, "-22%", "-4Hz",
     "Here is the first thing Noah built in the new world. Not a house. Not "
     "a fence. He gathered stones and built an altar, and he gave thanks. "
     "And God answered that small smoking altar with a promise about the "
     "whole future."),
    # --- s4: jv22 — seedtime and harvest ---
    ("jv22", GOD, "-26%", "-6Hz",
     "While the earth remaineth, seedtime and harvest, and cold and heat, "
     "and summer and winter, and day and night shall not cease."),
    ("n4", NARRATOR, "-22%", "-4Hz",
     "Planting time and gathering time, winter and summer, morning and "
     "night. The world would keep its rhythm for as long as it stands. But "
     "God was not finished, because he knew something about these eight "
     "people. He knew what rain now meant to them."),
    # --- s5: the fear ---
    ("n5", NARRATOR, "-22%", "-4Hz",
     "Think about the first time clouds rolled in after the flood. For "
     "Noah's family, a dark sky was no longer just weather. It was the "
     "memory of everything they had lost. And God did not scold them for "
     "being afraid. He moved to meet the fear."),
    # --- s6: jv9 — the covenant ---
    ("jv9", GOD, "-26%", "-6Hz",
     "And I, behold, I establish my covenant with you, and with your seed "
     "after you."),
    ("n6", NARRATOR, "-22%", "-4Hz",
     "A covenant is the Bible's most serious word for a promise, one that "
     "binds the person who makes it. And notice who is doing the binding "
     "here. Noah is not asked to promise anything, sign anything, or earn "
     "anything. God binds himself, one way, for free. To Noah, to his "
     "children, and to every living creature that walked off that boat."),
    # --- s7: jv11 — never again ---
    ("jv11", GOD, "-26%", "-6Hz",
     "And I will establish my covenant with you; neither shall all flesh be "
     "cut off any more by the waters of a flood; neither shall there any "
     "more be a flood to destroy the earth."),
    ("n7", NARRATOR, "-22%", "-4Hz",
     "Never again. That is the whole promise, with no conditions attached "
     "and no expiration date. And then God does something wonderfully "
     "tender. He gives the promise a sign you can see with your eyes."),
    # --- s8: jv13 — the bow in the cloud. SACRED SILENCE 1 — verse card. ---
    ("jv13", GOD, "-26%", "-6Hz",
     "I do set my bow in the cloud, and it shall be for a token of a "
     "covenant between me and the earth."),
    # --- s9: the war-bow gem ---
    ("n8", NARRATOR, "-22%", "-4Hz",
     "The word there is simply bow, and it is the same word the Bible uses "
     "for a battle bow, a weapon of war. God hangs a bow in the clouds, "
     "unstrung, aimed away from the earth. It is the picture of a warrior "
     "hanging up his weapon on the wall. The storm between heaven and earth "
     "is over."),
    # --- s10: jv16 — I will look upon it. SACRED SILENCE 2 — the Seed. ---
    ("jv16", GOD, "-26%", "-6Hz",
     "And the bow shall be in the cloud; and I will look upon it, that I "
     "may remember the everlasting covenant between God and every living "
     "creature of all flesh that is upon the earth."),
    ("n9", NARRATOR, "-22%", "-4Hz",
     "Did you catch who the sign is for? God set the reminder where he "
     "would see it. The rainbow is the string God tied around his own "
     "finger. Before it ever comforts you, it is his own promise, kept "
     "deliberately in his own sight."),
    # --- s11: every rain since ---
    ("n10", NARRATOR, "-22%", "-4Hz",
     "And the promise held. Rain has come and gone for thousands of years "
     "since that mountainside, and when the shower passes, the same sign "
     "still climbs the sky. Children point at it. Nobody runs from it. That "
     "is what it feels like to live inside a promise God is keeping."),
    # --- s12: the God who binds himself ---
    ("n11", NARRATOR, "-24%", "-4Hz",
     "This is the God the whole story has been about. A God who knows "
     "exactly what frightens his people, and answers fear with beauty "
     "instead of blame. A God who binds himself with promises, and then "
     "keeps them. He has not changed."),
    # --- closing card, read gently (Readable-Card Law) ---
    ("card", NARRATOR, "-26%", "-4Hz",
     "After the flood, God made a one-way promise, and hung the reminder "
     "where he himself would see it. The next rainbow you see is God "
     "remembering. What might change for you, if you believed he keeps his "
     "promises?"),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        await save_narration(text, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
