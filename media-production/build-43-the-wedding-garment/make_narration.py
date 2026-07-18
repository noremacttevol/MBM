#!/usr/bin/env python3
"""Generate narration audio for Story Video #43 — The Wedding Garment
(Matthew 22:1-14).

Narrator: en-US-AndrewNeural — plain American, never a Multilingual model.
Jesus voice: en-US-ChristopherNeural — American, never British.

Jesus speaks ONLY exact KJV. Five lines. Per the #38/#39/#40 precedent, the
characters quoted INSIDE the parable (here, the KING) are spoken by the Jesus
voice, because Jesus is the one quoting them and the words are exact KJV:
  jv4   = Matt 22:4        the king's invitation ("all things are ready: come")
  jv8_9 = Matt 22:8-9      THE GRACE PIVOT — "go into the highways" (verse-card /
                           sacred silence 1)
  jv12  = Matt 22:12       "Friend, how camest thou in hither..." (the tender
                           pivot — verse-card line, Matt 22:11-12 per PAIRING-LIST;
                           sacred silence 2)
  jv13  = Matt 22:13       "...cast into outer darkness" (exact contiguous span,
                           trimmed of "weeping and gnashing" — the J-law keeps the
                           IMAGE restrained; the narrator carries the meaning gently)
  jv14  = Matt 22:14       "For many are called, but few are chosen." (Jesus's own
                           frame line — the coda)

CARE FLAGS J, L (CONTENT-CARE.md). This is a JUDGMENT parable, and the whole point
of the narration is to CARRY THE MERCY THAT IS IN THE TEXT so it does not rebuild a
cruel God: the invitation goes to EVERYONE off the highways, "both bad and good"
(n9); the king CLOTHES every guest himself at the door (n10); the king calls the one
man "Friend" (jv12, n12). Outer darkness is spoken as a place a man CHOSE, out of a
light left standing open for him (n13) — never a torture threat. The closing card is
an INVITATION, never a fear-question (J-law: no "are you ready?", "which will you
be?").

TRANSLATION LAW: after every KJV line the narrator gives only the plain modern
meaning and never re-quotes or echoes the KJV wording. n15 says "everyone is
invited" and "the ones who came", NOT "many are called / few are chosen"; n8 says
"out to the roads", not "the highways"; n13 says "back outside, in the dark", not
"outer darkness". The one deliberate hook is the single word "Friend" in n12 — the
emotional hinge of the story — which is a one-word echo, not a re-quote of Jesus's
sentence.

CLARITY / WHY-LAW: this parable is heard as "dress right or God tortures you." The
build exists to say the opposite out loud. THE GARMENT GEM (n10-n12): nobody dragged
in off the road owned wedding clothes, so the clean robe was the king's to give,
handed to every guest at the door — the man was not shut out for being poor
(everyone there was poor) but for refusing the free gift. That single fact turns the
whole parable from merit into grace. A viewer with zero Bible background must finish
able to say: the invitation is free, the King clothes you himself, you only have to
come and let him.

NUMBER-STRESS LAW: no sentence opens with a bare number. "Not one of them" is worded
so the count lands stressed mid-sentence; n5 opens "They all had something else"
rather than "One had a field".
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text) — text is BOTH spoken and captioned.
    # --- s1: the frame — he tells the parable to the men who want him gone ---
    ("n1", NARRATOR, "-20%", "-4Hz",
     "He was teaching in the temple, and the men who were hunting for a way to "
     "arrest him were standing right in front of him. So he told them a story: about "
     "a king, a wedding, and an invitation that almost nobody took."),
    # --- s2: v2 — the feast is ready ---
    ("n2", NARRATOR, "-22%", "-4Hz",
     "A king was giving a wedding feast for his son. The oxen were prepared, the "
     "tables were loaded, the hall was full of light. And the guests had been invited "
     "long before. They had already said they would come."),
    # --- s3: v3-4 — the summons goes out. KJV. ---
    ("n3", NARRATOR, "-22%", "-4Hz",
     "So when the day arrived, the king sent his servants to go and bring them in."),
    ("jv4", JESUS, "-26%", "-6Hz",
     "Behold, I have prepared my dinner: my oxen and my fatlings are killed, and all "
     "things are ready: come unto the marriage."),
    # --- s4: v3 — they would not come ---
    ("n4", NARRATOR, "-22%", "-4Hz",
     "And they would not come. Not one of them. They had said yes, and now, with "
     "everything ready and waiting, they simply would not walk over."),
    # --- s5: v5 — they made light of it ---
    ("n5", NARRATOR, "-22%", "-4Hz",
     "They all had something else. A field to go look at. A shop to keep. The king's "
     "own guests looked at his son's wedding and decided they had better things to do."),
    # --- s6: v6-7 — restrained; off-screen. Told in scripture's economy. ---
    ("n6", NARRATOR, "-22%", "-4Hz",
     "And some of them did worse. They turned on the servants who came to invite "
     "them. It was the kind of insult a kingdom does not survive, and that city did "
     "not survive it."),
    # --- s7: v8-9 — the grace pivot. KJV. SACRED SILENCE 1. ---
    ("n7", NARRATOR, "-22%", "-4Hz",
     "But the feast was still ready. The food was still hot. And a hall built for a "
     "wedding was standing empty. So the king made a decision."),
    ("jv8_9", JESUS, "-27%", "-6Hz",
     "The wedding is ready, but they which were bidden were not worthy. Go ye "
     "therefore into the highways, and as many as ye shall find, bid to the marriage."),
    # --- s8: v9 — out to the roads ---
    ("n8", NARRATOR, "-22%", "-4Hz",
     "Out to the roads. Not the guest list. The roads. Whoever happened to be out "
     "there. The day laborers, the beggars, the people nobody ever puts on a list."),
    # --- s9: v10 — both bad and good ---
    ("n9", NARRATOR, "-22%", "-4Hz",
     "They brought in everyone they could find. The story does not clean it up. It "
     "says both the bad and the good, and the wedding hall filled right up."),
    # --- s9 cont / s10: THE GARMENT GEM ---
    ("n10", NARRATOR, "-22%", "-4Hz",
     "And here is the part almost everyone misses. Nobody dragged in off the street "
     "owned wedding clothes. At a king's feast, the clean festival robe was the "
     "king's to give, handed to every guest at the door. Every person in that hall "
     "was wearing something the king had put on them."),
    # --- s10: v11 — the king finds the one man ---
    ("n11", NARRATOR, "-22%", "-4Hz",
     "Then the king came in to meet his guests. And he found one man still in his own "
     "dusty road clothes. Not because he was too poor. Everyone there was too poor. "
     "Because he had been handed a robe at the door, and had said no to it."),
    # --- s11: v12 — Friend. KJV. SACRED SILENCE 2. ---
    ("jv12", JESUS, "-26%", "-6Hz",
     "Friend, how camest thou in hither not having a wedding garment?"),
    ("n12", NARRATOR, "-22%", "-4Hz",
     "Friend. That is what the king called him. Not intruder. Not thief. Friend, and "
     "a question, and every chance in the world to answer. And the man had nothing to "
     "say."),
    # --- s12: v13 — outer darkness. Restrained. KJV span. ---
    ("n13", NARRATOR, "-23%", "-4Hz",
     "He had come to the feast and refused the one thing that made him a guest. So he "
     "ended up where he had chosen to be. Back outside, in the dark, away from a light "
     "that had been standing wide open for him."),
    ("jv13", JESUS, "-27%", "-6Hz",
     "Bind him hand and foot, and take him away, and cast him into outer darkness."),
    # --- s13: the frame returns. v14. KJV. The Why. ---
    ("n14", NARRATOR, "-22%", "-4Hz",
     "The men listening knew exactly who the story was about. They were the invited "
     "guests, the ones who had said yes for a lifetime and would not come when the "
     "King actually arrived. But do not miss what the story is really doing."),
    ("jv14", JESUS, "-26%", "-6Hz",
     "For many are called, but few are chosen."),
    ("n15", NARRATOR, "-22%", "-4Hz",
     "Everyone is invited. That is the whole world. The ones who end up at the table "
     "are simply the ones who came, and who let the King put the clean clothes on "
     "them."),
    # --- s14: the invitation. Milk framing — free, open, no pressure. ---
    ("n16", NARRATOR, "-24%", "-4Hz",
     "You do not have to make yourself presentable first. Nobody in that hall could "
     "have, and neither can you. The invitation is free, the door is open, and the "
     "clean clothes are already bought and folded and waiting inside. All you have to "
     "do is come in, and let him dress you."),
    # --- closing card, read gently (Readable-Card Law) ---
    ("card", NARRATOR, "-26%", "-4Hz",
     "The King fills his hall with people straight off the road, and hands each one "
     "clean clothes at the door. What has he been holding out for you to put on, that "
     "you keep walking past?"),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        await save_narration(text, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
