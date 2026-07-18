#!/usr/bin/env python3
"""Generate narration audio for Story Video #3 — Zacchaeus (Luke 19:1-10).
Narrator: modern, warm, low, unhurried (American). Plain US model only —
Multilingual models are banned (Cameron, 2026-07-08).
Jesus voice: AMERICAN, never British (Cameron's permanent law, 2026-07-07).
Jesus speaks ONLY exact KJV: Luke 19:5, 19:9, 19:10 (fetched, not hand-typed).
Script pre-flighted on paper per PRODUCTION-BIBLE.md section 4b — see
PREFLIGHT.md. FULL-STORY law: all ten verses covered, vv7-10 included
(the pack had stopped early and marked v10 "optional" — caught on paper).
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

# V2 SCRIPT (2026-07-09) — Cameron rejected v1: "confusing, I don't get
# the point... explain WHY Jesus would do some things... scripture-study
# emphasis... clarify the Matthew mix-up... small tidbits so people can
# connect." Every beat now carries its WHY (CLARITY/WHY-LAW, Bible §4b).
SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    # The Matthew mix-up tidbit, right up front (Cameron asked directly).
    ("n0", NARRATOR, "-20%", "-4Hz",
     "In Jericho there lived a man named Zacchaeus. And if you're "
     "thinking of Matthew — the tax collector who became an apostle — "
     "that's a different man. It's one of the most common mix-ups in the "
     "Bible. Matthew worked a tax booth up in Galilee. Zacchaeus ran the "
     "whole tax office in Jericho. And he was rich."),
    # WHY he was hated.
    ("n1", NARRATOR, "-20%", "-4Hz",
     "Here's why that mattered. Tax collectors worked for Rome — the "
     "empire occupying their own people — and they got rich by charging "
     "extra and keeping the difference. So to his neighbors, Zacchaeus "
     "wasn't just a cheat. He was a traitor. No one greeted him. No one "
     "wanted him at their table."),
    # The problem: short, and no one makes room.
    ("n2", NARRATOR, "-20%", "-4Hz",
     "When Jesus came to Jericho, the whole city pressed into the street "
     "to see him. And Zacchaeus had a problem. He was a short man — the "
     "scripture goes out of its way to mention it — and the crowd stood "
     "like a wall. Not one person made room for him."),
    ("n3a", NARRATOR, "-20%", "-4Hz",
     "So this small, wealthy man did something no respectable person "
     "would ever do. He gathered up his fine robes, and he ran."),
    # Study gem: the dignity he traded.
    ("n3b", NARRATOR, "-20%", "-4Hz",
     "And he climbed a sycamore tree, like a child. Bible students love "
     "this detail. In that world, a grown man running and climbing was "
     "humiliating. Zacchaeus traded the last of his dignity for one "
     "glimpse of Jesus — from a distance. He would have settled for "
     "that."),
    # PEAK — music has already cut to full silence before this line
    ("n4", NARRATOR, "-25%", "-5Hz",
     "He got far more. Jesus stopped — under that exact tree — looked "
     "up, and called him by name."),
    # Exact KJV Luke 19:5b (fetched, not hand-typed) — split at the KJV
    # semicolon so each half carries its own caption (clip, then still).
    # j1a at -22%: the -25% take slurred "Zacchaeus" (failed BOTH whisper
    # models — a real TTS defect); the -22% take passes medium.en at 1.00.
    ("j1a", JESUS, "-22%", "-6Hz",
     "Zacchaeus, make haste, and come down;"),
    ("j1b", JESUS, "-25%", "-6Hz",
     "for to day I must abide at thy house."),
    # WHY the meal was shocking — the point of the whole story.
    ("n5", NARRATOR, "-22%", "-4Hz",
     "Now — why would Jesus do that? Understand what a meal meant back "
     "then. To eat at a man's house was to publicly accept him. Jesus "
     "didn't tell him to clean up his life first. He invited himself "
     "in — before Zacchaeus had changed a single thing. That is the "
     "point of the whole story. Jesus moves first."),
    # v6-7: joy, and WHY the crowd grumbled (Full-Story law).
    ("n6", NARRATOR, "-22%", "-4Hz",
     "Zacchaeus came down faster than he had climbed up, and welcomed "
     "him with joy. But the crowd was appalled, and grumbled out loud — "
     "of every house in Jericho, he had chosen the worst man's. In their "
     "rules, you earned your way back before anyone sat at your table."),
    # v8 split: the standing gift, then the fourfold study gem.
    ("n7a", NARRATOR, "-22%", "-4Hz",
     "Then, at that table, it happened. Zacchaeus stood up in front of "
     "everyone: half of everything I own goes to the poor."),
    ("n7b", NARRATOR, "-22%", "-4Hz",
     "And anyone I have cheated, I will pay back four times over. That "
     "number is a study gem. The law of Moses required fourfold "
     "repayment only for outright theft. Zacchaeus was judging himself "
     "by the harshest standard — and paying it gladly. Nobody demanded "
     "it. Being loved first is what changed him."),
    ("n7c", NARRATOR, "-25%", "-5Hz",
     "And Jesus answered him with the words this story was written to "
     "keep."),
    # Exact KJV Luke 19:9b and 19:10 — the TRUE last story words.
    ("j2a", JESUS, "-25%", "-6Hz",
     "This day is salvation come to this house, forsomuch as he also is "
     "a son of Abraham."),
    ("j2b", JESUS, "-25%", "-6Hz",
     "For the Son of man is come to seek and to save that which was "
     "lost."),
    # WHY "son of Abraham" matters (3-word commentary, Translation Law
    # per the v1 "I must" precedent).
    ("n8", NARRATOR, "-25%", "-5Hz",
     "A son of Abraham — with those words, Jesus gave him back his place "
     "in the family his whole city said he had forfeited."),
    ("n9", NARRATOR, "-25%", "-5Hz",
     "And that last line is the key to everything. Jesus was not stuck "
     "in that crowd by accident. He was seeking. The man everyone "
     "stepped in front of was the one he came to find."),
    # Closing card read aloud, gently (Readable-Card Law).
    ("n10", NARRATOR, "-25%", "-5Hz",
     "Jesus called him by name before he changed anything. What would it "
     "mean to you — to be wanted like that, exactly as you are right "
     "now?"),
]

async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        await save_narration(text, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
