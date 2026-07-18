#!/usr/bin/env python3
"""Generate narration audio for Story Video #19 — Breakfast on the Shore:
Peter Restored (John 21:1-17).

Narrator: en-US-AndrewNeural — plain American, never a Multilingual model.
Jesus voice: en-US-ChristopherNeural — American, never British.
Jesus speaks ONLY exact KJV: John 21:16 (j1) and John 21:17 (j2).

CAPTIONS ARE VERBATIM (Cameron, 2026-07-11): build.py imports these SEGMENTS
and word-wraps each text as the on-screen caption, so every spoken word is on
the screen. The narrator keeps the KJV Jesus lines in Old English AND explains
plainly, in the next breath, what he meant — the point every time being how
GOOD he is (he restores the man who failed him worst).

Two standards: STILLS-ONLY (Law E) + Jesus face-never (#18) — a parable-simple
shore scene; the Lord is only ever behind / hand-only / at dawn distance.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)  — text is BOTH spoken and captioned.
    # --- Shot 1: the night of the denial (prologue) ---
    ("n1", NARRATOR, "-20%", "-4Hz",
     "Peter had sworn he would die before he would ever deny Jesus."),
    ("n2", NARRATOR, "-22%", "-4Hz",
     "Then, in one terrible night, he denied him three times. The rooster "
     "crowed, Jesus turned and looked at him, and Peter went out and wept "
     "bitterly."),
    # --- Shot 2: back to the old life ---
    ("n3", NARRATOR, "-22%", "-4Hz",
     "After the resurrection, Peter went back to fishing. Back to the old "
     "life."),
    ("n4", NARRATOR, "-22%", "-4Hz",
     "It is what people do with a failure they cannot carry. They go back to "
     "what they knew before it happened. And that night they caught nothing."),
    # --- Shot 3: the figure on the shore ---
    ("n5", NARRATOR, "-22%", "-4Hz",
     "At dawn, a figure on the shore called out to the boat, and told them "
     "where to let down the net. Suddenly it was full."),
    ("n6", NARRATOR, "-22%", "-4Hz",
     "Then one of them went very still and said, it is the Lord. And Peter "
     "did not wait for the boat. He threw himself into the sea and swam for "
     "shore, leaving everything behind."),
    # --- Shot 4: the charcoal fire (the emotional key) ---
    ("n7", NARRATOR, "-22%", "-4Hz",
     "When he waded out of the water, he stopped cold. On the sand was a "
     "charcoal fire, with fish already laid over it, and bread."),
    ("n8", NARRATOR, "-24%", "-4Hz",
     "A charcoal fire. The same kind of fire Peter had stood beside in the "
     "courtyard the night he denied him. The smell alone would have brought "
     "the whole night back."),
    ("n9", NARRATOR, "-22%", "-4Hz",
     "Jesus did not bring up the denial. He simply had breakfast waiting, and "
     "they ate together on the shore in the first gold light."),
    # --- Shot 5: do you love me, three times (the peak) ---
    ("n10", NARRATOR, "-22%", "-4Hz",
     "When breakfast was over, Jesus turned to Peter. Three times, once it "
     "seems for each denial, he asked him the same question, using Peter's "
     "old name, the name he had before any of it:"),
    ("j1", JESUS, "-27%", "-6Hz",
     "Simon, son of Jonas, lovest thou me?"),
    ("n11", NARRATOR, "-22%", "-4Hz",
     "Simon, son of Jonas, do you love me. Not, how could you. Not, prove it. "
     "Not one word thrown back at him about the denial. Only: do you love me."),
    # --- Shot 6: feed my sheep ---
    ("n12", NARRATOR, "-22%", "-4Hz",
     "Three times Peter answered him, yes, Lord, you know that I love you. "
     "Each time it cost him more, and each time he meant it more."),
    ("j2", JESUS, "-26%", "-6Hz",
     "Feed my sheep."),
    ("n13", NARRATOR, "-22%", "-4Hz",
     "Feed my sheep. To the man who had failed him worst, Jesus handed the "
     "biggest job of all. He did not only forgive Peter. He trusted him "
     "again."),
    # --- Shot 7: the failure who feeds ---
    ("n14", NARRATOR, "-24%", "-4Hz",
     "That is how good he is. He takes your worst night and hands you back "
     "your life, with a purpose bigger than the one you thought you had "
     "thrown away."),
    # --- closing card, read gently (Readable-Card Law) ---
    ("card", NARRATOR, "-26%", "-4Hz",
     "Peter went back to fishing because he thought his failure was final. "
     "Is there a failure you have quietly decided is final?"),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        await save_narration(text, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
