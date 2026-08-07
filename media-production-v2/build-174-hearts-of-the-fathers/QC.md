# QC / RUNNER HANDOFF — build-174-hearts-of-the-fathers

Row 174 · Malachi 4:5-6 ("Behold, I will send you Elijah the prophet... and he
shall turn the heart of the fathers to the children, and the heart of the children
to their fathers"). RESTORATION shelf (the Elijah / family-reconciliation
promise). Authored fresh 2026-08-07 (Machine A `Dev`, Fable-5 author lane, $0).

## COMPLAINT LEDGER
- **No open Cameron complaint.** `v2_outline.py 174` shows none. First-time V2
  picture map on the already-authored SPEAKER-LAW narration (audio OK).

## SPEAKER LAW + HARD GATE (verified)
Malachi — s1a and s1b are the **GOD voice → GREEN captions**. **HARD GATE: GOD IS
NEVER EMBODIED** — no figure, face, hand, beam, rays or shaft from heaven, no
divine being in any frame (same gate as rows 165/166/168/169). God's words land on
the prophet, the land and the people, shown as ordinary natural light. On the two
GOD beats that picture Elijah (b02/b03) his mouth is CLOSED — he is the one God is
*sending*, not the speaker, so it never reads as Elijah mouthing God's words. All
other beats are WHITE narrator. **NO Jesus and NO cream anywhere in this row.**
`--check` v4 PASS, no warnings.

## CONTENT-CARE
"lest I come and smite the earth with a curse" (end of s1b, in b08's caption) is
**NOT pictured** as smiting/disaster/fire/cursed earth — b08 shows the
reconciliation the promise is *for*. Elijah's errand is "to mend, not to thunder":
peaceable, empty-handed, a staff not a weapon (b06/b09) — never calling down fire.
No halo/glow/rim-light on anyone.

## Cast (build-local locks — hold identity across frames)
- **ELIJAH** — aged grey prophet, rough haircloth mantle + leather girdle, staff
  (b01-b06, b09).
- **JOHN-BAPTIST** — lean young Baptist, dark hair, camel-hair garment (b10). A
  DIFFERENT man from Elijah. NOTE: do NOT use the global `JOHN` token (that is
  John the apostle); this build uses `JOHN-BAPTIST`.
- **FAMILY-THREE** — three generations (aged grandfather / grown father / young
  child), same faces across b07/b08/b09/b11/b12.

## Places (both NEW build-local)
- **WILDERNESS-ROAD** — Elijah + John under the open sky (b01-b06, b10).
- **FAMILY-HOME** — the household courtyard, hearts turning (b07-b09, b11, b12).

## 🅿️ RUNNER — build steps (paid image lane)
Two NEW places; promote each from its first good frame BEFORE the rest that share
it (lesson 11):
1. **Generate b01 first** (WILDERNESS-ROAD establishing wide, Elijah). QC it, then:
   `python3 media-production-v2/v2_stash.py --promote build-174-hearts-of-the-fathers WILDERNESS-ROAD build-174-hearts-of-the-fathers/assets/s01-a-messenger-sent-ahead.jpeg`
2. **Generate b07 next** (FAMILY-HOME establishing wide, three generations). QC it,
   then:
   `python3 media-production-v2/v2_stash.py --promote build-174-hearts-of-the-fathers FAMILY-HOME build-174-hearts-of-the-fathers/assets/s07-hearts-of-the-fathers.jpeg`
3. Re-run `v2_stash.py --wire build-174-hearts-of-the-fathers`, then `--check`
   (PASS) and `--dump`.
4. Generate the remaining beats against the plated places.
5. **Gates:** run the SACRED-FIGURE gate by eye on every GOD beat (b02/b03/b04/
   b07/b08) — confirm NO God figure/face/hand/beam anywhere. Elijah's mouth CLOSED
   on b02/b03. Face-board: ELIJAH identical across his beats, FAMILY-THREE
   identical across family beats, JOHN-BAPTIST distinct from ELIJAH. Content-care:
   no smiting/curse/fire on b08. Scale: everyone ordinary-sized.
   (No `jesus_face_gate` beats — there is no Jesus in this row.)
6. Assemble (AUDIO LOCK — narration authored + OK, byte-identical; do NOT
   re-voice). Re-audit, then ship. No open complaint to answer, so the card just
   presents the finished cut.

## Coverage / windows (authored, verified)
12 beats, windows contiguous 0.400 → 57.228 (= card_start), monotonic, each
segment's speech onset inside its window. ~4.75 s/picture. `--check` v4 PASS.
