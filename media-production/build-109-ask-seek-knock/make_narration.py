#!/usr/bin/env python3
"""Narration for build-109-ask-seek-knock — Matthew 7.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

All three existing red beats are correctly red and were left alone. Matthew 7 is
the Sermon on the Mount - Jesus speaking in the flesh, continuously - and none of
these segments carried an evangelist framing clause, so there was nothing to
split and nothing to move out of red.

STAYED RED (jesus):
  jv7   Matt 7:7   'Ask, and it shall be given you; seek, and ye shall find;
                    knock, and it shall be opened unto you:'
  jv8   Matt 7:8   'For every one that asketh receiveth; and he that seeketh
                    findeth; and to him that knocketh it shall be opened.'
  jv11  Matt 7:11  'If ye then, being evil, know how to give good gifts unto your
                    children, how much more shall your Father which is in heaven
                    give good things to them that ask him?'

LIFTED FROM PARAPHRASE - also Jesus, so also RED:
  jv910 Matt 7:9-10 'Or what man is there of you, whom if his son ask bread, will
                     he give him a stone? Or if he ask a fish, will he give him a
                     serpent?'
n5 was retelling these two verses in modern English while the verses themselves
were missing, which left jv11's 'if ye then, being evil' resting on a picture the
viewer had only heard described. Now the real verse speaks first.

EDIT TO EXISTING NARRATOR TEXT: n5 is split at its own seam. n5 keeps only its
lead-in sentence - 'Then Jesus makes it personal with a picture from any home.'
- and hands to jv910. Its remaining four sentences become n5b, unchanged word for
word, now functioning as the retelling. All three beats stay on S7, so the
picture is unchanged.

WOMEN: Matthew 7 records no woman speaking. Nothing was added rather than
reaching outside the chapter for one.

WHY-LAW: prayer is not technique and not endurance. It is a child putting out its
hands to a Father who is glad to be asked. Milk framing - just ask.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "People have always wondered how prayer really works. Do you have to say it just right? Wear God down? Jesus, teaching on a hillside, made it startlingly simple."),
    # Matthew 7:7
    ("jv7", JESUS, "Ask, and it shall be given you; seek, and ye shall find; knock, and it shall be opened unto you:"),
    ("n2", NARRATOR, "Three words, and each one is warmer and more personal than the last. Ask — like a child who simply puts out its hands, trusting, expecting good."),
    ("n3", NARRATOR, "Seek — more than a word now; it is getting up and searching, patient and hopeful, sure that what you are looking for is really there to be found."),
    # Matthew 7:8
    ("jv8", JESUS, "For every one that asketh receiveth; and he that seeketh findeth; and to him that knocketh it shall be opened."),
    ("n4", NARRATOR, "Knock — and keep knocking — on a door you cannot yet see behind. And the promise is that the door does open. Not maybe. Not for the specially worthy. Every one who asks, receives."),
    ("n5", NARRATOR, "Then Jesus makes it personal with a picture from any home."),
    # Matthew 7:9-10
    ("jv910", JESUS, "Or what man is there of you, whom if his son ask bread, will he give him a stone? Or if he ask a fish, will he give him a serpent?"),
    ("n5b", NARRATOR, "A child asks its father for bread. What kind of father hands his hungry child a stone instead? Or a snake when he asks for a fish? No father you would trust."),
    # Matthew 7:11
    ("jv11", JESUS, "If ye then, being evil, know how to give good gifts unto your children, how much more shall your Father which is in heaven give good things to them that ask him?"),
    ("n6", NARRATOR, "How much more. If flawed, tired, imperfect parents still love to give their kids good things — how much more does a perfect Father delight to give to you? Prayer is not twisting God's arm. It is a child asking a good Father who is glad to be asked."),
    ("n7", NARRATOR, "So the invitation is just this: ask. Not perfectly. Not impressively. Simply, honestly, like a child. The Father is not reluctant. He is leaning in, glad to hear your voice."),
    ("card", NARRATOR, "Ask, seek, knock. Jesus says your Father in heaven is far kinder than the best parent you can imagine, and glad to be asked. Is there something you have been afraid to ask him for?"),
]

# Homographs this build decides for itself (never auto-replaced globally).
# Cameron denials 2026-07-18:
#   "kinder"  — read the German way (KIN-der, as in kindergarten). It is the
#               English comparative of "kind": KYNE-der.
#   "findeth" — must be FYND-uhth (long i), not FIN-deth.
# Captions still show the exact words; only the spoken audio is respelled.
SPOKEN = {
    "kinder": "kynder",
    "findeth": "fyndeth",
}


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
