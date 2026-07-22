#!/usr/bin/env python3
"""Narration for build-164-unity-of-faith — Ephesians 4.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

Ephesians is an epistle — Paul writing. A red-letter King James Bible prints no
red in Ephesians 4. Both red beats move to SCRIPTURE (light blue):
  kv11  Ephesians 4:11  'And he gave some, apostles...'                   RED -> SCRIPTURE
  kv13  Ephesians 4:13  'Till we all come in the unity of the faith...'   RED -> SCRIPTURE

kv11's subject is Christ — 'he gave' — but Paul is the one saying it, and the
verse is about Christ rather than from him. Same error as build-163.

No mixed segments, nothing split.

ADDED: s14 lifts Ephesians 4:14 out of n5's paraphrase. n5 was describing the
tossed-about children image in modern English while the actual verse — one of
the most vivid lines Paul wrote — went unheard. It sits on S7, the still that
n5 was already using, so no new artwork is needed, and n5 now functions as the
retelling immediately after it.

WHY-LAW: milk. The study gem in n6 is left exactly as written — if the gifts
were given until we ALL come to the unity of the faith, and we plainly have
not, then they were never meant to stop. That is stated as a reading of Paul's
own sentence, not as a claim about any church.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "When the risen Lord returned to heaven, he did not leave his church leaderless and on its own. From above, he poured out gifts on his people — and the greatest of those gifts were living leaders, given to shepherd and to teach."),
    # Ephesians 4:11
    ("kv11", SCRIPTURE, "And he gave some, apostles; and some, prophets; and some, evangelists; and some, pastors and teachers;"),
    ("n2", NARRATOR, "He gave them for a reason. Their whole calling was to mend and mature the ordinary believers — to do the work of the ministry, and to build up the body until it stood strong and whole."),
    ("n3", NARRATOR, "So the people were never meant to be a scattered crowd. Taught and strengthened, they were knit together, growing closer, becoming one body that could bear one another up."),
    ("n4", NARRATOR, "And there was a destination in view. All of them were being drawn toward the same place — one shared faith, one true knowledge of the Son of God, a people grown at last into full and finished maturity."),
    # Ephesians 4:13
    ("kv13", SCRIPTURE, "Till we all come in the unity of the faith, and of the knowledge of the Son of God, unto a perfect man, unto the measure of the stature of the fulness of Christ:"),
    # Ephesians 4:14
    ("s14", SCRIPTURE, "That we henceforth be no more children, tossed to and fro, and carried about with every wind of doctrine, by the sleight of men, and cunning craftiness, whereby they lie in wait to deceive;"),
    ("n5", NARRATOR, "Paul set the opposite right beside it. Without that steady leading, believers stay children — pushed back and forth, carried off by every new wind of teaching, easy prey for clever men who lie in wait to fool them."),
    ("n6", NARRATOR, "Here is the quiet study gem. If those leaders were given until we ALL arrive at that unity, and the church has plainly not arrived yet, then the gifts were never meant to be temporary. His people still need apostles and prophets to keep them from drifting."),
    ("n7", NARRATOR, "And that is where it leaves you. You were never meant to grow up alone, or to be blown about by whatever is newest. You are meant to grow up in this, together, into one settled faith. When he offers you a place in it, will you come and grow?"),
    ("card", NARRATOR, "The risen Lord gave his church apostles and prophets, pastors and teachers — to build his people up until they all come to one faith and full maturity. When he offers you a place in it, will you come and grow?"),
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
