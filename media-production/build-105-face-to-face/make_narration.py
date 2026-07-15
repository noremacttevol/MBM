#!/usr/bin/env python3
"""Narration audio for Video #105 — Face to Face, as a Friend (Exodus 33).

Narrator: en-US-AndrewNeural. The Lord's voice: en-US-ChristopherNeural (exact KJV
only). The narrative KJV line 'the LORD spake unto Moses face to face, as a man
speaketh unto his friend' is NARRATION (not God's direct speech) and is voiced by the
narrator (white caption); God's own words render cream-italic.

The Lord's KJV lines (Christopher, cream italic):
  jv14  Ex 33:14  "My presence shall go with thee, and I will give thee rest." — silence 1
  jv19  Ex 33:19  "I will make all my goodness pass before thee..."
  jv20  Ex 33:20  "Thou canst not see my face... and live." — silence 2

WHY-LAW: the wonder here is not thunder and law — it is FRIENDSHIP. The God of the
whole universe spoke with a man the way you speak with a trusted friend. And when even
that was not enough for Moses's hungry heart, God did not rebuke him for wanting more —
he tenderly hid him in a rock and let his goodness pass by, because to see God's full
face would be too much for any mortal to bear. Milk framing: God WANTS to be known, as
a friend. Never a threat.

HOMOGRAPH EAR-CHECK: none of the high-risk homographs appear. NUMBER-STRESS LAW obeyed.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"
LORD = "en-US-ChristopherNeural"

SEGMENTS = [
    ("n1", NARRATOR, "-20%", "-4Hz",
     "Moses pitched a tent a little way outside the camp and called it the Tent of "
     "Meeting. It was the place he went to be with God — set apart, quiet, away from "
     "everything else.", None),
    ("n2", NARRATOR, "-22%", "-4Hz",
     "Whenever Moses walked out to that tent, something happened that had never happened "
     "for anyone.", None),
    ("n3", NARRATOR, "-22%", "-4Hz",
     "All the people would rise and stand, each at the door of their own tent, and watch "
     "him go, and worship — because they knew where he was going, and who was waiting "
     "for him there.", None),
    ("n4", NARRATOR, "-22%", "-4Hz",
     "As Moses reached the tent, a great pillar of cloud would come down and stand at the "
     "door — the presence of God himself, come down to meet one man.", None),
    # nface — the heart line (narration, white caption)
    ("nface", NARRATOR, "-22%", "-2Hz",
     "And the Lord spake unto Moses face to face, as a man speaketh unto his friend.", None),
    ("n5", NARRATOR, "-22%", "-4Hz",
     "Not a master barking at a servant. Not a king across a vast throne room. As a man "
     "speaks with his friend — easy, honest, close. God wanted Moses, not just his "
     "obedience. He wanted his friendship.", None),
    # jv14 — the promise, sacred silence 1
    ("jv14", LORD, "-26%", "-6Hz",
     "My presence shall go with thee, and I will give thee rest.", None),
    ("n6", NARRATOR, "-22%", "-4Hz",
     "And that friendship made Moses bold. He asked for the one thing no one had ever "
     "dared to ask. Show me your glory. Let me see you — really see you.", None),
    # jv19 — goodness
    ("jv19", LORD, "-24%", "-6Hz",
     "I will make all my goodness pass before thee, and I will proclaim the name of the "
     "LORD before thee.", None),
    # jv20 — the tender limit, sacred silence 2
    ("jv20", LORD, "-26%", "-6Hz",
     "Thou canst not see my face: for there shall no man see me, and live.", None),
    ("n7", NARRATOR, "-22%", "-4Hz",
     "So God did the gentlest thing. He tucked Moses into a cleft in the rock, and "
     "covered him with his own hand, and let all his goodness pass by — near enough to "
     "feel, too much to look on. He protected his friend even from the weight of his own "
     "glory.", None),
    ("n8", NARRATOR, "-24%", "-4Hz",
     "And when Moses came back down, his face was shining. He did not even know it. That "
     "is what happens to a person who spends time close to God — you start, quietly, to "
     "glow with a little of him. It began with a friendship, at a tent, outside the camp.", None),
    ("card", NARRATOR, "-26%", "-4Hz",
     "God spoke with a man as with a friend, and hid him in a rock to keep him safe from "
     "too much glory. He still wants to be known like that — not feared from far off, but "
     "known up close. Would you let him be that kind of friend to you?", None),
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
