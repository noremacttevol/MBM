#!/usr/bin/env python3
"""Narration audio for Video #101 — The Still Small Voice (1 Kings 19:1-18).

Narrator: en-US-AndrewNeural — plain American, never a Multilingual model.
The Lord's voice: en-US-ChristopherNeural — American, never British. The Lord speaks
ONLY exact KJV; Elijah's words are given by the narrator in plain paraphrase (two-voice
law: narrator = modern paraphrase, the divine voice = exact KJV).

The Lord's KJV lines (Christopher, cream italic captions in build.py):
  jv9   1 Kgs 19:9   "What doest thou here, Elijah?"
  jv11  1 Kgs 19:11  "Go forth, and stand upon the mount before the LORD..."
  jv12  1 Kgs 19:12  "...and after the fire a still small voice."
  jv18  1 Kgs 19:18  "Yet I have left me seven thousand in Israel..."

WHY-LAW: the misread is that God meets exhaustion and failure with thunder and rebuke.
The point is the opposite — after the wind, quake and fire that were NOT him, God came
in a gentle whisper, and answered "I am the only one left" with tenderness: you are not
alone, there are seven thousand more. Milk framing: comfort for the burned-out and the
lonely. An invitation, never a threat. Nobody is harmed.

HOMOGRAPH EAR-CHECK (playbook): "wind" must be /wɪnd/ (moving air), NEVER /waɪnd/.
edge-tts default for the noun 'wind' is correct here, but VERIFY. "bowed" (v18) = bent
the knee, /baʊd/ — correct as written. If any misreads, add a SPOKEN override below and
re-listen; captions keep the true KJV word.

NUMBER-STRESS LAW: no sentence opens with a bare number ("Seven thousand" is fine as a
phrase mid-sentence; the card and n-lines avoid opening on a numeral).
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"
LORD = "en-US-ChristopherNeural"

# (filename, voice, rate, pitch, spoken_text, caption_override_or_None)
# If caption_override is None the caption IS the spoken text. Where a SPOKEN respelling
# is needed for a homograph, put the true KJV/plain words in the override so the SCREEN
# stays correct while the ear hears it right.
SEGMENTS = [
    # --- s1: the flight, the end of his strength ---
    ("n1", NARRATOR, "-20%", "-4Hz",
     "Elijah had just won the greatest victory of his life. And then a single threat "
     "sent him running for the wilderness, until he sank down under a lone bush, worn "
     "out and afraid, and asked God to let him die.", None),
    # --- s2: the gentle provision ---
    ("n2", NARRATOR, "-22%", "-4Hz",
     "God did not scold him. While he slept, warm bread was baked for him and a jar of "
     "water set by his head. Twice he was fed, and gently told the journey was too great "
     "for him to make alone.", None),
    # --- s3: the long journey to the mount ---
    ("n3", NARRATOR, "-22%", "-4Hz",
     "In that strength he walked forty days across the wilderness, all the way to the "
     "mountain of God, and found a cave, and went in, and stayed there in the dark.", None),
    # --- s4: the question ---
    ("jv9", LORD, "-24%", "-6Hz",
     "What doest thou here, Elijah?", None),
    ("n4", NARRATOR, "-22%", "-4Hz",
     "And out it all poured. I have given everything for you, he said. They have torn "
     "down your altars and killed your prophets. I am the only one left, and now they "
     "want me dead too.", None),
    # --- s5/s6/s7: wind, earthquake, fire — but not the Lord ---
    ("jv11a", LORD, "-24%", "-6Hz",
     "Go forth, and stand upon the mount before the LORD. And, behold, the LORD passed "
     "by, and a great and strong wind rent the mountains, and brake in pieces the rocks "
     "before the LORD; but the LORD was not in the wind:", None),
    ("jv11b", LORD, "-24%", "-6Hz",
     "and after the wind an earthquake; but the LORD was not in the earthquake:", None),
    ("n5", NARRATOR, "-22%", "-4Hz",
     "A wind strong enough to tear the mountain apart. Then an earthquake that split the "
     "rock under his feet. Then a fire sweeping across the stone. Surely God would be in "
     "something that big. But he was not in any of them.", None),
    # --- s8: the still small voice. the hush. ---
    ("jv12", LORD, "-26%", "-6Hz",
     "And after the fire a still small voice.", None),
    ("n6", NARRATOR, "-22%", "-4Hz",
     "After all the noise and power, everything went quiet. And in the quiet came a low, "
     "gentle whisper. That was where God was. Elijah heard it, and wrapped his face in "
     "his cloak, and came to the mouth of the cave to listen.", None),
    # --- s9: the gentle recommission ---
    ("n7", NARRATOR, "-22%", "-4Hz",
     "The whisper did not shame him for being afraid. It asked him again what troubled "
     "him, let him say it all a second time, and then quietly gave him work to do and "
     "people to go to. He was being sent back, steadied and not alone.", None),
    # --- s10: seven thousand. you are not the only one. ---
    ("jv18", LORD, "-24%", "-6Hz",
     "Yet I have left me seven thousand in Israel, all the knees which have not bowed "
     "unto Baal, and every mouth which hath not kissed him.", None),
    ("n8", NARRATOR, "-24%", "-4Hz",
     "You are not the only one, God told him. Scattered across the land are thousands "
     "who have never bent the knee to the lie. You feel alone, but you are not. That is "
     "how God answered a tired, frightened man — not with thunder, but with a whisper, "
     "and with the truth that he was never as alone as he feared.", None),
    # --- closing card, read gently (Readable-Card Law) ---
    ("card", NARRATOR, "-26%", "-4Hz",
     "The wind, the earthquake and the fire were not God. The whisper was. When you are "
     "worn out and sure you are the only one left, could the voice you most need be the "
     "gentle one?", None),
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
