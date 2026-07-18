#!/usr/bin/env python3
"""Narration for Story Video #15 — The Centurion's Servant (Matthew 8:5-13).

REWRITTEN 2026-07-11 to Cameron's feedback:
 - Phase 1 is STILLS-ONLY (Law E reversed) — no motion clips; this script is
   unchanged by that but the build is all stills.
 - Every spoken word is captioned VERBATIM: build.py imports SEGMENTS and uses
   each segment's exact text as its on-screen caption, so nothing spoken is ever
   missing from the screen.
 - Clearer, more sensible wording; each Jesus (KJV) line is explained plainly in
   terms of HOW GOOD Jesus is, without echoing his words (Translation Law).
 - A warmer, genuinely inviting closing question.
 - Number/homophone stress rule: no sentence opens with a bare number.

Narrator: en-US-AndrewNeural (plain American, never Multilingual).
Jesus: en-US-ChristopherNeural (American, never British; speaks ONLY exact KJV).
Jesus lines verified char-for-char against qc/matthew8-kjv.txt:
  j1 = 8:7, j2 = 8:10, j2b = 8:11, j3 = 8:13a.
Each segment is one short caption-screenful mapped to one still.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NAR = "en-US-AndrewNeural"        # plain American — never a Multilingual model
JES = "en-US-ChristopherNeural"   # American. Never a British voice.

# (filename, voice, rate, pitch, text)   text == the on-screen caption, verbatim
SEGMENTS = [
    # --- s1: Capernaum, a Roman-occupied town ---
    ("n1", NAR, "-15%", "-4Hz",
     "This is Capernaum, a fishing town on the Sea of Galilee, where Jesus "
     "often stayed and taught. It was also filled with Roman soldiers — the "
     "army that had conquered these people and now ruled them by force."),
    ("n2", NAR, "-15%", "-4Hz",
     "So the Jews here had every reason to hate Rome. Hold on to that, because "
     "the man this story is about wears a Roman uniform."),
    # --- s2: the dying servant ---
    ("n3", NAR, "-15%", "-4Hz",
     "In one of those Roman houses, a young servant was dying. His body had "
     "gone stiff and useless, and he was in terrible pain."),
    ("n4", NAR, "-15%", "-4Hz",
     "A servant in those days was treated as property. If he died, most "
     "masters would simply replace him. But this master could not bring "
     "himself to walk away."),
    # --- s3: the centurion goes to Jesus ---
    ("n5", NAR, "-15%", "-4Hz",
     "The master was a centurion — a Roman officer in command of a hundred "
     "soldiers. A powerful man, and to the Jews, the enemy."),
    ("n6", NAR, "-15%", "-4Hz",
     "Yet he left his house and went straight to Jesus, a Jewish teacher, to "
     "beg for help. Not for himself. Not even for his own son. For a servant."),
    # --- s4: the humble plea ---
    ("n7", NAR, "-16%", "-4Hz",
     "He came humbly, head bowed, and told Jesus the plain truth: his servant "
     "was at home, unable to move, in agony. Could Jesus help him?"),
    # --- s5: Jesus offers to come (j1) ---
    ("n8", NAR, "-15%", "-4Hz",
     "Jesus did not hesitate for a moment. He answered that he would go to the "
     "house himself."),
    ("j1", JES, "-20%", "-6Hz",
     "I will come and heal him."),
    ("n9", NAR, "-16%", "-4Hz",
     "Stop and see what that means. Jesus was willing to walk into the home of "
     "a Roman — the enemy — for the sake of one dying servant nobody else "
     "valued. That is who Jesus is."),
    # --- s6: not worthy / just say the word ---
    ("n10", NAR, "-16%", "-4Hz",
     "But the officer stopped him. Lord, he said, I am not worthy to have you "
     "come into my home. Only speak the word, and my servant will be healed."),
    ("n11", NAR, "-16%", "-4Hz",
     "He was not just being polite. He truly believed Jesus did not need to be "
     "there at all. He believed that Jesus's word, by itself, was enough."),
    # --- s7: the logic of authority ---
    ("n12", NAR, "-15%", "-4Hz",
     "And he explained why, in the only language a soldier knows. I am a man "
     "under authority, he said. I tell one soldier, Go, and he goes. I tell "
     "another, Come, and he comes."),
    ("n13", NAR, "-16%", "-4Hz",
     "He never has to go himself; his word alone carries his power across the "
     "whole camp. He was certain Jesus's word worked the same way — that it "
     "could reach across the town and heal on its own."),
    # --- s8: Jesus marvels (j2) ---
    ("n14", NAR, "-16%", "-4Hz",
     "And this amazed Jesus. The Gospels almost never say that anyone "
     "surprised him, yet the faith of this Roman outsider stopped him. He "
     "turned to the crowd and said:"),
    ("j2", JES, "-20%", "-6Hz",
     "Verily I say unto you, I have not found so great faith, no, not in "
     "Israel."),
    ("n15", NAR, "-16%", "-4Hz",
     "In plain words: no one among his own people, the ones who should have "
     "known God best, had ever trusted him the way this outsider just had."),
    # --- s9: the door opened to every nation (j2b) ---
    ("n16", NAR, "-16%", "-4Hz",
     "Then Jesus opened heaven wider than anyone listening expected:"),
    ("j2b", JES, "-20%", "-6Hz",
     "And I say unto you, That many shall come from the east and west, and "
     "shall sit down with Abraham, and Isaac, and Jacob, in the kingdom of "
     "heaven."),
    ("n17", NAR, "-16%", "-4Hz",
     "He meant that people from every nation on earth would be welcomed to "
     "God's table. What brings you in is not where you were born, or which "
     "group you belong to. It is whether you trust him."),
    # --- s10: the word that heals (j3) ---
    ("n18", NAR, "-15%", "-4Hz",
     "Then Jesus turned back to the soldier and gave him the one thing he had "
     "asked for — a single word."),
    ("j3", JES, "-20%", "-6Hz",
     "Go thy way; and as thou hast believed, so be it done unto thee."),
    ("n19", NAR, "-16%", "-4Hz",
     "Go home; it has already happened, just as you trusted it would. No "
     "touch, no visit — only his word, sent across the town."),
    # --- s11: healed at a distance ---
    ("n20", NAR, "-16%", "-4Hz",
     "And in that very hour, far away in the Roman house, the young servant "
     "drew a deep, clean breath. The color flowed back into his face, his body "
     "loosened, and he sat up, completely well."),
    ("n21", NAR, "-16%", "-4Hz",
     "No one was in the room with him. He was made whole by nothing but the "
     "word of a man he had never even met."),
    # --- s12: the reunion ---
    ("n22", NAR, "-16%", "-4Hz",
     "When the officer reached home, his servant rose to meet him at the door, "
     "alive and well. This hardened soldier, who commanded a hundred men, came "
     "apart. He had trusted Jesus's word, and the word had been enough."),
    # --- closing card (read aloud gently) ---
    ("card", NAR, "-17%", "-4Hz",
     "This Roman soldier trusted Jesus before he saw any proof at all. Is "
     "there something in your life you would place in Jesus's hands like that "
     "— simply on his word?"),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        await save_narration(text, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
