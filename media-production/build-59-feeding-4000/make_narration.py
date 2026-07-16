#!/usr/bin/env python3
"""Generate narration audio for Video #59 — Feeding the Four Thousand (Mark 8:1-9).

Narrator: en-US-AndrewNeural — plain American, never a Multilingual model.
Jesus voice: en-US-ChristopherNeural — American, never British.

Jesus speaks ONLY exact KJV. One red-letter line + one non-verbal sacred beat:
  jv2 = Mark 8:2  "I have compassion on the multitude, because they have now been with me
                   three days, and have nothing to eat."   (SACRED SILENCE 1 — compassion)
  (nbless) Mark 8:6 — the BLESSING of the loaves (narrator-told) = SACRED SILENCE 2.

TRANSLATION LAW: the narrator paraphrases everything else and never re-quotes the
red-letter line. Distinct from #58 (the five thousand): this crowd has been with him THREE
DAYS in a remote wilderness, seven loaves (not five), seven baskets (not twelve), four
thousand (not five) — and the heart of it is his COMPASSION, that they would faint on the
way home.

HOMOGRAPH LAW: no TTS homographs (avoided archaic "brake"; no live/bow/wound/read/tear/
wind/lead/sow). SPOKEN is empty.

CARE — GREEN: a tender miracle of compassion and provision; the fish are simple food, never
gory. Ends on an open invitation.

NUMBER-STRESS LAW: no sentence opens with a bare number.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"
JESUS = "en-US-ChristopherNeural"

SPOKEN = {}

SEGMENTS = [
    # (filename, voice, rate, pitch, text) — text is BOTH spoken and captioned.
    # --- s1: three days with him ---
    ("n1", NARRATOR, "-20%", "-4Hz",
     "Another huge crowd had come to Jesus, this time in a remote and rugged place far "
     "from any town. They had been with him three whole days, listening and being healed, "
     "and now their food was completely gone, and they were a long way from home."),
    # --- s2: jv2 — I have compassion. SACRED SILENCE 1. ---
    ("jv2", JESUS, "-26%", "-6Hz",
     "I have compassion on the multitude, because they have now been with me three days, "
     "and have nothing to eat."),
    # --- s3: lest they faint; the disciples baffled ---
    ("n2", NARRATOR, "-22%", "-4Hz",
     "He would not just send them off. If I send them away hungry, he said, they will "
     "faint on the way, for some have come a very long distance. So he turned to his "
     "disciples; but they were baffled. Where, out here in the wilderness, could anyone "
     "find enough bread for a crowd this size?"),
    # --- s4: seven loaves ---
    ("n3", NARRATOR, "-22%", "-4Hz",
     "Jesus asked them what they already had. They had seven loaves, they said, and a few "
     "small fish. It was almost nothing against so great a need. But he took it gladly; in "
     "his hands, it was more than enough."),
    # --- s5: he gave thanks and brake. SACRED SILENCE 2. ---
    ("nbless", NARRATOR, "-24%", "-5Hz",
     "He had the people sit down on the ground. Then he took the seven loaves, and gave "
     "thanks, and broke them, and gave them to his disciples to set before the crowd."),
    # --- s6: all were filled ---
    ("n4", NARRATOR, "-22%", "-4Hz",
     "And once again the food did not run out. The disciples carried bread and fish "
     "through the whole multitude, and everyone ate until they were completely satisfied, "
     "thousands of people, fed from almost nothing."),
    # --- s7: seven baskets ---
    ("n5", NARRATOR, "-22%", "-4Hz",
     "When they gathered up what was left over, they filled seven large baskets with the "
     "broken pieces. There was far more at the end than there had been at the start."),
    # --- s8: four thousand fed ---
    ("n6", NARRATOR, "-22%", "-4Hz",
     "About four thousand people were there that day, and every single one of them went "
     "home full. Then he sent them away, cared for, in body and in soul."),
    # --- s9: who he is ---
    ("n7", NARRATOR, "-24%", "-4Hz",
     "He did not owe them a meal. But he saw tired, hungry people a long way from home, "
     "and he could not bear to send them away empty. That is simply who he is."),
    # --- closing card, read gently (Readable-Card Law) ---
    ("card", NARRATOR, "-26%", "-4Hz",
     "He notices what everyone else overlooks, that you are tired, that you are running on "
     "empty, that you have come a long way. He cares about your soul, and he also cares "
     "that you would faint on the road. What ordinary need are you afraid is too small to "
     "bring to him?"),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        spoken = SPOKEN.get(name, text)
        tts = edge_tts.Communicate(spoken, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")


if __name__ == "__main__":
    asyncio.run(main())
