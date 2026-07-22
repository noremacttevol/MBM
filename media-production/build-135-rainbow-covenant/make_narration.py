#!/usr/bin/env python3
"""Narration for build-135-rainbow-covenant — Genesis 9.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

All five red beats - jv22, jv9, jv11, jv13, jv16 - are God speaking in Genesis 8 and 9.
Old Testament, so a red-letter KJV prints every one of them black. All five become GOD
(green). Nothing in this build is `jesus`. That is the entire doctrinal change here,
and it is a big one: this video was five-sixths red.

All five were already verbatim KJV and all five already had a narrator retelling after
them, so the running order barely moves. This build was in good shape.

ADDED: gv91, Genesis 9:1 - 'Be fruitful, and multiply, and replenish the earth' - on
S2, the first steps off the ark. The video showed eight people walking out onto wet
grass with nothing, and the first thing God actually said to them was a blessing. That
belonged in it.

LEFT AS PARAPHRASE ON PURPOSE:
  Genesis 8:21, God's word over the altar ('I will not again curse the ground'). The
  verse runs through a middle clause about the imagination of man's heart, and quoting
  around it would mean stitching two fragments together. Not doing that - n3 stays
  narrator.
  Noah is never recorded speaking in Genesis 8 or 9 except in the Canaan passage at
  9:25-27, which is meat and does not belong in this video. So there is no SCRIPTURE
  beat here. No woman speaks anywhere in the passage - checked.

SPOKEN: 'bow' is respelled 'boh'. In this build every use of the word means the archery
bow, the token in the cloud, never bowing down. Verified across jv13, jv16 and n8.

MILK FRAMING: a one-way covenant. Noah signs nothing and earns nothing. God binds
himself, and hangs the reminder where he will see it.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import GOD, NARRATOR

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "The rain had stopped. For the better part of a year, one family and a great wooden boat full of animals had ridden out the end of the world they knew. Then one morning the ark sat still on a mountainside, and the earth lay quiet and washed and new."),
    ("n2", NARRATOR, "Noah and his family stepped out onto wet grass under an open sky. There were eight of them, and everything they had ever known was gone. The whole human story was starting over. And the very first thing God said to them was not a warning."),
    # Genesis 9:1
    ("gv91", GOD, "Be fruitful, and multiply, and replenish the earth."),
    ("n2b", NARRATOR, "Fill it back up. Go live. Eight people standing in the wreckage of a drowned world, and God's opening word to them is a blessing and a future. But one heavy question still hung over it all. Could anyone trust the sky again?"),
    ("n3", NARRATOR, "Here is the first thing Noah built in the new world. Not a house. Not a fence. He gathered stones and built an altar, and he gave thanks. And God answered that small smoking altar with a promise about the whole future."),
    # Genesis 8:22
    ("jv22", GOD, "While the earth remaineth, seedtime and harvest, and cold and heat, and summer and winter, and day and night shall not cease."),
    ("n4", NARRATOR, "Planting time and gathering time, winter and summer, morning and night. The world would keep its rhythm for as long as it stands. But God was not finished, because he knew something about these eight people. He knew what rain now meant to them."),
    ("n5", NARRATOR, "Think about the first time clouds rolled in after the flood. For Noah's family, a dark sky was no longer just weather. It was the memory of everything they had lost. And God did not scold them for being afraid. He moved to meet the fear."),
    # Genesis 9:9
    ("jv9", GOD, "And I, behold, I establish my covenant with you, and with your seed after you."),
    ("n6", NARRATOR, "A covenant is the Bible's most serious word for a promise, one that binds the person who makes it. And notice who is doing the binding here. Noah is not asked to promise anything, sign anything, or earn anything. God binds himself, one way, for free. To Noah, to his children, and to every living creature that walked off that boat."),
    # Genesis 9:11
    ("jv11", GOD, "And I will establish my covenant with you; neither shall all flesh be cut off any more by the waters of a flood; neither shall there any more be a flood to destroy the earth."),
    ("n7", NARRATOR, "Never again. That is the whole promise, with no conditions attached and no expiration date. And then God does something wonderfully tender. He gives the promise a sign you can see with your eyes."),
    # Genesis 9:13
    ("jv13", GOD, "I do set my bow in the cloud, and it shall be for a token of a covenant between me and the earth."),
    ("n8", NARRATOR, "The word there is simply bow, and it is the same word the Bible uses for a battle bow, a weapon of war. God hangs a bow in the clouds, unstrung, aimed away from the earth. It is the picture of a warrior hanging up his weapon on the wall. The storm between heaven and earth is over."),
    # Genesis 9:16
    ("jv16", GOD, "And the bow shall be in the cloud; and I will look upon it, that I may remember the everlasting covenant between God and every living creature of all flesh that is upon the earth."),
    ("n9", NARRATOR, "Did you catch who the sign is for? God set the reminder where he would see it. The rainbow is the string God tied around his own finger. Before it ever comforts you, it is his own promise, kept deliberately in his own sight."),
    ("n10", NARRATOR, "And the promise held. Rain has come and gone for thousands of years since that mountainside, and when the shower passes, the same sign still climbs the sky. Children point at it. Nobody runs from it. That is what it feels like to live inside a promise God is keeping."),
    ("n11", NARRATOR, "This is the God the whole story has been about. A God who knows exactly what frightens his people, and answers fear with beauty instead of blame. A God who binds himself with promises, and then keeps them. He has not changed."),
    ("card", NARRATOR, "After the flood, God made a one-way promise, and hung the reminder where he himself would see it. The next rainbow you see is God remembering. What might change for you, if you believed he keeps his promises?"),
]

# Homographs this build decides for itself (never auto-replaced globally).
SPOKEN = {
    "bow": "boh",
}


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
