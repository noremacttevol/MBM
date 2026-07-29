#!/usr/bin/env python3
"""Narration for build-03-zacchaeus — Luke 19.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

STAYED RED: all four existing red beats are Jesus speaking in the flesh and a
red-letter KJV prints every one of them.
  j1a/j1b  Luke 19:5    'Zacchaeus, make haste, and come down; for to day I must
                         abide at thy house.'
  j2a/j2b  Luke 19:9-10 'This day is salvation come to this house... For the Son
                         of man is come to seek and to save that which was lost.'
Nothing moved out of red in this build.

LIFTED FROM PARAPHRASE - two voices the story needs and did not have:
  s7   Luke 19:7  the crowd: 'That he was gone to be guest with a man that is a
                  sinner.'  SCRIPTURE (blue - the murmuring city)
  s8   Luke 19:8  Zacchaeus himself: 'Behold, Lord, the half of my goods I give
                  to the poor; and if I have taken any thing from any man by
                  false accusation, I restore him fourfold.'  SCRIPTURE

s8 is the big one. The whole video turns on what Zacchaeus says at that table,
and he was never allowed to say it - the narrator said it for him, across two
beats, in modern English. Now he speaks it, and the narrator's study note about
fourfold repayment follows as the retelling, which is what that note was always
for.

EDITS TO EXISTING NARRATOR TEXT: n6 now ends on 'grumbled out loud' and hands to
s7; the rest of its old text became n6b, opening with the retelling. n7a now ends
on 'stood up in front of everyone' and hands to s8; n7b regains the half-of-my-
goods clause as its opening retelling and then continues word for word as before.
Nothing else changed.

NOT LIFTED: n0's Matthew/Zacchaeus mix-up note and n2's 'he was a short man' are
the storyteller explaining, not quoting - they stay narrator, correctly.

WOMEN: Luke 19:1-10 records no woman speaking. Nothing added; nothing invented.

WHY-LAW: Jesus invited himself in before Zacchaeus had changed one thing, and the
changing came after. Milk framing - being wanted first is what changes a person,
and 'son of Abraham' gave a hated man his family back, in public.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "In Jericho there lived a man named Zacchaeus. And if you're thinking of Matthew — the tax collector who became an apostle — that's a different man. It's one of the most common mix-ups in the Bible. Matthew worked a tax booth up in Galilee. Zacchaeus ran the whole tax office in Jericho. And he was rich."),
    ("n1", NARRATOR, "Here's why that mattered. Tax collectors worked for Rome — the empire occupying their own people — and they got rich by charging extra and keeping the difference. So to his neighbors, Zacchaeus wasn't just a cheat. He was a traitor. No one greeted him. No one wanted him at their table."),
    ("n2", NARRATOR, "When Jesus came to Jericho, the whole city pressed into the street to see him. And Zacchaeus had a problem. He was a short man — the scripture goes out of its way to mention it — and the crowd stood like a wall. Not one person made room for him."),
    ("n3a", NARRATOR, "So this small, wealthy man did something no respectable person would ever do. He gathered up his fine robes, and he ran."),
    ("n3b", NARRATOR, "And he climbed a sycamore tree, like a child. Bible students love this detail. In that world, a grown man running and climbing was humiliating. Zacchaeus traded the last of his dignity for one glimpse of Jesus — from a distance. He would have settled for that."),
    ("n4", NARRATOR, "He got far more. Jesus stopped — under that exact tree — looked up, and called him by name."),
    # Luke 19:5
    ("j1a", JESUS, "Zacchaeus, make haste, and come down;"),
    # Luke 19:5
    ("j1b", JESUS, "for to day I must abide at thy house."),
    ("n5", NARRATOR, "Now — why would Jesus do that? Understand what a meal meant back then. To eat at a man's house was to publicly accept him. Jesus didn't tell him to clean up his life first. He invited himself in — before Zacchaeus had changed a single thing. That is the point of the whole story. Jesus moves first."),
    ("n6", NARRATOR, "Zacchaeus came down faster than he had climbed up, and welcomed him with joy. But the crowd was appalled, and they grumbled out loud."),
    # Luke 19:7
    ("s7", SCRIPTURE, "That he was gone to be guest with a man that is a sinner."),
    ("n6b", NARRATOR, "Of every house in Jericho, he had chosen the worst man's. In their rules, you earned your way back before anyone sat at your table."),
    ("n7a", NARRATOR, "Then, at that table, it happened. Zacchaeus stood up in front of everyone."),
    # Luke 19:8
    ("s8", SCRIPTURE, "Behold, Lord, the half of my goods I give to the poor; and if I have taken any thing from any man by false accusation, I restore him fourfold."),
    ("n7b", NARRATOR, "Half of everything I own goes to the poor, he said — and anyone I have cheated, I will pay back four times over. That number is a study gem. The law of Moses required fourfold repayment only for outright theft. Zacchaeus was judging himself by the harshest standard — and paying it gladly. Nobody demanded it. Being loved first is what changed him."),
    ("n7c", NARRATOR, "And Jesus answered him with the words this story was written to keep."),
    # Luke 19:9
    ("j2a", JESUS, "This day is salvation come to this house, forsomuch as he also is a son of Abraham."),
    # Luke 19:10
    ("j2b", JESUS, "For the Son of man is come to seek and to save that which was lost."),
    ("n8", NARRATOR, "A son of Abraham — with those words, Jesus gave him back his place in the family his whole city said he had forfeited."),
    ("n9", NARRATOR, "And that last line is the key to everything. Jesus was not stuck in that crowd by accident. He was seeking. The man everyone stepped in front of was the one he came to find."),
    ("n10", NARRATOR, "Jesus called him by name before he changed anything. What would it mean to you — to be wanted like that, exactly as you are right now?"),
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
