#!/usr/bin/env python3
"""Generate narration audio for Story Video #25 — The Wheat and the Tares
(Matthew 13:24-30, 36-43).

Narrator: en-US-AndrewNeural — plain American, never a Multilingual model.
Jesus voice: en-US-ChristopherNeural — American, never British.
Jesus speaks ONLY exact KJV: the householder's patient reply Matthew 13:29-30 (j1)
and the promise Matthew 13:43 (j2). (In the parable j1 is the householder's
words; Jesus is the storyteller quoting them, so the Jesus voice carries them —
same pattern as #23.)

CAPTIONS ARE VERBATIM. After each KJV line the narrator gives ONLY the plain
modern meaning and never re-quotes the KJV words (Translation Law).

Stills-only parable (Law E): NO Jesus figure on screen — his narrating voice +
KJV only; face gate trivial. Every character in the story (the farmer, his
workers, the enemy) is shown fully.

MILK: this parable has a hard edge in scripture (the furnace, the wailing). We
keep the LIGHT on the good news the story is really about — God's PATIENCE is
mercy: he will not rip out the weeds early because he refuses to lose one stalk
of good wheat, and in the end the righteous shine. The judgment is stated
plainly and gently (the weeds are gathered away at harvest), never dwelt on
luridly. WHY-LAW / STUDY-GEM: the "tare" (darnel) looks almost identical to young
wheat until the heads form, and their roots tangle together — so pulling the
weeds early would uproot the wheat. That is the whole reason he waits.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text) — text is BOTH spoken and captioned.
    # --- s1: the good seed ---
    ("n1", NARRATOR, "-20%", "-4Hz",
     "Jesus told them another story. The kingdom of heaven, he said, is like a "
     "farmer who sowed good seed all across his field."),
    ("n2", NARRATOR, "-22%", "-4Hz",
     "It was clean, good wheat seed. He wanted a good harvest, and he did "
     "everything right."),
    # --- s2: the enemy sows tares by night ---
    ("n3", NARRATOR, "-22%", "-4Hz",
     "But that night, while everyone was asleep, an enemy of his crept into the "
     "field and scattered weed seeds all through the wheat. Then he slipped "
     "away, and no one saw."),
    ("n4", NARRATOR, "-22%", "-4Hz",
     "The weed he chose looks almost exactly like young wheat. You cannot tell "
     "them apart until they grow up and the heads appear."),
    # --- s3: both come up together ---
    ("n5", NARRATOR, "-22%", "-4Hz",
     "So the wheat came up green and strong, and right in the middle of it, so "
     "did the weeds. Now anyone could see the field was full of both."),
    # --- s4: the servants ask ---
    ("n6", NARRATOR, "-22%", "-4Hz",
     "The workers were upset. They came to the farmer and said, did you not "
     "plant good seed? Where did all these weeds come from?"),
    ("n7", NARRATOR, "-22%", "-4Hz",
     "He told them, an enemy has done this. And they asked, do you want us to go "
     "and pull all the weeds out right now?"),
    # --- s5: let both grow (KJV j1 = Matthew 13:29-30) ---
    ("n8", NARRATOR, "-22%", "-4Hz",
     "And here is where you see what kind of man he is. He did not send them "
     "tearing through the field. He said, no."),
    ("j1", JESUS, "-26%", "-6Hz",
     "Nay; lest while ye gather up the tares, ye root up also the wheat with "
     "them. Let both grow together until the harvest."),
    ("n9", NARRATOR, "-23%", "-4Hz",
     "In other words: if you rip the weeds out now, their roots are tangled "
     "around the wheat, and you will tear up the good plants along with them. So "
     "let them both grow. He would rather wait than lose a single stalk of "
     "wheat."),
    # --- s6: patience protects the crop ---
    ("n10", NARRATOR, "-22%", "-4Hz",
     "So the farmer waited. All season long the wheat and the weeds grew up side "
     "by side, and he let them, because his patience was protecting the crop he "
     "loved."),
    # --- s7: the harvest sorts it ---
    ("n11", NARRATOR, "-22%", "-4Hz",
     "Then harvest came. And at harvest, the two are finally easy to tell apart. "
     "The reapers gathered the weeds and bundled them away, and then gathered "
     "all the good wheat safely into the barn."),
    ("n12", NARRATOR, "-22%", "-4Hz",
     "Nothing good was lost. Everything the farmer had waited and hoped for came "
     "safely home."),
    # --- s8: the righteous shine (KJV j2 = Matthew 13:43) ---
    ("n13", NARRATOR, "-22%", "-4Hz",
     "Jesus said that is how God works with the world. He is not quick to rip "
     "things up. He gives time, because his patience is mercy. And in the end,"),
    ("j2", JESUS, "-25%", "-6Hz",
     "Then shall the righteous shine forth as the sun in the kingdom of their "
     "Father. Who hath ears to hear, let him hear."),
    ("n14", NARRATOR, "-24%", "-4Hz",
     "The people who belong to him will shine like the sun. That is how good he "
     "is. He is patient enough to wait for you, and he will not let one good "
     "stalk be lost."),
    # --- closing card, read gently (Readable-Card Law) ---
    ("card", NARRATOR, "-26%", "-4Hz",
     "He is patient enough to wait for you. Will you grow toward the light?"),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        await save_narration(text, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
