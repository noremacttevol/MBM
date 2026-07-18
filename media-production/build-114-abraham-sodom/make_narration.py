#!/usr/bin/env python3
"""Narration audio for Video #114 — Abraham Pleads for Sodom (Genesis 18).

Narrator: en-US-AndrewNeural. God's voice: en-US-ChristopherNeural (exact KJV only).
Abraham's words (incl. 'Shall not the Judge of all the earth do right?') are voiced by
the NARRATOR; God's own KJV answers render cream-italic.

God's KJV lines (Christopher, cream italic):
  jv26  Gen 18:26  "If I find in Sodom fifty righteous within the city, then I will spare
                    all the place for their sakes." — sacred silence 1
  jv32  Gen 18:32  "I will not destroy it for ten's sake." — sacred silence 2

WHY-LAW (CONTENT-CARE #165, care J): the story is NOT the destruction — it is the
NEGOTIATION. God lets one man argue with him, out loud, for the sake of strangers, and
keeps saying yes — fifty, forty-five, forty, thirty, twenty, ten. Every step reveals a God
far more willing to spare than to destroy, who welcomes bold intercession. Destruction is
kept entirely off-screen. Milk framing: God is not looking for a reason to condemn; he is
being talked DOWN by mercy, and he invites you to plead boldly too. An invitation, never a threat.

HOMOGRAPH EAR-CHECK: no high-risk homographs. NUMBER-STRESS LAW: no line opens on a numeral.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"
GOD = "en-US-ChristopherNeural"

SEGMENTS = [
    ("n1", NARRATOR, "-20%", "-4Hz",
     "In the heat of the day, three travelers appeared at Abraham's tent. He did not know "
     "at first who they were. He only knew they were strangers, and tired, and that was "
     "enough. He ran to welcome them.", None),
    ("n2", NARRATOR, "-22%", "-4Hz",
     "He washed their feet, baked fresh bread, set out the best he had, and waited on "
     "them himself under the oak. And as they ate, they brought him astonishing news — "
     "and then they rose and looked out toward the cities of the plain.", None),
    ("n3", NARRATOR, "-22%", "-4Hz",
     "For those cities had grown very dark, and judgment was near. Two of the travelers "
     "went on ahead. But Abraham stayed behind, standing before the warm presence of God "
     "— and then this old man did something almost unthinkable. He began to argue.", None),
    ("n4", NARRATOR, "-22%", "-4Hz",
     "Not for himself. For strangers — for the good people who might still be down in "
     "that doomed city. Wilt thou also destroy the righteous with the wicked, he asked. "
     "Shall not the Judge of all the earth do right?", None),
    # jv26 — fifty righteous — silence 1
    ("jv26", GOD, "-26%", "-6Hz",
     "If I find in Sodom fifty righteous within the city, then I will spare all the place "
     "for their sakes.", None),
    ("n5", NARRATOR, "-22%", "-4Hz",
     "Yes, God said. For fifty, I will spare them all. And you can almost feel Abraham's "
     "courage grow. What about forty-five? What about forty? Thirty? Each time, gently, "
     "the answer came back — yes. Yes. I will spare it.", None),
    ("n6", NARRATOR, "-22%", "-4Hz",
     "He is not wearing God down. He is discovering how merciful God already is — how much "
     "God would rather spare than destroy. So Abraham dares one last step. What if there "
     "are only ten?", None),
    # jv32 — for ten's sake — silence 2
    ("jv32", GOD, "-26%", "-6Hz",
     "I will not destroy it for ten's sake.", None),
    ("n7", NARRATOR, "-22%", "-4Hz",
     "For the sake of ten good people, the whole place would be spared. That is the God "
     "Abraham found at the top of that hill. Not one straining to condemn — one who could "
     "be talked, again and again, toward mercy. And what happened to the cities is left "
     "quietly in the distance; this story is about the yeses.", None),
    ("n8", NARRATOR, "-24%", "-4Hz",
     "Abraham went home in the dusk, amazed. He had dared to plead for strangers, and "
     "found God kinder than he had hoped. God let a man argue with him — and kept saying "
     "yes.", None),
    ("card", NARRATOR, "-26%", "-4Hz",
     "God let one old man plead for strangers, and answered mercy every time. He is not "
     "looking for reasons to condemn — he welcomes the bold and the interceding. Who might "
     "you find the courage to plead for?", None),
]


async def main():
    for name, voice, rate, pitch, text, cap in SEGMENTS:
        await save_narration(text, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")


if __name__ == "__main__":
    import os
    os.makedirs("audio", exist_ok=True)
    asyncio.run(main())
