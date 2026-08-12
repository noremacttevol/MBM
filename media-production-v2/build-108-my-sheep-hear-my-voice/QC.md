# QC / RUNNER HANDOFF — build-108-my-sheep-hear-my-voice (John 10)

Lesson-12 + complaint-corpus pass done 2026-08-05 (Machine A). `--check`
PASSES, zero WARNs. 23 beats, ~133 s.

## Two shepherds (identity law)

The custom beats (b01-b03, b17) use the GENERIC olive-mantled shepherd
(SHEP lock); from the I-AM beats the shepherd IS Jesus (cream, ref).
The handover must be clean: never the generic man in cream, never
Jesus in the custom beats. Face-board both.

## Lead-from-the-front (the row's direction doctrine — row-83 class)

Every following frame has the shepherd AHEAD, back to the flock, the
sheep strung AFTER the voice — no one behind the flock, no raised
stick, ever. If a render shows driving-from-behind, the doctrine
inverts; reject.

## The sheep (the row-11 animal class)

A modest MIXED flock — grey-white and brown-black, several lambs,
individually varied so single sheep are recognizable (the by-name
calling depends on it: b06's called individuals must be distinct
animals). Same flock across frames; no sudden herd-size changes.

## Coverage shape

Four true wides with stated geometry: b02 (the invisible leash in one
profile), b03 (the shared fold behind the woolly backs), b06 (the
by-name calling in profile), b15 (the human flock behind the
gathered shoulders). Nine flips including b19's LONE carry through
rough weather (single + lamb — phantom trap) and b09's sheep-only
pool (no people at all).

- The pluck-them-from-my-hand beat rides on the carrying grip —
  contact believable (anatomy law), weather real, no drama beyond
  the wind.
- Dawn → green day → golden evening → night at the gate: one
  direction.
- HILLS promote-first from b09's pool hollow; FOLD from b03.
- Only Jesus wears cream (his beats only).

---

## RUNNER PARK (A-auto Machine A, 2026-08-06) — NEEDS-AUDIO, $0 spent

Pre-flighted the AUDIO LOCK at step 2 (both gates) BEFORE any generation.
**STALE-V1-FINAL — both tripwires fail:**
- RECENCY: V1 mp4 `john-10_my-sheep-hear-my-voice.mp4` rendered 2026-07-24
  10:15:29; all 14/14 narration mp3s are NEWER (2026-07-29 09:44:22). Copying
  the V1 audio stream would ship stale voices/deleted segments.
- DURATION: timeline total 148.623s vs V1 mp4 146.494s, |Δ|=2.129s > 1.0
  (v2_assemble line 531).

The board Audio column read "OK" but the authoritative pre-flight fails — trust
the pre-flight (RUNNER-LESSONS FLEET rule). Runner cannot re-voice/edit beats
under audio-immutability.

**Author fix:** set `AUDIO_FROM_V1_SEGMENTS = True` in beats_v2.py (narration
then renders from the V1 build's own mp3s at extract_beats offsets — nothing
re-voiced, V1 stays read-only), then this row is BUILDABLE.

**Resume command (runner, after author fix):**
`python3 media-production-v2/v2_story_cast.py build-108-my-sheep-hear-my-voice`
then generate. No stills were generated; nothing to reuse yet.

---

## RUNNER BUILD + FULL-CUT GATE + SHIP (Opus runner, Machine A `Dev`, 2026-08-12, unattended/headless)

**COMPLAINT LEDGER** (`v2_outline.py 108` / COMPLAINTS.md row 108):
- OPEN: *"Calleth still wrong again. Same problem"* (status "newer cut shipped — VERIFY fixed").
  **How this cut fixes it:** the jv3 audio was ALREADY re-voiced with the spoken respelling
  "kawleth" (FIXNOTES.json #1475, "narration re-recorded"). This cut ships that fixed audio
  BYTE-IDENTICAL via `AUDIO_FROM_V1_SEGMENTS=True` — the shipping V1-dir `audio/jv3.mp3`
  md5 `76019f98…` == the V2-dir copy, so no orphan (row-50 trap cleared). VERIFIED in the
  delivered mp4: faster-whisper reads "calleth" cleanly at 36.3s, and the "call" vowel LPC
  formant is **F1=744 / F2=1272 = a back /ɔ~ɑ/ ("KAWL-eth")**, NOT the old rejected /æ/
  "Kalloth" (which would read F2>1600). Whisper is deaf to this vowel (memory:
  homograph-vowel-validate-by-formant) — the formant is the proof. Complaint's fix is in.

**AUDIO integrity (STALE-V1 batch checks, row 108 is named in RUNNER-LESSONS §ASSEMBLY):**
- AUDIO REBUILD PASS SHA256 `083e2e62…`, 148.6s; rebuilt from the 14 V1-dir mp3s.
- Window drift: max beats_v2 window end 132.54 ≈ extract_beats card_start 132.817 (Δ0.28s) —
  no stale-window overrun; all 23 stills placed, video 148.67s ≈ audio 148.62s.
- Structural desync (row-95): all four Jesus red-letter lines land inside their Jesus-frame
  windows — jv3 "calleth" @36.3 (s07), jv27 "My sheep hear my voice" @43.5 (s08), jv11
  "I am the good shepherd" @61.7 (s12), jv28 "…pluck them out of my hand" @88.1 (s16).

**CAPTION↔AUDIO FIX caught by the full-cut gate (row-84/131 class, n4b):**
- The V1-dir `make_narration.py` SEGMENTS n4b carries THREE sentences (opening
  "Not a hired man who runs off when it turns dangerous — a shepherd who lays his own life
  down for the sheep."), but the re-voiced audio (`audio/n4b.timing.json`, V1==V2) speaks
  only the LAST TWO ("That is what he was willing to spend to keep them / to keep you").
  extract_beats fed the stale 3-sentence text to the caption, so the burned caption printed
  "Not a hired man…" while the voice said "That is what he was willing to spend…"
  (confirmed by extracting the 69s frame from the rendered mp4).
- Deleting the `segs/*_N.txt` caption cache does NOT fix it (it regenerates the same stale
  text from the V1 SEGMENTS). FIX = `TEXT_OVERRIDES={"n4b": "<timing.json spoken text>"}` in
  beats_v2.py (the blessed `v2_assemble._text_overrides` path). Re-assembled → caption now
  reads "That is what he was willing to spend to keep them" (verified @69s). V1 make_narration
  NEVER edited (hard rail); audio SHA unchanged `083e2e62…` (byte-identical, $0).

**FULL-CUT GATE §6b — 23/23 rendered frames + question card reviewed, ALL PASS, 0 rerolls:**
- Realistic-only (no cartoon/mix). Jesus cream-only in every Jesus frame; the generic SHEP
  (image-locked to CAST-REF-V2/shep.jpeg) is olive-mantle/charcoal-cloth, NEVER cream — clean
  two-shepherd handover (custom beats b01-04/b17 = SHEP; I-AM beats = Jesus). No second-cream
  / Jesus-double (swept the s14 crowd + s15).
- Scale gate: Jesus ordinary-sized in every multi-figure frame (s05/s06/s14/s15). Beard board:
  Jesus full dark beard consistent; SHEP short dark beard consistent. Jesus green/hazel eyes
  are REF-TRUE (JESUS-V2-REF) — left as-is per rubric lesson 20 (NEVER reroll/brown-edit).
- Anatomy: sheep-carry contact (s10/s18/s19/s22) natural; the "my hand" insert (s16) is one
  natural hand. Lead-from-front direction correct (s01/s02/s11/s17 shepherd ahead of flock, no
  driving). Time-of-day arc correct (dawn fold → green day → golden evening → blue-hour close).
- No modern objects, no sky wires, no rotation, no collage, no white tears/blood, no lens-stare.
  Captions bottom-band only; red = Jesus voice, white = narrator. Question card clean.

**PLACES:** FOLD image-locked (PLACE-REF/fold.jpeg, from build-21) — consistent across
b03/b04/b07/b17/b20/b21/b23. **HILLS = FORCED NO-PROMOTE** (like row-51 BOATS): the QC note
said "promote HILLS from b09," but b09 is `jesus:True` (Jesus in cream on a stone) and every
other HILLS candidate is either Jesus-bearing or SHEP-peopled — promoting any would stamp a
second-cream figure or a fixed composition across all 10 HILLS beats (lessons 1016/1199). Left
HILLS on its text lock; QC confirmed the green hills + still pool read consistently across
s01/s06/s09/s11/s14 (natural landscape variation only, no drift complaint risk).

**COST:** SHEP portrait $0.13 + 23 stills $3.08 = **~$3.21 / 0 rerolls (0%)** — well under the
$6.10/row baseline and the 15% reroll budget; COST-LAW trend DOWN. Audio $0 (byte-identical).
