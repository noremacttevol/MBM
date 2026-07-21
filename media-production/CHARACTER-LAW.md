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

## Roster (FINAL — locked by the character session, 2026-07-21, after scanning
## all 201 build PROMPTS.md + QUEUE.md + the name harvest)

**Locked already:** Jesus (JESUS-MASTER-REF), God the Father (SPEC in
GOD-THE-FATHER-LOCK.md; sheet render below).

**New Testament (26):** Peter, John (beloved), James (son of Zebedee), Andrew,
Matthew, Thomas, Judas Iscariot, John the Baptist, Mary (mother of Jesus),
Joseph of Nazareth, Mary Magdalene, Martha, Mary of Bethany, Lazarus,
Zacchaeus, Nicodemus, Pilate, Stephen, Paul, **Bartimaeus (#12), Jairus (#57),
Cleopas (#18), Barabbas (#93), Zebedee (#51/#71), Malchus (#66),
Simon the Pharisee (#74)** — the bolded seven were added by the scan: each is a
named on-screen story lead.

**Old Testament (35):** Adam, Eve, Noah, Abraham, Sarah, Isaac, Jacob,
Joseph (of Egypt), Moses, Elijah, Elisha, Eli, Samuel, Hannah, David, Ruth,
Naomi, Boaz, Job, Jonah, Daniel, Shadrach, Meshach, Abednego, Nebuchadnezzar,
Naaman, Isaiah, Jeremiah, Ezekiel, Hosea, **Aaron (#161), Joshua (#196),
Gomer (#117), Joel (#197), Malachi (#174/#191)** — added by the scan.

**Variant sheet:** Young Jesus (boy, ~12) for #87 — must read as the SAME
person as JESUS-MASTER-REF, features scaled young (per CHARACTERS/WANTED.md).

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
