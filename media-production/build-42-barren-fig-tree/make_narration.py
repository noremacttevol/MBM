#!/usr/bin/env python3
"""Generate narration audio for Story Video #42 — The Barren Fig Tree Spared (Luke 13:6-9).

Narrator: en-US-AndrewNeural — plain American, never a Multilingual model.
Jesus voice: en-US-ChristopherNeural — American, never British.

Jesus speaks ONLY exact KJV. Four lines (the whole parable is his direct speech):
  jv6 = Luke 13:6   "A certain man had a fig tree planted in his vineyard..."
  jv7 = Luke 13:7   the owner's verdict — "cut it down; why cumbereth it the ground?"
  jv8 = Luke 13:8   the gardener's plea — "let it alone this year also..."   THE HEART
  jv9 = Luke 13:9   "And if it bear fruit, well..."
("He spake also this parable;" is Luke's own narration, not the parable proper —
it is carried by the narrator in n1, so the Jesus voice speaks only the story itself.)

CAPTIONS ARE VERBATIM (Cameron, 2026-07-11): build.py imports these SEGMENTS and
word-wraps each text as the on-screen caption. KJV (Jesus) lines render cream italic.

CARE-FLAG J — MERCY-IN-JUDGMENT (CONTENT-CARE.md). This is the whole job on this story.
Told flat, the barren fig tree rebuilds the cruel-God picture: produce or be destroyed.
The mercy that is IN the text has to be found and spoken out loud, and it is everywhere:
the tree is GIVEN another year (v8); the gardener does not scold it, he asks to WORK for
it — loosen the soil, feed it by hand (v8); and the reprieve is not earned by the tree,
it is asked for on the tree's behalf by someone who cares for it. The axe is never swung.
The closing card is an INVITATION, never a fear-question ("are you barren?", "will you be
cut down?" are forbidden). Fear is not this app's tool because it was not his.

TRANSLATION LAW: after every KJV line the narrator gives only the plain modern meaning
and never re-quotes or echoes the KJV wording. That is why n5 says "holding a place a
fruitful one could use" instead of echoing "cumbereth the ground", n7 says "break up the
hard packed earth" instead of echoing "dig about it", and n8 says "feed it" instead of
echoing "dung it".

NUMBER-STRESS LAW: no sentence opens with a bare number. "Coming up on three seasons
now..." lands the count mid-sentence, stressed, never as a flat leading word.

THE TURN (n10/n10b) is why this is milk at all: the tree had not changed — it got its
year because someone stood between it and the axe and asked. Grace is asked FOR you before
you have earned a thing. That is the good news the warning was hiding.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text) — text is BOTH spoken and captioned.
    # --- s1: the frame — he begins the parable ---
    ("n1", NARRATOR, "-20%", "-4Hz",
     "He told them a short story about a tree that was not doing its job. It "
     "sounds at first like a warning. Stay with it, because it turns into one of "
     "the kindest things he ever said about being given more time."),
    # --- s2: v6 — a fig tree in a vineyard, given the best of everything ---
    ("jv6", JESUS, "-26%", "-6Hz",
     "A certain man had a fig tree planted in his vineyard; and he came and "
     "sought fruit thereon, and found none."),
    ("n2", NARRATOR, "-22%", "-4Hz",
     "A fig tree in a vineyard had the best spot on the whole property. Deep "
     "worked soil, water meant for the grapes, a wall around it, full sun. "
     "Everything a tree could want was already handed to it. All it had to do "
     "was grow figs."),
    # --- s3: he came looking, and there was nothing ---
    ("n3", NARRATOR, "-22%", "-4Hz",
     "So the owner came out to pick a few, the way you would. And there was "
     "nothing on it. Not a small crop. Not a late one. Bare leaves, and no fruit "
     "at all."),
    # --- s4: three years of it ---
    ("n4", NARRATOR, "-22%", "-4Hz",
     "And this was not the first time. Coming up on three seasons now he had "
     "walked out to that same tree expecting figs, and walked back with empty "
     "hands every time. A fig tree gets a fair trial, and this one had had a "
     "long one."),
    # --- s5: v7 — THE VERDICT. Sacred silence 1. ---
    ("jv7", JESUS, "-26%", "-6Hz",
     "Then said he unto the dresser of his vineyard, Behold, these three years I "
     "come seeking fruit on this fig tree, and find none: cut it down; why "
     "cumbereth it the ground?"),
    ("n5", NARRATOR, "-22%", "-4Hz",
     "And you can hear that he is not being cruel. His last words are just plain "
     "sense. The tree is holding a place a fruitful one could be using, and any "
     "farmer in that crowd would have nodded. It was a fair call."),
    # --- s6: v8 — THE PLEA. Sacred silence 2. The heart of the whole video. ---
    ("jv8", JESUS, "-28%", "-6Hz",
     "And he answering said unto him, Lord, let it alone this year also, till I "
     "shall dig about it, and dung it:"),
    ("n6", NARRATOR, "-22%", "-4Hz",
     "And then someone speaks up for the tree. The man who tends it. He does not "
     "argue that the owner is wrong. He just asks for one more year, and takes "
     "the tree's side when it cannot speak for itself."),
    # --- s7: what he offers to DO — loosen the soil ---
    ("n7", NARRATOR, "-22%", "-4Hz",
     "And look at what he offers to do with that year. Get down and break up the "
     "hard, packed earth around the roots, so the tree can finally breathe and "
     "drink. Not scold the tree. Work the soil."),
    # --- s8: and feed it — the humblest work ---
    ("n8", NARRATOR, "-22%", "-4Hz",
     "And then feed it. The lowest, messiest job on the whole farm, done by hand "
     "at the foot of a tree that has given him nothing back. He is not asking for "
     "time so he can wait and watch. He is asking for time so he can go to work."),
    # --- s9: v9 — and if it bear fruit, well ---
    ("jv9", JESUS, "-26%", "-6Hz",
     "And if it bear fruit, well: and if not, then after that thou shalt cut it "
     "down."),
    ("n9", NARRATOR, "-22%", "-4Hz",
     "And if it comes to life, wonderful. And if it does not, we will face that "
     "when it comes. But not today. The axe goes back against the wall, and the "
     "tree gets its year."),
    # --- s10: THE TURN — the tree had not changed ---
    ("n10", NARRATOR, "-22%", "-4Hz",
     "Here is the part worth sitting with. The tree had not changed. It had not "
     "turned itself around or grown a single fig overnight. It got its extra year "
     "for one reason only. Someone who cared for it stood between it and the axe "
     "and asked."),
    ("n10b", NARRATOR, "-22%", "-4Hz",
     "That is the whole picture. Not a tree earning its keep. A gardener buying "
     "it time it could never have bought for itself."),
    # --- s11: he never says who the gardener is ---
    ("n11", NARRATOR, "-22%", "-4Hz",
     "He never tells us who the gardener is. He does not have to. Everyone "
     "listening knew what it felt like to be the barren tree. And every one of "
     "them just heard that there is Someone in the vineyard whose first move is "
     "to ask for more time on your behalf."),
    # --- s12: the frame returns — the invitation ---
    ("n12", NARRATOR, "-24%", "-4Hz",
     "So the story he told to warn them turns out to be the story that saves "
     "them. The owner had every right to the axe. The gardener asked for the "
     "year. And the tree is still standing."),
    # --- closing card, read gently (Readable-Card Law). An INVITATION. ---
    ("card", NARRATOR, "-26%", "-4Hz",
     "He told a story where the tree that had earned the axe got another year "
     "instead, because someone knelt down in the dirt and asked for it. What "
     "would you say to a Gardener like that?"),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
