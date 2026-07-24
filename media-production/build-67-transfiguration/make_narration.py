#!/usr/bin/env python3
"""Generate narration audio for Story Video #67 — The Transfiguration (Matt 17:1-8 / Mark 9).
Narrator: modern, warm, low, unhurried (American). Plain US model only.
Jesus voice: AMERICAN, never British. Jesus speaks ONLY exact KJV: Matt 17:7.
The FATHER'S voice from the cloud (Matt 17:5) is read by the scripture voice as an
exact quotation — the Father is never voiced as a character (build-169/#69 precedent).
CONTENT-CARE: glory handled as tender comfort, never awe-terror; the cloud reassures.
HOMOGRAPH LAW: ear-check list scanned; no offenders voiced.
Built on Hermes draft row-067; expanded per WHY-law (why Moses & Elijah, why 'hear him').
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.
SCRIPTURE = JESUS                   # scripture-quote voice (the voice from the cloud)

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0", NARRATOR, "-20%", "-4Hz",
     "About a week after Jesus first told his friends plainly that he "
     "was going to Jerusalem to suffer and die, he took three of them "
     "— Peter, James, and John — and led them up a high mountain, off "
     "by themselves. The same three who would later watch him sweat "
     "blood in a garden. Before the darkness, he gave them a glimpse "
     "of the light."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "And there, as he was praying, it happened. The gospel writers "
     "reach for words and almost run out. His face changed. His plain "
     "clothes turned a white so pure that Mark says no laundry on "
     "earth could match it. For one unguarded moment, the glory Jesus "
     "had always carried underneath simply came to the surface. This "
     "was not light shining ON him. It was light coming OUT of who he "
     "already was."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "This is worth sitting with. The disciples had been following a "
     "carpenter from Nazareth — dusty feet, tired eyes, a man who got "
     "hungry and slept in boats. And for one moment the veil lifted, "
     "and they saw who had been walking beside them the whole time. "
     "The wonder is not that he shone on the mountain. The wonder is "
     "that he hid it every other day."),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "And he was not alone. Two men from the old scriptures stood with "
     "him and talked with him: Moses, who gave the law, and Elijah, "
     "the greatest of the prophets. The law and the prophets — the "
     "whole Old Testament, standing on that mountain — and both of "
     "them turned toward Jesus, because both of them had always been "
     "pointing to him."),
    ("n4", NARRATOR, "-20%", "-4Hz",
     "Peter, being Peter, could not just be still. He blurted out "
     "that they should build three shelters — one for Jesus, one for "
     "Moses, one for Elijah — trying to hold the moment, to make it "
     "last, maybe to keep all three side by side and equal. He meant "
     "well. He had not yet understood that these three did not belong "
     "on the same level."),
    ("n5", NARRATOR, "-20%", "-4Hz",
     "And while he was still talking, a bright cloud came down and "
     "wrapped the whole peak — the same kind of cloud that had filled "
     "the temple, the presence of God himself settling over them. And "
     "out of that cloud came a voice — the same voice that had spoken "
     "at the river, the Father speaking about his Son:"),
    # Exact KJV Matt 17:5 — the voice from the cloud (scripture-voice). SACRED SILENCE.
    ("jv1", SCRIPTURE, "-26%", "-6Hz",
     "This is my beloved Son, in whom I am well pleased; hear ye him."),
    ("n6", NARRATOR, "-20%", "-4Hz",
     "Hear ye him. It was a gentle correction to Peter's plan. Do not "
     "build three equal shelters — there are not three voices to "
     "listen to here. There is one. Moses and Elijah were signposts; "
     "Jesus is the destination. And at the sound of the voice, the "
     "three men fell on their faces, overwhelmed. That is when Jesus "
     "did the most tender thing on that whole blazing mountain."),
    # Exact KJV Matt 17:7 — SILENCE around it.
    ("j1", JESUS, "-20%", "-2Hz",
     "Arise, and be not afraid."),
    ("n7", NARRATOR, "-20%", "-4Hz",
     "He came over, and touched them, and told them not to be afraid. "
     "And when they lifted their eyes, the light had gently drawn "
     "back, the cloud was gone, Moses and Elijah were gone — and "
     "there was Jesus, alone, the same friend they had climbed up "
     "with. The glory had not made him distant. He reached down into "
     "their fear, with a hand and a familiar face, and walked them "
     "back down the mountain."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "The Father said it as plainly as it can be said: this is my Son "
     "— hear him. Whatever else is shouting at you, lean in, and "
     "listen. That same voice is still speaking."),
]

# HOMOGRAPH LAW — scanned: no bow/wound/wind/tears/lead/sow/live(s)/read/dove/
# bass/minute/use(d)/close voiced. No overrides needed.
SPOKEN = {}


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts_text = SPOKEN.get(name, text)
        tts = edge_tts.Communicate(tts_text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
