#!/usr/bin/env python3
"""Generate narration audio for Story Video #140 — Naaman washes (2 Kings 5).
From DRAFTS/row-140-naaman-washes.md (v2 — the swapped story that REPLACED the
purged far-country dupe, 2026-07-20 repeat audit).

The great captain who almost missed his healing because the instruction was
too simple — "wash, and be clean." For the returner: do the simple thing again.

Quoted lines are EXACT KJV via the speaker system:
  w1 = the little maid (2 Kgs 5:3)        -> WOMAN voice, pink
  s1 = Elisha's messenger (2 Kgs 5:10)    -> SCRIPTURE voice, light blue
  s2 = his servants (2 Kgs 5:13b)         -> SCRIPTURE voice
  s3 = the narrative verse (2 Kgs 5:14b)  -> SCRIPTURE voice, the CENTERPIECE
No divine figure appears; Elisha stays unseen (5:10-11 is the point).

CONTENT-CARE: leprosy modest (forearms/hands only, never graphic).
HOMOGRAPH LAW: scanned — no bow/wound/wind/tears/lead/sow/live/read/dove/close
voiced. "Naaman", "Elisha" (name only in captions, never voiced — narration
says "the prophet"), "wroth" avoided (narration says "furious"). River names
Abana/Pharpar NOT used. Whisper ear-check decides if "Naaman" needs a SPOKEN
override — never trust a respelling untested (pronunciation system 2.0).
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import NARRATOR, SCRIPTURE, WOMAN

# (id, speaker, caption_text). The caption always shows this exact text; only
# the string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR,
     "Naaman was a great man. Captain of the armies of Syria, honorable, "
     "mighty in valour. And under all that armor — he was a leper."),
    ("n1", NARRATOR,
     "In his house served a young girl carried captive out of Israel. She "
     "knew where healing was."),
    # Exact KJV 2 Kings 5:3 — the maid.
    ("w1", WOMAN,
     "Would God my lord were with the prophet that is in Samaria! for he "
     "would recover him of his leprosy."),
    ("n2", NARRATOR,
     "So Naaman came — with his horses, his chariots, his silver and gold — "
     "and stood at the door of a plain little house. The prophet didn't even "
     "come out. He sent a messenger."),
    # Exact KJV 2 Kings 5:10 — the messenger's instruction.
    ("s1", SCRIPTURE,
     "Go and wash in Jordan seven times, and thy flesh shall come again to "
     "thee, and thou shalt be clean."),
    ("n3", NARRATOR,
     "And Naaman was furious. He had expected something great — a mighty "
     "ceremony worthy of a mighty man. Wash in the Jordan? It was too "
     "plain. Too simple. He turned and rode away in a rage."),
    # Exact KJV 2 Kings 5:13b — his servants, the wisest words in the story.
    ("s2", SCRIPTURE,
     "If the prophet had bid thee do some great thing, wouldest thou not "
     "have done it? how much rather then, when he saith to thee, Wash, and "
     "be clean?"),
    ("n4", NARRATOR,
     "So the great captain went down, and dipped himself in the Jordan. "
     "Once. Twice. Seven times, exactly as the man of God had said."),
    # Exact KJV 2 Kings 5:14b — sacred silence, the centerpiece.
    ("s3", SCRIPTURE,
     "And his flesh came again like unto the flesh of a little child, and "
     "he was clean."),
    ("n5", NARRATOR,
     "The instruction wasn't beneath him. It was the way back. If you've "
     "been away, the way back may look almost too simple — pray again, read "
     "again, come back again. Do the simple thing."),
    ("card", NARRATOR,
     "He almost rode away from his healing because it sounded too simple. "
     "Do the simple thing."),
]

# Homographs this build decides for itself (never auto-replaced globally).
# n5 "read again" — present-tense REED is intended AND is the TTS's natural
# reading of "read again"; identity entry marks it decided (audit silence).
SPOKEN = {"read": "read"}


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
