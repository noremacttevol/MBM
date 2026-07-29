#!/usr/bin/env python3
"""Narration for build-43-the-wedding-garment — Matthew 22.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

PARABLE LAW APPLIED. Matthew 22:1-14 is one parable from verse 2 to verse 14, so the
king, the servants and the whole of the dialogue are Jesus's words and a red-letter
KJV inks all of it. Every existing red beat stays red:
  jv4    Matt 22:4     'Behold, I have prepared my dinner...' -- the king's summons
  jv8_9  Matt 22:8-9   'The wedding is ready, but they which were bidden were not
         worthy. Go ye therefore into the highways...'
  jv12   Matt 22:12    'Friend, how camest thou in hither not having a wedding
         garment?' -- the king to the man. Red, not blue.
  jv13   Matt 22:13    'Bind him hand and foot...' -- the king to the servants. Red.
  jv14   Matt 22:14    'For many are called, but few are chosen.'

BLUE ADDED -- the single line in the passage that is Matthew and not Jesus:
  s1  Matt 22:1  'And Jesus answered and spake unto them again by parables, and said.'
      Matthew writing, so `scripture`, light blue. It opens the video and the existing
      n1 keeps its id and now retells it, naming the temple and the men hunting him.

RED ADDED -- the build told most of this parable in the narrator's voice, so four of
Jesus's own blocks come back in, each alternating with an existing narrator beat that
becomes its retelling:
  jv2    Matt 22:2    'The kingdom of heaven is like unto a certain king, which made
         a marriage for his son.' n2 retells it.
  jv3    Matt 22:3    'And sent forth his servants to call them that were bidden to
         the wedding: and they would not come.' Sits first on S3; n3 retells the
         sending, then jv4 gives the message, then n4 lands the refusal.
  jv5_6  Matt 22:5-6  'But they made light of it, and went their ways, one to his
         farm, another to his merchandise: And the remnant took his servants, and
         entreated them spitefully, and slew them.' This was all white paraphrase
         across n5 and n6; both keep their ids and now retell it.
  jv10   Matt 22:10   'So those servants went out into the highways, and gathered
         together all as many as they found, both bad and good: and the wedding was
         furnished with guests.' n9 already says 'the story does not clean it up --
         it says both the bad and the good,' and now the viewer actually hears it.

Deliberately NOT lifted: verse 7, the armies and the burned city -- n6 handles it in
one restrained sentence and quoting it would put the heaviest verse in the passage on
screen in red in a video whose point is the open door. Also not lifted: the second
half of verse 13, 'there shall be weeping and gnashing of teeth.' Same reason, and the
existing jv13 already stops short of it, which was a deliberate choice by whoever
wrote this build and it is left standing.

NO GREEN and NO WOMEN: there is a wedding in this parable and not one woman in it who
speaks. Nothing invented.

WHY-LAW: nobody dragged in off the road owned wedding clothes -- the robe was the
king's to give. Milk: you do not make yourself presentable first, you let him dress
you.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    # Matthew 22:1
    ("s1", SCRIPTURE, "And Jesus answered and spake unto them again by parables, and said,"),
    ("n1", NARRATOR, "He was teaching in the temple, and the men who were hunting for a way to arrest him were standing right in front of him. So he told them a story: about a king, a wedding, and an invitation that almost nobody took."),
    # Matthew 22:2
    ("jv2", JESUS, "The kingdom of heaven is like unto a certain king, which made a marriage for his son,"),
    ("n2", NARRATOR, "A king was giving a wedding feast for his son. The oxen were prepared, the tables were loaded, the hall was full of light. And the guests had been invited long before. They had already said they would come."),
    # Matthew 22:3
    ("jv3", JESUS, "And sent forth his servants to call them that were bidden to the wedding: and they would not come."),
    ("n3", NARRATOR, "So when the day arrived, the king sent his servants to go and bring them in."),
    # Matthew 22:4
    ("jv4", JESUS, "Behold, I have prepared my dinner: my oxen and my fatlings are killed, and all things are ready: come unto the marriage."),
    ("n4", NARRATOR, "And they would not come. Not one of them. They had said yes, and now, with everything ready and waiting, they simply would not walk over."),
    # Matthew 22:5-6
    ("jv5_6", JESUS, "But they made light of it, and went their ways, one to his farm, another to his merchandise: And the remnant took his servants, and entreated them spitefully, and slew them."),
    ("n5", NARRATOR, "They all had something else. A field to go look at. A shop to keep. The king's own guests looked at his son's wedding and decided they had better things to do."),
    ("n6", NARRATOR, "And some of them did worse. They turned on the servants who came to invite them. It was the kind of insult a kingdom does not survive, and that city did not survive it."),
    ("n7", NARRATOR, "But the feast was still ready. The food was still hot. And a hall built for a wedding was standing empty. So the king made a decision."),
    # Matthew 22:8-9
    ("jv8_9", JESUS, "The wedding is ready, but they which were bidden were not worthy. Go ye therefore into the highways, and as many as ye shall find, bid to the marriage."),
    ("n8", NARRATOR, "Out to the roads. Not the guest list. The roads. Whoever happened to be out there. The day laborers, the beggars, the people nobody ever puts on a list."),
    # Matthew 22:10
    ("jv10", JESUS, "So those servants went out into the highways, and gathered together all as many as they found, both bad and good: and the wedding was furnished with guests."),
    ("n9", NARRATOR, "They brought in everyone they could find. The story does not clean it up. It says both the bad and the good, and the wedding hall filled right up."),
    ("n10", NARRATOR, "And here is the part almost everyone misses. Nobody dragged in off the street owned wedding clothes. At a king's feast, the clean festival robe was the king's to give, handed to every guest at the door. Every person in that hall was wearing something the king had put on them."),
    ("n11", NARRATOR, "Then the king came in to meet his guests. And he found one man still in his own dusty road clothes. Not because he was too poor. Everyone there was too poor. Because he had been handed a robe at the door, and had said no to it."),
    # Matthew 22:12
    ("jv12", JESUS, "Friend, how camest thou in hither not having a wedding garment?"),
    ("n12", NARRATOR, "Friend. That is what the king called him. Not intruder. Not thief. Friend, and a question, and every chance in the world to answer. And the man had nothing to say."),
    ("n13", NARRATOR, "He had come to the feast and refused the one thing that made him a guest. So he ended up where he had chosen to be. Back outside, in the dark, away from a light that had been standing wide open for him."),
    # Matthew 22:13
    ("jv13", JESUS, "Bind him hand and foot, and take him away, and cast him into outer darkness."),
    ("n14", NARRATOR, "The men listening knew exactly who the story was about. They were the invited guests, the ones who had said yes for a lifetime and would not come when the King actually arrived. But do not miss what the story is really doing."),
    # Matthew 22:14
    ("jv14", JESUS, "For many are called, but few are chosen."),
    ("n15", NARRATOR, "Everyone is invited. That is the whole world. The ones who end up at the table are simply the ones who came, and who let the King put the clean clothes on them."),
    ("n16", NARRATOR, "You do not have to make yourself presentable first. Nobody in that hall could have, and neither can you. The invitation is free, the door is open, and the clean clothes are already bought and folded and waiting inside. All you have to do is come in, and let him dress you."),
    ("card", NARRATOR, "The King fills his hall with people straight off the road, and hands each one clean clothes at the door. What has he been holding out for you to put on, that you keep walking past?"),
]

# Homographs this build decides for itself (never auto-replaced globally).
SPOKEN = {}


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
