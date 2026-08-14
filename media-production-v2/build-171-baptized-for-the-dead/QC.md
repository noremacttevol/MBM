# QC — row 171, build-171-baptized-for-the-dead (1 Corinthians 15:29 + vv.20-22)

**Authored 2026-08-07, Machine A `Dev`, Fable-5 author lane, $0** (0 pictures
generated, 0 audio touched). `v2_prompt.py --check` PASS (15 beats, no warnings).
Windows contiguous + monotonic 0.400 → 73.427 (card_start), every segment onset
in-window. Audio column OK on AUTHOR-BOARD.

## COMPLAINT LEDGER (LEARNING LAW — one open complaint, ADDRESSED)
- **OPEN:** *"First picture is weird there are no scripture that roll like that on
  2 edges."* — The V1 first still put a SCROLL with rendered scripture text
  CURLING on two edges into the frame; it read as a fake panel / generated-text
  artifact. **FIXED in this map:** the new first picture (**b01**) is PEOPLE —
  Paul debating the Corinthians in a portico — and its `must_not_show` HARD-BANS
  any scroll, any parchment/paper with visible writing, any curling/rolling edge,
  any rendered letters/numerals, and any panel/border/frame along any side. AND
  **every one of the 15 beats** carries "nothing written anywhere / no scroll,
  writing or panel" in its must_not_show, so no frame in the build renders
  scripture text as art (captions are added later, bottom band only). The review
  card should tell Cameron the weird rolling-scroll first picture is gone.

## Speaker law
Paul's epistle — **s1, s20, s22 are all the SCRIPTURE voice → LIGHT-BLUE
captions, never red.** No Jesus-red, no God-voice. Jesus is embodied (risen Lord,
locked face + REF, cream) only on the two resurrection-anchor beats **b09** and
**b11**; the picture shows him because "Christ risen" is the concrete fact, but
the caption stays scripture-blue (s20) / narrator.

## Content-care (row 171 is GREEN, but the subject is the DEAD → restraint)
- The departed are shown with DIGNITY and HOPE — a mourner's remembering face,
  the ordinance done in love; **NEVER a corpse, never gore.**
- "the grave loses its grip" (b11) and "in Christ all made alive" (b13) are DAWN
  LIGHT + an EMPTY tomb + a living risen man + hopeful faces — **NEVER rising
  corpses, opened graves with figures climbing out, or zombies.**
- "reaches across the veil" (b14) is SOFT LIGHT only — **no ghost, spirit-figure
  or apparition** stands in it.
- The person "baptized for the dead" is a LIVING PROXY going into the water on
  behalf of one who died — **never a body in the water.**
- The risen Christ (b09/b11) is warm, solid, real — **not a ghost, not a glare;**
  no wound-gore. Scale gate applies.

## The doctrine made concrete (realistic, not V1's abstract metaphors)
Three real settings: **CORINTH-PORTICO** (Paul teaching, b01-b02), **BAPTISM-
WATER** (the proxy baptism + the remembering family, b03-b08, b14-b15), and
**RISEN-DAWN** (the empty tomb + the risen Christ, the resurrection anchor,
b09-b13).

## Locks
- **PAUL** — BYTE-IDENTICAL to rows 138/155/166 (cross-video same man; face
  carried by the text lock, no face sheet yet — same as those rows).
- **PROXY** (living believer baptized for the dead) and **MOURNER** (the departed's
  family) — build-local person locks, one consistent face each across their beats.
- **CORINTH-PORTICO / BAPTISM-WATER / RISEN-DAWN** — build-local place locks.
- **BACKGROUND-CAST** (shared) on multi-figure beats for distinct faces (lesson 3).
- Jesus: locked V2 face + REF auto-attached by the jesus/ref flags on b09/b11.

## RUNNER — do this (paid picture lane; audio is DONE and untouched)
1. Confirm `--check` PASS on this machine.
2. Generate **b01** (Corinth), QC, `--promote build-171-baptized-for-the-dead
   CORINTH-PORTICO <b01>`; **b03** (water), QC, `--promote … BAPTISM-WATER <b03>`;
   **b10** (empty tomb — NOT b09/b11, which are Jesus frames), QC, `--promote …
   RISEN-DAWN <b10>`; then generate the rest on the existing audio (Audio OK — do
   NOT re-voice; AUDIO LOCK byte-identical to V1).
3. **Face board (lesson 10) + beard board (lesson 13):** Paul one man (b01/b02);
   the PROXY one person across the water beats; the MOURNER one woman across her
   beats; the risen Jesus the locked V2 face (b09/b11).
4. **Restraint gate on every departed/resurrection frame** (b05, b10, b11, b12,
   b13, b14): no corpse, no gore, no rising bodies/opened graves, no ghost — dawn
   light and empty tomb only. **Scale gate** on Jesus (b09/b11) and multi-figure
   frames.
5. **First-picture gate (the complaint):** b01 must contain NO scroll, NO written
   text, NO rolling/curling edge, NO panel — verify in the rendered frame.
6. Assemble (`v2_assemble.py` — AUDIO LOCK PASS), technical gates, caption QC
   (bottom-band; s1/s20/s22 light-blue, narrator default), publish to review.html,
   ship with a card noting the weird rolling-scroll first picture is fixed.
7. **Reroll budget ≤15% of 15 = ~2 beats.** Two failed rerolls → FIX-WAVE, keep
   best, move on. Log $/row + reroll % vs the $6.10 average. Expected cost ~15 ×
   $0.20 ≈ $3.0 (all-new build, short row).

---

## RUNNER BUILD — SHIPPED 2026-08-13 (A-auto `Dev`, Opus runner, headless)

**COMPLAINT LEDGER (LEARNING LAW) — 1 open complaint, VERIFIED FIXED in the rendered mp4:**
- OPEN: *"First picture is weird there are no scripture that roll like that on 2 edges."*
  → **FIXED + gate-verified.** The frame that plays FIRST (0:00, b01 `s01-pauls-question.jpeg`,
  extracted from the delivered mp4) is PEOPLE — Paul debating skeptical Corinthians in a
  harbour portico. NO scroll, NO parchment/writing, NO curling/rolling edge, NO panel or
  border anywhere. Every one of the 15 beats bans rendered text; captions live only in the
  bottom band. The complaint cannot recur.

**Build:** all-new 15-beat build. 3 portraits (PAUL/PROXY/MOURNER, text-lock design — not
wired, matching rows 138/155/166) + 15 stills. **0 rerolls (0% vs 15% budget).** Promote-first:
CORINTH-PORTICO←b01, BAPTISM-WATER←b03, RISEN-DAWN←b10 (empty tomb, NOT a Jesus frame).

**Cost:** ~$2.40 Gemini total (3 portraits ~$0.40 + 18 image pulls) — **well under the
$6.10/row baseline; 0% rerolls beats the 19% average** (COST LAW trend DOWN).

**Assembly (runner timing-metadata, no re-voice/reroll):**
- Set `AUDIO_FROM_V1_SEGMENTS = True` + `OUTPUT_VIDEO_NAME` — the V1 mp4 (82.6s, old
  ASSEMBLY-C spacing) does not match `extract_beats` (live 74.45s), so the track is rebuilt
  from the 12 V1-dir segment mp3s at the current-pipeline offsets (proper LEAD/GAP spacing).
  Segment mp3s are byte-identical content — audio is the same ElevenLabs narration.
- **Window remap (row-42/89 fix):** the authored beats_v2 windows ran to 73.427 (a stale,
  inflated scaffold) while live card_start = 66.672. That dropped the final still (s15) and
  drifted every still vs its caption. Remapped all 15 windows piecewise onto the live
  segment slices (split multi-beat segments by authored width ratio; last beat → card_start).
  Result: 15/15 stills placed, video 74.47s ≈ audio 74.45s, stills synced to captions.
- `AUDIO REBUILD PASS` SHA256 `95ac6e5e…`; final mp4 `1-corinthians-15_baptized-for-the-dead.mp4`.

**FULL-CUT GATE (per-beat frames from the RENDERED mp4 + 3 caption frames + card): PASS.**
- b01 first-frame: complaint fixed (verified above). Upright, no rotation on any sampled frame.
- Jesus b09/b11: locked V2 face consistent, cream-only, ordinary scale, ref-true green eyes
  (NOT brown-edited — lesson 20), calm gaze, no halo/rim-light, no wound-gore.
- Content-care (the DEAD → restraint): living proxy in the water (never a body), empty tomb +
  dawn (never rising corpses / opened graves / zombies), "across the veil" = soft light (no
  ghost), mourners dignified (no tears/white-streaks / no gore).
- Distinct faces (no twins / no Jesus-double), child dark-haired, no modern objects, all-realistic
  (no cartoon/mix), no lens-stare.
- Captions bottom-band only: narrator WHITE; s1/s20/s22 SCRIPTURE LIGHT-BLUE (verified all
  three in the rendered mp4); no red, no God-voice. Question card clean, centered, well-margined.

**RESUME (if ever needed):** all art in `assets/`, plates promoted, windows remapped, mp4 built.
Re-assemble = `python3 media-production-v2/v2_assemble.py 171` (must print AUDIO REBUILD PASS).

---

## INDEPENDENT LEGACY-COMPLAINT AUDIT — 2026-08-13, Codex `Dev`

The complaint predates Reviewer hash tracking (`complaintHash: null`), so I did not accept
the earlier “fixed” note without checking the encoded replacement itself.

- Inspected the source b01 and encoded frames at 0.1, 1, 3, 5, and 7 seconds. The first
  picture is Paul speaking to real people in a Corinthian harbour portico. It contains
  **no scroll, scripture writing, curled/rolled edge, border, or picture panel**.
- Inspected a complete rendered-video contact sheet sampled every four seconds plus the
  closing card. The rejected scroll/panel does not recur; captions remain in the bottom
  band and the closing card is clean.
- `v2_prompt.py --check` PASS (15/15); `verify-mp4.sh` PASS; full ffmpeg decode PASS;
  exact content-hash render receipt recorded; `admin/qc_gate.py` with Whisper PASS.
- Final MP4 remains byte-unchanged: 74.466667 s / 19,877,733 B / standard SHA-256
  `6ac92ea26b34a0e8720ca888e1c33d74183a41653b551ddd87a741ba5ab54e15`.

Verdict: the existing realistic V2 cut genuinely fixes Cameron's complaint. No picture,
audio, timing, caption, or finished-video bytes were changed. Reviewer classification may
mark this audited legacy complaint as a replacement while retaining the complaint text.
