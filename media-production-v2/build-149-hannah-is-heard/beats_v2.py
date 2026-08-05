#!/usr/bin/env python3
"""V2 beat map — row 149, build-149-hannah-is-heard (1 Samuel 1).

COVERAGE: 22 pictures over 126.2 s = 5.7 s/picture (matches the library density).

SCRIPTURE FACTS (1 Samuel 1 KJV):
  1:7   "year by year... therefore she wept, and did not eat" — the
        yearly grief at SHILOH; her ADVERSARY (the other wife)
        provoked her.
  1:13  "Hannah, she SPAKE IN HER HEART; only her LIPS MOVED, but
        her voice was not heard: therefore Eli thought she had been
        drunken."
  1:11  the vow: "if thou wilt... REMEMBER ME... but wilt give unto
        thine handmaid A MAN CHILD, then I WILL GIVE HIM UNTO THE
        LORD all the days of his life."
  1:15  "No, my lord, I am a woman of A SORROWFUL SPIRIT... I have
        POURED OUT MY SOUL before the LORD."
  1:17  Eli: "GO IN PEACE: and the God of Israel grant thee thy
        petition."
  1:18  "her countenance was NO MORE SAD." — before any answer came.
  1:20  SAMUEL — "Because I have ASKED HIM of the LORD."
  1:28  "I have LENT HIM to the LORD; as long as he liveth" — she
        kept the vow.

RENDERING LAWS:
  - HANNAH'S GRIEF WITH TOTAL DIGNITY (rows 44/74 class): barrenness
    rendered as the empty lap and the yearly ache — never abject,
    never hysterical; her silent prayer is the row's centre.
  - THE OTHER WIFE (b02) is smugness, not cartoon cruelty: a
    satisfied glance across the feast, her children arranged around
    her; Hannah bearing it. One frame only; she is not the story.
  - ELI's misreading (b11) is weary error, not malice; his turn to
    compassion (b13-b16) must read across the beats.
  - THE VOW'S PARADOX is the row's signature gesture-language: the
    asking hand drawn in, the giving hand open out (b06/b09/b10) —
    wanting and surrendering in one body.
  - b17's eased face comes BEFORE any answer — faith's receipt; do
    not stage the child early.
  - b22's leaving: Hannah walks away DOWN the road while little
    Samuel stands with Eli at the door — the costliest kept vow;
    her face broken AND at peace; direction law exact.

TIME OF DAY ARC (intentional): the yearly grief in flat bright
festival light; the silent prayer at DUSK by the doorpost lamps
(deliberate); the Eli exchange in the same lamplit dusk; the eased
walk in soft evening; the child scenes in warm gold; the leaving
at clear quiet morning.

CHANGING CONDITIONS (kept OUT of the locks): Hannah's face — worn
with grief, then eased, then radiant, then broken-and-at-peace;
Samuel — newborn, toddling, then a small boy at the door.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Only Jesus wears cream (not in this row).
LOCKS = {
    "HANNAH": (
        "HANNAH LOCK: Hannah is the same woman in every shot — "
        "about thirty, slight and fine-featured with deep gentle "
        "eyes, dark hair under a DEEP MADDER-BROWN head-shawl, a "
        "simple DARK SLATE-BLUE dress with a woven belt (never "
        "cream, never white); grief with dignity, then ease, then "
        "radiance; never abject."
    ),
    "ELI": (
        "ELI LOCK: Eli is the same man in every shot — the old "
        "priest of Shiloh, heavy and slow, about seventy-five, a "
        "long white beard, dim kind eyes, in DARK PRIESTLY LAYERS "
        "of deep blue and umber (never cream, never white); weary "
        "error turning to blessing."
    ),
    "SHILOH": (
        "SHILOH LOCK: the house of the LORD at Shiloh — a "
        "weathered stone-and-timber sanctuary court with a broad "
        "doorway flanked by posts, oil lamps at the posts, worn "
        "steps, festival tents on the slope beyond. The same "
        "doorway, posts and court throughout."
    ),
    "SAMUEL": (
        "SAMUEL LOCK: Samuel is the same child at each age — dark "
        "curls, his mother's deep gentle eyes, in a small DARK "
        "OLIVE tunic (never cream, never white; his little robe is "
        "his mother's yearly gift); newborn, toddler, then a small "
        "boy of about four."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r149-b01", "out": "s01-year-after-year-hannah-went.jpeg", "seg": "n0a",
        "window": "0.40-4.53", "wide": True, "jesus": False, "ref": False,
        "locks": ["HANNAH", "SHILOH"],
        "narration": (
            "Year after year, Hannah went to the house of the LORD and came "
            "away with an empty lap."
        ),
        "must_show": "the yearly ache — the festival court at Shiloh full of families and children, and Hannah moving through them with her arms and lap conspicuously empty; grief with dignity amid plenty.",
        "must_not_show": "no halo; her emptiness carried by CONTRAST (families everywhere), never by collapse.",
        "scene": (
            "The festival is a yearly inventory of what she "
            "does not have, the camera looking across the "
            "court past the milling families' backs: Shiloh's "
            "steps alive with pilgrims — babies riding hips, "
            "toddlers towed by their wrists, boys chasing "
            "between the tents — and moving through all of "
            "that abundance, upright and alone, Hannah with "
            "her shawl drawn close over an empty lap — a "
            "woman keeping her yearly appointment with the "
            "house of the LORD, and with the ache she brings "
            "home from it every year unchanged. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r149-b02", "out": "s02-the-other-wife-mocked-her.jpeg", "seg": "n0b",
        "window": "6.09-7.99", "wide": False, "jesus": False, "ref": False,
        "locks": ["HANNAH"],
        "narration": "The other wife mocked her for it.",
        "must_show": "the provocation — across the feast cloth, the other wife's smug satisfied glance, her several children arranged around her; Hannah bearing it with a still face.",
        "must_not_show": "no halo; the mockery a GLANCE, not cartoon cruelty; Hannah's stillness dignified.",
        "scene": (
            "The wound is administered with one satisfied "
            "look: across the feast cloth the other wife "
            "presides over her arranged abundance — a baby "
            "at her shoulder, children flanking her like "
            "credentials — and lets her glance travel slow "
            "and smug to Hannah's empty place setting — "
            "nothing said, nothing needing to be — while "
            "Hannah receives the yearly barb with a still "
            "face and steady hands, bearing what she has "
            "learned no feast will let her forget. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r149-b03", "out": "s03-one-year-at-shiloh-hannah.jpeg", "seg": "n1",
        "window": "9.43-16.94", "wide": False, "jesus": False, "ref": False,
        "locks": ["HANNAH", "SHILOH"],
        "narration": (
            "One year at Shiloh, Hannah slipped to the door of the "
            "tabernacle and prayed with a voice no one could hear — only "
            "her lips moved."
        ),
        "must_show": "SCRIPTURE-EXACT: the silent prayer — Hannah alone at the lamplit doorpost at dusk, lips moving without sound, tears bright; the row's centre image.",
        "must_not_show": "no halo; the silence VISIBLE — moving lips, no gesture of wailing; dusk lamps physical.",
        "scene": (
            "The most important prayer in Israel that year "
            "makes no sound at all: Hannah alone at the "
            "tabernacle doorpost in the dusk, the post-lamps "
            "warm on her wet face, her lips moving through "
            "words that never reach the air — the feast's "
            "noise far behind her, the sanctuary dark and "
            "listening ahead — a woman pouring her whole "
            "soul through the crack under heaven's door in "
            "complete silence, only her lips carrying the "
            "torrent. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r149-b04", "out": "s04-this-is-what-she-said.jpeg", "seg": "n1",
        "window": "16.94-18.81", "wide": False, "jesus": False, "ref": False,
        "locks": ["HANNAH"],
        "narration": "This is what she said.",
        "must_show": "the words' gate — extreme close on Hannah's moving lips and wet lashes in the lamp warmth; the prayer about to be given to the viewer.",
        "must_not_show": "no halo; extreme close, tender — lips and lashes carry the frame.",
        "scene": (
            "Lean close enough and the silence has words in "
            "it: extreme close on Hannah's face in the lamp "
            "warmth — the lips shaping their soundless "
            "syllables one by one, the lashes heavy and "
            "bright, a tear finding the line of her cheek — "
            "the camera close the way heaven was close, "
            "reading what no ear in the court could catch — "
            "and the words themselves arriving now, for us, "
            "the way they arrived above. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r149-b05", "out": "s05-o-lord-of-hosts-if.jpeg", "seg": "w1a",
        "window": "20.35-28.01", "wide": False, "jesus": False, "ref": False,
        "locks": ["HANNAH", "SHILOH"],
        "narration": (
            "O LORD of hosts, if thou wilt indeed look on the affliction of "
            "thine handmaid, and remember me, and not forget thine handmaid,"
        ),
        "must_show": "SCRIPTURE-EXACT: the plea — Hannah's face upturned at the doorpost, both hands pressed at her chest; look-on-me and remember-me in the posture.",
        "must_not_show": "no halo; the hands AT HER CHEST (the drawn-in asking hand of the row's gesture-language).",
        "scene": (
            "The plea leads with her own smallness: Hannah's "
            "face tips up into the dark above the doorposts — "
            "O LORD of HOSTS, commander of everything — and "
            "both her hands press in against her chest, "
            "gathering herself into the smallest possible "
            "offering — look on the affliction of thine "
            "handmaid; REMEMBER me; do not forget — the "
            "asking hands drawn in tight over the exact "
            "place the ache lives, before the LORD of "
            "armies, at the door. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r149-b06", "out": "s06-but-wilt-give-unto-thine.jpeg", "seg": "w1b",
        "window": "29.95-36.26", "wide": False, "jesus": False, "ref": False,
        "locks": ["HANNAH", "SHILOH"],
        "narration": (
            "but wilt give unto thine handmaid a man child, then I will "
            "give him unto the LORD all the days of his life."
        ),
        "must_show": "SCRIPTURE-EXACT: the vow — her hands turning OUTWARD and open toward the sanctuary even as the ask is made; asking and giving-back in one motion; the row's signature gesture.",
        "must_not_show": "no halo; the hands' TURN readable — drawn-in ask becoming open-out offering.",
        "scene": (
            "The ask turns into an offering before it "
            "finishes leaving her: as the vow's second half "
            "comes — give me a son — Hannah's pressed-in "
            "hands turn slowly OUTWARD, palms opening toward "
            "the dark sanctuary door — and I will GIVE HIM "
            "BACK, all the days of his life — the wanting "
            "and the surrendering performed in one motion by "
            "two hands that cannot tell anymore which they "
            "are doing — the boldest trade ever proposed at "
            "that doorway, silently. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r149-b07", "out": "s07-just-look-at-me-she.jpeg", "seg": "n2",
        "window": "38.14-39.85", "wide": False, "jesus": False, "ref": False,
        "locks": ["HANNAH"],
        "narration": "Just look at me, she was saying.",
        "must_show": "the plea's core — extreme close: the wet upturned eyes alone, asking only to be SEEN; the simplest prayer underneath the vow.",
        "must_not_show": "no halo; the eyes the whole frame — seen-ness as the request.",
        "scene": (
            "Under all the vow's architecture the request is "
            "tiny: extreme close on the upturned eyes — wet, "
            "steady, aimed past the lintel into the dark "
            "where the LORD of hosts keeps his listening — "
            "and everything in them saying only the smallest "
            "thing a person can ask of heaven: look at me — "
            "just look — one woman at a door, requesting "
            "eye contact with God, which is where every "
            "miracle in her story begins. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r149-b08", "out": "s08-remember-me.jpeg", "seg": "n2",
        "window": "39.85-40.92", "wide": False, "jesus": False, "ref": False,
        "locks": ["HANNAH"],
        "narration": "Remember me.",
        "must_show": "the two words — Hannah's small hand flat over her own heart at the doorpost; remembrance asked for at the body's centre.",
        "must_not_show": "no halo; the hand small and flat at the HEART — nothing else moves.",
        "scene": (
            "Two words, one hand: Hannah's palm comes to "
            "rest flat over her own heart in the lamp "
            "warmth — remember ME — the place she keeps the "
            "whole unanswered decade pressed gently under "
            "her own fingers, held up for heaven's "
            "attention like a child showing where it "
            "hurts — the entire petition reduced to its "
            "kernel: that the God of armies would keep one "
            "small name in mind. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r149-b09", "out": "s09-she-asked-for-the-one.jpeg", "seg": "n2",
        "window": "47.03-53.56", "wide": False, "jesus": False, "ref": False,
        "locks": ["HANNAH", "SHILOH"],
        "narration": (
            "She asked for the one thing she wanted most, and promised it "
            "away in the same breath."
        ),
        "must_show": "the paradox stated — both gestures at once: one hand drawn in at her chest (the wanting), the other open toward the sanctuary (the giving away); the row's signature in full.",
        "must_not_show": "no halo; BOTH hands doing their opposite jobs simultaneously — the paradox readable.",
        "scene": (
            "Her two hands are doing opposite things and "
            "both are telling the truth: the left drawn in "
            "hard against her chest, holding the want of "
            "her whole life — and the right open outward "
            "toward the sanctuary dark, already giving "
            "away the thing the left is asking for — one "
            "breath carrying both clauses, one woman "
            "wanting most and surrendering first, the "
            "prayer that out-negotiated every sensible "
            "prayer in the court by offering heaven its "
            "own gift back. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r149-b10", "out": "s10-give-me-a-son-and.jpeg", "seg": "n2",
        "window": "42.32-47.03", "wide": False, "jesus": False, "ref": False,
        "locks": ["HANNAH", "SHILOH"],
        "narration": "Give me a son — and I will give him back to You for the whole of his life.",
        "must_show": "the trade spoken — Hannah's whole posture the vow: hunger and offering together, face resolute through tears at the doorway.",
        "must_not_show": "no halo; RESOLVE through the tears — the vow is strength, not desperation.",
        "scene": (
            "The trade is stated in full and she means every "
            "word of both halves: Hannah at the doorway "
            "with her tear-streaked face gone resolute — "
            "GIVE me a son — the hunger of ten festivals "
            "in the first clause — and I will give him "
            "BACK, for the whole of his life — the "
            "surrender of a lifetime in the second — a "
            "woman negotiating with heaven from her knees "
            "and somehow holding the stronger position, "
            "because she has offered the one thing God "
            "cannot refuse: everything. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r149-b11", "out": "s11-eli-the-priest-watched-her.jpeg", "seg": "n3a",
        "window": "54.95-59.83", "wide": False, "jesus": False, "ref": False,
        "locks": ["HANNAH", "ELI", "SHILOH"],
        "narration": (
            "Eli the priest watched her lips move with no sound coming out, "
            "and thought she was drunk."
        ),
        "must_show": "SCRIPTURE-EXACT: the misreading — old Eli on his seat by the doorpost squinting at the silently-praying woman, weary judgment forming; his error human, not cruel.",
        "must_not_show": "no halo; Eli's misjudgment WEARY, not malicious; her prayer continuing unbroken.",
        "scene": (
            "The professional on duty misreads the best "
            "prayer of his career: from his worn seat by "
            "the doorpost old Eli squints down at the "
            "swaying shawled figure — lips going, no sound, "
            "at this hour, at a festival — and his heavy "
            "face settles into the weary diagnosis of a "
            "man who has seen too many feast-days: wine — "
            "the priest of Shiloh watching the purest "
            "petition in Israel and reaching, tiredly, for "
            "entirely the wrong shelf. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r149-b12", "out": "s12-no-my-lord-i-am.jpeg", "seg": "w2",
        "window": "61.26-70.73", "wide": False, "jesus": False, "ref": False,
        "locks": ["HANNAH", "ELI", "SHILOH"],
        "narration": (
            "No, my lord, I am a woman of a sorrowful spirit: I have drunk "
            "neither wine nor strong drink, but have poured out my soul "
            "before the LORD."
        ),
        "must_show": "SCRIPTURE-EXACT: the correction — Hannah standing straight before Eli, unashamed, the gentle firm answer given; dignity correcting authority respectfully.",
        "must_not_show": "no halo; her correction GENTLE and level — no grovel, no heat; Eli beginning to see.",
        "scene": (
            "She corrects the priest of Israel the way she "
            "prays — with complete quiet dignity: Hannah "
            "stands straight under his accusation, the "
            "tear-tracks still bright, and gives the gentle "
            "level answer — no, my lord — not wine: SORROW — "
            "I have poured out my SOUL before the LORD — "
            "the misread woman explaining herself to "
            "authority without one degree of shame or one "
            "degree of heat, while the old eyes above her "
            "begin, slowly, to focus on what they are "
            "actually looking at. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r149-b13", "out": "s13-no-my-lord-she-told.jpeg", "seg": "n3b",
        "window": "72.63-73.83", "wide": False, "jesus": False, "ref": False,
        "locks": ["HANNAH"],
        "narration": "No, my lord, she told him.",
        "must_show": "the correction's poise — close on Hannah's level, unashamed face mid-answer; respect and self-possession in one look.",
        "must_not_show": "no halo; POISE the frame — neither defiance nor apology.",
        "scene": (
            "Four words, perfectly weighted: close on "
            "Hannah's face as she says them — no, my lord — "
            "the deep gentle eyes level on the old priest's, "
            "respect intact in the address and self-"
            "possession intact in the no — a woman "
            "sorrow-schooled into a poise that neither "
            "grovels nor bristles, correcting the highest "
            "religious authority she knows with the calm "
            "of somebody who has just been talking to a "
            "higher one. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r149-b14", "out": "s14-i-been-drinking-a-woman.jpeg", "seg": "n3b",
        "window": "73.83-79.57", "wide": False, "jesus": False, "ref": False,
        "locks": ["HANNAH", "ELI"],
        "narration": (
            "I haven't been drinking. I'm a woman with a heavy heart, and "
            "I've been pouring my soul out to the Lord."
        ),
        "must_show": "the truth landing — Eli's old face changing as he finally sees her: the weary judgment dissolving into priestly compassion.",
        "must_not_show": "no halo; the CHANGE on Eli readable — error to compassion across the old features.",
        "scene": (
            "The old man's face makes the journey from "
            "verdict to compassion in one listening: as "
            "her plain truth reaches him — a heavy heart; "
            "a soul poured out — the weary judgment "
            "dissolves off Eli's heavy features layer by "
            "layer, the dim kind eyes coming clear, the "
            "professional slump straightening into "
            "something like reverence — a priest "
            "discovering that the drunk woman at his door "
            "is the most sober soul in the sanctuary, and "
            "adjusting his whole old frame to honour it. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r149-b15", "out": "s15-she-was-not-ashamed-of.jpeg", "seg": "n3b",
        "window": "79.57-84.89", "wide": False, "jesus": False, "ref": False,
        "locks": ["HANNAH"],
        "narration": (
            "She was not ashamed of the prayer. She just wanted him to know "
            "what he was looking at."
        ),
        "must_show": "the unashamed — Hannah's open level face, tear-tracks unwiped, hiding nothing; the prayer owned in full.",
        "must_not_show": "no halo; the tear-tracks LEFT VISIBLE — nothing wiped away, nothing hidden.",
        "scene": (
            "She does not tidy her face for the "
            "explanation: the tear-tracks stay where the "
            "prayer put them, bright and unwiped in the "
            "lamplight, and she stands inside her own "
            "sorrow with the door of it open — nothing "
            "hidden, nothing performed, nothing to be "
            "ashamed of anywhere in the whole poured-out "
            "hour — just the quiet insistence that the "
            "man in the seat know exactly what he is "
            "looking at: not weakness; prayer. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r149-b16", "out": "s16-go-in-peace-and-the.jpeg", "seg": "s1",
        "window": "86.39-91.73", "wide": False, "jesus": False, "ref": False,
        "locks": ["HANNAH", "ELI", "SHILOH"],
        "narration": (
            "Go in peace: and the God of Israel grant thee thy petition "
            "that thou hast asked of him."
        ),
        "must_show": "SCRIPTURE-EXACT: the blessing — Eli's old hand raised over bowed Hannah at the doorway, the priestly blessing given in the lamp warmth.",
        "must_not_show": "no halo; the blessing WARM and formal — the office redeeming its earlier error.",
        "scene": (
            "The office recovers itself magnificently: "
            "Eli's old hand rises over the bowed shawled "
            "head — go in PEACE — the priestly blessing "
            "descending through the lamp warmth with the "
            "full weight of Shiloh behind it — and the God "
            "of Israel GRANT thee thy petition — the same "
            "voice that misjudged her now spending its "
            "whole authority on her behalf, an old man's "
            "amends made in the only currency he has "
            "worth giving. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r149-b17", "out": "s17-she-went-away-and-her.jpeg", "seg": "n4",
        "window": "93.68-96.59", "wide": False, "jesus": False, "ref": False,
        "locks": ["HANNAH", "SHILOH"],
        "narration": "She went away, and her face was no longer sad.",
        "must_show": "SCRIPTURE-EXACT: faith's receipt — Hannah walking from the doorway through the soft evening, her face visibly EASED — before any answer exists; the transformation pre-dates the gift.",
        "must_not_show": "ABSOLUTE: no child yet, no sign — the ease arrives on FAITH alone; the same woman, unburdened.",
        "scene": (
            "Nothing has changed and everything has: Hannah "
            "walks back through the soft evening court with "
            "her shawl loose and her face — the same face "
            "that carried ten years of festivals — visibly "
            "EASED, the grief-weight set down somewhere "
            "between the doorpost and the steps — no child "
            "in her arms, no promise in her hands, nothing "
            "different in the whole visible world except "
            "one thing: she has been HEARD, and is walking "
            "like a woman who knows it. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r149-b18", "out": "s18-the-lord-remembered-her-because.jpeg", "seg": "n4 + w3",
        "window": "96.59-102.18", "wide": False, "jesus": False, "ref": False,
        "locks": ["HANNAH", "SAMUEL"],
        "narration": (
            "The LORD remembered her. Because I have asked him of the LORD."
        ),
        "must_show": "SCRIPTURE-EXACT: the remembering — Hannah with newborn Samuel in her once-empty lap, wonder and tears; the name's meaning alive in her arms.",
        "must_not_show": "no halo; the LAP exact — the emptiness of b01 filled; her wonder quiet and enormous.",
        "scene": (
            "The empty lap from every festival finally has "
            "its answer in it: Hannah sits in the warm "
            "gold with the newborn gathered exactly where "
            "the ache lived all those years — the small "
            "dark-curled head in the crook of her arm, her "
            "tears falling free and different now — "
            "REMEMBERED, the scripture says, and she "
            "answers with his name: Samuel — asked of the "
            "LORD — every syllable of him a receipt. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r149-b19", "out": "s19-every-time-anyone-said-that.jpeg", "seg": "n5",
        "window": "104.08-109.66", "wide": False, "jesus": False, "ref": False,
        "locks": ["HANNAH", "SAMUEL"],
        "narration": (
            "Every time anyone said that child's name, they were saying it "
            "again: I asked, and He heard."
        ),
        "must_show": "the name as testimony — Hannah calling the toddling Samuel across the sunny courtyard, his name in her mouth, his arms up toward her; the testimony running daily.",
        "must_not_show": "no halo; the ordinariness the point — a name called at lunch, carrying a miracle.",
        "scene": (
            "The testimony gets repeated every time lunch "
            "is ready: across the sunny courtyard Hannah "
            "calls the name — Samuel! — and the dark-"
            "curled toddler turns from his game and comes "
            "at his small run, arms up — asked-of-the-LORD, "
            "shouted over washing lines, murmured at "
            "bedtime, laughed across the yard — a woman's "
            "whole answered prayer built into the one word "
            "she will say most for the rest of her life, "
            "preaching every time it is spoken. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r149-b20", "out": "s20-forget-me.jpeg", "seg": "n2",
        "window": "40.92-42.32", "wide": False, "jesus": False, "ref": False,
        "locks": ["HANNAH", "SHILOH"],
        "narration": "Don't forget me.",
        "must_show": "the plea's last word — Hannah's brow resting against the doorpost wood, hand flat on it; the smallest, nearest posture of the whole prayer.",
        "must_not_show": "no halo; the brow ON the post — intimacy with the threshold; tears on the wood.",
        "scene": (
            "The prayer ends with her forehead on the "
            "doorframe of heaven: Hannah's brow comes to "
            "rest against the worn lamplit post, one hand "
            "flat on the old wood beside her face — don't "
            "forget me — the last three words pressed "
            "directly into the timber of the LORD's house "
            "like a note slipped under a door — as close "
            "to the listening dark as a body can lean, "
            "asking the one thing forgetting would kill. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r149-b21", "out": "s21-therefore-also-i-have-lent.jpeg", "seg": "w4",
        "window": "111.15-117.61", "wide": False, "jesus": False, "ref": False,
        "locks": ["HANNAH", "ELI", "SAMUEL", "SHILOH"],
        "narration": (
            "Therefore also I have lent him to the LORD; as long as he "
            "liveth he shall be lent to the LORD."
        ),
        "must_show": "SCRIPTURE-EXACT: the presenting — Hannah's hands on small Samuel's shoulders before old Eli at the doorway, the vow being paid in person; the boy small and brave.",
        "must_not_show": "no halo; her hands STEADY on the small shoulders — the costliest gesture performed with love.",
        "scene": (
            "The vow comes due and she pays it standing "
            "up: at the same doorway where she prayed him "
            "into being, Hannah's hands rest steady on "
            "small Samuel's shoulders, presenting him to "
            "old Eli — LENT to the LORD, she says over the "
            "dark curls, as long as he liveth — the boy "
            "small and brave in his little olive tunic "
            "under his mother's steady grip, the priest's "
            "dim eyes wet — a woman handing back the "
            "answer to her own prayer, whole, at the door "
            "where she asked it. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r149-b22", "out": "s22-she-kept-her-word-when.jpeg", "seg": "n6",
        "window": "119.50-125.17", "wide": False, "jesus": False, "ref": False,
        "locks": ["HANNAH", "ELI", "SAMUEL", "SHILOH"],
        "narration": (
            "She kept her word. When he was weaned, she brought him to the "
            "house of the LORD and left him there to serve."
        ),
        "must_show": "the keeping — Hannah walking away DOWN the morning road, small Samuel standing at the tabernacle door with Eli's hand on his shoulder, both watching her go; broken and at peace in her carriage.",
        "must_not_show": "no halo; DIRECTION exact — she away down the road, the boy at the door; her bearing both grieved and at peace.",
        "scene": (
            "Keeping her word looks like the hardest walk "
            "of her life, taken steadily: down the clear "
            "morning road from Shiloh Hannah goes alone, "
            "back straight, steps even, the tears allowed "
            "and the pace unbroken — while behind her at "
            "the sanctuary door the small figure of "
            "Samuel stands under Eli's gentle old hand, "
            "watching his mother go — a vow paid in full "
            "at the door of the house of the LORD, by a "
            "woman walking home with an empty lap and a "
            "kept promise, at peace in the middle of the "
            "breaking. Every figure has two arms, two "
            "hands and one head."
        ),
    },
]


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# Each token's plate is attached as a PLACE LOCK image to every beat whose
# `locks` name it. Plates live in PLACE-REF/ (gitignored art); PLACE-WIRING.json
# is the committed record — `v2_stash.py --wire <this build>` rebuilds the
# plates on any machine that has the source builds' stills.
PLACE_REFS = {
}
# === end PLACE-PLATES ===
