# PICTURE REDO WORKLIST — apply the locked CAST-REF to every video that needs it

> Started 2026-07-22, Machine C. Cameron approved the locked cast (`CAST-REF/`, Jesus +
> the Twelve). The reference images are BRAND NEW, so no existing video uses them yet —
> every video that shows the disciples needs its disciple stills regenerated with the
> new REF images so Peter and the Twelve are the same faces everywhere.
>
> **Method per video:** attach the relevant refs when regenerating each disciple still —
> `--ref CAST-REF/the-twelve.jpeg` for crowd/boat scenes, plus the solo ref(s) for any
> featured man (`CAST-REF/peter.jpeg`, `CAST-REF/john.jpeg`, …), and `--ref
> JESUS-MASTER-REF/jesus-face.jpeg` whenever Jesus shares the shot. Only regenerate the
> stills that actually contain a disciple; Jesus-only / scenery / other-character stills
> are left alone. Then rebuild the mp4 (build.py), full QC, present to Cameron.
>
> Priorities came from an automated disciple-prominence scan of every build's PROMPTS.md,
> then hand-pruned: **John-the-Baptist videos and KJV scripture-citations are NOT the
> disciples** and were removed.

## Progress key: ⬜ todo · 🔄 in progress · ✅ done+shown

---

## P1 — DISCIPLE-DEFINING SCENES (do these first — a viewer WILL notice a wrong Peter/face)
Named disciples or the whole Twelve are the visible subject.

| ✓ | # | Build | Who is featured |
|---|---|---|---|
| ✅ | 7   | build-07-peter-water            | Peter (lead), the Twelve, the boat — REBUILT 2026-07-22, awaiting Cameron's watch |
| ⬜ | 71  | build-71-calling-the-fishermen  | Peter, Andrew, James, John — by name |
| ⬜ | 51  | build-51-first-catch-of-fish    | Peter, James, John, boat, nets |
| ⬜ | 11  | build-11-storm                  | the Twelve, the boat (Sea of Galilee) |
| ⬜ | 89  | build-89-the-last-supper        | all Twelve at the table |
| ⬜ | 90  | build-90-washing-feet           | Peter + the Twelve |
| ⬜ | 91  | build-91-gethsemane             | Peter, James, John |
| ⬜ | 92  | build-92-peters-denial          | Peter |
| ⬜ | 103 | build-103-peters-confession     | Peter + the Twelve |
| ⬜ | 99  | build-99-flesh-and-bone-thomas  | Thomas + the Twelve |
| ⬜ | 145 | build-145-way-truth-life        | Thomas, Philip + the Twelve (upper room) |
| ⬜ | 53  | build-53-peters-mother-in-law   | Peter, Andrew, James, John |
| ⬜ | 72  | build-72-calling-matthew        | Matthew (Levi) |
| ⬜ | 19  | build-19-shore                  | Peter, John, boat, nets (breakfast on the shore) |
| ⬜ | 18  | build-18-emmaus                 | two disciples (Cleopas + one) |
| ⬜ | 100 | build-100-the-ascension         | the Twelve |
| ⬜ | 162 | build-162-keys-of-kingdom       | Peter |
| ⬜ | 165 | build-165-laying-on-hands       | Peter, John, apostles |

## P2 — THE TWELVE PRESENT AS A GROUP (do after P1)
The disciples are in-frame but not the whole subject; regenerate the group/crowd stills.

| ✓ | # | Build |
|---|---|---|
| ⬜ | 58  | build-58-feeding-5000 (Andrew, the Twelve) |
| ⬜ | 59  | build-59-feeding-4000 |
| ⬜ | 60  | build-60-gerasene-demoniac (boat) |
| ⬜ | 57  | build-57-jairus-daughter (Peter, James, John) |
| ⬜ | 76  | build-76-suffer-the-little-children |
| ⬜ | 88  | build-88-triumphal-entry |
| ⬜ | 63  | build-63-man-born-blind |
| ⬜ | 130 | build-130-what-manner-of-spirit (James, John) |
| ⬜ | 132 | build-132-forbid-him-not (John) |
| ⬜ | 133 | build-133-many-mansions (upper room) |
| ⬜ | 166 | build-166-baptized-properly |
| ⬜ | 185 | build-185-many-mansions-member |
| ⬜ | 193 | build-193-the-comforter |
| ⬜ | 200 | build-200-gospel-to-all-the-world |
| ⬜ | 1   | build-01-cloak (disciples around Jesus) |
| ⬜ | 48  | build-48-new-wine-old-bottles |
| ⬜ | 22  | build-22-unmerciful-servant (Peter asks) |
| ⬜ | 197 | build-197-sons-and-daughters-prophesy (Peter, Pentecost) |
| ⬜ | 30  | build-30-net (fishermen/boat parable) |
| ⬜ | 24  | build-24-sower (boat pulpit) |
| ⬜ | 61  | build-61-syrophoenician-woman |
| ⬜ | 10  | build-10-well (disciples return) |
| ⬜ | 14  | build-14-ten-lepers |
| ⬜ | 15  | build-15-centurion |
| ⬜ | 49  | build-49-water-to-wine |
| ⬜ | 77  | build-77-widows-mite |
| ⬜ | 96  | build-96-it-is-finished (John at the cross) |
| ⬜ | 98  | build-98-mary-her-name (John) |
| ⬜ | 163 | build-163-apostles-prophets |
| ⬜ | 164 | build-164-unity-of-faith (apostles) |

## VERIFY BEFORE TOUCHING (borderline — open the mp4/PROMPTS first)
153 restitution · 190 faith-without-works (Epistle of James?) · 108/134/141/142/143/144/146/159/168/172/173/174 (mostly John-citation verse cards — likely SKIP) · 62 ephphatha · 161 called-of-god.

## EXCLUDE — NOT a cast-redo (scan false positives)
- **John the Baptist, not disciple John:** 69 baptism · 107 john-baptist-doubt · 169 fulfil-righteousness.
- **KJV scripture-citation only** (the closing verse card cites "Matthew"/"John" the book): the ~40 Tier-2 rows scoring 3 on a single citation and nothing else — no disciple is depicted. Skip unless a spot-check shows disciples in the art.

## NOTES
- One video per chat keeps context low (standing rule). This worklist is the shared queue
  so any machine can pull the next ⬜ P1 row, mark it 🔄, and go.
- Credits: disciple stills regenerate on Nano Banana 2 (0 credits) with the refs attached.
