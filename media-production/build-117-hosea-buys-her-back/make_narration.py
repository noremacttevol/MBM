#!/usr/bin/env python3
"""Narration audio for Video #117 — Hosea Buys Her Back (Hosea 1-3).

Narrator: en-US-AndrewNeural. God's voice: en-US-ChristopherNeural (exact KJV only).
The prophet Hosea's own buy-back line (Hosea 3:2) is voiced by the NARRATOR (white caption);
God's own KJV promises render cream-italic in the scripture voice.

God's KJV lines (Christopher, cream italic):
  jvA  Hosea 2:14  "I will allure her, and bring her into the wilderness, and speak
                    comfortably unto her." — sacred silence 1
  jvB  Hosea 2:19-20  "And I will betroth thee unto me for ever... in lovingkindness, and
                       in mercies... and thou shalt know the LORD." — sacred silence 2

CARE FLAGS D, L (Hosea): redemption at the price paid, NEVER the scandal; scripture's own
economy of words about what she was; nothing explicit. Narration never depicts or dwells on
her past — only that she wandered, was brought low, and was bought back and loved home.

WHY-LAW: God dramatized his own love with a marriage. His people wandered; he did not cast
them off. He told Hosea to go love her still, and Hosea went, found her brought low, and
PAID a real price to buy her back — then covered her and led her home. Milk framing: however
far you are sure you have wandered, God comes looking, pays the price himself, and betroths
you to him forever in mercy. An invitation home, never a threat.

HOMOGRAPH EAR-CHECK: 'homer' (dry measure) reads plainly. NUMBER-STRESS LAW obeyed
("fifteen pieces of silver").
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"
GOD = "en-US-ChristopherNeural"

SEGMENTS = [
    ("n1", NARRATOR, "-20%", "-4Hz",
     "Love is easy to picture at the beginning. A man and a woman, hands joined, a "
     "covenant freely given, a home with the door open and the road ahead warm. That is "
     "how God's love for his people began.", None),
    ("n2", NARRATOR, "-22%", "-4Hz",
     "But she wandered. Not because he stopped being good to her — he never did — but "
     "because her heart drifted, and one day she walked away from that warm home down the "
     "long road toward the cold lights of somewhere else.", None),
    ("n3", NARRATOR, "-22%", "-4Hz",
     "And here the story stops being like any other. God did not tell Hosea to forget her. "
     "He told him to go and love her still — to love her the very way God loves a people "
     "who leave him.", None),
    ("n4", NARRATOR, "-22%", "-4Hz",
     "By the time he found where she had ended up, she had lost nearly everything. Brought "
     "low, sitting at the edge of a far marketplace, poor and unseen — a long way from the "
     "home she left.", None),
    ("n5", NARRATOR, "-22%", "-4Hz",
     "He could have let her stay lost. Instead he came looking. He walked all that way into "
     "a place that was not his own, searching the crowd for the one face he had never "
     "stopped loving.", None),
    ("n6", NARRATOR, "-22%", "-4Hz",
     "And when he found her, he did not lecture her. He paid for her. So I bought her to me "
     "for fifteen pieces of silver, and for an homer of barley, and an half homer of "
     "barley. An ordinary price, counted out in full, to buy back her freedom.", None),
    ("n7", NARRATOR, "-22%", "-4Hz",
     "He lifted her up off the ground with his own hands, drew his cloak around her "
     "shoulders, and covered her — no shame thrown at her, no debt held over her, only "
     "welcome. She was his again, not because she earned it, but because he paid.", None),
    # jvA — I will allure her, and bring her into the wilderness — sacred silence 1
    ("jvA", GOD, "-26%", "-6Hz",
     "I will allure her, and bring her into the wilderness, and speak comfortably unto "
     "her.", None),
    # jvB — I will betroth thee unto me for ever — sacred silence 2
    ("jvB", GOD, "-26%", "-6Hz",
     "And I will betroth thee unto me for ever; yea, I will betroth thee unto me in "
     "righteousness, and in judgment, and in lovingkindness, and in mercies. I will even "
     "betroth thee unto me in faithfulness: and thou shalt know the LORD.", None),
    ("n8", NARRATOR, "-24%", "-4Hz",
     "That is what God says to everyone sure they have wandered too far to be wanted back. "
     "He does not wait at the door with a list of your failures. He comes looking, he pays "
     "the price himself, and he calls you home — betrothed to him for ever, in mercy.", None),
    ("card", NARRATOR, "-26%", "-4Hz",
     "God dramatized his own love with a marriage: however far she wandered, he went and "
     "bought her back and brought her home. You are not too far gone to be wanted. What "
     "would it mean to be loved home like that?", None),
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
