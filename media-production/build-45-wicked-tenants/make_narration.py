#!/usr/bin/env python3
"""Generate narration audio for Story Video #45 — The Wicked Tenants (Mark 12:1-11).

Narrator: en-US-AndrewNeural — plain American, never a Multilingual model.
Jesus voice: en-US-ChristopherNeural — American, never British.

Jesus speaks ONLY exact KJV. Five lines (the whole parable is his direct speech):
  jv1  = Mark 12:1     the owner builds and entrusts the vineyard
  jv2  = Mark 12:2     he sends a servant at the season for the fruit
  jv6  = Mark 12:6     "his wellbeloved, he sent him also" — the verse card. THE HEART.
  jv9  = Mark 12:9     "what shall the lord of the vineyard do..."
  jv10 = Mark 12:10-11 the stone the builders rejected — the head of the corner. THE TURN.
("And he began to speak unto them by parables." is the evangelist's frame, not the
parable proper — carried by the narrator in n1.)

CAPTIONS ARE VERBATIM (Cameron, 2026-07-11): build.py imports these SEGMENTS and
word-wraps each text as the on-screen caption. KJV (Jesus) lines render cream italic.

CARE-FLAG R — RESTRAINT (violence), and J — MERCY-IN-JUDGMENT (CONTENT-CARE.md).
This is the whole job on this story:
  * R: the beatings and the killing are NEVER the picture and NEVER dwelt on in the
    narration. n5/n6 show the servant returning empty and roughed up (aftermath, not
    the blows); n10 says plainly and BRIEFLY that they took the son's life and moves
    straight to the father's grief — the witness carries the weight, not the act. No
    frame or line lingers on violence. QC every frame: would a parent let a ten-year-old
    see this?
  * J: the mercy that is IN the text is the OWNER'S PATIENCE — he keeps sending long
    past the point anyone else would (n5/n6/n7), and finally sends the son he loves most
    (jv6). The reckoning (jv9) is reframed away from doom: the vineyard goes to people
    who will give its fruit (n11), not "watch them be destroyed." And the ending is pure
    hope: the rejected son becomes the cornerstone (jv10/n12) — rejection turned into the
    foundation. The verse-card truth (PAIRING-LIST #45, Mark 12:6): God keeps sending.

TRANSLATION LAW: after every KJV line the narrator gives only the plain modern meaning
and never re-quotes the KJV wording — n2 says "wall / press / lookout" not "hedge /
winefat / tower", n8 says "respect" not "reverence", n12 says "block / reject pile /
the building leans its weight on" not "stone / rejected / head of the corner".

CLOSING CARD IS AN INVITATION, never a fear-question. No "will he destroy you?", no
"are you a wicked tenant?". The owner who keeps sending is the good news.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text) — text is BOTH spoken and captioned.
    # --- s1: the frame — told in the temple, against his accusers ---
    ("n1", NARRATOR, "-20%", "-4Hz",
     "He told this one in the temple, standing in front of the very men who were "
     "plotting against him. And underneath it, it is a story about patience. About "
     "an owner who kept giving people one more chance, long past the point anyone "
     "else would have."),
    # --- s2: v1 — the owner builds and entrusts the vineyard ---
    ("jv1", JESUS, "-26%", "-6Hz",
     "A certain man planted a vineyard, and set an hedge about it, and digged a "
     "place for the winefat, and built a tower, and let it out to husbandmen, and "
     "went into a far country."),
    ("n2", NARRATOR, "-22%", "-4Hz",
     "Picture how much he put into it. He broke the ground and set in the young "
     "vines, ringed it with a wall to guard them, hollowed out a press for the "
     "grapes, and raised a lookout over the whole field. Everything was ready. Then "
     "he handed the whole place to the workers and trusted them with it."),
    # --- s3: he goes away, trusting them ---
    ("n3", NARRATOR, "-22%", "-4Hz",
     "And he left. That is the setup. The owner is far away, the workers have the "
     "run of the place, and all he asked for was a share of the harvest when it "
     "came in, the way any honest agreement works."),
    # --- s4: v2 — he sends a servant for the fruit ---
    ("jv2", JESUS, "-26%", "-6Hz",
     "And at the season he sent to the husbandmen a servant, that he might receive "
     "from the husbandmen of the fruit of the vineyard."),
    ("n4", NARRATOR, "-22%", "-4Hz",
     "So when the season came, he sent a man to collect his share. Not soldiers. "
     "One messenger, walking up the road with an empty basket, expecting nothing "
     "but an honest exchange."),
    # --- s5: aftermath, RESTRAINT — the servant returns empty and roughed up ---
    ("n5", NARRATOR, "-22%", "-4Hz",
     "And the man came back with the basket still empty, and shaken. They had "
     "handled him roughly and sent him off with nothing. Now here is where the "
     "story stops making ordinary sense. Anyone else sends the law next. This "
     "owner sent another messenger."),
    # --- s6: he sends more — the pattern ---
    ("n6", NARRATOR, "-22%", "-4Hz",
     "And they treated that one worse. So he sent another. And another after that. "
     "Message after message, season after season, and every time it came back the "
     "same, or did not come back at all."),
    # --- s7: the patience is the point ---
    ("n7", NARRATOR, "-22%", "-4Hz",
     "Stop and feel how strange that is. Every reasonable line was crossed a long "
     "time ago. He had every right to come with force and end it. Instead he kept "
     "doing the one thing that left him exposed. He kept reaching out to people who "
     "had already shown him exactly who they were."),
    # --- s8: v6 — the beloved son. SACRED SILENCE 1. The heart. ---
    ("jv6", JESUS, "-28%", "-6Hz",
     "Having yet therefore one son, his wellbeloved, he sent him also last unto "
     "them, saying, They will reverence my son."),
    ("n8", NARRATOR, "-22%", "-4Hz",
     "He had one person left. His son. The one he loved most in the world. And he "
     "sent him too, holding on to a hope you can hear him say out loud. Surely they "
     "will respect my son."),
    # --- s9: the plot — RESTRAINT, cold arithmetic, no violence ---
    ("n9", NARRATOR, "-22%", "-4Hz",
     "But when the workers saw the son coming up the road, they did not see a "
     "person. They saw an opening. If the heir is gone, they said to each other, "
     "the whole place falls to us. It is the coldest arithmetic in any story he "
     "ever told."),
    # --- s10: the aftermath — RESTRAINT, the father's grief carries it ---
    ("n10", NARRATOR, "-24%", "-4Hz",
     "You can guess what they chose. The story does not linger on it and neither "
     "will we. They shut him out, and they took his life. And the father who had "
     "waited all those years, still hoping, lost the one he loved most of all. That "
     "is how far the patience went, and what it finally cost him."),
    # --- s11: v9 — the reckoning, reframed toward the fruit, not doom ---
    ("jv9", JESUS, "-26%", "-6Hz",
     "What shall therefore the lord of the vineyard do? he will come and destroy "
     "the husbandmen, and will give the vineyard unto others."),
    ("n11", NARRATOR, "-22%", "-4Hz",
     "Then he turned it into a question. What is the owner going to do now? And the "
     "weight of the answer is not really the punishment. It is that the vineyard "
     "finally passes to people who will actually tend it and give its fruit back. "
     "The trust does not vanish. It goes to hands that will keep it. And then he "
     "reached back into their own scriptures for the last word."),
    # --- s12: v10-11 — the cornerstone. SACRED SILENCE 2. The turn. ---
    ("jv10", JESUS, "-26%", "-6Hz",
     "And have ye not read this scripture; The stone which the builders rejected is "
     "become the head of the corner: This was the Lord's doing, and it is "
     "marvellous in our eyes?"),
    ("n12", NARRATOR, "-22%", "-4Hz",
     "The block the builders threw on the reject pile turned out to be the one the "
     "whole building leans its weight on. He is talking about himself. The son they "
     "were ready to throw out is the foundation everything else gets built on. They "
     "meant it for an ending. It was the beginning."),
    # --- s13: the frame returns — the invitation ---
    ("n13", NARRATOR, "-24%", "-4Hz",
     "The men he told it to heard themselves in it, and it made them furious. But "
     "sitting right underneath their anger is the kindest fact in the whole story. "
     "The owner never stopped sending. Not after the first, not after the tenth, "
     "not even after the worst. That is the God this whole thing is about."),
    # --- closing card, read gently (Readable-Card Law). An INVITATION. ---
    ("card", NARRATOR, "-26%", "-4Hz",
     "He told this to the very people about to reject him, and he was still calling "
     "them in. An owner who keeps sending, after all of that, is not looking for a "
     "reason to be done with you. What would you do with a patience like that?"),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        await save_narration(text, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
