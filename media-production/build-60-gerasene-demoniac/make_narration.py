#!/usr/bin/env python3
"""Generate narration audio for Story Video #60 — The Gerasene Demoniac (Mark 5:1-20).
Narrator: modern, warm, low, unhurried (American). Plain US model only.
Jesus voice: AMERICAN, never British. Jesus speaks ONLY exact KJV:
Mark 5:8, 5:9, 5:19 (fetched, not hand-typed).
CONTENT-CARE (A,R): no embodied devils anywhere; the self-harm of Mark 5:5 is
NEVER depicted and not dwelt on in narration; before/after dignity for the man;
the demon's own line is paraphrased by the narrator (never the Jesus voice).
Homograph law: "lived" in n1 gets a SPOKEN respelling (caption stays exact).
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0", NARRATOR, "-20%", "-4Hz",
     "The boat touched the far shore of the Sea of Galilee at first light "
     "— the disciples still shaking from the storm that had nearly sunk "
     "them in the night. This was the other side. Gentile country. "
     "Foreign gods, foreign food, herds of pigs on the hills. No rabbi "
     "took his students here on purpose. Jesus had crossed the whole sea "
     "in a storm to reach it."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "Because one man lived there — if you could call it living. He made "
     "his home among the tombs, the caves where the dead were laid, "
     "because the town had driven him out. Something had hold of him "
     "that no one could fix. They had tried chains. He tore them apart. "
     "Night and day he cried out among the graves. To his town he was "
     "no longer a name. He was a warning."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "And when that man saw Jesus step out of the boat, far down the "
     "shore, he ran. Not to attack him. He ran and fell down at his "
     "feet. And the thing inside him cried out in terror — because it "
     "knew exactly who was standing on that beach, and what he could "
     "do. The man's own town had given up on him. The darkness holding "
     "him knew better."),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "Jesus did not step back. He was not afraid of him. He spoke "
     "straight past the man, to the thing that held him."),
    # Exact KJV Mark 5:8 — SACRED SILENCE around this line.
    ("j1", JESUS, "-18%", "-2Hz",
     "Come out of the man, thou unclean spirit."),
    ("n4", NARRATOR, "-20%", "-4Hz",
     "Then he asked it a question."),
    # Exact KJV Mark 5:9a.
    ("j2", JESUS, "-18%", "-2Hz",
     "What is thy name?"),
    ("n5", NARRATOR, "-20%", "-4Hz",
     "The answer that came back was a Roman army word. Legion. A legion "
     "was thousands of soldiers. That is how outnumbered this one man "
     "was on the inside. And standing in front of Jesus, the thousands "
     "were the ones begging."),
    ("n6", NARRATOR, "-20%", "-4Hz",
     "On the hillside above them, a herd of about two thousand pigs was "
     "feeding — remember, this was Gentile land; no Jewish town keeps "
     "pigs. The spirits begged not to be sent out of the country, but "
     "into the herd. And Jesus gave them leave. In an instant the whole "
     "herd stampeded down the steep bank into the sea, and the water "
     "closed over them. The men tending the pigs ran for town with the "
     "story of their lives."),
    ("n7", NARRATOR, "-20%", "-4Hz",
     "The whole town came out to see. And what they found was the man "
     "they had chained and lost and buried in their memory — sitting "
     "quietly at the feet of Jesus. Clothed. Calm. In his right mind. "
     "And the scripture says a strange thing: they were afraid. Power "
     "like that, standing on their beach, had just cost them two "
     "thousand pigs. So they asked Jesus to leave."),
    ("n8", NARRATOR, "-20%", "-4Hz",
     "And he did. He never argues his way in where he is not wanted. "
     "But as he climbed into the boat, the healed man begged to come "
     "with him. It is the only time in the gospels someone asks to "
     "follow Jesus and is told no. Listen to what he was given "
     "instead."),
    # Exact KJV Mark 5:19b — SACRED SILENCE around this line.
    ("j3", JESUS, "-20%", "-2Hz",
     "Go home to thy friends, and tell them how great things the Lord "
     "hath done for thee, and hath had compassion on thee."),
    ("n9", NARRATOR, "-20%", "-4Hz",
     "Go home. To the town that chained you. To the people who gave up "
     "on you. Tell them what God did. The man everyone had written off "
     "became the first person Jesus ever sent out with his story — a "
     "one-man mission to the ten Gentile cities of the Decapolis. And "
     "everywhere he went, people were amazed."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "He crossed a sea in a storm for one man everyone else had given "
     "up on. There is no distance he will not cross for you."),
]

# HOMOGRAPH LAW — TTS-only respellings; captions keep the exact SEGMENTS text.
SPOKEN = {
    "n1": ("Because one man livd there — if you could call it living. He made "
           "his home among the tombs, the caves where the dead were laid, "
           "because the town had driven him out. Something had hold of him "
           "that no one could fix. They had tried chains. He tore them apart. "
           "Night and day he cried out among the graves. To his town he was "
           "no longer a name. He was a warning."),
}


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts_text = SPOKEN.get(name, text)
        tts = edge_tts.Communicate(tts_text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
