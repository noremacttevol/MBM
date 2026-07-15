#!/usr/bin/env python3
"""Narration for Story Video #50 — The Nobleman's Son (John 4:46-54).

Narrator: en-US-AndrewNeural — plain American, never a Multilingual model.
Jesus voice: en-US-ChristopherNeural — American, never British.

CAPTIONS ARE VERBATIM: build.py imports these SEGMENTS and captions the exact
text[4]. A 6th tuple element, when present, is a SPOKEN-ONLY override used for TTS
(homograph law) while the caption still shows the true KJV word.

HOMOGRAPH LAW: the KJV "liveth" must say /liv/, never /lyve/ — the spoken override
respells it. Narrator paraphrases avoid live/lives entirely (worded as alive/well).
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

# (filename, voice, rate, pitch, caption_text[, spoken_override])
SEGMENTS = [
    # --- s1: Jesus back in Cana ---
    ("n1", NARRATOR, "-20%", "-4Hz",
     "Jesus came back to Cana, the little town where he had turned the water into "
     "wine. And word of it was spreading fast."),
    # --- s2: a father, and a dying boy ---
    ("n2", NARRATOR, "-22%", "-4Hz",
     "About twenty miles away, in Capernaum, a royal official sat by his son's bed. "
     "A man of rank, used to giving orders and being obeyed. And none of it was any "
     "use now. His boy was burning with fever, and the doctors had run out of "
     "answers."),
    # --- s3: he drops everything and goes ---
    ("n3", NARRATOR, "-22%", "-4Hz",
     "Then he heard the healer was in Cana, a full day's walk uphill. So this "
     "powerful man dropped everything and went, hurrying on foot to find a village "
     "carpenter's son, because he had nowhere else left to turn."),
    # --- s4: he finds Jesus and begs ---
    ("n4", NARRATOR, "-22%", "-4Hz",
     "He found Jesus and begged him to come down to Capernaum and heal his boy "
     "before it was too late. A father with no pride left, only fear."),
    # --- s5: v48 — Jesus draws out real faith ---
    ("jv48", JESUS, "-26%", "-6Hz",
     "Except ye see signs and wonders, ye will not believe."),
    ("n5", NARRATOR, "-22%", "-4Hz",
     "It can sound like a scolding, but it was not. Jesus was reaching past the "
     "man's panic for something deeper. He was inviting him to trust without needing "
     "a show first."),
    # --- s6: the father pleads again ---
    ("n6", NARRATOR, "-22%", "-4Hz",
     "The father does not argue about it. He just says it again, plain and "
     "breaking. Sir, come down before my child dies."),
    # --- s7: v50 — the healing word. SACRED SILENCE. ---
    ("jv50", JESUS, "-28%", "-6Hz",
     "Go thy way; thy son liveth.",
     "Go thy way; thy son livveth."),
    ("n7", NARRATOR, "-22%", "-4Hz",
     "No trip to Capernaum. No hand laid on the boy. Just a word, spoken over a "
     "sick child a day's journey away. And the man believed him, turned, and started "
     "home."),
    # --- s8: the long walk on nothing but a promise ---
    ("n8", NARRATOR, "-22%", "-4Hz",
     "Think about that walk. A whole day on the road with no proof in his hands, "
     "nothing to hold but a stranger's word that his son was already well."),
    # --- s9: the servants meet him ---
    ("n9", NARRATOR, "-22%", "-4Hz",
     "The next day his servants came running to meet him. Your boy is up, they said. "
     "He is well. The fever broke and left him."),
    # --- s10: the same hour ---
    ("n10", NARRATOR, "-22%", "-4Hz",
     "He asked them exactly when the boy started to mend. Yesterday, they said, at "
     "the seventh hour. The very hour Jesus had told him his son was healed."),
    # --- s11: he and his whole house believed ---
    ("n11", NARRATOR, "-24%", "-4Hz",
     "And that settled it. The man believed, and his whole household believed with "
     "him. The word had been true the entire way home, working quietly while he "
     "walked and could not see it."),
    # --- closing card, an INVITATION ---
    ("card", NARRATOR, "-26%", "-4Hz",
     "He healed a boy he never touched, with a word that was already true before "
     "anyone could prove it. If his word can carry a whole day's journey, how far do "
     "you think it can reach? What would you trust him with tonight?"),
]


async def main():
    for seg in SEGMENTS:
        name, voice, rate, pitch, text = seg[0], seg[1], seg[2], seg[3], seg[4]
        spoken = seg[5] if len(seg) > 5 else text
        tts = edge_tts.Communicate(spoken, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"  {name}.mp3")


if __name__ == "__main__":
    asyncio.run(main())
