#!/usr/bin/env python3
"""Narration for build-30-net — Matthew 13.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

STAYED RED: both existing red beats are Jesus in the flesh telling a parable and
then explaining it, and a red-letter KJV prints both.
  j1  Matthew 13:47  the net cast into the sea
  j2  Matthew 13:49  'So shall it be at the end of the world: the angels shall come
      forth, and sever the wicked from among the just'
Both verified verbatim against the KJV. Neither moves off red.

THE ONE STRUCTURAL FIX -- j1 WAS CARRYING TWO VERSES. j1 held all of 13:47 AND all
of 13:48 in a single block, spoken over one still while the storyteller had not yet
described the net at all. The sorting on the shore was therefore given away eight
beats before the picture of it arrived. Split in two, each verse landing on the still
that already shows it, and both halves stay JESUS, red -- nothing changes colour:
  j1   Matthew 13:47  'Again, the kingdom of heaven is like unto a net, that was cast
       into the sea, and gathered of every kind:'   -- stays on S1, n2 and n3 retell it.
  j48  Matthew 13:48  'Which, when it was full, they drew to shore, and sat down, and
       gathered the good into vessels, but cast the bad away.'   -- moved onto S3,
       'draw to shore', where n5 was already the retelling and now follows it directly.
This is a split for pacing, not for colour, but it obeys the same rule the colour
splits do: no new artwork, and each half sits on a still the build already had.

ADDED RED. One line of Jesus's explanation was left only in paraphrase:
  j50  Matthew 13:50  'And shall cast them into the furnace of fire: there shall be
       wailing and gnashing of teeth.'  -- placed on S5 straight after j2, which is
       the same sentence continuing, with n8 as the retelling for both.

NO FRAMING SPLIT: 'Again' at the head of 13:47 is Jesus's own word carrying on from
the previous parables, not Matthew's framing, and a red-letter KJV inks it red. There
is no evangelist's 'and he said unto them' in 13:47-50 to lift out.

NO GREEN: no voice from heaven in Matthew 13.

WOMEN: Matthew 13:47-50 records no woman speaking. Nothing added; nothing invented.

PRONUNCIATION: 'sow' and 'sowed' do NOT occur in this build -- checked; the sowing
homograph belongs to build-25, not here. Nothing else in the KJV lines is on the
homograph list, so `spoken` is left empty. A bad respelling is worse than none.

WHY-LAW: the gathering comes first and it is indiscriminate -- the net was thrown
over the whole ocean. The sorting is at the very end, and it belongs to the angels.
It was never handed to you.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "Jesus told one more short story about the kingdom of heaven, and this time he set it out on the water."),
    # Matthew 13:47
    ("j1", JESUS, "Again, the kingdom of heaven is like unto a net, that was cast into the sea, and gathered of every kind:"),
    ("n2", NARRATOR, "Picture fishermen throwing a great wide net off the side of the boat, letting it sink down and drag through the whole sea."),
    ("n3", NARRATOR, "And here is the first beautiful thing. That net does not pick and choose. It sweeps up every kind of fish there is: big ones, small ones, common ones, strange ones, everything the sea has in it, gathered in together."),
    ("n4", NARRATOR, "The net is not fussy about who gets caught up in it. The gathering is wide open. Nobody swimming in that sea is too ordinary, or too far gone, to be swept up into it."),
    # Matthew 13:48
    ("j48", JESUS, "Which, when it was full, they drew to shore, and sat down, and gathered the good into vessels, but cast the bad away."),
    ("n5", NARRATOR, "When the net is full, the fishermen drag the whole heavy thing up onto the shore, and they sit down beside it. And only then, once everyone is already gathered in, does any sorting begin."),
    ("n6", NARRATOR, "They gather the good fish carefully into baskets, keeping them, valuing them, not losing a single one."),
    ("n7", NARRATOR, "And the ones that cannot be kept, they set aside. Jesus said that is a picture of how things finally end."),
    # Matthew 13:49
    ("j2", JESUS, "So shall it be at the end of the world: the angels shall come forth, and sever the wicked from among the just"),
    # Matthew 13:50
    ("j50", JESUS, "And shall cast them into the furnace of fire: there shall be wailing and gnashing of teeth."),
    ("n8", NARRATOR, "There is a real end, and a real sorting. But notice whose job it is. The angels do it. God does it. At the very end. It was never handed to us to do."),
    ("n9", NARRATOR, "So here is what the little story leaves you with. You do not have to spend your life deciding who belongs and who does not. That is not your net, and it is not your sorting."),
    ("n10", NARRATOR, "Your part is simply this: the net was cast for the whole sea, and it was cast for you. The gathering came first. Grace reached out wide enough to catch you up in it."),
    ("n11", NARRATOR, "That is how good he is. He threw the net over the whole ocean of us, of every kind, so that not one soul who wanted to be found would be missed."),
    ("card", NARRATOR, "The net was cast wide enough to gather you in. Will you let yourself be caught up in his grace?"),
]

# Homographs this build decides for itself (never auto-replaced globally).
SPOKEN = {}


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
