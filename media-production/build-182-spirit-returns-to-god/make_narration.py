#!/usr/bin/env python3
"""Generate narration audio for MEMBER Verse Video #182 — The Spirit Returns
to God (Ecclesiastes 12:1-7). From DRAFTS/row-182.md, validated against
the laws.
Narrator: modern, warm, low, unhurried (American). Plain US model only.
The Preacher's words (Ecclesiastes 12:7, verified exact) are carried by the
SCRIPTURE VOICE (Christopher) — the verse-video centerpiece is present in
the draft. The narrator never quotes KJV.
Closing card carries the Gospel Library pointer:
"Learn more — Gospel Library: Plan of Salvation" (THE-200 → GL).
CONTENT-CARE: death carried with reverent distance and hope — no grim detail;
no divine figure — God conveyed through receiving light only.
HOMOGRAPH LAW: ear-checked — no bow/wound/wind/tears/lead/sow/live/read/dove/
bass/minute/use(d)/close in any segment (card included). No SPOKEN overrides
needed.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"      # plain American — never a Multilingual model
SCRIPTURE = "en-US-ChristopherNeural"  # the scripture voice. Exact KJV only.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0", NARRATOR, "-20%", "-4Hz",
     "The Teacher, Solomon, wrote honestly about the end of life. "
     "The body grows old, the days grow dim, and then — the breath "
     "leaves."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "He did not leave it there in the dark. He pointed plainly to "
     "where the breath goes."),
    # Exact KJV Eccl 12:7 — THE CENTERPIECE, scripture voice.
    ("s1", SCRIPTURE, "-24%", "-2Hz",
     "Then shall the dust return to the earth as it was: and the "
     "spirit shall return unto God who gave it."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "The body, made from dust, goes back to the ground. But the "
     "part of you that is from God goes home to Him."),
    # sacred-silence beat follows n2.
    ("n3", NARRATOR, "-20%", "-4Hz",
     "Death is not the end of the story. It is the spirit's quiet "
     "return to the One who lent it."),
    # n4 is split in two so the line's two halves land on their two
    # storyboard stills (s6 peace-on-the-face, s7 rest-not-terror) with the
    # caption on screen always matching what is being said (CAPTION LAW).
    ("n4a", NARRATOR, "-20%", "-4Hz",
     "And the Giver who receives it back is the same Giver who "
     "first breathed it into you —"),
    ("n4b", NARRATOR, "-20%", "-4Hz",
     "— with mercy, not anger."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "You were given breath by God. He is ready to receive it — "
     "and ready to give you more."),
]

# HOMOGRAPH LAW — every segment ear-checked against the flag list
# (bow, wound, wind, tears, lead, sow, live/lives, read, dove, bass,
# minute, use/used, close): none present. Captions stay exact.
# n4a/n4b: the split leaves dangling em-dashes; speak clean sentences,
# captions keep the verbatim text.
SPOKEN = {
    "n4a": "And the Giver who receives it back is the same Giver who "
           "first breathed it into you.",
    "n4b": "With mercy, not anger.",
}


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts_text = SPOKEN.get(name, text)
        tts = edge_tts.Communicate(tts_text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
