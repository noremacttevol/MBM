#!/usr/bin/env python3
"""Generate narration audio for Story Video #20 — The Good Samaritan
(Luke 10:25-37).

Narrator: en-US-AndrewNeural — plain American, never a Multilingual model.
Jesus voice: en-US-ChristopherNeural — American, never British.
Jesus speaks ONLY exact KJV: Luke 10:36 (j1) and Luke 10:37 (j2).

CAPTIONS ARE VERBATIM (Cameron, 2026-07-11): build.py imports these SEGMENTS
and word-wraps each text as the on-screen caption, so every spoken word is on
the screen. After each KJV Jesus line the narrator gives ONLY the plain modern
meaning and never re-quotes the KJV words (Translation Law).

A parable told BY Jesus: he is the narrating voice and appears only in the
bookend shots as a seated storyteller seen from behind (STILLS-ONLY, Law E;
Jesus face-never, #18). Every other character is shown fully.

WHY-LAW: the script explains why the crowd despised Samaritans and why making
one the hero was shocking — a viewer with zero Bible background can say the
point in one sentence. STUDY-GEMS woven in small: the Jerusalem-to-Jericho road
was a notorious robber road; the priest/Levite may have feared a bloody body
would make them ceremonially unclean; two pence was about two days' wages.
NUMBER-STRESS: "two silver coins" never opens a sentence (Andrew under-stresses
a sentence-initial "two" into "to").
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text) — text is BOTH spoken and captioned.
    # --- Shot 1: the scholar's trap question ---
    ("n1", NARRATOR, "-20%", "-4Hz",
     "A scholar of the law stood up to test Jesus, and asked him, who is my "
     "neighbor. It sounds humble. It was not."),
    ("n2", NARRATOR, "-22%", "-4Hz",
     "It was the kind of question you ask when you are hoping the answer has "
     "limits. He wanted a line drawn, so he could know exactly who he was "
     "allowed to ignore."),
    # --- Shot 2: the man left half dead on the Jericho road ---
    ("n3", NARRATOR, "-22%", "-4Hz",
     "Jesus answered with a story. A man was traveling the steep, lonely road "
     "down to Jericho, a road so full of robbers that people called it the Way "
     "of Blood."),
    ("n4", NARRATOR, "-22%", "-4Hz",
     "Robbers were exactly what he found. They stripped him, beat him, and "
     "left him half dead in the dust beside the road."),
    # --- Shot 3: the priest and the Levite cross over ---
    ("n5", NARRATOR, "-22%", "-4Hz",
     "A priest came down that same road, saw the man, and crossed to the far "
     "side. Then a temple assistant came, looked, and also crossed over."),
    ("n6", NARRATOR, "-22%", "-4Hz",
     "These were the religious professionals, the men who knew the law best. "
     "Maybe they feared a bloody body would make them unclean for the temple. "
     "Either way, they kept their distance."),
    # --- Shot 4: the Samaritan, moved with compassion (the peak) ---
    ("n7", NARRATOR, "-22%", "-4Hz",
     "Then a Samaritan came down the road. And the crowd listening to Jesus "
     "was raised to despise Samaritans. Different blood, wrong worship, an old "
     "hatred hundreds of years deep."),
    ("n8", NARRATOR, "-22%", "-4Hz",
     "A Samaritan was the last man in the world they expected to be the hero "
     "of the story."),
    ("n9", NARRATOR, "-25%", "-5Hz",
     "He saw the beaten stranger. And the text says he was moved with "
     "compassion."),
    # --- Shot 5: bound his wounds, put him on his own animal ---
    ("n10", NARRATOR, "-22%", "-4Hz",
     "He knelt down in the dirt beside a man his people were supposed to hate. "
     "He cleaned and bound the wounds, lifted him onto his own animal, and "
     "walked beside him on foot."),
    # --- Shot 6: the inn, the payment, the promise to return ---
    ("n11", NARRATOR, "-22%", "-4Hz",
     "He brought him to an inn and cared for him through the night. In the "
     "morning he pressed two silver coins into the innkeeper's hand, about two "
     "days wages, and said, take care of him."),
    ("n12", NARRATOR, "-22%", "-4Hz",
     "And whatever more it costs, when I come back, I will repay you myself. He "
     "did not just help and move on. He tied his own name to a stranger's "
     "recovery."),
    # --- Shot 7: Jesus turns the question around (KJV j1) ---
    ("n13", NARRATOR, "-22%", "-4Hz",
     "Then Jesus turned the scholar's own question back on him, and asked which "
     "of the three men had been the neighbor."),
    ("j1", JESUS, "-26%", "-6Hz",
     "Which now of these three, thinkest thou, was neighbour unto him that "
     "fell among the thieves?"),
    ("n14", NARRATOR, "-22%", "-4Hz",
     "The scholar could not even say the word Samaritan. He answered, the one "
     "who showed mercy. Jesus had flipped the whole question. Not who counts "
     "as my neighbor, but which of them acted like one."),
    # --- Shot 8: go and do likewise (KJV j2), the sending ---
    ("j2", JESUS, "-25%", "-6Hz",
     "Go, and do thou likewise."),
    ("n15", NARRATOR, "-24%", "-4Hz",
     "Stop asking who you are allowed to walk past. Go, and be the neighbor. "
     "That is how good he is. He will not even let you keep score."),
    # --- closing card, read gently (Readable-Card Law) ---
    ("card", NARRATOR, "-26%", "-4Hz",
     "Everyone finds themselves somewhere on that road. Where are you on it "
     "right now?"),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        await save_narration(text, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
