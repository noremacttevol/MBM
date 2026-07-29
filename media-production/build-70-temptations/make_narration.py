#!/usr/bin/env python3
"""Narration for build-70-temptations — Matthew 4.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

STAYED RED, all three, unchanged. j1 (Matthew 4:4), j2 (4:7) and j3 (4:10) are
Jesus in the flesh and a red-letter KJV inks every one of them.

THE ONE RULING THAT MATTERS HERE: all three of his answers begin 'It is written'
and then quote Deuteronomy. They STAY RED. The test is never whose words are
being quoted, it is who is talking - and it is Jesus talking, out loud, in the
wilderness. Turning the quoted law green would say the Father was speaking in
that moment, and he was not. Same principle as build-73, where Jesus reads
Isaiah aloud in the synagogue and the reading is red.

SATAN NOW SPEAKS, AND HE IS LIGHT BLUE, NOT RED. All three temptations were
modern paraphrase inside narrator beats. They are now lifted out verbatim as
SCRIPTURE - a being in the story, quoted from the KJV like anybody else in it.
He is not Jesus and he is not God, so blue is the only honest colour, and the
red/blue alternation is what finally makes the scene read as the duel it is:
  s3   Matthew 4:3  'If thou be the Son of God, command that these stones be
       made bread.'  -> n2 keeps its id and now retells it; its first two
       sentences came out because s3 says them straight.
  s6   Matthew 4:6  'If thou be the Son of God, cast thyself down...' - the
       temptation where the devil quotes Psalm 91 himself. n4 was split: n4
       keeps its id and sets the scene, s6 is the verse, n4b retells it.
  s9   Matthew 4:9  'All these things will I give thee, if thou wilt fall down
       and worship me.'  n5 keeps its id and sets it up, n5b retells.

ALSO ADDED AS SCRIPTURE:
  s11  Matthew 4:11  'Then the devil leaveth him, and, behold, angels came and
       ministered unto him.'  n6 keeps its text and now retells it.
  s415 Hebrews 4:15  'For we have not an high priest which cannot be touched
       with the feeling of our infirmities; but was in all points tempted like
       as we are, yet without sin.'  n7 already SAID 'the book of Hebrews says
       it plainly' and then paraphrased it. Now the viewer hears the verse and
       then hears n7 retell it. An epistle, so the writer - scripture, blue.
  n6a  new narrator beat on S8 so 'Get thee hence, Satan' is retold before the
       scene moves on.

WOMEN: Matthew 4:1-11 records no woman speaking. Nothing added, nothing invented.

NO GREEN: the Father does not speak in this chapter. n0 refers to 'this is my
beloved Son' from the baptism a chapter earlier, but only as narration - it is
not lifted, because the baptism belongs to its own video.

WHY-LAW: he fought hungry, as a man, with a sentence off the shelf that any of
us could memorise. He never once used his own power to get out of it.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "Straight from the river, still carrying his Father's words — this is my beloved Son — Jesus was led by the Spirit up into the wilderness. Not by accident. Led there. Before the teaching, before the miracles, there was going to be a battle, and it was going to happen in the emptiest place in the country: bare rock, dead heat, and silence."),
    ("n1", NARRATOR, "He fasted forty days and forty nights. Mark that: he was not floating above any of it. He got hungrier every single day, the way you would. And when he was at his weakest and emptiest — that is exactly when the tempter came."),
    # Matthew 4:3
    ("s3", SCRIPTURE, "If thou be the Son of God, command that these stones be made bread."),
    ("n2", NARRATOR, "Hear what that little word IF is doing. Heaven had just said, this IS my Son. The very first attack was aimed at that sentence — prove it, earn it, doubt it. And the bait was reasonable: you're starving, you have the power, feed yourself. Use what you are for you."),
    # Matthew 4:4
    ("j1", JESUS, "It is written, Man shall not live by bread alone, but by every word that proceedeth out of the mouth of God."),
    ("n3", NARRATOR, "Notice what he did NOT do. He did not argue. He did not use his own power. He answered with a line of scripture — a sentence any of us could memorize — and stood on it. The Son of God fought hungry, as a man, with the same weapon you have on your shelf."),
    ("n4", NARRATOR, "The second try was stranger. In a flash he was at the highest corner of the temple, the city far below — and the voice turned religious. It quoted scripture back at him."),
    # Matthew 4:6
    ("s6", SCRIPTURE, "If thou be the Son of God, cast thyself down: for it is written, He shall give his angels charge concerning thee: and in their hands they shall bear thee up, lest at any time thou dash thy foot against a stone."),
    ("n4b", NARRATOR, "Throw yourself down, it said — the angels are promised to catch you. Force your Father to prove himself, publicly, on demand. Make God perform."),
    # Matthew 4:7
    ("j2", JESUS, "It is written again, Thou shalt not tempt the Lord thy God."),
    ("n5", NARRATOR, "Trust does not run experiments on the one it trusts. Then came the last offer, the biggest one. From a high mountain, all the kingdoms of the world and the glory of them, spread out like a feast."),
    # Matthew 4:9
    ("s9", SCRIPTURE, "All these things will I give thee, if thou wilt fall down and worship me."),
    ("n5b", NARRATOR, "All of it, yours, right now — one bow, to me. It was the crown without the cross. Everything he came to win, offered as a shortcut with only one small condition: worship the wrong king."),
    # Matthew 4:10
    ("j3", JESUS, "Get thee hence, Satan: for it is written, Thou shalt worship the Lord thy God, and him only shalt thou serve."),
    ("n6a", NARRATOR, "Get away from me. He did not haggle with the offer, and he did not admire it. He named it and ended it."),
    # Matthew 4:11
    ("s11", SCRIPTURE, "Then the devil leaveth him, and, behold, angels came and ministered unto him."),
    ("n6", NARRATOR, "And it was over. The devil left him — for a season. And angels came and ministered to him, the way dawn comes after the longest night. Bread, after the fast. Company, after the silence. His Father had not been absent for one minute of it — he had been trusted."),
    # Hebrews 4:15
    ("s415", SCRIPTURE, "For we have not an high priest which cannot be touched with the feeling of our infirmities; but was in all points tempted like as we are, yet without sin."),
    ("n7", NARRATOR, "That is what the book of Hebrews is saying. We do not have a Savior who cannot understand our weakness — he was tempted in every way we are. Hungry, alone, offered every shortcut. He has stood in your exact spot. That is why he knows how to stand next to you in it."),
    ("card", NARRATOR, "He has stood where you stand — hungry, alone, offered every shortcut — and he held. Ask him. He knows how to help you hold."),
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
