#!/usr/bin/env python3
"""Narration for build-124-love-your-enemies — Matthew 5.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

BOTH ORIGINAL RED BEATS STAY RED. jvA (Matthew 5:44) and jvB (Matthew 5:45)
are Jesus in the flesh on the mount. Nothing moved out of red.

LIFTED FROM PARAPHRASE — and this is the one that matters most here:
  jv43  Matthew 5:43  'Ye have heard that it hath been said, Thou shalt love
                       thy neighbour, and hate thine enemy.'         JESUS
jvA opens with 'But I say unto you' and there was nothing in the build for it
to answer — the 'ye have heard that it hath been said' half existed only as
narrator paraphrase inside n2. It is now spoken verbatim, and it is RED, not
green and not blue. Jesus quoting the old saying is still Jesus talking. A
red-letter KJV inks the whole of Matthew 5:43 red even though he is citing
the law. Do not let the quoted fragment tempt anyone into recolouring it.

  jv46  Matthew 5:46  'For if ye love them which love you, what reward have
                       ye? do not even the publicans the same?'      JESUS
n8 already said 'even the tax collectors managed that much' without ever
letting Jesus say it. Now he does, and n8 is the retelling.

NO RED RUNS BACK TO BACK. jv43 is deliberately separated from jvA by n2, so
the viewer hears the old rule, hears it explained, and only then gets the
turn. Order: n1, jv43, n2, jvA, n3-n6, jvB, n7, jv46, n8.

EDITS TO EXISTING NARRATOR TEXT: n2 now opens by retelling jv43 in plain
English and then continues word for word as it was, ending on 'And then Jesus
said this.' — which now hands straight into jvA exactly as it always meant
to. n7 gained a closing sentence to hand into jv46, and n8 gained an opening
sentence retelling it. Nothing else changed.

NEW BEATS REUSE EXISTING STILLS: jv43 sits on S2 with n2, jv46 sits on S9
with n7. No new artwork.

NO MIXED SEGMENTS. None of the four red beats has a narration frame in it.

NOTHING LEFT AS PARAPHRASE FROM UNCERTAINTY.

WHY-LAW: the reason given is not that the enemy deserves it. It is family
resemblance — the Father's sun rises on everybody. Milk framing, and it keeps
the beat off guilt and on likeness.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "On a green hillside above the Sea of Galilee, Jesus sat down to teach, and a whole countryside climbed up to listen. He was walking through the old sayings one at a time — you have heard it said — and then he came to the hardest one of all: what to do with an enemy."),
    # Matthew 5:43
    ("jv43", JESUS, "Ye have heard that it hath been said, Thou shalt love thy neighbour, and hate thine enemy."),
    ("n2", NARRATOR, "You have heard it said, he began — love your neighbour, and hate your enemy. Everyone on that hillside knew that old arithmetic. Love the people who love you. Keep your guard up against the ones who don't. It felt fair. It felt safe. And then Jesus said this."),
    # Matthew 5:44
    ("jvA", JESUS, "But I say unto you, Love your enemies, bless them that curse you, do good to them that hate you, and pray for them which despitefully use you, and persecute you;"),
    ("n3", NARRATOR, "Not tolerate them. Not stay out of their way. Bless. Do good. Pray. Every one of those is something you go and do — aimed straight at the person who has earned none of it. Picture a farmer whose neighbor has wronged him: the fence knocked down, the insult at the well, years of cold looks across one stone wall."),
    ("n4", NARRATOR, "He has every right to answer coldness with coldness. That is the old arithmetic, and nobody would blame him for it. Instead, when his neighbor's wall gives way in the rains, he walks over quietly and starts lifting stones."),
    ("n5", NARRATOR, "And at night, when the work is done and no one is watching, he does the thing Jesus asked that no one ever sees. By the light of his lamp, he prays for the man across the wall — not about him. For him. By name."),
    ("n6", NARRATOR, "Why would Jesus ask for something this unreasonable? He was not pretending enemies don't hurt. He gave his reason on the same hillside, and the reason changes everything."),
    # Matthew 5:45
    ("jvB", JESUS, "That ye may be the children of your Father which is in heaven: for he maketh his sun to rise on the evil and on the good, and sendeth rain on the just and on the unjust."),
    ("n7", NARRATOR, "Look at the sky, he was saying. Your Father's sun came up this morning over every field in the valley — the kind man's and the cruel man's alike. His rain waters both. Loving an enemy is not unnatural. In this family, it is the resemblance. And then he asked the question that leaves none of us out."),
    # Matthew 5:46
    ("jv46", JESUS, "For if ye love them which love you, what reward have ye? do not even the publicans the same?"),
    ("n8", NARRATOR, "If you only love the people who love you back, he asked, what credit is that? Even the tax collectors manage that much. The love that marks you as your Father's child is the love that is not owed. And sometimes, slowly, it wins what coldness never could: the wall between two houses becomes the place where they meet."),
    ("card", NARRATOR, "Jesus never said your enemy deserves it. He said this is how the family likeness shows. Who is the hardest person in your life to bless? What might change if, tonight, you prayed for them — by name?"),
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
