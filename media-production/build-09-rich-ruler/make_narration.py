#!/usr/bin/env python3
"""Narration for build-09-rich-ruler — Mark 10.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

Mark 10:17-22. j1 is Jesus in the flesh and stays RED. The rich young ruler
himself never got to speak - both of his lines were narrator paraphrase and are now
SCRIPTURE (blue), because he is a man in the story, not Jesus:
  s17  Mark 10:17  'Good Master, what shall I do that I may inherit eternal life?'
  s20  Mark 10:20  'Master, all these have I observed from my youth.'
n0, n3 and n4 were single audio files spread across two different stills by the old
template; each is split at the caption boundary the old build already used, so the
pictures and the edit are unchanged (n0b, n3b, n4b).
n7 is the closing card and keeps its id.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "Jesus was setting out on a journey when a young man came running down the road after him. Running. You need to understand what that looked like."),
    ("n0b", NARRATOR, "This man was wealthy — fine robes, gold rings, a name people knew. Men like that did not run in public. It was beneath them. He ran anyway, in front of everyone, and dropped to his knees in the dust at Jesus's feet."),
    # Mark 10:17
    ("s17", SCRIPTURE, "Good Master, what shall I do that I may inherit eternal life?"),
    ("n1", NARRATOR, "He asked the question he had been carrying, maybe his whole life. Good teacher — what do I have to do to live forever with God? Jesus pointed him to the commandments. Don't cheat anyone. Don't steal. Don't lie. Honor your father and your mother. And the young man answered: Teacher, I have kept every one of them since I was a boy. And here is the thing. He meant it. This was not a proud man showing off. This was a student who had done all the homework, kneeling in the dirt, asking if it was enough."),
    # Mark 10:20
    ("s20", SCRIPTURE, "Master, all these have I observed from my youth."),
    ("n2", NARRATOR, "Mark writes what happened next in five words. Jesus, looking at him, loved him. Of all the people in Mark's story, this is the one he says it about, straight out. Jesus looked at this man — his sincerity, his gold rings, his hope — and loved him. And then, with love in his voice, he said the hardest sentence in the book."),
    # Mark 10:21
    ("j1", JESUS, "One thing thou lackest: go thy way, sell whatsoever thou hast, and give to the poor, and thou shalt have treasure in heaven: and come, take up the cross, and follow me."),
    ("n3", NARRATOR, "You're missing one thing. Not one more rule. One thing standing between you and God. Sell what you have. Give it to the people who have nothing. And then — come, follow me."),
    ("n3b", NARRATOR, "Hear that last part. It was an invitation. The same words Jesus used to call Peter, and Andrew, and James, and John. He was being invited into the inner circle. It just came wrapped in the one thing this man could not put down."),
    ("n4", NARRATOR, "His face fell. And he walked away grieved — because he was very rich. Notice what the text does not say. It does not say he stopped believing. It does not say he argued."),
    ("n4b", NARRATOR, "He grieved — because he believed every word, and the price was the thing he loved most. He turned around, and he walked back down that road toward everything he owned."),
    ("n5", NARRATOR, "And Jesus let him go. He did not lower the bar. He did not soften the terms. He did not chase him down the road. He stood there, and he watched him walk away — and he loved him the whole time."),
    ("n6", NARRATOR, "The road emptied. The sun went down. And the story just ends there — Mark leaves it exactly that sad, on purpose. Sit with it. A love that will not force you. Is that weakness — or is it the deepest respect you have ever been shown?"),
    ("n7", NARRATOR, "Is there something you already know — quietly — that stands between you and fully following what you believe?"),
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
