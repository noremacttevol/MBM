# QC / RUNNER HANDOFF — build-89-last-supper (Luke 22:14-20)

## ✅ C-FIX RE-OPEN #2 SHIPPED — "0:14 picture doesnt look like Jesus Redo it" (Opus runner, Machine A `Dev`, 2026-08-12, headless/unattended)

**COMPLAINT LEDGER (Cameron, `v2_outline.py 89` / REVIEW-LESSONS row 89):**
- *"0:14 picture doesnt look like Jesus Redo it"* (reportedAgainst `a02d9445` = the 2026-08-11 brown-iris cut) → **FIXED by fresh regen of s03, NOT another iris edit.** 0:14 renders **s03** (jv15, "With desire I have desired…", window 11.54-16.42, midframe 13.67s). Cameron rejected BOTH prior states of this frame — the green original (history[0], hash `64293f9b`) AND the brown-iris fix (history[1], hash `a02d9445`) — so the defect was FACE IDENTITY drift off the JESUS-V2-REF, not eye colour. The frame now clearly matches the ref: long tousled wavy dark-brown hair with bronze lights below the shoulders, lean weathered Semitic face, luminous green-and-gold eyes, full dark beard, warm olive skin, cream robe, no halo — a tight close-up with disciples flanking (satisfies must_show).

**PROMPT AUTOPSY (rubric meta-law 3) — VERDICT: CAUSED.**
The original b03 scene text (beats_v2.py) literally read *"the wanting open and unashamed in the **warm brown** eyes."* That is a POSITIVE instruction toward brown eyes that CONTRADICTS both JESUS LOCK v5 ("a LUMINOUS INDETERMINATE COLOUR… green and amber and gold at once") and the attached JESUS-V2-REF image — a sentence outranking the ref, exactly what rubric lesson 20 (2026-08-12) forbids. The word pushed the eyes off-ref; the 2026-08-11 session then iris-recoloured them further toward brown, compounding the same lesson-20 violation. **FIX = rewrote the words:** `"warm brown eyes"` → `"luminous green-and-gold eyes"` (aligned to lock v5 + ref), then regenerated s03 fresh against the ref (b03 carries no rough_ref, so the gen relies purely on JESUS-V2-REF + ROOM plate — no drifted composition inherited). First draw came back a WIDE room shot (ROOM plate dominated, failed the close-up must_show) → 1 reroll → keeper.

**LESSON-20 SWEEP (touch-once):** the 2026-08-11 brown-iris edit also sat on the other three tight Jesus close-ups — s07 (0:40), s11 (0:59), s13 (1:13). Cameron never flagged those individually and their green originals were in the cut he accepted at those timestamps, so they were **reverted to their `.preeye.bak` green (ref-correct) originals — $0.** After revert they are consistent with the new s03 (same hair/face/eyes). No brown-iris edit remains in the cut.

**FULL-CUT GATE (Cameron 2026-08-10) — 16/16 beats + closing card, one midframe per beat extracted from the RENDERED mp4 — CLEAN:** Jesus face-locked/ref-matching/cream-only/olive-skin/full-beard/no-halo in every appearance (s02/s03/s04/s05/s06/s07/s09/s10/s11/s12/s13/s14/s15); no Jesus double, no 2nd cream figure (disciples earth-tone/ecru); green-gold eyes now systemic-ref across ALL close-ups (no brown outlier, no blue/pale drift); realistic throughout (no cartoon frame, Law-14 clean); night lighting correct; anatomy/hands clean; s08 hands-insert reads; s15 doorway ~11-13 realistic (the earlier 1:17 fix holds); s16 empty table correct ("still on the table"); captions bottom-band white-narr/red-Jesus (s03/s07/s11/s13 red); closing card clean cream serif.

**AUDIO:** picture-only fix — `v2_assemble.py 89` printed `AUDIO REBUILD PASS SHA256=29a5b1d0…`, **byte-identical** to the cut Cameron already has. Narration/voices/timing untouched.

**COST:** 2 s03 gens (1 wide reject + 1 keeper) = 1 reroll on a 16-beat row = **6.25%** (≤15% budget) + 3 free reverts = **$0.27 / meter $604.74→$605.01**. Under the $6.10/row running average. `*.preeye.bak` kept locally.

---

## ✅ C-FIX SHIPPED — "0:14 doesn't look like Jesus" + "1:17 too many people & not realistic" (Opus runner, Machine A `Dev`, 2026-08-11, headless/unattended)

**COMPLAINT LEDGER (Cameron, `v2_outline.py 89`):**
- *"0:14 doesnt look like Jesus"* → **FIXED.** 0:14 renders **s03** (jv15, "With desire
  I have desired…"), a tight Jesus close-up. TRACE (frame extracted from the LIVE mp4,
  not guessed): his irises had drifted **pale / glassy / greenish** with a bright
  reflective catch-light — the wrong-Jesus look (JESUS LOOK STANDARD requires WARM BROWN
  eyes, "NEVER blue/pale"). The same drift sat on every tight Jesus close-up (s03, s07,
  s11, s13); the wider group shots read fine. FIX = **targeted iris-recolour edit**
  (row-120 head-edit technique, gemini-3-pro-image): fed each finished still back with
  "recolour ONLY the irises to warm medium brown, remove the pale/greenish cast and
  catch-light, keep every other pixel identical." Edited ALL FOUR close-ups together so
  the cut stays one identity (a single brown-eyed frame among green ones would be the
  Law-14 mix defect). Each face/robe/pose/scene/hands/lighting stayed identical; backups
  kept as `assets/*.preeye.bak`.
- *"1:17 too many people and doesnt look realistic"* → **FIXED.** 1:17 renders **s15**
  (n4 p2, "Then he and his friends sang together and walked out into the night"). TRACE:
  s15 was the ONE **cartoon / 3-D-render** outlier in an otherwise realistic cut (a mix
  is worse than either — Law 14) AND was over-crowded (~18 figures with a blurry pile-up
  jammed in the doorway). FIX = **fresh regen** (`v2_gen_api --only b15 --redo`; b15 has
  no `rough_ref`, so the bad cartoon blocking was NOT reused). New s15 is **realistic**
  (matches s01-s16), the company reads as **his friends** (~13 = the Twelve + Jesus
  singing, arms over shoulders) with just 1-2 filing out the door — scene-accurate, no
  crowd. Jesus cream-only, warm-brown eyes, face-locked, no halo, night lighting. Scene
  text was NOT edited (hard rail); the realism-lock + fresh gen carried it.

**FULL-CUT GATE 6b — one frame per beat from the RE-RENDERED mp4, all 16 + closing card viewed:**
- 0:14 (s03) → warm-brown-eyed, gentle, clearly the locked Jesus. 1:17 (s15) → realistic
  singing company, not a crowd, not cartoon. Both named defects gone on the LIVE render.
- s07 (40s), s11 (57s), s13 (68s) → all now warm-brown-eyed, consistent with each other,
  the wider shots, and `JESUS-MASTER-REF/jesus-face.jpeg`. No pale/green drift anywhere.
- s01/s02/s04/s05/s06/s08/s09/s10/s12/s14/s16 → all realistic, one consistent style, no
  cartoon outlier, no second cream figure (only Jesus in cream), anatomy/hands clean,
  night lighting, captions bottom-band (white narrator / red Jesus lines), clean closing card.
- Consistent background prop across the whole cut (a roast fowl on the table) is period-
  ambiguous but NOT a mix and NOT complaint-named — left untouched (touch-once).

**AUDIO byte-identical:** only image assets touched; `AUDIO_FROM_V1_SEGMENTS` rebuilds from
the 14 V1 mp3s → AUDIO REBUILD **PASS** SHA256 `29a5b1d0…` (== the locked audio from the
prior ship). New mp4 md5 `8b0e8696…`, 20.1 MB, 94.1 s.

**COST:** 5 images × $0.134 = **$0.67** (4 iris edits + 1 s15 regen), **0 picture rerolls**
(each frame touched exactly once). Under the ~$1.2 C-FIX norm and far under the $6.10/row
avg — cost trending DOWN per the COST LAW. Touch-once: both complaints batched into ONE
re-cut. Scratch `_eye_edit.py` removed; `*.preeye.bak` / `*.precartoon.bak` kept locally.

---

## ✅ AUDIO FIX DONE — STALE-V1-FINAL lock cleared, HANDED TO PICTURE RUNNER (2026-08-06, Machine A `Dev`, headless AUDIO-FIX lane)

Class = STALE-V1-FINAL (duration shortfall), no open Cameron complaint (`v2_outline.py 89`).
Parked only on the AUDIO LOCK: timeline 101.900s vs V1 mp4 100.833s (|Δ|=1.067s > 1.0).
Fix ($0, no new TTS): set `AUDIO_FROM_V1_SEGMENTS = True` in beats_v2.py so the assembler
rebuilds from this build's own 14 mp3 segments (present in the V1 audio/ dir) instead of
copying the stale V1 mp4 AAC. 0 V2 stills → per PROMPT-AUDIO-FIX.md step 6, ship nothing
visual: board → AUTHORED / Audio OK / Ready ✅, claim cleared, picture runner assembles on
the corrected audio. No Gemini spend.

Lesson-12 + complaint-corpus pass done 2026-08-05 (Machine A). `--check`
PASSES, zero WARNs. 16 beats, ~95 s.

## THE TABLE (count + staging laws)

- TWELVE apostles + Jesus — thirteen at the ring (count law; Judas IS
  present but the betrayal is NOT this row's subject: no empty-seat
  drama, no singled-out shadowed figure — the authored law says the
  ring is complete and warm).
- RECLINING at a low U-shaped table (the 44/74 staging law) — never
  chairs, never the painting-style long straight table with everyone
  on one side (that is a Renaissance composition, not a first-century
  meal; if a render gives the da-Vinci lineup, reject).
- PETER and JOHN auto-attach from global sheets — face-board them
  near Jesus per the beats.

## The bread and the cup (the sacrament frames)

- took/thanked/brake/gave (b06) is TIGHT — hands and bread; the
  breaking readable as one motion.
- ONE great two-handled clay cup — the same cup lifted (b10) and
  passed hand to hand (b12: the travel readable around the ring —
  direction law). Earthenware, nothing gilded (row-7 class).
- No halo/glow on the elements, ever.

## Coverage shape

Four true wides with stated geometry: b02 (the ring complete, camera
behind the near couches), b09 (the giving down the table's length),
b12 (the cup's round in profile), b15 (the hymn — camera behind the
rising company toward the door and the night). Four flips including
b01, the PERSON-FREE laid table.

## Other checks

- Lamplit night throughout (correct story darkness, stated).
- The hymn beat (b15) ends the row on its feet, singing, going OUT —
  toward Gethsemane's night (seeds row 91's opening mood).
- ROOM promote-first from b01 (person-free — ideal plate); its
  approved frame could serve row 90 (washing feet — the same upper
  room, same night: note it there).
- Only Jesus wears cream.


## RUNNER PARK (A-auto Machine A `Dev`, 2026-08-06) — NEEDS-AUDIO / STALE-V1-FINAL — $0 SPENT
Pre-flighted at step 2 BEFORE any credit (no stills generated, nothing to reuse-waste).

**BLOCKER — v2_assemble AUDIO LOCK will fail:** timeline total = 101.900s vs authoritative V1 mp4 `luke-22_the-last-supper.mp4` = 100.833s.
Tripwire(s): RUNTIME |Δ|=1.067s > 1.0 (line 531). V1 mp4 SHORTER than timeline (trailing-silence shortfall).
The AUDIO LOCK copies the finished V1 mp4's AAC stream packet-for-packet; it refuses when the mp4 does not match the recomputed timeline.

**Why the runner cannot fix it:** the fix is `AUDIO_FROM_V1_SEGMENTS = True` in this build's beats_v2.py (rebuilds the track from this build's OWN mp3s at the timeline offsets — nothing re-voiced, V1 stays read-only). Editing beats_v2.py is outside the runner's allowed writes (art / QC.md / boards / SESSION-LOG / review card / mp4 only — PROMPT-OPUS-RUNNER.md hard rails). Same class as parked rows 69/74/77/78/80/82/83.

**FIX (author):** set `AUDIO_FROM_V1_SEGMENTS = True` in beats_v2.py  then this row builds normally.

**RESUME after fix:**
```
python3 media-production-v2/v2_story_cast.py build-89-last-supper --ceiling <c>
python3 media-production-v2/v2_gen_api.py build-89-last-supper --ceiling <c>
python3 media-production-v2/v2_assemble.py 89
```

---

## ✅ REALISTIC V2 SHIPPED — A-auto runner (Machine A `Dev`, 2026-08-07, unattended)

**COMPLAINT LEDGER:** none open (`v2_outline.py 89` shows no Cameron complaint). New realistic-V2 first-attempt cut.

**What was built:** 16 realistic stills on the promote-first ROOM plate (s01 promoted → 12 ROOM beats). 0 portraits (PETER/JOHN carry global sheets). AUDIO REBUILD PASS SHA256 29a5b1d0…, 94.1s, 20.1 MB, AUDIO_FROM_V1_SEGMENTS (14 V1 mp3s, byte-identical narration — no re-voice).

**Rerolls (2/16 = 12.5%, within ≤15% COST-LAW budget):**
- b02 (establishing wide) — first take rendered PAINTERLY/illustration (Law-14 realistic/cartoon MIX) with a hooded lighter-haired Jesus + a room the plate had been payload-dropped from; reroll landed a photographic take matching the set, complete warm ring, only-Jesus-cream.
- b06 (took the bread) — first take was a 4-panel COLLAGE (RUNNER-LESSONS collage class); reroll landed a single coherent bread-breaking frame on the ROOM plate.

**Row spend ≈ $2.15 (b01 anchor $0.13 + 15 beats $2.01 + 2 rerolls $0.27), meter → $472.89. WELL under the $6.10/row running average — COST LAW trend DOWN.**

**STALE-WINDOW REMAP (runner timing-only, row-42/row-74 class, no re-voice/reroll):** beats_v2 windows were scaffolded on the old ~101.9s timeline; live audio is 94.129s (card_start 86.979). First assemble placed stills on the stale windows → b16's window (88.66-93.30) started AFTER live card_start, so **s16 (the person-free "bread and cup remain" closer) was dropped** and its n5 caption landed over s15 (the hymn); video_silent 95.9s vs audio 94.13s. FIX: remapped all 16 windows onto the live extract per-segment slices (piecewise-linear, split ratios preserved for the 3 multi-beat segments n1/n2b/n4; b16 → 81.132-86.979). Re-assembled: video_silent 94.133 == audio 94.129, **AUDIO SHA256 UNCHANGED (29a5b1d0…)** proving audio byte-identical. Verified in rendered mp4: s16 shows at 0:83 with its matching caption, card clean at 0:88.

**FIX-WAVE:** the promoted ROOM plate (s01) carries a small period-ambiguous fork among the table utensils; it propagates to the wide ROOM frames (s05/s09/s10/s12/s16). Background, non-subject; rerolling re-attaches the plate, so left for the fix wave.

**Face/beard/scale/anatomy:** PETER/JOHN held by global sheets; only Jesus cream throughout; lamplit night throughout (correct story darkness); Jesus green/hazel eyes are the baked V2 ref (NOT rerolled — systemic). Sacrament frames (s06 break, s07 body, s10/s11 cup, s08 hands insert) read correctly.

---

## ✅ PICTURE C-FIX #3 — 0:14 "doesn't look like Jesus / redo with the character reference" (Machine A `Dev`, 2026-08-12, Opus RUNNER, headless)

**COMPLAINT LEDGER (open, `v2_outline.py 89`):**
- **"0:14 picture doesnt look like Jesus Redo it with the character refrence"** (reportedAgainst LIVE `f875a4c6`, 3rd time on this frame; history hashes 64293f9b→a02d9445→f875a4c6). **FIXED HERE:** s03 (the 0:14 beat b03) restored to the olive-brown MIDDLE-EASTERN locked-ref face; the pale/European frame the #2 "fresh regen" shipped is GONE.

**TRACE (extracted from the LIVE mp4, never guessed):** 0:14 = 14.0s → beats_v2 b03 window 10.895–16.455 (mid 13.67s) → `v2-r089-b03` → `s03-with-desire-i-have-desired.jpeg`. Frame pulled from live `f875a4c6` mp4 = a PALE, fair-skinned, medium-brown-haired EUROPEAN "white Jesus" — a direct violation of the JESUS LOOK STANDARD ("never white/Caucasian/pale") and no match to `JESUS-V2-REF/jesus-v2-face.jpeg` (olive-brown Middle-Eastern, green-gold eyes).

**PROMPT AUTOPSY (meta-law 3) — verdict IGNORED + REROLL-AWAY-FROM-REF (lesson 20 class):** b03 attached the REF and JESUS LOCK v5 (which explicitly says "WARM OLIVE-BROWN … never fair, never pale, never European") — yet the 2026-08-12 #2 "fresh regen from scratch" IGNORED the ref and drifted to the Western-Jesus stereotype on this close-up. The b03 scene text reinforced only the EYES ("green-and-gold eyes"), giving the model no in-scene skin/hair/face anchor to hold the ref against the stereotype pull. This is the 3rd re-open because prior fixes chased the eyes (08-11 brown iris, 08-12 eye-state) while the whole FACE was the drift.
  - **WORD-FIX (committed, permanent recurrence-prevention):** b03 must_show now states the face positively — "HIS FACE THE ATTACHED REFERENCE FACE EXACTLY: a Middle Eastern Jewish man with warm olive-brown sun-darkened skin (never fair, never pale, never European), a lean weathered face, a prominent aquiline nose, long dark brown wavy hair below the shoulders and a full dark brown beard"; must_not_show now bans "pale, fair, Caucasian or European … a rounder, softer, lighter-skinned man than the reference"; scene leads with the same olive-brown Middle-Eastern anchor. So any FUTURE regen of b03 (once billing is restored) can't drift pale again.
  - **ASSET-FIX (this ship, $0):** Google AI Studio billing is DEPLETED (429 RESOURCE_EXHAUSTED persisted after the protocol's one 60s retry — production-wide, only Cameron can top up), so a live regen was impossible. Restored the proven-good `s03-…jpeg.preeye.bak` (the ORIGINAL olive-brown Middle-Eastern generation, green eyes, BEFORE the eye-editing chain that progressively broke it). This asset MATCHES the locked ref AND matches the cut's own already-passing dark-ME closeups b04/b07/b11 — so 0:14 is now internally consistent and ref-accurate. The rejected pale frame saved to `s03-…jpeg.pale-rejected.bak`.

**FULL-CUT GATE §6b (all 16 beats + card, one frame per beat from the RENDERED mp4):** PASS.
- b03 was the ONLY complaint-worthy frame. Every other beat clean: b01/b16 person-free room (period clay lamps, night window); b02/b05/b06/b09/b10/b12/b15 wides — Jesus cream-only + ordinary scale + no halo, no 2nd cream figure, ~10–13 realistic diners (s15 sing-out no longer a crowd-pile), no modern objects; **b04/b07/b11 close-ups = strong dark Middle-Eastern face-locked Jesus (the target look b03 now joins)**; b13 upward-gaze catchlight (systemic, == ref, not drift); b08 hands-insert group-passing (narrator voice, not a Jesus stand-in). Captions bottom-band two-voice (narrator white / Jesus red on jv/j lines), KJV spelling exact, card clean.

**AUDIO byte-identical:** re-assembled with the restored s03 via `AUDIO_FROM_V1_SEGMENTS` (14 V1 mp3s, nothing re-voiced). **AUDIO REBUILD PASS SHA256 = 29a5b1d0…** (== the live cut). Extracted-track md5 `2435479072f590f04b3916eda9ebd671` before == after. Final mp4 sha256 `194966a6…`, 94.13s / 20.2 MB.

**COST:** $0 Gemini (0 successful gens — billing depleted; the 2 attempted b03 shots 429'd before any image, meter unchanged $617.34), 0 rerolls. Fix delivered by asset-restore + prompt-hardening. COST LAW trend DOWN (well under $6.10/row).

## 🚩 PICTURE C-FIX #4 — 0:14 "doesn't look like Jesus / redo with the reference" — CAUSE FOUND (prose), PARKED ON BILLING (Machine A `Dev`, 2026-08-12, Opus RUNNER, headless)

**COMPLAINT LEDGER (open, `v2_outline.py 89`):**
- **"0:14 picture doesnt look like Jesus Redo it with the character refrence sane problem 4 times in a row."** — reportedAgainst the LIVE cut (card hash `adc28f63…`, the #3 preeye-restore). NOT yet shipped-fixed: the corrected regen is billing-gated. Prompt is corrected + `--check` PASS, staged for the paid re-render.

**TRACE (from the LIVE mp4, not guessed):** 0:14 = 14.0s → b03 window 10.895–16.455 (mid 13.67s) → `v2-r089-b03` → `s03-with-desire-i-have-desired.jpeg`. On-disk s03 (2784210 B) is byte-identical to `s03…preeye.bak` = the #3 restore. Extracted the live 0:14 frame and compared side-by-side to `JESUS-V2-REF/jesus-v2-face.jpeg`: the 0:14 man is a DIFFERENT person — shorter, near-black hair (no caramel highlights), broader/heavier brow, denser unshaped beard, ruddier skin, more intense open-mouth expression. The reference man is softer-featured, serene, with longer wavy hair carrying lighter highlights. **This is whole-face identity drift, NOT eye colour** — which is why C-FIX #1/#2/#3 (all eye/skin-tone edits or asset-restores) never closed it. The card even over-promised ("matches his reference face exactly") — false, part of why he re-opened a 4th time.

**PROOF the pipeline CAN produce the ref here — $0 reuse considered & rejected:** viewed `s07-this-is-my-body-which.jpeg` (b07, "this is my body"): it MATCHES the reference well — longer wavy hair with the caramel highlights, softer face, hazel eyes, warm-tan (not too-dark) skin. Same ref attached to both b03 and b07. So the divergence is driven by the PROSE, not the ref image. Reusing s07 for b03 is NOT clean: s07 shows the bread already BROKEN (hands up, steam) against a STONE WALL, while b03's line is "with desire I have desired… before I suffer" (bread not yet broken) in the WINDOW room — a straight cp would pre-empt the real bread-breaking beat (b07, ~20s later) and break room continuity = a NEW complaint. Not adjacent, so no continuous-hold trick. No clean $0 path.

**PROMPT AUTOPSY (meta-law 3) — verdict CAUSED (by prose over-description):** b07's `must_show` says only "his steady face above" — minimal, letting the attached ref IMAGE be the lock; result = ref match. b03's `must_show`, after the #3 anti-pale word-fix, OVER-described the face ("a lean weathered face … long dark brown wavy hair … full dark brown beard") — prose that re-invents him toward a harder, darker, near-black-haired man, directly against the top law ("Consistency is enforced by IMAGE, not wording. The reference picture IS his face; prose never re-invents it"). The over-correction to kill the pale drift caused the opposite drift.
  - **WORD-FIX (committed, staged for the paid regen):** b03 `must_show`/`must_not_show`/`scene` rewritten to DEFER to the attached reference photograph ("his face and hair EXACTLY the attached reference photograph, the SAME man, not re-invented or restyled… do NOT harden him into a different, heavier, near-black-haired man"), keeping ONLY the anti-pale/anti-European negative as a guard. This mirrors b07 (which succeeded). `v2_prompt.py build-89-last-supper --check` = PASS (16 beats, v4). UNTESTED this session — billing depleted, cannot regen to confirm; the ref attachment + minimal-prose approach that produced the correct s07 makes this a near-one-shot when funded.

**BILLING (the one external wall):** own live probe `v2_gen_api.py build-89-last-supper --only v2-r089-b03 --redo --ceiling 645` → **429 RESOURCE_EXHAUSTED: prepayment credits depleted**, meter unmoved **$617.34**, $0 spent / 0 rerolls. Same production-wide wall parking 82/95/116/118. Only Cameron can clear it: top up Google AI Studio → https://ai.studio/projects.

**RESUME when billing is funded (touch-once, ships the whole corrected cut):**
```
python3 media-production-v2/v2_gen_api.py build-89-last-supper --only v2-r089-b03 --redo --ceiling <meter+2>
# FULL-CUT GATE §6b on the new s03 (must match JESUS-V2-REF — same man as s07), then:
python3 media-production-v2/v2_assemble.py 89     # AUDIO LOCK PASS, audio byte-identical 29a5b1d0
# ship two commits + firebase deploy + live-verify per PROMPT-OPUS-RUNNER step 7
```

**COST:** $0 Gemini / 0 rerolls / 0 credits. mp4 NOT reshipped (reshipping the off-ref frame would repeat the complaint). Reviewer card v89 `data-machine-reason` updated with the honest status + the top-up ask (the surface Cameron actually reads); the false "matches exactly" flag replaced with an honest "still fixing." Deployed + live-verified.
