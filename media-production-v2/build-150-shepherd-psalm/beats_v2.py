#!/usr/bin/env python3
"""V2 beat map — row 150, build-150-shepherd-psalm (Psalm 23).

COVERAGE: 21 pictures over 122.5 s = 5.8 s/picture (matches the library density).

SCRIPTURE FACTS (Psalm 23 KJV):
  v1 "The LORD is my shepherd; I SHALL NOT WANT."
  v2 "He maketh me to LIE DOWN in green pastures: he leadeth me
     beside the STILL waters."
  v3 "He RESTORETH my soul: he leadeth me in the paths of
     righteousness FOR HIS NAME'S SAKE."
  v4 "Yea, though I walk through the VALLEY OF THE SHADOW OF DEATH,
     I will fear no evil: for THOU art with me; thy ROD and thy
     STAFF they comfort me." — the He→THOU turn happens in the dark.
  v5 "Thou preparest a TABLE before me in the presence of mine
     enemies: thou ANOINTEST my head with oil; my CUP RUNNETH OVER."
  v6 "Surely goodness and mercy shall FOLLOW me... and I will DWELL
     in the house of the LORD for ever."
  Author: DAVID — the shepherd-king writing about being shepherded.

RENDERING LAWS:
  - DAVID HAS TWO AGES, one face: the KING (~50, writing with harp
    near) and the remembered YOUNG SHEPHERD (~17, in the psalm's
    field frames) — same features, aged; face-board the pair.
  - THE VALLEY (b11/b13) is a REAL dark gorge — deep shadow, real
    dark, light at its far end; NO death imagery, no bones, no
    spectres, ever. The comfort is rod, staff, and nearness.
  - THE ENEMIES (b14/b15) are FAR RIDGE SILHOUETTES only — vague,
    distant, unable to approach; never close, never armed in
    detail; the table's calm is the picture.
  - The He→THOU grammar turn (b12/b13) is the row's discovery:
    nearness increases IN the dark — the sheep pressing close to
    the shepherd's legs in the gorge.
  - Goodness-and-mercy PURSUING (b18/b19) is rendered as the
    shepherd walking BEHIND the homeward flock, striding — the
    following made of the shepherd himself.
  - All light physical; the psalm's scroll script indistinct.

TIME OF DAY ARC (intentional): the king's writing frames at warm
lamplit evening; the pasture frames in soft green morning; the
valley at TRUE deep shadow with far daylight (deliberate); the
table at golden late afternoon; the homecoming at warm dusk; the
close at lamplit night, at rest.

CHANGING CONDITIONS (kept OUT of the locks): David's age per frame
(king writing / young shepherd remembered); the flock — grazing,
lying down, led, through the gorge, home.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Only Jesus wears cream (not in this row).
# NARRATIVE REBUILD (2026-08-30, Cameron complaint): narration re-written and
# re-voiced (n0/n1a/n1b/n2) — track rebuilt from the V1 mp3s.
AUDIO_FROM_V1_SEGMENTS = True

LOCKS = {
    "DAVID": (
        "DAVID LOCK: David is the same face at two ages — as KING "
        "(~50): a strong lined face, russet-grey beard, in a DEEP "
        "ROYAL-BLUE robe with a dark mantle (never cream, never "
        "white), the harp near; as the remembered YOUNG SHEPHERD "
        "(~17): the same features young — ruddy, bright-eyed, in a "
        "short DARK RUST tunic with a sling at his belt and a "
        "shepherd's staff. One face, two ages, per beat."
    ),
    "PASTURE": (
        "PASTURE LOCK: the green pastures — deep spring-green "
        "meadows in a sheltered valley, a slow stream widening to "
        "GLASS-STILL pools, willows at the banks; cream-wool sheep. "
        "The same valley and pools throughout."
    ),
    "GORGE": (
        "GORGE LOCK: the valley of shadow — a narrow deep-cut gorge "
        "of dark rock, the path threading its floor in true deep "
        "shade, a bright doorway of daylight at its FAR end. The "
        "same gorge and far light throughout."
    ),
    "TABLE": (
        "TABLE LOCK: the prepared table — a sturdy wooden table "
        "spread with a woven cloth, flat bread, a horn of oil and "
        "one generous cup, set in open golden hill-country. The "
        "same table and setting throughout."
    ),
}

REF = True

BEATS = [
    {'id': 'v2-r150-b01',
     'out': 's22-david-had-many-jobs.jpeg',
     'seg': 'n0',
     'window': '0.400-7.400',
     'wide': False,
     'jesus': False,
     'ref': False,
     'locks': [],
     'narration': 'Before he was a king, David had many jobs. Court musician. Soldier. Ruler of a '
                  'nation.',
     'must_show': 'the grown KING from behind and beside — crown and rich robe, seated before a '
                  "lamplit court, his old shepherd's harp resting against the throne; a full "
                  "life's jobs in one frame.",
     'must_not_show': 'no halo; his FACE not the focus (three-quarter from behind — the boy '
                      'version of him carries this video); no cream; no modern object; realistic '
                      'photograph, never painted or illustrated.',
     'scene': 'From behind and beside the throne: a grown king in a deep-red royal robe and '
              'simple gold circlet, seen three-quarters from the back so his face stays soft, a '
              'great lamplit stone hall falling away before him — and leaning against the throne '
              'within reach of his hand, a worn wooden HARP, the one thing in the frame older '
              'than the kingship. CAMERA low behind his shoulder. Warm real lamplight, real '
              'fabric weave; nobody else near.'},
    {'id': 'v2-r150-b02',
     'out': 's23-his-first-job.jpeg',
     'seg': 'n0',
     'window': '7.400-14.200',
     'wide': False,
     'jesus': False,
     'ref': False,
     'locks': ['DAVID', 'PASTURE'],
     'narration': 'But when he reached for a way to describe God, he went back to his first job, '
                  "the one he had as a boy watching his father's sheep.",
     'must_show': 'the BOY shepherd David of this video — the same young face as the reference — '
                  "out on the Bethlehem hills with his father's sheep around him, staff in hand; "
                  'the first job.',
     'must_not_show': 'no halo; the SAME boy as every other frame (reference attached); no crown, '
                      'no armour; no cream; realistic photograph.',
     'scene': 'Golden hill-country morning: the young shepherd DAVID — his face, hair and build '
              'EXACTLY as the attached reference — stands mid-slope with his staff, a dozen sheep '
              'grazing loosely around his knees, the Bethlehem hills rolling behind. CAMERA a '
              'level medium from his front-left, his young face open. Simple earth-brown wool, '
              'bare hills, real morning light. NOT a close-up and NOT a from-behind wide.'},
    {'id': 'v2-r150-b03',
     'out': 's04-it-starts-like-this.jpeg',
     'seg': 'n0',
     'window': '14.200-20.596',
     'wide': False,
     'jesus': False,
     'ref': False,
     'locks': ['DAVID'],
     'narration': 'It starts like this:',
     'must_show': "the first line — close on the king's pen touching the scroll's first line in "
                  'lamplight; the song beginning in ink. Script indistinct.',
     'must_not_show': "no halo; NO readable text — the pen's touch and fresh ink line only.",
     'scene': 'The most-loved poem in the world starts as one wet line of ink: close on the reed '
              "pen's tip touching down at the scroll's head in the lamp's warm ring — the first "
              "stroke drawn steady, the line still shining wet, the king's scarred knuckles quiet "
              'around the reed — three thousand years of deathbeds and cradles and green Sunday '
              'mornings, all waiting downstream of the sentence this hand is beginning. Every '
              'figure has two arms, two hands and one head.'},
    {'id': 'v2-r150-b04',
     'out': 's02-the-lord-is-my-shepherd.jpeg',
     'seg': 's1',
     'window': '20.596-25.094',
     'wide': False,
     'jesus': False,
     'ref': False,
     'locks': ['DAVID', 'PASTURE'],
     'narration': 'The LORD is my shepherd; I shall not want.',
     'must_show': 'SCRIPTURE-EXACT: the opening line lived — YOUNG David the shepherd among his '
                  'contented flock in the green valley, at ease, wanting nothing; the singer '
                  'inside his own metaphor.',
     'must_not_show': "no halo; YOUNG David (same face, ~17); the flock's contentment total.",
     'scene': "The song's first line is a memory of mornings like this: young David — the same "
              'face, ruddy and seventeen — stands easy among his grazing flock in the deep green '
              'valley, staff loose across his shoulders, the sheep spread unbothered around him — '
              'a boy who is, this morning, everything to these animals that the LORD will be to '
              'him: provider, protector, the reason nothing on this hillside wants for anything. '
              'Every figure has two arms, two hands and one head.'},
    {'id': 'v2-r150-b05',
     'out': 's03-david-begins-with-trust-not.jpeg',
     'seg': 'n0b',
     'window': '25.093-37.582',
     'wide': False,
     'jesus': False,
     'ref': False,
     'locks': ['PASTURE'],
     'narration': 'David begins with trust, not scarcity.',
     'must_show': 'trust as landscape — the flock feeding unhurried across abundant green, no '
                  'scanning, no huddling; plenty and safety as the opening premise.',
     'must_not_show': 'no halo; NOTHING anxious anywhere in the flock — ease is the picture.',
     'scene': 'The psalm opens its books on abundance: the flock feeds unhurried across the deep '
              'green — heads down in the sweet grass, lambs sprawled flat in the warmth, not one '
              'ear turned to scan the ridgelines, not one animal pressed against another in worry '
              '— a hillside whose whole economy runs on the fact of its shepherd — trust, '
              'published in wool across a green page, before one hard thing has been mentioned. '
              'No people are needed in this frame.'},
    {'id': 'v2-r150-b06',
     'out': 's05-he-maketh-me-to-lie.jpeg',
     'seg': 's2',
     'window': '37.583-45.216',
     'wide': False,
     'jesus': False,
     'ref': False,
     'locks': ['PASTURE'],
     'narration': 'He maketh me to lie down in green pastures: he leadeth me beside the still '
                  'waters.',
     'must_show': 'SCRIPTURE-EXACT: the verse itself — sheep LYING DOWN in the deep green, and '
                  "the stream's GLASS-STILL pool holding the sky; the psalm's most famous "
                  'picture, exact.',
     'must_not_show': 'no halo; the water STILL as glass (never rushing); the lying-down general.',
     'scene': 'The two famous images share one sheltered valley: across the deep spring green the '
              'flock lies DOWN — folded legs, settled wool, chins on the grass — while beside '
              'them the stream widens into a pool gone still as glass, holding the willows and '
              'the sky upside down without a ripple — grass a sheep can trust and water a sheep '
              'can drink without fear of the current: the whole verse, lying quietly in one '
              'valley. No people are needed in this frame.'},
    {'id': 'v2-r150-b07',
     'out': 's06-the-image-is-deliberate-a.jpeg',
     'seg': 'n1a',
     'window': '45.216-51.916',
     'wide': False,
     'jesus': False,
     'ref': False,
     'locks': ['DAVID', 'PASTURE'],
     'narration': 'The image is deliberate: a sheep lies down only when it feels safe.',
     'must_show': 'the fact behind the image — close on one ewe folded fully down at rest, eyes '
                  "soft, unafraid — with the young shepherd's legs standing near; safety as the "
                  'precondition.',
     'must_not_show': "no halo; the ewe's ease TOTAL — soft eyes, settled breath; his nearness "
                      'the reason.',
     'scene': 'Shepherds know what the poets borrowed: close on one ewe folded fully down in the '
              'sweet grass — legs tucked, wool settled, the dark eyes gone soft and half-lidded — '
              "and standing near enough to touch, the young shepherd's steady legs and grounded "
              'staff — because a sheep is a walking list of fears, and it lies down for exactly '
              'one reason: somebody it trusts is standing guard over the moment. Every figure has '
              'two arms, two hands and one head.'},
    {'id': 'v2-r150-b08',
     'out': 's24-afraid-of-rushing-water.jpeg',
     'seg': 'n1a',
     'window': '51.916-58.816',
     'wide': False,
     'jesus': False,
     'ref': False,
     'locks': [],
     'narration': 'A sheep will not drink from rushing water. It is afraid of it.',
     'must_show': 'the fact shown plainly — a fast white-water stream and a ewe balking at its '
                  'edge, feet planted, head pulled back from the noise; the fear readable.',
     'must_not_show': 'no halo; the water FAST (white over rocks); the ewe clearly refusing, not '
                      'drinking; no person in this frame; realistic photograph.',
     'scene': 'A rocky stream in spate — quick white water breaking over stones — and at its edge '
              'ONE ewe stopped stiff, forelegs braced, head drawn back from the rush, ears '
              'pinned; two more sheep hang back on the bank behind her. CAMERA low at the '
              'waterline from across the stream, the blur of fast water in the near foreground, '
              'the balking ewe sharp beyond it. Grey-green light off the water; no shepherd in '
              'this frame. THE EWE STANDS ON THE DRY BANK, not in the water — all four feet on dry land at the edge of the stream, refusing to step in; no sheep touches the water anywhere.'},
    {'id': 'v2-r150-b09',
     'out': 's25-the-quiet-pools.jpeg',
     'seg': 'n1a',
     'window': '58.816-65.313',
     'wide': False,
     'jesus': False,
     'ref': False,
     'locks': ['DAVID'],
     'narration': 'So the shepherd goes ahead and finds the quiet pools, because he knows what '
                  'his sheep cannot say.',
     'must_show': 'the answer — the boy shepherd kneeling at a STILL pool he has led them to, '
                  'sheep drinking at ease along its edge; provision that understands.',
     'must_not_show': 'no halo; the water GLASS-STILL (mirror surface); the same boy as the '
                      'reference; sheep drinking calmly; realistic photograph.',
     'scene': 'A still green pool cupped in rock, its surface flat as glass — along its near edge '
              'a line of sheep drink, settled and unafraid, while the young shepherd DAVID (face '
              'exactly as the attached reference) kneels on one knee among them, one hand resting '
              "on a drinking ewe's back. CAMERA level across the pool so the mirror-stillness "
              'fills the lower frame and doubles the flock. Warm late light. NOT the stream '
              'framing of the previous shot. ONE single continuous photograph — absolutely NO inset picture, NO small portrait pasted in any corner, NO picture-in-picture, NO frame within the frame.'},
    {'id': 'v2-r150-b10',
     'out': 's07-he-restoreth-my-soul-the.jpeg',
     'seg': 's3a',
     'window': '65.313-72.513',
     'wide': False,
     'jesus': False,
     'ref': False,
     'locks': ['DAVID', 'PASTURE'],
     'narration': 'He restoreth my soul: The Shepherd does more than keep David alive; he brings '
                  'him back when he is spent.',
     'must_show': 'SCRIPTURE-EXACT: the restoring — the young shepherd lifting a spent, cast ewe '
                  'back onto her feet, steadying her until she stands; restoration as a '
                  "shepherd's real work.",
     'must_not_show': 'no halo; the ewe SPENT, not injured — cast and weary; the lift gentle and '
                      'practiced.',
     'scene': 'Restoring a soul looks like this on a hillside: the young shepherd crouches over a '
              'cast ewe — down too long, legs folded wrong, too spent to right herself — and '
              'gathers her up with practiced arms, setting her back on her feet and holding '
              'steady while the legs remember their job — not rescue from death, something '
              'quieter and more common: brought BACK, stood up, breathed alongside until walking '
              'works again — the verse every worn-out believer was written for. Every figure has '
              'two arms, two hands and one head.'},
    {'id': 'v2-r150-b11',
     'out': 's26-cast.jpeg',
     'seg': 'n1b',
     'window': '72.513-80.613',
     'wide': False,
     'jesus': False,
     'ref': False,
     'locks': ['PASTURE'],
     'narration': 'Shepherds have a word for a sheep stuck on its back, legs in the air, unable '
                  'to rise. Cast. A cast sheep will die where it lies unless someone comes.',
     'must_show': 'the word made visible — ONE sheep flipped fully onto its back in the grass, '
                  'all four legs up and pawing air, wool-heavy body helpless; alone, the trouble '
                  'unmistakable.',
     'must_not_show': 'no halo; the sheep genuinely UPSIDE-DOWN (spine to the ground, legs '
                      'skyward) — not merely lying down; no blood, no wound, no predator; no '
                      'person in this frame; realistic photograph.',
     'scene': 'Open pasture, and in the middle of it ONE ewe cast on her back — spine flat to the '
              'grass, heavy wool holding her down, all four legs up and working uselessly at the '
              'air, head tipped back. Nothing else near her; the flock a soft blur far behind. '
              'CAMERA low in the grass a few feet away at her level, the helplessness filling the '
              'frame. Flat honest overcast light.'},
    {'id': 'v2-r150-b12',
     'out': 's27-held-until.jpeg',
     'seg': 'n1b',
     'window': '80.613-91.113',
     'wide': False,
     'jesus': False,
     'ref': False,
     'locks': ['DAVID', 'PASTURE'],
     'narration': 'So the shepherd restores it. He lifts it upright and holds it tight against '
                  'himself until the blood runs back into its legs.',
     'must_show': 'the restoring itself — the boy shepherd crouched with the ewe set upright '
                  'against his legs and chest, both arms wrapped firm around her body, holding '
                  'her steady; patient, close, unhurried.',
     'must_not_show': 'no halo; the HOLD tight and supporting (her feet under her but her weight '
                      'leaned into him); the same boy as the reference; realistic photograph.',
     'scene': 'Close on the rescue: the young shepherd DAVID (face exactly as the attached '
              'reference) kneels in the grass with the ewe gathered UPRIGHT against his legs and '
              'chest, both arms wrapped firmly around her body, his cheek near her wool, her feet '
              'set under her but her weight still leaned into him — held tight while the blood '
              'comes back into her legs. CAMERA close at his side at kneeling height, the '
              'patience readable in his hands. NOT the low lone-sheep framing of the previous '
              'shot.'},
    {'id': 'v2-r150-b13',
     'out': 's28-stand-again.jpeg',
     'seg': 'n1b',
     'window': '91.113-99.099',
     'wide': False,
     'jesus': False,
     'ref': False,
     'locks': ['DAVID', 'PASTURE'],
     'narration': 'That is the word David chose. Held until you can stand.',
     'must_show': 'the outcome — the ewe back on her own four feet beside him, steadying, and the '
                  'boy still crouched with one hand resting on her back; restored.',
     'must_not_show': 'no halo; she stands on ALL FOUR feet, upright and certain; his hand still '
                      'on her back; the same boy as the reference; realistic photograph.',
     'scene': 'The ewe stands again — all four feet under her in the cropped grass, body angled '
              'slightly toward the boy as if trusting the nearness — and the young shepherd DAVID '
              '(face exactly as the attached reference) stays crouched beside her, one steadying '
              'hand spread on her back, watching her hold her own weight. CAMERA a step back at '
              'HER eye level, the two of them centred, pasture soft beyond. Quiet relief, not '
              'triumph. NOT the tight embrace framing of the previous shot.'},
    {'id': 'v2-r150-b14',
     'out': 's08-he-leadeth-me-in-the.jpeg',
     'seg': 's3b',
     'window': '99.099-104.764',
     'wide': False,
     'jesus': False,
     'ref': False,
     'locks': ['DAVID', 'PASTURE'],
     'narration': "he leadeth me in the paths of righteousness for his name's sake.",
     'must_show': 'SCRIPTURE-EXACT: the right path — the flock following the young shepherd '
                  'single-file along a true worn path on the hillside; led, not driven; he AHEAD.',
     'must_not_show': 'no halo; DIRECTION — the shepherd ahead, the flock following the path he '
                      'chose.',
     'scene': 'Right paths are chosen from the front: the young shepherd walks AHEAD along the '
              'worn hillside track, and behind him the flock follows single-file — nose to tail '
              'down the path he picked, past the drop he knows about and the bad water he does '
              'not stop at — led, never driven, every safe step of theirs riding on his knowledge '
              "of the ground — a shepherd's route-craft, staked on his own name every time the "
              'flock arrives whole. Every figure has two arms, two hands and one head.'},
    {'id': 'v2-r150-b15',
     'out': 's09-the-guarantee-is-the-own.jpeg',
     'seg': 'n2',
     'window': '104.764-112.264',
     'wide': False,
     'jesus': False,
     'ref': False,
     'locks': ['DAVID', 'PASTURE'],
     'narration': "The guarantee is the Shepherd's own character, not David's performance.",
     'must_show': "for-his-name's-sake — the shepherd's steady back leading on; the flock's "
                  "safety resting visibly on HIM, not on any sheep's merit.",
     'must_not_show': 'no halo; the composition weights the SHEPHERD — the flock ordinary, the '
                      'leader the guarantee.',
     'scene': "Notice whose reputation the safety rides on: the shepherd's steady back leads on "
              'up the path, staff swinging its easy rhythm — and behind him the flock is just a '
              'flock: some obedient, some straggling, one lamb wandering a step wide and being '
              'whistled back — nothing in their performance holding the system up — the whole '
              'guarantee walking in front of them, in the character of the one whose name is on '
              'the flock. Every figure has two arms, two hands and one head.'},
    {'id': 'v2-r150-b16',
     'out': 's29-a-voice-they-know.jpeg',
     'seg': 'n2',
     'window': '112.264-120.864',
     'wide': False,
     'jesus': False,
     'ref': False,
     'locks': ['DAVID'],
     'narration': "Sheep will only follow a voice they know. A stranger's call scatters them. And "
                  "in David's day the shepherd lived with his sheep.",
     'must_show': 'the following — the boy shepherd walking AHEAD up the path, not driving from '
                  'behind, the flock strung out close on his heels of its own will; led by a '
                  'known voice.',
     'must_not_show': 'no halo; he leads FROM THE FRONT (flock behind him, nobody driving); the '
                      'same boy as the reference; realistic photograph.',
     'scene': 'A worn hill path in morning light: the young shepherd DAVID (face exactly as the '
              'attached reference) walks AHEAD up the trail, staff loose in his hand, not looking '
              'back — and behind him the flock follows close and willing, strung along the path '
              'in his footsteps, the nearest ewe almost at his heel. CAMERA behind and above the '
              'LAST sheep, looking up the line to the boy at its head. Leading, never driving. '
              'NOT a meadow wide. EVERY sheep is BEHIND him on the path — not one sheep between the boy and the camera-side of the trail ahead of him; he is unmistakably first, at the head of the line.'},
    {'id': 'v2-r150-b17',
     'out': 's30-he-slept-beside-them.jpeg',
     'seg': 'n2',
     'window': '120.864-129.795',
     'wide': False,
     'jesus': False,
     'ref': False,
     'locks': ['DAVID'],
     'narration': 'He slept beside them under the open sky and walked out ahead of them each '
                  'morning. The guiding voice was the most familiar voice in their world.',
     'must_show': 'the living-with — night on the hills, the boy shepherd asleep on the ground IN '
                  'AMONG the bedded flock, staff beside him, low ember-light keeping the near wool '
                  'warm; a shepherd who stays.',
     'must_not_show': 'no halo; he sleeps AMONG them (sheep bedded close on both sides, one '
                      'nearly against his back); warm ember light on every face and fleece, never '
                      'grey moonlit pallor; the same boy as the reference; realistic photograph.',
     'scene': 'Night on the open hillside: the flock bedded down in a loose warm mass under the '
              'stars, and IN AMONG THEM — not apart — the young shepherd DAVID (face as the '
              'attached reference) asleep on his side on a spread cloak, staff within reach, the '
              'nearest ewe settled almost against his back. The low amber light of a dying '
              "watch-fire at the frame's edge keeps faces and fleece warm, never grey. CAMERA low "
              'and close across the backs of the sheep to the sleeping boy. Still, safe, '
              'personal.'},
    {'id': 'v2-r150-b18',
     'out': 's11-yea-though-i-walk-through.jpeg',
     'seg': 's4',
     'window': '129.795-140.727',
     'wide': False,
     'jesus': False,
     'ref': False,
     'locks': ['DAVID', 'GORGE'],
     'narration': 'Yea, though I walk through the valley of the shadow of death, I will fear no '
                  'evil: for thou art with me; thy rod and thy staff they comfort me.',
     'must_show': 'SCRIPTURE-EXACT: the valley — the YOUNG shepherd (ruddy, seventeen, short DARK '
                  'RUST tunic) and flock passing THROUGH the deep-shadowed gorge, ROD (a short '
                  'club) in one hand AND STAFF (a crook) in the other, BOTH clearly visible, the '
                  'bright far end visible; real dark, no fear imagery beyond it.',
     'must_not_show': 'ABSOLUTE: no death imagery, no bones, no spectres — real deep shadow and '
                      'the THROUGH; ROD and STAFF BOTH visible; David is the YOUNG shepherd here '
                      '(~17, rust tunic), NEVER the older king in blue.',
     'scene': 'The dark part of the route is on the map and the shepherd walks it anyway: down '
              "the gorge's shadowed floor the little procession moves — true deep shade, the rock "
              'walls close, the flock bunched and quiet — and at their centre the YOUNG shepherd '
              '(ruddy, seventeen, in the short dark rust tunic) with the ROD (a short club) in '
              'one fist for whatever the dark holds and the STAFF (a crook) in the other for the '
              "flock's own stumbling, both clearly in view — while far ahead, small and certain, "
              "the gorge's bright doorway of daylight waits: THROUGH, says the whole picture; "
              'this valley is a road, not a residence. Every figure has two arms, two hands and '
              'one head.'},
    {'id': 'v2-r150-b19',
     'out': 's12-notice-what-changes-here-up.jpeg',
     'seg': 'n3',
     'window': '140.727-146.827',
     'wide': False,
     'jesus': False,
     'ref': False,
     'locks': ['DAVID'],
     'narration': 'Notice what changes here: up to now David has been saying He.',
     'must_show': "the grammar noticed — the king's face lifting from the scroll mid-thought, pen "
                  'paused; the discovery arriving in the writing.',
     'must_not_show': 'no halo; the pause READABLE — pen lifted, eyes away, the noticing.',
     'scene': "The poet catches his own pronoun changing: the king's pen stops mid-line and his "
              'face lifts from the scroll, eyes gone away into the middle distance of the chamber '
              '— HE leadeth; HE restoreth; HE, HE, all down the sunlit verses — and then the '
              'valley entered the poem, and something in the grammar moved closer — the discovery '
              'arriving now in the lamplight, pen in the air, that the dark did something to the '
              'distance. Every figure has two arms, two hands and one head.'},
    {'id': 'v2-r150-b20',
     'out': 's13-in-the-valley-he-starts.jpeg',
     'seg': 'n3',
     'window': '146.827-152.840',
     'wide': False,
     'jesus': False,
     'ref': False,
     'locks': ['DAVID', 'GORGE'],
     'narration': 'In the valley he starts saying You. He gets closer to the Shepherd in the '
                  'dark, not further away.',
     'must_show': 'the nearness in the dark — IN the gorge: a sheep pressed hard against the '
                  "shepherd's legs, his hand down on its head; THOU-art-with-me as physical "
                  'closeness.',
     'must_not_show': 'ABSOLUTE: no death imagery; the closeness the whole frame — pressed wool, '
                      'resting hand, deep shade.',
     'scene': "The pronoun changed because the distance did: in the gorge's deepest shade a ewe "
              "presses hard against the shepherd's legs — flank to shin, wool crushed close, "
              'walking in his stride the way fear walks in trust — and his free hand comes down '
              'to rest on her head as they move — THOU art with me: not a doctrine at this depth '
              'of shadow but a pressure, warm and immediate, at exactly the place the dark '
              'presses hardest — closer in the valley than anywhere on the sunlit grass. Every '
              'figure has two arms, two hands and one head.'},
    {'id': 'v2-r150-b21',
     'out': 's14-thou-preparest-a-table-before.jpeg',
     'seg': 's5a',
     'window': '152.840-158.765',
     'wide': False,
     'jesus': False,
     'ref': False,
     'locks': ['TABLE'],
     'narration': 'Thou preparest a table before me in the presence of mine enemies:',
     'must_show': 'SCRIPTURE-EXACT: the table — the spread wooden table in open golden country, '
                  'laid full; on the FAR ridgeline, vague distant silhouettes watching, unable to '
                  'approach.',
     'must_not_show': 'ABSOLUTE: the enemies FAR and vague — ridge silhouettes only, never close, '
                      "never detailed; the table's calm the picture.",
     'scene': 'The strangest banquet in scripture is set in the open on purpose: the wooden table '
              'stands spread in the golden hill-country — cloth laid, bread stacked, the horn of '
              'oil and the generous cup in their places — while far off on the ridgeline a '
              'scatter of vague silhouettes stands watching, small as thorn bushes and exactly as '
              'able to interfere — a meal prepared with unhurried care in full view of everything '
              'that wishes it could prevent it. Every figure has two arms, two hands and one '
              'head.'},
    {'id': 'v2-r150-b22',
     'out': 's15-even-danger-has-to-watch.jpeg',
     'seg': 'n4a',
     'window': '158.766-164.588',
     'wide': False,
     'jesus': False,
     'ref': False,
     'locks': ['TABLE', 'DAVID'],
     'narration': 'Even danger has to watch while the Shepherd provides.',
     'must_show': 'the calm meal — the guest (young David) seated and EATING at ease at the '
                  'table, back straight, unhurried; the far watchers still on their ridge, still '
                  'helpless.',
     'must_not_show': "ABSOLUTE: enemies stay far silhouettes; the guest's EASE the doctrine — "
                      'eating slowly in full view.',
     'scene': 'The provocation of the table is how slowly he eats at it: young David sits at the '
              'spread cloth in the golden light, tearing bread without hurry, cup at his hand, '
              "back straight and shoulders easy — while the ridge's far silhouettes hold their "
              'distance, present, watching, and perfectly helpless — safety performed at dinner '
              "pace in the presence of everything that objects to it: the Shepherd's table, where "
              "danger's whole role is spectator. Every figure has two arms, two hands and one "
              'head.'},
    {'id': 'v2-r150-b23',
     'out': 's16-thou-anointest-my-head-with.jpeg',
     'seg': 's5b',
     'window': '164.587-170.249',
     'wide': False,
     'jesus': False,
     'ref': False,
     'locks': ['TABLE', 'DAVID'],
     'narration': 'thou anointest my head with oil; my cup runneth over.',
     'must_show': "SCRIPTURE-EXACT: the anointing and the overflow — a host's hand pouring oil "
                  "onto the seated guest's head (the guest is YOUNG David, ~17, ruddy, short dark "
                  'rust tunic — the same young man seated at the table in b15), AND the cup '
                  'filled past its brim, running onto the cloth.',
     'must_not_show': 'no halo; the overflow REAL — PALE TRANSLUCENT AMBER-GOLD grape wine over '
                      'the brim, pooling as a light golden wet patch; ABSOLUTELY NO red, crimson, '
                      'burgundy, dark maroon, blood-like liquid, blood-like stain, wound or gore '
                      "anywhere; the oil's pour gentle on the head; the guest is the YOUNG "
                      'shepherd (~17), NEVER the older king in blue.',
     'scene': "The host's generosity gets physically out of hand: from above, a steady hand tips "
              'the horn and the oil comes down bright onto the bowed head of the guest — YOUNG '
              'David, seventeen, ruddy, in the short dark rust tunic, the same young man from the '
              'table in b15 — the old extravagant welcome, running warm at the hairline — while '
              'on the cloth the cup has already passed its brim, pale translucent amber-gold '
              'grape wine trembling over the lip and spreading a LIGHT GOLDEN wet patch into the '
              'weave — visibly wine, never red and never blood-like — anointed and overfilled at '
              'the same table, by a host whose measures simply do not stop at full. Every figure '
              'has two arms, two hands and one head.'},
        {'id': 'v2-r150-b24',
     'out': 's31-cup-runneth-over.jpeg',
     'seg': 'n4b',
     'window': '170.249-172.997',
     'wide': False,
     'jesus': False,
     'ref': False,
     'locks': ['TABLE'],
     'narration': 'You honor me;',
     'must_show': 'the honoring made visible — a TIGHT INSERT on the one generous cup at the table, filled past its brim, wine running down its sides and pooling on the wood; abundance overflowing.',
     'must_not_show': 'no halo; a CLOSE insert only (no wide table view — that framing belongs to an earlier shot); the cup genuinely OVERFLOWING; no people in frame; realistic photograph.',
     'scene': 'A tight close insert at table height: the one generous cup filled past its brim, dark red wine sliding down its sides in slow ribbons and pooling in the woodgrain around its base, the woven cloth and a torn piece of flat bread soft behind it in golden late light. CAMERA close and low across the table top, the overflowing cup filling the frame. Honor poured past the rim. NOT the wide spread-table framing used earlier.'},
    {'id': 'v2-r150-b25',
     'out': 's18-surely-goodness-and-mercy-shall.jpeg',
     'seg': 's6a',
     'window': '172.997-178.856',
     'wide': False,
     'jesus': False,
     'ref': False,
     'locks': ['DAVID', 'PASTURE'],
     'narration': 'Surely goodness and mercy shall follow me all the days of my life:',
     'must_show': 'SCRIPTURE-EXACT: the following — the flock heading home at warm dusk with the '
                  'shepherd walking BEHIND them; the following made of the shepherd himself, rear '
                  'guard of goodness.',
     'must_not_show': 'no halo; DIRECTION — flock ahead toward home, shepherd BEHIND; the '
                      'pursuit-position exact.',
     'scene': "At the day's end the shepherd changes position and the verse is born: the flock "
              'strings out ahead down the homeward path in the warm dusk — and BEHIND them, where '
              'the stragglers and the wolves and the night all live, the shepherd walks rear '
              'guard, staff easy, eyes on every trailing lamb — goodness and mercy in their true '
              'station: not up front where you can watch them, but behind you, where you are '
              'weakest, following all the way home. Every figure has two arms, two hands and one '
              'head.'},
    {'id': 'v2-r150-b26',
     'out': 's19-david-pictures-those-gifts-not.jpeg',
     'seg': 'n5a',
     'window': '178.856-185.329',
     'wide': False,
     'jesus': False,
     'ref': False,
     'locks': ['DAVID', 'PASTURE'],
     'narration': 'David pictures those gifts not trailing weakly behind, but pursuing him.',
     'must_show': 'the pursuit — the shepherd striding ENERGETICALLY after the flock, closing '
                  'distance on a straggler, purposeful; following as active chase.',
     'must_not_show': 'no halo; the stride VIGOROUS — pursuit, not drift; the straggler being '
                      'caught up to.',
     'scene': "The Hebrew word is closer to hunted-down than tagging-along: the shepherd's easy "
              'walk breaks into a purposeful stride — closing hard on a straggling lamb that has '
              'fallen back into the dusk, his staff swinging with intent, ground disappearing '
              'under him — goodness that will not let the slowest sheep drift out of its reach, '
              'mercy that RUNS when the gap opens — pursued, all the days of his life, by exactly '
              'the two hunters a soul wants on its trail. Every figure has two arms, two hands '
              'and one head.'},
    {'id': 'v2-r150-b27',
     'out': 's20-and-i-will-dwell-in.jpeg',
     'seg': 's6b',
     'window': '185.329-190.177',
     'wide': False,
     'jesus': False,
     'ref': False,
     'locks': ['PASTURE'],
     'narration': 'and I will dwell in the house of the LORD forever.',
     'must_show': 'SCRIPTURE-EXACT: the arriving — the warm-lit fold-house at dusk, its door '
                  "standing open, the flock streaming IN; home as the psalm's destination.",
     'must_not_show': 'no halo; the door OPEN and warm; DIRECTION — inward, home; lamplight '
                      'physical.',
     'scene': "The song's last road leads to a lit doorway: the stone fold-house stands warm "
              'against the dusk with its wide door open and lamplight lying out across the '
              'threshold — and the flock streams IN, wool brushing the doorposts, animal after '
              'animal crossing from the cooling dark into the kept warmth — dwelling, the verse '
              'calls it: not visiting, not passing through — the house of the LORD receiving its '
              'own for good, which is where every road in the psalm was always going. Every '
              'figure has two arms, two hands and one head.'},
    {'id': 'v2-r150-b28',
     'out': 's21-the-song-ends-where-every.jpeg',
     'seg': 'n5b',
     'window': '190.177-193.945',
     'wide': False,
     'jesus': False,
     'ref': False,
     'locks': [],
     'narration': "The song ends where every sheep longs to be: safely in the Shepherd's "
                  'presence.',
     'must_show': 'ONE single coherent frame — the rest at nightfall: inside a lamplit stone '
                  'sheepfold the flock lies folded and asleep, safe within the walls, and on a '
                  'low stone ledge WITHIN the same fold the finished curled scroll rests beside '
                  'the quiet harp; a single period clay oil lamp lights the whole scene.',
     'must_not_show': 'ABSOLUTE: NOT a two-panel / split / diptych / collage frame — ONE '
                      'continuous photographic space, no horizontal or vertical seam dividing two '
                      'scenes; NO separate palace-desk half; no second location; no figure/person '
                      'in frame; no halo or glow; no modern kerosene lamp — a clay oil lamp only; '
                      'script on the scroll indistinct.',
     'scene': 'The song comes to rest in one quiet room at nightfall: inside a lamplit stone '
              "sheepfold the flock lies folded and breathing slow, safe within the Shepherd's "
              'kept walls — and on a low stone ledge along that same fold, in the same warm '
              "lamplight, the finished scroll lies curled beside the quiet harp, the day's "
              'shepherding and the psalm both set down and at peace. One single photographic '
              'frame, one continuous space, one small clay oil lamp — the sheep safe and the song '
              'finished in the very same kept place, exactly where every sheep alive longs to be: '
              'in the presence, safe, home. No people are in the frame.'},
]


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# Each token's plate is attached as a PLACE LOCK image to every beat whose
# `locks` name it. Plates live in PLACE-REF/ (gitignored art); PLACE-WIRING.json
# is the committed record — `v2_stash.py --wire <this build>` rebuilds the
# plates on any machine that has the source builds' stills.
PLACE_REFS = {
    "PASTURE": "PLACE-REF/pasture.jpeg",  # build-150-shepherd-psalm s05-he-maketh-me-to-lie (manual)
    "TABLE": "PLACE-REF/table.jpeg",  # build-150-shepherd-psalm s14-thou-preparest-a-table-before (manual)
}
# === end PLACE-PLATES ===

# Per-story face sheets, generated by v2_story_cast.py. Identity is
# carried by IMAGE, not by wording — text locks let the elder son come
# back as three different men in row 2 (Cameron, 2026-07-30).
REFS = {
    "DAVID": "CAST-REF-V2/david.jpeg",
}
