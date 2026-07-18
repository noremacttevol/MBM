#!/usr/bin/env python3
"""Narration for build-120-job-from-whirlwind — Job 38.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

Both red beats - 'Where wast thou when I laid the foundations of the earth?' and
'Canst thou bind the sweet influences of Pleiades' - are God speaking out of the
whirlwind in Job 38. Old Testament, so a red-letter KJV prints them black. They become
GOD (green). Nothing in this build is `jesus`.

Added one more from the same speech, jv387, Job 38:7 - 'When the morning stars sang
together' - because still S8 is literally named the-morning-stars and the video was
not saying the line the picture was painted for.

JOB'S OWN REPLIES LIFTED OUT OF PARAPHRASE (all SCRIPTURE - Job is a man, not Deity):
  s404  Job 40:4-5  'Behold, I am vile; what shall I answer thee?...' - his first
                    reply, missing entirely
  s425  Job 42:5    'I have heard of thee by the hearing of the ear: but now mine eye
                    seeth thee.' This was sitting inside narrator beat n7 as a
                    half-quote in the narrator's voice. It is the last line of the
                    argument and the whole point of the book. Now verbatim.
  s121  Job 1:21    'the LORD gave, and the LORD hath taken away; blessed be the name
                    of the LORD' - what he actually said when it all went
  s1925 Job 19:25   'I know that my redeemer liveth' - the hope underneath the grief

LEFT OUT ON PURPOSE:
  Job 42:6 ('Wherefore I abhor myself, and repent in dust and ashes') - verbatim and
  correct, but it turns the ending toward self-loathing when the point of the ending is
  that God came near. Left off so 42:5 lands clean.
  Job 2:9, Job's wife - 'curse God, and die' - is a woman the Bible records speaking,
  and I checked for her as instructed. Left out: it is the bleakest line in the book,
  no still supports it, and it would pull a comfort video toward despair. Flagging it
  so the decision is visible rather than an oversight.

MILK FRAMING: God never answers the why. He answers with himself, and that is what the
grief actually needed. Nothing here argues about the problem of evil.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import GOD, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "Job was a good man — honest, generous, devoted to God — and for most of his life that goodness and a happy, prosperous home went together."),
    ("n2", NARRATOR, "And then, in a single devastating stretch, it was all taken. His wealth, his health, and — most unbearable of all — his children. One of the oldest, hardest questions in the world landed on the best man in it: why do good people suffer? And this is what he said on the day it happened."),
    # Job 1:21
    ("s121", SCRIPTURE, "Naked came I out of my mother's womb, and naked shall I return thither: the LORD gave, and the LORD hath taken away; blessed be the name of the LORD."),
    ("n2b", NARRATOR, "I came into this world with nothing and I will leave with nothing. God gave it and God has taken it, and I will bless him anyway. He is not calm when he says it. He has just torn his coat and shaved his head. He is wrecked, and still holding on."),
    ("n3", NARRATOR, "He sat down in the ashes, sick and broken, and he did not pretend to be all right. He grieved out loud. And scripture never once scolds him for it."),
    ("n4", NARRATOR, "His friends came, and at first they simply sat with him — which was the best thing they did. Then they started explaining. You must have sinned, they said. This must be your fault. Their tidy answers only deepened the wound."),
    ("n5", NARRATOR, "But Job would not accept easy lies about God or about himself. He did something braver than pretending. He took his anguish straight to God and demanded an answer — and then, in the middle of it, he said this."),
    # Job 19:25
    ("s1925", SCRIPTURE, "For I know that my redeemer liveth, and that he shall stand at the latter day upon the earth."),
    ("n5b", NARRATOR, "I know my redeemer is alive, he says, and one day he will stand right here on this earth. That is a man in the ashes with nothing left, saying it out loud. He does not understand a thing that is happening to him, and he still knows who is coming."),
    ("n6", NARRATOR, "And God answered — though not in the way anyone expected. Out of a great whirlwind, the Maker of everything finally spoke."),
    # Job 38:4
    ("jvA", GOD, "Where wast thou when I laid the foundations of the earth? declare, if thou hast understanding."),
    ("n6b", NARRATOR, "Where were you when I laid the foundations of the earth? It sounds like a rebuke, and it is not. God is doing something gentler than that. He is taking a man who has shrunk down to the size of his own pain, and slowly widening the room."),
    # Job 38:7
    ("jv387", GOD, "When the morning stars sang together, and all the sons of God shouted for joy."),
    ("n7a", NARRATOR, "The morning stars sang together, and all the sons of God shouted for joy. That is God describing the day the world was made — and it is not a lecture about power. It is a memory, and it is full of gladness."),
    # Job 38:31
    ("jvB", GOD, "Canst thou bind the sweet influences of Pleiades, or loose the bands of Orion?"),
    ("n7b", NARRATOR, "Can you tie up the Pleiades, God asks, or unfasten Orion's belt? On and on it goes — the sea, the snow, the wild donkey, the horse, the hawk. Chapter after chapter of a world far bigger and stranger and kinder than the tidy little courtroom Job's friends had built."),
    # Job 40:4-5
    ("s404", SCRIPTURE, "Behold, I am vile; what shall I answer thee? I will lay mine hand upon my mouth. Once have I spoken; but I will not answer: yea, twice; but I will proceed no further."),
    ("n7", NARRATOR, "I have nothing to say, Job answers. I am putting my hand over my mouth. I have said my piece and I will not say it again. Not beaten — quieted. God never explained why. Instead he showed Job the sea and the stars and the wild goodness of a world Job could never have made or held. And somehow it was enough."),
    # Job 42:5
    ("s425", SCRIPTURE, "I have heard of thee by the hearing of the ear: but now mine eye seeth thee."),
    ("n7c", NARRATOR, "I had only ever heard about you, Job says. Now I have seen you with my own eyes. That is the ending. Not because he got his answer, but because he got God himself."),
    ("n8", NARRATOR, "The suffering was never fully explained — not to Job, and not to us. But Job was no longer alone in it. The God he thought had abandoned him had come near, and that nearness was the answer his grief actually needed."),
    ("card", NARRATOR, "Job's comfort was never a reason for his pain. It was a Person who showed up in it. If you are in the ashes right now, the promise is not a tidy explanation — it is that God draws near to the broken. Where do you most need him to show up?"),
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
