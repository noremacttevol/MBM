#!/usr/bin/env python3
"""Narration for build-16-mary-martha — Luke 10.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

STAYED RED: the one existing red beat is Jesus in the flesh and a red-letter KJV
prints it.
  j1  Luke 10:41-42  'Martha, Martha, thou art careful and troubled about many
      things: But one thing is needful: and Mary hath chosen that good part,
      which shall not be taken away from her.'
Luke's framing -- 'And Jesus answered and said unto her' -- was already outside
the segment and is carried by n9 in the storyteller's voice, so no split was
needed here.

THE FIX THIS BUILD EXISTED FOR -- MARTHA WAS NEVER HEARD. This is a story about
a woman, and the only thing she says in it was a narrator paraphrase in white:
n8, 'Lord, don't you care that my sister has left me to do all of this work by
myself?' Lifted out verbatim as WOMAN (pink):
  w40  Luke 10:40  'Lord, dost thou not care that my sister hath left me to serve
       alone? bid her therefore that she help me.'
n7 was already the frame ('she stopped, looked at her sister... and said out
loud... exactly what she was feeling'), so it needed no trimming. n8 keeps its
original text and now works as the retelling immediately after her real words.
w40 sits on the SAME still S4 that n7 and n8 already used -- no new artwork, and
the edit the viewer sees is unchanged.

The two voices in this video are now Martha in pink and Jesus in red, answering
each other. That is the whole story, and until now the viewer heard only one side.

WOMEN, MORE: Luke 10:38-42 records only Martha speaking. Mary says nothing in
this passage -- her whole part is that she sits and listens, which is the point.
Nothing was put in Mary's mouth.

NO GREEN: no voice from heaven anywhere in Luke 10:38-42.

WHY-LAW: he never scolded the serving; he was troubled by the worry underneath
it. She did not have to earn her place near him.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, WOMAN

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "This is the little village of Bethany, just outside Jerusalem. One evening, Jesus came here to the home of two sisters, Martha and Mary, and Martha gladly welcomed him in."),
    ("n2", NARRATOR, "In that day, hosting a guest like this was a real honor, and a great deal of work. There was a meal to cook, water to carry, and a whole house to ready. Martha took all of it onto herself."),
    ("n3", NARRATOR, "So Martha threw herself into the serving. Stirring, carrying, cleaning, fixing, moving without a pause, giving this guest everything she thought he deserved."),
    ("n4", NARRATOR, "But little by little, the joy of having him there got buried under the weight of getting it all just right. Her hands stayed busy while, inside, she wound tighter and tighter."),
    ("n5", NARRATOR, "Her sister Mary had made a completely different choice. She sat down on the floor at Jesus's feet, and she simply listened to every word he said."),
    ("n6", NARRATOR, "Back then, sitting at a teacher's feet was the place a student sat, and it was not a place people expected a woman to take. Mary took it anyway. She wanted to be near him more than anything else that night."),
    ("n7", NARRATOR, "Meanwhile Martha, worn thin, finally reached her breaking point. She stopped, looked at her sister just sitting there, and said out loud, in front of everyone, exactly what she was feeling."),
    # Luke 10:40
    ("w40", WOMAN, "Lord, dost thou not care that my sister hath left me to serve alone? bid her therefore that she help me."),
    ("n8", NARRATOR, "Lord, don't you care that my sister has left me to do all of this work by myself? Tell her to get up and help me."),
    ("n9", NARRATOR, "The whole room went quiet. And Jesus answered her, not with a scolding, but with her own name, said twice, and said gently."),
    # Luke 10:41-42
    ("j1", JESUS, "Martha, Martha, thou art careful and troubled about many things: But one thing is needful: and Mary hath chosen that good part, which shall not be taken away from her."),
    ("n10", NARRATOR, "He did not scold her for serving, and he was never upset that she worked so hard. What troubled him was the worry underneath it, the anxiety that was pulling her apart. And the quiet thing Mary had chosen, just being with him, he promised no one would ever take away from her."),
    ("n11", NARRATOR, "He was not picking one sister over the other. He was telling a woman he loved that she did not have to earn her place near him by working herself ragged. She was allowed to stop, and sit, and simply be with him, the same as her sister."),
    ("n12", NARRATOR, "He never scolded the serving. He worried about the worry. That is the kind of God he is."),
    ("card", NARRATOR, "Worried and troubled about many things, or sitting down long enough to listen. Which one sounds more like your life right now?"),
]

# Homographs this build decides for itself (never auto-replaced globally).
# Cameron denial #16 (2026-07-19): "That's not how you pronounce wound".
# Here "she wound tighter" is the PAST TENSE OF WIND — /waund/, rhyming with
# "found" — not the injury /wu:nd/. Homograph, so it stays per-build (the
# global map must never force one reading of "wound" on every video).
SPOKEN = {
    "wound": "wownd",
}


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
