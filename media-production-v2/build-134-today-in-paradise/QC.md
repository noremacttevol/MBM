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
