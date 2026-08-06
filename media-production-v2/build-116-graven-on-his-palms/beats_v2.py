#!/usr/bin/env python3
"""V2 beat map — row 116, build-116-graven-on-his-palms (Isaiah 49:14-16).

COVERAGE: 21 pictures over 121.3 s = 5.8 s/picture (matches the library density).

SCRIPTURE FACTS (Isaiah 49 KJV):
  v14   "But ZION SAID, The LORD hath forsaken me, and my Lord hath
        FORGOTTEN me." — the fear said out loud; Zion personified as
        a woman who feels left behind.
  v15   "CAN A WOMAN FORGET HER SUCKING CHILD...? yea, they may
        forget, YET WILL I NOT FORGET THEE." — the strongest human
        love invoked, and outdone.
  v16   "Behold, I have GRAVEN THEE UPON THE PALMS OF MY HANDS; thy
        WALLS are continually before me." — engraved: cut deep,
        permanent, not a note that fades.

GOD RENDERING (CONTENT-CARE law): God is NEVER embodied — his palms
are NEVER painted. The graven image is carried by metaphor: an
ENGRAVER cutting a name deep into enduring bronze (permanence),
contrasted with a fading ink note on a human palm (the note you
might lose). The v15 love is a real mother-and-newborn vignette.
Zion is personified as the WOMAN who feared she was forgotten.

TIME OF DAY ARC (intentional): the loneliness beats at blue dusk; the
mother and engraver vignettes in warm lamplight; the walls beat at
first light; the close in full warm morning. Correct story lighting.

CHANGING CONDITION (kept OUT of the locks): the woman — forsaken-
feeling, then hearing, then held; the engraving — begun, cut deep,
finished; the light — dusk to morning.
"""

# LOCKS: one entry per recurring person and per setting. Clothing colours
# stated POSITIVELY and dark — only Jesus wears cream (not in this row).
LOCKS = {
    "WOMAN": (
        "WOMAN LOCK: the woman who felt forgotten is the same in "
        "every shot — about fifty, a worn gentle face with deep "
        "tired eyes, greying dark hair under a DEEP SLATE-BLUE "
        "shawl, a plain DEEP SLATE-BLUE dress (never cream, never "
        "white); her loneliness dignified, her comfort earned."
    ),
    "MOTHER": (
        "MOTHER LOCK: the vignette mother is the same in every such "
        "shot — young, dark-haired, in a DARK MADDER-RED dress "
        "(never cream, never white), with her days-old newborn "
        "swaddled in soft grey cloth; tenderness absolute, modesty "
        "complete."
    ),
    "ENGRAVER": (
        "ENGRAVER LOCK: the craftsman is the same in every such "
        "shot — about sixty, strong forearms, half-spectacled "
        "concentration, in a DARK LEATHER apron over a CHARCOAL "
        "tunic; his bench holds a heavy BRONZE PLATE, gravers and "
        "an oil lamp. The same bench and plate throughout."
    ),
    "CITY": (
        "CITY LOCK: the woman's city — pale stone walls and "
        "rooftops on a hill, her small house door opening onto a "
        "walled lane. The same walls and lane throughout."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r116-b01", "out": "s01-there-is-a-particular-loneliness.jpeg", "seg": "n1",
        "window": "0.28-3.57", "wide": False, "jesus": False, "ref": False,
        "locks": ["CITY", "WOMAN"],
        "narration": (
            "There is a particular loneliness that comes from feeling "
            "forgotten."
        ),
        "must_show": "the particular loneliness — blue dusk in the walled lane: the woman alone in her doorway as lit windows and passing families move beyond her; unincluded, unnoticed.",
        "must_not_show": "no halo; the loneliness SPECIFIC — life happening around her, none of it turning her way.",
        "scene": (
            "Blue dusk finds the "
            "particular kind: the woman "
            "alone in her doorway while "
            "the lane lives on past "
            "her — windows warming one "
            "by one down the walled "
            "street, a family laughing "
            "home from the well, "
            "neighbors calling "
            "good-nights that are not "
            "for her — nothing cruel "
            "anywhere, no enemy, just "
            "the specific ache of "
            "standing in a doorway "
            "while the world's warmth "
            "moves past without once "
            "turning its head. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r116-b02", "out": "s02-slipped-from-mind-as-if.jpeg", "seg": "n1",
        "window": "5.98-10.91", "wide": False, "jesus": False, "ref": False,
        "locks": ["WOMAN"],
        "narration": (
            "Slipped from someone's mind, as if you never really mattered "
            "enough to be remembered."
        ),
        "must_show": "the slipped-from-mind — close on the woman's face in the dusk light: the wound of unimportance; eyes that have stopped expecting to be thought of.",
        "must_not_show": "no halo; NO self-pity theatrics — the quiet settled ache of long unimportance.",
        "scene": (
            "Close on the quietest wound "
            "there is: the worn gentle "
            "face in the last blue "
            "light, and in the deep "
            "tired eyes not the sharp "
            "grief of loss but the "
            "settled ache of "
            "unimportance — the look "
            "of someone who has "
            "checked the door and the "
            "road and the years and "
            "slowly concluded that no "
            "mind anywhere is holding "
            "her in it — slipped, not "
            "thrown; faded, not "
            "banished; which somehow "
            "hurts longer. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r116-b03", "out": "s03-but-zion-said-the-lord.jpeg", "seg": "s14",
        "window": "11.48-15.94", "wide": False, "jesus": False, "ref": False,
        "locks": ["WOMAN", "CITY"],
        "narration": (
            "But Zion said, The LORD hath forsaken me, and my Lord hath "
            "forgotten me."
        ),
        "must_show": "SCRIPTURE-EXACT: the fear said aloud — the woman at her dark window speaking it out into the night: FORSAKEN, FORGOTTEN; the accusation as prayer.",
        "must_not_show": "no figure of God; the saying HONEST — a believer's worst thought, finally voiced.",
        "scene": (
            "At the dark window she "
            "finally says it out loud: "
            "THE LORD HATH FORSAKEN "
            "ME — the words leaving "
            "her into the night air "
            "half accusation, half "
            "prayer — AND MY LORD "
            "HATH FORGOTTEN ME — a "
            "believer's most forbidden "
            "sentence spoken at last "
            "to the One it is about, "
            "which is, though she "
            "cannot feel it yet, "
            "still a way of talking "
            "to him, still a thread, "
            "still held. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r116-b04", "out": "s04-that-is-exactly-how-people.jpeg", "seg": "n2",
        "window": "17.50-26.18", "wide": True, "jesus": False, "ref": False,
        "locks": ["CITY"],
        "narration": (
            "That is exactly how God's people felt, and they said it out "
            "loud — the Lord has walked away from me, and my God has "
            "forgotten I exist."
        ),
        "must_show": "the feeling city-wide — the dusk city's lanes: other solitary figures at other windows and doorways, each carrying the same unspoken sentence; a shared secret loneliness.",
        "must_not_show": "no figure of God; the multiplicity QUIET — separate lonelinesses, not a crowd scene.",
        "scene": (
            "The dusk city holds, the camera high along a lane "
            "so every solitary figure faces away from the lens "
            "into a doorway "
            "or window, more of "
            "the same sentence than "
            "anyone admits: here an "
            "old man alone at his "
            "lamplit table with two "
            "cups and one drinker; "
            "there a widow's silhouette "
            "unmoving at her window; "
            "further, a young man on "
            "a rooftop staring at "
            "stars that never write "
            "back — a whole city of "
            "separate rooms quietly "
            "concluding the same "
            "thing: walked away from; "
            "forgotten I exist — each "
            "one certain they are the "
            "only one. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r116-b05", "out": "s05-and-answer-to-that-fear.jpeg", "seg": "n2",
        "window": "26.18-30.59", "wide": False, "jesus": False, "ref": False,
        "locks": ["WOMAN"],
        "narration": (
            "And God's answer to that fear is one of the most tender things "
            "he ever said."
        ),
        "must_show": "the answer approaching — the woman's night room beginning to warm: dawn's first faint gold reaching her window; tenderness arriving as light.",
        "must_not_show": "no figure of God; the warming SUBTLE — the answer's tone before its words.",
        "scene": (
            "Into the room where the "
            "worst sentence was spoken, "
            "the answer's tone arrives "
            "first: the window's black "
            "going grey, then faintly, "
            "unmistakably gold at its "
            "lower edge — dawn finding "
            "the woman still at her "
            "sill — and something in "
            "the light's gentleness "
            "already contradicting the "
            "accusation before one "
            "word of the reply is "
            "spoken: this is not how "
            "light behaves in a house "
            "that has been forgotten. "
            "Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r116-b06", "out": "s06-just-overlooked.jpeg", "seg": "n1",
        "window": "4.83-5.98", "wide": False, "jesus": False, "ref": False,
        "locks": ["WOMAN", "CITY"],
        "narration": "Just overlooked.",
        "must_show": "the overlooking — the lane's traffic passing the woman's doorway, every gaze sliding past her; invisibility in one image.",
        "must_not_show": "no halo; NO malice in any passer — the sliding-past unthinking, which is the wound.",
        "scene": (
            "One image of the word: the "
            "lane's evening traffic "
            "flowing past her doorway — "
            "a merchant's eyes on his "
            "ledger, two friends deep "
            "in each other, a mother "
            "counting her children — "
            "every gaze sliding past "
            "the slate-blue figure in "
            "the doorway without "
            "snagging, without malice, "
            "without ever once "
            "landing — overlooked: not "
            "wounded by anything "
            "anyone did, only by "
            "everything everyone "
            "didn't. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r116-b07", "out": "s07-he-points-to-the-strongest.jpeg", "seg": "n3",
        "window": "31.19-42.52", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOTHER"],
        "narration": (
            "He points to the strongest, most instinctive love a human "
            "being knows — a mother with her newborn, unable to look away, "
            "unable to forget the child at her breast."
        ),
        "must_show": "the strongest love — the lamplit vignette: the young mother nursing her swaddled newborn, gaze locked down on the small face, the unable-to-look-away absolute; modesty complete.",
        "must_not_show": "modesty total — swaddling and shawl arranged; the LOCKED GAZE the subject.",
        "scene": (
            "The argument's exhibit is "
            "the oldest scene in the "
            "world: lamplight, a young "
            "mother, and the days-old "
            "child gathered to her "
            "beneath the drape of her "
            "shawl — and the thing the "
            "verse points at is her "
            "GAZE: locked downward on "
            "the small sleeping face, "
            "unable to leave it, "
            "returning every time it "
            "is called away like "
            "water finding its level — "
            "the most instinctive love "
            "a human frame can hold, "
            "burning quietly at full "
            "strength. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r116-b08", "out": "s08-not-hated.jpeg", "seg": "n1",
        "window": "3.57-4.83", "wide": False, "jesus": False, "ref": False,
        "locks": ["WOMAN"],
        "narration": "Not hated.",
        "must_show": "the distinction — the woman's face free of any persecution-mark: nobody's enemy, nobody's target; the ache precisely NOT hatred's.",
        "must_not_show": "no halo; no drama of enmity — the gentler, lonelier diagnosis.",
        "scene": (
            "Close on what the ache is "
            "NOT: no enemy has marked "
            "this face, no slander "
            "bruised it, no door has "
            "ever been slammed on it "
            "in anger — nobody hates "
            "her; that would at least "
            "mean being thought of — "
            "the worn features carry "
            "the gentler, lonelier "
            "diagnosis instead: not "
            "hated, not fought, not "
            "even wronged — just "
            "unthought-of, which "
            "leaves no one to forgive "
            "and nothing to fix. "
            "Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r116-b09", "out": "s09-can-a-woman-forget-her.jpeg", "seg": "jv15",
        "window": "43.09-50.09", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOTHER"],
        "narration": (
            "Can a woman forget her sucking child, that she should not have "
            "compassion on the son of her womb?"
        ),
        "must_show": "SCRIPTURE-EXACT: the question over the vignette — the nursing mother's bowed tenderness at full frame; the question's absurdity answered by the image itself.",
        "must_not_show": "no figure of God; modesty complete; the impossibility VISIBLE — this love does not forget.",
        "scene": (
            "The question hangs over "
            "the lamplit scene and "
            "answers itself: CAN A "
            "WOMAN FORGET — the young "
            "mother bowed over the "
            "swaddled weight at her "
            "breast, one fingertip "
            "tracing the tiny sleeping "
            "brow for the hundredth "
            "time tonight — forget? "
            "She cannot finish a "
            "sentence to a neighbor "
            "without her eyes dropping "
            "back to him; she wakes "
            "before he cries; her "
            "whole body is a memory "
            "of him — the absurdity "
            "of the question being "
            "the entire point of "
            "asking it. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r116-b10", "out": "s10-yea-they-may-forget-yet.jpeg", "seg": "jv15",
        "window": "50.09-56.23", "wide": False, "jesus": False, "ref": False,
        "locks": ["WOMAN"],
        "narration": "yea, they may forget, yet will I not forget thee.",
        "must_show": "SCRIPTURE-EXACT: the outdoing — the forgotten woman in the first gold light, the words settling over her: even that love outdone; YET WILL I NOT.",
        "must_not_show": "ABSOLUTE: no figure of God — the promise carried by light and her receiving face.",
        "scene": (
            "And then the argument goes "
            "past its own exhibit: YEA, "
            "THEY MAY FORGET — even "
            "that love, the strongest "
            "the species owns, has "
            "failed somewhere, some "
            "night — YET WILL I NOT "
            "FORGET THEE — and the "
            "words settle over the "
            "slate-blue woman in her "
            "first gold light like a "
            "verdict overturning "
            "years: measured against "
            "a nursing mother's "
            "memory, and promised "
            "stronger — to her, the "
            "overlooked one, by "
            "name. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r116-b11", "out": "s11-even-if-a-mother-somehow.jpeg", "seg": "n4",
        "window": "57.73-61.37", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOTHER", "WOMAN"],
        "narration": "Even if a mother somehow could forget — I never will.",
        "must_show": "the even-if — the two women's images held in one frame's diptych feeling: the mother's locked gaze near, the once-forgotten woman lifting her face; the promise bridging them.",
        "must_not_show": "no figure of God; the bridge COMPOSITIONAL — one love pointing past itself to a greater.",
        "scene": (
            "One frame holds the "
            "comparison the promise "
            "builds on: near, the "
            "young mother's bowed "
            "unbreakable attention on "
            "her child — and across "
            "the frame's breadth, in "
            "her own doorway's new "
            "gold, the older woman "
            "lifting her face like "
            "someone hearing her name "
            "from far off — the "
            "strongest human love "
            "standing as merely the "
            "FLOOR of what is being "
            "promised: even if this "
            "failed — I never will. "
            "Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r116-b12", "out": "s12-he-does-not-just-keep.jpeg", "seg": "n4",
        "window": "64.91-67.08", "wide": False, "jesus": False, "ref": False,
        "locks": ["ENGRAVER"],
        "narration": "He does not just keep you in mind.",
        "must_show": "beyond remembering — the engraver's bench in lamplight: the heavy bronze plate and gravers laid ready; something more permanent than memory about to begin.",
        "must_not_show": "no figure of God; the bench WAITING — tools and metal, intent visible.",
        "scene": (
            "The metaphor sets its "
            "bench: in the workshop's "
            "lamplight the heavy "
            "bronze plate lies waiting "
            "— thick as a door hinge, "
            "polished dull gold — and "
            "beside it the row of "
            "gravers, honed and "
            "ordered by hand — the "
            "tools of the one kind of "
            "keeping that outlasts "
            "keeping-in-mind: not the "
            "faculty of memory, which "
            "tires, but the act of "
            "engraving, which does "
            "not — something permanent, "
            "about to be begun. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r116-b13", "out": "s13-and-then-he-says-something.jpeg", "seg": "n4",
        "window": "61.37-64.91", "wide": False, "jesus": False, "ref": False,
        "locks": ["WOMAN"],
        "narration": "And then he says something almost too intimate to imagine.",
        "must_show": "the almost-too-intimate — the woman's face braced-then-softening as the next words approach; intimacy's approach visible.",
        "must_not_show": "no figure of God; the register HUSHED — the frame leaning toward what comes next.",
        "scene": (
            "Close on a face preparing "
            "for something it cannot "
            "prepare for: the woman in "
            "the strengthening gold, "
            "the promise of "
            "not-forgetting still "
            "settling — and now "
            "something further coming, "
            "felt before heard, the "
            "way you feel a speaker "
            "lower their voice to say "
            "the realest thing — her "
            "breath stilling, the "
            "worn hands going quiet "
            "in her lap — the whole "
            "frame hushed and leaning "
            "toward an intimacy "
            "almost too great to "
            "receive. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r116-b14", "out": "s14-behold-i-have-graven-thee.jpeg", "seg": "jv16",
        "window": "71.57-78.91", "wide": False, "jesus": False, "ref": False,
        "locks": ["ENGRAVER"],
        "narration": (
            "Behold, I have graven thee upon the palms of my hands; thy "
            "walls are continually before me."
        ),
        "must_show": "SCRIPTURE-EXACT rendered per law: the engraving — the craftsman's graver cutting a NAME deep into the bronze, bright metal curling from the stroke; permanence mid-act; GOD'S HANDS NEVER SHOWN.",
        "must_not_show": "ABSOLUTE: no divine hands or figure — the human engraver's work carries the metaphor whole.",
        "scene": (
            "The verse happens at the "
            "bench: the old craftsman "
            "bowed in his lamplight, "
            "graver set to the bronze, "
            "and the stroke going in "
            "DEEP — bright metal "
            "curling up from the "
            "cutting edge as a name "
            "sinks letter by letter "
            "into a surface that will "
            "outlast the hand, the "
            "bench, the city — not "
            "ink, not memory, not "
            "wax: GRAVEN — cut into "
            "the substance itself, "
            "where nothing short of "
            "destroying the hand "
            "could ever get it out "
            "again. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r116-b15", "out": "s15-graven-engraved-cut-in-deep.jpeg", "seg": "n5",
        "window": "80.47-85.22", "wide": False, "jesus": False, "ref": False,
        "locks": ["ENGRAVER"],
        "narration": (
            "Graven — engraved, cut in deep, permanent. Not a note he might "
            "lose."
        ),
        "must_show": "the contrast — the deep-cut bronze name beside a fading smudged ink note on scrap: permanence versus the note you might lose, in one frame.",
        "must_not_show": "no divine hands; the CONTRAST explicit — cut depth against smudge.",
        "scene": (
            "The bench states the "
            "difference side by side: "
            "in the lamplight, the "
            "bronze with its name cut "
            "deep — shadows pooling "
            "in the strokes, letters "
            "you could read with your "
            "fingertips in the dark — "
            "and beside it, curling "
            "at the edges, a scrap "
            "note in ink gone brown "
            "and smudged, half a word "
            "already rubbed to "
            "ghost — the two ways of "
            "keeping a name: the kind "
            "that fades in a season, "
            "and the kind you would "
            "have to destroy the "
            "metal to lose. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r116-b16", "out": "s16-you-are-written-into-the.jpeg", "seg": "n5",
        "window": "85.22-93.05", "wide": True, "jesus": False, "ref": False,
        "locks": ["CITY"],
        "narration": (
            "You are written into the very hands of God, and everything "
            "about you is always right there in front of him. He could not "
            "forget you if he tried."
        ),
        "must_show": "SCRIPTURE-EXACT: thy walls continually before me — the woman's whole city at first light, held complete in the frame: every wall and rooftop of her life, continually seen.",
        "must_not_show": "ABSOLUTE: no divine figure or hands — the CONTINUAL SEEING carried by the city lying whole and lit in view.",
        "scene": (
            "The frame does, the camera on the wall's height "
            "taking the waking city from the side, what the "
            "promise says is always "
            "being done: holds her "
            "whole life in view at "
            "once — the pale walls of "
            "her city in first light, "
            "every rooftop and lane "
            "and stair of it, her own "
            "small doorway findable "
            "among the rest — nothing "
            "cropped, nothing outside "
            "the seeing — THY WALLS "
            "CONTINUALLY BEFORE ME — "
            "a life kept whole in an "
            "unblinking view, the way "
            "an engraved palm keeps "
            "its name: always open, "
            "always there. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r116-b17", "out": "s17-and-that-changes-the-person.jpeg", "seg": "n6",
        "window": "93.65-97.08", "wide": False, "jesus": False, "ref": False,
        "locks": ["WOMAN"],
        "narration": "And that changes the person who thought she had been left behind.",
        "must_show": "the change — the woman's face remade in the morning light: the settled ache dissolving, worth returning; a remembered person emerging.",
        "must_not_show": "no halo; the change GRADUAL and real — years of ache releasing, not an instant mask-swap.",
        "scene": (
            "Close on a face being "
            "remembered back to life: "
            "the deep tired eyes in "
            "the morning gold, and "
            "the years-old ache in "
            "them beginning to "
            "dissolve — not snapped "
            "away but releasing, the "
            "way frost releases from "
            "a window as the sun "
            "finds it — the settled "
            "unimportance losing its "
            "grip line by line as a "
            "different fact takes the "
            "features over: graven; "
            "held; never once out of "
            "view — a left-behind "
            "woman discovering she "
            "was carried the whole "
            "way. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r116-b18", "out": "s18-the-same-god-she-feared.jpeg", "seg": "n6",
        "window": "97.08-106.38", "wide": False, "jesus": False, "ref": False,
        "locks": ["WOMAN", "CITY"],
        "narration": (
            "The same God she feared had forgotten her was carrying her the "
            "whole time — her name, her walls, her whole life, held in his "
            "hands."
        ),
        "must_show": "the carried-all-along — the woman stepping out of her doorway into the full morning, the lit city around her; her walk changed from the opening beat's stillness.",
        "must_not_show": "ABSOLUTE: no divine figure or hands — the carrying shown as her changed bearing inside her held city.",
        "scene": (
            "The doorway that held her "
            "loneliness now launches "
            "her: the woman stepping "
            "out into the full "
            "morning, slate-blue shawl "
            "bright in the sun, her "
            "walk carrying something "
            "it did not have at dusk — "
            "and around her the whole "
            "held city going about "
            "its lit and ordinary "
            "business — the same "
            "lanes, the same walls, "
            "all of it, and her small "
            "life among it, revealed "
            "as having been carried "
            "entire the whole time "
            "she thought she was "
            "dropped. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r116-b19", "out": "s19-he-has-carved-you-into.jpeg", "seg": "n4",
        "window": "67.08-70.97", "wide": False, "jesus": False, "ref": False,
        "locks": ["ENGRAVER"],
        "narration": (
            "He has carved you into his own hands, where he cannot help but "
            "see you."
        ),
        "must_show": "the cannot-help-but-see — the finished engraving close in the lamplight: the deep-cut name catching light in every stroke; unmissable by design.",
        "must_not_show": "ABSOLUTE: no divine hands — the bronze name alone, filling the frame.",
        "scene": (
            "Close on the finished "
            "cutting: the name deep in "
            "the bronze, every stroke "
            "holding its own line of "
            "lamplight, shadows "
            "pooled rich in the "
            "letterforms — placed "
            "where the metal is "
            "handled most, worn "
            "brightest, seen soonest — "
            "a name positioned so "
            "that every use of the "
            "hands presents it, every "
            "opening of the palm "
            "reads it — remembering "
            "engineered into the "
            "structure itself, where "
            "forgetting has nowhere "
            "left to happen. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r116-b20", "out": "s20-so-if-you-have-ever.jpeg", "seg": "n7 + n7b",
        "window": "106.97-115.44", "wide": False, "jesus": False, "ref": False,
        "locks": ["CITY"],
        "narration": (
            "So if you have ever felt like the one who gets forgotten — the "
            "one nobody keeps in mind — hear this slowly. You are not out "
            "of sight."
        ),
        "must_show": "the address widening — the morning city with its many windows and doorways open to the light: every once-lonely room from b04 now lit; the you reaching everyone overlooked.",
        "must_not_show": "no divine figure; the ECHO of b04 deliberate — same rooms, new light.",
        "scene": (
            "The morning re-answers "
            "every dusk room from "
            "before: the old man's "
            "window flung open with "
            "his lamp needless in the "
            "sun, the widow's sill "
            "warm and occupied by "
            "morning doves, the "
            "rooftop where the young "
            "man stared at silent "
            "stars now flooded with "
            "answering gold — the "
            "whole city of separate "
            "lonelinesses relit room "
            "by room — NOT OUT OF "
            "SIGHT, says the light, "
            "going in every window "
            "at once. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r116-b21", "out": "s21-you-are-not-out-of.jpeg", "seg": "n7b",
        "window": "115.44-120.96", "wide": False, "jesus": False, "ref": False,
        "locks": ["ENGRAVER"],
        "narration": (
            "You are not out of mind. You are graven on the hands of God, "
            "and he has never once looked away."
        ),
        "must_show": "the closing image — the engraved bronze name in full warm light, held up angled toward the viewer; the permanence addressed outward; the row's last word cut in metal.",
        "must_not_show": "ABSOLUTE: no divine hands or figure — the engraved name, offered to whoever is looking.",
        "scene": (
            "The closing frame turns "
            "the engraving toward "
            "whoever is watching: the "
            "bronze lifted into the "
            "full warm light, angled "
            "outward, the deep-cut "
            "name blazing its lines "
            "at the viewer — cut past "
            "fading, past losing, "
            "past every night anyone "
            "ever concluded they had "
            "slipped some mind — "
            "GRAVEN, where the seeing "
            "never stops and the "
            "looking-away has never "
            "once happened — your "
            "name, reader, in the "
            "metal, held up to the "
            "light. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
]


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# Each token's plate is attached as a PLACE LOCK image to every beat whose
# `locks` name it. Plates live in PLACE-REF/ (gitignored art); PLACE-WIRING.json
# is the committed record — `v2_stash.py --wire <this build>` rebuilds the
# plates on any machine that has the source builds' stills.
PLACE_REFS = {
    "CITY": "PLACE-REF/city.jpeg",  # build-116-graven-on-his-palms s04-that-is-exactly-how-people (manual)
}
# === end PLACE-PLATES ===

# Per-story face sheets, generated by v2_story_cast.py. Identity is
# carried by IMAGE, not by wording — text locks let the elder son come
# back as three different men in row 2 (Cameron, 2026-07-30).
REFS = {
    "WOMAN": "CAST-REF-V2/woman.jpeg",
}
