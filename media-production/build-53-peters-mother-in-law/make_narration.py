#!/usr/bin/env python3
"""Generate narration audio for Video #53 — Peter's Mother-in-Law (Mark 1:29-31).

Narrator: en-US-AndrewNeural — plain American, never a Multilingual model.
Jesus voice: en-US-ChristopherNeural — American (unused here; see below).

Jesus speaks ONLY exact KJV. In THIS passage he says nothing — Mark records no words
from him, only the touch — so there is NO red-letter line and NO cream-italic caption.
The reverent beat (the SACRED SILENCE where the music bed dies) lands on the moment he
takes her by the hand (n5). The narrator carries the whole story in the plain white style.

HOMOGRAPH LAW: no TTS homographs in this text (no live/bow/wound/read/tear/wind/lead/
sow). SPOKEN is empty.

CARE — GREEN: a gentle, intimate healing. No violence, no fear; a sickbed in an ordinary
house, one touch, and a woman made well who rises to serve. Ends on an open invitation.

NUMBER-STRESS LAW: no sentence opens with a bare number.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"
JESUS = "en-US-ChristopherNeural"  # unused this video; kept for the shared format

SPOKEN = {}

SEGMENTS = [
    # (filename, voice, rate, pitch, text) — text is BOTH spoken and captioned.
    # --- s1: home from the synagogue ---
    ("n1", NARRATOR, "-20%", "-4Hz",
     "When Jesus came out of the synagogue that sabbath, he did not go off alone. He "
     "went home with his friends, into the house of Simon and Andrew, and James and John "
     "went in with them."),
    # --- s2: an ordinary house, and a shadow over it ---
    ("n2", NARRATOR, "-22%", "-4Hz",
     "It was an ordinary house, the kind of place where real life happens. But that day "
     "the house was heavy, because someone they loved was ill."),
    # --- s3: sick of a fever ---
    ("n3", NARRATOR, "-22%", "-4Hz",
     "Simon's wife's mother lay in a back room, sick with a fever. In those days a fever "
     "like that could take a life, and there was little anyone could do but sit beside "
     "her and worry."),
    # --- s4: they tell him ---
    ("n4", NARRATOR, "-22%", "-4Hz",
     "So they told Jesus about her. They did not make a speech or a grand request; they "
     "simply brought their trouble to him, the way you tell a friend what is wrong."),
    # --- s5: he took her by the hand. SACRED SILENCE. ---
    ("n5", NARRATOR, "-24%", "-5Hz",
     "And he came to where she lay, and he took her by the hand."),
    # --- s6: the fever left her ---
    ("n6", NARRATOR, "-22%", "-4Hz",
     "He lifted her up, and in that moment the fever simply left her. No slow recovery, "
     "no days of weakness; the heat and the sickness were gone, and she was herself once "
     "more, well and strong."),
    # --- s7: she ministered unto them ---
    ("n7", NARRATOR, "-22%", "-4Hz",
     "And the first thing she did was rise and serve them. With her strength fully back, "
     "she cared for the very ones who had carried her trouble to Jesus, glad to be on her "
     "feet again."),
    # --- s8: the quiet of it ---
    ("n8", NARRATOR, "-24%", "-4Hz",
     "It is a small, quiet miracle, tucked into an ordinary house. No crowd and no "
     "spectacle; only a tired family, a sickbed, and a Savior who came in, took her by "
     "the hand, and made her whole."),
    # --- closing card, read gently (Readable-Card Law) ---
    ("card", NARRATOR, "-26%", "-4Hz",
     "He still comes into ordinary houses and ordinary lives. You do not need the right "
     "words or a grand request; you only need to tell him where it hurts. What would it "
     "mean to simply put your trouble into his hand?"),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        spoken = SPOKEN.get(name, text)
        tts = edge_tts.Communicate(spoken, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")


if __name__ == "__main__":
    asyncio.run(main())
