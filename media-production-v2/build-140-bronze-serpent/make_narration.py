#!/usr/bin/env python3
"""Generate narration audio for Story Video #140 — The Bronze Serpent
(Numbers 21:4-9 + John 3:14-15).

Authored 2026-08-13 as the REPLACEMENT for the archived Naaman build (Cameron
rejected Naaman's "way back / come home" moral as a duplicate of #2 Prodigal
Son). This is the wilderness event Jesus HIMSELF chose to explain his cross:
"as Moses lifted up the serpent... even so must the Son of man be lifted up"
(John 3:14). Moral: look in faith to God's provision and live — a simple,
desperate looking that saves. NOT a Nicodemus dupe (#4 is the John 3
conversation; this is the historical type it points back to).

Quoted lines are EXACT KJV via the speaker system:
  p1 = the people's murmuring  (Num 21:5)   -> SCRIPTURE voice, light blue
  s1 = the fiery serpents      (Num 21:6)   -> SCRIPTURE voice
  p2 = the people's confession (Num 21:7)   -> SCRIPTURE voice
  g1 = the LORD to Moses        (Num 21:8)   -> GOD voice, green (OT theophany
                                               of Jehovah; NOT red-lettered)
  s2 = Moses makes the serpent (Num 21:9)   -> SCRIPTURE voice, the CENTERPIECE
  j1 = the Son of man lifted up (John 3:14-15) -> JESUS voice, red — the
                                               connection Jesus drew himself
No divine figure is shown in any frame (OT era). The bronze serpent on the
pole is the visual anchor and the cross-foreshadow. The LORD and the Son of
man are VOICED (green / red captions) but never depicted.

CONTENT-CARE: the fiery serpents are real venomous snakes in a real camp; the
bitten are shown with DIGNITY (fear, weakness, being carried and tended) —
NEVER horror, gore, wounds, or lingering death detail. See CONTENT-CARE.md.
HOMOGRAPH LAW: scanned — no bow/wound/wind/tears/lead/sow/read/dove/close
voiced. "live/lived" ear-checked (Num 21:8 "shall live", card "look, and
live"); the SPOKEN dict below pins any that break on ElevenLabs Brian.
"Edom" and "wilderness" ear-checked. Names (Moses) never mispronounce.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import NARRATOR, SCRIPTURE, GOD, JESUS

# (id, speaker, caption_text). The caption always shows this exact text; only
# the string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR,
     "Israel had walked out of Egypt on a miracle — a sea split open, bread "
     "fallen from the sky, water struck out of a rock. But the wilderness was "
     "long, and their patience wore through."),
    ("n1", NARRATOR,
     "On the hard road around Edom, tired and discouraged, they turned on the "
     "very God who had rescued them, and on Moses."),
    # Exact KJV Numbers 21:5 — the people's murmuring.
    ("p1", SCRIPTURE,
     "Wherefore have ye brought us up out of Egypt to die in the wilderness? "
     "for there is no bread, neither is there any water; and our soul loatheth "
     "this light bread."),
    ("n2", NARRATOR,
     "They had bread from heaven every morning — and called it worthless. And "
     "the wilderness they blamed for their misery was about to show them what "
     "a real danger looked like."),
    # Exact KJV Numbers 21:6 — the fiery serpents.
    ("s1", SCRIPTURE,
     "And the LORD sent fiery serpents among the people, and they bit the "
     "people; and much people of Israel died."),
    ("n3", NARRATOR,
     "The bites spread through the camp. And the same people who had cursed "
     "God came running back to Moses, broken."),
    # Exact KJV Numbers 21:7 — the people's confession.
    ("p2", SCRIPTURE,
     "We have sinned, for we have spoken against the LORD, and against thee; "
     "pray unto the LORD, that he take away the serpents from us."),
    ("n4", NARRATOR,
     "So Moses prayed for the people who had just turned on him. And the LORD "
     "answered — but not the way anyone expected."),
    # Exact KJV Numbers 21:8 — the LORD to Moses (Jehovah; green, not red).
    ("g1", GOD,
     "Make thee a fiery serpent, and set it upon a pole: and it shall come to "
     "pass, that every one that is bitten, when he looketh upon it, shall "
     "live."),
    ("n5", NARRATOR,
     "No cure to brew. No ritual to perform. No strength left to muster. Just "
     "a shape of bronze lifted on a pole, and one thing left to do — look."),
    # Exact KJV Numbers 21:9 — the serpent of brass, the centerpiece.
    ("s2", SCRIPTURE,
     "And Moses made a serpent of brass, and put it upon a pole, and it came "
     "to pass, that if a serpent had bitten any man, when he beheld the "
     "serpent of brass, he lived."),
    ("n6", NARRATOR,
     "A dying man didn't have to earn it, or explain it, or even understand "
     "it. He only had to trust it enough to lift his eyes toward it."),
    ("n7", NARRATOR,
     "Fourteen hundred years later, Jesus reached back and picked this exact "
     "moment to explain his own cross."),
    # Exact KJV John 3:14-15 — the Son of man lifted up (Jesus's own words).
    ("j1", JESUS,
     "And as Moses lifted up the serpent in the wilderness, even so must the "
     "Son of man be lifted up: That whosoever believeth in him should not "
     "perish, but have eternal life."),
    ("card", NARRATOR,
     "The whole camp was dying, and their healing hung on a pole. All they "
     "had to do was look. Look, and live."),
]

# Homographs this build decides for itself (never auto-replaced globally).
# "live" (Num 21:8 "shall live"; card "look, and live") is the verb /lɪv/, in
# unambiguous post-"shall" / post-"and" contexts ElevenLabs Brian reads
# correctly — decided AS-IS (identity entry marks it decided, audit silence).
SPOKEN = {"live": "live"}


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
