#!/usr/bin/env python3
"""Narration audio for Video #119 — The Fourth Man in the Fire (Daniel 3).

ALL NARRATOR voice (en-US-AndrewNeural). Daniel 3 has NO direct speech from God — the divine
is shown by the fourth figure's PRESENCE, not by words — so there is no scripture (Christopher)
voice and no cream-italic line in this video. Every KJV quotation here belongs to human
speakers (the three Hebrews; King Nebuchadnezzar) and is therefore in the narrator voice with
a WHITE caption, per the rule "others' KJV = narrator voice, white caption."

TWO MUSIC HUSHES (the bed dies to true silence on the two most sacred beats, though both are
narrator-voiced): n3 (the "but if not" confession) and n6 (the king counting a fourth figure,
Dan 3:25). No-Dead-Air holds — the narrator never stops, only the music does.

CARE FLAG R (fiery furnace): the fourth man IN the fire, NEVER burning flesh. Narration keeps
the focus on the three preserved and the presence with them; the men who carried them are not
dwelt on, no gore, no lingering on pain.

WHY-LAW: God did not spare these three the furnace — he met them inside it. The promise is
not "you will never face fire," but "you will never face it alone." Milk framing: whatever
furnace you are in, God comes into it with you and brings you through. An assurance, never a
threat.

HOMOGRAPH EAR-CHECK: 'bow' = bow-down (context clear); no high-risk homographs.
NUMBER-STRESS LAW obeyed ("ninety feet", "seven times hotter", "three", "four").
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"

SEGMENTS = [
    ("n1", NARRATOR, "-20%", "-4Hz",
     "A king built a golden statue ninety feet high and made one rule: when the music "
     "plays, everyone bows. And everyone did — a whole plain of people face-down in the "
     "dust. Everyone except three.", None),
    ("n2", NARRATOR, "-22%", "-4Hz",
     "Shadrach, Meshach, and Abednego would not bow to anything but God. So they were "
     "dragged before the furious king, who gave them one last chance: bow, or burn in the "
     "furnace.", None),
    # n3 — the "but if not" confession — MUSIC HUSH 1
    ("n3", NARRATOR, "-24%", "-4Hz",
     "Their answer is one of the bravest things anyone ever said. Our God whom we serve is "
     "able to deliver us, and he will deliver us out of your hand, O king. But if not — even "
     "if he does not — we still will not serve your gods.", None),
    ("n4", NARRATOR, "-22%", "-4Hz",
     "So the king had the furnace stoked seven times hotter than ever and had the three "
     "cast in, still bound hand and foot — a fire so fierce no one should have survived a "
     "single moment in it.", None),
    ("n5", NARRATOR, "-22%", "-4Hz",
     "And that is exactly when the impossible began. The ropes burned away, but the men did "
     "not. They stood up inside the fire, unharmed, not a single thread of their clothing "
     "even scorched.", None),
    # n6 — the king counts a fourth (Dan 3:25) — MUSIC HUSH 2
    ("n6", NARRATOR, "-24%", "-4Hz",
     "Then the king leapt up in astonishment. He had thrown in three men. Now he counted "
     "four. Lo, I see four men loose, walking in the midst of the fire, and they have no "
     "hurt; and the form of the fourth is like the Son of God.", None),
    ("n7", NARRATOR, "-22%", "-4Hz",
     "They were not alone in the fire. Whatever else that fourth figure was, it walked with "
     "them, and where it walked the flames could not touch them. God had not kept them out "
     "of the furnace — he met them inside it.", None),
    ("n8", NARRATOR, "-22%", "-4Hz",
     "The king called them out, and they walked from the heart of the fire onto solid "
     "ground, alive and whole, in front of everyone who had watched them go in.", None),
    ("n9", NARRATOR, "-22%", "-4Hz",
     "The officials crowded around and could not believe it. Not a hair of their heads was "
     "singed, their coats were not burned, and there was not even the smell of smoke on "
     "them. The fire had done nothing at all.", None),
    # n10 — Nebuchadnezzar blesses their God (Dan 3:28)
    ("n10", NARRATOR, "-24%", "-4Hz",
     "And the proud king who built that golden image blessed the God he had just watched "
     "rescue them. Blessed be the God of Shadrach, Meshach, and Abednego, who hath sent his "
     "angel, and delivered his servants that trusted in him.", None),
    ("card", NARRATOR, "-26%", "-4Hz",
     "God never promised these three that they would not face the fire. He promised "
     "something better — that he would be in it with them. What would change if you believed "
     "God meets you inside the hard thing, not only on the far side of it?", None),
]


async def main():
    for name, voice, rate, pitch, text, cap in SEGMENTS:
        tts = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")


if __name__ == "__main__":
    import os
    os.makedirs("audio", exist_ok=True)
    asyncio.run(main())
