#!/usr/bin/env python3
"""Generate narration audio for Story Video #44 — The Two Debtors
(Luke 7:36-50, the parable told in verses 41-43).

Narrator: en-US-AndrewNeural — plain American, never a Multilingual model.
Jesus voice: en-US-ChristopherNeural — American, never British.

Jesus speaks ONLY exact KJV. Five lines:
  j1 = Luke 7:40   "Simon, I have somewhat to say unto thee." — he answers the
                   thought Simon never said out loud.
  j2 = Luke 7:41   the parable set up — the creditor and his two debtors.
  j3 = Luke 7:42   THE VERDICT — the verse-card line (PAIRING-LIST.md):
                   "...he frankly forgave them both."
  j4 = Luke 7:47   THE PAYOFF — "...for she loved much."
  j5 = Luke 7:50   "Thy faith hath saved thee; go in peace."

CAPTIONS ARE VERBATIM (Cameron, 2026-07-11): build.py imports these SEGMENTS and
word-wraps each text as the on-screen caption. What is spoken is what is shown.

TWO-VOICE LAW: only Jesus's own words are the Jesus voice + exact KJV. Simon's
reply inside the exchange ("I suppose that he, to whom he forgave most") is
reported by the NARRATOR in plain words, not quoted — Simon is a real person
answering, not a line Jesus is quoting.

TRANSLATION LAW: after every KJV line the narrator gives only the plain modern
meaning and never re-quotes the KJV wording. "Frankly forgave" is unpacked as
"tore the debts up and asked for nothing back" (n7); the payoff is unpacked by
saying the love came AFTER the forgiveness, never by echoing "loved much".

CLARITY / WHY-LAW: this story is most often flipped backwards — people hear "she
loved much" and think her love EARNED the forgiveness. n9 exists to say out loud
that it is the other way round: she loved much BECAUSE she had already been
forgiven much. The tears are the receipt, not the payment. Without n9 this video
would teach people to try to earn what only comes as a gift.

NUMBER-STRESS LAW: no sentence opens with a bare number. "Five hundred pence" and
"fifty" occur only inside Jesus's own KJV line (j2), mid-sentence and stressed.
The narrator says "two people owed him", "about two years of wages", "a couple of
months" — every count lands late.

MILK FRAMING: God is good. The debt is cancelled freely, before anything is paid
back. The size of your love for him is simply the size of the debt you know he
tore up — so the danger is not being too sinful to love him, it is thinking you
owed too little to bother. End on invitation: let yourself be the one forgiven
much, and you get to be the one who loves much.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text) — text is BOTH spoken and captioned.
    # --- s1: the invitation ---
    ("n1", NARRATOR, "-20%", "-4Hz",
     "A Pharisee named Simon invited Jesus to dinner. It was a careful, "
     "respectable house, and having a well-known teacher at your table made you "
     "look good. So Jesus came, and took his place at the low table with the "
     "other guests."),
    # --- s2: the woman comes in ---
    ("n2", NARRATOR, "-22%", "-4Hz",
     "Then the door opened, and a woman came in who did not belong there. "
     "Everyone in that town knew what she was. She had lived a life the whole "
     "village whispered about, and she walked into a Pharisee's house carrying a "
     "small alabaster jar of costly perfume."),
    # --- s3: at his feet (the heart) ---
    ("n3", NARRATOR, "-22%", "-4Hz",
     "She went straight to his feet. And there, in front of every important man "
     "in the room, she broke. She wept until her tears fell on his feet, and she "
     "wiped them away with her own hair, and kissed them, and poured the perfume "
     "out over them."),
    # --- s4: Simon judges ---
    ("n4", NARRATOR, "-22%", "-4Hz",
     "Simon watched, and said nothing out loud. But inside, he had already made "
     "up his mind. If this man were really a prophet, he thought, he would know "
     "what kind of woman is touching him, and he would never let her near."),
    # --- s4: Jesus answers the unspoken thought. KJV. ---
    ("j1", JESUS, "-26%", "-6Hz",
     "Simon, I have somewhat to say unto thee."),
    # --- s5: the parable set up ---
    ("n5", NARRATOR, "-22%", "-4Hz",
     "And instead of scolding anyone, Jesus told him a small story. There was a "
     "man who lent money, and two people owed him."),
    ("j2", JESUS, "-26%", "-6Hz",
     "There was a certain creditor which had two debtors: the one owed five "
     "hundred pence, and the other fifty."),
    ("n6", NARRATOR, "-22%", "-4Hz",
     "One of them owed about two years of wages. The other owed a couple of "
     "months. Very different weights around their necks. But the same problem: "
     "neither of them had a single coin left to pay it back."),
    # --- s6: THE VERDICT. Music is already in FULL SILENCE here. ---
    ("j3", JESUS, "-28%", "-6Hz",
     "And when they had nothing to pay, he frankly forgave them both. Tell me "
     "therefore, which of them will love him most?"),
    ("n7", NARRATOR, "-22%", "-4Hz",
     "To forgive them frankly meant he simply let it go. He did not lower the "
     "payments. He tore both debts up and asked for nothing back. And Simon "
     "answered, a little carefully: I suppose the one who was let off the most. "
     "You have judged rightly, Jesus told him. The one who was carrying the "
     "heavier weight is the one who walks away loving the most."),
    # --- s7: the two of them, side by side ---
    ("n8", NARRATOR, "-22%", "-4Hz",
     "Then Jesus turned and looked at the woman, but he kept speaking to Simon. "
     "He set the two of them side by side. Simon had given him no water for his "
     "feet; she had washed them with her tears. Simon had given him no greeting; "
     "she had not stopped kissing his feet since she came in."),
    # --- s7: THE PAYOFF. Full silence again. ---
    ("j4", JESUS, "-26%", "-6Hz",
     "Her sins, which are many, are forgiven; for she loved much: but to whom "
     "little is forgiven, the same loveth little."),
    ("n9", NARRATOR, "-22%", "-4Hz",
     "Read that slowly, because it is easy to turn it backwards. She was not "
     "forgiven because she loved so much. She loved so much because she had "
     "already been forgiven. The tears were not the payment. They were what it "
     "looks like when a debt you could never repay is torn up right in front of "
     "you. Simon loved little, because he believed he owed little."),
    # --- s8: go in peace. KJV. ---
    ("j5", JESUS, "-26%", "-6Hz",
     "Thy faith hath saved thee; go in peace."),
    # --- s8: milk close. Invitation, no pressure. ---
    ("n10", NARRATOR, "-24%", "-4Hz",
     "She came in as the woman everybody had already judged. She walked out "
     "saved, and at peace, and loved. And here is the quiet danger in Simon's "
     "seat at the table. If you are sure you are only a small sinner, you will "
     "only ever be a small lover of God. But let yourself be the one forgiven "
     "much, and you get to be the one who loves much. That was never the "
     "punishment. That is the gift."),
    # --- closing card, read gently (Readable-Card Law) ---
    ("card", NARRATOR, "-26%", "-4Hz",
     "The woman knew exactly how much she had been forgiven, and it made her "
     "fearless with love. How much do you believe you have been forgiven?"),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
