# QC / RUNNER HANDOFF — build-105-face-to-face (Exodus 33-34)

Lesson-12 + complaint-corpus pass done 2026-08-05 (Machine A). `--check`
PASSES, zero WARNs. 26 beats, ~148 s.

## GOD RENDERING (the strictest content-care row — the build's own law)

The LORD is NEVER embodied: no figure, face, shape, silhouette, or
LITERAL HAND anywhere. The pillar of cloud is CLOUD; the covering hand
of v22 is a deep sheltering SHADOW folding over the cleft while
brilliance passes. Face-to-face intimacy is carried by Moses's posture
and warm near light inside the tent. Any embodied render = automatic
reject. (Row 113's complaint — "God has a body" — is a NARRATION-
doctrine matter for that row; the no-depiction law here is about
imagery and stands regardless.)

## Moses (new anchor)

~80, powerful, long grey-white beard per lock — face/beard-board across
~20 frames (beard-QC). His SHINING face (b24-b25) is bright skin the
onlookers react to — luminous complexion, NO rays, no halo, and he
himself unaware ("he wist not" — his manner ordinary while others
shield their eyes). Moses's approved face should seed row 67's
transfiguration MOSES (glorified, older-of-days — family resemblance
note in whichever builds second).

## Coverage shape

Two true wides with stated geometry: b04 (every man at his tent door —
down a tent-row behind the watchers) and b06 (the pillar descending —
far back behind the watching camp). Eight flips including b26's
PERSON-FREE closing tent and the tight cleft sequence (b22 — pressed
in the cleft, shadow folding over: the row's most delicate frame,
TIGHT by design).

- The lone tent's APARTNESS is spatial in every tent frame (distance
  readable to the camp rows).
- Direction: the walk OUT crosses the open ground toward the in-frame
  tent; the shining descent comes DOWN toward the camp.
- CLEFT promote-first from b21; CAMP/TENT from b01.

---

## RUNNER PARK — 2026-08-06 (Opus autopilot, Machine A `Dev`), $0 pre-flight

STALE-V1-FINAL: the V1 mp4 was rendered 2026-07-24 but all narration mp3s are
NEWER (2026-07-29) — v2_assemble's recency gate refuses AUDIO LOCK, and row 106
also fails the duration gate (|Δ|=6.61s). Copying the V1 mp4 would ship stale
voices. The runner is forbidden to re-voice or edit beats_v2.py (audio
immutability). NO credits spent — parked at step 2 before any generation.
RESUME (author): add `AUDIO_FROM_V1_SEGMENTS = True` to this row's beats_v2.py
(renders narration from the V1 build's own mp3s at extract_beats offsets,
nothing re-voiced), then this row is BUILDABLE. See the row-92-100 batch and
rows 74/78/80 for the same fix.

## ✅ RUNNER BUILT + SHIPPED — 2026-08-13 (Machine A `Dev`, Opus runner, headless)

**COMPLAINT LEDGER: none open** (`v2_outline.py 105` shows no OPEN reviewer complaint). First V2 realistic build of this row.

- **26/26 realistic stills**, Moses locked by promote-first plate (MOSES from s05) → consistent ~80yo grey-white-bearded man in madder-red-over-charcoal across all 25 appearances; CAMP/TENT from s01, CLEFT from s21 also promoted. Face/beard-board PASS.
- **GOD NEVER EMBODIED** (build's own strictest law): pillar of cloud is cloud (b06/b11), face-to-face intimacy carried by warm tent light (b07/b09/b13/b15), the cleft glory is brilliant light passing (b21/b22/b23), covering = sheltering shadow. No figure/face/hand/silhouette anywhere. b26 person-free closing tent.
- **3 rerolls / 26 = 11.5%** (≤15%): b06 (was stacked triptych + steam → single-frame pillar of cloud), b10 (was ambiguous over-shoulder partner → solo warm Moses), b24 (was full halo-burst on shining face → localized facial shine, people shielding eyes, per author's "bright skin, no halo" law). ~$3.89 Gemini (29 gens × $0.134), under the $6.10 baseline.
- **AUDIO REBUILD PASS** SHA256 `8f3417de…` (AUDIO_FROM_V1_SEGMENTS=True, 18 V1-dir new-voice mp3s, 164.3s — nothing re-voiced/re-timed).
- **FULL-CUT GATE** on all 26 rendered beats + caption frames + question card: captions bottom-band only (white narration / green scripture), question card clean margins, no modern objects, anatomy/hands clean, no cream robe, no lens-stare.

## 🔎 QC-VERIFY-FIX — 2026-08-13 (Machine A `Dev`, Opus verify pass, headless)

Full-cut gate re-run on the shipped cut BEFORE Cameron's eyes reached it (row was
BUILT + Unwatched, NOT approved — approvals.json 105 approved:false). Extracted one
frame per beat from the RENDERED mp4 and viewed all 26 + both card frames.

**ONE defect found → fixed in ONE touch-once re-cut (2 rerolls of b24 only, 1/26 = 3.8%, ≤15%; ~$0.27 Gemini):**
- **b24 (shining face, `s24`)** shipped with a harsh WHITE LIGHT-BURST concentrated
  ON THE EYES — read as glowing/white demon-eyes, the exact defect the beat's own
  `must_not_show` forbids ("no halo or ring of light — the SKIN of the face itself
  bright") and that Cameron has filed as a complaint THREE times on other rows
  (67 "eyes turned into light... looks like a demon", 94 "eyes are Lake white and
  looks evil", 96). Rerolled ×2 → radiance now sits as a soft backlight bloom
  behind/around the head with NATURAL downcast eyes; three onlookers shield their
  eyes; Moses unaware. Verified in the rendered mp4 at t=134.0s.
- All other 25 beats + both question-card frames were CLEAN and were NOT touched.

**AUDIO UNCHANGED** — re-assemble printed the same SHA256 `8f3417de…` (AUDIO_FROM_V1_SEGMENTS,
164.3s). The review card's "audio byte-identical" claim stays true. Only the s24
picture changed. Redeployed + live-verified. COMPLAINT LEDGER: none open (this was
a pre-emptive quality catch, not a filed complaint).
