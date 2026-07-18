#!/usr/bin/env python3
"""Generate narration audio for Story Video #124 — Gethsemane
(Luke 22:39-46, with the fuller witness of Matthew 26:36-46).

Narrator: en-US-AndrewNeural — plain American, never a Multilingual model.
Jesus voice: en-US-ChristopherNeural — American, never British.

Jesus speaks ONLY exact KJV. Four lines — his words in the garden:
  jv38 = Matthew 26:38  "my soul is exceeding sorrowful ... watch with me"
  jv42 = Luke 22:42     "Father ... not my will, but thine, be done"  (SACRED SILENCE 1)
  jv41 = Matthew 26:41  "watch and pray ... the spirit ... the flesh is weak"
  jv46 = Matthew 26:46  "Rise, let us be going ... he is at hand that doth betray me"  (SILENCE 2)

The two sacred silences land on the two turning beats: jv42 (the surrender — "not my
will, but thine"), the theological heart of the whole night, and jv46 (he rises to meet
it) — the courage that carries him to the cross.

CARE FLAGS: ARC, R, G (CONTENT-CARE #124).
  R — the agony is real but restrained: the narration names the sweat "like great drops
  of blood" once, plainly, as Luke's physician detail, and never lingers or grows gory.
  G — the grief is honored, not rushed, and God's answer is PRESENCE: the angel (n8) is
  the hope-beat, and the narration lands there ("He was not abandoned").
  ARC — the arrest is only distant torches; no violence in word or picture.

TRANSLATION LAW: after each KJV line the narrator gives the plain meaning and never
re-quotes it (n4 says "how heavy his heart was," not "exceeding sorrowful"; n6 says
"whatever his Father willed," not "not my will but thine"; n10 says "their tired bodies
gave out," not "the flesh is weak").

MILK FRAMING: this is the goodness of Jesus — he faced the worst night in love, on
purpose, for us. The closing card is an invitation to trust him, never a fear-question.

NUMBER-STRESS LAW: no sentence opens with a bare number.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"
JESUS = "en-US-ChristopherNeural"

SEGMENTS = [
    # (filename, voice, rate, pitch, text) — text is BOTH spoken and captioned.
    # --- s1: arrival at the garden ---
    ("n1", NARRATOR, "-22%", "-4Hz",
     "It was late on the night before he died. The supper was over, the songs were "
     "sung, and Jesus led his friends out of the city, down across the valley, and up "
     "into a quiet grove of olive trees called Gethsemane. He had come here often. But "
     "this night was not like the others."),
    # --- s2: sit ye here ---
    ("n2", NARRATOR, "-22%", "-4Hz",
     "At the edge of the garden he stopped, and asked most of them to sit and wait "
     "while he went ahead to pray. He told them gently to pray as well, so that what "
     "was coming would not overtake them. Then he went deeper into the trees."),
    # --- s3: he took Peter, James and John ---
    ("n3", NARRATOR, "-22%", "-4Hz",
     "He took only three with him — Peter, James, and John, the ones who had been "
     "closest to him. And as he walked, something began to break over him: a weight "
     "none of them had ever seen him carry. He was sorrowful, and deeply troubled."),
    # --- s4: jv38 — exceeding sorrowful ---
    ("jv38", JESUS, "-26%", "-6Hz",
     "My soul is exceeding sorrowful, even unto death: tarry ye here, and watch with "
     "me."),
    ("n4", NARRATOR, "-22%", "-4Hz",
     "He did not hide it from them. He told them plainly how heavy his heart was — "
     "heavy enough, he said, to crush the life out of him — and he asked them simply "
     "to stay near, and stay awake, while he prayed. He did not want to be alone."),
    # --- s5: withdrawn a stone's cast ---
    ("n5", NARRATOR, "-22%", "-4Hz",
     "Then he went on a little further by himself, about as far as a man can throw a "
     "stone, and he sank down onto the ground among the roots and the rocks. "
     "Everything that was coming, all of it, he carried to his Father in prayer."),
    # --- s6: jv42 — not my will, but thine. SACRED SILENCE 1 ---
    ("jv42", JESUS, "-27%", "-6Hz",
     "Father, if thou be willing, remove this cup from me: nevertheless not my will, "
     "but thine, be done."),
    ("n6", NARRATOR, "-22%", "-4Hz",
     "He asked, honestly, if there were any other way — if this cup of suffering could "
     "pass from him, let it pass. But even in his agony he did not stop there. Whatever "
     "his Father wanted, that was what he wanted more. Not his own will, he prayed, but "
     "his Father's."),
    # --- s7: the agony, drop by drop (R — restrained) ---
    ("n7", NARRATOR, "-22%", "-4Hz",
     "This was no calm, quiet moment. Luke, who was a physician, tells us that as he "
     "prayed in that anguish, his sweat fell like great drops of blood to the ground. "
     "The suffering was real, and he felt every ounce of it. And still he stayed, and "
     "still he prayed."),
    # --- s8: the angel — God's answer is presence (G — the hope beat) ---
    ("n8", NARRATOR, "-22%", "-4Hz",
     "And heaven did not leave him there alone. An angel came to him out of the "
     "darkness and strengthened him. God's answer, in that hour, was not to take the "
     "pain away. It was to come near, and hold him up, and give him what he needed to "
     "go on. He was not abandoned."),
    # --- s9: found them sleeping for sorrow ---
    ("n9", NARRATOR, "-22%", "-4Hz",
     "When he rose and came back to his three friends, he found them fast asleep. Not "
     "from carelessness — Luke says they were sleeping for sorrow. Their own grief had "
     "worn them out. He had asked them to watch with him, and they could not."),
    # --- s10: jv41 — the spirit is willing, the flesh is weak ---
    ("jv41", JESUS, "-26%", "-6Hz",
     "Watch and pray, that ye enter not into temptation: the spirit indeed is willing, "
     "but the flesh is weak."),
    ("n10", NARRATOR, "-22%", "-4Hz",
     "He woke them, but he did not scold them. He understood exactly what they were "
     "made of. Their hearts longed to be faithful; their tired bodies simply gave out. "
     "He knew the difference, and he was tender with them even now, on the worst night "
     "of his life."),
    # --- s11: the third prayer, settled ---
    ("n11", NARRATOR, "-22%", "-4Hz",
     "He went back and prayed again, and a third time, the very same words, until his "
     "heart was fully settled. The struggle was over. He had looked straight at "
     "everything that was coming, and he had said yes to his Father anyway. He rose "
     "from that place resolved."),
    # --- s12: jv46 — Rise, let us be going. SACRED SILENCE 2 ---
    ("jv46", JESUS, "-26%", "-6Hz",
     "Rise, let us be going: behold, he is at hand that doth betray me."),
    ("n12", NARRATOR, "-22%", "-4Hz",
     "Across the valley, torches were already winding up the hill — the men who had "
     "come to arrest him. He did not run, and he did not hide. He woke his friends, and "
     "he walked out to meet it. Everything he had just wrestled with in the dark, he "
     "now carried toward the cross. He did it on purpose. He did it for us."),
    # --- closing card, read gently (Readable-Card Law) ---
    ("card", NARRATOR, "-25%", "-4Hz",
     "On the hardest night of his life, Jesus asked his Father for another way — and "
     "then trusted him with the answer. He faced that night so that you would never "
     "have to face your darkest one alone. Where is he asking you to trust him, even "
     "now?"),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        await save_narration(text, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
