#!/usr/bin/env python3
"""Narration for Story Video #16 — Mary and Martha (Luke 10:38-42).

PHASE-1 STILLS-ONLY build. Two-Voice Law: narrator modern (en-US-AndrewNeural),
Jesus speaks ONLY exact KJV (en-US-ChristopherNeural). Martha's outburst stays
with the narrator, modern (per the production pack).

Pre-flight laws honored:
 - Full story through the final verse (10:38-42), with the WHY made plain.
 - Translation Law: the narrator NEVER re-quotes Jesus's KJV words. The bridge
   after j1 explains the meaning without echoing "careful and troubled" / "one
   thing is needful" / "good part".
 - Number/homophone stress: no sentence opens with a bare number word.
 - Captions are VERBATIM: build.py uses each segment's exact text on screen.

Jesus line j1 = Luke 10:41-42, verified char-for-char against the pack /
PAIRING-LIST.md ("thou art careful and troubled about many things").
"""
import asyncio
import edge_tts

NAR = "en-US-AndrewNeural"        # plain American — never a Multilingual model
JES = "en-US-ChristopherNeural"   # American. Never a British voice.

# (filename, voice, rate, pitch, text)   text == the on-screen caption, verbatim
SEGMENTS = [
    # --- s1: the guest arrives ---
    ("n1", NAR, "-15%", "-4Hz",
     "This is the little village of Bethany, just outside Jerusalem. One "
     "evening, Jesus came here to the home of two sisters, Martha and Mary, and "
     "Martha gladly welcomed him in."),
    ("n2", NAR, "-15%", "-4Hz",
     "In that day, hosting a guest like this was a real honor, and a great deal "
     "of work. There was a meal to cook, water to carry, and a whole house to "
     "ready. Martha took all of it onto herself."),
    # --- s2: Martha at full speed ---
    ("n3", NAR, "-15%", "-4Hz",
     "So Martha threw herself into the serving. Stirring, carrying, cleaning, "
     "fixing, moving without a pause, giving this guest everything she thought "
     "he deserved."),
    ("n4", NAR, "-16%", "-4Hz",
     "But little by little, the joy of having him there got buried under the "
     "weight of getting it all just right. Her hands stayed busy while, inside, "
     "she wound tighter and tighter."),
    # --- s3: Mary at his feet ---
    ("n5", NAR, "-15%", "-4Hz",
     "Her sister Mary had made a completely different choice. She sat down on "
     "the floor at Jesus's feet, and she simply listened to every word he "
     "said."),
    ("n6", NAR, "-16%", "-4Hz",
     "Back then, sitting at a teacher's feet was the place a student sat, and "
     "it was not a place people expected a woman to take. Mary took it anyway. "
     "She wanted to be near him more than anything else that night."),
    # --- s4: worn thin, she speaks (Martha's line stays modern, narrator) ---
    ("n7", NAR, "-16%", "-4Hz",
     "Meanwhile Martha, worn thin, finally reached her breaking point. She "
     "stopped, looked at her sister just sitting there, and said out loud, in "
     "front of everyone, exactly what she was feeling."),
    ("n8", NAR, "-15%", "-4Hz",
     "Lord, don't you care that my sister has left me to do all of this work by "
     "myself? Tell her to get up and help me."),
    # --- s5: her name, twice, gently (the money shot) ---
    ("n9", NAR, "-16%", "-4Hz",
     "The whole room went quiet. And Jesus answered her, not with a scolding, "
     "but with her own name, said twice, and said gently."),
    ("j1", JES, "-21%", "-6Hz",
     "Martha, Martha, thou art careful and troubled about many things: But one "
     "thing is needful: and Mary hath chosen that good part, which shall not be "
     "taken away from her."),
    ("n10", NAR, "-16%", "-4Hz",
     "He did not scold her for serving, and he was never upset that she worked "
     "so hard. What troubled him was the worry underneath it, the anxiety that "
     "was pulling her apart. And the quiet thing Mary had chosen, just being "
     "with him, he promised no one would ever take away from her."),
    # --- s6: two sisters in the lamplight ---
    ("n11", NAR, "-16%", "-4Hz",
     "He was not picking one sister over the other. He was telling a woman he "
     "loved that she did not have to earn her place near him by working herself "
     "ragged. She was allowed to stop, and sit, and simply be with him, the "
     "same as her sister."),
    ("n12", NAR, "-17%", "-4Hz",
     "He never scolded the serving. He worried about the worry. That is the "
     "kind of God he is."),
    # --- closing card (read aloud gently) ---
    ("card", NAR, "-17%", "-4Hz",
     "Worried and troubled about many things, or sitting down long enough to "
     "listen. Which one sounds more like your life right now?"),
]


# SPOKEN overrides: text sent to the TTS instead of the caption text, to correct a
# heteronym the neural voice reads wrong. The ON-SCREEN caption is unchanged
# (build.py captions from SEGMENTS index 4); only the spoken audio uses these.
#   n4: edge-tts reads bare "wound" as the injury (/wuːnd/). Here it is the past
#   tense of "to wind" (/waʊnd/, "wound up"). "waund" forces that pronunciation.
SPOKEN = {
    "n4": "But little by little, the joy of having him there got buried under the "
          "weight of getting it all just right. Her hands stayed busy while, inside, "
          "she waund tighter and tighter.",
}


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        spoken = SPOKEN.get(name, text)
        tts = edge_tts.Communicate(spoken, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
