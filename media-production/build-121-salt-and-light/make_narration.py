#!/usr/bin/env python3
"""Generate narration audio for Story Video #121 — Salt and Light
(Matthew 5:13-16, the Sermon on the Mount).

Narrator: en-US-AndrewNeural — plain American, never a Multilingual model.
Jesus voice: en-US-ChristopherNeural — American, never British.

Jesus speaks ONLY exact KJV. Four lines:
  jv13 = Matthew 5:13  the salt of the earth
  jv14 = Matthew 5:14  the light of the world / a city on a hill   (SACRED SILENCE 1)
  jv15 = Matthew 5:15  the candle on a candlestick, not under a bushel
  jv16 = Matthew 5:16  let your light so shine ... glorify your Father  (SILENCE 2)

The two sacred silences land on the two identity/charge beats: jv14 ("ye are the light
of the world") and jv16 ("let your light so shine") — the heart of the encouragement.

CARE FLAGS: none — GREEN, plain milk. This is pure encouragement: YOU are salt and
light, kept bright you are what the world needs. The one warning (salt losing its
savour) is gentle and about usefulness, never fear.

TRANSLATION LAW: after each KJV line the narrator gives the plain meaning and never
re-quotes it (n2 says "salt was precious," not "salt of the earth"; n5 says "hides it
under a basket," not "under a bushel"; n8 says "their eyes lift to God," not "glorify
your Father").

MILK FRAMING: the goodness of Jesus telling ordinary people who they already are. The
closing card is an invitation to shine, never a threat.

NUMBER-STRESS LAW: no sentence opens with a bare number.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"
JESUS = "en-US-ChristopherNeural"

SEGMENTS = [
    # (filename, voice, rate, pitch, text) — text is BOTH spoken and captioned.
    # --- s1: the teaching on the hillside ---
    ("n1", NARRATOR, "-22%", "-4Hz",
     "Jesus sat on a green hillside above the Sea of Galilee, an ordinary crowd gathered "
     "on the grass around him — fishermen, mothers, farmers, children. And to these "
     "plain, unremarkable people he said something astonishing about who they were. He "
     "began with salt."),
    # --- s2: jv13 — the salt of the earth ---
    ("jv13", JESUS, "-26%", "-6Hz",
     "Ye are the salt of the earth: but if the salt have lost his savour, wherewith shall "
     "it be salted? it is thenceforth good for nothing, but to be cast out, and to be "
     "trodden under foot of men."),
    ("n2", NARRATOR, "-22%", "-4Hz",
     "In that world salt was precious. It kept food from spoiling and it made plain "
     "things taste good. That, he told them, is what you are — you keep the world from "
     "going bad, and you bring out the good in it. You matter that much."),
    # --- s3: salt trodden ---
    ("n3", NARRATOR, "-22%", "-4Hz",
     "But salt has one job, and if it goes flat and loses its flavour it is no use to "
     "anyone — it just gets swept out and walked over. He was not threatening them; he "
     "was telling them not to waste what they were. Stay salty. Stay yourselves."),
    # --- s4: jv14 — the light of the world. SACRED SILENCE 1 ---
    ("jv14", JESUS, "-26%", "-6Hz",
     "Ye are the light of the world. A city that is set on an hill cannot be hid."),
    ("n4", NARRATOR, "-22%", "-4Hz",
     "Then he pointed them to light. A town built up on a hilltop, its lamps lit at dusk, "
     "can be seen for miles — there is no hiding it. That, he said, is you: not something "
     "the world should have to squint to find, but a light set up where everyone can "
     "see."),
    # --- s6: jv15 — the candle on a candlestick ---
    ("jv15", JESUS, "-26%", "-6Hz",
     "Neither do men light a candle, and put it under a bushel, but on a candlestick; and "
     "it giveth light unto all that are in the house."),
    ("n5", NARRATOR, "-22%", "-4Hz",
     "Nobody lights a lamp and then hides it under a basket. That would be pointless — "
     "smothering the very thing they lit it for."),
    # --- s7: on the stand, giving light to all ---
    ("n6", NARRATOR, "-22%", "-4Hz",
     "You set it up high, on a stand, so its light reaches into every corner and everyone "
     "in the house can see. Your goodness was never meant to be hidden away. It was meant "
     "to give light to the people around you."),
    # --- s8: jv16 — let your light so shine. SACRED SILENCE 2 ---
    ("jv16", JESUS, "-26%", "-6Hz",
     "Let your light so shine before men, that they may see your good works, and glorify "
     "your Father which is in heaven."),
    ("n7", NARRATOR, "-22%", "-4Hz",
     "So let it shine, he said. Live openly good — kind, honest, generous — right out "
     "where people can see it."),
    # --- s9: glorify your Father ---
    ("n8", NARRATOR, "-22%", "-4Hz",
     "But notice the reason. Not so they will admire you. So that when they see the good "
     "you do, their eyes will lift past you to God, and they will love him for it. Your "
     "light is not about you at all. It points home to your Father."),
    # --- s10: go and be salt and light ---
    ("n9", NARRATOR, "-22%", "-4Hz",
     "That is the whole charge, and it is a gentle one. You do not have to become "
     "something you are not. You already are salt; you already are light. Just don't lose "
     "your savour, and don't hide your lamp. Go out, stay bright, and be exactly what the "
     "world needs."),
    # --- closing card, read gently (Readable-Card Law) ---
    ("card", NARRATOR, "-25%", "-4Hz",
     "You are the salt of the earth. You are the light of the world. Not someday, if you "
     "are good enough — right now, as you are. Where could your light give someone else a "
     "little more of God today?"),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        await save_narration(text, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
