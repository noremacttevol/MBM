#!/usr/bin/env python3
"""Generate narration audio for Story Video #40 — The Friend at Midnight
(Luke 11:1-13).

Narrator: en-US-AndrewNeural — plain American, never a Multilingual model.
Jesus voice: en-US-ChristopherNeural — American, never British.

Jesus speaks ONLY exact KJV. Six lines:
  j0 = Luke 11:2      "Our Father which art in heaven" — the word the whole
                      passage turns on, planted early so v13 pays it off
  j1 = Luke 11:5b-6   the man at the door (quoted inside the parable)
  j2 = Luke 11:7      the neighbour's refusal (quoted inside the parable)
  j3 = Luke 11:8      THE VERDICT — the verse card line (PAIRING-LIST.md)
  j4 = Luke 11:9      ask, seek, knock
  j5 = Luke 11:13     THE PAYOFF — how much more shall your heavenly Father
Per the #38/#39 precedent, characters quoted INSIDE a parable are spoken by the
Jesus voice, because Jesus is the one quoting them and the words are exact KJV.

CAPTIONS ARE VERBATIM (Cameron, 2026-07-11): build.py imports these SEGMENTS and
word-wraps each text as the on-screen caption.

TRANSLATION LAW: after every KJV line the narrator gives only the plain modern
meaning and never re-quotes or echoes the KJV wording. This is why the
*shamelessness* study gem lands in n11 — BEFORE Jesus says "importunity" in j3.
The idea gets explained in the narrator's own words first, so the KJV word arrives
already understood and the narrator never has to repeat Jesus's sentence back at
him. Same reason n12 says "an armful" instead of echoing "as many as he needeth",
and n17 says "he was never asleep" instead of echoing "how much more".

CLARITY / WHY-LAW: this parable is misread more than almost any other, and the
misreading is cruel — people hear "pester God until he caves" and come away with a
God who is reluctant and asleep. n14a and n14b exist to say out loud that the
neighbour is the CONTRAST, not the portrait. Without those two segments this video
would do harm. A viewer with zero Bible background must finish able to say: God is
not the man behind the door — he is the opposite of him, so ask without shame.

NUMBER-STRESS LAW: no sentence opens with a bare number. "Three loaves" occurs only
inside Jesus's own KJV line, mid-sentence and stressed. The narrator says "one man's
supper", "an armful", "eight of them" — every count lands late.

MILK FRAMING: God is good. He is not worn down, not annoyed, not asleep; the best
thing he wants to hand you is not bread, it is himself. End on invitation, never
pressure — the door is open and the light is already on.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text) — text is BOTH spoken and captioned.
    # --- s1: v1 — they ask him to teach them to pray ---
    ("n1", NARRATOR, "-20%", "-4Hz",
     "His disciples had watched him pray for years, and watched him come back from it "
     "different. So one morning they asked him for the thing they wanted most. Teach "
     "us how to do that."),
    # --- s2: v2 — the prayer opens on one word ---
    ("n2", NARRATOR, "-22%", "-4Hz",
     "So he gave them a prayer. And the first word of it was not Lord, and it was "
     "not God. It was the word a small child uses."),
    ("j0", JESUS, "-26%", "-6Hz",
     "When ye pray, say, Our Father which art in heaven, Hallowed be thy name."),
    ("n3", NARRATOR, "-22%", "-4Hz",
     "He taught them to walk up to God and call him Father. And then, to show them what "
     "kind of Father he meant, he told a story about a man banging on a door in the "
     "middle of the night."),
    # --- s3: v6 — the guest arrives ---
    ("n4", NARRATOR, "-22%", "-4Hz",
     "People travelled at night there, because the daytime heat could kill you. So a "
     "friend really could turn up at midnight, starving. And you did not send him "
     "away. Feeding a guest was a duty, and the shame of failing belonged to the "
     "whole village."),
    # --- s4: v6 — nothing in the house ---
    ("n5", NARRATOR, "-22%", "-4Hz",
     "So a man opens his door at midnight to a friend who has walked all day. Then "
     "he looks at his own shelf, and there is nothing on it. Not a crumb."),
    # --- s5: v5 — out into the dark ---
    ("n6", NARRATOR, "-22%", "-4Hz",
     "So he picks up his little clay lamp and walks out into a sleeping village, "
     "toward the one door he knows still has bread behind it."),
    # --- s6: v5b-6 — the knock. KJV. ---
    ("j1", JESUS, "-26%", "-6Hz",
     "Friend, lend me three loaves; for a friend of mine in his journey is come to "
     "me, and I have nothing to set before him."),
    ("n7", NARRATOR, "-22%", "-4Hz",
     "Notice who he is asking for. He is standing out there in the dark, begging for "
     "bread he will not eat."),
    # --- s7: v7 — what is on the other side of that door ---
    ("n8", NARRATOR, "-22%", "-4Hz",
     "And look at what is on the other side of that door. A village house was one "
     "room. The whole family slept on one platform under one blanket, with a heavy "
     "bar across the door. Getting up meant waking every child in the house."),
    # --- s8: v7 — the refusal. KJV. ---
    ("j2", JESUS, "-26%", "-6Hz",
     "Trouble me not: the door is now shut, and my children are with me in bed; I "
     "cannot rise and give thee."),
    ("n9", NARRATOR, "-22%", "-4Hz",
     "That is a no. And it is not a lazy no. That is a tired man with sleeping "
     "children and a real reason."),
    # --- s9: v8 — he knocks again, and the gem that unlocks the verse ---
    ("n10", NARRATOR, "-22%", "-4Hz",
     "So the man outside does the thing nobody expected. He knocks again. Louder. "
     "Shutters bang open up the street. Dogs start barking. And he keeps knocking."),
    ("n11", NARRATOR, "-22%", "-4Hz",
     "The word Luke uses here shows up nowhere else in the whole New Testament. Most "
     "Bibles turn it into the word persistence. It does not mean persistence. It "
     "means shamelessness. He was not too proud to look like a fool."),
    # --- s10: v8 — THE VERDICT. Music is already in FULL SILENCE here. ---
    ("j3", JESUS, "-28%", "-6Hz",
     "I say unto you, Though he will not rise and give him, because he is his "
     "friend, yet because of his importunity he will rise and give him as many as he "
     "needeth."),
    ("n12", NARRATOR, "-22%", "-4Hz",
     "He went for enough bread to feed one man. He came home with an armful. And "
     "notice why. The neighbour did not get up because they were friends. He got up "
     "because the man outside would not stop asking."),
    # --- s11: the stranger eats ---
    ("n13", NARRATOR, "-24%", "-4Hz",
     "And in a dark house at midnight, a tired stranger ate a meal he never knew "
     "somebody had fought for."),
    # --- s12: THE TURN. The whole reason this video exists. ---
    ("n14a", NARRATOR, "-22%", "-4Hz",
     "Here is where almost everybody gets this story wrong. People hear it and think "
     "God is the man behind the door. Annoyed. Asleep. Somebody you have to wear "
     "down."),
    ("n14b", NARRATOR, "-22%", "-4Hz",
     "That is the opposite of what he said. The neighbour is not a picture of God. "
     "The neighbour is the contrast. If even a worn-out man with a barred door and a "
     "house full of sleeping kids will get up for you in the end, what do you think "
     "your Father will do, when he was never asleep at all?"),
    # --- s13: v9 — ask, seek, knock. KJV. ---
    ("j4", JESUS, "-26%", "-6Hz",
     "Ask, and it shall be given you; seek, and ye shall find; knock, and it shall "
     "be opened unto you."),
    ("n15", NARRATOR, "-22%", "-4Hz",
     "In the Greek, none of those is a one-time act. Every one of them means keep "
     "coming back."),
    # --- s14: vv11-12 — the lookalikes ---
    ("n16a", NARRATOR, "-22%", "-4Hz",
     "Then he asked them a question. If your son asked you for bread, would you put a "
     "rock in his hand? If he asked for a fish, would you hand him a snake? If he "
     "asked for an egg, would you give him a scorpion?"),
    ("n16b", NARRATOR, "-22%", "-4Hz",
     "Every pair is a lookalike. A smooth river stone is the size and shape of a flat "
     "loaf. A scorpion curls up pale and round, like an egg. He is describing a "
     "father who hands his hungry child a counterfeit. And not one of you, he said, "
     "would ever do it."),
    # --- s15: v13 — THE PAYOFF. Full silence again. ---
    ("j5", JESUS, "-26%", "-6Hz",
     "If ye then, being evil, know how to give good gifts unto your children: how "
     "much more shall your heavenly Father give the Holy Spirit to them that ask "
     "him?"),
    ("n17", NARRATOR, "-22%", "-4Hz",
     "You already know how to be good to your kids. And you are not half as good as "
     "he is. That is the whole argument. Not that God has to be worn down, but that "
     "he was never asleep in the first place."),
    # --- s16: the invitation. Milk framing — no pressure, the door is open. ---
    ("n18", NARRATOR, "-24%", "-4Hz",
     "The man in the story was knocking on a door with somebody asleep behind it. "
     "You are not. Whatever you quit asking for, because you decided it was too "
     "small, or too late, or too much — the light in that house is already on. And "
     "the best thing he has to give you was never bread. It is himself."),
    # --- closing card, read gently (Readable-Card Law) ---
    ("card", NARRATOR, "-26%", "-4Hz",
     "The man at the door was not asking for himself, and he was not too proud to "
     "look foolish. What would you ask God for tonight, if you knew for certain he "
     "was awake?"),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        await save_narration(text, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
