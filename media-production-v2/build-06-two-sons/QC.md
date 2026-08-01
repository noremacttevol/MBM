# Story 06 — The Two Sons — realistic V2 QC record (2026-08-01)

## The complaint this cut fixes (OPEN, reported 2026-07-28 against 3114a34d)

> "Your shortening of the videos has gotten out of hand. In this one the father
> didnt really ask either son anything and thats not how Jesus tsught it. It can
> be shorter than the original but it has to hit all of the points well. And
> here you cut out the original thing the father asked the sons"

**Root cause found:** the 2026-07-24 REDO voiced the COMPLETE script — j28 (the
father's KJV ask, Matt 21:28), j29/j30 (both sons' KJV answers), n1b, n2b, j29b
("but afterward he repented, and went"), s31 (the crowd's KJV answer) and n5b
(the modern-terms publican/harlot explanation from Cameron's QUEUE note) — but
`media-production/build-06-two-sons/build.py` BEATS was never updated, so the
assembled 82.7 s cut silently dropped every one of those segments.

**Fix (assembly-only, zero re-voicing):** BEATS now carries all 18 voiced
segments in make_narration.SEGMENTS order with speaker-aware KJV gaps that
match extract_beats exactly. V1 final rebuilt at 125.8 s.

## Audio verification

- faster-whisper (base.en) transcription of the rebuilt V1 final: all 19 lines
  present in order, including "Son, go work today in my vineyard", "I will
  not", "I go, sir, and went not", "They say unto him, The first", and the
  tax-collector explanation. No dropped or slurred words.
- `v2_assemble.py 6` AUDIO LOCK PASS — the realistic cut's encoded audio is
  packet-for-packet identical to the rebuilt V1 final
  (SHA256=4ef87e9cc25b704b876425edb33c07989061bc921185da741494aef4cc1c60e2).
- No music bed (bed amplitudes remain zeroed; narration + intentional silence).

## Pictures — 23 realistic beats at native 2K (gemini-3-pro-image)

- Beat map: `beats_v2.py` (windows from the fixed extract_beats against the
  rebuilt 125.786 s timeline; card at 112.99 s). v4 checklist PASS.
- Identity anchors generated and attached to every beat naming the lock:
  `CAST-REF-V2/father-ref.jpeg`, `first-son-ref.jpeg`, `second-son-ref.jpeg`,
  `priests-ref.jpeg`; Jesus locked by JESUS-V2-REF + LOCK v5 in all 7 shots.
- Every one of the 23 finals was eyeballed at full size. 18 passed first take.
- Rerolls (5): b01 (only three priests visible — lock says four), b10 (partial
  second figure at the frame edge + stray animal forms), b14 (Jesus's gaze
  grazed the camera — Session 6 defect), b16 (HARD FAIL: model returned a
  three-panel triptych with a dissolving figure), b22 (distant pale-robed
  teaching figure read as an unlocked stray Jesus).
- Rough-draft lesson (prodigal b20 pattern) confirmed twice: b10's rough (old
  s05) itself contains the edge figure and background workers, and b16's rough
  (old s11) is ITSELF a triptych — both roughs dropped, both rerolls clean.
- Face-board pass: father, first son, second son, Jesus and the four priests
  read as the same actors across all their appearances; the two sons are
  clearly different men (stocky/curly/rust-brown vs taller/tidy/dusty-indigo).
- Action-logic: the ask (b03) reads as a real ask with no refusal yet; the
  refusal (b05) is a turned back + flat palm, readable with no words; the
  courteous yes (b08) is a bow + hand on heart with no slyness; bailing-style
  count checks (arms/hands/heads) applied to every frame.
- Content-care at b21/b22: the women are covered, ordinary and dignified;
  nothing suggests the trade; nobody shames them.

## Rendered-product checks (on the delivered MP4, not the inputs)

- `admin/verify-mp4.sh` OK — video 125.83 s, audio 125.81 s, 19.9 MB.
- Frame pulls at 3/14/25/40/57/74/84/100/111/120 s: captions live only in the
  bottom band, split in sync; narrator white, Jesus RED (j28 ask at 14 s,
  j29b repentance at 57 s), scripture LIGHT BLUE (s31 at 84 s); pictures match
  their narration windows; closing question card clean with proper margins.

## Spend

- 4 identity anchors + 23 beats + 5 rerolls = 32 API images ≈ $4.29 at $0.134,
  logged to `api-spend.jsonl`, every run under a hard `--ceiling`.
