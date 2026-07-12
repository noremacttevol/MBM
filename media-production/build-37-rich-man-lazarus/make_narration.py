#!/usr/bin/env python3
"""Narration for Story Video #37 — The Rich Man and Lazarus (Luke 16:19-31).
Two-Voice Law: Andrew narrates (plain American, NEVER Multilingual); Christopher
speaks ONLY the exact KJV lines — here Abraham's words (16:25 and 16:31).
Translation Law: the narrator paraphrases and quotes characters in modern English
and never echoes the KJV wording of the two spoken lines (16:25 / 16:31)."""
import asyncio, edge_tts, os

NARRATOR = "en-US-AndrewNeural"        # plain American, NEVER Multilingual
JESUS    = "en-US-ChristopherNeural"   # American, never British

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0",  NARRATOR, "-18%", "-4Hz",
     "Jesus once told a story about two men who lived side by side, "
     "yet worlds apart."),
    ("n1",  NARRATOR, "-18%", "-4Hz",
     "One was rich. He wore the finest purple and linen, and every day of his "
     "life was a feast."),
    ("n2",  NARRATOR, "-18%", "-4Hz",
     "Just outside his house, at his own gate, lay a poor beggar named Lazarus."),
    ("n3",  NARRATOR, "-18%", "-4Hz",
     "He was covered in sores, and so hungry he only wished for the scraps that "
     "fell from the rich man's table. Even the stray dogs came and licked his "
     "wounds."),
    ("n4",  NARRATOR, "-18%", "-4Hz",
     "The rich man walked past that gate every single day. And every day he "
     "stepped around the suffering man lying there, and did nothing."),
    ("n5",  NARRATOR, "-18%", "-4Hz",
     "Then the day came that comes for us all. Lazarus died — and the angels "
     "carried him home, to Abraham's side, into light and comfort at last."),
    ("n6",  NARRATOR, "-18%", "-4Hz",
     "The rich man died too, and was buried. But he opened his eyes in a place "
     "of torment: a dark and thirsty place, far from the light."),
    ("n7",  NARRATOR, "-18%", "-4Hz",
     "Across a vast divide he could see Abraham in the distance, with Lazarus "
     "resting beside him. And he cried out, begging for just a drop of water to "
     "cool his tongue."),
    ("j1",  JESUS,    "-22%", "-5Hz",
     "Son, remember that thou in thy lifetime receivedst thy good things, and "
     "likewise Lazarus evil things: but now he is comforted, and thou art "
     "tormented."),
    ("n8",  NARRATOR, "-18%", "-4Hz",
     "And between them, Abraham said, a great gulf had been fixed — one that no "
     "one could ever cross."),
    ("n9",  NARRATOR, "-18%", "-4Hz",
     "So the rich man begged again: then send someone to my five brothers, to "
     "warn them, so they never come to this place."),
    ("n10", NARRATOR, "-18%", "-4Hz",
     "They already have the writings of Moses and the prophets, Abraham replied. "
     "Let them listen. But the man pleaded — no, if only someone came back from "
     "the dead, then they would turn."),
    ("n11", NARRATOR, "-18%", "-4Hz",
     "And Abraham gave his final answer."),
    ("j2",  JESUS,    "-22%", "-5Hz",
     "If they hear not Moses and the prophets, neither will they be persuaded, "
     "though one rose from the dead."),
    ("n12", NARRATOR, "-18%", "-4Hz",
     "Jesus told this to people who had everything, and walked right past the "
     "ones who had nothing. It was a warning — but underneath it, a mercy."),
    ("n13", NARRATOR, "-18%", "-4Hz",
     "Because there is still a gate in front of you today. There is still someone "
     "you walk past. And there is still time to stop, and see them, and turn — "
     "while the day is yours."),
    ("card", NARRATOR, "-18%", "-4Hz",
     "There is a gate before you today, and someone waiting at it. "
     "Who are you walking past — and will you stop while there is still time?"),
]

async def main():
    os.makedirs("audio", exist_ok=True)
    for name, voice, rate, pitch, text in SEGMENTS:
        await edge_tts.Communicate(text, voice, rate=rate, pitch=pitch).save(f"audio/{name}.mp3")
        print("saved", name)

# Guard so `from make_narration import SEGMENTS` (qc_narration.py) does NOT re-run TTS.
if __name__ == "__main__":
    asyncio.run(main())
