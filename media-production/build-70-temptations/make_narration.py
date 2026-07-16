#!/usr/bin/env python3
"""Generate narration audio for Story Video #70 — The Temptations (Matt 4:1-11).
Narrator: modern, warm, low, unhurried (American). Plain US model only.
Jesus voice: AMERICAN, never British. Jesus speaks ONLY exact KJV:
Matt 4:4, 4:7, 4:10 (fetched, not hand-typed).
CONTENT-CARE (A,L): the adversary is PRESENCE, never portrait — never depicted,
never voiced; his words are narrator-paraphrased. Jesus is alone in every frame.
HOMOGRAPH LAW: "live" in Matt 4:4 gets a SPOKEN respelling ("liv"); caption
stays exact KJV.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0", NARRATOR, "-20%", "-4Hz",
     "Straight from the river, still carrying his Father's words — "
     "this is my beloved Son — Jesus was led by the Spirit up into "
     "the wilderness. Not by accident. Led there. Before the "
     "teaching, before the miracles, there was going to be a "
     "battle, and it was going to happen in the emptiest place in "
     "the country: bare rock, dead heat, and silence."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "He fasted forty days and forty nights. Mark that: he was not "
     "floating above any of it. He got hungrier every single day, "
     "the way you would. And when he was at his weakest and "
     "emptiest — that is exactly when the tempter came."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "Listen to the first move. IF you are the Son of God — turn "
     "these stones into bread. Hear what that little word IF is "
     "doing. Heaven had just said, this IS my Son. The very first "
     "attack was aimed at that sentence — prove it, earn it, doubt "
     "it. And the bait was reasonable: you're starving, you have "
     "the power, feed yourself. Use what you are for you."),
    # Exact KJV Matt 4:4 — SILENCE around it.
    ("j1", JESUS, "-20%", "-2Hz",
     "It is written, Man shall not live by bread alone, but by "
     "every word that proceedeth out of the mouth of God."),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "Notice what he did NOT do. He did not argue. He did not use "
     "his own power. He answered with a line of scripture — a "
     "sentence any of us could memorize — and stood on it. The Son "
     "of God fought hungry, as a man, with the same weapon you "
     "have on your shelf."),
    ("n4", NARRATOR, "-20%", "-4Hz",
     "The second try was stranger. In a flash he was at the "
     "highest corner of the temple, the city far below — and the "
     "voice turned religious. It quoted scripture BACK at him: "
     "throw yourself down; the angels are promised to catch you. "
     "Force your Father to prove himself, publicly, on demand. "
     "Make God perform."),
    # Exact KJV Matt 4:7 — SILENCE around it.
    ("j2", JESUS, "-20%", "-2Hz",
     "It is written again, Thou shalt not tempt the Lord thy God."),
    ("n5", NARRATOR, "-20%", "-4Hz",
     "Trust does not run experiments on the one it trusts. Then "
     "came the last offer, the biggest one. From a high mountain, "
     "all the kingdoms of the world and the glory of them, spread "
     "out like a feast: all of it, yours, right now — one bow, to "
     "me. It was the crown without the cross. Everything he came "
     "to win, offered as a shortcut with only one small "
     "condition: worship the wrong king."),
    # Exact KJV Matt 4:10 — SILENCE around it.
    ("j3", JESUS, "-18%", "-2Hz",
     "Get thee hence, Satan: for it is written, Thou shalt worship "
     "the Lord thy God, and him only shalt thou serve."),
    ("n6", NARRATOR, "-20%", "-4Hz",
     "And it was over. The devil left him — for a season. And "
     "angels came and ministered to him, the way dawn comes after "
     "the longest night. Bread, after the fast. Company, after "
     "the silence. His Father had not been absent for one minute "
     "of it — he had been trusted."),
    ("n7", NARRATOR, "-20%", "-4Hz",
     "Why does this story matter to you? Because the book of "
     "Hebrews says it plainly: we do not have a Savior who cannot "
     "understand our weakness — he was tempted in all points like "
     "we are. Hungry, alone, offered every shortcut. He has stood "
     "in your exact spot. That is why he knows how to stand next "
     "to you in it."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "He has stood where you stand — hungry, alone, offered every "
     "shortcut — and he held. Ask him. He knows how to help you "
     "hold."),
]

# HOMOGRAPH LAW — Matt 4:4 contains "live" (the #1 TTS offender): SPOKEN
# respelling "liv" for audio; the caption keeps the exact KJV text.
SPOKEN = {
    "j1": ("It is written, Man shall not liv by bread alone, but by "
           "every word that proceedeth out of the mouth of God."),
    "n5": ("Trust does not run experiments on the one it trusts. Then "
           "came the last offer, the biggest one. From a high mountain, "
           "all the kingdoms of the world and the glory of them, spread "
           "out like a feast: all of it, yours, right now — one beau, to "
           "me. It was the crown without the cross. Everything he came "
           "to win, offered as a shortcut with only one small "
           "condition: worship the wrong king."),
}


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts_text = SPOKEN.get(name, text)
        tts = edge_tts.Communicate(tts_text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
