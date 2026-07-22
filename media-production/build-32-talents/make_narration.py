#!/usr/bin/env python3
"""Narration for build-32-talents — Matthew 25.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

STAYED RED: j1 is the lord in the parable of the talents, and SPEAKER-LAW names
this exact line as the standing example of where red is still right -- inside a
parable, the characters' words are Jesus's words:
  j1  Matthew 25:21  'Well done, thou good and faithful servant: thou hast been
      faithful over a few things, I will make thee ruler over many things: enter thou
      into the joy of thy lord.'
Verified verbatim (the framing clause 'His lord said unto him,' is not in the beat,
and it would not have needed splitting anyway -- inside a parable that framing is
Jesus narrating too, and a red-letter KJV inks it red along with the rest).

THE REAL FIX -- j2 WAS NOT VERBATIM. j2 read 'Lord, I knew thee that thou art an hard
man, and I was afraid, and went and hid thy talent in the earth.' That is a splice.
It welds the front of 25:24 to the middle of 25:25 and silently drops 'reaping where
thou hast not sown, and strawing where thou hast not strawed:' from between them. A
viewer who looked it up would not find that sentence anywhere in the KJV, which is
exactly what the hard rule forbids. Fixed by splitting it into the two real verses,
BOTH ON THE SAME STILL S7, both JESUS, both red -- no new artwork and no colour change:
  j24  Matthew 25:24  'Lord, I knew thee that thou art an hard man, reaping where thou
       hast not sown, and strawing where thou hast not strawed:'
  j2   Matthew 25:25  'And I was afraid, and went and hid thy talent in the earth: lo,
       there thou hast that is thine.'   -- id kept, so the music beds are not orphaned.
n9 is already the retelling and follows both, untouched.

ADDED RED. The opening of the parable was told only in paraphrase:
  j14  Matthew 25:14  'For the kingdom of heaven is as a man travelling into a far
       country, who called his own servants, and delivered unto them his goods.'
       -- placed on S1 ahead of n1, which keeps its text and now retells it.

LEFT AS PARAPHRASE ON PURPOSE. Matthew 25:15 (the five, two and one) and 25:20 (the
first servant's report, 'Lord, thou deliveredst unto me five talents') are both red in
a red-letter KJV and both could have been lifted. They are deliberately left in the
storyteller's voice: n2 through n6 are a fast, plain run through the setup, and
dropping two more Old English blocks into it would turn the first half of the video
into a recitation. Verbatim and retold, alternating -- red now lands on S1, S6 and S7.

NO GREEN: no voice from heaven in Matthew 25:14-30.

WOMEN: the parable of the talents records no woman speaking. Nothing added; nothing
invented.

PRONUNCIATION: `spoken` is left EMPTY on purpose, and this is a judgement call worth
flagging. 'sown' in j24 is the seed word but it already rhymes with 'own' as spelled,
so it needs nothing. 'strawing' and 'strawed' are genuinely obscure archaic verbs and
I am NOT confident of a respelling that would improve them -- SPEAKER-LAW says a bad
respelling is worse than none, so they are left alone and flagged here for the
faster_whisper audit to check in the rendered audio.

WHY-LAW: the tragedy is not that he had little. It is that he was wrong about his
master. His fear was built on a lie about who the man really was, and the lie cost him
everything. God is not the hard man that servant imagined.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    # Matthew 25:14
    ("j14", JESUS, "For the kingdom of heaven is as a man travelling into a far country, who called his own servants, and delivered unto them his goods."),
    ("n1", NARRATOR, "Jesus told a story about a wealthy man who, before a long journey, entrusted his servants with his own fortune. To one he gave five bags of silver, to another two, and to another one, each according to what he could handle."),
    ("n2", NARRATOR, "It was a staggering amount of trust. He handed his wealth to his servants and left them free to use it."),
    ("n3", NARRATOR, "The servant with five bags went straight to work, trading and investing, and doubled everything he had been given."),
    ("n4", NARRATOR, "The servant with two bags did the same, and doubled his as well. Neither one played it safe. They took what they were trusted with and made it grow."),
    ("n5", NARRATOR, "But the servant with one bag was afraid. So he dug a hole in the ground, buried the silver, and did nothing with it at all."),
    ("n6", NARRATOR, "When the master came home, the first two servants showed him what they had made. And he was overjoyed."),
    # Matthew 25:21
    ("j1", JESUS, "Well done, thou good and faithful servant: thou hast been faithful over a few things, I will make thee ruler over many things: enter thou into the joy of thy lord."),
    ("n7", NARRATOR, "Enter into the joy of your master. He did not just reward them, he shared his own joy with them, and welcomed them deeper in."),
    ("n8", NARRATOR, "Then the last servant came, dug up his one buried bag, and handed it back untouched. And listen to why he had buried it."),
    # Matthew 25:24
    ("j24", JESUS, "Lord, I knew thee that thou art an hard man, reaping where thou hast not sown, and strawing where thou hast not strawed:"),
    # Matthew 25:25
    ("j2", JESUS, "And I was afraid, and went and hid thy talent in the earth: lo, there thou hast that is thine."),
    ("n9", NARRATOR, "There it is. He buried the gift because he believed his master was harsh and cruel. He was wrong about him. His fear was built on a lie about who his master really was, and that lie cost him everything."),
    ("n10", NARRATOR, "That is the real tragedy of the story. Not that he had little, but that he so badly misjudged the heart of the one who trusted him. God is not the hard man that servant imagined. He trusts you with something real, and he is longing to say to you, well done, and to share his joy."),
    ("card", NARRATOR, "What has God trusted you with that fear has kept you from using? What if he is kinder than you think?"),
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
