#!/usr/bin/env python3
"""Generate narration audio for Video #51 — The First Catch of Fish (Luke 5:1-11).

Narrator: en-US-AndrewNeural — plain American, never a Multilingual model.
Jesus voice: en-US-ChristopherNeural — American, never British.

Jesus speaks ONLY exact KJV. Two lines — his whole speech in this passage:
  jv4  = Luke 5:4   "Launch out into the deep..."   (SACRED SILENCE 1 — the command)
  jv10 = Luke 5:10  "Fear not; ...catch men."       (SACRED SILENCE 2 — the calling)

TRANSLATION LAW: after each KJV line the narrator gives plain meaning and never
re-quotes it. Peter's own words ("Master, we have toiled..."; "I am a sinful man")
are NOT red-letter KJV — the narrator reports them plainly; they are not captioned in
the cream scripture style.

HOMOGRAPH LAW: "draught" (a haul of fish, = /draft/) is respelled for TTS only via
SPOKEN; the caption still shows the true KJV word "draught". Avoided "close" (adj/verb
homograph) in n5 by rewording to "began to sink".

MILK FRAMING: wonder and calling, never fear. He meets them at their emptiest, fills
their hands past overflowing, and calls the man who felt unworthy. Ends on the open
invitation to leave and follow.

NUMBER-STRESS LAW: no sentence opens with a bare number.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"
JESUS = "en-US-ChristopherNeural"

# TTS-only respellings (captions still show the true text in build.py).
SPOKEN = {
    "jv4": "Launch out into the deep, and let down your nets for a draft.",
}

SEGMENTS = [
    # (filename, voice, rate, pitch, text) — text is BOTH spoken and captioned.
    # --- s1: the empty morning ---
    ("n1", NARRATOR, "-20%", "-4Hz",
     "By the lake of Gennesaret, a crowd pressed in around him, hungry to hear the word "
     "of God. Two empty boats sat at the water's edge, and beside them tired fishermen "
     "were washing out their nets after a long night that had given them nothing."),
    # --- s2: he teaches from the boat ---
    ("n2", NARRATOR, "-22%", "-4Hz",
     "He stepped into one of the boats. It belonged to a fisherman named Simon. He asked "
     "him to push out a little way from the shore, and then he sat down and taught the "
     "people from the water."),
    # --- s3: jv4 — launch out. SACRED SILENCE 1. ---
    ("jv4", JESUS, "-26%", "-6Hz",
     "Launch out into the deep, and let down your nets for a draught."),
    # --- s4: Peter obeys against his judgement ---
    ("n3", NARRATOR, "-22%", "-4Hz",
     "Simon was bone-tired. They had worked that water all night and come back with "
     "nothing, and every instinct told him it was pointless. But something in this man "
     "made him do it anyway. Master, he said, at your word I will let the net down again."),
    # --- s5: the great catch ---
    ("n4", NARRATOR, "-22%", "-4Hz",
     "The moment the nets went down, they filled. A great shining mass of fish, far more "
     "than the ropes were made to hold, and the net began to tear under the sheer weight "
     "of it."),
    # --- s6: both boats sink ---
    ("n5", NARRATOR, "-22%", "-4Hz",
     "There were too many for one boat. They waved to their partners, James and John, in "
     "the other boat to come and help, and both boats were loaded until they sat low in "
     "the water and began to sink."),
    # --- s7: Peter at his knees ---
    ("n6", NARRATOR, "-22%", "-4Hz",
     "When Simon Peter saw it, he fell down at Jesus' knees. He did not feel worthy of "
     "any of this. Depart from me, he said, for I am a sinful man, O Lord. The wonder of "
     "it had shown him exactly who he was, and exactly who this was."),
    # --- s8: jv10 — fear not, catch men. SACRED SILENCE 2. ---
    ("jv10", JESUS, "-26%", "-6Hz",
     "Fear not; from henceforth thou shalt catch men."),
    ("n7", NARRATOR, "-22%", "-4Hz",
     "He does not send Peter away. He calls him. The trembling fisherman who begged him "
     "to leave is the very man he wants, and from this day on he will be gathering people, "
     "not fish."),
    # --- s9: they forsook all ---
    ("n8", NARRATOR, "-24%", "-4Hz",
     "And that was enough. They brought the boats to land, left the greatest catch of "
     "their lives lying there on the shore, and followed him. They forsook all, the nets, "
     "the boats, the best day they had ever had, and went with him."),
    # --- closing card, read gently (Readable-Card Law) ---
    ("card", NARRATOR, "-26%", "-4Hz",
     "He met them at their emptiest, a whole night of work and nothing to show, and "
     "filled their hands past overflowing. Then he asked for all of it, so he could give "
     "them something far greater. What is he calling you to leave behind, to follow him?"),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        spoken = SPOKEN.get(name, text)
        tts = edge_tts.Communicate(spoken, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
