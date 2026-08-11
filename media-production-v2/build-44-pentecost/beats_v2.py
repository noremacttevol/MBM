#!/usr/bin/env python3
"""V2 beat map — row 44, build-44-pentecost (Acts 2 — the Spirit poured out).

Row 44 was swapped 2026-07-23 (Cameron) from "The two debtors" (a double-telling
of #74's Luke 7 scene) to PENTECOST, an all-new Bible-only milk story. It has NO
prior V1 render, so the narration was voiced from scratch with the LOCKED
ElevenLabs cast (narrator Brian, scripture Roger) and the audio track is rebuilt
from those mp3s at the extract_beats offsets — AUDIO_FROM_V1_SEGMENTS = True.

COVERAGE: 24 pictures over 138.0 s of picture time = 5.75 s/picture (house style).

SCRIPTURE FACTS (Acts 2 KJV):
  2:1-2  they were all with one accord in one place; a sound from heaven as of a
         RUSHING MIGHTY WIND filled all the house where they were sitting.
  2:3    cloven tongues LIKE AS OF FIRE sat upon EACH of them.
  2:4    filled with the Holy Ghost, they began to speak with OTHER TONGUES.
  2:5-6  devout men out of EVERY NATION; every man heard them in his OWN language.
  2:13   others mocking said, These men are full of new wine.
  2:14   Peter, standing up with the eleven, lifted up his voice.
  2:23-24 him... ye have taken, and by wicked hands have crucified and slain: whom
         God hath raised up, having loosed the pains of death.
  2:36   God hath made that same Jesus, whom ye have crucified, both LORD and CHRIST.
  2:37   they were PRICKED IN THEIR HEART, and said, Men and brethren, what shall we do?
  2:38   Repent, and be baptized every one of you in the name of Jesus Christ...
  2:41   the same day there were added about THREE THOUSAND souls.

RENDERING LAWS (this row's hard gates):
  - TONGUES OF FIRE: small, calm flames resting in the AIR just ABOVE each bowed
    head — reverent light, never touching, never burning hair, clothing, skin or
    the room. NO dove anywhere (Acts says fire, not a dove — Luke 3 is a different
    scene). NO halo, glow or rim-light on anyone. A frame with a house on fire,
    people burning, scorch, smoke of judgment, or a descending dove is a reject.
  - JESUS IS NOT PRESENT — this is after the Ascension. jesus:False, ref:False on
    EVERY beat. He is proclaimed, never shown. Because only Jesus ever wears cream,
    NOBODY in this video wears cream/off-white robes: Peter and the apostles are in
    ordinary first-century tunics of earth-brown, indigo, ochre and olive.
  - THE APOSTLES: PETER is the locked focus; JOHN, JAMES-Z and ANDREW carry the
    other named faces. Judas is dead (Acts 1) so TWELVE-CANONICAL is deliberately
    NOT used (its roster still lists Judas-Iscariot); the wider group reads as "the
    apostles," dark-haired first-century Galilean men, never a blond among them.
  - PETER'S ARC: fearful denier weeks ago -> now standing UNAFRAID above the crowd,
    the change visible in his bearing. The sermon is entirely about the risen Jesus,
    never about Peter, the wind or the fire.
  - THE CROWD is the subject of the preaching beats: pilgrims of many nations in
    varied period dress, their faces moving from mockery -> astonishment -> pricked
    to the heart. Gazes converge on Peter; he is never a small detached figure.

TIME OF DAY: one bright Pentecost morning. Interior upper room at soft dawn; the
public square in full clear morning sun; the baptism pool in late-morning light.

CHANGING CONDITION (kept OUT of the locks): the crowd's faces (mocking -> pricked);
Peter's posture (praying -> standing bold); the flames exist ONLY in the s1 beats.
"""

OUTPUT_VIDEO_NAME = "acts-2_pentecost.mp4"

# Rebuild the narration track from this build's OWN ElevenLabs mp3s at the
# extract_beats offsets (there is no V1 mp4 to copy). Re-voices nothing.
AUDIO_FROM_V1_SEGMENTS = True

REF = False  # Jesus is not present in this story.

# LOCKS: one entry per recurring SETTING. Setting locks never name a character.
# Recurring people (PETER, JOHN, JAMES-Z, ANDREW) come from the shared CAST-V2
# library by token — do not redefine them here. Nobody wears cream (only Jesus
# does, and he is absent).
LOCKS = {
    "UPPER-ROOM": (
        "UPPER-ROOM LOCK: a large plain upper room in a first-century Jerusalem "
        "house — pale lime-plastered stone walls, a low wooden-beamed ceiling, a "
        "few small high windows letting in soft dawn light, simple reed floor mats "
        "and low stone benches, small clay oil lamps in wall niches. An ordinary "
        "quiet room, never a temple or a church. The same room throughout."
    ),
    "JERUSALEM-COURT": (
        "JERUSALEM-COURT LOCK: a broad open public square in first-century "
        "Jerusalem — pale worn limestone paving, a set of broad shallow stone steps "
        "rising on one side to a row of plain square stone pillars, flat-roofed "
        "sand-coloured houses and the temple walls beyond, bright clear morning sky. "
        "The same square, steps and pillars throughout."
    ),
    "BAPTISM-WATER": (
        "BAPTISM-WATER LOCK: a large stone-lined immersion pool in Jerusalem — broad "
        "shallow steps of pale limestone descending into clear still water, plastered "
        "surrounds, the sand-coloured city beyond in bright morning light. The same "
        "pool throughout."
    ),
}

BEATS = [
    # ---------------- n1 — they waited and prayed (upper room, dawn) ----------------
    {
        "id": "v2-r044-b01", "out": "s01-gathered-waiting-in-the-upper-room.jpeg", "seg": "n1",
        "window": "0.00-6.30", "wide": True, "jesus": False, "ref": REF,
        "locks": ["UPPER-ROOM", "PETER"],
        "narration": (
            "Before Jesus went back to heaven, he told his followers to wait in "
            "Jerusalem — he was going to send them help."
        ),
        "must_show": "an establishing wide of the upper room at dawn: the small company of Jesus's followers gathered together, some seated on mats, some kneeling, waiting — Peter among them; a quiet, expectant room.",
        "must_not_show": "no halo, glare or rim-light on anyone; no cream/off-white robes on anyone; no flames yet; not a temple or a church, just a plain house room.",
        "scene": (
            "Shot from the doorway of the room, the camera looking in past the backs "
            "of two seated followers toward the gathered company: a dozen and more "
            "of Jesus's people together in the pale dawn light of a plain upper room, "
            "some cross-legged on reed mats, some kneeling, Peter among them with his "
            "weathered fisherman's face turned in thought — all of them simply "
            "waiting, the way people wait for something promised but not yet "
            "understood. Ordinary earth-brown and indigo tunics, no fine clothes. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r044-b02", "out": "s02-they-waited-and-prayed.jpeg", "seg": "n1",
        "window": "6.30-12.32", "wide": False, "jesus": False, "ref": REF,
        "locks": ["UPPER-ROOM", "PETER", "JOHN"],
        "narration": (
            "They did not fully understand what he meant. So they waited, and they "
            "prayed. Then one morning it came."
        ),
        "must_show": "a closer two-shot of Peter and John at prayer among the company — heads bowed, hands open or clasped, the honest patience of people who do not yet know what they are waiting for.",
        "must_not_show": "no halo, glare or rim-light; no cream robes; no flames yet; reverent, not theatrical.",
        "scene": (
            "Closer now, a quiet two-shot: Peter and young John kneeling side by side "
            "on the reed mats, heads bowed over open hands, lips moving in prayer, the "
            "soft dawn from a high window laying plain light across their faces — two "
            "tired, faithful men holding a promise they cannot yet see, the whole room "
            "hushed around them. Dark hair, dark beards, ordinary tunics. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    # ---------------- s1 — the wind and the tongues of fire ----------------
    {
        "id": "v2-r044-b03", "out": "s03-a-rushing-mighty-wind.jpeg", "seg": "s1",
        "window": "12.32-17.00", "wide": True, "jesus": False, "ref": REF,
        "locks": ["UPPER-ROOM", "PETER"],
        "narration": (
            "And suddenly there came a sound from heaven as of a rushing mighty wind, "
            "and it filled all the house where they were sitting."
        ),
        "must_show": "the sudden wind filling the room: loose cloths, hair and lamp-flames all leaning hard the same way, dawn light rushing in through the high windows, the whole company startled and looking up toward the sound.",
        "must_not_show": "no halo, glare or rim-light; no cream robes; NO tongues of fire yet in THIS frame (that is the next beat); nothing burning; no dove; no broken windows or storm damage — the room is unharmed.",
        "scene": (
            "The camera inside the room now, low behind the backs of the near seated "
            "company and looking up past them: an unseen wind pours through the upper "
            "room from above — the "
            "small oil-lamp flames all bent flat one way, head-cloths and loose hair "
            "streaming, the men and women flinching and turning their faces up toward "
            "the sound none of them can see, dawn light flooding brighter through the "
            "high windows. The room itself stands whole and unharmed. Ordinary tunics, "
            "no fine robes. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r044-b04", "out": "s04-cloven-tongues-like-as-of-fire.jpeg", "seg": "s1",
        "window": "17.00-21.60", "wide": True, "jesus": False, "ref": REF,
        "locks": ["UPPER-ROOM", "PETER"],
        "narration": "And there appeared unto them cloven tongues like as of fire,",
        "must_show": "THE HARD GATE: small calm single flames, one hovering in the air a hand's-breadth ABOVE each bowed head across the company — quiet points of light like little candle-flames, reverent and gentle, the faces lit with awe.",
        "must_not_show": "ABSOLUTE: no flame ever touches hair, skin, cloth or the room; nothing burns; no smoke, no scorch, no house-fire; NO dove; no halo, ring of light, glow or rim-light around any head — only separate small flames resting in the air above the heads.",
        "scene": (
            "The camera holds on the gathered company from a low three-quarter angle "
            "past their shoulders: above each bowed or upturned head, resting in the "
            "air a hand's-breadth clear of the hair, a single small calm flame has "
            "appeared — a quiet point of fire like a steady candle-flame, one to a "
            "person, all across the room — touching no one, burning nothing, the warm "
            "little lights laid gently over the awed upturned faces while the room "
            "stays whole and unharmed. Each flame floats separate and distinct, never "
            "a ring or crown around a head. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r044-b05", "out": "s05-it-sat-upon-each-of-them.jpeg", "seg": "s1",
        "window": "21.60-25.91", "wide": False, "jesus": False, "ref": REF,
        "locks": ["UPPER-ROOM", "PETER"],
        "narration": "and it sat upon each of them.",
        "must_show": "an intimate insert: one small steady flame resting in the air just above Peter's head, his upturned weathered face lit with wonder and tears — the Spirit come to rest on one man, standing for all.",
        "must_not_show": "ABSOLUTE: the flame never touches his hair or skin; nothing burns; no dove; no halo, glow or rim-light — one small separate flame hovering clear above him.",
        "scene": (
            "Close on Peter from just below: his weathered face tilted up, eyes wet "
            "and wide with wonder, and a single small calm flame resting in the air a "
            "clear hand's-breadth above his head — steady, gentle, touching nothing, "
            "lighting his features from above like a soft candle. Just the man and the "
            "quiet fire that has come to rest on him. Two hands, one head, ordinary "
            "tunic."
        ),
    },
    # ---------------- n2 — other tongues, every nation hears ----------------
    {
        "id": "v2-r044-b06", "out": "s06-they-spoke-in-other-tongues.jpeg", "seg": "n2",
        "window": "25.91-34.00", "wide": True, "jesus": False, "ref": REF,
        "locks": ["JERUSALEM-COURT", "PETER", "JOHN"],
        "narration": (
            "The Holy Ghost filled every one of them. Ordinary people from Galilee "
            "began to speak in languages they had never learned."
        ),
        "must_show": "the apostles spilling out from the house into the bright public square, speaking boldly to gathering passers-by — plain Galilean men suddenly unafraid, mouths open in speech, hands lifted; Peter and John among them.",
        "must_not_show": "no halo, glare or rim-light; no cream robes; no flames out here (the fire was only in the room); nothing burning; no dove.",
        "scene": (
            "The camera stands out in the square behind the backs of the gathering "
            "listeners, angled up the broad stone steps and looking past them: the "
            "plain Galilean "
            "followers have come out from the house into the full morning sun and are "
            "speaking out to everyone within reach — Peter and John at the front with "
            "arms lifted and faces alight, ordinary fishermen suddenly bold, the words "
            "pouring out of them — and the first curious travellers slowing and turning "
            "toward the sound. Earth-toned tunics, no fine robes. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r044-b07", "out": "s07-each-heard-his-own-language.jpeg", "seg": "n2",
        "window": "34.00-41.48", "wide": False, "jesus": False, "ref": REF,
        "locks": ["JERUSALEM-COURT"],
        "narration": (
            "Jerusalem was packed that day with travelers from every nation — and each "
            "one heard the wonders of God in his own tongue."
        ),
        "must_show": "the wonder on the pilgrims: a tight cluster of listeners from many nations in visibly different regional dress and features — a north-African, a Parthian in a fur cap, a Roman, a Judean — each face astonished, some pointing to their own ear, hearing their own language.",
        "must_not_show": "no halo, glare or rim-light; no cream robes; no modern clothing or objects; no flames; every figure fully first-century.",
        "scene": (
            "A tight candid cluster of listeners filling the frame, shot at their "
            "level: travellers of clearly different nations pressed together — a "
            "dark-skinned north-African in bright striped cloth, a Parthian in a "
            "fur-edged cap, a toga-edged Roman, a plain Judean — every face turned the "
            "same way and lit with the same astonishment, one man's hand rising to his "
            "own ear as if to be sure, each of them hearing his own home language out "
            "of a Galilean's mouth. First-century dress only. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    # ---------------- n3 — the crowd, the mockers, Peter stands ----------------
    {
        "id": "v2-r044-b08", "out": "s08-a-crowd-gathered-amazed.jpeg", "seg": "n3",
        "window": "41.48-46.80", "wide": True, "jesus": False, "ref": REF,
        "locks": ["JERUSALEM-COURT"],
        "narration": "A crowd gathered, amazed and confused.",
        "must_show": "an establishing wide of the whole public square filling with a large mixed crowd of pilgrims converging toward the steps, amazed and murmuring — the place and its stone steps and pillars clearly readable for every later shot.",
        "must_not_show": "no halo, glare or rim-light; no cream robes; no modern objects; no flames; the crowd curious and stirred, not a riot.",
        "scene": (
            "A high establishing wide, the camera set back and above behind the outer "
            "edge of the crowd so we look across their heads and backs toward the broad "
            "stone steps: the whole Jerusalem square filling with a large mixed throng "
            "of pilgrims in the varied dress of many nations, all drifting and "
            "converging toward the steps where the apostles stand, heads together, "
            "murmuring in amazement. The pale limestone paving, the shallow steps and "
            "the plain pillars all clearly seen. Bright clear morning. A single unified "
            "photographic frame. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r044-b09", "out": "s09-some-mocked-and-said-drunk.jpeg", "seg": "n3",
        "window": "46.80-51.80", "wide": False, "jesus": False, "ref": REF,
        "locks": ["JERUSALEM-COURT"],
        "narration": "Some mocked and said they were drunk.",
        "must_show": "a tight shot of two or three scoffers in the crowd — smirking, one waving a dismissive hand, another leaning to a neighbour with a mocking grin, sneering that these men are drunk.",
        "must_not_show": "no halo, glare or rim-light; no cream robes; no wine cups or drunkenness actually shown — just the mockers' scorn; no modern objects.",
        "scene": (
            "Tight on a knot of scoffers at the crowd's edge, shot across a bystander's "
            "shoulder: two or three well-dressed mockers smirking and rolling their "
            "eyes, one flicking a dismissive hand toward the apostles, another leaning "
            "close to a neighbour with a scornful grin — the small ugly certainty of "
            "men deciding it is only new wine. First-century dress. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r044-b10", "out": "s10-peter-stood-up-unafraid.jpeg", "seg": "n3",
        "window": "51.80-56.55", "wide": True, "jesus": False, "ref": REF,
        "locks": ["JERUSALEM-COURT", "PETER", "JOHN", "JAMES-Z"],
        "narration": (
            "So Peter — the same man who had denied Jesus only weeks before — stood up "
            "in front of everyone, unafraid now, and told them the truth."
        ),
        "must_show": "Peter risen to his full height on the steps above the crowd, one hand lifted to speak, face set and fearless, the other apostles standing with him behind — the denier now the bold witness; the crowd's faces below turned up to him.",
        "must_not_show": "no halo, glare or rim-light; no cream robes; Peter is ordinary-sized, not a giant over the crowd; no flames; the gazes of the crowd converge on Peter, he is never small or detached at the frame edge.",
        "scene": (
            "The camera is down among the crowd looking up past their turned heads to "
            "the steps: Peter has risen to his full height above them, one hand lifted "
            "open to speak, jaw set, eyes steady and unafraid — the same man who wept "
            "and denied only weeks ago, now planted like a rock — and behind him John, "
            "James and the other apostles stand shoulder to shoulder. Every upturned "
            "face in the crowd is fixed on him. Peter stands a normal man's height, "
            "raised only by the steps. Earth-toned tunics, no fine robes. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    # ---------------- s2 — crucified and slain, whom God raised ----------------
    {
        "id": "v2-r044-b11", "out": "s11-ye-have-crucified-and-slain.jpeg", "seg": "s2",
        "window": "56.55-63.50", "wide": False, "jesus": False, "ref": REF,
        "locks": ["JERUSALEM-COURT", "PETER"],
        "narration": (
            "Him, being delivered by the determinate counsel and foreknowledge of God, "
            "ye have taken, and by wicked hands have crucified and slain:"
        ),
        "must_show": "a strong three-quarter shot of Peter preaching — mid-word, one hand pressed to his own chest and the other reaching out over the crowd in appeal, grave and earnest as he names the crucifixion; a slice of the listening crowd in the near foreground.",
        "must_not_show": "no halo, glare or rim-light; no cream robes; no cross or crucifixion actually depicted (Peter speaks of it, we do not show it); Peter ordinary-sized; no modern objects.",
        "scene": (
            "A strong three-quarter shot up at Peter on the steps, the near foreground "
            "soft with the backs of listeners' heads: caught mid-word, one hand flat "
            "against his own chest and the other stretched out over the crowd in open "
            "appeal, brows drawn, grave and earnest — a plain man laying an "
            "unbearable truth in front of the very people who did it. Bright morning "
            "light, ordinary tunic. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r044-b12", "out": "s12-whom-god-hath-raised-up.jpeg", "seg": "s2",
        "window": "63.50-70.27", "wide": False, "jesus": False, "ref": REF,
        "locks": ["JERUSALEM-COURT", "PETER"],
        "narration": (
            "whom God hath raised up, having loosed the pains of death."
        ),
        "must_show": "Peter's turn to hope: face lifting, one hand rising open toward the bright sky as he declares God raised him up — the same grave man now lit with certainty; nearby listeners beginning to still.",
        "must_not_show": "no halo, glare or rim-light; no cream robes; no vision of the risen Jesus in the sky (Peter testifies, we do not depict); no flames; Peter ordinary-sized.",
        "scene": (
            "Still on Peter, but his whole bearing has turned: chin lifting, one hand "
            "opening upward toward the bright clear morning sky, his grave face now "
            "steady with certainty as he speaks of God raising the dead man up and "
            "loosing the pains of death — and in the near frame a listener or two has "
            "gone still, caught. Empty bright sky above him, nothing depicted in it. "
            "Ordinary tunic. Two hands, one head."
        ),
    },
    # ---------------- n4 — not about himself; the apostles saw him alive ----------------
    {
        "id": "v2-r044-b13", "out": "s13-not-about-himself.jpeg", "seg": "n4",
        "window": "70.27-78.00", "wide": False, "jesus": False, "ref": REF,
        "locks": ["JERUSALEM-COURT", "PETER"],
        "narration": (
            "His message was not about himself, and not about the wind or the fire. It "
            "was about the man they had rejected — living again, exactly as he had "
            "promised."
        ),
        "must_show": "Peter in humble focus — a hand turned outward and away from himself, head slightly bowed, plainly pointing the crowd past himself to another; not self-important, wholly given over to his one subject.",
        "must_not_show": "no halo, glare or rim-light; no cream robes; no flames; no depiction of Jesus; Peter humble, never grandstanding.",
        "scene": (
            "A quieter medium shot of Peter, the crowd soft behind him: he has turned a "
            "hand outward and away from his own chest, head dipped a little, plainly "
            "waving the people's attention past himself — everything in his posture "
            "saying this is not about me. A plain, spent, honest man pointing at "
            "someone the crowd cannot see. Ordinary tunic, bright morning. Two hands, "
            "one head."
        ),
    },
    {
        "id": "v2-r044-b14", "out": "s14-the-apostles-all-saw-him.jpeg", "seg": "n4",
        "window": "78.00-85.38", "wide": False, "jesus": False, "ref": REF,
        "locks": ["JERUSALEM-COURT", "PETER", "JOHN", "ANDREW"],
        "narration": (
            "And Peter said the apostles had all seen him with their own eyes."
        ),
        "must_show": "the apostles as witnesses: Peter turning a hand back toward John, Andrew and the others gathered with him, all of them nodding grave and certain — a line of ordinary men testifying they saw the risen man themselves.",
        "must_not_show": "no halo, glare or rim-light; no cream robes; no flames; the apostles all dark-haired first-century Galileans, none blond; no modern objects.",
        "scene": (
            "The camera pulls to take in Peter and the apostles together on the steps, "
            "shot from the crowd's side: Peter half-turned, one hand sweeping back "
            "toward John, Andrew and the others ranged beside him — and each of those "
            "plain, weathered men meets it with a grave certain nod, the settled look "
            "of people telling something they saw with their own eyes. Earth-toned "
            "tunics, dark hair and beards. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    # ---------------- s3 — both Lord and Christ ----------------
    {
        "id": "v2-r044-b15", "out": "s15-both-lord-and-christ.jpeg", "seg": "s3",
        "window": "85.38-90.40", "wide": False, "jesus": False, "ref": REF,
        "locks": ["JERUSALEM-COURT", "PETER"],
        "narration": (
            "Therefore let all the house of Israel know assuredly, that God hath made "
            "that same Jesus, whom ye have crucified, both Lord and Christ."
        ),
        "must_show": "the climax of the sermon: Peter at full stretch, both the moment's weight in his face and one hand raised firm, declaring the crucified Jesus is Lord and Christ — the single most important sentence, landing.",
        "must_not_show": "no halo, glare or rim-light; no cream robes; no depiction of Jesus or a throne; no flames; Peter ordinary-sized, not towering.",
        "scene": (
            "Tight and strong on Peter at the sermon's peak, shot slightly up: his "
            "whole face gathered into the weight of it, one hand raised firm and "
            "certain, the words landing like a verdict — that the very man they "
            "crucified God has made both Lord and Christ. Bright clear light on his "
            "grave features, empty sky behind. Ordinary tunic. Two hands, one head."
        ),
    },
    {
        "id": "v2-r044-b16", "out": "s16-the-words-began-to-land.jpeg", "seg": "s3",
        "window": "90.40-95.17", "wide": False, "jesus": False, "ref": REF,
        "locks": ["JERUSALEM-COURT"],
        "narration": "",
        "must_show": "the crowd receiving it: a band of upturned listening faces, the mockery gone, the first shock of realization moving across them — mouths parting, eyes widening, a hand rising to a chest.",
        "must_not_show": "no halo, glare or rim-light; no cream robes; no flames; no modern objects; genuine dawning grief, not panic.",
        "scene": (
            "Off Peter now and onto the crowd, a band of upturned faces filling the "
            "frame at their own level: the smirks are gone, and the first real shock of "
            "understanding is moving through them — a mouth falling open, eyes "
            "widening, a hand lifting toward a chest — ordinary people beginning to "
            "grasp what they have done and who he was. First-century dress, many "
            "nations. Every figure has two arms, two hands and one head."
        ),
    },
    # ---------------- n5 — cut to the heart, the only question ----------------
    {
        "id": "v2-r044-b17", "out": "s17-cut-to-the-heart.jpeg", "seg": "n5",
        "window": "95.17-101.70", "wide": False, "jesus": False, "ref": REF,
        "locks": ["JERUSALEM-COURT"],
        "narration": (
            "The words went straight through them. They had helped condemn him — and "
            "God had lifted him up anyway, and given him a throne over everything."
        ),
        "must_show": "pricked in the heart: two or three individual faces in the crowd broken open — one man's hand pressed hard to his own chest, another with eyes shut and head bowing, a woman's face wet — grief and conviction, not fear.",
        "must_not_show": "no halo, glare or rim-light; no cream robes; no throne or vision depicted; no flames; sorrow that is tender, never hysterical.",
        "scene": (
            "Close on two or three faces in the crowd, shot intimately among them: one "
            "man has pressed his hand hard flat against his own chest, head dropping; "
            "beside him another stands with his eyes squeezed shut; a woman's cheeks "
            "are wet — the words have gone straight through them, and it shows as "
            "grief and conviction, quiet and real. First-century dress. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r044-b18", "out": "s18-they-asked-the-only-question.jpeg", "seg": "n5",
        "window": "101.70-108.06", "wide": False, "jesus": False, "ref": REF,
        "locks": ["JERUSALEM-COURT"],
        "narration": (
            "Cut to the very heart, they asked the only question left to ask."
        ),
        "must_show": "a stricken man in the crowd stepping half a pace forward, both hands opening toward the steps, mouth mid-question, the people around him leaning in with the same need — the whole crowd's turn from resistance to asking.",
        "must_not_show": "no halo, glare or rim-light; no cream robes; no flames; the appeal earnest and humble; no modern objects.",
        "scene": (
            "One stricken man near the front has taken half a step out from the crowd, "
            "both hands opening toward the steps, his face broken and mouth caught "
            "mid-question — and the people pressed around him lean in with the very "
            "same need on their faces, shot low from just beside him so we feel the "
            "crowd's whole weight turning from resistance to asking. Bright morning, "
            "first-century dress. Every figure has two arms, two hands and one head."
        ),
    },
    # ---------------- s4 — what shall we do ----------------
    {
        "id": "v2-r044-b19", "out": "s19-men-and-brethren-what-shall-we-do.jpeg", "seg": "s4",
        "window": "108.06-111.35", "wide": False, "jesus": False, "ref": REF,
        "locks": ["JERUSALEM-COURT"],
        "narration": "Men and brethren, what shall we do?",
        "must_show": "a tight single of the man from the crowd calling it out — face lifted to the apostles, both hands half-raised open in genuine appeal, the plain human cry of what shall we do.",
        "must_not_show": "no halo, glare or rim-light; no cream robes; no flames; the man ordinary and humble, not angry.",
        "scene": (
            "A tight single on the man calling out, shot from just below his lifted "
            "face: chin up toward the apostles on the steps, both hands half-raised and "
            "open, his whole face one honest question — men and brethren, what shall we "
            "do — the sound of a heart that has finally given way. Ordinary tunic, "
            "bright light. Two hands, one head."
        ),
    },
    # ---------------- s5 — repent and be baptized ----------------
    {
        "id": "v2-r044-b20", "out": "s20-repent-and-be-baptized.jpeg", "seg": "s5",
        "window": "111.35-116.50", "wide": False, "jesus": False, "ref": REF,
        "locks": ["JERUSALEM-COURT", "PETER"],
        "narration": (
            "Repent, and be baptized every one of you in the name of Jesus Christ for "
            "the remission of sins,"
        ),
        "must_show": "Peter's answer as open welcome: leaning down toward the crowd from the steps, both hands opening outward in invitation, his face warm and certain — the door held open, not a scolding.",
        "must_not_show": "no halo, glare or rim-light; no cream robes; no flames; Peter warm and inviting, never harsh or pointing in accusation; ordinary-sized.",
        "scene": (
            "Peter leans down toward the crowd from the steps, both hands opening wide "
            "and outward in plain welcome, his weathered face warm and sure as he gives "
            "the answer — repent, and be baptized, every one of you — the whole gesture "
            "a door swung open rather than a finger raised. Shot from the crowd's side, "
            "upturned faces soft in the near frame. Bright morning, ordinary tunic. Two "
            "hands, one head."
        ),
    },
    {
        "id": "v2-r044-b21", "out": "s21-receive-the-gift-of-the-holy-ghost.jpeg", "seg": "s5",
        "window": "116.50-121.39", "wide": False, "jesus": False, "ref": REF,
        "locks": ["JERUSALEM-COURT", "PETER"],
        "narration": (
            "in the name of Jesus Christ, and ye shall receive the gift of the Holy "
            "Ghost."
        ),
        "must_show": "the promise: Peter's open hand turning gently from the crowd upward, offering the gift of the Holy Ghost — near listeners' faces lifting with the first hope; the same warm invitation completing.",
        "must_not_show": "no halo, glare or rim-light; no cream robes; NO flames or dove in the sky here (the gift is spoken, not depicted); no vision; Peter ordinary-sized.",
        "scene": (
            "Peter's open hand turns gently from the people upward, offering rather than "
            "commanding, as he promises the gift of the Holy Ghost — and in the near "
            "frame the faces of the listeners are lifting, the first hope breaking "
            "across them. Empty bright sky, nothing depicted in it. Shot from among the "
            "crowd. Ordinary tunic. Two hands, one head."
        ),
    },
    # ---------------- n6 — three thousand baptized, the church begins, the open door ----------------
    {
        "id": "v2-r044-b22", "out": "s22-three-thousand-baptized.jpeg", "seg": "n6",
        "window": "121.39-127.50", "wide": True, "jesus": False, "ref": REF,
        "locks": ["BAPTISM-WATER", "PETER"],
        "narration": (
            "About three thousand people were baptized that same day."
        ),
        "must_show": "an establishing wide of the Jerusalem baptism pool that same day: many, many people wading and being lowered into the water by the apostles, others waiting on the steps and the surrounds — a vast joyful multitude being baptized; Peter in the water.",
        "must_not_show": "no halo, glare or rim-light; no cream robes; no flames; a joyful, orderly multitude, not chaos; period dress; no modern objects.",
        "scene": (
            "A high establishing wide, the camera set back and above behind the waiting "
            "people so we look across their backs to the great stone pool: hundreds "
            "upon hundreds of people that same day wading into the clear water and "
            "being lowered gently under by the apostles, more streaming down the pale "
            "steps and crowding the surrounds — Peter waist-deep among them, a vast "
            "joyful multitude being baptized in the bright morning. A single unified "
            "photographic frame. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r044-b23", "out": "s23-the-church-began.jpeg", "seg": "n6",
        "window": "127.50-133.00", "wide": False, "jesus": False, "ref": REF,
        "locks": ["BAPTISM-WATER", "PETER"],
        "narration": (
            "The church of Jesus Christ began — not with an army or a building, but "
            "with the Spirit poured out and a crowd who had finally understood who he "
            "really was."
        ),
        "must_show": "the new church as ordinary people: a close, warm group of the newly baptized — wet-haired, faces shining, embracing one another and clasping the apostles' hands at the water's edge — the church as people, no army and no building.",
        "must_not_show": "no halo, glare or rim-light; no cream robes; no flames; no church building, no banners, no weapons; simply people; no modern objects.",
        "scene": (
            "Close and warm at the water's edge: a knot of the newly baptized, "
            "wet-haired and shining, embracing one another and gripping the apostles' "
            "hands — an older man weeping with relief, a young couple holding a child, "
            "Peter clasping a stranger's shoulder — the whole church of Jesus Christ in "
            "its first hour, and it is nothing but people. Bright morning, ordinary wet "
            "tunics. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r044-b24", "out": "s24-the-invitation-still-open.jpeg", "seg": "n6",
        "window": "133.00-138.00", "wide": False, "jesus": False, "ref": REF,
        "locks": ["BAPTISM-WATER"],
        "narration": "That same invitation is still open to you.",
        "must_show": "a quiet closing insert: a single hand reaching out to help another up the wet steps out of the pool — one person lifting another toward the light — the open invitation, held out to whoever is next.",
        "must_not_show": "no halo, glare or rim-light; no cream robes; no flames; no faces needed as the subject; simple and tender; no modern objects.",
        "scene": (
            "A quiet closing insert, shot low at the water's edge: one strong hand "
            "reaching down and closing warm around another person's hand to lift them "
            "up the last wet step out of the pool, toward the bright open morning — the "
            "gesture of a door held open, an invitation passed on to whoever is next. "
            "Water beading on skin, bright soft light, ordinary tunics. The hands and "
            "arms are whole and natural."
        ),
    },
]

# === PLACE-PLATES (v2_stash.py --promote writes these; empty until the runner
# promotes each new place's first good frame). UPPER-ROOM, JERUSALEM-COURT and
# BAPTISM-WATER are all NEW places with no stash plate yet — the runner generates
# each place's anchor beat first (b01, b08, b22), eyeballs it, and promotes it so
# the remaining beats of that place copy its architecture. ===
PLACE_REFS = {}
# === end PLACE-PLATES ===
