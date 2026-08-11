# QC / RUNNER HANDOFF — build-95-thief-on-the-cross (Luke 23:39-43)

## ✅ QC-OK 2026-08-11 — FULL-CUT GATE 6b VERIFY-PASS on the re-shipped cut (Machine A `Dev`, unattended/headless, $0, 0 generation, NO re-cut)

**COMPLAINT LEDGER: none open** (`v2_outline.py 95` = beat/segment map only). This was a VERIFY-PASS on the BUILT row sitting in Cameron's Unwatched queue (mp4 `9059485916c1…`, cont.25's giant-composite re-ship) BEFORE his eyes reached it — the row-11 "quality is going down" mandate.

**Verdict: CLEAN — QC-OK, NOT re-cut** (the instruction is explicit: do not re-cut a clean row).

- Extracted ONE frame per beat (11) + the closing card from the RENDERED mp4 at each `beats_v2.py` window midpoint and viewed every one against the defect checklist + RUNNER-LESSONS.
- **b01 giant-composite RESOLVED, did NOT regress:** a true distant establish — three crosses far on the crest in silhouette, watchers small on the slope, city wall low behind, foreground watchers seen from behind at ONE consistent scale; no chest-up giants, no collage / composite / double-perspective, no haze seam.
- **Three-crosses geometry never swaps** (mocker LEFT / Jesus CENTRE-cream / thief RIGHT) across b01/b03/b05/b09/b11. **MOCKER (b02) + THIEF (b03/b04/b06/b08/b10) face-locked & consistent.** **Jesus face-locked every appearance** (b05/b07/b09/b11): warm Middle-Eastern, dark wavy hair, full beard, warm/green eyes; cream-only, no 2nd cream figure. **Rope-bound, NO nails / NO wounds / NO blood / NO gore anywhere** — merciful distance held.
- **Captions 3-colour correct:** white narrator, blue scripture (s40 @b03/b04, s42 @b07), RED Jesus (j1 @b09); bottom-band only; closing card renders clean (serif, centred, no squares/giant text).
- **faster-whisper transcription of the mp4 confirms caption↔audio↔picture SYNC:** every caption's words are actually spoken (NO ghost/stale caption — the row-84/cont.24 class is clean here), and Jesus's paradise line (50.76-54.88s, j1) lands on the Jesus frame b09 — **the desync fix HELD**. (The audio also speaks a redundant modern paraphrase "If you're really the Christ, save yourself and us" at ~8s — pre-existing, documented in beats_v2's DESYNC note, baked into the byte-identical delivered audio `e5ba558a`; the caption matches it, so it is in sync and NOT a picture defect a VERIFY pass re-cuts.)
- **Live-verified (assurance = gate output, not my word):** served mp4 md5 `6e807e29dd0456f06c7d4f077bd3a207` == local == the exact bytes I QC'd; live card `v95` hash `9059485916c1…`, NO `data-machine-reason` (correctly in Cameron's Unwatched queue). No deploy needed (clean, already live).
- **FIX-WAVE (logged, NOT blocking, NOT re-cut — same precedent as sibling crucifixion rows 94/96 QC-OK):** soft cross-frame wardrobe variance (Jesus in the full cream robe b05 vs bare-chested/loincloth b07/b09/b11 — John 19:23-24 garments-parted, each frame individually reverent) + warm golden light on the b09/b10 emotional-peak frames vs the row's cold-grey overcast elsewhere. Each frame is individually reverent and scripturally defensible; cross-frame soft-continuity harmonisation is the fix wave's job, not a verify re-cut (touch-once/cost law forbids voiding a pending approval + burning credits chasing subtle drift).

---

## ✅ GIANT-COMPOSITE RESOLVED + RE-SHIPPED — AUTHOR-FIX 2026-08-11 (Machine A `Dev`, unattended/headless, $0, 0 rerolls, 0 generation)

**The QC-VERIFY park below is CLOSED.** The b01 giant-composite/scale defect is fixed —
$0, no Gemini spend, no reroll (rerolls were proven unwinnable), audio byte-identical.

### Root cause (was in the beat wiring, not the model)
The prior b01 was authored `wide:True, jesus:True, ref:REF, locks:[HILL, MOCKER, THIEF]`
— it attached the Jesus + MOCKER + THIEF tight face-crop REF portraits onto an OPENING
ESTABLISHING WIDE. On a wide, those tight portraits paste in as giant chest-up foreground
figures over a miniature crowd (the "giant/composite" class); the worst reroll pasted them
as literal framed rectangles on the crosses. The model was never the problem — the beat was
asking for a portrait collage.

### The fix (author-lane, fix-spec option 1 = "person-free HILL-plate establish")
1. **Re-wired b01 to mirror the row-94 b01 that PRODUCED this build's HILL plate**:
   `wide:True, jesus:False, ref:False, locks:["HILL"]` — no character REF portraits at all.
   Scene/must_show/must_not_show rewritten to a TRUE distant establish (three crosses in far
   silhouette on the crest, watchers small on the slope, city wall low behind, ONE coherent
   photograph at one scale; explicitly forbids giant/chest-up foreground figures + collage +
   haze seam). The sneer and every face are now covered only in the singles that follow (b02+).
2. **Used the HILL plate directly as s01** (`cp PLACE-REF/hill.jpeg assets/s01…jpeg`) — it IS
   a person-free realistic distant establish of this exact Calvary (rows 94/95 are the same
   hill in sequence, so a shared establish is clean continuity). $0, zero generation.
3. **Re-assembled** (`v2_assemble.py 95`): AUDIO REBUILD PASS `SHA256=e5ba558a…` — byte-
   identical audio, only s01 changed, the 10 good stills + all 11 windows untouched. New mp4
   file sha256 `9059485916c18009…`, 70.7s / 19.7 MB.

### Proof (FULL-CUT GATE on the NEW mp4)
- Frame @3.5s & @6.5s (b01) = a distant establishing wide — three crosses far on the crest,
  watchers small in the foreground, city wall behind, correct single-photograph scale, NO
  giant portraits / NO composite / NO haze seam, realistic, no gore. Captions bottom-band:
  n0a white "Two criminals were crucified with Jesus…", s39 light-blue "If thou be Christ…".
- Frame @53.5s (b09, red-letter "…to day shalt thou be with me in paradise") = Jesus's locked
  face (cream robe, warm Middle-Eastern) turned full to the penitent thief — the desync fix
  did NOT regress; both men face-locked.
- `v2_prompt.py --check` PASS (11 beats). Face gate: v4 checklist PASS.

### Shipped
Reviewer card `v95`: `data-machine-reason` removed (back into Cameron's Unwatched queue),
`data-hash`→`9059485916c1…`, `?v=9059485916c1`, "what changed" rewritten to tell Cameron the
opening giant/scale problem was fixed. Board State NEEDS-REBUILD→BUILT. Deployed + live-
verified. **No approval voided** (row was in Unwatched, never Approved). Touch-once, $0.

---

## 🛑 QC-VERIFY → RUNNER PARK — NEEDS-REBUILD (FULL-CUT GATE, 2026-08-11, Machine A `Dev`, unattended/headless) — ✅ RESOLVED ABOVE 2026-08-11

**The desync fix below is CONFIRMED holding, but b01 (the opening 0–8s establishing
wide) carries a GIANT-COMPOSITE / SCALE defect that must NOT reach Cameron. Pulled from
his Unwatched queue (card `data-machine-reason`). State flipped BUILT→NEEDS-REBUILD so the
AUTHOR lane owns it — this is a BEAT-TEXT / structural fix, not a runner reroll.**

### What I verified (FULL-CUT GATE — one frame per beat from the RENDERED mp4)
Extracted mid-window frames for all 11 beats + the card and viewed every one.
- **10 of 11 CLEAN** (b02–b11 + card): three-crosses geometry holds (mocker L / Jesus
  C-cream / thief R, never swapped), MOCKER + THIEF face-locked and consistent, rope-not-
  nails / no gore throughout, cream-only-Jesus, JESUS face lock intact, eye-lines connect
  on the exchange beats (b07/b09/b11), captions bottom-band, question card clean.
- **RESOLVED-COMPLAINT NOT REGRESSED:** the cont.19 desync fix holds — at mp4 52.4s (b09)
  Jesus's face is full-frame under the red-letter "To day shalt thou be with me in
  paradise"; b10 (58.5s) the thief receives "Today"; the promise lands on Jesus, not the
  thief-alone. Every checked line sits under its own picture.

### The BLOCKING defect — b01 giant-composite (the FIX-WAVE item, now a hard block under the 2026-08-10 gate)
The opening establishing wide is a structural double-perspective composite: three ENORMOUS
chest-up figures (mocker / Jesus-cream / thief) cut off at the hilltop crest with a visible
haze seam, floating over a correctly-scaled downslope crowd + distant city. The men are
grossly out of scale with the watchers — the "giant / composite" complaint class, and it's
the FIRST frame Cameron sees. The prior runner shipped it as a "coherent 2nd take" under
the old "no-obvious-garbage" bar; the FULL-CUT GATE (2026-08-10, row-11 seven-bad-frames)
KILLED that bar — anything that would make Cameron type a complaint now BLOCKS. b05 proves
the model CAN render this exact wide at correct scale, so this is a beat-composition problem,
not a model limit.

### Rerolls are proven unwinnable on this beat (do NOT burn more meter)
Three attempts now return garbage: prior runner's initial gen (floating heads + haze) and
1 redo (composite) — both giant-trio-over-tiny-watchers; **this QC-VERIFY's reroll (2026-08-11,
$0.13, ceiling $588.94) came back WORSE**: the three REF portraits pasted as literal framed
rectangles onto the tops of the crosses. Stopped after 1 reroll per COST LAW. The overwritten
s01 source was restored from the shipped mp4 so the folder stays consistent with the cut.

### AUTHOR FIX SPEC (beat-text change — runner is barred from this)
Make b01 a TRUE distant establishing wide: either a person-free HILL-plate establish, or drop
the giant foreground trio and place the three men at genuine distance on their crosses against
the grey sky, watchers small in front — so scale reads as one coherent photograph, not a
portrait collage. Do NOT re-add the REF portraits as foreground giants (that is what keeps
compositing). Then the picture runner regens ONLY b01, re-assembles (audio byte-identical —
AUDIO REBUILD PASS `e5ba558a`, the 10 good stills untouched), FULL-CUT-GATE the new b01
frame, and re-ships (deploy + live-verify, restore the card to the ready wave).

**No approval is voided** — the row was in Cameron's Unwatched queue, never Approved. The
audio + the other 10 beats are good; only b01 needs re-authoring.

---

## ✅ DESYNC RESOLVED + RE-SHIPPED — AUTHOR-FIX 2026-08-11 (Machine A `Dev`, unattended/headless, $0, 0 rerolls)

**The QC-BLOCK below is CLOSED.** The ~4s audio↔picture desync is fixed. No re-voice,
no Gemini spend, V1 untouched — a pure picture-window re-time + re-assemble.

### What was done (per the FIX SPEC below, option "re-time pictures to the audio")
The audio + captions are driven entirely by `extract_beats(95)` (the V1 timeline); the
beats_v2 `window` fields only control when the pictures SWITCH, and they had been
authored against a paraphrase-free reading, so they drifted ~4s behind the audio that
actually plays. Rather than surgically strip the paraphrases out of read-only V1 mp3s,
the 11 picture windows were re-set to a `faster-whisper` transcription of the DELIVERED
audio — every picture now switches ~0.2s before its own spoken line, contiguous, no gaps.
New windows: b01 0.00 · b02 8.00 · b03 16.10 · b04 20.90 · b05 29.45 · b06 31.90 ·
b07 39.05 · b08 43.75 · b09 48.05 · b10 56.70 · b11 60.40 (→ card_start 64.648).

### Proof (re-transcribed + frame-verified on the NEW mp4)
- Audio is byte-identical: AUDIO REBUILD PASS `SHA256=e5ba558a…` (same as before) — only
  picture timing moved. New mp4 file sha256 `21c7cd3568929f25…`, 70.7s / 19.9 MB.
- Frame @53.5s (caption "…To day shalt thou be with me in paradise", red-letter j1) =
  **Jesus's face turned full to the penitent thief** (s09). THE defect is fixed — the
  promise lands on Jesus, not the thief-alone.
- Frame @58.0s ("Today. Not someday…") = the thief receiving the word (s10). ✓
- Frame @13.0s ("That was one of them, sneering…") = the mocker (s02). ✓
- Frame @62.0s ("…faith of a criminal was enough.") = the closing two crosses (s11). ✓
- Every other line checked lands on its intended picture; captions and pictures agree.

### Shipped
Reviewer card repointed: `data-machine-reason` removed, `data-hash`→`21c7cd35…`,
`?v=21c7cd356892`, flag → QC-VERIFIED, "what changed" now tells Cameron the timing was
fixed. Board State NEEDS-REBUILD→BUILT. Deployed + live-verified; back in his Unwatched
queue. The paraphrases in the V1 narration (taunt in s39+n0b, "remember me" in s42+n3)
are pre-existing V1 audio content, not the reported defect, and were left untouched.

---

## 🛑 QC-BLOCK → RUNNER PARK — NEEDS-REBUILD (FULL-CUT GATE, 2026-08-11, Machine A `Dev`, unattended/headless) — ✅ RESOLVED ABOVE 2026-08-11

**The 2026-08-07 shipped cut has a whole-video AUDIO↔PICTURE DESYNC of ~4s and must
NOT reach Cameron. Pulled from his Unwatched queue (reviewer card given
`data-machine-reason` → "machine is fixing" bucket). State flipped BUILT→NEEDS-REBUILD
so the author lane owns it — this is a structural beat-timeline fix, NOT a re-voice, so
the audio lane's `AUDIO_FROM_V1_SEGMENTS` rebuild would only REPRODUCE the bug.**

### The defect (what Cameron would have typed)
The narration runs ~4 seconds BEHIND the pictures for the whole back half. The worst
moment: Jesus SPEAKS his climactic promise "…today shalt thou be with me in paradise"
at mp4 **52.8–54.4s**, but the picture on screen then is **b10 = the thief ALONE**
(Jesus already left frame at the b09→b10 cut). Earlier the narrator says "That was one
of them, sneering at him" (12.5s, about the MOCKER) while the picture is already the
**b03 wide REBUKE** (the penitent thief). Every back-half beat shows its picture ~4s
before its words are spoken.

### Root cause (proven, not guessed)
- `AUDIO_FROM_V1_SEGMENTS = True` → the assembler builds the audio track from
  `extract_beats.extract(95)`, which returns the **V1 10-beat timeline**. Its **beat 3
  is the modern paraphrase "If you're really the Christ, save yourself — and us"** and it
  has **no `n0b`**.
- `beats_v2.py`'s **11-beat PICTURE map** has **`n0b` "That was one of them, sneering"**
  in that slot and **no paraphrase** (matches `beats.json` and the 11 `audio/*.mp3`).
- So the delivered audio carries a **stray ~3.4s segment** (the paraphrase) that the
  picture windows never budget for → all audio after 8s slides ~4s late vs the pictures.
- **The AUDIO LOCK only compares TOTAL duration** (audio 70.67s ≈ video 70.70s), so a
  per-segment structural mismatch sails straight through the gate. A duration match is
  NOT a sync check.

### Evidence
- `python3 -c "import extract_beats; extract_beats.extract(95)"` → 10 beats, beat 3 =
  "If you're really the Christ, save yourself — and us."
- faster-whisper word timestamps of the delivered mp4: paraphrase spoken 8.12–11.56s;
  "Verily I say" 50.70s; "today…in paradise" 52.82–54.36s; "Today, not someday" 56.90s
  — every content onset ~3.5–4.3s later than the `beats_v2.py` window for that line.
- Frame at 54.25s (audio = "in paradise", Jesus's own words) → picture is the thief alone.
- Pictures themselves are CLEAN (three-crosses geometry, face-locks, rope-not-gore,
  cream-only-Jesus, realistic) — the ONLY defect is timing.

### FIX SPEC for the author lane (touch-once, then re-assemble + re-verify)
Reconcile the audio timeline to the v2 11-beat PICTURE structure. Preferred:
1. **Drop the redundant modern paraphrase** from row 95's audio timeline (the KJV taunt
   `s39` "If thou be Christ, save thyself and us" already carries the mockery; `beats.json`
   and `beats_v2.py` both omit the paraphrase by design). Make the audio the 11 v2
   segments (`audio/*.mp3`: n0a, s39, n0b, s40, n1, n2, s42, n3, j1, n4 + card) laid at the
   `beats_v2.py` windows — this makes audio == pictures (~60s + card).
   *(If `extract_beats`' hardcoded V1 timeline is the only audio path, correct row 95's
   entry there to the 11-beat v2 structure — this is why it's an AUTHOR fix, not audio.)*
   Alternative (costs a still): keep the paraphrase and ADD a 12th picture beat for it,
   re-timing every v2 window to the extract offsets.
2. Re-assemble (AUDIO LOCK PASS on total) **AND re-transcribe the new mp4** to PROVE
   Jesus's "…today shalt thou be with me in paradise" lands on a Jesus picture and every
   line sits under its own picture. Do NOT ship on the duration check alone.
3. Ship (deploy + live-verify), review card answers the fix in Cameron's terms, restore
   the reviewer card to the ready wave (remove `data-machine-reason`, set new `data-hash`).

**No Gemini spend needed if option 1 (audio-only re-map); the 11 stills are already good.**

---

## ✅ REALISTIC-V2 SHIPPED — A-auto 2026-08-07 (Opus runner, Machine A `Dev`, unattended) — SUPERSEDED BY THE QC-BLOCK ABOVE (desync found 2026-08-11)

**COMPLAINT LEDGER: none open** (`v2_outline.py 95` shows only the beat map, no
Cameron complaint). Nothing to answer; this is a first realistic-V2 cut on the
already-corrected STALE-V1 audio.

- 11 stills, 70.7s, **AUDIO REBUILD PASS SHA256=e5ba558a0d4910f922303bab51e25b1799744040284ad361cc2c50fe02f36974**
  (AUDIO_FROM_V1_SEGMENTS=True — narration rebuilt byte-identical from the 11 V1 mp3s).
- Timeline verified: max still-window 60.17 < live card_start 64.648 → no stale-window
  overrun (the row-74/89 batch risk); all 11 stills placed, no dropped beat, video 70.7s == audio.
- **Three-crosses geometry HELD:** mocker LEFT (thin, dark hair, sparse beard),
  Jesus CENTRE (only-cream), penitent THIEF RIGHT (grey-streaked beard) — sides
  never swap across s01/s03/s05/s07/s09/s11. MOCKER + THIEF face-locked via
  v2_story_cast REFS (the row-52/55 face-flip fix — two distinct men, consistent
  across every beat).
- **MERCIFUL DISTANCE held** (row 94's law): all bound by ROPE, no nails, no gore,
  no wound detail; closeness peaks at the two faces across the gap (s07/s09/s11).
- **Eye-line CONNECTS** on the exchange beats: s07 (request), s09 (reply), s11
  (the two turned heads across the gap). Only Jesus wears cream throughout.
- HILL plate taken from row 94's approved frame (`--take HILL=build-94:v2-r094-b01`);
  PLACE-WIRING.json carries ONLY HILL (no wrong build-38 wire crept in).
- **Rerolls: 2/11 = 18%** (both the mandatory composite-seam garbage class, same as
  row 94's s03/s10 on this passion block): s01 (floating cut-out heads + haze seam),
  s11 (stacked portrait+landscape diptych). s11 landed clean on 1 redo. Slightly over
  the 15% row budget by one frame — justified: two true-garbage frames, and s11's fix
  is a clear win. ~$1.74 row total (11 stills $1.47 + 2 rerolls $0.27 + 2 portraits
  $0.27 counted separately). Meter after: ~$482.94.

### 🅿️ FIX-WAVE (author beat-text, not a runner reroll)
- **s01/b01 establishing wide is a structural double-perspective composite.** Both
  the initial gen (floating heads + haze) and the 1 redo returned the giant-trio-
  over-tiny-watchers composite — the beat text asks for a far-off distant-crosses
  WIDE *and* names the three men prominently, so the model keeps compositing a giant
  foreground trio onto the distant hill (row-45-b46 / row-114 structural-collage
  class — not a coin-flip a runner can win, so kept the coherent 2nd take and did
  NOT burn a 3rd reroll per COST LAW). The 2nd take is coherent and reads the correct
  geometry (mocker L / Jesus C-cream / penitent R, three crosses, watchers), but the
  scale is off (trio giant vs distant people). AUTHOR FIX: make b01 a true distant
  establishing wide (person-free HILL-plate establish, or drop the giant trio /
  place the three at true distance on the crosses), then regen only b01.


## ✅ AUDIO FIX DONE — STALE-V1-FINAL recency lock cleared, HANDED TO PICTURE RUNNER (2026-08-06, Machine A `Dev`, headless AUDIO-FIX lane)

Class = STALE-V1-FINAL (recency), no open Cameron complaint (`v2_outline.py 95`). Parked
because the narration mp3s are newer than the V1 mp4 (2026-07-24), so the packet-copy AUDIO
LOCK would ship stale voices. Fix ($0, no new TTS): set `AUDIO_FROM_V1_SEGMENTS = True` in
beats_v2.py so the assembler rebuilds from this build's own 11 mp3 segments (present in the
V1 audio/ dir). 0 V2 stills → per PROMPT-AUDIO-FIX.md step 6, board → AUTHORED / Audio OK /
Ready ✅, claim cleared, picture runner assembles on the corrected audio. No Gemini spend.

Lesson-12 + complaint-corpus pass done 2026-08-05 (Machine A). `--check`
PASSES, zero WARNs. 11 beats, ~60 s.

## ⚠ HILL UNWIRED (same wrong build-38 auto-wire as row 94)

Golgotha shares ONE Skull across rows 94/95/96: take row 94's approved
HILL frame once it exists (--take HILL=build-94...). The --wire tool
will re-add the wrong build-38 wire on every invocation — re-remove it
if you rerun wiring.

## Merciful distance (row 94's law binds here identically)

Crosses at distance, no wound detail, no gore, ever. The row's
closeness peaks at the two faces across the gap (b07) — faces, not
bodies.

## The three crosses (identity + geometry)

- The cross-LINE: Jesus CENTRE, the mocker on one side, the penitent
  THIEF on the other — the sides NEVER swap between frames (row-83
  class: b03's rebuke crosses IN FRONT of the silent centre; b07's
  request crosses the gap between centre and right; if the thief
  changes sides, the geometry lies).
- MOCKER and THIEF are distinct men per their locks (face-board);
  the thief's arc — mocking silenced → honest reckoning → the ask →
  "today" — plays entirely in his face at distance.
- "Remember me" / "To day shalt thou be with me in paradise": the
  exchange is two turned heads across the gap — the eye-line must
  CONNECT (row 92's look law, at the hardest angle in the library).

## Coverage shape

Two true wides with stated geometry: b01 (the three against the grey,
behind the watchers) and b03 (the rebuke — all three in one profile).
Three flips — the request (b07) is the tight heart.

- Grey morning throughout; SOLDIERS if visible follow row 94's
  build-15 group ref.
- Only Jesus wears cream — already stripped here; the divided robe
  belongs to row 94's dice frames, not this row.


## RUNNER PARK — NEEDS-AUDIO (A-auto 2026-08-06, $0 pre-flight)

Parked BEFORE any Gemini spend. `assert_v1_final_is_current` FAILS: this row's V1 mp4 was rendered 2026-07-24 but all 9 narration mp3s it would lock to are NEWER (2026-07-29) — copying that audio stream would ship stale voices / deleted segments (STALE-V1-FINAL class, same as rows 69/74/78/80/82/86-90).
- DURATION gate: within 1.0s (recency is the blocker).
Runner cannot fix (audio-immutability; needs an author edit to beats_v2.py).

**AUTHOR FIX:** add `AUDIO_FROM_V1_SEGMENTS = True` to this row's beats_v2.py, then the narration renders from the V1 build's own mp3s at the extract offsets — nothing re-voiced, nothing re-timed.

**RESUME (after the flag is set):** re-run the OPUS RUNNER loop on this row — it will pass pre-flight, generate stills, assemble (AUDIO LOCK), and ship.
