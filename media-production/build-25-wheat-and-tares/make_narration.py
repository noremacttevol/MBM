#!/usr/bin/env python3
"""Narration for build-25-wheat-and-tares — Matthew 13.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

STAYED RED: both existing red beats are Jesus in the flesh telling and closing a
parable, and a red-letter KJV prints both.
  j1  Matthew 13:29-30  'Nay; lest while ye gather up the tares... Let both grow
      together until the harvest.'  -- the householder's words INSIDE the parable,
      which is still Jesus speaking. Red is correct and it stays red.
  j2  Matthew 13:43     'Then shall the righteous shine forth as the sun...'

THE FRAMING SPLIT. Matthew 13:24 reads in full: 'Another parable put he forth unto
them, saying, The kingdom of heaven is likened unto a man which sowed good seed in
his field:'. Everything before 'The kingdom' is Matthew writing and a red-letter KJV
leaves it black. The build had that frame only as modern paraphrase inside n1, so
the verse is now split properly, BOTH HALVES ON THE SAME STILL S1 -- no new artwork:
  s24  Matthew 13:24  'Another parable put he forth unto them, saying,'  SCRIPTURE.
  j24  Matthew 13:24  'The kingdom of heaven is likened unto a man which sowed good
       seed in his field:'  JESUS, red.
n1 keeps its id and is trimmed to the retelling only -- its old opening sentence
'Jesus told them another story' was the frame and is now carried by s24.

ADDED RED, ALL INSIDE THE PARABLE. Three more of Jesus's own lines were being told
only in the storyteller's paraphrase. Every one of them a red-letter KJV prints red,
including the servants' dialogue -- inside a parable the characters' words are
Jesus's words:
  j25  Matthew 13:25  'But while men slept, his enemy came and sowed tares among the
       wheat, and went his way.'   -- n3 keeps its text and now retells it.
  j27  Matthew 13:27  'Sir, didst thou not sow good seed in thy field? from whence
       then hath it tares?'  -- the SERVANTS speaking, and still red. n6 retells.
  j30  Matthew 13:30  'Gather ye together first the tares, and bind them in bundles
       to burn them: but gather the wheat into my barn.'  -- n11 retells.
Red now lands on S1, S2, S4, S5, S7 and S8, with a narrator retelling after each.
Verse 26 (S3, n5) and the master's 'An enemy hath done this' are deliberately LEFT
in the storyteller's voice -- running the whole parable back to back in Old English
would turn the middle of the video into a recitation. Verbatim and retold, alternating.

NO GREEN: no voice from heaven in Matthew 13.

WOMEN: Matthew 13:24-30, 36-43 records no woman speaking. Nothing added; nothing
invented.

PRONUNCIATION: 'sow' and 'sowed' are on the SPEAKER-LAW homograph list -- the
seed-scattering word rhymes with 'so', not with 'cow'. Respelled in `spoken`; the
captions keep the true spelling. 'tares' is left alone -- it already reads correctly
and a bad respelling is worse than none.

WHY-LAW: the farmer would rather wait a whole season than lose one stalk of wheat.
His patience is not slowness, it is mercy, and it is aimed at protecting you.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    # Matthew 13:24
    ("s24", SCRIPTURE, "Another parable put he forth unto them, saying,"),
    # Matthew 13:24
    ("j24", JESUS, "The kingdom of heaven is likened unto a man which sowed good seed in his field:"),
    ("n1", NARRATOR, "The kingdom of heaven, he said, is like a farmer who sowed good seed all across his field."),
    ("n2", NARRATOR, "It was clean, good wheat seed. He wanted a good harvest, and he did everything right."),
    # Matthew 13:25
    ("j25", JESUS, "But while men slept, his enemy came and sowed tares among the wheat, and went his way."),
    ("n3", NARRATOR, "But that night, while everyone was asleep, an enemy of his crept into the field and scattered weed seeds all through the wheat. Then he slipped away, and no one saw."),
    ("n4", NARRATOR, "The weed he chose looks almost exactly like young wheat. You cannot tell them apart until they grow up and the heads appear."),
    ("n5", NARRATOR, "So the wheat came up green and strong, and right in the middle of it, so did the weeds. Now anyone could see the field was full of both."),
    # Matthew 13:27
    ("j27", JESUS, "Sir, didst thou not sow good seed in thy field? from whence then hath it tares?"),
    ("n6", NARRATOR, "The workers were upset. They came to the farmer and said, did you not plant good seed? Where did all these weeds come from?"),
    ("n7", NARRATOR, "He told them, an enemy has done this. And they asked, do you want us to go and pull all the weeds out right now?"),
    ("n8", NARRATOR, "And here is where you see what kind of man he is. He did not send them tearing through the field. He said, no."),
    # Matthew 13:29-30
    ("j1", JESUS, "Nay; lest while ye gather up the tares, ye root up also the wheat with them. Let both grow together until the harvest."),
    ("n9", NARRATOR, "In other words: if you rip the weeds out now, their roots are tangled around the wheat, and you will tear up the good plants along with them. So let them both grow. He would rather wait than lose a single stalk of wheat."),
    ("n10", NARRATOR, "So the farmer waited. All season long the wheat and the weeds grew up side by side, and he let them, because his patience was protecting the crop he loved."),
    # Matthew 13:30
    ("j30", JESUS, "Gather ye together first the tares, and bind them in bundles to burn them: but gather the wheat into my barn."),
    ("n11", NARRATOR, "Then harvest came. And at harvest, the two are finally easy to tell apart. The reapers gathered the weeds and bundled them away, and then gathered all the good wheat safely into the barn."),
    ("n12", NARRATOR, "Nothing good was lost. Everything the farmer had waited and hoped for came safely home."),
    ("n13", NARRATOR, "Jesus said that is how God works with the world. He is not quick to rip things up. He gives time, because his patience is mercy. And in the end,"),
    # Matthew 13:43
    ("j2", JESUS, "Then shall the righteous shine forth as the sun in the kingdom of their Father. Who hath ears to hear, let him hear."),
    ("n14", NARRATOR, "The people who belong to him will shine like the sun. That is how good he is. He is patient enough to wait for you, and he will not let one good stalk be lost."),
    ("card", NARRATOR, "He is patient enough to wait for you. Will you grow toward the light?"),
]

# Homographs this build decides for itself (never auto-replaced globally).
SPOKEN = {
    "sow": "soh",
    "sowed": "sohd",
}


async def main():
    os.makedirs("audio", exist_ok=True)
    for name, speaker, text in SEGMENTS:
        flagged = [w for w in audit(text) if w not in SPOKEN]
        if flagged:
            print(f"  ! {name}: undecided homograph(s) {flagged}")
        await save_speaker_narration(spoken_text(text, SPOKEN), speaker,
                                     f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3  [{speaker}]")


if __name__ == "__main__":
    asyncio.run(main())
