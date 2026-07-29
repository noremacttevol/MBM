#!/usr/bin/env python3
"""Narration for build-05-bent-woman — Luke 13.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

STAYED RED: both existing red beats are Jesus speaking in the flesh and a
red-letter KJV prints both.
  j1  Luke 13:12     'Woman, thou art loosed from thine infirmity.'
  j2  Luke 13:15-16  'Thou hypocrite, doth not each one of you on the sabbath
                      loose his ox or his ass from the stall...'
Neither carries Luke's narration inside it, so neither needed splitting.

THE WOMAN - checked, and she does not speak. Luke 13:11-13 says she was bowed
together, could in no wise lift up herself, and that she glorified God, but the
KJV records no words from her anywhere in the passage. So there is NO pink line
in this build and none was invented. n6 keeps her praise as narration, which is
the honest way to carry it. This is the one place in my six where a woman is at
the centre of the story and scripture still gives her nothing to say - worth
knowing, and worth not papering over.

LIFTED FROM PARAPHRASE - two voices, both SCRIPTURE (blue):
  s14  Luke 13:14  the ruler of the synagogue: 'There are six days in which men
                   ought to work: in them therefore come and be healed, and not on
                   the sabbath day.' - he is the man Jesus answers, and the answer
                   lands harder once the viewer has actually heard him.
  s17  Luke 13:17  Luke's own closing line: 'And when he had said these things,
                   all his adversaries were ashamed: and all the people rejoiced
                   for all the glorious things that were done by him.'

EDITS TO EXISTING NARRATOR TEXT: n7 now ends on 'And he said this to the people'
and hands to s14, with the rest becoming n7b. n11 now opens on 'Luke tells us how
the day ended', hands to s17, and the rest becomes n11b unchanged. Nothing else
was touched.

NOT LIFTED: n10's teaching on 'a daughter of Abraham' turns on phrases already
spoken verbatim inside j2, so it stays narrator retelling - correct, and it is the
best writing in the build.

WHY-LAW: she did not ask, did not push through, did not call out. He called her
first. Milk framing - her worth came before her healing, and he said so in front
of everyone who had stepped around her for eighteen years.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "There was a woman who had been bent over for eighteen years. She could not straighten up at all. Eighteen years of looking at the ground. Eighteen years of knowing people by their sandals instead of their faces. And in all that time, no one had been able to help her."),
    ("n1", NARRATOR, "One sabbath day, Jesus was teaching in a synagogue, and she was there — at the back, by the wall, folded over her walking stick. She had not come to ask him for anything. She was simply there, the way she had been there for years. Present, and unseen."),
    ("n2", NARRATOR, "And in the middle of his teaching, Jesus stopped. He looked past every face in the room, all the way to the back wall. He saw her. And he called her over."),
    ("n3", NARRATOR, "Notice what did not happen. She did not push through a crowd. She did not call out to him. She did not ask. He called her first. Before she said one word, he had already decided."),
    ("n4", NARRATOR, "She made her slow way up the middle of that room, her stick tapping the stone floor, every eye on her. And when she finally stood in front of him — still bent, still staring at the ground — he said this."),
    # Luke 13:12
    ("j1", JESUS, "Woman, thou art loosed from thine infirmity."),
    ("n5a", NARRATOR, "Loosed. In their language it was an everyday word. It meant untied — the same word a farmer used when he untied his animal from its stall. Something that had been knotted for eighteen years was coming undone."),
    ("n5b", NARRATOR, "He laid his hands on her. And slowly — for the first time in eighteen years — she stood up straight."),
    ("n6", NARRATOR, "The first thing she did with a straight back was praise God. Out loud, right there in the middle of the meeting. Eighteen years of silence turned into worship that nobody could stop."),
    ("n7", NARRATOR, "But not everyone rejoiced. The ruler of the synagogue — the man in charge of that meeting — was angry. In his mind, healing counted as work, and the sabbath was the day of rest. And he said this to the people."),
    # Luke 13:14
    ("s14", SCRIPTURE, "There are six days in which men ought to work: in them therefore come and be healed, and not on the sabbath day."),
    ("n7b", NARRATOR, "As if her freedom could have waited one more day. As if it had not already waited eighteen years."),
    ("n8", NARRATOR, "Jesus turned to him. And he did not soften it."),
    # Luke 13:15-16
    ("j2", JESUS, "Thou hypocrite, doth not each one of you on the sabbath loose his ox or his ass from the stall, and lead him away to watering? And ought not this woman, being a daughter of Abraham, whom Satan hath bound, lo, these eighteen years, be loosed from this bond on the sabbath day?"),
    ("n9", NARRATOR, "Every man in that room did exactly that on the sabbath. He untied his ox or his donkey and led it to water, and the rules allowed it — simple kindness to an animal was never against the day of rest. So Jesus asked the only question left. If you will untie an animal on the sabbath, how could it be wrong to untie a daughter?"),
    ("n10", NARRATOR, "And listen to what he called her. A daughter of Abraham. In that room, those words were a declaration — family of the covenant, a child of the promise. For eighteen years she had been the bent woman, the one people stepped around. Now, in front of everyone, he gave her back her name. And notice the order. He did not say she became a daughter by being healed. She was healed because of who she already was. Her worth came first. She belonged — she had always belonged."),
    ("n11", NARRATOR, "Luke tells us how the day ended."),
    # Luke 13:17
    ("s17", SCRIPTURE, "And when he had said these things, all his adversaries were ashamed: and all the people rejoiced for all the glorious things that were done by him."),
    ("n11b", NARRATOR, "And somewhere in that crowd stood a woman seeing faces instead of sandals — standing as straight as the truth he had just told about her."),
    ("n12", NARRATOR, "Is there something you have been carrying so long that you have stopped expecting it to change? He saw her at the back of the room. And he called her first."),
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
