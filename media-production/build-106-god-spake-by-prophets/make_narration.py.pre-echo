#!/usr/bin/env python3
"""Narration for build-106-god-spake-by-prophets — Hebrews 1.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

Hebrews is an epistle. The man writing it — Paul, by the traditional attribution —
is describing God, not speaking as him and certainly not as Jesus. All three red
beats were misattributed and all three move to light blue:

  jv1  Hebrews 1:1  'God, who at sundry times and in divers manners spake...'  RED -> SCRIPTURE
  jv2  Hebrews 1:2  'Hath in these last days spoken unto us by his Son'        RED -> SCRIPTURE
  jv3  Hebrews 1:3  'Who being the brightness of his glory...'                 RED -> SCRIPTURE

That is three lines out of red. Note what the old colouring did: it painted the
sentence 'God spake by the prophets' as though Jesus were saying it about himself,
which is exactly the misuse of red Cameron flagged.

THE SPLIT — Hebrews 1:5. This is the one place in the chapter where somebody other
than the writer opens his mouth, and it is the FATHER, quoting himself out of Psalm 2
and 2 Samuel 7. One verse, two speakers, alternating, so it becomes four beats:

  sv5   (scripture, blue)  'For unto which of the angels said he at any time,'
  gv5   (god, green)       'Thou art my Son, this day have I begotten thee?'
  sv5b  (scripture, blue)  'And again,'
  gv5b  (god, green)       'I will be to him a Father, and he shall be to me a Son?'

The Father naming the Son is the whole argument of Hebrews 1, and it was not in the
video at all — the chapter's climax was missing. It is now, verbatim, and green
carries who is speaking without a word of explanation on screen. All four beats sit
on S7, so this is four consecutive beats over one existing image and the cut the
viewer sees does not change. nA is a new narrator beat retelling the Father's words
in plain modern English, per the retelling rule; it also sits on S7.

All original ids kept; sv5, gv5, sv5b, gv5b and nA are the only additions. Nothing
left as paraphrase from uncertainty — Hebrews 1:1, 1:2, 1:3 and 1:5 are quoted from
the King James text as printed.

WHY-LAW: milk. God has always talked to people, and he never stopped. The green
tells the truth quietly — the voice calling him 'my Son' is the Father's.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import GOD, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "For thousands of years, God had been speaking. Never all at once. Never the whole picture. But always, patiently, reaching toward people who could barely hear him."),
    # Hebrews 1:1
    ("jv1", SCRIPTURE, "God, who at sundry times and in divers manners spake in time past unto the fathers by the prophets,"),
    ("n2", NARRATOR, "In many times, and in many different ways. To one he spoke from a bush that burned but would not burn up. To another, in fire that fell on a mountain."),
    ("n3", NARRATOR, "To one he gave words to write on a scroll in the lamplight. Another he sent to cry out in the city gate to people who mostly would not listen. A fragment here, a flash there — true, but partial."),
    ("n4", NARRATOR, "Century after century, messenger after messenger, each one carrying a piece of it. Never quite the whole. Never a face you could look full into and say, so that is what God is like."),
    ("n5", NARRATOR, "And then, after all the fragments, God did something he had never done. He stopped sending messages about himself — and came in person."),
    # Hebrews 1:2
    ("jv2", SCRIPTURE, "Hath in these last days spoken unto us by his Son."),
    # Hebrews 1:5
    ("sv5", SCRIPTURE, "For unto which of the angels said he at any time,"),
    # Hebrews 1:5 (Psalm 2:7)
    ("gv5", GOD, "Thou art my Son, this day have I begotten thee?"),
    # Hebrews 1:5
    ("sv5b", SCRIPTURE, "And again,"),
    # Hebrews 1:5 (2 Samuel 7:14)
    ("gv5b", GOD, "I will be to him a Father, and he shall be to me a Son?"),
    ("nA", NARRATOR, "Listen to who is talking there. That is the Father's own voice, saying it out loud: you are my Son. I will be a Father to him, and he will be a Son to me. God never said that to an angel. He said it to one person, and that is the person he sent."),
    ("n6", NARRATOR, "Not another prophet with another piece. The Son. God's own last and clearest word, spoken not in fire on a mountain, but in a real human life you could walk beside."),
    # Hebrews 1:3
    ("jv3", SCRIPTURE, "Who being the brightness of his glory, and the express image of his person, and upholding all things by the word of his power."),
    ("n7", NARRATOR, "The exact likeness of God, in a face you could actually look at. If you have ever wondered what God is really like — whether he is angry, or distant, or cold — the answer is not a guess. Look at Jesus. That is God, saying everything, at last."),
    ("card", NARRATOR, "For ages God spoke in fragments; then he said it all in a Son. His clearest word about himself is a warm human face inviting you in. If you want to know what God is really like, where might you start looking?"),
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
