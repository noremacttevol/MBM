#!/usr/bin/env python3
"""Generate narration audio for MEMBER Verse Video #192 — The Fast God Has
Chosen (Isaiah 58:6-12). From DRAFTS/row-192.md, validated against the laws.
MEMBER-FORMAT FIX: the draft had no spoken KJV — Isaiah 58:6 and the 58:8
light-fragment added verbatim as the SCRIPTURE VOICE centerpiece
(Christopher, cream italic caption, sacred silence). The 58:8 fragment ends
at "speedily:" by design (word-exact, in order). The narrator never quotes
KJV.
Closing card carries the Gospel Library pointer:
"Learn more — Gospel Library: Fasting" (THE-200 → GL).
Jesus does not appear (Isaiah's prophecy).
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
     "Isaiah told God's people what kind of fast the LORD actually "
     "wants — not just going hungry to look holy."),
    # Exact KJV Isaiah 58:6 — THE CENTERPIECE, scripture voice.
    ("s1", SCRIPTURE, "-24%", "-2Hz",
     "Is not this the fast that I have chosen? to loose the bands "
     "of wickedness, to undo the heavy burdens, and to let the "
     "oppressed go free, and that ye break every yoke?"),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "Share your bread with the hungry. Bring the poor, the ones "
     "with nowhere to go, into your home."),
    # sacred-silence beat follows n1.
    ("n2", NARRATOR, "-20%", "-4Hz",
     "When you see someone with no clothes, cover them. Don't turn "
     "away from your own family."),
    # Exact KJV Isaiah 58:8 fragment (ends at "speedily:" by design).
    ("s2", SCRIPTURE, "-24%", "-2Hz",
     "Then shall thy light break forth as the morning, and thine "
     "health shall spring forth speedily:"),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "The LORD promises — call, and He answers. Help others, and "
     "your own darkness becomes noonday."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "The fast God chooses is a hand opened to the hurting. Open "
     "yours — He meets you there."),
]

# HOMOGRAPH LAW — every segment ear-checked against the flag list
# (bow, wound, wind, tears, lead, sow, live/lives, read, dove, bass,
# minute, use/used, close): none present. Captions stay exact.
SPOKEN = {}


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts_text = SPOKEN.get(name, text)
        tts = edge_tts.Communicate(tts_text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
