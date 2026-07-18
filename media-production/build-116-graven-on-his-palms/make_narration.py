#!/usr/bin/env python3
"""Narration audio for Video #116 — Graven on His Palms (Isaiah 49:14-16).

Narrator: en-US-AndrewNeural. God's voice: en-US-ChristopherNeural (exact KJV only).
Zion's complaint ('The LORD hath forsaken me') is voiced by the NARRATOR; God's own KJV
answers render cream-italic.

God's KJV lines (Christopher, cream italic):
  jv15  Isa 49:15  "Can a woman forget her sucking child... yea, they may forget, yet
                    will I not forget thee." — sacred silence 1
  jv16  Isa 49:16  "Behold, I have graven thee upon the palms of my hands; thy walls are
                    continually before me." — sacred silence 2

WHY-LAW: to a people convinced God had forgotten them, God answers with the most tender
image in scripture — a nursing mother, who could never forget her baby; and then he goes
further: even if she somehow could, I never will — I have carved you into my own hands, and
your walls are always before my eyes. Milk framing: if you feel forgotten, overlooked, left
behind — you are carried, permanently, on the hands of God. (For the reader who knows the
gospel, those graven hands quietly foreshadow the nail-marks — but the verse's comfort is
simply: you are not forgotten.) An invitation to be found, never a threat.

HOMOGRAPH EAR-CHECK: no high-risk homographs. NUMBER-STRESS LAW obeyed.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"
GOD = "en-US-ChristopherNeural"

SEGMENTS = [
    ("n1", NARRATOR, "-20%", "-4Hz",
     "There is a particular loneliness that comes from feeling forgotten. Not hated. Just "
     "overlooked. Slipped from someone's mind, as if you never really mattered enough to "
     "be remembered.", None),
    ("n2", NARRATOR, "-22%", "-4Hz",
     "That is exactly how God's people felt when they said it out loud: the Lord has "
     "forsaken me. My God has forgotten me. And God's answer to that fear is one of the "
     "most tender things he ever said.", None),
    ("n3", NARRATOR, "-22%", "-4Hz",
     "He points to the strongest, most instinctive love a human being knows — a mother "
     "with her newborn, unable to look away, unable to forget the child at her breast even "
     "for a moment.", None),
    # jv15 — can a woman forget — silence 1
    ("jv15", GOD, "-26%", "-6Hz",
     "Can a woman forget her sucking child, that she should not have compassion on the son "
     "of her womb? yea, they may forget, yet will I not forget thee.", None),
    ("n4", NARRATOR, "-22%", "-4Hz",
     "Even if a mother somehow could forget — I never will. And then he says something "
     "almost too intimate to imagine. He does not just keep you in mind. He has carved you "
     "into his own hands, where he cannot help but see you.", None),
    # jv16 — graven on the palms — silence 2
    ("jv16", GOD, "-26%", "-6Hz",
     "Behold, I have graven thee upon the palms of my hands; thy walls are continually "
     "before me.", None),
    ("n5", NARRATOR, "-22%", "-4Hz",
     "Graven — engraved, cut in deep, permanent. Not a note he might lose. You are written "
     "into the very hands of God, and everything about you is always right there in front "
     "of him. He could not forget you if he tried.", None),
    ("n6", NARRATOR, "-22%", "-4Hz",
     "And that changes the person who thought she had been left behind. The same God she "
     "feared had forgotten her was carrying her the whole time — her name, her walls, her "
     "whole life, held in his hands.", None),
    ("n7", NARRATOR, "-24%", "-4Hz",
     "So if you have ever felt like the one who gets forgotten — the one nobody keeps in "
     "mind — hear this slowly.", None),
    ("n7b", NARRATOR, "-24%", "-4Hz",
     "You are not out of sight. You are not out of mind. You are graven on the hands of "
     "God, and he has never once looked away.", None),
    ("card", NARRATOR, "-26%", "-4Hz",
     "God told the ones who felt forgotten that he had carved them into his own hands, "
     "always before his eyes. You are not overlooked. Where do you most need to hear that "
     "you have not been forgotten?", None),
]


async def main():
    for name, voice, rate, pitch, text, cap in SEGMENTS:
        await save_narration(text, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")


if __name__ == "__main__":
    import os
    os.makedirs("audio", exist_ok=True)
    asyncio.run(main())
