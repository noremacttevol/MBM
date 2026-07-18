#!/usr/bin/env python3
"""Generate narration audio for Story Video #41 — Counting the Cost (Luke 14:25-35).

Narrator: en-US-AndrewNeural — plain American, never a Multilingual model.
Jesus voice: en-US-ChristopherNeural — American, never British.

Jesus speaks ONLY exact KJV. Seven lines:
  j1 = Luke 14:26     "hate not his father, and mother..."  — the hard saying
  j2 = Luke 14:27     "whosoever doth not bear his cross..."
  j3 = Luke 14:28     the tower — "sitteth not down first, and counteth the cost"
  j5 = Luke 14:31     the king — ten thousand against twenty thousand
  j6 = Luke 14:32     the ambassage — "conditions of peace"
  j7 = Luke 14:33     THE VERDICT — the verse card line (PAIRING-LIST.md #41)
  j8 = Luke 14:34-35  the salt — "He that hath ears to hear, let him hear"
(There is no j4: vv29-30, the mockery of the half-built tower, is carried by the
narrator in n7. Seven KJV lines with their reverent pauses is the ceiling for a
video this length, and the picture in s7 already says what vv29-30 say.)

CAPTIONS ARE VERBATIM (Cameron, 2026-07-11): build.py imports these SEGMENTS and
word-wraps each text as the on-screen caption.

TRANSLATION LAW: after every KJV line the narrator gives only the plain modern
meaning and never re-quotes or echoes the KJV wording. That is why n6 says "adding
it up" instead of echoing "counteth the cost", n10 says "letting go of your claim"
instead of echoing "forsaketh all", and n12 says "leaches away" instead of echoing
"savour". n3 explains the comparison idiom without repeating v26 back at him.

CLARITY / WHY-LAW — this is the whole job on this story. Three lines in this passage
do real damage if they are delivered flat, and a MILK video that leaves a stranger
thinking Jesus demands you hate your mother, carry an execution beam and hand over
everything you own has done the opposite of its job:
  1. "hate" (v26) is a SEMITIC COMPARISON, not an emotion — the language had no way
     to say "love less" (Genesis 29:31 calls Leah "hated" in the same breath that
     says Jacob loved Rachel more), and Matthew records the same teaching in the
     plain form, "loveth father or mother more than me" (Matt 10:37). n3 says this
     out loud. Without n3 this video should not exist.
     But it is NOT defused into nothing: n4 keeps the cost real. He is asking for
     first place, and first place is a seat you cannot give to two people.
  2. "bear his cross" (v27) is explained (n5) and NEVER depicted — Rome crucified
     along the public roads and the condemned man carried his own beam through his
     own town. No frame in this video shows it.
  3. "forsaketh all" (v33) is about letting go of your CLAIM (n10) — "not that
     everything is taken from you; that nothing is off limits to him."

THE TURN (n13a/n13b) is why this story is milk at all: he had the biggest crowd of
his life and used it to talk people out of following him. Every movement in history
inflates its numbers; he deflated his, out loud, and then let people walk home.
Nothing else in a person's life tells them the price first. The counting is a
KINDNESS — he is not keeping you out, he is keeping you from a half-built life.

NUMBER-STRESS LAW: no sentence opens with a bare number. "An army of ten thousand
against an army of twenty thousand..." and "a foundation with three courses of
stone" — every count lands mid-sentence and stressed, never as a flat leading word.

CLOSING CARD IS AN INVITATION, never a fear-question. No "are you ready?", no "could
you pay it?", no "what if you can't finish?". Fear is not this app's tool because it
was not his.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text) — text is BOTH spoken and captioned.
    # --- s1: v25 — the biggest crowd he ever had ---
    ("n1", NARRATOR, "-20%", "-4Hz",
     "By now the crowd walking with him was enormous. Not a dozen men. "
     "Thousands, filling the road, more joining at every village. This is the "
     "moment every movement dreams about."),
    # --- s2: v25 — and he turned ---
    ("n2", NARRATOR, "-22%", "-4Hz",
     "And then he turned around. And he did the last thing you would expect from "
     "a man with a crowd that size. He started talking them out of it."),
    ("j1", JESUS, "-26%", "-6Hz",
     "If any man come to me, and hate not his father, and mother, and wife, and "
     "children, and brethren, and sisters, yea, and his own life also, he cannot be "
     "my disciple."),
    # --- s3: THE GEM that unlocks the hard saying ---
    ("n3", NARRATOR, "-22%", "-4Hz",
     "That word stops people cold. But in the language he spoke, there was no "
     "way to say love less. You said hate, and everybody heard a comparison. "
     "Jacob hated Leah, and it only ever meant he loved Rachel more. Matthew "
     "wrote the same teaching plainly: anyone who loves father or mother more "
     "than me. He is not asking you to hate anyone. He is asking for first "
     "place."),
    # --- s4: and it still costs everything ---
    ("n4", NARRATOR, "-22%", "-4Hz",
     "And he was not softening it. First place is the one seat you cannot give "
     "to two people. For most of us, what keeps us from him is not some sin. It "
     "is something good we love more."),
    # --- s5: v27 — the cross, explained, never painted ---
    ("j2", JESUS, "-26%", "-6Hz",
     "And whosoever doth not bear his cross, and come after me, cannot be my "
     "disciple."),
    ("n5", NARRATOR, "-22%", "-4Hz",
     "Nobody in that road heard a figure of speech. Rome crucified people along "
     "the highways of Galilee, out in the open, where everybody walked past. And "
     "the condemned man carried the beam himself, through his own town."),
    # --- s6: v28 — the tower ---
    ("j3", JESUS, "-26%", "-6Hz",
     "For which of you, intending to build a tower, sitteth not down first, and "
     "counteth the cost, whether he have sufficient to finish it?"),
    ("n6", NARRATOR, "-22%", "-4Hz",
     "A watchtower in a vineyard guarded the harvest you had worked all year "
     "for. Everyone there had built something. And they all knew you do not "
     "start with the stones. You start sitting on them."),
    # --- s7: vv29-30 — carried by the narrator, not a Jesus line ---
    ("n7", NARRATOR, "-22%", "-4Hz",
     "Because half a tower is worse than none. An empty field is just a field. A "
     "foundation with three courses of stone and weeds growing through it is a "
     "monument to a man who did not think it through."),
    # --- s8: v31 — the king ---
    ("j5", JESUS, "-26%", "-6Hz",
     "Or what king, going to make war against another king, sitteth not down first, "
     "and consulteth whether he be able with ten thousand to meet him that cometh "
     "against him with twenty thousand?"),
    ("n8", NARRATOR, "-22%", "-4Hz",
     "Second picture, higher stakes. And look at what he asks about the king. "
     "Not whether he is brave. Whether he can count. An army of ten thousand "
     "against an army of twenty thousand is arithmetic, not courage."),
    # --- s9: v32 — the war that does not happen ---
    ("j6", JESUS, "-26%", "-6Hz",
     "Or else, while the other is yet a great way off, he sendeth an ambassage, and "
     "desireth conditions of peace."),
    ("n9", NARRATOR, "-22%", "-4Hz",
     "And the wise king does not win the war. He does not fight it. He sends men "
     "to ask for terms while there is still open ground between the armies. Both "
     "stories turn on one act. A man sits down while he still can, and tells "
     "himself the truth."),
    # --- s10: v33 — THE VERDICT. Music is in FULL SILENCE here. ---
    ("j7", JESUS, "-28%", "-6Hz",
     "So likewise, whosoever he be of you that forsaketh not all that he hath, he "
     "cannot be my disciple."),
    ("n10", NARRATOR, "-22%", "-4Hz",
     "He was not telling them to sell their houses in the road that afternoon. "
     "The word means letting go of your claim. No longer keeping one corner of "
     "your life back as the part he does not get to touch. Not that everything "
     "is taken from you. That nothing is off limits to him."),
    # --- s11: it worked, and he let them go ---
    ("n11", NARRATOR, "-22%", "-4Hz",
     "And it worked, the way he meant it to. The crowd got smaller. People who "
     "had walked with him all morning went home. He watched them go, and he did "
     "not lower the price."),
    # --- s12: vv34-35 — the salt, the last word of the discourse ---
    ("j8", JESUS, "-26%", "-6Hz",
     "Salt is good: but if the salt have lost his savour, wherewith shall it be "
     "seasoned? It is neither fit for the land, nor yet for the dunghill; but men "
     "cast it out. He that hath ears to hear, let him hear."),
    ("n12", NARRATOR, "-22%", "-4Hz",
     "Salt from the Dead Sea marshes was never pure. Leave it in the damp and "
     "the salt leaches away, and what is left is a powder that still looks like "
     "salt and does nothing at all. That is the warning. Not a bad man. A man "
     "who looks the part with nothing in him."),
    # --- s13: THE TURN. The whole reason this video exists. ---
    ("n13a", NARRATOR, "-22%", "-4Hz",
     "So here is the question. Why would a man who came to save the world take "
     "the biggest crowd he ever had, and try to thin it out?"),
    ("n13b", NARRATOR, "-22%", "-4Hz",
     "Because he will not let you sign before you have read it. Think what else "
     "in your life ever did that. The loan showed you the payment afterward. The "
     "habit showed you the cost years afterward. He told a crowd the whole price "
     "first, and let them choose."),
    # --- s14: the counting is a kindness ---
    ("n14", NARRATOR, "-22%", "-4Hz",
     "He is not trying to keep you out. He is trying to keep you from a half- "
     "built life. He tells you what it costs because he wants the tower "
     "standing."),
    # --- s15: he had already counted his own ---
    ("n15", NARRATOR, "-24%", "-4Hz",
     "And one more thing. The man asking that crowd to count what it would cost "
     "them had already counted what it would cost him. He was walking toward "
     "Jerusalem while he said it. He knew the number. He did not turn back."),
    # --- s16: the invitation. No pressure. The road is open. ---
    ("n16", NARRATOR, "-24%", "-4Hz",
     "So he is not waiting at the end of that road with a bill. He is standing "
     "at the start of it, telling you the truth, watching to see if you want to "
     "come. He would rather you came slowly than said yes in a hurry and quit."),
    # --- closing card, read gently (Readable-Card Law). An INVITATION. ---
    ("card", NARRATOR, "-26%", "-4Hz",
     "He told a crowd the whole price before a single one of them said yes. "
     "Nothing else in your life has done that for you. What would you ask a man "
     "who refuses to lie to you about the cost?"),
]


# SPOKEN overrides: text sent to the TTS instead of the caption text, to correct a
# word the neural voice reads wrong. The ON-SCREEN caption stays exact KJV; only
# the spoken audio uses these.
#   j7: edge-tts breaks "forsaketh" as fer-SAYK-uhth (Cameron 2026-07-17 — these
#   are Jesus's words, must be right; whisper hears the shipped audio as "for
#   Saccath"). Verified fix (Machine C 2026-07-17): respell "forsayketh" —
#   whisper hears the exact word "forsaketh" in context (for-SAY-keth), while the
#   plain spelling reproduces the broken split under the same test.
SPOKEN = {
    "j7": "So likewise, whosoever he be of you that forsayketh not all that he hath, he "
          "cannot be my disciple.",
}


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        spoken = SPOKEN.get(name, text)
        await save_narration(spoken, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
