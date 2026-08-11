# QC / RUNNER HANDOFF — build-150-shepherd-psalm (Psalm 23)

## 🅿️ RUNNER PARK → NEEDS-REBUILD (Opus runner, Machine A `Dev`, 2026-08-11)

**State:** 21 beats generated (native 2K), 18 clean + banked. Audio PRE-FLIGHT
PASS (buildable, not stale-V1). **3 beats blocked on AUTHOR beat-text — the
runner is barred from editing scene text (hard rail), so parked.** All frames
kept on disk; the author fix is $0 text, then the runner regenerates ONLY these
3 beats and assembles. Reroll budget spent: 4/21 = 19% (over the 15% cap —
see COST LAW note below; documented).

### BLOCKER — b21 (closing frame) is a STRUCTURAL DIPTYCH (REQUIRED author fix)
`v2-r150-b21` "both halves come home" names TWO places in one still — "in the
lamplit fold the flock lies folded... AND at the palace table the finished
scroll lies curled beside the quiet harp." That two-location text is a diptych
magnet (RUNNER-LESSONS lesson 481/954): **THREE takes all returned a hard
horizontal-seam two-panel collage** (young shepherd in the fold on top, old king
asleep at the desk on the bottom). Take 3 is photographic with a period clay oil
lamp (the cartoon style + modern kerosene lamp of take 1 are fixed), but it is
STILL a split-panel collage — the worst thing to ship as the CLOSING frame
(Cameron has complained about multi-panel frames). Reroll cannot fix a structural
diptych; it is an author beat-text job.
- **AUTHOR FIX:** de-scope b21 to ONE coherent single-frame scene, OR frame both
  halves in ONE continuous space with NO split/seam. Simplest: the lamplit stone
  fold at night — the flock folded and breathing slow, and on a bench/ledge WITHIN
  the same fold the finished curled scroll beside the quiet harp; ONE photographic
  frame, NO second palace-desk panel, period clay oil lamp only. (Or: the king
  asleep in his chair in the SAME lamplit room with the fold visible through a
  doorway — one continuous composition.)

### RECOMMENDED same pass — b11 & b16 age drift + b11 lost rod
The row is built on TWO ages, ONE face (QC below): KING (~50, royal blue, writing
frames b01/b04/b10/b12/b21) and YOUNG SHEPHERD (~17, ruddy, rust tunic, ALL field
frames). Per that design b11 (valley) and b16 (anointing) are field frames = young
shepherd — but their scene text lacks the explicit "young David"/"young shepherd"
cue that b13/b15/the pasture beats carry, so both rendered the MATURE KING in blue.
That leaves an age flip against the adjacent young frames (b13 young valley / b15
young at the table). A reroll does NOT move it (text-cue-driven, confirmed on both
b11 and b16 rerolls — RUNNER-LESSONS 1108/1112 family). Also the b11 reroll dropped
the ROD (its must_show requires "rod AND staff both visible" — the very "thy rod
and thy staff" line plays over it); the first take had both.
- **AUTHOR FIX (recommended, unifies the age + restores the rod in one pass):**
  b11 — add "the YOUNG shepherd (ruddy, seventeen, rust tunic)" and restore
  must_show "ROD (short club) in one hand AND STAFF (crook) in the other, BOTH
  clearly visible." b16 — add "YOUNG David (the guest from b15)" so the anointed
  head matches b15.
- (If the author instead INTENDS the older King David in the valley/at the royal
  banquet — a legitimate Psalm-23 reading — then leave b11/b16 old but still
  restore b11's rod, and it ships as-is.)

### RESUME (after the author edits b11/b16/b21 scene text + runs `--check`)
```
cd /home/noremacttevol/Desktop/MBM/media-production-v2
python3 v2_prompt.py media-production-v2/build-150-shepherd-psalm --check
python3 v2_gen_api.py build-150-shepherd-psalm --only v2-r150-b11 v2-r150-b16 v2-r150-b21 --redo --ceiling 608
# full-cut gate the 3 regens (age matches thread, rod+staff on b11, b21 single frame),
# then: python3 v2_assemble.py 150   (must print AUDIO LOCK PASS; pre-flight excess +0.485s OK)
# ship two commits + firebase deploy + live-verify per PROMPT-OPUS-RUNNER step 7.
```

### COMPLAINT LEDGER
Open complaint (`.approvals.json` 150, hash 4813ee79…): **"Bad old , english and
captions in white that are scripture."** Two parts, BOTH fixed structurally by the
V2 rebuild's 3-voice caption engine (verified at assembly, on the shipped cut):
- "captions in white that are scripture" → every KJV line (s1/s2/s3a/s3b/s4/s5a/
  s5b/s6a/s6b) is tagged `[scripture]` and renders in the SCRIPTURE colour (blue),
  never white; only the modern narrator paraphrase is white. Was white-tagged
  scripture in the old ASSEMBLY-C cut.
- "bad old english" → the narrator now speaks plain MODERN English; the archaic
  KJV wording appears ONLY as properly-attributed scripture (blue), so no "old
  english" sits in a white narrator caption. **Verify on the shipped mp4** by
  transcribing + reading caption colours per RUNNER-LESSONS 1105 (transcribe-diff
  the mp4 on the final assemble).

### COST LAW note
Row spend ≈ **$3.6** (1 DAVID portrait + 21 beats + 4 rerolls), meter $578.35→$582.10.
Rerolls 4/21 = **19%, over the 15% cap.** Breakdown: b16 (blood-like overflow →
acceptable wine, mandatory), b21 ×2 (closing-frame diptych — 1 to try to save the
ship, 1 to prove it is structural before parking) were justified mandatory attempts;
b11 ×1 was a low-value probe of a text-locked age (should have parked immediately —
see new RUNNER-LESSON). Row is PARKED not shipped, so no repeat-complaint risk from
the overage.

---

## AUTHORED FROM SCRATCH, 2026-08-05 (Machine A). `--check` PASSES, zero
WARNs. 21 beats, ~123 s.

## David has two ages, ONE face

KING (~50, royal blue, harp, writing frames: b01, b04, b10, b12,
b21) and YOUNG SHEPHERD (~17, rust tunic, sling, field frames).
Same features aged — face-board the pair hard; a different-looking
young David is a reject.

## The valley (b11/b13) — real dark, no death imagery

True deep gorge shade with the bright far doorway of daylight; NO
bones, spectres, or death imagery, ever. Rod AND staff both visible
in b11. b13 is the He→THOU discovery made physical: the ewe pressed
hard against his legs, his hand down on her head.

## The enemies (b14/b15) — far ridge silhouettes only

Vague, distant, unable to approach; never close, never armed in
detail. The guest's slow EASE at the table is the doctrine.

## Signature images (check exactness)

- b05: sheep LYING DOWN + GLASS-still pool (never rushing water).
- b07: the cast ewe restored — spent, not injured; the lift gentle.
- b16: oil poured on the head AND the cup running OVER onto the
  cloth — both in one frame.
- b18/b19: the shepherd BEHIND the homeward flock (pursuit
  position), then striding to close on a straggler — following as
  active chase.
- b20: the fold-house door OPEN, flock streaming IN at dusk.
- b21: the double rest — folded flock + finished scroll beside the
  quiet harp.

## Coverage shape

One true wide with stated geometry: b01 (camera into the chamber
past the harp's dark shoulder). No Jesus beats (the LORD as
shepherd is carried by David's own shepherding — never embodied
beyond the psalm's own imagery). Script indistinct everywhere.
File order ≠ story order (b04 at 5.12s, b10 at 15.21s) — build by
WINDOW.

- Plates: PASTURE promoted from b05 (person-free, clean), TABLE from
  b14 (person-free, clean). GORGE NOT promoted — b11 carries David
  (lesson 944: don't promote a figure-bearing frame; only 2 gorge
  beats, identity held by the DAVID ref).
