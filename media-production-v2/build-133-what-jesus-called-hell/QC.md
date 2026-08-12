# QC / RUNNER HANDOFF — build-133-what-jesus-called-hell (Mark 9:43-48)

AUTHORED FROM SCRATCH, 2026-08-05 (Machine A). `--check` PASSES, zero
WARNs. 22 beats, ~139 s. Cameron asked for this story BY NAME
(2026-07-20 repeat purge): "Judgment is real; the torturer God is
not. CARE: no horror imagery — the real valley, the real words."

## ⚠ ROW-IDENTITY FIX MADE THIS SESSION

The board listed row 133 as build-133-many-mansions — an ARCHIVED
dupe of live row 185. Slug corrected to canonical
what-jesus-called-hell; a stale V2 many-mansions dir (wrong prep)
deleted; v2_scaffold.py fixed to honor CANONICAL_BUILD_SLUGS (it had
written the scaffold into the archived dupe's dir). Row 134's slug
also corrected on the board (other-sheep → today-in-paradise).

## THE STRICTEST CONTENT-CARE ROW IN THE LIBRARY

- NO horror imagery, ever: no torture, demons, pitchforks, suffering
  figures in fire, maiming. Automatic reject, no reroll.
- Hand/eye verses (b10/b12) NEVER literal: Jesus's own WHOLE raised
  hand and his own clear steady eyes carry the severity. b15's
  craftsman hand is whole and working.
- Topheth (b05/b06): NO children, NO fire, NOTHING enacted — ruined
  shrine stones + the prophet's grief/denunciation only. Absolute.
- b13 (worm/fire): empty ground, low banked embers, thin smoke — no
  figures, no leaping flame.
- Later-tradition art (b01/b17): muddy indistinct canvases only —
  nothing lurid resolves; b17's easel+pigments make the argument.
- b20: the child is SAFE, caught well back from the well's edge.

## The row's argument in frames (check as a set)

Real geography (b02/b03) → real history by ruins+prophet (b04-b07)
→ Jesus owns the severity (b08-b14) → what the images price
(b15) → love's registers (b16/b20) → what tradition added (b17)
vs scripture's own objects (b18) → the purpose: the turn (b19,
rhymes with 117's reversal) → the speaker's character (b21 lamb
carry) → the closing map (b22: Jesus BETWEEN valley and city
lights, hand pointing HOME).

## Coverage shape

One true wide with stated geometry: b22 (camera behind the
listeners' backs at the ledge; two-zone composition — ruin below
one way, warm home-light the other). Seven Jesus beats (b08, b09,
b10, b12, b16, b21, b22). Dim/grey/dusk frames all BY DESIGN (see
header arc). File order ≠ story order (b08 at 4.66s, b11 at 40.98s
before b09's 47s) — build by WINDOW.

- Plates: none auto-matched. VALLEY promote-first from b02, OVERLOOK
  from b09. PROPHET face-board b05/b06.
- Two drift-word FAILs caught and fixed pre-ship ('glowless',
  'glowing' → 'banked', 'warm-lit').

## 🅿️ RUNNER PARK — NOT AUDIO-READY (2026-08-11, Machine A `Dev`, $0)

**Blocked before ANY credit — no stills generated, meter untouched.** The
board said "Audio OK / Ready ✅", but this row cannot be assembled: its audio
is NOT wired for `v2_assemble`. Three independent facts, all measured this
session, prove it (every buildable sibling — rows 100/105/108 — has all three;
this row has none):

1. **No V1 final mp4.** `media-production/build-133-what-jesus-called-hell/`
   has NO `*.mp4`. The locked-mp4 audio path in `v2_assemble.main()` (line ~533,
   `locked_final = <v1dir>/<name>.mp4` → `audio_stream_hash`) has nothing to
   hash → the assemble AUDIO LOCK cannot run.
2. **No V1 segment mp3s.** `media-production/build-133-what-jesus-called-hell/audio/`
   holds only the `.timing.json` files — **zero `.mp3`**. So even the
   `AUDIO_FROM_V1_SEGMENTS` path (`rebuild_audio_from_segments(v1dir,…)`,
   line ~174) would `SystemExit("AUDIO REBUILD: missing V1 segment audio …")`.
   This also makes `extract_beats.extract(133)` itself crash
   (`dur_of('')` ValueError) because the beats carry SEGMENTS text so it does
   not skip them — it probes the missing mp3.
3. **`AUDIO_FROM_V1_SEGMENTS` is not set** in `beats_v2.py` (grep count 0).

The narration DOES exist, just not where assembly reads it: the V1 `segs/`
dir has `audio_mix.m4a` + per-segment `.mp4`s (n0–n6, j1–j3, Jul 28), and the
**V2 dir `media-production-v2/build-133-what-jesus-called-hell/audio/` has all
11 fresh mp3s (n0–n6, j1–j3, card, Aug 5)**. The V1 build got to `segs/` but
its final mux + `audio/*.mp3` were never landed/committed in the V1 dir.

**Why the runner will not fix this:** restoring mp3s into the read-only V1 dir
violates hard-protection #1; setting `AUDIO_FROM_V1_SEGMENTS` edits `beats_v2.py`,
which is an AUTHOR/audio-lane decision outside runner writes (row-69 lesson).
Improvising audio setup is explicitly banned by PROMPT-OPUS-RUNNER.

**RESUME (author / audio lane):** copy the 11 V2-dir mp3s
(`media-production-v2/build-133-what-jesus-called-hell/audio/{n0..n6,j1..j3,card}.mp3`)
into `media-production/build-133-what-jesus-called-hell/audio/`, set
`AUDIO_FROM_V1_SEGMENTS = True` in this build's `beats_v2.py`, then re-run the
$0 pre-flight: `python3 -c "import extract_beats as E; print(E.extract(133)['total'])"`
must succeed, and `rebuild_audio_from_segments` must find all 11. THEN the
picture runner builds the 22 beats on that audio (VALLEY promote-first from b02,
OVERLOOK from b09, PROPHET portrait already made). Until then this row stays
**NOT-READY** — Ready ✅ cleared on AUTHOR-BOARD so no runner burns $6 of stills
that cannot assemble.

## ✅ AUDIO-WIRED → BUILDABLE (author/audio lane, Machine A `Dev`, 2026-08-11, $0)
Executed the RESUME above. Copied all 11 V2-dir mp3s
(`media-production-v2/build-133-what-jesus-called-hell/audio/{n0..n6,j1..j3,card}.mp3`,
all 44100 Hz / 128 kbps mono = the new-voice ElevenLabs spec) into
`media-production/build-133-what-jesus-called-hell/audio/`, and set
`AUDIO_FROM_V1_SEGMENTS = True` in beats_v2.py. Pre-flight now PASSES:
`extract_beats.extract(133)['total'] = 149.897`, `v2_prompt --check` PASS (22 beats,
zero WARNs), `audio_audit` flags 0 old-voice segments. Board → Audio OK, Ready ✅.
Row is now a normal picture build for the Opus runner (VALLEY promote-first b02,
OVERLOOK b09, PROPHET portrait already made). Content-care laws above still bind.
