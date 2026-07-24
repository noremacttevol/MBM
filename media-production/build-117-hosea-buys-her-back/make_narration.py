#!/usr/bin/env python3
"""Narration for build-117-hosea-buys-her-back — Hosea 1.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

Both red beats are Jehovah speaking in Hosea 2 - Old Testament, so a red-letter KJV
prints them black. They become GOD (green). Nothing in this build is `jesus`.

LINES LIFTED OUT OF NARRATOR PARAPHRASE:
  gv1  Hosea 3:1  the LORD's charge to Hosea - was paraphrased inside n3, now GOD
  s32  Hosea 3:2  'So I bought her to me for fifteen pieces of silver...' - this was
                  already sitting verbatim inside narrator beat n6, spoken in the
                  narrator's voice. It is Hosea's own first-person line, so SCRIPTURE.

THE WOMEN - this is the build the woman voice was made for. Hosea 2 records the
wife's own words twice, on both ends of the arc, and neither was in the video:
  w1  Hosea 2:5  'I will go after my lovers...'  - why she left
  w2  Hosea 2:7  'I will go and return to my first husband...' - why she came back
Putting w2 on S8, the road home, is the emotional centre of the piece: the video now
has her deciding to come home in her own recorded words.

Every Old English line gets a narrator retelling after it (n2b, n3, n6, n7b, n8w).
n6 keeps its id but the KJV clause is pulled out of it so it is a clean retelling.

MILK FRAMING: God dramatised his covenant love as a marriage. He is not the wronged
party keeping score - he is the husband who goes and pays. No wandering is too far.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import GOD, NARRATOR, SCRIPTURE, WOMAN

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "Love is easy to picture at the beginning. A man and a woman, hands joined, a covenant freely given, a home with the door open and the road ahead warm. That is how God's love for his people began."),
    ("n2", NARRATOR, "But she wandered. Not because he stopped being good to her — he never did — but because her heart drifted. And Hosea wrote down what she told herself as she went."),
    # Hosea 2:5
    ("w1", WOMAN, "I will go after my lovers, that give me my bread and my water, my wool and my flax, mine oil and my drink."),
    ("n2b", NARRATOR, "I am going after the ones who give me what I want, she said. My food, my water, my clothes. She did not think she was walking away from love. She thought she was walking toward it — down the long road toward the cold lights of somewhere else."),
    # Hosea 3:1
    ("gv1", GOD, "Go yet, love a woman beloved of her friend, yet an adulteress, according to the love of the LORD toward the children of Israel, who look to other gods."),
    ("n3", NARRATOR, "And here the story stops being like any other. God did not tell Hosea to forget her. Go and love her still, he said — love her the very way I love a people who leave me. The whole marriage was a picture of God's own heart, acted out by a man who had to live it."),
    ("n4", NARRATOR, "By the time he found where she had ended up, she had lost nearly everything. Brought low, sitting at the edge of a far marketplace, poor and unseen — a long way from the home she left."),
    ("n5", NARRATOR, "He could have let her stay lost. Instead he came looking. He walked all that way into a place that was not his own, searching the crowd for the one face he had never stopped loving."),
    # Hosea 3:2
    ("s32", SCRIPTURE, "So I bought her to me for fifteen pieces of silver, and for an homer of barley, and an half homer of barley."),
    ("n6", NARRATOR, "And when he found her, he did not lecture her. He paid for her."),
    ("n7", NARRATOR, "He lifted her up off the ground with his own hands, drew his cloak around her shoulders, and covered her — no shame thrown at her, no debt held over her, only welcome. She was his again, not because she earned it, but because he paid."),
    # Hosea 2:14
    ("jvA", GOD, "I will allure her, and bring her into the wilderness, and speak comfortably unto her."),
    ("n7b", NARRATOR, "I will win her back, God says. I will take her out where it is quiet, away from all the noise, and I will speak to her tenderly. Not shouting. Not shaming. Speaking comfortably — the way you talk to someone you are glad to have back."),
    # Hosea 2:7
    ("w2", WOMAN, "I will go and return to my first husband; for then was it better with me than now."),
    ("n8w", NARRATOR, "That is the whole of repentance in one honest sentence. Turning around on the road and heading home."),
    # Hosea 2:19-20
    ("jvB", GOD, "And I will betroth thee unto me for ever; yea, I will betroth thee unto me in righteousness, and in judgment, and in lovingkindness, and in mercies. I will even betroth thee unto me in faithfulness: and thou shalt know the LORD."),
    ("n8", NARRATOR, "Betrothed for ever. Not taken back on probation — married again, in righteousness and mercy and faithfulness, for good. That is what God says to everyone sure they have wandered too far to be wanted back. He does not wait at the door with a list of your failures. He comes looking, he pays the price himself, and he calls you home."),
    ("card", NARRATOR, "God dramatized his own love with a marriage: however far she wandered, he went and bought her back and brought her home. You are not too far gone to be wanted. What would it mean to be loved home like that?"),
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
