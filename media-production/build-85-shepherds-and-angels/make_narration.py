#!/usr/bin/env python3
"""Narration for build-85-shepherds-and-angels — Luke 2.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

THE FIX: THE ANGELS WERE PAINTED AS JESUS. Both red beats in this build were
wrong, and both are now `scripture` (light blue):
  j1  Luke 2:10-11  'Fear not: for, behold, I bring you good tidings of great
      joy, which shall be to all people. For unto you is born this day in the city
      of David a Saviour, which is Christ the Lord.'  That is THE ANGEL OF THE
      LORD, not Jesus. Leaving it red had the newborn in the manger announcing his
      own birth to shepherds on a hillside. Note the angel says 'unto YOU is born
      this day... a Saviour' -- the speaker is plainly not the Saviour.
  j2  Luke 2:14  'Glory to God in the highest, and on earth peace, good will
      toward men.'  That is THE HEAVENLY HOST -- a multitude of angels. Not Jesus.
Both ids kept.

A NOTE ON WHY THESE ARE BLUE AND NOT GREEN. An angel of the Lord is a messenger
delivering God's words, not the Father, the Holy Ghost, or premortal Jehovah
speaking in his own person. The law reserves green for Deity. Angels sit with
everyone else the KJV records speaking, which is `scripture`. There is NO GREEN in
this build, and no red either -- Jesus is in it, asleep in a trough, and does not
speak a word.

THE SHEPHERDS NOW SPEAK. n3 paraphrased them -- 'the shepherds said to each
other, let us go and see this thing' -- and these men get exactly one line in
scripture. Lifted verbatim as `scripture`:
  s15  Luke 2:15  'Let us now go even unto Bethlehem, and see this thing which is
       come to pass, which the Lord hath made known unto us.'  n3 is trimmed to
       the frame, n3b carries the retelling. Both on ST5.

MARY -- I CHECKED, AND SHE DOES NOT SPEAK. Luke 2:8-20 records not one word from
her. The only thing Luke tells us she did is verse 19, and it is explicitly about
her NOT speaking. So there is no pink line to add, and NOTHING was invented. But
her verse was already sitting in the build as narrator text in almost exactly its
KJV wording, so:
  n7  is re-speakered from `narrator` to `scripture`, verbatim Luke 2:19 -- 'But
      Mary kept all these things, and pondered them in her heart.' Its id is kept
      and n7b is added after it as the retelling. That gives the video its closing
      beat in Luke's own words, and it honours Mary exactly as Luke does: present,
      central, and silent.

RETELLINGS ADDED: n1b after j1 (on ST3), n2b after j2 (on ST4), n3b after s15,
n7b after n7. The build previously had two long Old English blocks with no plain
modern landing after either.

WHY-LAW: the first birth announcement in history was delivered to night-shift
workers, in a field, by name of nobody important. Milk: good tidings of great
joy, which shall be to ALL people -- and heaven went to the bottom of the list
first.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "Outside Bethlehem, shepherds were keeping watch over their flocks by night — ordinary men working the late shift, about the lowest job there was."),
    ("n1", NARRATOR, "Suddenly an angel of the Lord stood before them, and the glory of the Lord blazed all around. They were terrified. And the angel said:"),
    # Luke 2:10-11
    ("j1", SCRIPTURE, "Fear not: for, behold, I bring you good tidings of great joy, which shall be to all people. For unto you is born this day in the city of David a Saviour, which is Christ the Lord."),
    ("n1b", NARRATOR, "Don't be afraid, he told them — I'm bringing you good news, and it's going to be a joy to everybody. Today, in David's town, a Saviour has been born for you. Listen to who he says it is for. Not for the palace. Not for the temple. For you — the men out in the field on the night shift."),
    ("n2", NARRATOR, "And in a moment the one angel became a vast multitude of the heavenly host, filling the whole sky."),
    # Luke 2:14
    ("j2", SCRIPTURE, "Glory to God in the highest, and on earth peace, good will toward men."),
    ("n2b", NARRATOR, "That is what the sky said. Not a warning. Not a demand. Peace, and good will — heaven's opinion of the human race, said out loud over a sheep field."),
    ("n3", NARRATOR, "When the angels had gone away into heaven, the shepherds said to one another:"),
    # Luke 2:15
    ("s15", SCRIPTURE, "Let us now go even unto Bethlehem, and see this thing which is come to pass, which the Lord hath made known unto us."),
    ("n3b", NARRATOR, "Let's go over to Bethlehem right now and see this thing that has happened, that the Lord has told us about. They did not stand around discussing it. They came with haste into the town."),
    ("n4", NARRATOR, "They found Mary and Joseph, and the baby lying in the manger — exactly as they had been told."),
    ("n5", NARRATOR, "There he was: the Saviour of the world, a tiny newborn asleep in a feed trough, wrapped in strips of cloth."),
    ("n6", NARRATOR, "The shepherds could not keep it in. They went out glorifying and praising God, telling everyone they met what they had seen and heard."),
    # Luke 2:19
    ("n7", SCRIPTURE, "But Mary kept all these things, and pondered them in her heart."),
    ("n7b", NARRATOR, "In a story full of people shouting, Luke stops to tell you about the one person who said nothing. She gathered it all up — the angels, the shepherds, the trough, the strangers at the door in the middle of the night — and she held on to it, and turned it over, for the rest of her life."),
    ("card", NARRATOR, "The first birth announcement in history went to night-shift workers on a hillside. Good news of great joy, for all people. Including you."),
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
