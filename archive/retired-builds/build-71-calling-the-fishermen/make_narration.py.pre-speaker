#!/usr/bin/env python3
"""Generate narration audio for Story Video #84 — Calling the Fishermen (Matthew 4:18-22).

Narrator: en-US-AndrewNeural — plain American, never a Multilingual model.
Jesus voice: en-US-ChristopherNeural — American, never British.

Jesus speaks ONLY exact KJV. One line:
  j1 = Matthew 4:19   "Follow me, and I will make you fishers of men." — the call,
       the single sacred line of the passage (v21 "he called them" is narration, not
       quoted speech, so it is carried by the narrator in n8, not a Jesus line).

CAPTIONS ARE VERBATIM (Cameron, 2026-07-11): build.py imports these SEGMENTS and
word-wraps each text as the on-screen caption.

TRANSLATION LAW: after the KJV line the narrator gives only the plain modern meaning
and never re-quotes or echoes the KJV wording — n4 explains "fishers of men" as "make
it into something that saves people" instead of repeating the phrase. The narrator also
avoids the archaic "straightway"/"immediately" of vv20,22 and says "at once"/"right
then" (n6, n9) so the narration stays plain modern speech, not a second reading of KJV.

WHY-LAW — this story is milk of the plainest kind and the whole job is to let the
KINDNESS land, never guilt. Three things carry it:
  1. He came to THEM (n3) — not a temple, not the qualified; a working lake, wet nets.
  2. He takes what they ALREADY are (n4) — "fishers" — and makes it fishers of men;
     he does not ask them to become someone else first.
  3. He chose the ordinary (n10, n11) — no titles, no training; the men everyone else
     would walk past. The good news is that it was about willingness, not impressiveness.

COST, SHOWN GENTLY: James and John leave Zebedee their father in the boat (n9). The cost
is real and named, but Zebedee is never angry — weathered, tender, letting them go. No
shame framing, no fear.

NUMBER-STRESS LAW: no sentence opens with a bare number. "the ones who followed him ...
were four fishermen" lands the count mid-sentence, never as a flat leading word.

CLOSING CARD IS AN INVITATION, never a fear-question. No "are you ready?", no "could you
leave it all?". The card's question reassures — if he would walk up to a fishing boat,
he would not walk past you.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text) — text is BOTH spoken and captioned.
    # --- s1: the ordinary working morning ---
    ("n1", NARRATOR, "-20%", "-4Hz",
     "It is early morning on the Sea of Galilee. Not a temple, not a synagogue, "
     "not a hall full of scholars. Just a working lake at the start of an ordinary "
     "day, and the men whose whole lives were spent on it."),
    # --- s2: Simon and Andrew at their nets ---
    ("n2", NARRATOR, "-22%", "-4Hz",
     "Two brothers are out in the shallows, Simon and Andrew, throwing a net the "
     "way they had a thousand mornings before. Their hands are rough, their sleeves "
     "are wet. This is not where anyone would think to begin a kingdom."),
    # --- s3: and this is where he comes ---
    ("n3", NARRATOR, "-22%", "-4Hz",
     "And this is where he comes. Not waiting in a holy place for the right people "
     "to find him. Walking the shoreline, in the middle of their workday, straight "
     "up to two men with a net in their hands."),
    # --- s4: v19 — THE CALL. Sacred silence. ---
    ("j1", JESUS, "-26%", "-6Hz",
     "Follow me, and I will make you fishers of men."),
    ("n4", NARRATOR, "-22%", "-4Hz",
     "Notice what he does not say. He does not tell them to become someone else "
     "first. He does not ask them to be scholars or priests. He takes the very "
     "thing they already are, and says he will make it into something that saves "
     "people. He meets them exactly as they are."),
    # --- s5: what that voice did to Simon ---
    ("n5", NARRATOR, "-22%", "-4Hz",
     "Think about what it would take to make a man like Simon put his net down. He "
     "was not a boy with nothing to lose. He had a trade, a boat, a life he was "
     "good at. And one sentence from a stranger on the shore was enough."),
    # --- s6: v20 — they went at once ---
    ("n6", NARRATOR, "-22%", "-4Hz",
     "And they went at once. Not next season, not once they had saved a little "
     "more. That very morning, with the net still wet, they left it on the sand and "
     "followed him, and did not look back."),
    # --- s7: v21 — James and John with Zebedee ---
    ("n7", NARRATOR, "-22%", "-4Hz",
     "A little further along, two more brothers, James and John, sat in a boat "
     "mending the day's torn nets beside Zebedee, their father. The family trade, "
     "three lives on the same water."),
    # --- s8: v21 — and he called them ---
    ("n8", NARRATOR, "-22%", "-4Hz",
     "And he called them too. The same voice, the same invitation, held out to two "
     "more ordinary men doing ordinary work."),
    # --- s9: v22 — they left the ship and their father ---
    ("n9", NARRATOR, "-22%", "-4Hz",
     "And they did the same thing. Right then they climbed out of the boat, left "
     "the half-mended nets in the hull, and went. You can see old Zebedee there, "
     "watching his two sons walk away. The cost was real. But he does not call them "
     "back, and they do not turn around."),
    # --- s10: the four who followed ---
    ("n10", NARRATOR, "-22%", "-4Hz",
     "So the ones who followed him down the shore that morning were four fishermen. "
     "No titles, no training, no credentials. The men he chose first to carry the "
     "whole thing were the men everyone else would have walked right past."),
    # --- s11: the WHY — he chose the ordinary ---
    ("n11", NARRATOR, "-22%", "-4Hz",
     "That is the good news hiding in this small story. He did not go looking for "
     "the qualified. He went looking for the willing. He left the empty boats on "
     "the sand and took the men, because it was never about how impressive they "
     "were. It was only about whether they would come."),
    # --- s12: the invitation, still open ---
    ("n12", NARRATOR, "-24%", "-4Hz",
     "And the strange thing is, that shoreline is not closed. The same voice that "
     "walked up to men at their nets still walks up to ordinary people in the "
     "middle of ordinary days. He is not asking you to clean up first. He is asking "
     "you to come."),
    # --- closing card, read gently (Readable-Card Law). An INVITATION. ---
    ("card", NARRATOR, "-26%", "-4Hz",
     "He walked up to four working men on a normal morning and made them part of "
     "the greatest story ever told, exactly as they were. If he would walk up to a "
     "fishing boat and call the men there by name, what makes you think he would "
     "walk past you?"),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        await save_narration(text, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
