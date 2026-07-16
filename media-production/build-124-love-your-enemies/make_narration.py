#!/usr/bin/env python3
"""Narration audio for Video #124 — Love Your Enemies (Matthew 5:43-48).

Narrator: en-US-AndrewNeural. Jesus's voice: en-US-ChristopherNeural (exact KJV only).
Jesus's KJV lines (Christopher, cream italic; fetched from bible-api.com KJV, not hand-typed):
  jvA  Matt 5:44  "But I say unto you, Love your enemies, bless them that curse you..."
                  — sacred silence 1 (the command)
  jvB  Matt 5:45  "That ye may be the children of your Father which is in heaven..."
                  — sacred silence 2 (the reason: likeness)

CARE FLAGS: none (GREEN). A Sermon-on-the-Mount teaching; the illustration conflict is
cold looks and a broken fence — no violence, no shame framing.

WHY-LAW (THE-200 row 124: "that ye may be children of your Father — likeness is the point"):
loving an enemy is not presented as fairness or a burden but as FAMILY RESEMBLANCE — the
Father's sun and rain fall on evil and good alike, and this love is how his children look
like him. Never scolding; the closing card is an invitation to pray for one person by name.

HOMOGRAPH EAR-CHECK: "despitefully use you" — edge-tts reads 'use' as the verb (yooz),
correct. No read/lead/bow/wind/tears traps. NUMBER-STRESS LAW: no numbers in the script.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"
JESUS = "en-US-ChristopherNeural"

SEGMENTS = [
    ("n1", NARRATOR, "-20%", "-4Hz",
     "On a green hillside above the Sea of Galilee, Jesus sat down to teach, and a whole "
     "countryside climbed up to listen. He was walking through the old sayings one at a "
     "time — you have heard it said — and then he came to the hardest one of all: what to "
     "do with an enemy.", None),
    ("n2", NARRATOR, "-22%", "-4Hz",
     "Everyone on that hillside knew the old arithmetic. Love the people who love you. "
     "Keep your guard up against the ones who don't. It felt fair. It felt safe. And then "
     "Jesus said this.", None),
    # jvA — Matt 5:44 — sacred silence 1
    ("jvA", JESUS, "-26%", "-6Hz",
     "But I say unto you, Love your enemies, bless them that curse you, do good to them "
     "that hate you, and pray for them which despitefully use you, and persecute you;", None),
    ("n3", NARRATOR, "-22%", "-4Hz",
     "Not tolerate them. Not stay out of their way. Bless. Do good. Pray. Every one of "
     "those is something you go and do — aimed straight at the person who has earned none "
     "of it. Picture a farmer whose neighbor has wronged him: the fence knocked down, the "
     "insult at the well, years of cold looks across one stone wall.", None),
    ("n4", NARRATOR, "-22%", "-4Hz",
     "He has every right to answer coldness with coldness. That is the old arithmetic, "
     "and nobody would blame him for it. Instead, when his neighbor's wall gives way in "
     "the rains, he walks over quietly and starts lifting stones.", None),
    ("n5", NARRATOR, "-22%", "-4Hz",
     "And at night, when the work is done and no one is watching, he does the thing Jesus "
     "asked that no one ever sees. By the light of his lamp, he prays for the man across "
     "the wall — not about him. For him. By name.", None),
    ("n6", NARRATOR, "-22%", "-4Hz",
     "Why would Jesus ask for something this unreasonable? He was not pretending enemies "
     "don't hurt. He gave his reason on the same hillside, and the reason changes "
     "everything.", None),
    # jvB — Matt 5:45 — sacred silence 2
    ("jvB", JESUS, "-26%", "-6Hz",
     "That ye may be the children of your Father which is in heaven: for he maketh his "
     "sun to rise on the evil and on the good, and sendeth rain on the just and on the "
     "unjust.", None),
    ("n7", NARRATOR, "-22%", "-4Hz",
     "Look at the sky, he was saying. Your Father's sun came up this morning over every "
     "field in the valley — the kind man's and the cruel man's alike. His rain waters "
     "both. Loving an enemy is not unnatural. In this family, it is the resemblance.", None),
    ("n8", NARRATOR, "-24%", "-4Hz",
     "Anyone can love the people who love them back — Jesus pointed out that even the tax "
     "collectors managed that much. The love that marks you as your Father's child is the "
     "love that is not owed. And sometimes, slowly, it wins what coldness never could: the "
     "wall between two houses becomes the place where they meet.", None),
    ("card", NARRATOR, "-26%", "-4Hz",
     "Jesus never said your enemy deserves it. He said this is how the family likeness "
     "shows. Who is the hardest person in your life to bless? What might change if, "
     "tonight, you prayed for them — by name?", None),
]


async def main():
    for name, voice, rate, pitch, text, cap in SEGMENTS:
        tts = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")


if __name__ == "__main__":
    import os
    os.makedirs("audio", exist_ok=True)
    asyncio.run(main())
