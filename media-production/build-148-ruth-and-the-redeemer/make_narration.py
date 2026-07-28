#!/usr/bin/env python3
"""Narration for build-148-ruth-and-the-redeemer — Ruth 1.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

The single most quotable line in the Old Testament outside the psalms — Ruth 1:16-17 —
was a modern paraphrase in the narrator's voice ('Where you go, I'll go'). That is now
Ruth herself, WOMAN (pink), verbatim KJV, split in two so each half lands:
  w1a  Ruth 1:16  'Intreat me not to leave thee... thy God my God'
  w1b  Ruth 1:17  'Where thou diest, will I die...'
n2 is kept (id preserved) and rewritten from paraphrase into the retelling.

Naomi also speaks now — WOMAN — because it is the hinge of the chapter and it makes
the ending land harder when her arms are filled:
  w2a  Ruth 1:20  'Call me not Naomi, call me Mara...'
  w2b  Ruth 1:21  'I went out full, and the LORD hath brought me home again empty.'

Boaz gets his own voice as SCRIPTURE (light blue) — he is a man in the story, not Deity:
  s1   Ruth 2:12  'The LORD recompense thy work...'
  s2   Ruth 3:11  '...thou art a virtuous woman.'

Ruth is Old Testament, and no beat in this chapter is Deity speaking, so there is no
`jesus` and no `god` beat. Nothing was previously red; six new voiced lines were added
and every one is verbatim.

LEFT AS NARRATOR: the women of Bethlehem blessing Naomi in Ruth 4:14-15, and the
gate scene in Ruth 4:9-10. Both are strong, but I am not certain enough of the exact
KJV wording to put them in a coloured voice, so they stay in the storyteller's mouth.

WHY-LAW: Boaz is called the redeemer by law, and the last beat quietly points past him.
Nothing on screen argues it. Milk.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import NARRATOR, SCRIPTURE, WOMAN

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, 'A widow named Naomi lost everything in a foreign land — her husband and both sons buried there.'),
    ("n1", NARRATOR, 'She told her two daughters-in-law to go home to their own people. One kissed her and left. But Ruth clung to her, and would not go.'),
    ("w1a", WOMAN, 'Intreat me not to leave thee, or to return from following after thee: for whither thou goest, I will go; and where thou lodgest, I will lodge: thy people shall be my people, and thy God my God.'),
    ("w1b", WOMAN, 'Where thou diest, will I die, and there will I be buried: the LORD do so to me, and more also, if ought but death part thee and me.'),
    ("n2", NARRATOR, "Don't ask me to leave you, Ruth said. Wherever you go, I'm going. Wherever you stay, I'm staying. Your people are my people now, and your God is my God. Only death gets to separate us — and even that, may God deal with me if it does."),
    ("w2a", WOMAN, 'Call me not Naomi, call me Mara: for the Almighty hath dealt very bitterly with me.'),
    ("w2b", WOMAN, 'I went out full, and the LORD hath brought me home again empty.'),
    ("n2b", NARRATOR, "Naomi means pleasant. Don't call me that anymore, she said when she got home — call me bitter. I went out with a husband and two sons, and I've come back with nothing. Hold on to that word, empty. The story is not finished with it."),
    ("n3", NARRATOR, 'Ruth gleaned grain in the fields behind the harvesters to keep Naomi fed — and the field belonged to a man named Boaz.'),
    ("s1", SCRIPTURE, 'The LORD recompense thy work, and a full reward be given thee of the LORD God of Israel, under whose wings thou art come to trust.'),
    ("n4", NARRATOR, "May the Lord pay you back for what you've done, Boaz told her, and may He give you a full reward — the God of Israel, the One you came here to take shelter under. He protected her, fed her, and spoke kindly. He was a near kinsman — a redeemer by the law."),
    ("s2", SCRIPTURE, 'For all the city of my people doth know that thou art a virtuous woman.'),
    ("n5", NARRATOR, "The whole town knows what kind of woman you are, he said. At the threshing floor Ruth had asked him to cover her with his cloak, the sign of a kinsman's duty — and he promised to redeem her."),
    ("n6a", NARRATOR, 'Before the town gate, in front of witnesses, Boaz bought the right to marry Ruth.'),
    ("n6b", NARRATOR, "Naomi's emptiness was filled; a son was born, and the neighbour women laid him in her lap."),
    ("n7", NARRATOR, 'That boy became the grandfather of King David — and part of the line that leads to the greater Redeemer still to come.'),
    ("card", NARRATOR, "Ruth gave up everything to follow the God she'd come to love. He never let her go. Neither will He let you go."),
]

# Homographs this build decides for itself (never auto-replaced globally).
SPOKEN = {
    "Intreat": "in-treat",
    "ought": "awt",
    # 2026-07-21 whisper sweep of the shipped mp4: Michelle read "diest" as
    # "dost" (breaks Ruth's vow) and Andrew's "Boaz" came out "Boas/boss".
    # A/B-tested in the real voices: 'dyest' round-trips "die-est"; 'bohazz'
    # restores the two syllables BOH-az. Captions keep the exact KJV words.
    "diest": "dyest",
    "Boaz": "bohazz",
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
