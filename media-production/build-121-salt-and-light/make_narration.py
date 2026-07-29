#!/usr/bin/env python3
"""Narration for build-121-salt-and-light — Matthew 5.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

ALL FOUR RED BEATS STAY RED, UNCHANGED. jv13 (Matthew 5:13), jv14 (5:14),
jv15 (5:15) and jv16 (5:16) are Jesus speaking in the flesh on the mount. A
red-letter KJV prints all of it red. Nothing moved out of red.

NO MIXED SEGMENTS. Every red block here is pure speech — there is no 'and he
said unto them' welded onto any of them, so nothing needed splitting. Checked
each of the four against the KJV verse boundaries: jv13 is 5:13 entire, jv14
is 5:14 entire, jv15 is 5:15 entire, jv16 is 5:16 entire. All verbatim.

RETELLING COVERAGE: already complete, so nothing was added. n2 and n3 retell
jv13 (salt that is precious, salt that goes flat). n4 retells jv14 (the town
on the hilltop). n5 and n6 retell jv15 (the lamp under the basket, the lamp
on the stand). n7 and n8 retell jv16 (shine, and why). No red block anywhere
in this build is followed by another red block.

n1 already carries the framing in the narrator's own modern English — the
hillside, the crowd, 'he began with salt' — rather than quoting Matthew, so
it correctly stays narrator. It was left word for word as it was.

NOTHING LEFT AS PARAPHRASE FROM UNCERTAINTY. This build needed confirmation,
not correction.

WHY-LAW: he does not tell them to become salt and light. He tells them they
already are. Milk framing — the charge is gentle, and it is about not wasting
what you already have.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "Jesus sat on a green hillside above the Sea of Galilee, an ordinary crowd gathered on the grass around him — fishermen, mothers, farmers, children. And to these plain, unremarkable people he said something astonishing about who they were. He began with salt."),
    # Matthew 5:13
    ("jv13", JESUS, "Ye are the salt of the earth: but if the salt have lost his savour, wherewith shall it be salted? it is thenceforth good for nothing, but to be cast out, and to be trodden under foot of men."),
    ("n2", NARRATOR, "In that world salt was precious. It kept food from spoiling and it made plain things taste good. That, he told them, is what you are — you keep the world from going bad, and you bring out the good in it. You matter that much."),
    ("n3", NARRATOR, "But salt has one job, and if it goes flat and loses its flavour it is no use to anyone — it just gets swept out and walked over. He was not threatening them; he was telling them not to waste what they were. Stay salty. Stay yourselves."),
    # Matthew 5:14
    ("jv14", JESUS, "Ye are the light of the world. A city that is set on an hill cannot be hid."),
    ("n4", NARRATOR, "Then he pointed them to light. A town built up on a hilltop, its lamps lit at dusk, can be seen for miles — there is no hiding it. That, he said, is you: not something the world should have to squint to find, but a light set up where everyone can see."),
    # Matthew 5:15
    ("jv15", JESUS, "Neither do men light a candle, and put it under a bushel, but on a candlestick; and it giveth light unto all that are in the house."),
    ("n5", NARRATOR, "Nobody lights a lamp and then hides it under a basket. That would be pointless — smothering the very thing they lit it for."),
    ("n6", NARRATOR, "You set it up high, on a stand, so its light reaches into every corner and everyone in the house can see. Your goodness was never meant to be hidden away. It was meant to give light to the people around you."),
    # Matthew 5:16
    ("jv16", JESUS, "Let your light so shine before men, that they may see your good works, and glorify your Father which is in heaven."),
    ("n7", NARRATOR, "Live openly good — kind, honest, generous — right out where people can see it."),
    ("n8", NARRATOR, "But notice the reason. Not so they will admire you. So that when they see the good you do, their eyes will lift past you to God, and they will love him for it. Your light is not about you at all. It points home to your Father."),
    ("n9", NARRATOR, "That is the whole charge, and it is a gentle one. You do not have to become something you are not. You already are salt; you already are light. Just don't lose your savour, and don't hide your lamp. Go out, stay bright, and be exactly what the world needs."),
    ("card", NARRATOR, "You are the salt of the earth. You are the light of the world. Not someday, if you are good enough — right now, as you are. Where could your light give someone else a little more of God today?"),
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
