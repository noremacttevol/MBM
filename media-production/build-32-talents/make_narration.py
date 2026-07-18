#!/usr/bin/env python3
"""Generate narration audio for Story Video #32 — The Talents
(Matthew 25:14-30).

Narrator: en-US-AndrewNeural — plain American, never a Multilingual model.
Jesus voice: en-US-ChristopherNeural — American, never British.
Jesus speaks ONLY exact KJV, delivering the parable's quoted lines:
Matthew 25:21 (j1, the master's "Well done") and 25:24-25 (j2, the fearful
servant's excuse).

CAPTIONS ARE VERBATIM (Cameron, 2026-07-11): build.py imports these SEGMENTS
and word-wraps each text as the on-screen caption, so every word spoken is on
the screen. After each KJV line the narrator gives ONLY the plain modern meaning
and never re-quotes the KJV words (Translation Law).

A parable told BY Jesus with NO Jesus figure on screen — only his narrating
voice; the master is an ordinary parable character shown fully (STILLS-ONLY,
Law E; face gate trivial — no Jesus figure at all).

MILK FRAMING (how GOOD he is): the third servant buried the gift because he
believed a LIE about his master's heart ("thou art an hard man"). The tragedy
is not that he had little, but that he so badly misjudged the one who trusted
him. God is not that hard man; he trusts you with something real and longs to
say "well done" and share his own joy with you.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text) — text is BOTH spoken and captioned.
    # --- s1: the master entrusts his money ---
    ("n1", NARRATOR, "-20%", "-4Hz",
     "Jesus told a story about a wealthy man who, before a long journey, "
     "entrusted his servants with his own fortune. To one he gave five bags of "
     "silver, to another two, and to another one, each according to what he "
     "could handle."),
    ("n2", NARRATOR, "-22%", "-4Hz",
     "It was a staggering amount of trust. He handed his wealth to his servants "
     "and left them free to use it."),
    # --- s2: the five-bag servant trades and doubles ---
    ("n3", NARRATOR, "-22%", "-4Hz",
     "The servant with five bags went straight to work, trading and investing, "
     "and doubled everything he had been given."),
    # --- s3: the two-bag servant doubles his ---
    ("n4", NARRATOR, "-22%", "-4Hz",
     "The servant with two bags did the same, and doubled his as well. Neither "
     "one played it safe. They took what they were trusted with and made it "
     "grow."),
    # --- s4: the one-bag servant buries it in fear ---
    ("n5", NARRATOR, "-22%", "-4Hz",
     "But the servant with one bag was afraid. So he dug a hole in the ground, "
     "buried the silver, and did nothing with it at all."),
    # --- s5: the master returns, overjoyed ---
    ("n6", NARRATOR, "-22%", "-4Hz",
     "When the master came home, the first two servants showed him what they "
     "had made. And he was overjoyed."),
    # --- s6: Well done (KJV j1), the peak ---
    ("j1", JESUS, "-26%", "-6Hz",
     "Well done, thou good and faithful servant: thou hast been faithful over a "
     "few things, I will make thee ruler over many things: enter thou into the "
     "joy of thy lord."),
    ("n7", NARRATOR, "-22%", "-4Hz",
     "Enter into the joy of your master. He did not just reward them, he shared "
     "his own joy with them, and welcomed them deeper in."),
    # --- s7: the fearful servant's excuse (KJV j2) ---
    ("n8", NARRATOR, "-22%", "-4Hz",
     "Then the last servant came, dug up his one buried bag, and handed it back "
     "untouched. And listen to why he had buried it."),
    ("j2", JESUS, "-25%", "-6Hz",
     "Lord, I knew thee that thou art an hard man, and I was afraid, and went "
     "and hid thy talent in the earth."),
    ("n9", NARRATOR, "-22%", "-4Hz",
     "There it is. He buried the gift because he believed his master was harsh "
     "and cruel. He was wrong about him. His fear was built on a lie about who "
     "his master really was, and that lie cost him everything."),
    # --- s6 reprise: the hopeful reframe ---
    ("n10", NARRATOR, "-24%", "-4Hz",
     "That is the real tragedy of the story. Not that he had little, but that "
     "he so badly misjudged the heart of the one who trusted him. God is not "
     "the hard man that servant imagined. He trusts you with something real, "
     "and he is longing to say to you, well done, and to share his joy."),
    # --- closing card, read gently (Readable-Card Law) ---
    ("card", NARRATOR, "-26%", "-4Hz",
     "What has God trusted you with that fear has kept you from using? What if "
     "he is kinder than you think?"),
]


# SPOKEN overrides: text sent to the TTS instead of the caption text, to correct a
# word the neural voice reads wrong. The ON-SCREEN caption is unchanged (build.py
# captions from SEGMENTS text); only the spoken audio uses these.
#   card: edge-tts reads "kinder" with the German/kindergarten short-i — "KIN-der"
#   (Cameron 2026-07-17: "pronounced Kender"). Whisper lexicon-corrects it so a
#   transcript check can't catch this; verified acoustically (log-mel DTW vs
#   reference words "kind"/"kin", Machine C 2026-07-17): plain "kinder" renders
#   the /ɪ/ defect, "kynder" renders the correct /kaɪndər/.
SPOKEN = {
    "card": "What has God trusted you with that fear has kept you from using? What if "
            "he is kynder than you think?",
    #   n10: mid-sentence "say to you, well done, and" glides into "while done"
    #   (caught by whisper word-timestamps during the kinder fix, Machine C
    #   2026-07-17). A colon + period around "Well done" makes it land as its
    #   own stressed phrase; verified "well done" by the same check.
    "n10": "That is the real tragedy of the story. Not that he had little, but that "
           "he so badly misjudged the heart of the one who trusted him. God is not "
           "the hard man that servant imagined. He trusts you with something real, "
           "and he is longing to say to you: Well done. And to share his joy.",
}


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        spoken = SPOKEN.get(name, text)
        await save_narration(spoken, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
