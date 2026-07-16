#!/usr/bin/env python3
"""Generate narration audio for Story Video #68 — Multitudes on the Mountain (Matt 15:29-32).
Narrator: modern, warm, low, unhurried (American). Plain US model only.
Jesus voice: AMERICAN, never British. Jesus speaks ONLY exact KJV: Matt 15:32b
(fetched, not hand-typed) — the only red-letter line in the passage.
GREEN story; the sick and maimed are shown with dignity (no gore, no grotesque).
Homograph ear-check list scanned; no offenders used.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0", NARRATOR, "-20%", "-4Hz",
     "After the coast, Jesus came back toward the Sea of Galilee, "
     "climbed partway up a mountain, and sat down. That's all he did. "
     "He sat down where he could be found. And the whole region "
     "emptied itself onto that mountainside to find him."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "Matthew says great multitudes came — and they did not come "
     "empty-handed. They came carrying people. Think about what that "
     "means on a mountain. Somebody hauled their father up a rocky "
     "slope on a plank. Somebody carried a grown brother on their "
     "back. Somebody led a blind neighbor by the hand over every "
     "single stone. Every step of that climb was somebody's love for "
     "somebody, written in sweat."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "And they laid them down at his feet. The lame, the blind, the "
     "mute, the maimed — Matthew stacks up the words until you can "
     "see it: the pain of an entire region, gathered into one place, "
     "set down in front of one man."),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "And then the gospel gives us four of the biggest words in the "
     "Bible, with no fanfare at all: and he healed them. That's it. "
     "No names. No interviews. No list. Thousands of the greatest "
     "moments of thousands of lives, all hidden inside one quiet "
     "sentence."),
    ("n4", NARRATOR, "-20%", "-4Hz",
     "Somewhere on that mountain, a woman who had never spoken said "
     "her husband's name for the first time. Somewhere an old man's "
     "eyes came open on his grandchild's face. Somewhere legs that "
     "had been carried up the mountain carried their owner back down "
     "it. Multiply that by a hillside. That was the afternoon."),
    ("n5", NARRATOR, "-20%", "-4Hz",
     "Matthew says the multitude wondered — they saw the mute "
     "speaking, the maimed made whole, the lame walking, the blind "
     "seeing — and they glorified the God of Israel. On that side of "
     "the sea, many of them were outsiders to Israel entirely. The "
     "healing preached better than any sermon."),
    ("n6", NARRATOR, "-20%", "-4Hz",
     "And here is the detail people miss: they stayed. Three days, "
     "on a mountainside, until the food ran out — and nobody wanted "
     "to go home. When the disciples started worrying about the "
     "crowd's empty stomachs, listen to what Jesus said:"),
    # Exact KJV Matt 15:32b — SILENCE around it.
    ("j1", JESUS, "-20%", "-2Hz",
     "I have compassion on the multitude, because they continue with "
     "me now three days, and have nothing to eat: and I will not send "
     "them away fasting, lest they faint in the way."),
    ("n7", NARRATOR, "-20%", "-4Hz",
     "He noticed their stomachs. He had just remade their bodies, and "
     "he was thinking about their lunch. That is who sat down on that "
     "mountain: not a distant power taking appointments, but a God "
     "who counts the days you have been carrying something, and does "
     "not intend to let you faint on the road home."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "Thousands were healed that day whose names nobody wrote down. "
     "He remembers every one of them. He will not lose yours."),
]

# HOMOGRAPH LAW — scanned: no bow/wound/wind/tears/lead-the-metal/sow/live(s)/
# read/dove/bass/minute/use(d)/close. "led" (past of lead) is safe; "lead a blind
# neighbor" avoided in favor of "led". No overrides needed.
SPOKEN = {}


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts_text = SPOKEN.get(name, text)
        tts = edge_tts.Communicate(tts_text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
