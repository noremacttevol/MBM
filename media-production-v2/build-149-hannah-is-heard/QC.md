# QC / RUNNER HANDOFF — build-149-hannah-is-heard (1 Samuel 1)

AUTHORED FROM SCRATCH, 2026-08-05 (Machine A). `--check` PASSES, zero
WARNs. 22 beats, ~126 s.

## ✅ INDEPENDENT COMPLAINT RE-AUDIT 2026-08-13 (Codex, Machine A `Dev`)

Cameron's legacy complaint has no `complaintHash`, so the Reviewer kept this already
replaced cut in red. I did not trust the green card: extracted 124.5/125.5/126.0/
126.5/127.5-second frames from the exact MP4 and transcribed 123–131 seconds. At
exactly **2:06**, the visible caption is **“When he was weaned”** while the audio says
“She kept her word. When he was weaned, she brought him to the house of the Lord and
left him there to serve.” They are correct and synchronized; the old frozen-caption
tail is absent. Closing card at 132.5/138.5 is clean. `verify-mp4.sh`, full decode,
new exact content receipt, and `admin/qc_gate.py` with Whisper PASS. Current MP4:
139.620998 s / 20,179,467 B / standard SHA-256
`5300bc0a73407a851494f510dc8326160ef46fb4bf0048589ce8fce12eda6989`.
No video/audio/picture bytes changed in this audit. Reviewer card receives the audited
legacy-replacement marker so this existing replacement can finally move from red to
**Fixed — check your complaint**, while the complaint text stays visible.

## 🅿️ COMPLAINT LEDGER — OPEN complaint ROOT-CAUSED to the dead-tail class (2026-08-07, Machine A `Dev`, $0 Fable-5 author lane)

- **OPEN Cameron complaint (`v2_outline.py 149`): "Wrong caption at 2:06."** ROOT CAUSE =
  the **trailing dead-tail / frozen-caption** family (same class as rows 83 & 86 — "13 extra
  seconds on the end... cut off as soon as the voice stops"). **Measured:** the live V1 mp4
  (`media-production/build-149-.../1-samuel-1_hannah-is-heard.mp4`) runs **139.62 s**, but the
  narration + card content ends at **126.2 s = exactly 2:06** — Cameron's timestamp lands on the
  narration-end point. So a **13.4 s dead tail** freezes the final caption on screen past the
  voice; that lingering/mis-timed caption at 2:06 is what he flagged.
- **Source is CORRECT — no author text error:** every caption text matches KJV/narration and the
  2-voice colouring is right (Hannah's prayer = WOMAN pink; Eli's blessing s1 = SCRIPTURE light
  blue; card = narrator). Nothing in beats_v2.py / make_narration.py reproduces a *wrong* caption;
  the fault is purely the over-long V1 render's tail.
- **🅿️ RUNNER — do this (this row has 0 stills → you BUILD the fresh V2):** the V2 assembler's
  **TAIL GATE** (row-74/86 lesson) fixes this automatically — the picture ends when the closing
  card begins and the final mp4 ends on the last word (rendered mp4 tail ≈ the standard TAIL
  constant, NOT +13 s). **VERIFY at assembly:** captioned.mp4 duration ≈ card seg_start (±0.2 s)
  and final mp4 duration = audio total exactly (no trailing dead-air); then eyeball the closing
  caption at the 2:06 narration→card boundary (w4 "…as long as he liveth…" light-blue → card).
  Ship with a card telling Cameron the end was trimmed to the last word (no more frozen caption).
  If, once built, a *specific* caption is still wrong at 2:06 (not just the tail), localize it
  against the delivered mp4 and fix that segment — but the measured evidence is the dead tail.

## Hannah's dignity (rows 44/74 class, strictly)

Barrenness = the empty lap + the yearly ache — never abject, never
hysterical. The silent prayer (b03/b04) is the row's centre: LIPS
MOVING, NO SOUND, tears bright — no wailing gestures ever.
Tear-tracks stay UNWIPED in b15.

## The vow's gesture-language (the row's signature)

Asking hand drawn IN at the chest / giving hand open OUT toward the
sanctuary — b05 (in), b06 (the turn out), b09 (BOTH at once), b10
(the whole posture). Check the hands across these four as a set.

## Order-of-events gates

- b17's eased face comes BEFORE any answer — NO child, NO sign in
  frame; faith's receipt only. A child in b17 is a reject.
- Samuel's ages: newborn (b18) → toddler (b19) → small boy ~4
  (b21/b22). Face-board the ageing; his little olive tunic is the
  mother's yearly gift.

## Eli's arc

Weary error (b11, never malice) → focusing (b12) → compassion
(b14) → full blessing (b16, hand raised) → gentle hand on Samuel's
shoulder (b22). One old man, five registers.

## The leaving (b22, direction law exact)

Hannah walks AWAY down the morning road, back straight, steps even,
tears allowed; Samuel at the door under Eli's hand, both watching
her go. Broken AND at peace — both must read.

---

## ✅ RUNNER — SHIPPED 2026-08-13 (Machine A `Dev`, Opus runner, headless)

**COMPLAINT LEDGER (LEARNING LAW):**
- **OPEN complaint "Wrong caption at 2:06" — FIXED and byte-verified in the
  rendered mp4.** Root cause was the frozen/dead-tail class (V1's picture caption
  froze during the trailing seconds). This fresh V2 cut fixes it: extracted the
  rendered frames at 125.5s / 127.5s (= 2:05–2:07) and the caption is the CORRECT,
  synced narrator line ("She kept her word… she brought him to the house of the
  LORD and left him there to serve.") over the correct picture (s22, Hannah walking
  away) — NOT a frozen/wrong caption. Then a clean, narrated closing card
  (131.6s→139.2s, "Hannah prayed the prayer no one else could hear, and God
  answered. Your quiet prayers are heard too."), ending ~1.6s after the last word.
  Transcription proof: audio is fully narrated to ~138s (no 13s dead tail); final
  video 139.17s vs audio 139.62s (video ends on/before audio; no trailing dead-air).
  AUDIO LOCK PASS (SHA256 eb5cb45e…) — audio byte-identical to the V1 mp4, nothing
  re-voiced. Review card answers Cameron in his words.

**BUILD:** 22 realistic-V2 stills, first-attempt, **2 rerolls / 22 = 9.1%**
(under the 15% COST-LAW budget), 3 reused-forever portraits (HANNAH/ELI/SAMUEL,
the SAMUEL sheet is a deliberate newborn→toddler→boy age panel). ~**$3.62**, meter
$630.7→$634.4 — under the $6.10/row average (cost trend DOWN).
- Reroll 1 — **b03** (s03-one-year-at-shiloh): first take was a 3-panel COLLAGE
  triptych (RUNNER-LESSONS collage class) → rerolled to one coherent frame (Hannah
  kneeling at the tabernacle door, period clay saucer lamp).
- Reroll 2 — **b20** (s20-forget-me): first take rendered a MODERN glass-chimney
  hurricane/kerosene lamp on the post (modern-object class) → rerolled to a period
  clay oil lamp.

**FULL-CUT GATE (6b) — PASS on the RENDERED mp4** (every beat's source AND rendered
frame viewed, + 3 caption-type frames + card + the 2:06 boundary):
- Identity ONE actor each: Hannah (dark hair, blue-grey dress + rust shawl),
  Eli (aged white-bearded priest), Samuel (newborn→toddler→boy ~4, the age-order
  gate held: b17 has NO child/sign, faith's receipt only ✓). Scale gate PASS.
- Realistic-only (no cartoon/mix/collage after rerolls); period props throughout
  (clay saucer lamps every scene, wooden benches/chairs, wattle laundry draped not
  pegged); no modern object after b20 reroll; no anatomy/hand faults; OT story so
  no Jesus/cream-robe surface (jesus_face_gate N/A).
- Captions: 3-voice colour scheme correct — NARRATOR white, HANNAH/woman-KJV pink,
  SCRIPTURE (Eli's "Go in peace… grant thee thy petition") light-blue; all
  bottom-band only, never over the art, synced to audio; closing card clean
  (cream, centred, no squares/margin faults).
- The vow gesture-language set (b05 in / b06 turn-out / b09 both / b10 posture)
  reads; Hannah's dignity held (silent-prayer centre, unwiped tears b15, no
  wailing); Eli's five registers read; the leaving (b22) direction-law exact
  (walks AWAY, looks back, Samuel at door under Eli's hand).

**FIX-WAVE (minor, non-blocking, logged not rerolled — COST LAW):** one background
incidental toddler reads light-haired in the crowd wides (s01/s19); Eli's soft cap
appears/absent across frames (his full white beard is consistent — beard-board
PASS). Neither is a Cameron-complaint-level defect; not worth a reroll.

**No new RUNNER-LESSONS defect class** (collage + modern-lamp already catalogued).

## Other gates

- The other wife: ONE frame (b02), a smug glance — not cartoon
  cruelty.
- b20's brow-on-the-doorpost intimacy — tears on the wood.
- Dusk lamps physical (deliberate dusk for the prayer sequence).

## Coverage shape

One true wide with stated geometry: b01 (camera across the court
past the milling families' backs). No Jesus beats (OT row). File
order ≠ story order (b09 at 47s before b10's 42s, b20 at 40.92s) —
build by WINDOW.

- Plates: none auto-matched (clean). SHILOH promote-first from b03.
