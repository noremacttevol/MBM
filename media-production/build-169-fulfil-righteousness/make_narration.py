#!/usr/bin/env python3
"""Generate narration audio for Story Video #169 — "To fulfil all righteousness"
(Matthew 3:13-17). MEMBER shelf verse-video. → Gospel Library topics: Baptism; Godhead.

Narrator: en-US-AndrewNeural — plain American, modern paraphrase, never a
Multilingual model, never echoes the KJV wording.
Scripture voice: en-US-ChristopherNeural — speaks the KJV text EXACTLY.

FACE-SHOWN build: Jesus is depicted (master face, cream robe). The Father is shown only as
warm light from the opened heaven; the Holy Ghost is the descending white dove (scriptural).

KJV lines (exact):
  kv15 = Matt 3:15  ...thus it becometh us to fulfil all righteousness (NAMED — SACRED SILENCE 1)
  kv17 = Matt 3:17  a voice from heaven: This is my beloved Son (SACRED SILENCE 2)

WHY-LAW: example + doctrine — even the Sinless One was baptized, so baptism is for everyone;
and the Godhead stood revealed as three distinct persons (Son in the water, Spirit as a dove,
Father's voice). STUDY GEM: the Godhead is three distinct, present together — not one person in
three masks; and even He was baptized (n6).

TRANSLATION LAW: the narrator never re-quotes a KJV line. n2 paraphrases v14, n3-n4 paraphrase
v16; the exact KJV lands only in kv15/kv17.

HOMOGRAPH NOTE: "dove" (n4) — the bird /duhv/, in the fixed phrase "like a dove," which
edge-tts reads correctly; no override needed. Re-listen if ever rebuilt.

MILK FRAMING: an invitation. The closing card ends on an open question and a one-line
pointer to the Gospel Library topics (Baptism; Godhead). No shame, no fear.

NUMBER-STRESS LAW: no sentence opens with a bare number.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"
SCRIPTURE = "en-US-ChristopherNeural"

SEGMENTS = [
    ("n1", NARRATOR, "-20%", "-4Hz",
     "Something startling happens at the very start of it all. Jesus, who had no sin to wash "
     "away, walks down to the river Jordan and asks John to baptize him — the sinless One, "
     "lining up for the sinner's ordinance."),
    ("n2", NARRATOR, "-22%", "-4Hz",
     "John was stunned, and tried to stop him. He felt the whole thing backwards: surely he "
     "was the one who needed to be baptized by Jesus, not Jesus by him. Who was he to baptize "
     "the Lord?"),
    # kv15 — NAMED VERSE, SACRED SILENCE 1
    ("kv15", SCRIPTURE, "-26%", "-6Hz",
     "And Jesus answering said unto him, Suffer it to be so now: for thus it becometh us to "
     "fulfil all righteousness. Then he suffered him."),
    ("n3", NARRATOR, "-22%", "-4Hz",
     "So even the perfect One went down into the water. Not because he needed cleansing, but "
     "to fulfil all righteousness — to walk the path himself, and leave us an example that "
     "this gate is the way in, for everyone."),
    ("n4", NARRATOR, "-22%", "-4Hz",
     "And as he came up out of the water, heaven itself answered. The skies opened, and the "
     "Spirit of God came down gently, like a dove, and rested upon him in the warm light."),
    # kv17 — SACRED SILENCE 2
    ("kv17", SCRIPTURE, "-26%", "-6Hz",
     "And lo a voice from heaven, saying, This is my beloved Son, in whom I am well pleased."),
    ("n5", NARRATOR, "-22%", "-4Hz",
     "Look closely at that one moment, because it opens a window into who God is. Three were "
     "there at once, and each was distinct: the Son standing in the river, the Spirit resting "
     "as the dove, and the Father speaking from the opened heaven."),
    ("n6", NARRATOR, "-22%", "-4Hz",
     "Here is the quiet study gem. This was not one person changing costumes. It was three "
     "distinct persons, together, each doing his own part — the Godhead, standing plain to "
     "see. And notice: even He was baptized."),
    ("n7", NARRATOR, "-24%", "-4Hz",
     "And that settles it for the rest of us. If the one man who never needed it still went "
     "down into the water to fulfil all righteousness, then the way is surely open, and good, "
     "for you. When you come to that same water, will you go down into it?"),
    ("card", NARRATOR, "-26%", "-4Hz",
     "Even the Sinless One was baptized, to fulfil all righteousness — and there the Godhead "
     "stood revealed: the Son, the Spirit, and the Father, three and distinct. When you come "
     "to that same water, will you go down into it?"),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
