#!/usr/bin/env python3
"""Generate narration audio for Story Video #148 — Ruth and the Redeemer
(Ruth 1:16-17; 4:13-17). From DRAFTS/row-148.md, validated against the laws.
Narrator: modern, warm, low, unhurried (American). Plain US model only.
Old Testament narrative — Jesus does not appear and there is no KJV line in
this draft: Ruth's vow is carried as the narrator's modern paraphrase (the
Translation Law permits paraphrase; only KJV itself is barred from the
narrator, and none is quoted).
HOMOGRAPH LAW — BUILDER EAR-CHECK n7 ("the line that LEADS to the greater
Redeemer"): "lead" is on the flag list — must read /LEEDZ/, never /LEDZ/.
The natural reading is usually right; LISTEN before assembly. If misread,
respell SPOKEN "leeds". No other flagged words in any segment (the draft's
"tears"/"live" flags refer to words that do not appear in the final text).

SEGMENTATION (ASSEMBLY-C, 2026-07-17): n6 split at its sentence break so all
9 stills carry a beat synced to what is being said (CAPTION LAW): n6a→s7 the
town gate, n6b→s8 Naomi's arms filled. Words unchanged from the draft.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0", NARRATOR, "-20%", "-4Hz",
     "A widow named Naomi lost everything in a foreign land — her "
     "husband and both sons buried there."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "She told her two daughters-in-law to go home. One kissed her "
     "and left. But Ruth clung to her."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "Where you go, I'll go, Ruth said. Your people will be my "
     "people, and your God my God."),
    # sacred-silence beat follows n2.
    ("n3", NARRATOR, "-20%", "-4Hz",
     "Back in Bethlehem, Ruth gleaned grain in the fields to keep "
     "Naomi fed — and the field belonged to a man named Boaz."),
    ("n4", NARRATOR, "-20%", "-4Hz",
     "Boaz noticed her. He protected her, fed her, and spoke "
     "kindly. He was a near kinsman — a redeemer by the law."),
    ("n5", NARRATOR, "-20%", "-4Hz",
     "At the threshing floor, Ruth asked him to cover her with his "
     "cloak, the sign of a kinsman's duty. He promised to redeem "
     "her."),
    ("n6a", NARRATOR, "-20%", "-4Hz",
     "Before the town gate, Boaz bought the right to marry Ruth."),
    ("n6b", NARRATOR, "-20%", "-4Hz",
     "Naomi's emptiness was filled; a son was born."),
    ("n7", NARRATOR, "-20%", "-4Hz",
     "That boy became the grandfather of King David — and part of "
     "the line that leads to the greater Redeemer still to come."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "Ruth gave up everything to follow the God she'd come to "
     "love. He never let her go. Neither will He let you go."),
]

# HOMOGRAPH LAW — ear-check n7 "leads" (see docstring). If misread,
# uncomment the override. Captions stay exact.
SPOKEN = {
    # "n7": ("That boy became the grandfather of King David — and part of "
    #        "the line that leeds to the greater Redeemer still to come."),
}


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts_text = SPOKEN.get(name, text)
        tts = edge_tts.Communicate(tts_text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
