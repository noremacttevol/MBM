#!/usr/bin/env python3
"""Narration for build-157-marvellous-work — Isaiah 29.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

The two red beats split apart doctrinally — one goes blue, one goes green. This build is the clearest illustration in the set of why the distinction matters.

  kv11  Isaiah 29:11  scripture (was red) — Isaiah NARRATING the sealed book. Third person throughout. The man writing, not Deity.
  kv14  Isaiah 29:14  god (was red) — first-person LORD: 'I will proceed to do a marvellous work among this people'. Premortal Jehovah, so green.

kv11 contains quoted human speech ('Read this, I pray thee' / 'I cannot; for it is sealed'). It is NOT split: the people and the learned man are both SCRIPTURE, the same colour and the same voice as Isaiah narrating around them, so a split would change nothing on screen or in the audio.

ADDED — Isaiah 29:13, lifted out of narrator paraphrase (n5 was already retelling it in modern English). This verse genuinely mixes a narrator and a speaker for a full clause, so it IS split:
  kv13a  scripture  'Wherefore the Lord said,'  — Isaiah's attribution
  kv13b  god        'Forasmuch as this people draw near me with their mouth...' — the LORD in first person
Both halves sit on S5, consecutive beats over one image, so no new artwork and the edit the viewer sees is unchanged. n5 stays exactly where it is and now reads as the retelling that follows.

WHY-LAW: when human wisdom hits its limit, God is only getting started. The sealed book is opened by an act of God, not by an expert. Nothing on screen argues the point — a viewer who later learns what the marvellous work was will find the video was quietly right all along.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import GOD, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "The prophet Isaiah painted a strange, almost sad picture of his people. The truth of God, he said, had become to them like a book that is sealed shut — right there in their hands, and yet closed, its meaning locked away."),
    ("n2", NARRATOR, "Imagine a precious book, clasped and sealed, that no one around can open. Everyone senses it matters. No one can get inside it. The words of heaven, sitting sealed in the middle of them."),
    ("n3", NARRATOR, "So they carry it to their most educated man, the scholar everyone respects, and they say, please, read this for us. He turns it over in his hands, and has to admit the plain truth: he cannot. It is sealed."),
    # Isaiah 29:11
    ("kv11", SCRIPTURE, "And the vision of all is become unto you as the words of a book that is sealed, which men deliver to one that is learned, saying, Read this, I pray thee: and he saith, I cannot; for it is sealed:"),
    ("n4", NARRATOR, "Then they hand it to a plain, unschooled man, hoping simple honesty might succeed where learning failed. But he only shakes his head kindly. Neither the wise nor the simple can open it on their own."),
    # Isaiah 29:13
    ("kv13a", SCRIPTURE, "Wherefore the Lord said,"),
    # Isaiah 29:13
    ("kv13b", GOD, "Forasmuch as this people draw near me with their mouth, and with their lips do honour me, but have removed their heart far from me, and their fear toward me is taught by the precept of men:"),
    ("n5", NARRATOR, "Isaiah saw the deeper trouble underneath. The people still said the right words and kept the outward forms, honouring God with their lips — but their hearts had quietly drifted far away, and their worship had shrunk to habits taught by men."),
    ("n6", NARRATOR, "And no amount of human cleverness was going to fix that. The wisdom of the wise had run to the very end of itself. The experts had no key for a sealed book, or for a heart that had wandered off."),
    # Isaiah 29:14
    ("kv14", GOD, "Therefore, behold, I will proceed to do a marvellous work among this people, even a marvellous work and a wonder: for the wisdom of their wise men shall perish, and the understanding of their prudent men shall be hid."),
    ("n7", NARRATOR, "So God promised to step in himself and do something marvellous — a genuine wonder. Not one more lecture from the learned, but an act of God that would open what men had sealed and reach hearts that had wandered."),
    ("n8", NARRATOR, "That is the beautiful turn in this verse. When human wisdom hits its limit, God is only getting started. He is fond of marvellous works and wonders — the very things the experts said could not happen. So the only question is a hopeful one. When the wonder comes, will you be humble enough to receive it?"),
    ("card", NARRATOR, "When human wisdom runs dry and the book is sealed, God promises a marvellous work and a wonder — opening what men could not, and reaching hearts that had wandered. When the wonder comes, will you receive it?"),
]

# Homographs this build decides for itself (never auto-replaced globally).
SPOKEN = {}


async def main():
    os.makedirs("audio", exist_ok=True)
    for name, speaker, text in SEGMENTS:
        flagged = [w for w in audit(text) if w not in SPOKEN]
        if flagged:
            print(f"  ! {name}: undecided homograph(s) {flagged}")
        await save_speaker_narration(spoken_text(text, SPOKEN), speaker,
                                     f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3  [{speaker}]")


if __name__ == "__main__":
    asyncio.run(main())
