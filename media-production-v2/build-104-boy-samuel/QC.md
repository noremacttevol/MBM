# QC / RUNNER HANDOFF — build-104-boy-samuel (1 Samuel 3)

## 🛠 C-FIX SHIP — Machine A (`Dev`) 2026-08-07 (Opus runner) — RUNNING-WRONG-WAY FIX DONE

**OPEN complaint (`v2_outline.py 104`): "0:35 pic Samuel is running the wrong way,
same thing with 0:53."** FIXED. Regenerated exactly the two run frames over the
author's fixed prompts (pinned LEFT→RIGHT hall geography):

- **s06 (0:35)** — regen: Samuel now runs unmistakably LEFT→RIGHT, body/lean/bare
  feet/gaze all driving rightward TOWARD Eli, who sits at frame RIGHT in his
  doorway reaching out. He runs toward the old man, no longer away. (Old frame:
  boy ran LEFT, away from Eli on the right.)
- **s10 (0:53)** — regen: same left-to-right dash toward Eli seated at frame RIGHT.
  (Old frame: boy ran toward the camera, away from Eli behind him.)
- **s04 (establish):** KEPT byte-identical — Eli sleeps deep in the back room
  (not on the left), so it does not contradict the pinned geography; no regen.
- **Every other still KEPT byte-identical.** Audio untouched (AUDIO LOCK PASS,
  byte-identical). Rerolls: 2 / 22 = **9%** — within the 15% budget. Spend this
  C-FIX: **$0.27** (2 stills, no portraits), meter $500.36 → $500.62.

QC on the two new frames: Samuel child-sized vs Eli/furniture (scale gate PASS);
Eli one full white beard + hair (beard board PASS); Samuel navy tunic + dark curls,
one child (PASS); photographic, no cartoon (Law-14 PASS); no halo/God figure/glow
(rendering law PASS); anatomy clean; menorah/oil-lamp/stone hall, no modern objects.

### COMPLAINT LEDGER (this C-FIX)
1. **"0:35 Samuel is running the wrong way"** → s06 regenerated: runs left-to-right
   straight TOWARD Eli at frame right — fixed.
2. **"same thing with 0:53"** → s10 regenerated the same way: second run is the
   same clear left-to-right dash toward Eli — fixed.


## ✅ AUTHOR DONE — 2026-08-07 (Machine A `Dev`, Fable-5 author lane, $0) — RUNNING-WRONG-WAY FIX

**OPEN complaint (`v2_outline.py 104`): "0:35 pic Samuel is running the wrong way,
same thing with 0:53."** Root-caused + author-fixed in `beats_v2.py`.

### Root cause (row-14 travel-direction law)
0:35 = **b06** (s06, the first run to Eli) and 0:53 = **b10** (s10, the second run).
Both scenes said only "sprint across the hall TOWARD the old man's doorway" — they
never PINNED which SIDE of frame Eli's room is on, so the model drew Samuel running
toward the curtain / away from where Eli sits, i.e. the wrong way. The wide
establishing shot **b04** also left the two rooms' sides unpinned, so nothing fixed
the geography for the runs to agree with.

### What the author did ($0)
1. **Pinned a FIXED SCREEN GEOGRAPHY in the HOUSE lock:** the boy's mat + the holy-
   place curtain are on the **LEFT**; Eli's side room + doorway are on the **RIGHT**.
   So going to Eli is always **LEFT→RIGHT**; being sent back is **RIGHT→LEFT**.
2. **b04 (establish):** stated boy/curtain LEFT, Eli's room RIGHT so the wide shot
   sets the same geography the runs rely on.
3. **b06 (0:35) + b10 (0:53):** rewrote must_show / must_not_show / scene so Samuel
   runs unmistakably LEFT→RIGHT — body, lean, bare feet and gaze all aimed rightward
   at Eli **ahead of him**, arriving at the right-hand bed; explicitly "runs TOWARD
   the old man, never away / never left toward the curtain."
4. **b08 (sent back):** pinned the return as RIGHT→LEFT toward his mat, so the
   reversal is consistent and doesn't read as a new wrong-way.
5. `v2_prompt.py --check` **PASS (22 beats)**; audio untouched (Audio col OK).

### 🅿️ RUNNER — the paid step (minimal re-cut, then ship)
- **Regen `s06` and `s10`** (the two complaint frames) over the fixed prompts — Samuel
  clearly running LEFT→RIGHT toward Eli in both. **Check `s04`'s current render:** if
  it already shows the boy/curtain on the LEFT and Eli's room on the RIGHT, keep it
  byte-identical; if it's mirrored (Eli on the left), regen `s04` too so the runs
  agree with the establishing shot. **KEEP every other still byte-identical.**
- Body-board Samuel (one age/size/blue tunic, lesson-56 class) + beard-board Eli on
  any regenerated frame; re-assemble (AUDIO byte-identical), ship via C-FIX flow.
- Cost: 2 (or 3 with s04) / 22 = ≤14% — within the reroll budget.

### COMPLAINT LEDGER — the review card must tell Cameron, in his words
1. **"0:35 Samuel is running the wrong way"** → s06 regenerated: Samuel now runs
   left-to-right straight TOWARD Eli, facing and leaning toward the old man ahead of
   him, arriving at his bedside — no longer running away.
2. **"same thing with 0:53"** → s10 regenerated the same way: the second run is the
   same clear left-to-right dash toward Eli, matching the pinned hall geography.

---

Lesson-12 + complaint-corpus pass done 2026-08-05 (Machine A). `--check`
PASSES, zero WARNs. 22 beats, ~122 s.

## The two (identity — child + elder, the row-56/87 class)

- SAMUEL: ONE age (a boy per his lock), ONE size, ONE tunic across
  every frame — the row-56 child-drift complaint class; body-board
  him. Scale-check him against Eli and the hall (child-small, no
  giant hall-furniture distortions).
- ELI: old, heavy, near-blind per his lock — beard/face constant
  (beard-QC).

## The voice (rendering law — same as rows 101/102)

The calling voice is NEVER visualized — no light, no figure, no
glow. The lamp of God burning low (b02) is the scene's only symbol,
and it is a real seven-branched oil lamp, gold and low. "Speak, for
thy servant heareth" plays as the boy's open-eyed listening stillness.

## The three runs (frame-per-action, the row's ladder)

Boy asleep → the run to Eli (b06, sprint in profile) → sent back →
second cycle (b10, tighter) → the teaching (b12: old hands on small
shoulders) → the waiting posture → the listening through the night.
The RUNS get distinct energy; the final LISTENING is stillness — the
arc from motion to stillness is the doctrine.

## Coverage shape

Two true wides with stated geometry: b04 (both sleepers' stations in
one profile — the hall's geography the runs depend on) and b06 (the
first sprint in profile). Nine flips including b01's PERSON-FREE hall
and three lone-boy frames.

- HOUSE is the SHILOH TABERNACLE hall — heavy hangings, the lamp,
  the ark's curtained room implied but NEVER shown (content-care: no
  invented sacred furniture). Bethany-lane declined an ELEVENTH time.
  Promote-first from b01 (person-free — ideal plate).
- Night → first gold dawn, one direction.

---

## RUNNER SHIP — A-auto Machine A (`Dev`) 2026-08-06 (Opus runner)

**SHIPPED REALISTIC V2.** `1samuel-3_the-boy-samuel.mp4`, 141.5s, 19.1 MB.
**AUDIO LOCK PASS** SHA256=`037b796c6203a0d8f5a025ca80ff8ab994734a029b05e378eec588735fc7f90b`
(V1 audio byte-identical; nothing re-voiced). 22 painted stills @ native 2K
(V1 had 10). 2 story-cast portraits (SAMUEL, ELI). Place: HOUSE (Shiloh
tabernacle hall) promoted-first from the person-free b01 anchor, wired to 17
beats — the Bethany lane was NOT taken (QC ban honored).

### COMPLAINT LEDGER
**none open** — `v2_outline.py 104` shows zero filed complaints for this row.

### Gates / lessons checked
- **SCALE GATE (lesson 14):** Samuel stays child-sized against Eli and the hall
  furniture in every multi-figure frame (s04/s06/s11/s12/s13); Eli ordinary
  adult; no giant. PASS.
- **BEARD BOARD (lesson 13):** Eli holds one full white beard + white hair in
  every frame (s04/s06/s08/s10/s11/s12/s13/s14); no appear/disappear/recolor.
  Samuel is a beardless child throughout. PASS.
- **The calling voice is NEVER visualized** (rendering law, rows 101/102): no
  light, figure, or glow for God's voice — only the boy's reactive/listening
  stillness (s05/s16/s17/s19). PASS. The lamp of God (real multi-wick oil lamp /
  seven-branched menorah, gold and low) is the scene's only symbol.
- **Realistic-only (Law 14):** every frame photographic; no cartoon/CGI mix.
  (b06 reroll #1 came back as a stylized CGI render — caught and rerolled to a
  photographic single; see FIX-WAVE/reroll log.)
- Time-of-day: night throughout → first gold dawn at the epilogue (b21/b22),
  one direction. Historical: first-century tabernacle, oil lamps, clay/wood,
  no modern objects.

### Rerolls (4 images / 22 beats = 18.2% — OVER the 15% budget; explained)
- **b06 ×2:** batch take was a stacked 3-panel COLLAGE triptych (row-66 action
  triptych class) → reroll #1 landed a stylized CGI/animated-film render (Law-14
  mix fail) → reroll #2 (its 2nd/last allowed attempt) landed a clean
  photographic single (boy running toward Eli's room). A cartoon frame is a hard
  fail I cannot ship, so the 2nd attempt was mandatory; this is the sole cause of
  the reroll overage.
- **b07 ×1:** boy stared dead into the lens → rerolled to him looking off-frame. FIXED.
- **b14 ×1:** boy's tunic reads TAN not the story-consistent NAVY. ROOT CAUSE:
  the b14/n4 beat carries only the ELI ref (`[+1 char ref: ELI]`), no SAMUEL ref,
  so nothing enforces his blue tunic; a reroll re-drifts (confirmed — the reroll
  came back tan too). Runner cannot edit the beat (hard rail). **FIX-WAVE for the
  author: add the SAMUEL ref to beat b14** so his navy tunic locks. Kept the best
  take.

### FIX-WAVE (kept best take, no reroll — cost/authoring)
- **b21:** epilogue dawn portrait is a mild front-on lens-look; kept to stay
  near the reroll budget (least story-breaking of the lens frames).
- Minor footwear (barefoot vs sandals) and sleeve-length (long vs short)
  drift on Samuel across frames — small, not story-breaking.
- **b14 tan tunic** (see reroll log) — author ref fix, not a runner reroll.

### Cost
Row spend ≈ **$3.73** (2 portraits $0.27 + 22 stills $2.94 + 4 rerolls $0.52) —
well UNDER the $6.10/row average (COST LAW $ trend DOWN), though reroll % (18.2%)
is above 15% for the one b06 cartoon-escape reroll noted above.
