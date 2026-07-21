#!/usr/bin/env python3
"""Narration for build-68-multitudes-mountain — Matthew 15.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

STAYED RED: j1, Matthew 15:32, 'I have compassion on the multitude, because
they continue with me now three days, and have nothing to eat: and I will not
send them away fasting, lest they faint in the way.' Verbatim, Jesus in the
flesh, a red-letter KJV prints it. Unchanged, id kept.

LIFTED OUT OF PARAPHRASE -- MATTHEW HIMSELF. This build's whole strength is that
it slows down over two verses of Matthew's narration, and the viewer never
actually heard either of them. Both are now `scripture` (light blue -- Matthew
writing, not Jesus speaking), on the stills the paraphrase already used:
  s30  Matthew 15:30  'And great multitudes came unto him, having with them those
       that were lame, blind, dumb, maimed, and many others, and cast them down at
       Jesus' feet;'  Deliberately cut before 'and he healed them' so that n3 still
       gets to land those four words as the reveal, which is the best beat in the
       build. n2 keeps its id and now frames the verse.
  s31  Matthew 15:31  'Insomuch that the multitude wondered, when they saw the
       dumb to speak, the maimed to be whole, the lame to walk, and the blind to
       see: and they glorified the God of Israel.'  n5 said this in modern English
       without the viewer ever hearing it. n5 is trimmed to the frame and n5b
       carries the retelling and the point about the outsiders.

RETELLING ADDED: n6b after j1, so the Old English lands before n7's commentary.

NO GREEN: nothing in Matthew 15:29-39 is the Father or a voice from heaven.

WOMEN: no woman speaks in Matthew 15:29-39. The Canaanite woman -- who does
speak, magnificently -- is verses 21 to 28, immediately BEFORE this passage, and
n0's 'after the coast' is the reference to her. She is not brought into this cut
because this build is the mountainside, not the coast, and dragging her in would
mean telling a different story. Nothing invented.

NOTE ON ARTWORK: s6-opened-eyes.jpeg is on disk but has no still var in the
build, so no beat can point at it. Left alone.

WHY-LAW: thousands of the best days of thousands of lives are hidden inside four
words -- and he healed them -- and then he worried about their lunch. Milk: he
counts the days you have been carrying something.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "After the coast, Jesus came back toward the Sea of Galilee, climbed partway up a mountain, and sat down. That's all he did. He sat down where he could be found. And the whole region emptied itself onto that mountainside to find him."),
    ("n1", NARRATOR, "Matthew says great multitudes came — and they did not come empty-handed. They came carrying people. Think about what that means on a mountain. Somebody hauled their father up a rocky slope on a plank. Somebody carried a grown brother on their back. Somebody led a blind neighbor by the hand over every single stone. Every step of that climb was somebody's love for somebody, written in sweat."),
    ("n2", NARRATOR, "And they laid them down at his feet. Here is exactly how Matthew writes it:"),
    # Matthew 15:30
    ("s30", SCRIPTURE, "And great multitudes came unto him, having with them those that were lame, blind, dumb, maimed, and many others, and cast them down at Jesus' feet;"),
    ("n3", NARRATOR, "The lame, the blind, the mute, the maimed — he stacks up the words until you can see it: the pain of an entire region, gathered into one place, set down in front of one man. And then the gospel gives us four of the biggest words in the Bible, with no fanfare at all: and he healed them. That's it. No names. No interviews. No list. Thousands of the greatest moments of thousands of lives, all hidden inside one quiet sentence."),
    ("n4", NARRATOR, "Somewhere on that mountain, a woman who had never spoken said her husband's name for the first time. Somewhere an old man's eyes came open on his grandchild's face. Somewhere legs that had been carried up the mountain carried their owner back down it. Multiply that by a hillside. That was the afternoon."),
    ("n5", NARRATOR, "And Matthew tells you what the crowd did with it:"),
    # Matthew 15:31
    ("s31", SCRIPTURE, "Insomuch that the multitude wondered, when they saw the dumb to speak, the maimed to be whole, the lame to walk, and the blind to see: and they glorified the God of Israel."),
    ("n5b", NARRATOR, "They could not believe their eyes — people who had never spoken were talking, broken bodies were whole, the lame were walking, the blind could see — and they gave the glory to the God of Israel. On that side of the sea, many of them were outsiders to Israel entirely. The healing preached better than any sermon."),
    ("n6", NARRATOR, "And here is the detail people miss: they stayed. Three days, on a mountainside, until the food ran out — and nobody wanted to go home. When the disciples started worrying about the crowd's empty stomachs, listen to what Jesus said:"),
    # Matthew 15:32
    ("j1", JESUS, "I have compassion on the multitude, because they continue with me now three days, and have nothing to eat: and I will not send them away fasting, lest they faint in the way."),
    ("n6b", NARRATOR, "I feel for these people, he said. They have been with me three days now and they have nothing to eat, and I am not sending them home hungry, in case they collapse on the way."),
    ("n7", NARRATOR, "He noticed their stomachs. He had just remade their bodies, and he was thinking about their lunch. That is who sat down on that mountain: not a distant power taking appointments, but a God who counts the days you have been carrying something, and does not intend to let you faint on the road home."),
    ("card", NARRATOR, "Thousands were healed that day whose names nobody wrote down. He remembers every one of them. He will not lose yours."),
]

# Homographs this build decides for itself (never auto-replaced globally).
SPOKEN = {}


SPOKEN.update({'faint': 'faynt'})  # round2 in-context A/B winners 2026-07-20 (SWEEP/round2-state.json)

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
