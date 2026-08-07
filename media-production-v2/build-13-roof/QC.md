# Story 13 Realistic V3 QC — The Man Through the Roof

## ✅ C-FIX 2026-08-07 SHIPPED — 1:40 MISSING-MAN **REGRESSION** root-caused + CLOSED (Opus runner, Machine A `Dev`)

**COMPLAINT LEDGER (this cut) — Cameron RE-FILED against the LIVE cut (`v2_outline.py 13`):**
> "1:40 picture is missing the man in it again, that was fixed previously but brought
> back now for some reason, it should have been deleted. picture at 1:49 still has ghost
> ropes and a weird room they are dropping him into. its a bad picture remove it."

**WHY IT SILENTLY REGRESSED (the root cause — this is the important part):**
The frame Cameron sees at **1:37 / 1:40 is `s17-easy-to-miss`** — its display window is
**96.109–103.412s** (from the schedule map at the bottom of `beats_v2.py`). s17 had rendered
Jesus + the four faces + ropes descending to an **EMPTY mat** — the man missing, and the ropes
running down to *nothing* (that is also exactly his "1:49 ghost ropes / weird room they are
dropping him into"). But every one of the **three** prior fixes rerolled **`s18-the-four-
sweat-streaked-faces`** (window **103.412–108.528s**) because that beat is literally NAMED
after the missing-man idea. The man was "restored" in s18 — a frame that plays **3–5 s later**
than the one Cameron actually looks at — so from his seat nothing ever changed and it read as
the fix being undone. Each prior fix even PASSED its own QC by checking s18 at 105.5 s, the
wrong timestamp. **s17 was never touched by any fix.** The lesson (timestamp→beat must come
from the shipped mp4 + window map, never the beat name) is now the top entry of
RUNNER-LESSONS.md → "C-FIX / COMPLAINT HANDLING".

**THE FIX (one reroll, the frame Cameron actually sees):**
- **b17 / `s17-easy-to-miss` rerolled once** against its OWN committed intent (`wide:False`,
  "Close on Jesus… his face tipped UP… looking at the men who made the hole, not at the man
  on the floor"). The prior render had disobeyed by widening to include an empty mat + ropes.
  The new frame is a clean close on the LOCKED Jesus (warm olive skin, dark wavy shoulder-length
  hair, full beard, cream robe, **no halo/glow** — the only light is the sunshaft through the
  hole) looking UP at the torn roof-hole in a legible basalt Galilean house. **No mat, no ropes,
  no empty room** → there is no longer any mat to be "missing a man," no rope leading to nothing,
  no weird empty room. The man remains correctly present on his mat in the neighbouring frames
  (s16 landed at Jesus' feet, s18 four-faces-with-mat, s19 close on the silent man), so the
  narrative is intact: man lands → Jesus looks up in gratitude at the friends → the four faces
  and the mat → the silent man.
- **Verified at Cameron's exact seconds in the RE-BUILT mp4** (the discipline the regression
  violated): **1:40 (100 s)** now = Jesus looking up, no empty mat/ropes; **1:49 (109 s)** = s19
  unchanged, four SOLID taut connected ropes, man present, legible roof — no ghost ropes.
  Question card @291 s clean serif on cream. Captions bottom-band white.

**ROOT-CAUSE HARDENING (so a shipped fix can't silently regress again):**
1. New top RUNNER-LESSONS rule: map complaint-second → asset via the `beats_v2.py` window table,
   extract that second from the SHIPPED mp4 to confirm the frame, fix THAT asset, and re-verify
   the SAME second in the rebuilt mp4 — never trust the beat NAME.
2. Prior ghost-rope ship had committed only the mp4, leaving s14/s15/s18 UNCOMMITTED (a
   `git checkout` would have reverted the shipped frames). **This cut commits the mp4 WITH all
   touched assets (s14, s15, s17, s18) in the same commit**; `git status assets-realistic/` is
   clean after ship. Added as a RUNNER-LESSONS rule too.

**COST / TOUCH-ONCE:** **1 reroll / 45 beats = 2.2%** (far under the 15% budget), **≈$0.13**
(meter $498.75 → $499.02 with concurrent lanes). Both of Cameron's timestamps traced to the ONE
empty-mat frame and fixed in ONE re-cut. **AUDIO byte-identical** — rebuilt from the same 23 V1
segment mp3s, **AUDIO REBUILD PASS SHA256=`da5d35f0d7badc48a384104f6b475cbb087090c3609acb11a152325dea1e063b`**
(the SAME hash as the prior ship — narration/voices/timing untouched), 298.3 s.

---

## ✅ C-FIX 2026-08-07 SHIPPED — ghost-rope / weird-roof complaint CLOSED (Opus runner, Machine A `Dev`)

**COMPLAINT LEDGER (this cut) — the open complaint on the row, in Cameron's words:**
> "1:44 the 4 friends are not standing on a roof with a hole in it it looks weird just get rid of
> that picture. 1:49 has ghost ropes and a weird room they are dropping him into. its a bad
> picture remove it."

Both named pictures were REBUILT (not left as-is) against the author's SOLID-ROPE / GHOST-ROPE-BAN
prose (rubric lesson 19), one re-cut, everything else byte-identical:

- **"1:44 four friends on a roof with a hole looks weird" → FIXED.** Rerolled **s18**
  (`s18-the-four-sweat-streaked-faces`, displays 103.4–108.5s = 1:43–1:48). The four distinct
  dusty friends now read UNMISTAKABLY as leaning over the edge of a real flat clay roof around a
  real torn hole; the paralysed man on his mat is present in the near foreground; ropes run down
  as solid taut cord. The old disembodied corner-arms / ambiguous opening are gone. Verified in
  the RENDERED mp4 at 105.5s.
- **"1:49 ghost ropes + weird room they are dropping him into" → FIXED.** Rerolled **s15**
  (`s15-swaying-on-four-ropes`, 90.0–92.9s) — the mat now hangs at a sensible mid-height on **four
  solid, opaque, taut ropes** connected roof-beam→mat-corner in a clean legible stone room, instead
  of the old mat floating high near the ceiling on faint ropes. Verified in the RENDERED mp4 at
  91.5s under the caption "lowered with enormous care." Also rerolled the companion lowering frame
  **s14** (`s14-four-faces-at-the-hole`, 85.5–90.0s) — same solid-rope, legible-room fix so the
  whole lowering sequence is consistent (no ghost ropes anywhere).
- **GHOST-ROPE BAN satisfied** on every rope in the re-cut: solid opaque physical cord, taut/slack,
  connected at both ends — never transparent, faint, floating or disconnected. Roofs read as real
  torn clay roofs. Four distinct friends (correct count), same four men across s14/s15/s18, no
  second cream-robed figure, no modern objects, no lens-stare.

- **COST / TOUCH-ONCE:** **3 rerolls (s14, s15, s18) / 45 beats = 6.7%** — under the 15% budget;
  ≈ **$0.40** this row (meter $494.33 → $494.73). Touch-once: both open picture complaints batched
  into ONE re-cut. **AUDIO byte-identical** — rebuilt from the same 23 V1 segment mp3s
  (`AUDIO_FROM_V1_SEGMENTS=True`), **AUDIO REBUILD PASS SHA256=`da5d35f0d7badc48a384104f6b475cbb087090c3609acb11a152325dea1e063b`**,
  298.3s. Nothing re-voiced, re-timed or resynthesised. Question card clean, captions bottom-band
  white serif.

---

## 🅿️ NEEDS-REBUILD — NEW open complaint AUTHOR-FIXED (2026-08-07, Machine A `Dev`, $0 Fable-5 lane)

**COMPLAINT LEDGER — this is a SECOND, still-open complaint** (the earlier "1:37 picture missing
the man on the mat" was already C-FIX-shipped; the review board's `latest` is now this one):
> "1:44 the 4 friends are not standing on a roof with a hole in it it looks weird just get rid of
> that picture. 1:49 has ghost ropes and a weird room they are dropping him into. its a bad
> picture remove it."

- **Root cause:** two render failures in the roof-opening / lowering sequence — (a) **GHOST ROPES**:
  the four lowering ropes rendered transparent/floating/disconnected (new **rubric lesson 19**);
  (b) the four-friends-over-the-hole + the lowering room read weird/warped and un-legible.
- **AUTHOR FIX ($0, no image gen):** added a hard **SOLID-ROPE requirement + GHOST-ROPE BAN** to the
  rope beats **b14** (s14 four faces paying rope), **b15** (s15 swaying on ropes) and **b16** (s16
  landing, slack ropes), and **roof-legibility + ghost-rope ban** to **b18** (s18 four faces at the
  hole). Ropes must now be solid opaque cord, taut/slack, connected hand→mat-corner; the roof reads
  as a real flat clay roof with a real torn hole. `--check` PASS (pre-existing b44/b45 wide-geometry
  WARNs untouched). Audio UNTOUCHED.
- **🅿️ RUNNER — do this (paid, targeted re-cut):** reroll the flagged lowering/roof frames
  (**s14, s15, s18** — the four-on-roof + rope-lowering shots at ~1:34-1:49) against the fixed prose;
  face/rope-board them. If a reroll STILL reads weird after ≤2 tries, **DROP the redundant b18**
  (b14 already covers four-faces-at-the-hole) rather than churn credits. Keep every other still
  byte-identical, **AUDIO LOCK byte-identical**, ship with a card telling Cameron the ghost-rope /
  weird-roof pictures were fixed.

Final candidate: `mark-2_man-through-the-roof-realistic-v3.mp4`

## Delivery proof

- 45 realistic 9:16 source pictures, normalized to 1882×3344 JPEG.
- Final: 1080×1920 H.264, 30 fps, 298.817007 seconds, 21,581,743 bytes.
- Final Git blob SHA-1: `069c50869a43e29d7eba902445adf0ccd028aa84`.
- Final SHA-256: `432a11dfffe90367f155c8f4944a3df2897f9ab6b468c039be22445d6fdbb49f`.
- Encoded-audio packet SHA-256: `1f7b80dfc50649b95e935efe939161f3b3f4b56965e6c219da84b8a4fb8b46a8`.
- `admin/verify-mp4.sh`: PASS; video and audio both reach 298.817007 seconds.
- Six recurring identities pass the hash-backed face-board gate: the paralysed
  man, all four distinct friends, and Jesus.

## Audio and script fidelity

- No narration was generated, shortened, substituted, or rewritten for this
  rebuild. The complete timeline contains all 23 existing tracked source clips,
  including all three Jesus sayings, both Scripture clips, and the full closing
  question. `AUDIO-SOURCE-MANIFEST.json` records each source hash and position.
- The checked-in V1 MP4 is a stale 258.967-second render, so it cannot be the
  complete audio authority. The existing source clips form the complete
  298.817-second timeline; the final copies that locked AAC master unchanged.
- Jesus is **Alexander**, not Chris. At commit `e0542b134` the shared engine maps
  Jesus to Alexander (`UMnEnzK9QLLdRwnUyxMW`), and that commit's `j1`, `j2`, and
  `j3` files have exactly the same SHA-256 hashes as the current source clips.
  A later non-ancestral branch did generate Chris, but those blobs are not in
  the current source set and are not in this cut.
- Punctuation is present in the Alexander take. Signal measurement finds 0.567s,
  0.878s, and 0.416s internal pauses in `j2`, plus a 0.625s pause in `j3`.

## Story and continuity proof

- The four friends are the same four distinguishable men throughout. Exactly
  four carry the mat, one per corner; all four work on and remain on the roof.
- The paralysed man keeps the same face, dark grey-brown clothing, and reed mat.
  The mat is carried level, lowered on four functional ropes, remains under him,
  is rolled only after Jesus' command, and is carried out by the healed man.
- The house remains a small dark-basalt Galilean house with a plausible flat
  packed-clay, reed, and beam roof. The hole admits daylight, dust, and straw.
- The scribes reason silently with closed mouths. Forgiveness occurs before
  physical healing; Jesus answers the unspoken reasoning; motion progresses
  from first effort to trembling stand, mat roll, and walking out.
- Jesus is not surrounded by an artificial worship circle. The crowded room has
  natural sightlines and actions, with the four friends separated above.
- Full-resolution checks rejected and replaced wrong headcounts, changing faces,
  missing roof friends, an airborne mat, misplaced indoor friends, premature mat
  movement, a duplicate paralytic, and a wrong standing identity.
- Late identity repairs corrected all four bearers in `s10`, all four roof faces
  and Jesus in `s17`, Jesus beneath the four-rope mat in `s15`, and the same four
  friends celebrating in `s44`.
- One decoded frame from each of all 45 final beat windows was inspected after
  crop, captions, and encoding. The command, first standing, mat roll, exit,
  Scripture close, and closing card occur in the right order and timing.

The reviewer replacement hash returns Story 13 to **Unwatched** while retaining
the prior picture complaint for comparison. The mobile app and app-feed video
remain unchanged.

## OPEN CAMERON COMPLAINT — gate before rebuild

"1:37 picture is missing the man on the mat" → beat v2-r013-b18
rewritten: shot from low inside the room so the man on his mat lies
soft in the near foreground UNDER the hole while the four faces ring
it above. The mat man must be PRESENT in the frame — his absence is
an automatic reject.

## COMPLAINT LEDGER (C-FIX 2026-08-07, Machine A Dev) — CLOSED

- OPEN complaint (only one on this row): **"1:37 picture is missing the
  man on the mat."** FIX: beat **v2-r013-b18** (`s18-the-four-sweat-streaked-faces.jpeg`,
  displays 103.4–108.5s) was rerolled ONCE against the author's rewritten
  scene. The new frame is shot from low inside the room: **the paralysed man
  lies on his reed mat across the near foreground**, ropes trailing from the
  mat corners, and all four dust-caked friends ring him from above under the
  broken roof hole. Verified in the RENDERED mp4 at 105.5s — the mat man is
  now the foreground subject; his absence (the exact defect Cameron named) is
  gone. Realistic, four friends (correct count), no Jesus in frame, no modern
  objects, caption in the bottom band.
- Rerolls this row: **1 / 45 beats = 2.2%** (well under the 15% COST-LAW budget).
- Touch-once: this was the only open complaint on the row; nothing else was
  changed. Every other still is byte-identical.

## AUDIO — unchanged, rebuilt from the identical V1 source clips

The checked-in V1 mp4 (`media-production/build-13-roof/mark-2_man-through-the-roof.mp4`)
is a **stale 258.967s** render, so the AUDIO LOCK's default copy-from-V1-mp4 path
refuses (STALE-V1-FINAL guard). Set `AUDIO_FROM_V1_SEGMENTS = True`: the
narration is rebuilt from the V1 build's OWN 23 mp3 segments at the extract_beats
offsets (same mechanism shipped on rows 61 and 69). `v2_assemble.py 13` prints
**AUDIO REBUILD PASS**. Nothing was re-voiced, re-timed, or resynthesised — same
words, same voices, same offsets. Both the old shipped v3 and this new cut measure
**-15.1 LUFS** integrated loudness; the only difference is 0.5s of trailing card
tail (298.3s vs the old 298.8s). The audio Cameron already heard is unchanged.
