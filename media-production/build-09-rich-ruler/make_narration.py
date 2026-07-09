#!/usr/bin/env python3
"""Generate narration audio for Story Video #9 — The Rich Young Ruler
(Mark 10:17-22 — the ending stays in sorrow, per the pack's directive).
Narrator: en-US-AndrewNeural — plain American, never Multilingual.
Jesus voice: en-US-ChristopherNeural — American, never British.
Jesus speaks ONLY exact KJV: Mark 10:21 (fetched from bible-api.com, not
hand-typed — the pack's "take up THY cross" corrected to the real KJV
"take up THE cross").
Pre-flighted on paper per PRODUCTION-BIBLE §4b — see PREFLIGHT.md.
vv23-27 consciously excluded per the pack: the young man's story ends at
v22 and the ending must not be softened.
Translation Law: no narrator line echoes KJV wording; modern meaning only.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    # n0 — the run (s1 clip). v17 + the WHY-gem about running.
    ("n0", NARRATOR, "-20%", "-4Hz",
     "Jesus was setting out on a journey when a young man came running "
     "down the road after him. Running. You need to understand what "
     "that looked like. This man was wealthy — fine robes, gold rings, "
     "a name people knew. Men like that did not run in public. It was "
     "beneath them. He ran anyway, in front of everyone, and dropped "
     "to his knees in the dust at Jesus's feet."),
    # n1 — the question + the record (s2). v17b, v19-20 paraphrased modern.
    ("n1", NARRATOR, "-20%", "-4Hz",
     "He asked the question he had been carrying, maybe his whole "
     "life. Good teacher — what do I have to do to live forever with "
     "God? Jesus pointed him to the commandments. Don't cheat anyone. "
     "Don't steal. Don't lie. Honor your father and your mother. And "
     "the young man answered: Teacher, I have kept every one of them "
     "since I was a boy. And here is the thing. He meant it. This "
     "was not a proud man showing off. This was a student who had "
     "done all the homework, kneeling in the dirt, asking if it was "
     "enough."),
    # n2 — the look (s3). v21a. Held beat; music thins under this.
    ("n2", NARRATOR, "-24%", "-4Hz",
     "Mark writes what happened next in five words. Jesus, looking at "
     "him, loved him. Of all the people in Mark's story, this is the "
     "one he says it about, straight out. Jesus looked at this man — "
     "his sincerity, his gold rings, his hope — and loved him. And "
     "then, with love in his voice, he said the hardest sentence in "
     "the book."),
    # J1 — exact KJV Mark 10:21. Slow, warm, in full silence.
    ("j1", JESUS, "-27%", "-6Hz",
     "One thing thou lackest: go thy way, sell whatsoever thou hast, "
     "and give to the poor, and thou shalt have treasure in heaven: "
     "and come, take up the cross, and follow me."),
    # n3 — translation bridge (s4 inserts). Translation Law: modern meaning.
    ("n3", NARRATOR, "-24%", "-4Hz",
     "You're missing one thing. Not one more rule. One thing standing "
     "between you and God. Sell what you have. Give it to the people "
     "who have nothing. And then — come, follow me. Hear that last "
     "part. It was an invitation. The same words Jesus used to call "
     "Peter, and Andrew, and James, and John. He was being invited "
     "into the inner circle. It just came wrapped in the one thing "
     "this man could not put down."),
    # n4 — the turn + the walk away (s5 → s6 clip). v22.
    ("n4", NARRATOR, "-22%", "-4Hz",
     "His face fell. And he walked away grieved — because he was very "
     "rich. Notice what the text does not say. It does not say he "
     "stopped believing. It does not say he argued. He grieved — "
     "because he believed every word, and the price was the thing he "
     "loved most. He turned around, and he walked back down that road "
     "toward everything he owned."),
    # n5 — THE PEAK (s7). Music dies at the start of this and never returns.
    ("n5", NARRATOR, "-24%", "-4Hz",
     "And Jesus let him go. He did not lower the bar. He did not "
     "soften the terms. He did not chase him down the road. He stood "
     "there, and he watched him walk away — and he loved him the "
     "whole time."),
    # n6 — the coda, in the silence (s8).
    ("n6", NARRATOR, "-26%", "-4Hz",
     "The road emptied. The sun went down. And the story just ends "
     "there — Mark leaves it exactly that sad, on purpose. Sit with "
     "it. A love that will not force you. Is that weakness — or is it "
     "the deepest respect you have ever been shown?"),
    # n7 — the closing card, read aloud gently (Readable-Card Law).
    ("n7", NARRATOR, "-26%", "-4Hz",
     "Is there something you already know — quietly — that stands "
     "between you and fully following what you believe?"),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
