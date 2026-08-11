# QC / RUNNER HANDOFF — build-95-thief-on-the-cross (Luke 23:39-43)

## 🛑 QC-BLOCK → RUNNER PARK — NEEDS-REBUILD (FULL-CUT GATE, 2026-08-11, Machine A `Dev`, unattended/headless)

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
