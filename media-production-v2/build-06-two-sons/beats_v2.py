#!/usr/bin/env python3
"""V2 beat map — row 6, build-06-two-sons (Matthew 21:28-32) — REALISTIC REBUILD.

Consumed by media-production-v2/v2_prompt.py (--check/--dump) and
media-production-v2/v2_gen_api.py (generation). STYLE-V2, the QUALITY LOCK, the
anti-panel clause and JESUS LOCK v5 are prepended by the assembler so they stay
byte-identical across every prompt.

REALISTIC REBUILD (Session 8, 2026-08-01). The 16 stills in `assets/` are the
2026-07-29 set that falls under the Session 6 blanket rejection of the old V2
look. They are kept untouched as ROUGH-DRAFT composition references while the
realistic set generates fresh at native 2K into `assets-realistic/`. Per the
Session 6 root-cause list, every beat states: the DIRECTION its light comes
from, a real-lens feel, people caught MID-ACTION rather than posed, the ONE
emotion the beat exists for, and that NOBODY looks at the camera.

THE COMPLAINT THIS REBUILD FIXES (Cameron, 2026-07-28, OPEN): "the father didnt
really ask either son anything and thats not how Jesus tsught it ... you cut
out the original thing the father asked the sons." Root cause: the 2026-07-24
REDO voiced the complete script (j28 the father's KJV ask, j29/j30 both sons'
KJV answers, n1b, n2b, j29b, s31 the crowd's KJV answer, n5b the modern-terms
publican/harlot line Cameron asked for in his QUEUE note) but the V1 build.py
BEATS list was never updated, so the assembled cut silently dropped them all.
The V1 build.py was fixed (assembly-only — every take already existed, nothing
re-voiced) and the V1 final rebuilt at 125.8 s. THIS beat map covers the full
fixed timeline: the ask, both answers, the repentance and the empty promise
each land on their own frame.

TIMING: windows computed 2026-08-01 from the fixed extract_beats.py against
the rebuilt V1 final — absolute audio phrase times, card at 112.99 s, total
125.79 s, matching the rebuilt V1 cut exactly.

COVERAGE (STORY-COVERAGE-LAW): 23 pictures over 125.8 s (~18 per 100 s,
the build-02 realistic density).

SCRIPTURE FACTS THAT GOVERN THE PICTURES (Matthew 21 KJV):
  21:23  the frame story is IN THE TEMPLE at Jerusalem — the chief priests and
         elders came to him AS HE WAS TEACHING. The great paved outer court.
  21:28  "Son, go work to day in my vineyard" — the father ASKS each son
         directly, face to face. The whole parable is one working day.
  21:29  the first son: "I will not: but afterward he REPENTED, and WENT."
  21:30  the second son: "I go, sir: and went NOT." He is not a villain — he
         is polite, likeable, sincere in the moment, and absent.
  21:31  Jesus asks; the crowd answers "The first"; the verdict lands on the
         leaders — "the publicans and the harlots go into the kingdom of God
         before you."

CONTENT-CARE: row 6 is GREEN. The D-flag restraint is applied voluntarily at
b21-b23, the only frames touching the word "harlots": the people Jesus names
are poor covered women and a tax collector at the court's outer margin, their
dignity intact. Nothing suggests the trade, nothing is sexualised.

TWO FATHERS, DELIBERATELY DIFFERENT: row 2's prodigal father is a dignified
landowner in deep indigo with a full silver beard. This father is a working
vinedresser — wiry, sun-scorched, short grizzled beard, dark olive tunic and a
leather apron. Two parables, two fathers.

TIME-OF-DAY ARC (self-consistent; one working day): temple frames = bright
mid-morning with real directional sun · the two asks and answers = low early
morning light · idle shade / the wrestle = hard mid-morning · the work = full
working daylight · the empty row and the one-hillside frame = long low late
afternoon. No night anywhere in this build.
"""

from pathlib import Path

OUTPUT_ASSET_DIR = "assets-realistic"
OUTPUT_VIDEO_NAME = "matthew-21_two-sons-realistic-v2.mp4"

# Identity anchors by IMAGE (CAST-BIBLE principle; row-2 CAST-DRIFT lesson —
# recurring men come back as different actors on text locks alone). Each
# recurring character has ONE canonical anchor; every beat naming his lock
# attaches it automatically.
REFS = {
    "FATHER": "CAST-REF-V2/father-ref.jpeg",
    "FIRST-SON": "CAST-REF-V2/first-son-ref.jpeg",
    "SECOND-SON": "CAST-REF-V2/second-son-ref.jpeg",
    "PRIESTS": "CAST-REF-V2/priests-ref.jpeg",
}

LOCKS = {
    # SETTING LOCKS NAME NO CHARACTER (STRAY-JESUS defect).
    "TEMPLE": (
        "TEMPLE LOCK: the great outer court of the temple at Jerusalem — a vast "
        "courtyard of worn pale limestone paving under open sky, a long colonnade of "
        "massive fluted stone columns running down one side, broad stone steps, and "
        "the huge dressed-stone facade of the temple rising beyond with its high "
        "gateway. Pilgrims and city people fill the court in SATURATED DEEP earth "
        "colours — dark chocolate brown, deep russet, burnt ochre, dark olive, dusty "
        "indigo and faded plum wool — each a distinct individual caught mid-gesture, "
        "never a posed row. No one in the crowd wears off-white, ivory or any "
        "near-white cloth, and no one in the crowd looks toward the camera."
    ),
    "VINEYARD": (
        "VINEYARD LOCK: a terraced hillside vineyard above a small stone farmhouse — "
        "dry-stone terrace walls stepping up the slope, long rows of low staked vines "
        "heavy with green leaf, a rough watchtower of piled stone at the top, dusty "
        "paths of pale earth between the rows, pruning hooks and reed baskets set "
        "about, dry Judean hills and olive terraces beyond."
    ),
    "PRIESTS": (
        "CHIEF PRIESTS LOCK: the chief priests and elders are the same four men in "
        "every shot — older men of settled authority, long carefully combed beards in "
        "grey and iron-grey, heavy brows, watchful unhurried eyes. They wear finely "
        "woven, DEEPLY DYED robes — NEAR-BLACK indigo and DARK UMBER with woven "
        "dark-red borders — and prayer shawls of that SAME saturated near-black and "
        "dark-indigo wool with dark stripes and dark fringe, plainly DARKER than the "
        "sunlit limestone around them. They stand together, still and composed. "
        "Their faces are shown clearly and none of them ever looks toward the camera."
    ),
    "FATHER": (
        "VINEDRESSER FATHER LOCK: the father is the same man in every shot — a "
        "working vine-grower of about fifty-five, wiry and sun-scorched, a SHORT "
        "grizzled iron-grey beard, close-cropped greying hair, deep crow's feet, "
        "big cracked working hands. He wears a DARK OLIVE-GREEN wool tunic with a "
        "worn leather apron and a plain leather belt, sleeves pushed back (never "
        "cream, never white). His face is shown clearly and he never looks toward "
        "the camera."
    ),
    # The first son's clothing does not change, but his HANDS do — clean at the
    # refusal, stained and cut by the day's end. That is stated per beat, not in
    # the lock, so the lock can never argue with a frame.
    "FIRST-SON": (
        "FIRST SON LOCK: the first son is the same young man in every shot — early "
        "twenties, stocky and strong-shouldered, thick dark curly hair, heavy dark "
        "brows over deep-set brown eyes, a short rough dark beard, a stubborn set to "
        "the jaw. He wears a faded RUST-BROWN work tunic with a rope belt and bare "
        "forearms (never cream, never white). He is plainly a DIFFERENT man from his "
        "taller, slighter, tidier brother. His face is shown clearly and he never "
        "looks toward the camera."
    ),
    "SECOND-SON": (
        "SECOND SON LOCK: the second son is the same young man in every shot — mid "
        "twenties, taller and slighter than his stocky brother, neatly trimmed dark "
        "beard, tidy dark hair, a pleasant open likeable face and easy manners. He "
        "wears a clean well-kept DUSTY-INDIGO tunic with a woven sash and good "
        "sandals (never cream, never white). His hands are clean and uncalloused. "
        "He is plainly a DIFFERENT man from his stocky curly-haired brother. His "
        "face is shown clearly and he never looks toward the camera."
    ),
    # Realistic-cinematography lock, byte-identical wherever named: the Session 6
    # rejection was flat noon light, posed extras and camera-gaze on every frame.
    "CAMERA": (
        "CAMERA LOCK: photographed like a real film still on location with a real "
        "cinema lens — light arrives from ONE believable direction and models "
        "faces with true shadow, shallow depth of field holds the subject sharp "
        "while the background falls gently away, and every person is caught "
        "mid-action in a truthful candid instant, never posed, never lined up, "
        "and NEVER looking at the camera."
    ),
}

REF = True

BEATS = [
    # ------------------------------------------- n0 — the temple frame story ----
    {
        "id": "v2-r006-b01", "out": "s01-he-told-it-to-them.jpeg", "seg": "n0 p1",
        "window": "0.28-5.81", "wide": True, "jesus": True, "ref": REF,
        "locks": ["CAMERA", "PRIESTS", "TEMPLE"],
        "narration": ("Jesus told this story to religious leaders — people who "
                      "were sure they had already said yes to God."),
        "must_show": "the temple court: Jesus teaching, and EXACTLY FOUR chief priests planted before him — all four fully visible, no more and no fewer — composed and entirely certain of themselves. The ONE emotion: their unshakable self-assurance meeting his calm.",
        "must_not_show": "no halo, glare or rim-light; Jesus is not detached at the frame edge — the priests and the nearby crowd face him; nobody looks at the camera; not flat noon light.",
        "scene": (
            "In the great outer court of the temple, mid-morning sun raking in low "
            "over the colonnade from one side so the columns throw long real shadows "
            "across the worn limestone paving, Jesus stands teaching, caught "
            "mid-sentence with one hand half-raised. Directly in front of him the "
            "four chief priests and elders stand together in their dark robes, arms "
            "folded or hands clasped, chins level, completely composed and sure of "
            "themselves, their eyes fixed on him — EXACTLY FOUR of them, every "
            "one of the four fully in view. Behind and around them ordinary "
            "city people have stopped mid-errand to listen — a man with a basket "
            "still on his shoulder, a woman half-turned — every face toward Jesus. "
            "The temple facade rises beyond, soft in the depth of field. The camera "
            "is back far enough to hold Jesus and the four men head to sandals. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r006-b02", "out": "s02-hear-themselves-in-it.jpeg", "seg": "n0 p2 + j28 p1",
        "window": "5.81-10.60", "wide": False, "jesus": True, "ref": REF,
        "locks": ["CAMERA", "PRIESTS", "TEMPLE"],
        "narration": ("He told it so they would hear themselves in it. / But what "
                      "think ye? (Matthew 21:28)"),
        "must_show": "Jesus opening the story straight at the priests — leaning slightly toward them, open storyteller's hand, warm and direct; the nearest priest's attention caught despite himself. The ONE emotion: a story aimed with love, not thrown.",
        "must_not_show": "no anger or challenge in his posture; no halo, glare or rim-light; nobody looks at the camera.",
        "scene": (
            "Closer now among the columns: Jesus mid-word, turned square toward the "
            "four priests, one open hand lifted in the easy manner of a man "
            "beginning a story he means someone to find themselves inside, his face "
            "warm, direct and unhurried. The nearest priest fills the soft edge of "
            "the frame in the shallow focus, his composed expression just beginning "
            "to attend despite itself. The low morning sun models one side of every "
            "face and leaves the other in true shadow. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    # -------------------------------------- j28 p2 — THE FATHER'S ASK (the fix) ----
    {
        "id": "v2-r006-b03", "out": "s03-go-work-in-my-vineyard.jpeg", "seg": "j28 p2",
        "window": "10.60-19.23", "wide": True, "jesus": False, "ref": False,
        "locks": ["CAMERA", "FATHER", "FIRST-SON", "VINEYARD"],
        "narration": ("A certain man had two sons; and he came to the first, and "
                      "said, Son, go work to day in my vineyard. (Matthew 21:28)"),
        "must_show": "THE ASK ITSELF — the father face to face with his first son, one big hand out toward the vine rows, genuinely asking; the son listening with his arms beginning to cross. The ONE emotion: a father's plain, hopeful request. This is the beat Cameron said was cut out — it must read as a real ask at a glance.",
        "must_not_show": "the son has NOT refused yet — no raised palm, no turned back; no anger anywhere; neither man looks at the camera.",
        "scene": (
            "Early morning at the edge of the terraced vineyard, the sun barely "
            "over the eastern ridge so long gold light rakes across the rows and "
            "dew still hangs on the leaves. The father stands face to face with "
            "his first son, caught mid-sentence, one big cracked hand stretched "
            "out toward the long rows of staked vines climbing the terraces behind "
            "him, his weathered face open and asking. The stocky young man stands "
            "listening, weight back on his heels, arms just beginning to fold "
            "across his chest, eyes on the rows his father points to — the answer "
            "not yet given. A pruning hook and a reed basket wait against the "
            "dry-stone wall beside them. Exactly two people are in the frame; each "
            "has two arms, two hands of five fingers each, two legs and one head."
        ),
    },
    {
        "id": "v2-r006-b04", "out": "s04-answered-him-flat.jpeg", "seg": "n1",
        "window": "19.23-23.66", "wide": False, "jesus": False, "ref": False,
        "locks": ["CAMERA", "FATHER", "FIRST-SON", "VINEYARD"],
        "narration": "A father told his first son: And the son answered him flat.",
        "must_show": "the instant before the no — tight on the first son's face gone hard, jaw set, eyes dropped away from his father; the father's outstretched hand still hanging in the ask. The ONE emotion: the refusal forming.",
        "must_not_show": "not shouting, not sneering — a young man closing a door; neither man looks at the camera.",
        "scene": (
            "A tight two-shot in the same low early-morning light: the first son's "
            "face fills one side of the frame in sharp shallow focus, his heavy "
            "brows drawn down, jaw clamped, eyes cut away toward the ground — the "
            "no already formed in his face before it is spoken — while past his "
            "shoulder, soft in the falloff of the lens, his father's outstretched "
            "hand still hangs open in the unanswered ask, the old man's face "
            "waiting behind it. The morning sun cuts across the son's cheek from "
            "one side and leaves the other dark. Exactly two people are in the "
            "frame; each visible hand has five fingers."
        ),
    },
    {
        "id": "v2-r006-b05", "out": "s05-i-will-not.jpeg", "seg": "j29",
        "window": "23.66-27.66", "wide": True, "jesus": False, "ref": False,
        "locks": ["CAMERA", "FATHER", "FIRST-SON", "VINEYARD"],
        "narration": "He answered and said, I will not. (Matthew 21:29)",
        "must_show": "A FLAT NO, readable with no words: the son already half turned away toward the farmhouse, flat open palm thrown up between them, face shut; the father's asking hand falling. The ONE emotion: the door shutting in a father's face.",
        "must_not_show": "no shouting, no shoving, no raised fist — a hard refusal, not a fight; nobody else in the frame; neither man looks at the camera.",
        "scene": (
            "The same vineyard edge a breath later, low morning sun from the east "
            "dragging both men's shadows long across the pale dust. The first son "
            "has already turned his shoulders and his whole body away toward the "
            "stone farmhouse, caught mid-step, and without looking back he has "
            "thrown up one flat open palm between himself and his father — the "
            "whole shape of him says no. His jaw is set, his eyes fixed on the "
            "ground ahead of him. The father's outstretched arm is just falling, "
            "his weathered face taking the refusal in silence. Exactly two people "
            "are in the frame; each has two arms, two hands of five fingers each, "
            "two legs and one head."
        ),
    },
    {
        "id": "v2-r006-b06", "out": "s06-just-no.jpeg", "seg": "n1b",
        "window": "27.66-32.47", "wide": True, "jesus": False, "ref": False,
        "locks": ["CAMERA", "FATHER", "FIRST-SON", "VINEYARD"],
        "narration": "I will not. No excuse offered, nothing softened. Just no.",
        "must_show": "the aftermath — the son walking away toward the farmhouse without a backward glance, the father left standing alone by the waiting rows. The ONE emotion: a no left hanging in the morning air.",
        "must_not_show": "the son's face is NOT visible — he is seen from behind, walking away; the father does not chase or call; neither man looks at the camera.",
        "scene": (
            "SHOT FROM BESIDE THE FATHER at the vineyard's edge: in the near "
            "ground, slightly soft, the old vine-grower stands still with his "
            "empty hands at his sides, watching — and down the dusty path ahead of "
            "his gaze the stocky first son walks away toward the stone farmhouse, "
            "SEEN FROM DIRECTLY BEHIND, the back of his curly head and his rust-"
            "brown shoulders to the camera, mid-stride, arms swinging loose, never "
            "once looking back. The long early light throws his shadow sideways "
            "across the path. The pruning hook and reed basket stand untouched "
            "against the wall. Exactly two people are in the frame; each has two "
            "arms, two hands, two legs and one head."
        ),
    },
    # ------------------------------------------------ n2 + j30 — the second son ----
    {
        "id": "v2-r006-b07", "out": "s07-he-went-to-the-second.jpeg", "seg": "n2",
        "window": "32.47-36.58", "wide": True, "jesus": False, "ref": False,
        "locks": ["CAMERA", "FATHER", "SECOND-SON", "VINEYARD"],
        "narration": "Then the father went to his second son and asked him the same thing.",
        "must_show": "the SAME ask happening again — the father mid-word before his second son at the farmhouse corner, the same hand out toward the same rows; the tidy son turning to him pleasantly. The ONE emotion: hope trying a second door.",
        "must_not_show": "the second son must NOT look sly or scheming — he is warm and attentive; neither man looks at the camera.",
        "scene": (
            "At the corner of the stone farmhouse a few minutes later, the morning "
            "sun still low from the east and warm on the stone, the father stands "
            "before his second son caught mid-ask, the same big cracked hand "
            "swung out toward the long vine rows climbing the terraces, his lined "
            "face hopeful. The taller, slighter young man in his clean dusty-"
            "indigo tunic has turned to his father with easy pleasant attention, "
            "head tipped, listening with a warm open face. Exactly two people are "
            "in the frame; each has two arms, two hands of five fingers each, two "
            "legs and one head."
        ),
    },
    {
        "id": "v2-r006-b08", "out": "s08-i-go-sir.jpeg", "seg": "j30",
        "window": "36.58-44.42", "wide": True, "jesus": False, "ref": False,
        "locks": ["CAMERA", "FATHER", "SECOND-SON", "VINEYARD"],
        "narration": ("And he came to the second, and said likewise. And he answered "
                      "and said, I go, sir: and went not. (Matthew 21:30)"),
        "must_show": "A COURTEOUS YES, readable with no words: the second son with his head bowed respectfully and one clean hand laid on his own heart, giving his word; the father's shoulders easing with relief. The ONE emotion: a promise that feels wonderful and costs nothing.",
        "must_not_show": "he must NOT look sly, smirking or deceitful — he is warm, likeable and completely sincere in the moment; that is what makes the story work; neither man looks at the camera.",
        "scene": (
            "The same farmhouse corner in the low golden morning light. The second "
            "son stands before his father with his head inclined in respect and "
            "one clean uncalloused hand laid flat on his own chest, giving his "
            "word, his pleasant face lifted in a warm agreeable smile — completely "
            "sincere in this moment. The father has half-relaxed, one hand come up "
            "in glad acknowledgement, the tightness going out of his shoulders, "
            "relief plain on his weathered face. Behind them the vine rows run "
            "away up the sunlit terraces, waiting. Exactly two people are in the "
            "frame; each has two arms, two hands of five fingers each, two legs "
            "and one head."
        ),
    },
    {
        "id": "v2-r006-b09", "out": "s09-and-didnt.jpeg", "seg": "n2b",
        "window": "44.42-47.99", "wide": True, "jesus": False, "ref": False,
        "locks": ["CAMERA", "SECOND-SON", "VINEYARD"],
        "narration": "Yes sir, that one said. I'm going. And didn't.",
        "must_show": "the promise dissolving — the second son comfortable in the shade doing nothing, his pruning hook and basket untouched against the wall, the vine rows waiting behind him. The ONE emotion: ease that has quietly let it go.",
        "must_not_show": "he is not sneering or gloating — he is simply at ease and has let it go; nothing suggests he decided against it, only that he never started; he does not look at the camera.",
        "scene": (
            "Later in the morning, the sun higher now and the farmhouse wall "
            "throwing one clean band of shade. The second son sits comfortably in "
            "that shade with his back against the warm stone, one knee up, a stem "
            "of grass idle in his clean fingers, entirely at ease and doing "
            "nothing at all, his gaze drifted somewhere down the valley. A pruning "
            "hook and an empty reed basket lean against the wall beside him "
            "exactly where they were left, the blade clean and unused — and beyond "
            "him, sharp in the raking light, the long rows of vines run up the "
            "terraces untouched and waiting. He has two arms, two hands of five "
            "fingers each, two legs and one head."
        ),
    },
    # ------------------------------------------ n2c — the no that wouldn't hold ----
    {
        "id": "v2-r006-b10", "out": "s10-it-kept-pulling-at-him.jpeg", "seg": "n2c",
        "window": "47.99-55.20", "wide": True, "jesus": False, "ref": False,
        "locks": ["CAMERA", "FIRST-SON", "VINEYARD"],
        "narration": ("The first son meant his no. But it wouldn't leave him alone. "
                      "All morning, the vineyard kept pulling at him."),
        "must_show": "the argument going on inside him: sitting apart on a terrace wall, arms folded hard, jaw set — but his head turned and his eyes dragged back to the vine rows. The ONE emotion: a no coming apart from the inside.",
        "must_not_show": "he is not sad or sorry yet; he is still stubborn — the tell is only that he cannot stop looking at the rows; he does not look at the camera; NO second person, NO part of any second person and NO animal appears anywhere in the frame or at any edge of it.",
        "scene": (
            "Hard mid-morning light now, the sun climbing so the shadows have "
            "shortened and the heat sits on the dust. The first son sits alone on "
            "a dry-stone terrace wall some way off from the vines, elbows on his "
            "knees, thick arms crossed hard in front of him, his jaw clamped and "
            "his mouth a flat line — a young man holding a position. But his head "
            "has turned away from where he meant to be looking, back toward the "
            "long rows of vines climbing the terraces, and his deep-set eyes are "
            "fixed on them, caught. A pruning hook lies in the dust at his feet "
            "where he dropped it. The rows stand sharp in the light beyond him. "
            "He is COMPLETELY ALONE on the hillside — no other person, no part "
            "or garment of any other person at any edge of the picture, and no "
            "animals. He has two arms, two hands of five fingers each, two legs "
            "and one head."
        ),
    },
    {
        "id": "v2-r006-b11", "out": "s11-he-repented-and-went.jpeg", "seg": "j29b",
        "window": "55.20-58.66", "wide": False, "jesus": False, "ref": False,
        "locks": ["CAMERA", "FIRST-SON", "VINEYARD"],
        "narration": "but afterward he repented, and went. (Matthew 21:29)",
        "must_show": "THE TURNING — caught mid-rise off the wall, weight already thrown forward, one hand pushing off the stone, the other reaching down for the dropped pruning hook, eyes gone to the rows. The ONE emotion: repentance as a physical movement.",
        "must_not_show": "not standing and not sitting — this frame exists only to catch the middle of the movement; nobody is watching him; he does not look at the camera.",
        "scene": (
            "Close on the first son CAUGHT MID-RISE from the terrace wall in the "
            "hard late-morning sun — his weight already thrown forward off the "
            "stone, one broad hand still pressing down on the wall behind him as "
            "he comes up, the other hand reaching down mid-grab for the pruning "
            "hook in the dust, dust already stirring at his feet. His head is up "
            "and turned toward the vine rows and his eyes have gone hard with "
            "decision, the stubbornness converted whole into resolve. The sun "
            "models his face from one side with true shadow. Each hand has five "
            "fingers."
        ),
    },
    {
        "id": "v2-r006-b12", "out": "s12-and-he-worked.jpeg", "seg": "n2d",
        "window": "58.66-66.10", "wide": True, "jesus": False, "ref": False,
        "locks": ["CAMERA", "FIRST-SON", "VINEYARD"],
        "narration": ("So he got up. And he went. No announcement, no apology. He "
                      "went back to the vineyard, and he worked."),
        "must_show": "him deep in the rows actually working — pruning hook mid-cut, sleeves back, sweat and vine sap, a filling basket, a stretch of finished rows behind him — and NOBODY in the frame to see him do it. The ONE emotion: obedience with no audience.",
        "must_not_show": "no father watching, no brother, no witness of any kind — the whole point is that he told nobody; he does not look at the camera.",
        "scene": (
            "Full working daylight, deep among the staked vines on the terrace, "
            "the high sun dappling hard light and leaf-shadow across everything. "
            "The first son is at work, caught mid-cut — one hand pulling a heavy "
            "leafy cane aside, the pruning hook biting in the other, his forearms "
            "scratched and streaked with dust and vine sap, dark sweat between "
            "the shoulders of his rust-brown tunic, his eyes on the cut. A reed "
            "basket behind him is already half filled, and a long stretch of rows "
            "behind him stands visibly finished and clean. There is no one else "
            "anywhere in the frame. The camera is back far enough to see him head "
            "to sandals among the rows. He has two arms, two hands of five "
            "fingers each, two legs and one head."
        ),
    },
    # ---------------------------------------------------- n3 — the empty row ----
    {
        "id": "v2-r006-b13", "out": "s13-the-row-stayed-empty.jpeg", "seg": "n3 p1",
        "window": "66.10-69.09", "wide": True, "jesus": False, "ref": False,
        "locks": ["CAMERA", "VINEYARD"],
        "narration": "The row the second son promised to work stayed empty all day.",
        "must_show": "the untouched row at day's end — overgrown unpruned vines, the clean unused pruning hook and empty basket still leaning where they were left, long low shadows, nobody there. The ONE emotion: a promise visible as an absence.",
        "must_not_show": "no people at all in this frame; do not make it sinister — just a job not done.",
        "scene": (
            "Late afternoon, the low golden sun raking in from the west so every "
            "stake and sprawling cane drags a long shadow down the terrace. One "
            "long row of vines stands untouched and overgrown — canes sprawling "
            "off their stakes, dead wood still on the vines, the pale earth "
            "between them unbroken by any footprint. At the head of the row a "
            "clean unused pruning hook and an empty reed basket lean against the "
            "dry-stone wall exactly where they were set down that morning, their "
            "shadows stretched long. There is not a single person in the frame."
        ),
    },
    {
        "id": "v2-r006-b14", "out": "s14-he-asked-the-crowd.jpeg", "seg": "n3 p2",
        "window": "69.09-72.71", "wide": True, "jesus": True, "ref": REF,
        "locks": ["CAMERA", "PRIESTS", "TEMPLE"],
        "narration": "Then Jesus asked the crowd a question.",
        "must_show": "back in the temple court — Jesus turning from the priests to put a question to the wider crowd, heads coming up all around. The ONE emotion: the whole court being drawn into the verdict.",
        "must_not_show": "no halo, glare or rim-light; he is among the people, not standing apart at the frame edge; nobody looks at the camera.",
        "scene": (
            "Back in the bright temple court, the mid-morning sun still raking "
            "shadow off the colonnade. Jesus is seen from the side in "
            "three-quarter profile, turned away from the four chief priests "
            "toward the wider crowd ACROSS the court, caught mid-turn with one "
            "hand lifting to put the question to them — his eyes are on those "
            "people, his gaze aimed clearly PAST the camera at the crowd he is "
            "asking, never toward the lens — and heads are coming up all "
            "across the court — a water-seller pausing mid-pour, two pilgrims "
            "turning in mid-step. The four priests stand off to one side in their "
            "dark robes, still composed, watching. The columns and the temple "
            "facade rise soft beyond the shallow focus. The camera holds Jesus, "
            "the priests and the near crowd head to sandals. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r006-b15", "out": "s15-whether-of-them-twain.jpeg", "seg": "j1",
        "window": "72.71-76.60", "wide": False, "jesus": True, "ref": REF,
        "locks": ["CAMERA", "TEMPLE"],
        "narration": "Whether of them twain did the will of his father? (Matthew 21:31)",
        "must_show": "close on Jesus asking it — open hand, level and unhurried, genuinely waiting for their answer. The ONE emotion: a real question, honestly asked.",
        "must_not_show": "no halo, glare or rim-light; no trap in his face — the question is asked plainly and he means it; he does not look at the camera.",
        "scene": (
            "Close on Jesus in the sunlit temple court, mid-question, one hand "
            "open and lifted in front of him, his head slightly tilted as he "
            "waits, his eyes on the men he is asking. His face is calm, unhurried "
            "and completely open — a man who has asked a real question and is "
            "willing to stand in the silence for its answer. The morning sun "
            "models his face from one side. The blurred shapes of the crowd and "
            "the massive pale columns are soft behind him in the shallow depth of "
            "field. His hand has five fingers."
        ),
    },
    # ----------------------------------------- n4 + s31 — what they finally DID ----
    {
        "id": "v2-r006-b16", "out": "s16-what-they-finally-did.jpeg", "seg": "n4 p1",
        "window": "76.60-80.73", "wide": True, "jesus": False, "ref": False,
        "locks": ["CAMERA", "FIRST-SON", "VINEYARD"],
        "narration": ("He was asking: which of the two actually did what his "
                      "father wanted?"),
        "must_show": "ONE CONTINUOUS VIEW at day's end holding both outcomes: the first son straightening up tired at the end of his finished rows, and further along the same hillside the one row still overgrown and untouched. The ONE emotion: the day itself giving the answer.",
        "must_not_show": "NOT a split screen, NOT a before-and-after pair, NOT two panels — one single hillside seen in one shot, with both things in it; he does not look at the camera.",
        "scene": (
            "ONE SINGLE CONTINUOUS UNBROKEN PHOTOGRAPH — one camera position, "
            "one moment, one frame filling the whole picture edge to edge with "
            "no horizontal seams — a view across the terraced hillside in long "
            "late-afternoon light, the low sun gilding the dust. In the near "
            "ground the first son straightens up from the last of his work, "
            "caught mid-stretch with one hand pressed to the small of his back, "
            "his forearms filthy and scratched, the rows behind him pruned clean "
            "and their cut wood stacked. Further along the same slope, "
            "unmistakably part of the same hillside and the same moment, the "
            "second son's row stands sprawling and overgrown with its clean "
            "tools still leaning at the head of it. No dividing line and no "
            "second frame — one hillside, one photograph. He has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r006-b17", "out": "s17-the-first.jpeg", "seg": "n4 p2 + s31",
        "window": "80.73-86.40", "wide": True, "jesus": True, "ref": REF,
        "locks": ["CAMERA", "PRIESTS", "TEMPLE"],
        "narration": ("And the crowd answered him. / They say unto him, The first. "
                      "(Matthew 21:31)"),
        "must_show": "the crowd answering — an ordinary working man speaking up mid-word with his hand half raised, heads nodding around him, Jesus facing them listening, unsurprised. The ONE emotion: an answer so obvious the whole court says it.",
        "must_not_show": "no halo or rim-light on Jesus; nobody is arguing — this is the easy part and their faces show it; nobody looks at the camera.",
        "scene": (
            "In the temple court the crowd have answered. An ordinary weathered "
            "working man near the front has spoken up, caught mid-word with his "
            "hand half lifted, and all around him the answer ripples — a woman "
            "saying it to her neighbour behind her hand, an old man gesturing as "
            "if it hardly needed asking, two heads nodding at once. Jesus stands "
            "facing them, listening, unsurprised, the light warm on the side of "
            "his face. The four priests hold their dark knot at the edge of the "
            "crowd. The whole court has the look of a question that answered "
            "itself. The camera holds the near crowd and Jesus head to sandals. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    # ------------------------------------------ n5 — it turns on the leaders ----
    {
        "id": "v2-r006-b18", "out": "s18-their-own-answer.jpeg", "seg": "n5 p1-p2",
        "window": "86.40-89.52", "wide": False, "jesus": False, "ref": False,
        "locks": ["CAMERA", "PRIESTS", "TEMPLE"],
        "narration": "The first one, they said. The one who started with no.",
        "must_show": "the four priests' faces close, as the answer they just heard turns around on them — the certainty cracking, one working it out, one already stiffening. The ONE emotion: the floor shifting under certain men.",
        "must_not_show": "do not put Jesus in this frame; no cartoon outrage — the change is small and internal and shows mostly in the eyes; none of them looks at the camera.",
        "scene": (
            "Close on the four chief priests and elders standing together in "
            "their dark robes in the sunlit court, the morning light cutting "
            "across their faces from one side. The composure is coming apart by "
            "degrees — the nearest man's eyes have narrowed and slid sideways as "
            "he works out where the story has gone, the one behind him has gone "
            "very still with his mouth pressed shut, a third has begun to "
            "stiffen and lift his chin, and the fourth is looking at the paving. "
            "Not one of them is looking at anyone. The pale columns stand soft "
            "behind them in the shallow focus. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r006-b19", "out": "s19-he-turned-to-them.jpeg", "seg": "n5 p3",
        "window": "89.52-95.24", "wide": True, "jesus": True, "ref": REF,
        "locks": ["CAMERA", "PRIESTS", "TEMPLE"],
        "narration": ("Then he turned to the religious leaders — the ones who were "
                      "sure they were the second son."),
        "must_show": "Jesus turning bodily away from the crowd to face the four priests directly, the people falling back to leave open paving between them. The ONE emotion: the story arriving at its address.",
        "must_not_show": "no halo, glare or rim-light; no anger in his posture — he is squared up and steady, and the crowd is not being used against them; nobody looks at the camera.",
        "scene": (
            "Jesus has turned his whole body away from the crowd to face the "
            "four chief priests and elders directly across a clear stretch of "
            "sunlit limestone paving, caught at the end of the turn, his posture "
            "steady and unhurried, one hand loose at his side. The people "
            "nearest have drawn back on both sides mid-step, opening the ground "
            "between him and the four men, and gone quiet — a hush you can see. "
            "The priests stand shoulder to shoulder in their dark robes holding "
            "their position, faces guarded, the low sun modelling every face "
            "from the same side. The colonnade runs away behind them. The "
            "camera holds Jesus and all four men head to sandals. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    # ---------------------------------------------------------- j2 — verdict ----
    {
        "id": "v2-r006-b20", "out": "s20-verily-i-say.jpeg", "seg": "j2 p1a",
        "window": "95.24-99.60", "wide": False, "jesus": True, "ref": REF,
        "locks": ["CAMERA", "TEMPLE"],
        "narration": ("Verily I say unto you, That the publicans and the harlots "
                      "go into the kingdom of God (Matthew 21:31)"),
        "must_show": "close on Jesus saying it directly to them — level, certain, entirely without cruelty. The ONE emotion: truth spoken plainly, costing the hearer everything.",
        "must_not_show": "no halo, glare or rim-light; no scorn or triumph on his face; this is told as plain fact, not as a taunt; he does not look at the camera.",
        "scene": (
            "Close on Jesus in the bright temple court, mid-word, speaking "
            "straight ahead at the men in front of him, the morning sun firm on "
            "one side of his face and true shadow on the other. His face is "
            "level and certain and there is no cruelty anywhere in it — no scorn "
            "in the mouth, no heat in the eyes, only a man saying something true "
            "that costs the hearer everything. The blurred dark shapes of the "
            "listening priests stand at the very edge of the frame and the "
            "sunlit limestone falls soft behind him."
        ),
    },
    {
        "id": "v2-r006-b21", "out": "s21-the-ones-he-meant.jpeg", "seg": "j2 p1b",
        "window": "99.60-102.86", "wide": True, "jesus": False, "ref": False,
        "locks": ["CAMERA", "TEMPLE"],
        "narration": "before you. (Matthew 21:31)",
        "must_show": "the people he is talking about, at the far outer margin of the court — a tax collector at his small table and two poor women standing back near the colonnade, listening from a distance. The ONE emotion: unwelcome people hearing themselves welcomed.",
        "must_not_show": "CONTENT-CARE: nothing whatever suggests the women's trade, nothing is sexualised, no jewellery, paint or bare shoulders — they are poor, covered, ordinary and dignified. Nobody is shown shaming them. Do not put Jesus in this frame; nobody looks at the camera.",
        "scene": (
            "At the far outer edge of the temple court, back in the long shade "
            "of the colonnade where people who feel unwelcome stand, the light "
            "reaching them only as a warm bounce off the sunlit paving beyond. "
            "A tax collector sits at a small wooden table with his coin box and "
            "tally, half turned on his stool mid-listen, his stylus forgotten in "
            "his hand. A few steps from him two poor women stand close together "
            "against a column, heads and shoulders covered by worn dark shawls, "
            "their plain mended robes drawn about them, hands folded — holding "
            "very still, their tired faces lit with something careful that is "
            "almost hope. Nobody is speaking to them and nobody is driving them "
            "off. Far across the sunlit paving behind them the crowd is a "
            "distant blur in the shallow focus. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    # ------------------------------------------- n5b — the verdict in plain words ----
    {
        "id": "v2-r006-b22", "out": "s22-going-in-ahead-of-you.jpeg", "seg": "n5b p1-p2",
        "window": "102.86-109.13", "wide": True, "jesus": False, "ref": False,
        "locks": ["CAMERA", "TEMPLE"],
        "narration": ("The tax collectors and the worst-thought-of people in town "
                      "are going in ahead of you. Not because their lives were "
                      "tidier."),
        "must_show": "the outsiders drawn a few steps out of the shade toward the teaching — the tax collector risen halfway off his stool, one woman a step forward from the column, faces open. The ONE emotion: hope daring to move.",
        "must_not_show": "same CONTENT-CARE as the previous frame — covered, dignified, nothing sexualised; no Jesus in the frame and NO distinguishable distant figure that could read as him — the far court is only an indistinct blur; nobody looks at the camera.",
        "scene": (
            "The same outer margin of the court a moment later: the tax "
            "collector has risen halfway off his stool, one hand still on his "
            "little table, his body already leaning toward the far side of the "
            "court where the teaching is happening OUT OF THIS FRAME — and the "
            "nearer of the two covered women has "
            "taken one small step out of the colonnade's shade into the edge of "
            "the sunlight, her shawled head lifted, her companion's hand still "
            "on her arm. Their tired faces are open, listening, lit by the warm "
            "bounce off the paving. The far side of the court is an INDISTINCT "
            "soft blur of colour in which no single figure can be made out — no "
            "distant teacher, no pale-robed figure, nobody recognisable. "
            "Every figure has two arms, two hands of five fingers each and one "
            "head."
        ),
    },
    {
        "id": "v2-r006-b23", "out": "s23-they-turned-and-went.jpeg", "seg": "n5b p3",
        "window": "109.13-112.99", "wide": True, "jesus": False, "ref": False,
        "locks": ["CAMERA", "FIRST-SON", "VINEYARD"],
        "narration": ("Because when they finally heard, they turned around and "
                      "went."),
        "must_show": "the story's own picture of turning: the first son at golden hour, seen from behind mid-stride WALKING INTO the vine rows with the pruning hook over his shoulder — the refusal reversed into going. The ONE emotion: it is the turning that counts.",
        "must_not_show": "his face is not visible — he is walking away from the camera INTO the rows; nobody else in the frame; not sunset-red melodrama, just late gold light.",
        "scene": (
            "Late golden afternoon in the vineyard, the low sun ahead and to one "
            "side so the vine rows are edged in warm gold and the dust hangs "
            "bright where his heels kick it. SEEN FROM DIRECTLY BEHIND, the "
            "stocky first son walks away from the camera INTO the long green "
            "corridor of staked vines, mid-stride, the pruning hook balanced "
            "over one shoulder and the reed basket swinging from his other hand, "
            "his rust-brown tunic warm in the light — a man who said no, going. "
            "The row swallows him a step at a time; his face is entirely hidden "
            "because he is facing away up the row. Exactly one person is in the "
            "frame, with two arms, two hands, two legs and one head."
        ),
    },
]

# ROUGH-DRAFT CONTINUITY (the storm-11 pattern): the rejected-look still for a
# beat, when a matching one exists, is attached as the approved rough draft —
# its camera angle, blocking and travel directions were bought with the row-6
# authoring pass and must not be reinvented. Faces and identity always come
# from the FACE/CHARACTER lock images, never from the draft. New beats born of
# the complaint fix (the ask, the answer forming, the walk-away, the second
# ask, the outsiders moving, the closing turn) have no rough by design — and
# b03/b04 deliberately get none because the only old frame of the ask (old
# s02) already contains the refusal, the exact defect those beats must not
# copy (the prodigal b20 lesson: a rough carries its defects faithfully).
_ROUGH_BY_BEAT = {
    "v2-r006-b01": "s01-he-told-it-to-them.jpeg",
    "v2-r006-b05": "s02-i-will-not.jpeg",
    "v2-r006-b08": "s03-i-go-sir.jpeg",
    "v2-r006-b09": "s04-it-never-became-obedience.jpeg",
    # b10's rough (old s05) DROPPED after reroll QC: the rough itself contains
    # a partial figure at the frame edge, background field workers and a
    # near-camera gaze, and the first realistic take copied those defects
    # faithfully (prodigal b20 lesson).
    "v2-r006-b11": "s06-so-he-got-up.jpeg",
    "v2-r006-b12": "s07-and-he-worked.jpeg",
    "v2-r006-b13": "s08-the-row-stayed-empty.jpeg",
    "v2-r006-b14": "s09-a-question-for-the-crowd.jpeg",
    "v2-r006-b15": "s10-whether-of-them-twain.jpeg",
    # b16's rough (old s11) DROPPED after reroll QC: the rough is ITSELF a
    # three-panel triptych, and the first realistic take reproduced the panel
    # structure complete with a dissolving figure.
    "v2-r006-b17": "s12-the-crowd-knew.jpeg",
    "v2-r006-b18": "s13-their-own-answer.jpeg",
    "v2-r006-b19": "s14-he-turned-to-them.jpeg",
    "v2-r006-b20": "s15-before-you.jpeg",
    "v2-r006-b21": "s16-the-ones-he-meant.jpeg",
}
for _beat in BEATS:
    _name = _ROUGH_BY_BEAT.get(_beat["id"])
    if _name:
        _asset = Path(__file__).resolve().parent / "assets" / _name
        if _asset.is_file():
            _beat["rough_ref"] = str(_asset)
