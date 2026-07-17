#!/usr/bin/env python3
"""Generate narration audio for MEMBER Verse Video #176 — "Who Shall Ascend
into the Hill of the LORD?" (Psalm 24:3-4). From DRAFTS/row-176.md, validated
against the laws.
MEMBER-FORMAT FIX: the draft had no spoken KJV — the member verse-video format
(build-161 precedent) requires the exact KJV verses as the CENTERPIECE, read
by the SCRIPTURE VOICE (Christopher, cream italic caption, sacred silence).
Psalm 24:3 and 24:4 added verbatim as s1/s2.
TRANSLATION-LAW FIX: the draft's n4 echoed Psalm 24:8 verbatim ("The LORD
strong and mighty, the LORD mighty in battle") in the narrator's mouth —
reworded to plain modern words.
Closing card carries the Gospel Library pointer:
"Learn more — Gospel Library: Temple Worthiness" (THE-200 → GL).
No divine figure is depicted (OT Psalm).
HOMOGRAPH LAW: ear-checked — no bow/wound/wind/tears/lead/sow/live/read/dove/
bass/minute/use(d)/close in any segment. No SPOKEN overrides needed.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"      # plain American — never a Multilingual model
SCRIPTURE = "en-US-ChristopherNeural"  # the scripture voice. Exact KJV only.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0", NARRATOR, "-20%", "-4Hz",
     "A question was put to Israel long ago — who gets to climb "
     "the hill of the LORD and stand in his holy place?"),
    # Exact KJV Psalm 24:3 — THE CENTERPIECE, scripture voice.
    ("s1", SCRIPTURE, "-24%", "-2Hz",
     "Who shall ascend into the hill of the LORD? or who shall "
     "stand in his holy place?"),
    # Exact KJV Psalm 24:4.
    ("s2", SCRIPTURE, "-24%", "-2Hz",
     "He that hath clean hands, and a pure heart; who hath not "
     "lifted up his soul unto vanity, nor sworn deceitfully."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "The answer was not about bloodline or rank. It was about "
     "clean hands and a pure heart — someone who has not lifted "
     "their soul to what is false."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "Such a one receives blessing from the LORD, and "
     "righteousness from the God of their salvation."),
    ("n3a", NARRATOR, "-20%", "-4Hz",
     "Then the call goes out to the gates themselves — lift up "
     "your heads, you ancient doors,"),
    ("n3b", NARRATOR, "-20%", "-4Hz",
     "and let the King of glory come in."),
    # sacred-silence beat follows n3b.
    ("n4a", NARRATOR, "-20%", "-4Hz",
     "And who is this King of glory?"),
    ("n4b", NARRATOR, "-20%", "-4Hz",
     "The LORD himself — strong, mighty, and unbeatable. He is the "
     "one who comes in."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "The door is open to the one with a clean heart. Come and "
     "stand in his presence."),
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
