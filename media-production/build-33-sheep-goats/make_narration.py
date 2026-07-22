#!/usr/bin/env python3
"""Narration for build-33-sheep-goats — Matthew 25.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

STAYED RED: both existing red beats are Jesus in the flesh, and a red-letter KJV
prints all of Matthew 25:31-46 red -- the whole passage is one unbroken speech of his
to the disciples on the Mount of Olives, King and sheep and goats alike.
  j1  Matthew 25:34-36  'Come, ye blessed of my Father, inherit the kingdom prepared
      for you from the foundation of the world: For I was an hungred, and ye gave me
      meat...'   verified verbatim, three verses running contiguously.
  j2  Matthew 25:40    'Verily I say unto you, Inasmuch as ye have done it unto one of
      the least of these my brethren, ye have done it unto me.'
Neither moves. There is no evangelist framing anywhere inside this passage to split
out -- Matthew's last framing line is back at 25:31, before the build starts.

THE BIG ADD -- THE RIGHTEOUS WERE NEVER HEARD. The heart of this story is that the
people being welcomed in do not recognise their own kindness, and their bewildered
question was sitting entirely inside narrator paraphrase in n5, spoken in white. It is
Jesus's own words -- inside his parable, the characters' lines are his -- so it is red,
not blue, and it is lifted out verbatim on the SAME still n5 already used:
  j37  Matthew 25:37-39  'Lord, when saw we thee an hungred, and fed thee? or thirsty,
       and gave thee drink? When saw we thee a stranger, and took thee in? or naked,
       and clothed thee? Or when saw we thee sick, or in prison, and came unto thee?'
       -- three verses running contiguously, minus only Matthew's 'Then shall the
       righteous answer him, saying,' at the head of 25:37. n5 keeps its text and now
       lands as the retelling directly behind it.
This is the beat the video was missing. j2's answer now arrives as a real answer to a
question the viewer has actually heard asked.

ALSO ADDED RED. The opening image was paraphrase only:
  j32  Matthew 25:32  'And before him shall be gathered all nations: and he shall
       separate them one from another, as a shepherd divideth his sheep from the goats:'
       -- placed on S1 between n1 and n2, so n2 keeps its text and becomes the
       retelling. Red lands on S1, S2, S4 and S6, each with a narrator retelling after.

LEFT AS PARAPHRASE ON PURPOSE. Matthew 25:41-45, the word to those on the left hand,
is red in a red-letter KJV and could have been lifted. It is deliberately left in the
storyteller's compressed handling at n8. This is milk-before-meat: the video's whole
weight is on where he was hiding, not on the sentence, and dropping 'Depart from me,
ye cursed' in verbatim Old English would tip the tone of the piece somewhere it was
never built to go.

NO GREEN: 'my Father' is spoken ABOUT the Father by Christ in the flesh, not BY him.
That is red, not green. No voice from heaven in Matthew 25.

WOMEN: Matthew 25:31-46 records no woman speaking. Nothing added; nothing invented.

PRONUNCIATION: `spoken` is left empty. Nothing in the KJV lines is on the homograph
list. 'an hungred' is unusual but it is verbatim and it is spelled the way it should be
read; I am not confident a respelling improves it, and a bad respelling is worse than
none. Flagged for the faster_whisper audit.

WHY-LAW: he did not hide behind anything impressive. He hid in the people easiest to
overlook, so that plain ordinary kindness would always reach him.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "Near the end, Jesus told his friends what the last day would really be like. He said the King would gather all the nations in front of him and separate them into two groups."),
    # Matthew 25:32
    ("j32", JESUS, "And before him shall be gathered all nations: and he shall separate them one from another, as a shepherd divideth his sheep from the goats:"),
    ("n2", NARRATOR, "Like a shepherd at evening quietly dividing his flock, the sheep to one side and the goats to the other. And what decided which side you were on was not at all what people expect."),
    ("n3", NARRATOR, "To the first group, the ones he welcomed in, the King said this."),
    # Matthew 25:34-36
    ("j1", JESUS, "Come, ye blessed of my Father, inherit the kingdom prepared for you from the foundation of the world: For I was an hungred, and ye gave me meat: I was thirsty, and ye gave me drink: I was a stranger, and ye took me in: Naked, and ye clothed me: I was sick, and ye visited me: I was in prison, and ye came unto me."),
    ("n4", NARRATOR, "You fed me when I was hungry, he said. You gave me water when I was thirsty. You took me in when I was a stranger. You clothed me, you sat with me when I was sick, you came to me when I was locked away."),
    # Matthew 25:37-39
    ("j37", JESUS, "Lord, when saw we thee an hungred, and fed thee? or thirsty, and gave thee drink? When saw we thee a stranger, and took thee in? or naked, and clothed thee? Or when saw we thee sick, or in prison, and came unto thee?"),
    ("n5", NARRATOR, "And here is the beautiful part. The good people are confused. They say, Lord, when did we ever see you hungry, or thirsty, or sick, or in prison? They do not even remember doing anything special. They just helped whoever was in front of them."),
    ("n6", NARRATOR, "They were not keeping score. They were not trying to earn anything. Kindness was simply their reflex. And then the King tells them the secret behind all of it."),
    # Matthew 25:40
    ("j2", JESUS, "Verily I say unto you, Inasmuch as ye have done it unto one of the least of these my brethren, ye have done it unto me."),
    ("n7", NARRATOR, "He was in them the whole time. Every hungry person, every stranger, every sick and forgotten and locked-away person, was him, wearing a disguise."),
    ("n8", NARRATOR, "The others missed him for the very same reason. They were waiting to serve a King on a throne, and they walked right past him a hundred times, because he did not look like a King. He looked like someone who needed help."),
    ("n9", NARRATOR, "That is how good he is. He did not hide himself behind something impressive. He hid in the people easiest to overlook, so that plain, ordinary kindness would always reach him. So when someone small and needy stands in front of you, that is not an interruption. It might be him."),
    ("card", NARRATOR, "He is hidden in the person in front of you who needs help. Will you show him a kindness today?"),
]

# Homographs this build decides for itself (never auto-replaced globally).
# Homographs this build decides for itself (never auto-replaced globally).
# NOTE (2026-07-22): this build briefly carried its own "divideth" override
# ("divyedeth"). A parallel session landed a better-measured per-voice fix in
# the shared map -- "divighdeth", which round-trips as the EXACT word on this
# very line, where mine came back "devideth". Build overrides BEAT the shared
# map, so keeping mine would have silently suppressed the better fix. Removed
# on purpose: #33 now uses the shared jesus-voice entry.
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
