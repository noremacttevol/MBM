# QC / RUNNER HANDOFF — build-103-peters-confession

Complaint-gate addendum, 2026-08-05 (Machine A).

## OPEN CAMERON COMPLAINT — gates before build

"This is where peter got his name but it called him simon before and
the pictures are all bad they keep changing and are not remade with
the character [references]."
1. Peter's canonical face sheet attaches to EVERY frame of him —
   this is the name-giving story, so his face staying one man is the
   whole point. Face-board him hardest of any row.
2. All recurring faces must be generated with their canon references
   and boarded — 'the pictures keep changing' is the complaint;
   consistency is the deliverable.
3. (The Simon-before-Peter naming in narration is the SCRIPT reading
   Matthew 16 correctly — he IS Simon until the verse renames him;
   no prompt change needed for that half.)

---

## RUNNER SHIP LOG — A-auto Machine A `Dev`, 2026-08-06 (SHIPPED)

Realistic V2, 20 painted stills @ native 2K, Ken Burns, KJV/scripture captions,
question card. **AUDIO LOCK PASS SHA256=e46b00815c…** (V1 audio byte-identical,
nothing re-voiced). 19.9 MB / 127.5s. matthew-16_peters-confession.mp4.

### COMPLAINT LEDGER (the LEARNING LAW)
Open complaint (v2_outline.py 103): *"This is where peter got his name but it
called him simon before and the pictures are all bad they keep changing and are
not remade with the character ref in this."*

- **"the pictures keep changing / not remade with the character ref" → FIXED
  (the deliverable).** Peter is now ONE man in every frame he appears (curly
  black hair, full black beard, grey-blue robe), generated FROM his canonical
  character reference (`PETER:front` + `PETER:quarter` attached to every Peter
  beat — the payload even DROPPED the place plate to keep Peter's face refs on
  crowded beats). Face-boarded across s01/s05/s07/s08/s10/s11/s12/s13/s14/s15/
  s16/s17/s18 — same actor. The name-giving beat s18 ("thou art Peter, and upon
  this rock") shows his face clearly and it matches. Jesus is master-locked and
  identical throughout; Andrew (olive) and John (younger, lighter) are distinct
  and each consistent.
- **"it called him simon before" → correct by scripture, no change.** Matthew 16
  keeps him Simon (np "Simon Peter answered", jv17 "Simon Barjona") until jv18
  renames him "Peter." The narration reads the verse correctly; captions match.

### BEARD / SCALE / CREAM / STYLE gates
- Beard board: Peter full black beard, Jesus full dark beard, Andrew/John stable
  — no appear/disappear/recolor. PASS.
- Scale gate: all adults proportionate in every multi-figure wide (s01/s10/s20);
  Jesus ordinary-sized, never a giant. PASS.
- Cream law: only Jesus wears cream/off-white; disciples in blue/olive/brown/grey.
  PASS. (s04 has a cream-robed teacher figure that reads as Jesus present at the
  beat — not a stray disciple in cream.)
- Realistic-only (Law 14): ALL 20 frames photographic; zero cartoon/mixed. PASS.
- No modern objects, no lens-staring, no burned-in subtitles, anatomy clean. PASS.
- s09/Jesus close-ups carry the known systemic green/hazel eye cast (baked into
  JESUS-V2-REF) — NOT rerolled (RUNNER-LESSONS: master-ref level, not per-row).

### FIX-WAVE (author handoff — NOT a runner-fixable defect)
- **SETTING DRIFT on the 6 beats that do NOT lock CLIFF (b04, b06, b12, b13, b15,
  b17): the model rendered a generic INDOOR house / village-door setting instead
  of the row's locked "same glade under the pale cliff throughout."** Root cause:
  the CLIFF place plate only attaches to beats whose `locks` list names CLIFF, and
  these 6 beats' scene text carries NO outdoor cue — so with no place anchor the
  model defaults to an interior. The 14 CLIFF-locked beats all stayed correctly in
  the outdoor cliff glade. Faces on the indoor beats are still Peter-consistent, so
  under the complaint (which is about FACE consistency) the deliverable holds; the
  indoor setting is a SECONDARY continuity mismatch.
- **Runner could NOT fix this within rails:** rerolling is a coin-flip (no CLIFF
  lock, no outdoor scene cue) and I VERIFIED it — 2 rerolls of b13 both came back
  indoor, and the first even broke Peter's face. Rerolling further would burn
  meter for no reliable gain (COST LAW) and risk the very face consistency that is
  the deliverable, so I stopped at 2 rerolls (10%) and kept the face-consistent
  b13 take. The full fix is an AUTHOR edit: add `"CLIFF"` to the `locks` list of
  beats b04/b06/b12/b13/b15/b17 (or add "under the pale cliff, spring glade" to
  their scene text) so the glade plate attaches, then regenerate those 6 beats.
  The existing stills are reusable for every other beat — do NOT regen the row.

### COST
Row spend ≈ **$2.94** (20 stills + b19 anchor + 2 b13 rerolls, all @ ~$0.134).
Rerolls 2/20 = **10%** (under the 15% budget). Well under the $6.10/row average —
promoted the CLIFF plate from this row's own b19 (0 extra cost) and reused all
cast portraits free (0 portraits generated). The COST-LAW trend stays DOWN.

---

## ✅ AUTHOR DONE — SETTING DRIFT FIX (Fable-5 author lane, Machine A `Dev`, 2026-08-07, $0)

The FIX-WAVE handoff above is now applied in `beats_v2.py`. Complaint is
COMPLAINT-FIRST + LOW-NUMBER priority (open, shipped, low row) and is now
author-resolved; only a paid 6-still reroll remains.

**What was wrong (root cause, confirmed against the file + lesson 487):** row 103
is a single-location OUTDOOR story ("the same cliff, springs and glade
throughout"), but 6 close-up beats — b04, b06, b12, b13, b15, b17 — omitted the
`CLIFF` token from their `locks`. `CLIFF` is a PROSE lock (build LOCKS dict;
`PLACE_REFS` is empty — there is no CLIFF image plate), and the assemble() step
injects a lock's prose ONLY into beats whose `locks` name it. With no outdoor cue
in those 6 beats' scene text, the model defaulted to a generic indoor
house/village. The 2026-08-06 ship note explains WHY the runner dropped the
setting from crowded beats — "DROPPED the place plate to keep Peter's face refs" —
i.e. it treated setting-vs-face as a tradeoff. It is NOT a tradeoff here: `CLIFF`
is TEXT, so it costs zero reference-image slots; Peter's face sheet still attaches.

**Author fix applied ($0):** added `"CLIFF"` to the `locks` of all 6 beats
(b04→`["CLIFF","PETER","ANDREW"]`, b06→`["CLIFF","ANDREW"]`,
b12→`["CLIFF","PETER"]`, b13→`["CLIFF","PETER","JOHN","ANDREW"]`,
b15→`["CLIFF","PETER"]`, b17→`["CLIFF","PETER","ANDREW","JOHN"]`). All 20 beats
now carry CLIFF (verified: `assemble()` injects "GREAT PALE ROCK CLIFF" prose into
b06/b12/b15 — the tight close-ups — while their `scene` still says "Close on…" so
framing stays tight with the glade behind, not an interior). `--check` PASS
(20 beats, v4). Audio untouched (Audio OK). The Simon→Peter naming is correct by
scripture (Matt 16:17-18) — no narration change, per the gate note above.

### COMPLAINT LEDGER — this re-cut
Open complaint: *"…the pictures are all bad they keep changing and are not remade
with the character ref…"*
- **Interior drift half → FIXED (author):** the 6 close-ups now render in the
  locked cliff glade like the other 14, so the setting no longer "keeps changing"
  between wides and close-ups. This also removes the reason the runner had to
  reroll them (the rerolls are what "even broke Peter's locked face" — lesson 487),
  so Peter stays one man across the regen.
- **Peter face-consistency half → protected:** every Peter beat keeps its `PETER`
  cast ref (CLIFF is prose, added alongside — nothing dropped). Face-board Peter
  hardest of any row (name-giving story); s18 "thou art Peter" must clearly match.

### 🅿️ RUNNER — do this (paid, ONE re-cut, ~$0.80)
1. Regenerate ONLY b04, b06, b12, b13, b15, b17 against the fixed CLIFF-locked
   prompts. KEEP the other 14 stills (they were correct). Do NOT regen the row.
2. Face-board Peter across all his beats incl. the 6 new ones; identity-edit any
   drift, then recheck the full frame. Confirm each of the 6 renders OUTDOORS in
   the cliff glade (that is the gate — no interior, no village door).
3. Re-assemble (AUDIO byte-identical, LOCK PASS), re-audit, ship via C-FIX with
   this ledger on the review card so Cameron sees the setting + face fixed.
Reroll budget: the 6 named beats are the fix, not rerolls — treat 6 regens as the
planned re-cut; hold extra rerolls ≤15%.

---

## ✅ RUNNER C-FIX SHIPPED — SETTING DRIFT re-cut (Opus runner, Machine A `Dev`, 2026-08-07)

Executed the author's 6-still re-cut exactly as specced. Regenerated ONLY
b04/b06/b12/b13/b15/b17 over the now CLIFF-locked prompts (`--only b04 b06 b12
b13 b15 b17 --redo`); KEPT the other 14 stills byte-identical.

### COMPLAINT LEDGER (the LEARNING LAW)
Open complaint (`v2_outline.py 103`): *"This is where peter got his name but it
called him simon before and the pictures are all bad they keep changing and are
not remade with the character ref in this."*
- **"the pictures keep changing" (setting half) → FIXED.** The 6 close-ups that
  had drifted to a generic INDOOR house/village now render OUTDOORS in the same
  pale-rock cliff glade (waterfall + poplar/stream) as the other 14 stills, so
  the setting no longer flips between wides and close-ups. Verified in the RENDERED
  mp4 at 18s (s04), 22s (s17), 32s (s06), 70s (s13), 84s (s15) — all outdoors.
- **"not remade with the character ref" (face half) → held.** Every regen carried
  the PETER cast ref (`[+N char ref: PETER:front, PETER:quarter]` in the gen log);
  Peter is one man (dark curly hair, full black beard, grey-blue robe) across all
  his frames incl. the name-giving arc — face-boarded vs s01/s11/s18, matches.
  Jesus is cream-only + locked-face with calm eyes in s04/s15; Andrew/John distinct.
- **"it called him simon before" → correct by scripture, no change.** Matthew 16
  keeps him Simon until v18 renames him Peter; narration + captions read the verse
  correctly.

### GATES
- OUTDOOR gate: 6/6 render in the cliff glade (no interior, no village door). PASS.
- Cream law: only Jesus wears cream (s04/s15). PASS.
- Scale (lesson 14), beard (lesson 13), realistic-only (Law 14), no modern object,
  no lens-stare, anatomy: PASS on all 6.
- Captions bottom-band only (18s/70s verified); question card clean (124s). PASS.
- **AUDIO LOCK PASS SHA256=e46b00815c…** — IDENTICAL to the prior ship's audio
  hash, so narration/voices/timing are byte-identical. 127.5s / 20.0 MB.

### FIX-WAVE (minor, not rerolled — COST LAW / touch-once)
- s15: a couple of tiny dark marks on Peter's knuckles (row-39 ink-smudge class) —
  cosmetic, localized, does NOT repeat the complaint; not worth risking the good
  Jesus↔Peter two-shot + locked face. Leave for a later cosmetic edit pass.

### COST
0 images rerolled beyond the 6 planned regens. **6 regens / 20 beats; 0 extra
rerolls = 0% reroll budget used.** ~$0.81 this run (meter $499.55 → $500.36).
Well under the $6.10/row average; touched the row ONCE. COST-LAW trend DOWN.
