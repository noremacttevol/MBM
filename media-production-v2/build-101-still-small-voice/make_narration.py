#!/usr/bin/env python3
"""Narration for build-101-still-small-voice — 1 Kings 19.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

All five red beats were painted JESUS-RED. 1 Kings is Old Testament, so none of
them can be red — a red-letter KJV leaves the whole Old Testament black.

WHERE THEY LANDED:
  jv9   GOD    'What doest thou here, Elijah?'  (19:9)  — Jehovah speaking.
  jv11a GOD    'Go forth, and stand upon the mount before the LORD.' (19:11)
  jv18  GOD    'Yet I have left me seven thousand in Israel...' (19:18)
  jv11b SCRIPTURE  — see the deviation note below.
  jv12  SCRIPTURE  — see the deviation note below.

MIXED SEGMENT SPLIT: jv11a carried two speakers in one block. The command 'Go
forth, and stand upon the mount before the LORD' is Jehovah. Everything after it
('And, behold, the LORD passed by, and a great and strong wind rent the
mountains...') is the writer of 1 Kings describing what happened. Split into
jv11a (green) and the new jv11c (light blue). Both stay on S5, so the picture
the viewer sees is unchanged.

DEVIATION FROM THE BRIEFING NOTE — PLEASE REVIEW: the instruction said all five
red segments become `god`. Applying the law's own test to jv11b and jv12, I could
not do that honestly. jv11b ('and after the wind an earthquake; but the LORD was
not in the earthquake:') and jv12 ('And after the fire a still small voice.') are
not Deity speaking at all — they are the same 1 Kings narration that the briefing
itself told me to strip out of jv11a. The LORD is the subject of those sentences,
not the speaker. SPEAKER-LAW section 3 says narration about a speaker is
`scripture`, not the speaker's own colour. So both are light blue. If Cameron
wants the whole theophany green for visual continuity, that is a one-word change
in each and it is his call — but the law as written puts them in blue.

LIFTED FROM PARAPHRASE: Elijah's own answer was buried in n4's modern retelling.
It is now s10 (1 Kings 19:10), verbatim, with n4 unchanged after it as the
retelling. This is the emotional centre of the story and the viewer should hear
the man actually say it.

NO WOMEN: 1 Kings 19 records no woman speaking. Jezebel's threat is 19:2 and is
relayed by a messenger, not quoted in this video.

WHY-LAW: God feeds a suicidal prophet before he corrects him, and answers him in
a whisper. Milk framing — God is gentle with the worn out.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import GOD, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, 'Elijah had just won the greatest victory of his life. And then a single threat sent him running for the wilderness, until he sank down under a lone bush, worn out and afraid, and asked God to let him die.'),
    ("n2", NARRATOR, 'God did not scold him. While he slept, warm bread was baked for him and a jar of water set by his head. Twice he was fed, and gently told the journey was too great for him to make alone.'),
    ("n3", NARRATOR, 'In that strength he walked forty days across the wilderness, all the way to the mountain of God, and found a cave, and went in, and stayed there in the dark.'),
    ("jv9", GOD, 'What doest thou here, Elijah?'),
    ("s10", SCRIPTURE, 'I have been very jealous for the LORD God of hosts: for the children of Israel have forsaken thy covenant, thrown down thine altars, and slain thy prophets with the sword; and I, even I only, am left; and they seek my life, to take it away.'),
    ("n4", NARRATOR, 'And out it all poured. I have given everything for you, he said. I am the only one left, and now they want me dead too.'),
    ("jv11a", GOD, 'Go forth, and stand upon the mount before the LORD.'),
    ("jv11c", SCRIPTURE, 'And, behold, the LORD passed by, and a great and strong wind rent the mountains, and brake in pieces the rocks before the LORD; but the LORD was not in the wind:'),
    ("jv11b", SCRIPTURE, 'and after the wind an earthquake; but the LORD was not in the earthquake:'),
    ("n5", NARRATOR, 'A wind strong enough to tear the mountain apart. Then an earthquake that split the rock under his feet. Then a fire sweeping across the stone. Surely God would be in something that big. But he was not in any of them.'),
    ("jv12", SCRIPTURE, 'And after the fire a still small voice.'),
    ("n6", NARRATOR, 'After all the noise and power, everything went quiet. And in the quiet came a low, gentle whisper. That was where God was. Elijah heard it, and wrapped his face in his cloak, and came to the mouth of the cave to listen.'),
    ("n7", NARRATOR, 'The whisper did not shame him for being afraid. It asked him again what troubled him, let him say it all a second time, and then quietly gave him work to do and people to go to. He was being sent back, steadied and not alone.'),
    ("jv18", GOD, 'Yet I have left me seven thousand in Israel, all the knees which have not bowed unto Baal, and every mouth which hath not kissed him.'),
    ("n8", NARRATOR, 'You are not the only one, God told him. Scattered across the land are thousands who have never bent the knee to the lie. You feel alone, but you are not. That is how God answered a tired, frightened man — not with thunder, but with a whisper, and with the truth that he was never as alone as he feared.'),
    ("card", NARRATOR, 'The wind, the earthquake and the fire were not God. The whisper was. When you are worn out and sure you are the only one left, could the voice you most need be the gentle one?'),
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
