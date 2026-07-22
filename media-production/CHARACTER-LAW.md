# CHARACTER LAW (Cameron, 2026-07-21)

**No character is ever imagined twice.** Every prominent scripture figure has ONE
locked reference sheet, and every image that shows them is conditioned on it.
Cameron's words: *"I don't want to have to continuously fight the AI making
pictures for a story and then it not keeping the people looking the same at all."*

## The rules

1. **One character, one sheet, forever.** Each character gets a folder in
   `media-production/CHARACTERS/<name>/` holding a reference sheet: face front,
   face 3/4 profile, full body in standard garments — same person in all three.
   Jesus's existing ref stays where it is (`JESUS-MASTER-REF/jesus-face.jpeg`,
   face-law v3) and is the model for how locked a ref is. God the Father is
   governed by `GOD-THE-FATHER-LOCK.md` — embodied, glorified, consistent.
2. **Scripture first.** Where the text describes a person, the sheet obeys it
   (David: ruddy, beautiful countenance — 1 Sam 16:12. Zacchaeus: little of
   stature — Luke 19:3. John the Baptist: camel's hair, leather girdle — Matt
   3:4. Jesus: no beauty that we should desire him — Isa 53:2). Where scripture
   is silent, the default is **historically accurate Middle Eastern** for the
   period — first-century Judean for the NT, correct era for OT figures. Age,
   build, and bearing must fit the role (fishermen look like men who haul nets).
3. **Every prompt attaches the ref.** Any image prompt that includes a rostered
   character MUST condition on their sheet (Flow/Gemini master-ref) AND describe
   them from the sheet's written spec — never from imagination. A still whose
   character drifts from the sheet is a defect, same class as a wrong caption.
4. **New face → ref first.** If a story introduces a character not yet in the
   roster, build their sheet BEFORE generating story stills.
5. **Refs are locked.** Changing a sheet requires Cameron's explicit approval.
   Each character folder gets a `SPEC.md`: scripture citations, written
   description, generation prompt, and the date Cameron approved it.
6. **Each sheet needs Cameron's approval before it's marked locked.**
7. **A character shown at more than one age gets a sheet per age.** See the
   AGE-VARIANT KEY below. Never age a character by imagination inside a story
   prompt — if the beat needs him older or younger than his prime sheet, that
   stage needs its own sheet first (rule 4 applies to stages, not just faces).

---

# AGE-VARIANT KEY (Cameron, 2026-07-21)

*"A key for any other figures that are made into videos in their older years so
they don't get confused."*

Some figures live across decades on screen — the boy Samuel and the prophet
Samuel, Jacob fleeing and Jacob dying, Saul holding the coats and Paul writing
the epistles. Left alone, the image model paints them as unrelated strangers.
The key below makes every stage a first-class, locked sheet that still reads as
one person.

## Stage names (use these exact words — nothing else)
| Stage key | Means |
|---|---|
| `infant` | newborn to about two years |
| `child` | roughly three to twelve |
| `youth` | teens to early twenties |
| `prime` | the age the character is in MOST of his stories — **this is the base sheet** and carries no suffix |
| `aged` | visibly old: white or grey hair, lined skin, stooped or slowed |
| `glorified` | a resurrected, translated, or heavenly appearance |
| `risen` | reserved for Jesus after the Resurrection |

## How a variant is built
1. **The prime sheet comes first.** It is the base; every other stage is
   derived FROM it, never invented beside it.
2. **Folder name is `<stage>-<name>`** — `young-jesus`, `infant-jesus`,
   `risen-jesus`, `aged-abraham`, `child-samuel`. The prime sheet keeps the
   plain name (`abraham`, `samuel`, `jesus` → JESUS-MASTER-REF).
3. **Every variant prompt attaches the prime sheet as a `--ref`**, and the
   prompt says in words: *paint the SAME person at <age>*. A variant generated
   without the prime sheet attached is void — reroll it.
4. **Continuity anchors are mandatory.** Every variant SPEC.md carries a
   "Continuity anchors" line listing the 3–5 features that do NOT change with
   age: skin tone, eye color, facial structure, nose, any named scripture
   feature (David ruddy, Elisha bald). These are identical across every stage.
5. **Only these may change with age:** hair color and length, beard, skin
   texture and lines, build, posture, bearing, and garments appropriate to
   their station at that time.
6. **PROMPTS.md names the stage per shot.** A story spanning years must say
   which sheet each still uses and where it switches, so nobody has to guess.
7. **Cameron approves each stage separately.** An approved prime sheet does not
   auto-approve its variants.

## FINAL age-variant worklist (Cameron 2026-07-21, from the all-200 scan)

Built by `tools/char_story_map.py`, which reads each build's PROMPTS.md +
gen_stills_flow.py through `character_refs.find_in_text` with scripture
citations stripped (a "John 3:16" names a book, not a man standing in the shot).
**Story numbers below are the videos whose stills must be REDONE** once the
stage sheet exists — that is the redo trigger, not a suggestion.

| Character | Stage to build | Story numbers to redo | Why the stage differs |
|---|---|---|---|
| **Jesus** | `infant` | **84, 85, 86** | Luke 2:7 swaddled newborn in the manger (84, 85); Matt 2:11 "the young child" in a house, 1–2 years old (86). Two sub-stages — see `CHARACTERS/infant-jesus/SPEC.md`. |
| **Jesus** | `risen` | **97, 98, 99, 100, 134, 154, 179, 189** | Luke 24:39 flesh and bone with the wound marks; every post-Resurrection beat. `CHARACTERS/risen-jesus/SPEC.md`. |
| **Mary (mother)** | `youth` | **84, 85, 86, 87** | A young mother at the nativity and still young at the temple visit — she is decades younger here than at Cana (#49), which uses her prime sheet. |
| **John (beloved)** | `aged` | **154, 174, 189** | The Revelation beats are written by the old apostle on Patmos; the same face as the young fisherman of #51/#71 but sixty years on. |
| **Moses** | `glorified` | **67** | At the Transfiguration he appears from beyond death in glory — not the Sinai elder of #105/#177/#196. |
| **Elijah** | `glorified` | **67, 174** | Translated, not aged: the Transfiguration and the Mal 4 return promise. His prime sheet covers #101. |
| **Abraham** | `aged` | **115, 190** | Gen 22 puts him past 115 with Isaac grown — visibly older than the man arguing for Sodom at 99 (#114). |
| **Abraham** | `glorified` | **37** | In the rich man's parable he is seen in paradise, not on earth. |
| **Isaac** | `youth` | **115, 190** | The son carrying the wood is a young man, not the child or the later patriarch. |
| **Jacob** | `youth` | **102** | The ladder is Jacob fleeing Esau as a young man; his prime sheet is the elder. |
| **Samuel** | `child` | **104, 149** | 1 Sam 3 is a boy ministering before Eli — a child sheet, not the prophet. |
| **Peter** | `aged` | **172, 197** | The Pentecost/epistle beats are the elder apostle, not the fisherman of #7/#51. |
| **Paul** | `youth` (as Saul) | **179** *(only if the Acts 7:58 coat-holder beat is added)* | The young man consenting to Stephen's death is the same face as the apostle of #184/#186. |

Everything else on the roster appears at ONE life stage across all 200 and needs
no variant — their locked prime sheet already governs every shot they're in.

**Redo scope: 22 videos** — 37, 67, 84, 85, 86, 87, 97, 98, 99, 100, 102, 104,
115, 134, 149, 154, 172, 174, 179, 189, 190, 197. Every still in these that
shows the character at the stage named above gets regenerated against the new
sheet. Approved-locked cuts among them go to FIX-LATER instead of being
overwritten (approved-lock law still outranks this).

## Figures confirmed to need age variants (from the 200)
| Character | Stages needed | Where they diverge |
|---|---|---|
| **Jesus** | `infant`, `young` (12), **prime**, `risen` | #84/#85/#86 babe → #87 boy → ministry → #97/#98/#99/#100/#134/#179 |
| **Abraham** | **prime**, `aged` | #114 arguing for Sodom (~99) → #115 the ram in the thicket, Isaac a youth |
| **Isaac** | `youth`, **prime** | #115 the binding → later patriarch |
| **Jacob** | `youth`, **prime**, `aged` | #102 the ladder, fleeing → #147 dying in Egypt |
| **Joseph of Egypt** | `youth`, **prime** | sold at seventeen → vizier in #147 |
| **Samuel** | `child`, **prime** | #104 the boy who hears his name → the prophet |
| **David** | `youth`, **prime** | shepherd boy → the king who writes #150 / #176 |
| **Moses** | **prime**, `glorified` | #105/#177 Sinai → #67 the Transfiguration |
| **Elijah** | **prime**, `glorified` | #101 the still small voice → #67 the Transfiguration |
| **John (beloved)** | **prime**, `aged` | the young disciple → the old apostle of #154 / #189 |
| **Paul** | `youth` (as Saul), **prime** | the young man at Stephen's stoning (Acts 7:58) → the apostle of #184 / #186 |
| **God the Father** | `glorified` only | he has one appearance — `GOD-THE-FATHER-LOCK.md` |
| **Noah, Sarah, Naomi, Eli** | `aged` is their **prime** | they appear old in every story they're in — no second stage needed |

The character session finalizes this table after scanning all 200 PROMPTS.md;
anything it adds gets appended here, not kept in a session note.

## Roster (FINAL — locked by the character session, 2026-07-21, after scanning
## all 201 build PROMPTS.md + QUEUE.md + the name harvest)

**Locked already:** Jesus (JESUS-MASTER-REF), God the Father (SPEC in
GOD-THE-FATHER-LOCK.md; sheet render below).

**New Testament (31):** Peter, John (beloved), James (son of Zebedee), Andrew,
Matthew, Thomas, Judas Iscariot, John the Baptist, Mary (mother of Jesus),
Joseph of Nazareth, Mary Magdalene, Martha, Mary of Bethany, Lazarus,
Zacchaeus, Nicodemus, Pilate, Stephen, Paul, **Bartimaeus (#12), Jairus (#57),
Cleopas (#18), Barabbas (#93), Zebedee (#51/#71), Malchus (#66),
Simon the Pharisee (#74)** — the bolded seven were added by the scan: each is a
named on-screen story lead — plus the five apostles added 2026-07-21 to
complete the Twelve: **Philip, Bartholomew (Nathanael), James (son of
Alphaeus), Thaddaeus (Lebbaeus / Judas not Iscariot), Simon the Zealot.**

### THE TWELVE (Cameron, 2026-07-21: "we need all the disciples all 12 so we
### can use their faces in scenes")

All twelve apostles now have sheets, so a group scene is cast from the roster
instead of invented: `character_refs.twelve()` returns them in gospel order —
Peter, Andrew, James, John, Philip, Bartholomew, Matthew, Thomas, James son of
Alphaeus, Thaddaeus, Simon the Zealot, Judas Iscariot. Every one has a
different tunic colour, age and hair so twelve men in one frame read as twelve
different people:

| Apostle | Age | Tunic (locked) | Told apart by |
|---|---|---|---|
| Peter | ~35 | blue-grey | thick dark curls, full beard, broadest build |
| Andrew | ~30 | olive-drab | Peter's leaner younger brother |
| James (Zebedee) | ~25 | dark ochre-brown | short dark beard, solid |
| John (beloved) | ~20 | faded grey-blue | youngest, CLEAN-SHAVEN |
| Philip | ~32 | sand-tan | the only SANDY LIGHT-BROWN head |
| Bartholomew | ~45 | deep forest-green | eldest; silver-streaked, broadest beard |
| Matthew | ~40 | muted teal-green | finer cloth, city-kept, trimmed beard |
| Thomas | ~35 | indigo-charcoal | straight black hair to the jaw |
| James (Alphaeus) | ~30 | neutral stone-grey | SHORTEST of the twelve (Mark 15:40) |
| Thaddaeus | ~28 | mustard-gold + rust sash | CHESTNUT curly hair |
| Simon the Zealot | ~35 | oxblood-maroon | black hair tied back, lean and watchful |
| Judas Iscariot | ~35 | dark russet | ordinary and respectable — never sinister |

Three men in the gospels are called Simon and two are called James and two are
called Judas. In a prompt, write them out in full ("Simon the Zealot," "James
the son of Alphaeus," "Thaddaeus") — `character_refs` resolves every scriptural
alias (Nathanael, Zelotes, Lebbaeus, "Judas not Iscariot"), but bare "Simon" is
deliberately ambiguous and will not resolve.

**Old Testament (35):** Adam, Eve, Noah, Abraham, Sarah, Isaac, Jacob,
Joseph (of Egypt), Moses, Elijah, Elisha, Eli, Samuel, Hannah, David, Ruth,
Naomi, Boaz, Job, Jonah, Daniel, Shadrach, Meshach, Abednego, Nebuchadnezzar,
Naaman, Isaiah, Jeremiah, Ezekiel, Hosea, **Aaron (#161), Joshua (#196),
Gomer (#117), Joel (#197), Malachi (#174/#191)** — added by the scan.

**Variant sheets (Jesus has four stages — see the AGE-VARIANT KEY above):**
| Stage | Folder | Used in | Status |
|---|---|---|---|
| `infant` | `CHARACTERS/infant-jesus` | #84, #85, #86 | 🟡 SPEC written 2026-07-21 — **needs rendering + Cameron's approval** |
| `young` (boy ~12) | `CHARACTERS/young-jesus` | #87 | 🔒 LOCKED |
| **prime** (ministry) | `JESUS-MASTER-REF` | most of the 200 | 🔒 LOCKED (face-law v3) |
| `risen` (glorified) | `CHARACTERS/risen-jesus` | #97, #98, #99, #100, #134, #179, #154, #189 | 🟡 SPEC written 2026-07-21 — **needs rendering + Cameron's approval** |

Every one must read as the SAME person as JESUS-MASTER-REF, features scaled to
the stage. Other figures needing age variants are tabled in the AGE-VARIANT KEY.

**Scanned and EXCLUDED (named but one background still only, no recurrence —
in-build consistency lock suffices):** Peninnah (#149), Eldad & Medad (#196),
Herod (#86), Rahab (#190, verbal reference), Jesse (#198, "stem of Jesse"
imagery), Solomon (#111, verbal reference). The wise men (#86) are excluded as
unnamed in scripture — their in-build lock governs. If any of these ever
recurs in a new story, rule 4 kicks in: sheet first.

## Status board

**2026-07-21 — ALL 63 SHEETS APPROVED AND LOCKED BY CAMERON.** ("okay characters
are all good.") Every rostered character is now a LOCKED ref, exactly like
JESUS-MASTER-REF. From this moment rule 3 is binding on every build: a still
that shows a rostered character MUST attach that character's ref jpegs and use
the SPEC's written description. **Changing any sheet now requires Cameron's
explicit approval (rule 5).**

Board (kept live for reference): https://milk-b4-meat.web.app/characters.html
Contact sheets: `CHARACTERS/_approval-1-NT.jpg` / `_approval-2-OT.jpg`.

**⚠️ PENDING — added after the 63 were locked (Cameron, 2026-07-21):** two more
Jesus stages, `infant-jesus` and `risen-jesus`, plus the AGE-VARIANT KEY above.
Their SPEC.md files are written; the **sheets are not rendered and not
approved**. Any build showing the babe (#84, #85, #86) or the risen Christ
(#97, #98, #99, #100, #134, #179, #154, #189) is BLOCKED under rule 7 until
those two sheets are rendered and Cameron approves them on the board. The
age-variant stages listed for Abraham, Isaac, Jacob, Joseph, Samuel, David,
Moses, Elijah, John and Paul are likewise unbuilt — build them before any story
still shows those figures at a stage other than their locked prime sheet.

**How a build uses a sheet (do this, every time):**
```python
import sys; sys.path.insert(0, '../CHARACTERS')      # from a build-NN folder
from character_refs import refs, lock_text, find_in_text
refs('peter')        # -> [face-front.jpeg, three-quarter.jpeg, full-body.jpeg] to pass as --ref
lock_text('peter')   # -> the exact paragraph to paste into the prompt
```
Gate before spending any Flow credit, same as the face gate:
`python3 media-production/character_ref_gate.py --dir build-NN-slug` must exit 0.

Tools: `CHARACTERS/render_sheet.py` (reroll a view = delete the jpeg, rerun),
`CHARACTERS/qc_strip.py`, `CHARACTERS/approval_sheet.py`, `CHARACTERS/REFS.json`.

| Character | SPEC.md | Sheet rendered | Cameron approved |
|---|---|---|---|
| Jesus | ✅ (face-law v3) | ✅ JESUS-MASTER-REF | ✅ |
| God the Father | ✅ GOD-THE-FATHER-LOCK | ✅ | ✅ 2026-07-21 |
| Stephen | ✅ | ✅ | ✅ 2026-07-21 |
| Naaman | ✅ | ✅ | ✅ 2026-07-21 |
| Elisha | ✅ | ✅ | ✅ 2026-07-21 |
| Peter | ✅ | ✅ | ✅ 2026-07-21 |
| John (beloved) | ✅ | ✅ | ✅ 2026-07-21 |
| James (son of Zebedee) | ✅ | ✅ | ✅ 2026-07-21 |
| Andrew | ✅ | ✅ | ✅ 2026-07-21 |
| Matthew | ✅ | ✅ | ✅ 2026-07-21 |
| Thomas | ✅ | ✅ | ✅ 2026-07-21 |
| Judas Iscariot | ✅ | ✅ | ✅ 2026-07-21 |
| John the Baptist | ✅ | ✅ | ✅ 2026-07-21 |
| Mary (mother of Jesus) | ✅ | ✅ | ✅ 2026-07-21 |
| Joseph of Nazareth | ✅ | ✅ | ✅ 2026-07-21 |
| Mary Magdalene | ✅ | ✅ | ✅ 2026-07-21 |
| Martha | ✅ | ✅ | ✅ 2026-07-21 |
| Mary of Bethany | ✅ | ✅ | ✅ 2026-07-21 |
| Lazarus | ✅ | ✅ | ✅ 2026-07-21 |
| Zacchaeus | ✅ | ✅ | ✅ 2026-07-21 |
| Nicodemus | ✅ | ✅ | ✅ 2026-07-21 |
| Pilate | ✅ | ✅ | ✅ 2026-07-21 |
| Paul | ✅ | ✅ | ✅ 2026-07-21 |
| Bartimaeus | ✅ | ✅ | ✅ 2026-07-21 |
| Jairus | ✅ | ✅ | ✅ 2026-07-21 |
| Cleopas | ✅ | ✅ | ✅ 2026-07-21 |
| Barabbas | ✅ | ✅ | ✅ 2026-07-21 |
| Zebedee | ✅ | ✅ | ✅ 2026-07-21 |
| Malchus | ✅ | ✅ | ✅ 2026-07-21 |
| Simon the Pharisee | ✅ | ✅ | ✅ 2026-07-21 |
| Young Jesus (boy ~12) | ✅ | ✅ | ✅ 2026-07-21 |
| Philip | ✅ | ⬜ | ⬜ |
| Bartholomew (Nathanael) | ✅ | ⬜ | ⬜ |
| James (son of Alphaeus) | ✅ | ⬜ | ⬜ |
| Thaddaeus | ✅ | ⬜ | ⬜ |
| Simon the Zealot | ✅ | ⬜ | ⬜ |
| Adam | ✅ | ✅ | ✅ 2026-07-21 |
| Eve | ✅ | ✅ | ✅ 2026-07-21 |
| Noah | ✅ | ✅ | ✅ 2026-07-21 |
| Abraham | ✅ | ✅ | ✅ 2026-07-21 |
| Sarah | ✅ | ✅ | ✅ 2026-07-21 |
| Isaac | ✅ | ✅ | ✅ 2026-07-21 |
| Jacob | ✅ | ✅ | ✅ 2026-07-21 |
| Joseph (of Egypt) | ✅ | ✅ | ✅ 2026-07-21 |
| Moses | ✅ | ✅ | ✅ 2026-07-21 |
| Aaron | ✅ | ✅ | ✅ 2026-07-21 |
| Joshua | ✅ | ✅ | ✅ 2026-07-21 |
| Elijah | ✅ | ✅ | ✅ 2026-07-21 |
| Eli | ✅ | ✅ | ✅ 2026-07-21 |
| Samuel | ✅ | ✅ | ✅ 2026-07-21 |
| Hannah | ✅ | ✅ | ✅ 2026-07-21 |
| David | ✅ | ✅ | ✅ 2026-07-21 |
| Ruth | ✅ | ✅ | ✅ 2026-07-21 |
| Naomi | ✅ | ✅ | ✅ 2026-07-21 |
| Boaz | ✅ | ✅ | ✅ 2026-07-21 |
| Job | ✅ | ✅ | ✅ 2026-07-21 |
| Jonah | ✅ | ✅ | ✅ 2026-07-21 |
| Daniel | ✅ | ✅ | ✅ 2026-07-21 |
| Shadrach | ✅ | ✅ | ✅ 2026-07-21 |
| Meshach | ✅ | ✅ | ✅ 2026-07-21 |
| Abednego | ✅ | ✅ | ✅ 2026-07-21 |
| Nebuchadnezzar | ✅ | ✅ | ✅ 2026-07-21 |
| Isaiah | ✅ | ✅ | ✅ 2026-07-21 |
| Jeremiah | ✅ | ✅ | ✅ 2026-07-21 |
| Ezekiel | ✅ | ✅ | ✅ 2026-07-21 |
| Hosea | ✅ | ✅ | ✅ 2026-07-21 |
| Gomer | ✅ | ✅ | ✅ 2026-07-21 |
| Joel | ✅ | ✅ | ✅ 2026-07-21 |
| Malachi | ✅ | ✅ | ✅ 2026-07-21 |
