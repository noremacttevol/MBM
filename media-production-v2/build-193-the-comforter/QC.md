# QC / RUNNER HANDOFF — build-193-the-comforter

**Row 193 · John 14:18, 26 · "I will not leave you comfortless... the Comforter, which is
the Holy Ghost."** State: **AUTHORED / Ready ✅** (picture map authored, `--check` PASS,
audio OK, no open complaint). Fable-5 author lane, Machine A `Dev`, 2026-08-07, $0.

---

## COMPLAINT LEDGER
- **No open Cameron complaint** on row 193 (`v2_outline.py 193` shows none). Fresh
  NEEDS-BEATS → AUTHORED build. Board Audio = OK (audio-audit gate passed); default AUDIO
  LOCK stream-copy, no re-voice.

---

## ✅ AUTHOR DONE — 13-beat V2 map, `--check` PASS, windows contiguous 0.000→57.038 (=card)

Fresh movie-coverage beat map (NEEDS-BEATS → AUTHORED). 13 pictures over 57.038 s ≈
4.39 s/pic. The Upper-Room discourse on the last night: Jesus is the one doing the
comforting though he is hours from the cross; he promises the Comforter, and the red-letter
lands on his own face.

Beat spine:
- b01 the last night (**establishing wide, UPPER-ROOM promote** — Jesus + the Eleven at the
  lamplit table) · b02 not left alone (Jesus close with Peter & John)
- b03 **j0 RED** "I will not leave you comfortless: I will come to you." · b04 hours from
  the cross yet He comforts (Jesus's calm face) · b05 not on their own (disciples steadied)
- b06 another Helper — the Holy Ghost sent by the Father (Jesus promises; **Spirit & Father
  NOT shown**) · b07 teach them everything (disciples' understanding) · b08 bring to
  remembrance (**NON-Jesus insert** — a disciple's face lit with recollection)
- b09 **j1 RED** "But the Comforter, which is the Holy Ghost, whom the Father will send in
  my name," · b10 **j1 RED** "he shall teach you all things," · b11 **j1 RED** "and bring
  all things to your remembrance, whatsoever I have said unto you."
- b12 the promise still stands (Jesus's steady face) · b13 the Spirit teaches everyone who
  listens now (**NON-Jesus close** — disciples receptive in warm lamplight)

**SPEAKER LAW:** j0 (14:18) and j1 (14:26) = Jesus's own words → **red-letter** on Jesus;
all else narrator → white. Jesus IS in this story — every beat he appears sets jesus=True +
ref=True so the master face + JESUS LOCK attach and the red-letter lands on him. **Only
Jesus wears cream; no one else in cream or white.** (b08 and b13 are the two NON-Jesus
beats — inserts of the disciples; jesus=False there.)

**HARD GATE — GOD/THE FATHER NEVER EMBODIED, AND THE HOLY GHOST / COMFORTER NEVER EMBODIED.**
The Father who "will send" the Comforter is never shown. The Holy Ghost promised here is
NEVER given a body — NO third person for the Spirit, NO dove-with-rays, NO radiant/figure,
NO beam-shaped-like-a-person, NO halo. The Spirit's work (teaching, remembrance) is carried
by Jesus's promise and by the DISCIPLES' faces in ordinary warm lamplight only. Drift-word
gate clean (no halo/glow/rim-light in any scene). The b08/b13 `--check` "cream" WARNs are
benign — each says explicitly "(not cream)/(none cream)"; kept intentionally.

**CONTENT-CARE:** comfort, not fear. Jesus calm and giving hope though hours from the cross;
disciples troubled but steadied. **NO cross, NO wounds, NO blood, NO Gethsemane agony** —
the scene stays in the quiet upper room.

**TIME-OF-DAY:** NIGHT — warm oil-lamp light, dark windows. No daylight; but no divine glow
either — the light is the lamps.

---

## 🅿️ RUNNER — build the 13 stills (0 exist today)

**ONE place — UPPER-ROOM (NEW):** promote from **b01** (the establishing wide; Jesus is in
that frame but the plate carries the ROOM — Jesus is separately injected by the assembler),
reuse on b02-b13. `git add -f build-193-the-comforter/PLACE-REF/*.jpeg` after promoting.
(Optional: if `v2_stash.py --wire build-193-the-comforter` SUGGESTS the build-74 lamplit
`room` plate and you judge it a TRUE match — same first-century lamplit chamber, night — you
may `--take` it instead of promoting.)

**Gates before assembly:**
- **JESUS FACE GATE** — `python3 media-production-v2/jesus_face_gate.py --dir
  build-193-the-comforter` must exit 0 (11 of 13 beats are jesus=True/ref=True). Master face
  identical across b01-b07, b09-b12; only Jesus in cream.
- Face/beard board on the DISCIPLES (same Eleven across frames, distinct not twins), and
  PETER / JOHN on b02/b05 (global cast faces — must match their locked look).
- **Sacred-figure gate — FATHER & HOLY GHOST NEVER EMBODIED**: no figure/dove/beam/throne
  standing in for the Spirit or the Father in ANY frame (b06/b07/b08/b09/b10/b11/b13 most at
  risk). No halo/glow/rim-light.
- Content-care gate: no cross/wounds/blood/agony anywhere; comfort only.
- Realistic-only Law 14 (no cartoon/mixed frame); NO ONE but Jesus in cream/white.

**Audio:** default AUDIO LOCK stream-copy (byte-identical narration; no re-voice). Assemble,
light-QC per the gates above, then ship.

---

## 🛠 REVIEW CARD (for Cameron)
Jesus's promise of the Comforter (John 14) — realistic V2. His own words (red) rest on his
face; the Holy Ghost and the Father are never pictured — the Spirit's comfort is carried by
the disciples' faces in the lamplit upper room. No open complaint on this row.

---

## ✅ RUNNER SHIPPED (2026-08-24, Machine A `Dev`, Claude session)

Fresh build: DISCIPLES portrait + all 13 stills. **ZERO plate clones** although
ALL 13 beats share one place and eight were authored as "a shot of Jesus in the
lamplit room" — rubric lesson 26 applied first, 12 beats given distinct cameras
(over-shoulder / hand-forward medium / tight face with lamp at edge /
disciples-only two-shot / low from table height / along the row of faces /
extreme eye insert / profile through the lamp / open-hand insert / from behind
his shoulder / opposite-side close / high angle on the table).
**1 reroll / 13 = 7.7%. Cost $2.01 (15 gens).**
- The reroll (b07) was MY wording: "a wide LEVEL sweep" produced a LETTERBOXED
  frame with brown bars top and bottom instead of filling the 9:16 picture.
  Re-worded with an explicit no-bars/no-widescreen-strip ban. **Never say "wide
  sweep/cinematic wide" in a vertical row — it invites letterboxing.**
- **CROSS-VIDEO CONTINUITY:** UPPER-ROOM was `--take`n from build-170's own b01
  plate (built earlier this same session), so the Sacrament video and this one
  show the SAME upper room — rather than promoting a fresh room or accepting the
  stash's build-44 Pentecost suggestion, which is a different event and room.

**FULL-CUT GATE — 13 beats + card viewed on the ENCODED mp4: PASS.** SPEAKER
LAW: RED only on Jesus's exact John 14:18/14:26 words (b03, b09, b10, b11);
narrator white; no green, no blue. Jesus V2 face on-model throughout, **cream
ONLY him**, no halo. **HARD GATE held — the FATHER and the HOLY GHOST are NEVER
embodied**: no Spirit figure, no dove, no beam or rays; the Comforter's teaching
and remembrance are carried by Jesus's promise and the disciples' faces (b08 is
one man's remembering face). CONTENT-CARE: comfort, not fear — no cross, no
wounds, no agony; the whole row stays in the quiet lamplit upper room at night.
Card clean.

**AUDIO:** guard fix `AUDIO_FROM_V1_SEGMENTS` (V1 65.900s vs extract 63.671s,
gap placement; 10 ElevenLabs mp3s) — **AUDIO REBUILD PASS SHA256=6d22f4be68…**,
63.7s, 19.4 MB.
