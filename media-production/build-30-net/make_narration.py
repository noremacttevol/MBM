#!/usr/bin/env python3
"""Generate narration audio for Story Video #30 — The Net / The Dragnet
(Matthew 13:47-50).

Narrator: en-US-AndrewNeural — plain American, never a Multilingual model.
Jesus voice: en-US-ChristopherNeural — American, never British.
Jesus speaks ONLY exact KJV: Matthew 13:47-48 (j1) and 13:49 (j2).

CAPTIONS ARE VERBATIM. After each KJV line the narrator gives ONLY the plain
modern meaning and never re-quotes the KJV words (Translation Law).

Stills-only parable (Law E): NO Jesus figure on screen — his narrating voice +
KJV only; face gate trivial. The fishermen are characters in the story, shown
fully.

MILK: this parable has the same hard edge as #25 (the furnace of fire, the
wailing — Matt 13:50). We keep the LIGHT on the good news THE-200 names:
"gathering of every kind comes before sorting." The net is cast wide over the
WHOLE sea and gathers EVERY kind — nobody is too ordinary or too far gone to be
swept up into grace; the gathering (grace) comes FIRST. And the sorting at the
end is GOD'S alone — done by the angels, at the very end — it was never handed to
us. We state that there is a real end and a real sorting (j2 = 13:49) plainly and
gently, and do NOT depict or quote the furnace (13:50) luridly. The close lands
on grace: the net was cast for you.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text) — text is BOTH spoken and captioned.
    # --- s1: the net cast into the sea (KJV j1 = Matthew 13:47-48) ---
    ("n1", NARRATOR, "-20%", "-4Hz",
     "Jesus told one more short story about the kingdom of heaven, and this time "
     "he set it out on the water."),
    ("j1", JESUS, "-25%", "-6Hz",
     "Again, the kingdom of heaven is like unto a net, that was cast into the "
     "sea, and gathered of every kind: Which, when it was full, they drew to "
     "shore, and sat down, and gathered the good into vessels, but cast the bad "
     "away."),
    ("n2", NARRATOR, "-22%", "-4Hz",
     "Picture fishermen throwing a great wide net off the side of the boat, "
     "letting it sink down and drag through the whole sea."),
    # --- s2: gathered of EVERY kind ---
    ("n3", NARRATOR, "-22%", "-4Hz",
     "And here is the first beautiful thing. That net does not pick and choose. "
     "It sweeps up every kind of fish there is: big ones, small ones, common "
     "ones, strange ones, everything the sea has in it, gathered in together."),
    ("n4", NARRATOR, "-22%", "-4Hz",
     "The net is not fussy about who gets caught up in it. The gathering is wide "
     "open. Nobody swimming in that sea is too ordinary, or too far gone, to be "
     "swept up into it."),
    # --- s3: drawn to shore, THEN they sit down ---
    ("n5", NARRATOR, "-22%", "-4Hz",
     "When the net is full, the fishermen drag the whole heavy thing up onto the "
     "shore, and they sit down beside it. And only then, once everyone is "
     "already gathered in, does any sorting begin."),
    # --- s4: the good gathered into vessels ---
    ("n6", NARRATOR, "-22%", "-4Hz",
     "They gather the good fish carefully into baskets, keeping them, valuing "
     "them, not losing a single one."),
    # --- s5: the rest set aside (KJV j2 = Matthew 13:49) ---
    ("n7", NARRATOR, "-22%", "-4Hz",
     "And the ones that cannot be kept, they set aside. Jesus said that is a "
     "picture of how things finally end."),
    ("j2", JESUS, "-26%", "-6Hz",
     "So shall it be at the end of the world: the angels shall come forth, and "
     "sever the wicked from among the just"),
    ("n8", NARRATOR, "-23%", "-4Hz",
     "There is a real end, and a real sorting. But notice whose job it is. The "
     "angels do it. God does it. At the very end. It was never handed to us to "
     "do."),
    # --- s6: the gathering came first, and it came for you ---
    ("n9", NARRATOR, "-22%", "-4Hz",
     "So here is what the little story leaves you with. You do not have to spend "
     "your life deciding who belongs and who does not. That is not your net, and "
     "it is not your sorting."),
    ("n10", NARRATOR, "-22%", "-4Hz",
     "Your part is simply this: the net was cast for the whole sea, and it was "
     "cast for you. The gathering came first. Grace reached out wide enough to "
     "catch you up in it."),
    ("n11", NARRATOR, "-24%", "-4Hz",
     "That is how good he is. He threw the net over the whole ocean of us, of "
     "every kind, so that not one soul who wanted to be found would be missed."),
    # --- closing card, read gently (Readable-Card Law) ---
    ("card", NARRATOR, "-26%", "-4Hz",
     "The net was cast wide enough to gather you in. Will you let yourself be "
     "caught up in his grace?"),
]


# SPOKEN overrides: text sent to the TTS instead of the caption text, to correct a
# word the neural voice reads wrong. The ON-SCREEN caption is unchanged (build.py
# captions from SEGMENTS index 4); only the spoken audio uses these.
#   n11: edge-tts reads the word "us" here as the initialism "U.S." (you-ess).
#   "uhs" forces the plain word /ʌs/.
SPOKEN = {
    "n11": "That is how good he is. He threw the net over the whole ocean of uhs, of "
           "every kind, so that not one soul who wanted to be found would be missed.",
}


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        spoken = SPOKEN.get(name, text)
        tts = edge_tts.Communicate(spoken, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
