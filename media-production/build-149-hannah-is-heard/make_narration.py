#!/usr/bin/env python3
"""Narration for build-149-hannah-is-heard — 1 Samuel 1.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

This build had ZERO scripture voices — Hannah's vow, her answer to Eli, her naming
of Samuel and her giving him back were ALL paraphrased in the narrator's white voice.
Hannah is one of the great praying women in the Bible and the video never let her
speak. Fixed.

Lifted out as WOMAN (pink), verbatim KJV:
  w1a/w1b  1 Sam 1:11  her vow, split in two so the line is not one long breath
  w2       1 Sam 1:15  'No, my lord, I am a woman of a sorrowful spirit...'
  w3       1 Sam 1:20  'Because I have asked him of the LORD.'
  w4       1 Sam 1:28  'Therefore also I have lent him to the LORD...'
Eli's blessing is SCRIPTURE (light blue):
  s1       1 Sam 1:17  'Go in peace: and the God of Israel grant thee thy petition...'

1 Samuel is Old Testament — nothing here is `jesus`, and no one in this chapter is
Deity speaking, so there is no `god` beat either. Correct for the chapter.

LEFT OUT ON PURPOSE: 1 Sam 1:16 ('Count not thine handmaid for a daughter of
Belial'). I am confident of the wording, but 'daughter of Belial' needs a paragraph
of explanation a first-time viewer does not have. Milk before meat — verse 15 alone
carries her whole answer. Nothing is paraphrased-as-scripture anywhere in this plan.

Narrator segments n2, n3b, n4, n5 and n6 were rewritten from paraphrase-of-Hannah
into retellings that follow her Old English, per the retelling rule. Every original
segment id is kept.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import NARRATOR, SCRIPTURE, WOMAN

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0a", NARRATOR, "Year after year, Hannah went to the house of the LORD and came away with an empty lap."),
    ("n0b", NARRATOR, "The other wife mocked her for it."),
    ("n1", NARRATOR, "One year at Shiloh, Hannah slipped to the door of the tabernacle and prayed with a voice no one could hear — only her lips moved. This is what she said."),
    # 1 Samuel 1:11
    ("w1a", WOMAN, "O LORD of hosts, if thou wilt indeed look on the affliction of thine handmaid, and remember me, and not forget thine handmaid,"),
    # 1 Samuel 1:11
    ("w1b", WOMAN, "but wilt give unto thine handmaid a man child, then I will give him unto the LORD all the days of his life."),
    ("n2", NARRATOR, "Just look at me, she was saying. Remember me. Don't forget me. Give me a son — and I will give him back to You for the whole of his life. She asked for the one thing she wanted most, and promised it away in the same breath."),
    ("n3a", NARRATOR, "Eli the priest watched her lips move with no sound coming out, and thought she was drunk."),
    # 1 Samuel 1:15
    ("w2", WOMAN, "No, my lord, I am a woman of a sorrowful spirit: I have drunk neither wine nor strong drink, but have poured out my soul before the LORD."),
    ("n3b", NARRATOR, "No, my lord, she told him. I haven't been drinking. I'm a woman with a heavy heart, and I've been pouring my soul out to the Lord. She was not ashamed of the prayer. She just wanted him to know what he was looking at."),
    # 1 Samuel 1:17
    ("s1", SCRIPTURE, "Go in peace: and the God of Israel grant thee thy petition that thou hast asked of him."),
    ("n4", NARRATOR, "Go in peace, Eli said — and may the God of Israel give you the very thing you asked for. She went away, and her face was no longer sad. The LORD remembered her."),
    # 1 Samuel 1:20
    ("w3", WOMAN, "Because I have asked him of the LORD."),
    ("n5", NARRATOR, "A boy was born, and she named him Samuel — because I asked God for him. Every time anyone said that child's name, they were saying it again: I asked, and He heard."),
    # 1 Samuel 1:28
    ("w4", WOMAN, "Therefore also I have lent him to the LORD; as long as he liveth he shall be lent to the LORD."),
    ("n6", NARRATOR, "She kept her word. I have lent him to the Lord, she said — for as long as he lives. When he was weaned, she brought him to the house of the LORD and left him there to serve."),
    ("card", NARRATOR, "Hannah prayed the prayer no one else could hear, and God answered. Your quiet prayers are heard too."),
]

# Homographs this build decides for itself (never auto-replaced globally).
SPOKEN = {}


SPOKEN.update({'watched': 'wotched'})  # round2 in-context A/B winners 2026-07-20 (SWEEP/round2-state.json)
SPOKEN.update({'liveth': 'livveth'})  # Cameron complaint #149 "liveth pronounced wrong": whisper writes "liveeth" for every variant so it cannot rank them; 'livveth' is orthographically locked to LIV-eth (short i) and round-trips as clean as plain (A/B 2026-07-21)

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
