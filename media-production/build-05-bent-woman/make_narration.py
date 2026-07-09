#!/usr/bin/env python3
"""Generate narration audio for Story Video #5 — The Bent-Over Woman
(Luke 13:10-17, the FULL story through verse 17).
Narrator: modern, warm, low, unhurried (American). Plain US model only —
Multilingual models are banned (Cameron, 2026-07-08).
Jesus voice: AMERICAN, never British (Cameron's permanent law, 2026-07-07).
Jesus speaks ONLY exact KJV: Luke 13:12b and Luke 13:15b-16 (fetched from
bible-api.com, not hand-typed).
Script pre-flighted on paper per PRODUCTION-BIBLE.md — see PREFLIGHT.md.
FULL-STORY law: the pack stopped at "daughter of Abraham" and omitted the
ruler of the synagogue — the man j2 is spoken TO — and verse 17's ending.
Both are restored here.
Translation Law: no narrator line echoes KJV wording except the two
translation bridges the pack itself defines (loosed/untied, daughter of
Abraham — the Seed).
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    # n0 — eighteen years (s1 market, low view).
    ("n0", NARRATOR, "-20%", "-4Hz",
     "There was a woman who had been bent over for eighteen years. She "
     "could not straighten up at all. Eighteen years of looking at the "
     "ground. Eighteen years of knowing people by their sandals instead "
     "of their faces. And in all that time, no one had been able to "
     "help her."),
    # n1 — at the back wall (s2).
    ("n1", NARRATOR, "-20%", "-4Hz",
     "One sabbath day, Jesus was teaching in a synagogue, and she was "
     "there — at the back, by the wall, folded over her walking stick. "
     "She had not come to ask him for anything. She was simply there, "
     "the way she had been there for years. Present, and unseen."),
    # n2 — he stops teaching (s3).
    ("n2", NARRATOR, "-22%", "-4Hz",
     "And in the middle of his teaching, Jesus stopped. He looked past "
     "every face in the room, all the way to the back wall. He saw "
     "her. And he called her over."),
    # n3 — called first. Held beat after this line.
    ("n3", NARRATOR, "-22%", "-4Hz",
     "Notice what did not happen. She did not push through a crowd. "
     "She did not call out to him. She did not ask. He called her "
     "first. Before she said one word, he had already decided."),
    # n4 — before him (s5). Sets up j1.
    ("n4", NARRATOR, "-22%", "-4Hz",
     "She made her slow way up the middle of that room, her stick "
     "tapping the stone floor, every eye on her. And when she finally "
     "stood in front of him — still bent, still staring at the ground — "
     "he said this."),
    # J1 — exact KJV Luke 13:12b.
    ("j1", JESUS, "-25%", "-6Hz",
     "Woman, thou art loosed from thine infirmity."),
    # n5a — the "loosed = untied" study gem (pack's translation bridge).
    ("n5a", NARRATOR, "-22%", "-4Hz",
     "Loosed. In their language it was an everyday word. It meant "
     "untied — the same word a farmer used when he untied his animal "
     "from its stall. Something that had been knotted for eighteen "
     "years was coming undone."),
    # n5b — THE PEAK. Music dead before this line. Over the motion clip.
    ("n5b", NARRATOR, "-25%", "-5Hz",
     "He laid his hands on her. And slowly — for the first time in "
     "eighteen years — she stood up straight."),
    # n6 — she glorified God (13:13, restored) (s7).
    ("n6", NARRATOR, "-22%", "-4Hz",
     "The first thing she did with a straight back was praise God. Out "
     "loud, right there in the middle of the meeting. Eighteen years "
     "of silence turned into worship that nobody could stop."),
    # n7 — the ruler objects (13:14, restored). The WHY of the conflict (s8).
    ("n7", NARRATOR, "-22%", "-4Hz",
     "But not everyone rejoiced. The ruler of the synagogue — the man "
     "in charge of that meeting — was angry. In his mind, healing "
     "counted as work, and the sabbath was the day of rest. There are "
     "six working days, he told the crowd. Come and be healed on one "
     "of those. As if her freedom could have waited one more day. As "
     "if it had not already waited eighteen years."),
    # n8 — setup j2.
    ("n8", NARRATOR, "-25%", "-5Hz",
     "Jesus turned to him. And he did not soften it."),
    # J2 — exact KJV Luke 13:15b-16 (s9 donkey watering).
    ("j2", JESUS, "-25%", "-6Hz",
     "Thou hypocrite, doth not each one of you on the sabbath loose "
     "his ox or his ass from the stall, and lead him away to watering? "
     "And ought not this woman, being a daughter of Abraham, whom "
     "Satan hath bound, lo, these eighteen years, be loosed from this "
     "bond on the sabbath day?"),
    # n9 — bridge: their own custom, their own word (s9 hold).
    ("n9", NARRATOR, "-22%", "-4Hz",
     "Every man in that room did exactly that on the sabbath. He "
     "untied his ox or his donkey and led it to water, and the rules "
     "allowed it — simple kindness to an animal was never against the "
     "day of rest. So Jesus asked the only question left. If you will "
     "untie an animal on the sabbath, how could it be wrong to untie "
     "a daughter?"),
    # n10 — daughter of Abraham: the Seed. Worth BEFORE healing (s10).
    ("n10", NARRATOR, "-22%", "-4Hz",
     "And listen to what he called her. A daughter of Abraham. In that "
     "room, those words were a declaration — family of the covenant, a "
     "child of the promise. For eighteen years she had been the bent "
     "woman, the one people stepped around. Now, in front of everyone, "
     "he gave her back her name. And notice the order. He did not say "
     "she became a daughter by being healed. She was healed because of "
     "who she already was. Her worth came first. She belonged — she "
     "had always belonged."),
    # n11 — verse 17 ending, restored (s11).
    ("n11", NARRATOR, "-22%", "-4Hz",
     "Luke tells us how the day ended. The ones who had stood against "
     "Jesus were ashamed, and the whole crowd rejoiced at the glorious "
     "things he was doing. And somewhere in that crowd stood a woman "
     "seeing faces instead of sandals — standing as straight as the "
     "truth he had just told about her."),
    # n12 — closing + card read aloud (Readable-Card Law).
    ("n12", NARRATOR, "-25%", "-5Hz",
     "Is there something you have been carrying so long that you have "
     "stopped expecting it to change? He saw her at the back of the "
     "room. And he called her first."),
]

async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
