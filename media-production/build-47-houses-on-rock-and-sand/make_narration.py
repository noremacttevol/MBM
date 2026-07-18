#!/usr/bin/env python3
"""Generate narration audio for Story Video #47 — Houses on Rock and Sand
(Matthew 7:24-27).

Narrator: en-US-AndrewNeural — plain American, never a Multilingual model.
Jesus voice: en-US-ChristopherNeural — American, never British.

Jesus speaks ONLY exact KJV. Four lines — the whole parable is his direct speech:
  jv24 = Matt 7:24   the wise man on the rock (verse-card, sacred silence 1)
  jv25 = Matt 7:25   the storm, and "it fell not" (sacred silence 2 — the payoff)
  jv26 = Matt 7:26   the foolish man on the sand
  jv27 = Matt 7:27   the storm, and "great was the fall of it"

The two sacred silences land on the two ROCK beats (jv24, jv25) — the good news.
jv26/jv27 (the foolish man and the fall) play UNDER a soft moving bed on purpose, so
the weight stays on the rock, not the fall.

WHY-LAW: the misread is "be good or God wrecks you." The point is the opposite and
smaller and harder: BOTH men heard the same words (n2, n11) — the only difference was
that one went home and DID them. STUDY GEMS: in that land you build in the dry summer,
and the easy ground is the smooth sand of a dry riverbed — a wadi (n3, n6); the wise
man does the slow, unseen work of digging down to bedrock (n4); the winter rains turn
those dry beds into flash floods that hit BOTH houses the same (n7). The difference was
underneath, where no one could see it until the water rose (n10).

TRANSLATION LAW: after each KJV line the narrator gives only the plain meaning and
never re-quotes it. n5 says "stood without moving" not "it fell not"; n9 says "there
was nothing left" not "great was the fall".

MILK FRAMING: an invitation, never a threat. The foolish man is safe on the bank — it
is his life's work that falls, not him. Ends on the open door: build your life on his
words, and you can start with one thing this week.

NUMBER-STRESS LAW: no sentence opens with a bare number.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"
JESUS = "en-US-ChristopherNeural"

SEGMENTS = [
    # (filename, voice, rate, pitch, text) — text is BOTH spoken and captioned.
    # --- s1: the end of the sermon ---
    ("n1", NARRATOR, "-20%", "-4Hz",
     "He had been teaching all afternoon, and he ended with a story about two men and "
     "two houses. It sounds simple. It is one of the most searching things he ever "
     "said."),
    # --- s2: both men heard ---
    ("n2", NARRATOR, "-22%", "-4Hz",
     "Picture two men in that crowd. Both of them heard him. Every word. That matters, "
     "so hold onto it: both men heard exactly the same thing."),
    # --- s3: the wise man digs deep. the gem. ---
    ("n3", NARRATOR, "-22%", "-4Hz",
     "The first man goes home to build. In that country you build in the dry season, "
     "and the easy ground is the smooth, flat sand of a dry riverbed. But this man "
     "walks past the easy ground."),
    ("n4", NARRATOR, "-22%", "-4Hz",
     "He digs. Down through the loose soil, all the way to bedrock, and he lays his "
     "foundation on the stone. It is slow, hard work, and when he is done not one "
     "person will ever see it. The whole house depends on the part nobody can see."),
    # --- s4: jv24 — the wise man. SACRED SILENCE 1. ---
    ("jv24", JESUS, "-26%", "-6Hz",
     "Therefore whosoever heareth these sayings of mine, and doeth them, I will liken "
     "him unto a wise man, which built his house upon a rock."),
    # --- s5: the finished house, calm before the storm ---
    ("n5", NARRATOR, "-22%", "-4Hz",
     "His house goes up on the rock. It takes longer. And for a while, in the good "
     "weather, it does not look one bit better than any other house on the plain."),
    # --- s6: jv25 — the storm, it fell not. SACRED SILENCE 2. ---
    ("jv25", JESUS, "-26%", "-6Hz",
     "And the rain descended, and the floods came, and the winds blew, and beat upon "
     "that house; and it fell not: for it was founded upon a rock."),
    ("n6", NARRATOR, "-22%", "-4Hz",
     "The storm hit it with everything, and the house did not even move. Because of "
     "what was underneath it."),
    # --- s7: jv26 — the foolish man on the sand ---
    ("n7", NARRATOR, "-22%", "-4Hz",
     "Now the second man. He heard the very same words. But when he goes home, he "
     "builds the fast, easy way, straight down on the smooth sand, and he skips the "
     "digging altogether."),
    ("jv26", JESUS, "-26%", "-6Hz",
     "And every one that heareth these sayings of mine, and doeth them not, shall be "
     "likened unto a foolish man, which built his house upon the sand."),
    # --- s8: the finished sand house, careless ---
    ("n8", NARRATOR, "-22%", "-4Hz",
     "And here is the thing. His house looked fine. It went up faster, it stood there "
     "in the sunshine, and you could not have told the two houses apart. Not until the "
     "weather turned."),
    # --- s9: jv27 — the fall. Under music, restrained. ---
    ("jv27", JESUS, "-26%", "-6Hz",
     "And the rain descended, and the floods came, and the winds blew, and beat upon "
     "that house; and it fell: and great was the fall of it."),
    ("n9", NARRATOR, "-23%", "-4Hz",
     "The same dry riverbed became a wall of water, it tore the sand out from under "
     "the house, and there was nothing left. The man got out. But everything he had "
     "built was gone."),
    # --- s10: the morning after — the WHY ---
    ("n10", NARRATOR, "-22%", "-4Hz",
     "Two houses. One storm. One standing, one swept away. And the only difference "
     "between them was down in the foundation, where nobody could see it, until the "
     "day the water came up and asked."),
    # --- s11: frame return — the point ---
    ("n11", NARRATOR, "-22%", "-4Hz",
     "Do not miss what he is actually saying. Both men heard him. Hearing was never "
     "the thing that made the difference. The wise man is simply the one who went home "
     "and did something about what he heard."),
    # --- s12: the invitation. Milk framing. ---
    ("n12", NARRATOR, "-24%", "-4Hz",
     "That is the whole invitation. Not to admire what he said, and not to be afraid "
     "of the storm, but to build your actual life on his words, one of them at a time, "
     "starting now, while the weather is still good. The door is open, and the light "
     "is already on inside."),
    # --- closing card, read gently (Readable-Card Law) ---
    ("card", NARRATOR, "-26%", "-4Hz",
     "Everybody on that hillside heard the very same words. The one whose house stood "
     "was the one who went home and did them. What is one thing he said that you could "
     "actually go and do this week?"),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        await save_narration(text, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
