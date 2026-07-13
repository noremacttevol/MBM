#!/usr/bin/env python3
"""Generate narration audio for Story Video #39 — The Pharisee and the Publican
(Luke 18:9-14).

Narrator: en-US-AndrewNeural — plain American, never a Multilingual model.
Jesus voice: en-US-ChristopherNeural — American, never British.

Jesus speaks ONLY exact KJV. Three lines:
  j1 = Luke 18:11-12  the Pharisee's prayer, quoted inside the parable
  j2 = Luke 18:13     the publican's prayer, quoted inside the parable
  j3 = Luke 18:14     THE VERDICT — the verse card line (PAIRING-LIST.md)
Per the #38 precedent, characters quoted INSIDE a parable are spoken by the Jesus
voice, because Jesus is the one quoting them and the words are exact KJV.

CAPTIONS ARE VERBATIM (Cameron, 2026-07-11): build.py imports these SEGMENTS and
word-wraps each text as the on-screen caption.

TRANSLATION LAW: after each KJV line the narrator gives ONLY the plain modern
meaning and never re-quotes or echoes the KJV wording. Note n8 deliberately says
"one guilty man among many" rather than reusing the word from j2 — the idea is
explained, the words stay Jesus's.

NUMBER-STRESS LAW: no sentence opens with a bare number. Every count lands late
and stressed — "fasted twice a week", "the word I five times", "a prayer of only
seven words".

MILK FRAMING (how GOOD he is): the man everyone had written off went home right
with God, for the price of one honest sentence. And Jesus told this to the good
men not to shame them but to let them in too — the only thing keeping the Pharisee
out was his certainty that he was already in. End on invitation, never pressure.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text) — text is BOTH spoken and captioned.
    # --- s1: v9 — who he told it to, and why ---
    ("n1", NARRATOR, "-20%", "-4Hz",
     "Jesus told this story to a certain kind of man. The kind who was sure he "
     "was one of the good ones, and just as sure that other people were not."),
    # --- s2: v10 — two men go up ---
    ("n2", NARRATOR, "-22%", "-4Hz",
     "Two men went up to the temple to pray. One was a Pharisee. The other was a "
     "tax collector. And to anyone watching them climb those steps, it was "
     "obvious which of the two God was pleased with."),
    # --- s3: the WHY — the Pharisee was genuinely, impressively good ---
    ("n3", NARRATOR, "-22%", "-4Hz",
     "The Pharisee was not a fake. God had asked for one fast a year, and this "
     "man fasted twice a week. He gave away a tenth of everything he owned, down "
     "to the herbs in his garden. Ask that city who its best man was, and every "
     "finger would have pointed at him."),
    # --- s4: the WHY — the publican was genuinely, hatefully guilty ---
    ("n4", NARRATOR, "-22%", "-4Hz",
     "The tax collector was exactly what everyone thought he was. He worked for "
     "Rome, the empire occupying his own country, collecting from his own "
     "neighbors and keeping whatever extra he could squeeze out of them. A "
     "traitor with a money box. And he knew it."),
    # --- s5: v11-12 — the prayer that is all about himself ---
    ("n5", NARRATOR, "-22%", "-4Hz",
     "The Pharisee took his place out in the open, where he could be seen, and "
     "lifted his hands to pray. Listen to who his prayer is really about."),
    ("j1", JESUS, "-26%", "-6Hz",
     "God, I thank thee, that I am not as other men are, extortioners, unjust, "
     "adulterers, or even as this publican. I fast twice in the week, I give "
     "tithes of all that I possess."),
    ("n6", NARRATOR, "-22%", "-4Hz",
     "He is not asking God for anything. He is handing God a list of his own "
     "achievements. In one short prayer, he says the word I five times. And he "
     "cannot even finish it without stepping on the man behind him."),
    # --- s6: v13a — standing afar off ---
    ("n7", NARRATOR, "-22%", "-4Hz",
     "The tax collector did not go up front. He stopped at the very back, as far "
     "as a man could get and still be in the temple. He could not bring himself "
     "to lift his eyes. He struck his own chest, the way people do when someone "
     "has died. And he prayed a prayer of only seven words."),
    # --- s7: v13b — the seven words. Music is already in FULL SILENCE here. ---
    ("j2", JESUS, "-28%", "-6Hz",
     "God be merciful to me a sinner."),
    # n8 is split in two so no single caption becomes a 13-line wall of text and
    # no single still has to carry 30 seconds of narration. n8a rides the altar
    # still; n8b lands on the wide shot of the whole temple court — "the only one
    # in the building" spoken over the building.
    ("n8a", NARRATOR, "-24%", "-4Hz",
     "There is more in that prayer than it sounds like. He is standing in the "
     "temple at the hour of sacrifice, while a lamb is being killed for the sins "
     "of the whole nation, and he is asking God to let that mercy fall on him. "
     "Him, personally."),
    ("n8b", NARRATOR, "-24%", "-4Hz",
     "And in Luke's Greek, he does not count himself as one guilty man among "
     "many. He speaks as if he were the only one in the building."),
    # --- s8: both men in one frame ---
    ("n9", NARRATOR, "-22%", "-4Hz",
     "Two men. The same temple. The same God. One of them doing all the talking, "
     "the other barely able to speak. And then Jesus said the sentence that would "
     "have stopped every man listening to him cold."),
    # --- s9: v14 — THE VERDICT (the verse card line). Still in full silence. ---
    ("j3", JESUS, "-26%", "-6Hz",
     "I tell you, this man went down to his house justified rather than the "
     "other: for every one that exalteth himself shall be abased; and he that "
     "humbleth himself shall be exalted."),
    ("n10", NARRATOR, "-22%", "-4Hz",
     "The traitor walked home right with God. The good man walked home exactly as "
     "he came. Not because God is impressed by failure, but because one of them "
     "came holding a list, and the other came holding nothing. Only one of them "
     "was actually asking for anything."),
    # --- s10: he went DOWN to his house justified ---
    ("n11", NARRATOR, "-22%", "-4Hz",
     "He went down those steps a different man, and he had not done one thing to "
     "earn it. He had nothing to offer, and he knew it. That turned out to be the "
     "only thing he needed to get right."),
    # --- s11: "rather than the other" — the good man, unchanged ---
    ("n12", NARRATOR, "-24%", "-4Hz",
     "And the Pharisee? He is still standing there. Still praying. Still certain. "
     "Still fine. That is the saddest part of it. The only thing keeping that man "
     "out was how sure he was that he was already in."),
    # --- s12: the invitation. Milk framing — the door is open, no pressure. ---
    ("n13", NARRATOR, "-24%", "-4Hz",
     "Jesus did not tell this story to shame the good men listening. He told it "
     "to let them in too. The door is not closed to people who have done wrong. "
     "It only closes from the inside, by people convinced they do not need it."),
    # --- closing card, read gently (Readable-Card Law) ---
    ("card", NARRATOR, "-26%", "-4Hz",
     "One man brought God his record. The other brought God the truth. If you "
     "stopped performing for a moment, what would you actually say to him?"),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
