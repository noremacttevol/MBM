# QC / RUNNER HANDOFF — build-134-today-in-paradise (Luke 23:39-43; John 20:17)

AUTHORED FROM SCRATCH, 2026-08-05 (Machine A). `--check` PASSES, zero
WARNs. 18 beats, ~103 s. Cameron asked for this story BY NAME
(2026-07-20 repeat purge): "more geography to mercy than
one-heaven-one-chance allows. Asks the better question, names
nothing."

## Canon locks carried byte-identical (face/place-board against them)

- HILL + THIEF = build-95 (same Calvary, same penitent thief, cold
  grey overcast). Crucifixion canon absolute: chest-up, NO wounds,
  no nails detailed, no blood, ever — b03-b08.
- TOMB + MARY = build-98 (same garden tomb, same Magdalene,
  first-gold Easter morning). Risen Jesus natural — cream, warm,
  NO wounds, no shining — b10/b11.

## Paradise "names nothing" (b14/b15/b17/b18)

The waiting country is deliberately MODEST: green meadows, stream,
olives/cypress, lifting mist. NEVER gates, thrones, clouds of
glory, or final-heaven spectacle — automatic reject. b15's path
runs THROUGH and onward to brighter undetailed hills — the
in-between is the doctrine. b18: the Shepherd walks among resting
figures — natural, no shining.

## The two-doors pair (b01/b02) and the scroll pair (b09/b12/b13)

- b01 shut / b02 opened-wide: same wall, same doors — prop-board.
  No flames or theatrics behind them ever.
- The two scroll fragments: same table, same lamp, finger on FIRST
  (b12) then SECOND (b13); script indistinct throughout.

## Plate rejections (both wires wrong)

- HILL: build-38 doorway frame rejected (not Calvary) — anchor on
  build-95's approved frames.
- TOMB: build-37 PARABLE-tomb frame rejected per build-95's written
  law ("never the build-37 plate") — arid, no garden. ALSO FIXED:
  row 97 itself was latently carrying this same wrong wire;
  removed there too. Take 97/98's approved garden frame when one
  is promoted.

## Coverage shape

One true wide with stated geometry: b18 (camera across the meadow
from the rise, the resting country from the side). Six Jesus beats
(b03, b05, b06, b10, b11, b18). Grey Friday → gold Sunday → soft
morning is the row's engine — keep the light discipline exact.
File order = story order here.

- b16 mourner: comforted grief, dignity total; no trapdoor imagery.
- REST promote-first from b14.

## 🅿️ RUNNER PARK — NOT AUDIO-READY (2026-08-11, Machine A `Dev`, $0)

**Blocked before ANY credit — no stills generated, meter untouched.** IDENTICAL
audio-not-wired block to row 133 (parked same session). Measured: the V1 dir
`media-production/build-134-today-in-paradise/` has NO `*.mp4`; its `audio/`
holds only `.timing.json` (**0 `.mp3`**); `beats_v2.py` has no
`AUDIO_FROM_V1_SEGMENTS` (grep 0). Every buildable sibling (rows 100/105/108)
has all three; this row has none, so neither `v2_assemble` audio path can run
and `extract_beats.extract(134)` crashes on the missing mp3 durations. The V2
dir `media-production-v2/build-134-today-in-paradise/audio/` DOES have all 10
fresh mp3s (Aug 5) — the V1 build reached `segs/` but never landed its final
mux + `audio/*.mp3`.

**RESUME (author / audio lane):** copy the 10 V2-dir mp3s into
`media-production/build-134-today-in-paradise/audio/`, set
`AUDIO_FROM_V1_SEGMENTS = True` in this build's `beats_v2.py`, verify
`extract_beats.extract(134)['total']` succeeds and `rebuild_audio_from_segments`
finds all 10, THEN the picture runner builds the beats on that audio (REST
promote-first from b14). Ready ✅ cleared on AUTHOR-BOARD until then. Runner will
not restore V1 audio or edit beats_v2.py (hard-protection #1 + audio-immutability).

## ✅ AUDIO-WIRED → BUILDABLE (author/audio lane, Machine A `Dev`, 2026-08-11, $0)
Same fix as row 133. Copied all 10 V2-dir mp3s
(`media-production-v2/build-134-today-in-paradise/audio/{n0..n5,j1,j2,s1,card}.mp3`,
all 44100 Hz / 128 kbps mono = new-voice ElevenLabs) into
`media-production/build-134-today-in-paradise/audio/`, set
`AUDIO_FROM_V1_SEGMENTS = True` in beats_v2.py. Pre-flight PASSES:
`extract_beats.extract(134)['total'] = 116.57`, `v2_prompt --check` PASS (18 beats),
`audio_audit` flags 0 old-voice. Board → Audio OK, Ready ✅. Normal picture build
for the Opus runner (REST promote-first b14).

---

## SHIP NOTE — realistic-v2 FIRST CUT (Opus runner, Machine A `Dev`, headless, 2026-08-13)

**COMPLAINT LEDGER: none open** (`v2_outline.py 134` shows no filed Cameron complaint). Built to spec.

**REPLACED-story reconciliation VERIFIED ($0) before spending:** wired audio transcribes as today-in-paradise (Luke 23:43 thief "Lord remember me" / "today shalt thou be with me in paradise" + John 20:17 "touch me not"), NOT the stale other-sheep story it replaced; distinct from the dupe (#159 other-sheep). All 10 V1-dir mp3s 44100/128k = new-voice ElevenLabs. `AUDIO_FROM_V1_SEGMENTS=True` already set by the 08-11 audio lane.

**Wiring the runner added (runner-legal reuse, not scene/lock/beat content):**
- REFS: THIEF ← build-95 `CAST-REF-V2/thief.jpeg` (byte-identical, same penitent thief as #95); MARY ← crop of build-98's approved Mary (s10) → `CAST-REF-V2/mary.jpeg`. The build shipped with REFS absent → THIEF (4 legible beats) would have flipped (RUNNER-LESSONS rows 52/55/63/153/177).
- PLACE_REFS: HILL ← build-95 `PLACE-REF/hill.jpeg`; TOMB ← build-98 `PLACE-REF/tomb.jpeg`; REST ← promote-first from b14 (s14) per QC.md.
- OUTPUT_VIDEO_NAME set (REPLACED row has no V1 mp4 → name can't be inferred, RUNNER-LESSONS row-140).

**FULL-CUT GATE on the RENDERED mp4 — 18/18 beats + card PASS.** Realistic photography throughout (Law 14, no cartoon/mix). CONTENT-CARE held: crucifixion (b03/b05) rope-bound, chest-up/distant, NO wounds/nails/blood ever; risen Jesus (b10/b11/b18) natural — cream, warm, no wounds, no shining/halo; paradise (b14/b15/b17/b18) names NOTHING — modest garden-country, no gates/thrones/glory. Jesus canonical (green/hazel ref-true eyes, NOT brown-edited — rubric lesson 20) across all his frames; THIEF one grey-bearded man (build-95); MARY one dark-haired woman (build-98). Two-doors (b01 shut / b02 open), scroll-pair (b09/b12/b13 lamp on spout, finger first→second). SPEAKER LAW pixel-verified: narrator WHITE, thief's plea "Lord remember me" BLUE (scripture), Jesus "today shalt thou be with me in paradise" (j1) + "Touch me not" (j2) RED — both land on Jesus frames. Card clean, bottom-band captions. Transcript matches narration exactly; drop-check concat_base 18 == 18 BEATS; AUDIO REBUILD PASS SHA256 a192ad42.

**Rerolls: 7 (b03 ×1, b04 ×1, b11 ×5) = 39% — OVER the 15% COST-LAW budget.** Honest overage, ALL mandatory defect-driven (none drift-chasing):
- b03: stacked double-exposure (row-95 crucifixion-hill double magnet) → 1 redo landed a clean single.
- b04: lens-stare on the thief → 1 redo landed him chest-up on the cross, gaze lifted.
- b11 "touch me not": the row-98 prose-driven contact trap — 4 blind rerolls oscillated (touching↔drifted-face). Hardened `must_not_show` with an explicit no-contact ban (enforcing the scene's OWN "hand's-breadth from his sleeve / a pause, not a rejection" intent + the caption), then 2 more redos landed a canonical Jesus face AND a clear no-contact gap — the doctrinally-correct "touch me not."
Absolute row gen cost ≈ $3.35 (25 gens) — UNDER the $6.10/row average (COST-LAW absolute trend holds DOWN), but reroll RATIO over ceiling, driven entirely by the doctrinally-critical b11.

**LESSON for the memory:** on a Jesus↔woman "reach / touch-me-not" beat, HARDEN `must_not_show` with a no-contact ban FIRST (row-98), do not blind-reroll — blind rerolls oscillate touch↔face-drift and burn budget.

---

## RESUME-SHIP (Opus runner, Machine A `Dev`, unattended/headless, 2026-08-13)

The prior autopilot lane DIED after building + gating the whole cut but BEFORE
shipping (no committed mp4, no review card, no deploy; AUTHOR-BOARD still RUNNING,
Claim A-auto). Resumed per RUNNER PARALLEL-LANES resume branch.

- **Already-shipped check FIRST:** no committed mp4 in build-134 (`git ls-tree`),
  no `id="v134"` on the local page OR the live reviewer → NOT shipped. So resume
  the ship, do not tick BUILT-and-walk.
- **Staleness check (RUNNER-LESSONS row-63):** `beats_v2.py`/`QC.md` mtime 11:15 is
  AFTER the mp4 (09:25) — but the 11:15 diff is ONLY generation-side wiring
  (`OUTPUT_VIDEO_NAME`, b11 `must_not_show` no-contact hardening, `PLACE_REFS["REST"]`);
  none touch assembly/captions/windows. Asset s11 (the b11 redo) landed 09:19; all
  c-clips 09:23–24; mp4 09:25 — the mp4 POSTDATES every asset incl. the b11 fix, so
  it is fresh, not stale. Assembly-correct for the current beats_v2.py.
- **Re-ran the mechanical gate ($0):** `v2_prompt --check` PASS (18 beats, v4
  checklist); audio lock 116.60s mp4 / 116.57s audio, 44100/128k ElevenLabs;
  `concat_base` 18 == 18 BEATS (no dropped-beat, RUNNER-LESSONS row-173).
- **Re-ran the FULL-CUT GATE 6b MYSELF on the RENDERED mp4** (I am the shipping
  session — never trust a prior note's claimed pass, RUNNER-LESSONS row-146):
  extracted one mid-window frame per beat from the 18 c-clips + card + 6 caption
  frames from the final mp4, viewed EVERY one. **18/18 beats + captions + card CLEAN.**
  - Crucifixion (b03/b05/b06/b08) rope-bound (no nails), chest-up/distant, NO
    wounds/blood; b11 "touch me not" shows a clear air-gap between Mary's fingers
    and Jesus's raised hand (no contact — the doctrinally-critical frame is
    correct). Risen Jesus (b10/b11/b18) natural cream, no halo/shining/wounds;
    green/hazel ref eyes, ordinary scale, canonical locked face every Jesus beat.
    THIEF one grey-bearded man (build-95) across b04–b08; MARY one dark-haired
    woman (build-98) b10/b11. Paradise (b14/b15/b17/b18) names NOTHING — modest
    garden-country, no gates/thrones/glory. Two-doors b01 shut / b02 opened onto
    morning country. Realistic photography throughout (Law 14, no cartoon/mix); no
    modern objects; anatomy/hands clean.
  - Captions bottom-band only: narrator WHITE (b01), scripture BLUE (thief's plea
    "Lord, remember me…", b06), Jesus RED (j1 "Verily…in paradise", b06; j2 "Touch
    me not…", b11). Reflection card clean serif, no typo-squares.
  - Subtle-only (fix-wave, NON-blocking, not runner scope): mild crucifixion-attire
    variance (b06 clothed vs b05 loincloth) and scroll-reader tunic-tone drift
    (b12/b13). Neither is obvious garbage nor repeats any complaint.
- **COMPLAINT LEDGER: none open** (`v2_outline.py 134` shows no filed complaint;
  `.approvals.json` has no row-134 entry — never approved, never complained).
- **Outcome:** cut verified CLEAN and shipped AS-IS, **NO re-cut ($0/0 rerolls this
  resume session)** — a clean cut is not touched. AUTHOR-BOARD RUNNING→BUILT;
  QUEUE Built✅ (Appr untouched — Cameron's alone). Deployed to Firebase +
  live-verified.

---

## INDEPENDENT QC-VERIFY PASS — 2026-08-13 (Opus runner, Machine A `Dev`, headless)

Second, independent FULL-CUT GATE 6b re-run before Cameron's eyes reach the
Unwatched queue (the row-11 "seven bad frames reached him" failure this pass
exists to prevent). Row is BUILT + shipped but **NOT approved** (`.approvals.json`
has no row-134 entry → untouchable-approved check PASSES, this row is mine to
verify). **COMPLAINT LEDGER: none open** (fresh-authored story, no filed complaint
→ no resolved complaint to regress).

- Extracted ONE mid-window frame per beat from the RENDERED mp4 (18 beats via
  c000-c017 clip windows) + the reflection card, viewed EVERY one:
  - **18/18 beats + card CLEAN.** All realistic photography (Law 14, no
    cartoon/mix). Jesus ONE locked face across b04/b05/b09/b10/b17 (dark wavy
    hair, full beard, green/hazel V2 eyes, Middle-Eastern) — cream robe/loincloth
    ONLY on Jesus, no halo/glow/rim-light, ordinary scale. Easter "touch me not"
    gap held on b09/b10 (clear air between Mary's hand and his). Thief rope-bound,
    NO wounds/nails/blood (authored mercy choice held). No modern objects, clean
    anatomy/hands (5 fingers on every visible hand incl. b05 crop), no extra limbs,
    no head-swaps. Captions bottom-band only — narrator WHITE, Jesus KJV RED
    (b05 "Verily I say unto thee…", b10 "Touch me not…"). Reflection card clean
    serif, no typo-squares.
  - **b05 examined at crop:** the wooden shapes near the two men's chins are the
    CROSSBEAM ENDS their wrists are bound to (roped bindings visible in b04) — a
    solemn cross-to-cross exchange on SEPARATE crosses at natural distance, NOT a
    "too close/kiss" framing. Not a defect.
  - **b17 examined at crop:** no second cream-Jesus — the walking cream-robed
    figure is unmistakably Jesus; seated background figures are grey/oatmeal
    disciple robes at rest (expected for "the Shepherd among people at rest").
- **FIX-WAVE (minor, do NOT re-cut):** a couple of pale-oatmeal background
  shawls in b17 sit close to cream in tone — below the glance-read bar, same
  class as row 145's flagged background-diner tone drift. No re-cut warranted.
- **Live-verified:** live review.html card data-hash `4621a1576a47…` matches
  local; mp4 URL serves real bytes (HTTP 206, application/octet-stream). Audio
  rebuilt 116.57s (AUDIO REBUILD PASS on ship, byte-identical new-voice).
- **Outcome:** cut CONFIRMED CLEAN. No re-cut ($0/0 rerolls). Claim marked
  **QC-OK 2026-08-13**. A clean approved-pending cut is not touched.
