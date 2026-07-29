#!/usr/bin/env python3
"""Narration for build-40-the-friend-at-midnight — Luke 11.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

PARABLE LAW APPLIED. 'Trouble me not: the door is now shut, and my children are with
me in bed; I cannot rise and give thee' is the sleeping neighbour, and 'Friend, lend
me three loaves' is the man outside -- both are characters inside Jesus's parable, so
a red-letter KJV inks both red. Neither was turned blue. This is the trap in this
build and it was left alone.

STAYED RED, all five, and all correct as they stood:
  j0  Luke 11:2   'When ye pray, say, Our Father which art in heaven...'
  j1  Luke 11:5-6 'Friend, lend me three loaves...'
  j2  Luke 11:7   'Trouble me not: the door is now shut...'
  j3  Luke 11:8   'I say unto you, Though he will not rise and give him...'
  j4  Luke 11:9   'Ask, and it shall be given you...'
  j5  Luke 11:13  'If ye then, being evil, know how to give good gifts...'
None of them had Luke's framing welded on, so none needed splitting.

BLUE ADDED -- THE DISCIPLE WHO ASKED THE QUESTION WAS NEVER HEARD:
  s1  Luke 11:1  'And it came to pass, that, as he was praying in a certain place,
      when he ceased, one of his disciples said unto him, Lord, teach us to pray, as
      John also taught his disciples.' This is Luke narrating plus a disciple
      speaking -- both `scripture`, light blue, because it is outside the parable and
      it is not Jesus. The whole video hangs on that request and it was white
      paraphrase. n1 keeps its id and now retells it.

RED ADDED:
  jv5  Luke 11:5  'Which of you shall have a friend, and shall go unto him at
       midnight, and say unto him.' Jesus's own setup line, which the build skipped
       straight past. It sits on S5 immediately before j1, on the same still.
  jv11 Luke 11:11-12  'If a son shall ask bread of any of you that is a father, will
       he give him a stone? or if he ask a fish, will he for a fish give him a
       serpent? Or if he shall ask an egg, will he offer him a scorpion?' This was
       entirely paraphrase in n16a -- three of the best questions Jesus ever asked,
       and none of them were in his own words. n16a and n16b keep their ids and now
       retell it, including the lookalike explanation.

Deliberately NOT lifted: Luke 11:2b-4, the rest of the Lord's Prayer. j0 stops at
'Hallowed be thy name' on purpose -- the video is about the first word, Father, and
running the full prayer would hijack the story before it starts.

NO GREEN: the Father is spoken ABOUT here, never quoted, so nothing is green.
NO WOMEN: Luke 11:1-13 records none speaking. Nothing invented.

WHY-LAW: the neighbour is the contrast, not the picture. Milk: he was never asleep. 2026-07-21: narrator beats n4/n8/n14b/n16a/n16b/n17/n18 tightened (~275 chars) to clear the 25MB bitrate law; teaching unchanged.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    # Luke 11:1
    ("s1", SCRIPTURE, "And it came to pass, that, as he was praying in a certain place, when he ceased, one of his disciples said unto him, Lord, teach us to pray, as John also taught his disciples."),
    ("n1", NARRATOR, "His disciples had watched him pray for years, and watched him come back from it different. So one morning they asked him for the thing they wanted most. Teach us how to do that."),
    ("n2", NARRATOR, "So he gave them a prayer. And the first word of it was not Lord, and it was not God. It was the word a small child uses."),
    # Luke 11:2
    ("j0", JESUS, "When ye pray, say, Our Father which art in heaven, Hallowed be thy name."),
    ("n3", NARRATOR, "He taught them to walk up to God and call him Father. And then, to show them what kind of Father he meant, he told a story about a man banging on a door in the middle of the night."),
    ("n4", NARRATOR, "People travelled at night there, because the daytime heat could kill you. So a friend really could turn up at midnight, starving — and you did not send him away. Feeding a guest was a duty the whole village shared."),
    ("n5", NARRATOR, "So a man opens his door at midnight to a friend who has walked all day. Then he looks at his own shelf, and there is nothing on it. Not a crumb."),
    ("n6", NARRATOR, "So he picks up his little clay lamp and walks out into a sleeping village, toward the one door he knows still has bread behind it."),
    # Luke 11:5
    ("jv5", JESUS, "Which of you shall have a friend, and shall go unto him at midnight, and say unto him,"),
    # Luke 11:5-6
    ("j1", JESUS, "Friend, lend me three loaves; for a friend of mine in his journey is come to me, and I have nothing to set before him."),
    ("n7", NARRATOR, "Notice who he is asking for. He is standing out there in the dark, begging for bread he will not eat."),
    ("n8", NARRATOR, "On the other side of that door, a village house was one room. The whole family slept on one platform under one blanket, behind a heavy bar. Getting up meant waking every child in the house."),
    # Luke 11:7
    ("j2", JESUS, "Trouble me not: the door is now shut, and my children are with me in bed; I cannot rise and give thee."),
    ("n9", NARRATOR, "That is a no. And it is not a lazy no. That is a tired man with sleeping children and a real reason."),
    ("n10", NARRATOR, "So the man outside does the thing nobody expected. He knocks again. Louder. Shutters bang open up the street. Dogs start barking. And he keeps knocking."),
    ("n11", NARRATOR, "The word Luke uses here shows up nowhere else in the whole New Testament. Most Bibles turn it into the word persistence. It does not mean persistence. It means shamelessness. He was not too proud to look like a fool."),
    # Luke 11:8
    ("j3", JESUS, "I say unto you, Though he will not rise and give him, because he is his friend, yet because of his importunity he will rise and give him as many as he needeth."),
    ("n12", NARRATOR, "He went for enough bread to feed one man. He came home with an armful. And notice why. The neighbour did not get up because they were friends. He got up because the man outside would not stop asking."),
    ("n13", NARRATOR, "And in a dark house at midnight, a tired stranger ate a meal he never knew somebody had fought for."),
    ("n14a", NARRATOR, "Here is where almost everybody gets this story wrong. People hear it and think God is the man behind the door. Annoyed. Asleep. Somebody you have to wear down."),
    ("n14b", NARRATOR, "That is the opposite of what he said. The neighbour is not a picture of God — he is the contrast. If even a worn-out man behind a barred door will get up for you in the end, what will your Father do, when he was never asleep at all?"),
    # Luke 11:9
    ("j4", JESUS, "Ask, and it shall be given you; seek, and ye shall find; knock, and it shall be opened unto you."),
    ("n15", NARRATOR, "In the Greek, none of those is a one-time act. Every one of them means keep coming back."),
    # Luke 11:11-12
    ("jv11", JESUS, "If a son shall ask bread of any of you that is a father, will he give him a stone? or if he ask a fish, will he for a fish give him a serpent? Or if he shall ask an egg, will he offer him a scorpion?"),
    ("n16a", NARRATOR, "Then he asked them: if your son asked for bread, would you put a rock in his hand? If he asked for a fish, would you hand him a snake?"),
    ("n16b", NARRATOR, "Every pair is a lookalike — a river stone the size of a flat loaf, a scorpion curled pale and round like an egg. A father handing his hungry child a counterfeit. Not one of you, he said, would ever do it."),
    # Luke 11:13
    ("j5", JESUS, "If ye then, being evil, know how to give good gifts unto your children: how much more shall your heavenly Father give the Holy Spirit to them that ask him?"),
    ("n17", NARRATOR, "You already know how to be good to your kids — and you are not half as good as he is. That is the whole argument: God does not have to be worn down. He was never asleep."),
    ("n18", NARRATOR, "The man in the story was knocking on a door with somebody asleep behind it. You are not. Whatever you quit asking for — too small, too late, too much — the light in that house is already on. And the best thing he has to give was never bread. It is himself."),
    ("card", NARRATOR, "The man at the door was not asking for himself, and he was not too proud to look foolish. What would you ask God for tonight, if you knew for certain he was awake?"),
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
