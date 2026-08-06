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
