#!/usr/bin/env python3
"""Narration audio for Video #112 — The Beatitudes (Matthew 5:1-12).

Narrator: en-US-AndrewNeural. Jesus: en-US-ChristopherNeural (exact KJV only).

Jesus's KJV lines (Christopher, cream italic):
  jv3   Matt 5:3    "Blessed are the poor in spirit: for theirs is the kingdom of
                     heaven." — silence 1
  jv456 Matt 5:4-6  "Blessed are they that mourn... Blessed are the meek... Blessed are
                     they which do hunger and thirst after righteousness..."
  jv78  Matt 5:7-8  "Blessed are the merciful... Blessed are the pure in heart: for they
                     shall see God."
  jv910 Matt 5:9-10 "Blessed are the peacemakers... Blessed are they which are persecuted
                     for righteousness' sake: for theirs is the kingdom of heaven." — silence 2

WHY-LAW: the world hands out its blessings to the winners — the rich, the strong, the
admired. Jesus climbs a hill and turns it completely upside down: blessed are the ones the
world overlooks — the poor, the grieving, the gentle, the merciful, the persecuted. In his
kingdom, the last are first and the overlooked are honoured. Milk framing: if you have
ever felt small, unseen or worn down, these blessings are aimed straight at you. An
invitation, never a threat.

HOMOGRAPH EAR-CHECK: no high-risk homographs. NUMBER-STRESS LAW obeyed.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"
JESUS = "en-US-ChristopherNeural"

SEGMENTS = [
    ("n1", NARRATOR, "-20%", "-4Hz",
     "The crowds came up the mountain expecting, maybe, the usual — that God blesses the "
     "strong, the rich, the winners. Jesus sat down, and turned the whole thing upside "
     "down.", None),
    # jv3 — poor in spirit — silence 1
    ("jv3", JESUS, "-26%", "-6Hz",
     "Blessed are the poor in spirit: for theirs is the kingdom of heaven.", None),
    ("n2", NARRATOR, "-22%", "-4Hz",
     "He starts with the very people the world walks past. Not the self-made and "
     "self-assured — the ones who know they have nothing to offer God but empty hands. "
     "The kingdom, he says, belongs to them first.", None),
    # jv456 — mourn, meek, hunger
    ("jv456", JESUS, "-24%", "-6Hz",
     "Blessed are they that mourn: for they shall be comforted. Blessed are the meek: for "
     "they shall inherit the earth. Blessed are they which do hunger and thirst after "
     "righteousness: for they shall be filled.", None),
    ("n3", NARRATOR, "-22%", "-4Hz",
     "The grieving will be comforted. The gentle, who never push to the front, will "
     "inherit everything. Those aching to be made good will be filled. Every blessing "
     "goes to exactly the person the world would call a loser.", None),
    # jv78 — merciful, pure in heart
    ("jv78", JESUS, "-24%", "-6Hz",
     "Blessed are the merciful: for they shall obtain mercy. Blessed are the pure in "
     "heart: for they shall see God.", None),
    ("n4", NARRATOR, "-22%", "-4Hz",
     "The merciful will be shown mercy. The pure in heart — the simple, honest, "
     "unguarded ones — will actually see God. Not the clever or the powerful. The clean "
     "of heart.", None),
    # jv910 — peacemakers, persecuted — silence 2
    ("jv910", JESUS, "-26%", "-6Hz",
     "Blessed are the peacemakers: for they shall be called the children of God. Blessed "
     "are they which are persecuted for righteousness' sake: for theirs is the kingdom of "
     "heaven.", None),
    ("n5", NARRATOR, "-22%", "-4Hz",
     "The ones who make peace instead of winning fights are called God's own children. "
     "And even those pushed aside for doing right are not forgotten — the kingdom is "
     "theirs, too. Every last person the world overlooks, God is reaching for.", None),
    ("n6", NARRATOR, "-24%", "-4Hz",
     "So if you have ever felt small, unseen, worn thin, or passed over — listen closely. "
     "In his kingdom, you are not at the back of the line. You are exactly the one he came "
     "for. That is how upside down, and how good, his kingdom really is.", None),
    ("card", NARRATOR, "-26%", "-4Hz",
     "The world blesses the winners; Jesus blesses the overlooked — the poor, the "
     "grieving, the gentle, the merciful. Which of these blessings sounds like it was "
     "written for you?", None),
]


async def main():
    for name, voice, rate, pitch, text, cap in SEGMENTS:
        await save_narration(text, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")


if __name__ == "__main__":
    import os
    os.makedirs("audio", exist_ok=True)
    asyncio.run(main())
