#!/usr/bin/env python3
"""Generate narration audio for Story Video #48 — New Wine, Old Bottles
(Mark 2:18-22).

Narrator: en-US-AndrewNeural — plain American, never a Multilingual model.
Jesus voice: en-US-ChristopherNeural — American, never British.

Jesus speaks ONLY exact KJV. Four lines — his whole answer:
  jv19 = Mark 2:19   the bridegroom is present (sacred silence 1 — the joy)
  jv20 = Mark 2:20   the days will come when the bridegroom is taken away
  jv21 = Mark 2:21   new cloth on an old garment, the rent made worse
  jv22 = Mark 2:22   new wine bursts old bottles (sacred silence 2 — the payoff)

The two sacred silences land on the two GOOD-NEWS beats: jv19 (the Bridegroom is
HERE — the joy) and jv22 (new wine must be put into new bottles — the Seed).

WHY-LAW: the misread is "Jesus is soft on devotion." The point is the opposite —
the joy he brings is a NEW thing, too alive to be crammed back into the old rigid
forms. STUDY GEMS: fasting was the sign you were serious with God (n2); a wedding
guest does not go hungry while the groom is in the room (n3); wine was kept in
whole-animal-skin bottles, a fresh skin stretches but an old one has gone brittle,
and new wine still ferments and needs room to swell (n6).

TRANSLATION LAW: after each KJV line the narrator gives plain meaning and never
re-quotes it. n4 says "the groom will be gone" not "taken away"; n7 says "fresh
wine belongs in a fresh skin" not "must be put into new bottles".

MILK FRAMING: an invitation, never a threat. Nobody is harmed — it is only the old
leather bottle that fails. Ends on the open hand: God is offering something new and
full of joy, if you make room for it.

NUMBER-STRESS LAW: no sentence opens with a bare number.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"
JESUS = "en-US-ChristopherNeural"

SEGMENTS = [
    # (filename, voice, rate, pitch, text) — text is BOTH spoken and captioned.
    # --- s1: the question ---
    ("n1", NARRATOR, "-20%", "-4Hz",
     "Some very sincere, very religious men came to him with an honest question. "
     "John's followers fasted. The Pharisees fasted. So why, they asked, did his own "
     "disciples not fast like everyone else?"),
    # --- s2: what fasting meant ---
    ("n2", NARRATOR, "-22%", "-4Hz",
     "Fasting was how you showed God you were serious. These were good men, going "
     "hungry to draw close to him. And here were his disciples, not fasting at all. It "
     "looked careless. His answer was not what they expected."),
    # --- s3: jv19 — the bridegroom is present. SACRED SILENCE 1. ---
    ("jv19", JESUS, "-26%", "-6Hz",
     "Can the children of the bridechamber fast, while the bridegroom is with them? "
     "as long as they have the bridegroom with them, they cannot fast."),
    ("n3", NARRATOR, "-22%", "-4Hz",
     "He points them at a wedding. Nobody starves themselves at a wedding feast. While "
     "the groom is right there in the room, the only fitting thing to do is celebrate. "
     "And that was the quiet, staggering claim underneath it. The groom is here. He was "
     "talking about himself."),
    # --- s4: jv20 — the bridegroom taken away ---
    ("jv20", JESUS, "-26%", "-6Hz",
     "But the days will come, when the bridegroom shall be taken away from them, and "
     "then shall they fast in those days."),
    ("n4", NARRATOR, "-22%", "-4Hz",
     "Then he says something that must have landed strangely. A day is coming when the "
     "groom will be gone. He is looking straight past this moment to the cross. There "
     "will be a time to mourn, and a time to fast. But not now, not while he is standing "
     "in front of them."),
    # --- s5: the old garment ---
    ("n5", NARRATOR, "-22%", "-4Hz",
     "Then he gives them two small pictures from everyday life. The first one is about "
     "mending clothes. You do not sew a stiff, brand-new scrap onto a soft, worn-out old "
     "coat."),
    # --- s6: jv21 — the rent made worse ---
    ("jv21", JESUS, "-26%", "-6Hz",
     "No man also seweth a piece of new cloth on an old garment: else the new piece that "
     "filled it up taketh away from the old, and the rent is made worse."),
    # --- s7: the wineskin gem ---
    ("n6", NARRATOR, "-22%", "-4Hz",
     "The second picture is about wine. In that world you kept your wine in bottles made "
     "of leather, of whole animal skins. A fresh skin was soft and it could stretch. But "
     "an old skin had gone hard and brittle, and new wine, still working and giving off "
     "gas, needs room to swell."),
    # --- s8: jv22 — new wine bursts old bottles. SACRED SILENCE 2. ---
    ("jv22", JESUS, "-26%", "-6Hz",
     "And no man putteth new wine into old bottles: else the new wine doth burst the "
     "bottles, and the wine is spilled, and the bottles will be marred: but new wine "
     "must be put into new bottles."),
    # --- s9: resolution / the WHY ---
    ("n7", NARRATOR, "-22%", "-4Hz",
     "So you never pour fresh, living wine into a stiff old skin. The wine keeps growing, "
     "the hard leather cannot give, and the whole thing tears open and everything is "
     "lost. Fresh wine belongs in a fresh skin, one that can stretch along with it. That "
     "is what he is telling them. God is doing something so new and so alive that the old "
     "rigid forms simply cannot hold it. Not a patch on the old religion. A whole new "
     "thing."),
    # --- s10: frame / invitation ---
    ("n8", NARRATOR, "-24%", "-4Hz",
     "That is the good news hiding inside a question about fasting. God was not tinkering "
     "with the old rules. He was pouring out something brand new, full of life and joy, "
     "and he was standing right there to give it. The only thing he asks is a heart soft "
     "enough to hold it."),
    # --- closing card, read gently (Readable-Card Law) ---
    ("card", NARRATOR, "-26%", "-4Hz",
     "They came asking about a rule, and he answered with a wedding. God is doing a new "
     "thing, and it is full of joy. Where is he offering you something new, if you will "
     "only make room for it?"),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
