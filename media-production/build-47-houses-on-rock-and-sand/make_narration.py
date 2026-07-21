#!/usr/bin/env python3
"""Narration for build-47-houses-on-rock-and-sand — Matthew 7.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

STAYED RED, ALL FOUR. Matthew 7:24-27 is the closing parable of the Sermon on
the Mount, spoken by Jesus in the flesh, and a red-letter KJV inks every word of
it -- both houses, both storms. jv24, jv25, jv26, jv27 are verbatim and carry no
framing from Matthew, so none of them needed splitting.

NO SPLITS.

ADDED IN BLUE -- THE STILL NOBODY WAS USING. S11 is named s11-astonished.jpeg and
the original n11 never mentioned the crowd's astonishment at all; the picture was
carrying a moment the words had dropped. Matthew 7:28-29 is now lifted in as
SCRIPTURE (light blue -- that is Matthew writing, not Jesus speaking):
  s28  Matthew 7:28-29  'And it came to pass, when Jesus had ended these sayings,
       the people were astonished at his doctrine: For he taught them as one
       having authority, and not as the scribes.'
  n11a is new and retells it. n11 keeps its id, its text and its place right
  after, so nothing that references n11 outside BEATS is disturbed.

NO GREEN. Nothing in Matthew 7 is the Father or a voice from heaven.

WOMEN: Matthew 7:24-29 records no woman speaking. Nothing added; nothing
invented.

RETELLING RULE: jv24 is retold by n5, jv25 by n6, jv26 by n8, jv27 by n9, and the
new s28 by the new n11a. No two Old English blocks run back to back.

WHY-LAW: both men heard exactly the same words -- hearing was never the
difference. Milk: go home and do one of them, while the weather is still good.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "He had been teaching all afternoon, and he ended with a story about two men and two houses. It sounds simple. It is one of the most searching things he ever said."),
    ("n2", NARRATOR, "Picture two men in that crowd. Both of them heard him. Every word. That matters, so hold onto it: both men heard exactly the same thing."),
    ("n3", NARRATOR, "The first man goes home to build. In that country you build in the dry season, and the easy ground is the smooth, flat sand of a dry riverbed. But this man walks past the easy ground."),
    ("n4", NARRATOR, "He digs. Down through the loose soil, all the way to bedrock, and he lays his foundation on the stone. It is slow, hard work, and when he is done not one person will ever see it. The whole house depends on the part nobody can see."),
    # Matthew 7:24
    ("jv24", JESUS, "Therefore whosoever heareth these sayings of mine, and doeth them, I will liken him unto a wise man, which built his house upon a rock."),
    ("n5", NARRATOR, "His house goes up on the rock. It takes longer. And for a while, in the good weather, it does not look one bit better than any other house on the plain."),
    # Matthew 7:25
    ("jv25", JESUS, "And the rain descended, and the floods came, and the winds blew, and beat upon that house; and it fell not: for it was founded upon a rock."),
    ("n6", NARRATOR, "The storm hit it with everything, and the house did not even move. Because of what was underneath it."),
    ("n7", NARRATOR, "Now the second man. He heard the very same words. But when he goes home, he builds the fast, easy way, straight down on the smooth sand, and he skips the digging altogether."),
    # Matthew 7:26
    ("jv26", JESUS, "And every one that heareth these sayings of mine, and doeth them not, shall be likened unto a foolish man, which built his house upon the sand."),
    ("n8", NARRATOR, "And here is the thing. His house looked fine. It went up faster, it stood there in the sunshine, and you could not have told the two houses apart. Not until the weather turned."),
    # Matthew 7:27
    ("jv27", JESUS, "And the rain descended, and the floods came, and the winds blew, and beat upon that house; and it fell: and great was the fall of it."),
    ("n9", NARRATOR, "The same dry riverbed became a wall of water, it tore the sand out from under the house, and there was nothing left. The man got out. But everything he had built was gone."),
    ("n10", NARRATOR, "Two houses. One storm. One standing, one swept away. And the only difference between them was down in the foundation, where nobody could see it, until the day the water came up and asked."),
    # Matthew 7:28-29
    ("s28", SCRIPTURE, "And it came to pass, when Jesus had ended these sayings, the people were astonished at his doctrine: For he taught them as one having authority, and not as the scribes."),
    ("n11a", NARRATOR, "When he finished, the crowd just sat there. They had never heard anyone teach like that. Their own scholars quoted other men. This one spoke as though the words belonged to him."),
    ("n11", NARRATOR, "Do not miss what he is actually saying. Both men heard him. Hearing was never the thing that made the difference. The wise man is simply the one who went home and did something about what he heard."),
    ("n12", NARRATOR, "That is the whole invitation. Not to admire what he said, and not to be afraid of the storm, but to build your actual life on his words, one of them at a time, starting now, while the weather is still good. The door is open, and the light is already on inside."),
    ("card", NARRATOR, "Everybody on that hillside heard the very same words. The one whose house stood was the one who went home and did them. What is one thing he said that you could actually go and do this week?"),
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
