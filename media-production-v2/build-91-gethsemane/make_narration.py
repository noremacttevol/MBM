#!/usr/bin/env python3
"""Narration for build-91-gethsemane — Luke 22.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

THIS BUILD WAS ALREADY RIGHT, AND IT IS THE ONE TO BE MOST CAREFUL WITH.
All four red beats are Jesus speaking in the flesh, all four are verbatim, and a
red-letter KJV inks all four. Every id is unchanged and every one already had a
narrator retelling directly after it. Nothing moved.
  jv38  Matthew 26:38  'My soul is exceeding sorrowful, even unto death: tarry ye
        here, and watch with me.'   (Luke's parallel; the wording in the build is
        Matthew's and is exact, so it is tagged to Matthew.)  n4 retells it.
  jv42  Luke 22:42     'Father, if thou be willing, remove this cup from me:
        nevertheless not my will, but thine, be done.'   n6 retells it.
  jv41  Matthew 26:41  'Watch and pray, that ye enter not into temptation: the
        spirit indeed is willing, but the flesh is weak.'   n10 retells it.
  jv46  Matthew 26:46  'Rise, let us be going: behold, he is at hand that doth
        betray me.'   n12 retells it.

ON THE WORDING OF THE PRAYER. Matthew 26:39 has 'O my Father, if it be possible,
let this cup pass from me: nevertheless not as I will, but as thou wilt.' Luke
22:42 has 'Father, if thou be willing, remove this cup from me: nevertheless not
my will, but thine, be done.' Both are red and both are exact. The build already
carried Luke's wording word for word, and this build's reference is Luke 22, so
Luke's is what stayed. It was not changed for the sake of changing it.

NO GREEN, DELIBERATELY. The Father does not speak in Gethsemane. Luke 22:43 sends
an angel to strengthen him and records no words. n8 already says the right thing
about it -- heaven's answer was not to take the pain away but to come near. No
green beat was added, because there is nothing to put in it.

WOMEN: Gethsemane records no woman speaking. Nothing added, nothing invented.

CONSIDERED, LEFT OUT. Luke 22:40, 'Pray that ye enter not into temptation,' is
red, and n2 currently paraphrases it. Left out because it is the same sentence as
jv41, which is already in the video eight beats later; lifting both would play as
a repeat and would blunt the one that matters.

WHY-LAW: he asked for another way, out loud, and then handed the answer to his
Father anyway. Milk: asking is allowed. Trusting the answer is the faith.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "It was late on the night before he died. The supper was over, the songs were sung, and Jesus led his friends out of the city, down across the valley, and up into a quiet grove of olive trees called Gethsemane. He had come here often. But this night was not like the others."),
    ("n2", NARRATOR, "At the edge of the garden he stopped, and asked most of them to sit and wait while he went ahead to pray. He told them gently to pray as well, so that what was coming would not overtake them. Then he went deeper into the trees."),
    ("n3", NARRATOR, "He took only three with him — Peter, James, and John, the ones who had been closest to him. And as he walked, something began to break over him: a weight none of them had ever seen him carry. He was sorrowful, and deeply troubled."),
    # Matthew 26:38
    ("jv38", JESUS, "My soul is exceeding sorrowful, even unto death: tarry ye here, and watch with me."),
    ("n4", NARRATOR, "He did not hide it from them. He told them plainly how heavy his heart was — heavy enough, he said, to crush the life out of him — and he asked them simply to stay near, and stay awake, while he prayed. He did not want to be alone."),
    ("n5", NARRATOR, "Then he went on a little further by himself, about as far as a man can throw a stone, and he sank down onto the ground among the roots and the rocks. Everything that was coming, all of it, he carried to his Father in prayer."),
    # Luke 22:42
    ("jv42", JESUS, "Father, if thou be willing, remove this cup from me: nevertheless not my will, but thine, be done."),
    ("n6", NARRATOR, "He asked, honestly, if there were any other way — if this cup of suffering could pass from him, let it pass. But even in his agony he did not stop there. Whatever his Father wanted, that was what he wanted more. Not his own will, he prayed, but his Father's."),
    ("n7", NARRATOR, "This was no calm, quiet moment. Luke, who was a physician, tells us that as he prayed in that anguish, his sweat fell like great drops of blood to the ground. The suffering was real, and he felt every ounce of it. And still he stayed, and still he prayed."),
    ("n8", NARRATOR, "And heaven did not leave him there alone. An angel came to him out of the darkness and strengthened him. God's answer, in that hour, was not to take the pain away. It was to come near, and hold him up, and give him what he needed to go on. He was not abandoned."),
    ("n9", NARRATOR, "When he rose and came back to his three friends, he found them fast asleep. Not from carelessness — Luke says they were sleeping for sorrow. Their own grief had worn them out. He had asked them to watch with him, and they could not."),
    # Matthew 26:41
    ("jv41", JESUS, "Watch and pray, that ye enter not into temptation: the spirit indeed is willing, but the flesh is weak."),
    ("n10", NARRATOR, "He woke them, but he did not scold them. He understood exactly what they were made of. Their hearts longed to be faithful; their tired bodies simply gave out. He knew the difference, and he was tender with them even now, on the worst night of his life."),
    ("n11", NARRATOR, "He went back and prayed again, and a third time, the very same words, until his heart was fully settled. The struggle was over. He had looked straight at everything that was coming, and he had said yes to his Father anyway. He rose from that place resolved."),
    # Matthew 26:46
    ("jv46", JESUS, "Rise, let us be going: behold, he is at hand that doth betray me."),
    ("n12", NARRATOR, "Across the valley, torches were already winding up the hill — the men who had come to arrest him. He did not run, and he did not hide. He woke his friends, and he walked out to meet it. Everything he had just wrestled with in the dark, he now carried toward the cross. He did it on purpose. He did it for us."),
    ("card", NARRATOR, "On the hardest night of his life, Jesus asked his Father for another way — and then trusted him with the answer. He faced that night so that you would never have to face your darkest one alone. Where is he asking you to trust him, even now?"),
]

# Homographs this build decides for itself (never auto-replaced globally).
SPOKEN = {}


async def main():
    os.makedirs("audio", exist_ok=True)
    for name, speaker, text in SEGMENTS:
        flagged = [w for w in audit(text) if w not in SPOKEN]
        if flagged:
            print(f"  ! {name}: undecided homograph(s) {flagged}")
        await save_speaker_narration(spoken_text(text, SPOKEN, speaker), speaker,
                                     f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3  [{speaker}]")


if __name__ == "__main__":
    asyncio.run(main())
