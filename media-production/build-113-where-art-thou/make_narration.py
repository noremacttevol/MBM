#!/usr/bin/env python3
"""Narration audio for Video #113 — "Where Art Thou?" (Genesis 3).

Narrator: en-US-AndrewNeural. God's voice: en-US-ChristopherNeural (exact KJV only).
Adam's words and the narrative 'coats of skins' line are voiced by the NARRATOR (God's
voice is reserved for God's own words); God's KJV renders cream-italic.

God's KJV line (Christopher, cream italic):
  jv9  Gen 3:9  "Where art thou?" — the seeking call (sacred silence)

WHY-LAW: the very first question God asks a human being, after everything has gone wrong,
is not "what have you done?" but "where are you?" — the cry of a Father looking for a
child who is hiding. He comes not to destroy them but to find them; and before he sends
them out, he makes them clothes with his own hands and covers their shame. Milk framing:
however far you have run or however badly you have failed, God comes seeking, and he
covers what you cannot cover yourself. Tender and merciful, never a threat.

HOMOGRAPH EAR-CHECK: no high-risk homographs. NUMBER-STRESS LAW obeyed.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"
GOD = "en-US-ChristopherNeural"

SEGMENTS = [
    ("n1", NARRATOR, "-20%", "-4Hz",
     "In the beginning there was a garden, and in the garden, peace. People and God "
     "walking together in the cool of the day, with nothing to hide and nothing to fear.", None),
    ("n2", NARRATOR, "-22%", "-4Hz",
     "There was only one thing they were asked not to do. And, as people do, they did it "
     "anyway — reaching for the one thing that was not theirs, hoping it would make them "
     "more than they were.", None),
    ("n3", NARRATOR, "-22%", "-4Hz",
     "And everything changed. For the first time they felt shame. They saw themselves, "
     "and did not like what they saw, and scrambled to cover up, hiding from each other.", None),
    ("n4", NARRATOR, "-22%", "-4Hz",
     "And then they heard him coming — the warm presence of God moving through the garden "
     "in the cool of the evening, the way he always had. And this time, they ran and hid "
     "themselves among the trees.", None),
    # jv9 — Where art thou? — sacred silence
    ("jv9", GOD, "-26%", "-6Hz",
     "Where art thou?", None),
    ("n5", NARRATOR, "-22%", "-4Hz",
     "Where are you. Not, what have you done. Not, how dare you. Where are you — the cry "
     "of a Father looking for a child who is hiding. He knew exactly where they were. He "
     "asked so they would come out. And, trembling, the man answered: I heard you, and I "
     "was afraid, and I hid myself.", None),
    ("n6", NARRATOR, "-22%", "-4Hz",
     "There were consequences; there always are. The easy garden was behind them now, and "
     "a hard world lay ahead. They stood there, ashamed, waiting for the end of "
     "everything.", None),
    ("n7", NARRATOR, "-22%", "-4Hz",
     "And instead, God did something they never expected. He made them clothes. With his "
     "own care he covered their shame — better coverings than the leaves they had grabbed "
     "for themselves — because they could not fix what they had broken, and he would not "
     "leave them exposed.", None),
    ("n8", NARRATOR, "-22%", "-4Hz",
     "Then he sent them out into the wide world — but not naked, and not alone, and not "
     "without a promise. Clothed by the very One they had run from.", None),
    ("n9", NARRATOR, "-24%", "-4Hz",
     "That is the God of the very first story. Not one who waits for you to clean "
     "yourself up and come find him. One who comes walking through the garden in the cool "
     "of the evening, calling, still calling — where are you? — because he wants you back.", None),
    ("card", NARRATOR, "-26%", "-4Hz",
     "The first thing God said to hiding people was not a scolding — it was, where are "
     "you? He still comes seeking, and still covers the shame we cannot cover ourselves. "
     "Where are you hiding, that he is gently calling you out of?", None),
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
