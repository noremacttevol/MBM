#!/usr/bin/env python3
"""Generate narration audio for Story Video #33 — The Sheep and the Goats
(Matthew 25:31-46).

Narrator: en-US-AndrewNeural — plain American, never a Multilingual model.
Jesus voice: en-US-ChristopherNeural — American, never British.
Jesus speaks ONLY exact KJV: the King's welcome Matthew 25:34-36 (j1) and the
reveal Matthew 25:40 (j2). (The King / Son of man in the scene IS Jesus, so the
Jesus voice carries his words; he is kept FULLY OFF-SCREEN in the art.)

CAPTIONS ARE VERBATIM. After each KJV line the narrator gives ONLY the plain
modern meaning and never re-quotes the KJV words (Translation Law).

Stills-only (Law E): NO Jesus figure on screen — the King is voice + KJV only.
The art shows a shepherd dividing his flock (from behind / at a distance, the
simile) and, above all, the ACTS OF MERCY and the people who did them.

MILK: this is a judgment scene with a hard side (the goats, the punishment). We
keep the LIGHT on the heart THE-200 names: "ye did it unto me — God hides in the
needy." The good news is that Jesus so identifies with the hungry, the stranger,
the sick, the imprisoned, and the overlooked that every small kindness to them is
kindness to HIM — and the righteous did it by reflex, without keeping score,
surprised to learn Whom they had served. The goats' side is stated gently (they
were waiting for a King on a throne and walked past him), never dwelt on
luridly; the close lands on grace and on the person in front of you.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text) — text is BOTH spoken and captioned.
    # --- s1: the King separates the nations, like a shepherd ---
    ("n1", NARRATOR, "-20%", "-4Hz",
     "Near the end, Jesus told his friends what the last day would really be "
     "like. He said the King would gather all the nations in front of him and "
     "separate them into two groups."),
    ("n2", NARRATOR, "-22%", "-4Hz",
     "Like a shepherd at evening quietly dividing his flock, the sheep to one "
     "side and the goats to the other. And what decided which side you were on "
     "was not at all what people expect."),
    # --- s2: the welcome (KJV j1 = Matthew 25:34-36) ---
    ("n3", NARRATOR, "-22%", "-4Hz",
     "To the first group, the ones he welcomed in, the King said this."),
    ("j1", JESUS, "-25%", "-6Hz",
     "Come, ye blessed of my Father, inherit the kingdom prepared for you from "
     "the foundation of the world: For I was an hungred, and ye gave me meat: I "
     "was thirsty, and ye gave me drink: I was a stranger, and ye took me in: "
     "Naked, and ye clothed me: I was sick, and ye visited me: I was in prison, "
     "and ye came unto me."),
    # --- s3: the plain meaning of the list ---
    ("n4", NARRATOR, "-22%", "-4Hz",
     "You fed me when I was hungry, he said. You gave me water when I was "
     "thirsty. You took me in when I was a stranger. You clothed me, you sat "
     "with me when I was sick, you came to me when I was locked away."),
    # --- s4: the righteous are confused ---
    ("n5", NARRATOR, "-22%", "-4Hz",
     "And here is the beautiful part. The good people are confused. They say, "
     "Lord, when did we ever see you hungry, or thirsty, or sick, or in prison? "
     "They do not even remember doing anything special. They just helped whoever "
     "was in front of them."),
    # --- s5: they were not keeping score ---
    ("n6", NARRATOR, "-22%", "-4Hz",
     "They were not keeping score. They were not trying to earn anything. "
     "Kindness was simply their reflex. And then the King tells them the secret "
     "behind all of it."),
    # --- s6: the reveal (KJV j2 = Matthew 25:40), the least ---
    ("j2", JESUS, "-26%", "-6Hz",
     "Verily I say unto you, Inasmuch as ye have done it unto one of the least "
     "of these my brethren, ye have done it unto me."),
    ("n7", NARRATOR, "-23%", "-4Hz",
     "He was in them the whole time. Every hungry person, every stranger, every "
     "sick and forgotten and locked-away person, was him, wearing a disguise."),
    # --- s7: the ones who missed him, and the good news ---
    ("n8", NARRATOR, "-22%", "-4Hz",
     "The others missed him for the very same reason. They were waiting to serve "
     "a King on a throne, and they walked right past him a hundred times, "
     "because he did not look like a King. He looked like someone who needed "
     "help."),
    ("n9", NARRATOR, "-24%", "-4Hz",
     "That is how good he is. He did not hide himself behind something "
     "impressive. He hid in the people easiest to overlook, so that plain, "
     "ordinary kindness would always reach him. So when someone small and needy "
     "stands in front of you, that is not an interruption. It might be him."),
    # --- closing card, read gently (Readable-Card Law) ---
    ("card", NARRATOR, "-26%", "-4Hz",
     "He is hidden in the person in front of you who needs help. Will you show "
     "him a kindness today?"),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        await save_narration(text, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
