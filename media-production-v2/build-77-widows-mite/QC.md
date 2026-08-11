# QC / RUNNER HANDOFF — build-77-widows-mite (Mark 12:41-44)

Lesson-12 + complaint-corpus pass done 2026-08-05 (Machine A). `--check`
PASSES, zero WARNs. 16 beats, ~92 s.

## Coverage shape

Three true wides with stated geometry: b01 (the watching post — bench
and chest-row in profile), b09 (the unnoticing court — her small
departing back crossing the frame while the rich mid-cast glitter), b12
(the verdict — camera behind the disciples' shoulders following his
pointing line to her distant figure). Five flips — her gift itself (b06)
is TIGHT: the two small coins need closeness.

## THE TWO MITES (count law at its smallest)

- Exactly TWO tiny copper coins — countable in b06 and in any insert;
  worn, thin, near-worthless-looking. Never silver, never a handful.
- The rich men's gifts are HANDFULS of silver arcing loud into the
  trumpet-mouthed chests — the contrast is sound and volume; their
  giving is public-postured, hers is small and quick.
- b16's closing contrast (the chest's silver heap vs her two mites) is
  an object insert — person-free; the arithmetic in one look.

## Other checks

- TREASURY wired (manual --take) to the build-06 temple family — same
  temple as rows 43/63/64/75; the chest-row (trumpet-mouthed bronze
  chests in a row) is per-beat prose on top of the plate.
- The WIDOW: small, charcoal-clad, worn — dignity absolute (44/74/75
  class); her face-board across arrival→gift→departure.
- Direction (row-83): the givers' procession moves ALONG the chest
  row; she departs AWAY small in b09/b12 — the pointing line in b12
  must land on HER figure (Cameron's Peter class: the gesture's
  target in frame).
- PETER/JOHN auto-attach from global sheets — face-board.
- GIVERS varied wealthy (90/107), never cartoon-fat-cats.
- Only Jesus wears cream.

---

## 🅿️ RUNNER PARK — A-auto 2026-08-06 (NEEDS-AUDIO — V1/timeline mismatch, row-69 class)

16 stills GENERATED + QC-PASS (1 reroll: b04 collage → clean single wide), but
`v2_assemble` refuses the AUDIO LOCK: **extracted timeline 98.846s vs V1 final
97.106s** — a 1.74s shortfall, over the assembler's hard `abs(total−locked)>1.0`
tolerance (v2_assemble.py line 531). The V1 mp4 is NOT stale by recency
(newer_mp3s=0), but its duration is 1.74s short of the extract_beats timeline,
so the AAC stream can't be copied aligned.

The runner CANNOT fix this — the fix is `AUDIO_FROM_V1_SEGMENTS = True` in this
row's beats_v2.py (rebuild the track from the V1 mp3s at extract_beats offsets),
which is an author edit outside runner scope (audio-immutability law).

**Stills are valid + reusable — do NOT regenerate.** 16 assets @ 2K, WIDOW
portrait, TREASURY plate (build-06). CARE held: two mites countable (s07 = 2
coins, s16 = 2 coins), widow charcoal-clad dignified, rich give handfuls of
silver, pointing line lands on her (s12), only Jesus in cream.

**RESUME (author/audio session):** add `AUDIO_FROM_V1_SEGMENTS = True` to
beats_v2.py, then `python3 media-production-v2/v2_assemble.py 77` (stills already
present), QC captions, ship. Then flip AUTHOR-BOARD row 77 → BUILT.

---

## ✅ SHIPPED — 2026-08-07 (Machine A `Dev`, Fable-5 author lane), $0, 0 image credits

**STALE-V1 audio-lock CLEARED + realistic-V2 cut assembled and shipped.** Added
`AUDIO_FROM_V1_SEGMENTS = True` to beats_v2.py (the RESUME step above). The track
rebuilt from the 12 V1 segment mp3s at the extract_beats offsets = **98.846 s**, so
the 1.74 s duration drift is gone and the 16 realistic stills sit on the right words.

- `v2_assemble.py 77` → **AUDIO REBUILD PASS SHA256=6b2142d9c5094459**, 98.8 s,
  20.9 MB, mark-12_the-widows-mite.mp4. Decodes with **0 errors**.
- Caption QC (frames @8/40/97 s): captions bottom-band only, scripture light-blue
  / narrator white, question card clean. Realistic-only (Law 14) holds on all 16 —
  every frame photographic, no cartoon/mixed frame.
- **No open Cameron complaint on this row** (`v2_outline.py 77` shows none); this
  was a build-blocking stale-lock, not a complaint fix. Ledger had `versions: []`
  (never published) → this is the row's FIRST publish of a v2 cut.
- 0 pictures touched, 0 rerolls, $0 (no Gemini, no ElevenLabs — edge-tts V1 mp3s
  rebuilt). Stills unchanged from the A-auto 2026-08-06 generation.
- Shipped: mp4 + board + QC committed; review.html v77 repointed to the V2 path
  with data-review-wave="realistic-v2"; firebase deploy + live-verify; publish
  ledger synced. Board row 77 NEEDS-AUDIO→BUILT, Audio CHECK→OK.

---

## ✅ QC-VERIFY — 2026-08-11 (Machine A `Dev`, FULL-CUT GATE 6b, before Cameron's eyes)

Row 77 was BUILT and sitting in Cameron's Unwatched queue. Ran the full-cut gate
(PROMPT-OPUS-RUNNER §6b) BEFORE he watched it. Extracted ONE frame per beat from the
RENDERED mp4 (mid-clip, using the real c000–c015 segment durations, not the raw beat
windows) + the question card, and viewed EVERY one against the defect checklist +
RUNNER-LESSONS + the row's resolved state.

**Result: CLEAN — no defect, no re-cut.**
- Identity/locked face: Jesus consistent across s01/s03/s09/s11/s12/s13 — olive skin,
  dark wavy shoulder-length hair, full dark beard, green/hazel locked-ref eyes (NOT a
  reroll target). Widow face-board consistent across s06/s08/s10.
- Cream-only-Jesus: holds every multi-figure frame. The blue-robed long-haired giver in
  s09 is clearly a wealthy man (gold chain, blue robe), not a cream Jesus-double.
- Count law (two mites): exactly two worn copper coins in s06 (hand at chest), s07 (palm
  insert) and s16 (closing object insert). Rich give handfuls of silver (s02/s04/s05).
- Anatomy/hands: s07 palm (5 digits), s13 jaw-cup (5 digits), s15 empty hand (5 digits)
  all correct. s11 foreground hands darkened only by the caption-band gradient (frame
  edge), not malformed.
- Direction/geometry: givers process ALONG the chest row (s04); widow departs small &
  away (s08/s09); Jesus's pointing line in s12 lands on HER distant figure (QC target law).
- Captions: scripture light-blue (s41/s42), narrator white, Jesus KJV line RED (SPEAKER-LAW
  JESUS_RED — verified in mbm_caption_timing.py, intentional). All bottom-band. Question
  card clean cream serif, no render glitch/squares.
- No modern objects, no lens-stares, no empty-scene-that-should-have-people (s16 is a
  person-free object insert BY DESIGN).
- No open Cameron complaint on this row (build-blocking stale-lock fix), so nothing to
  regress. Served-bytes verified: live card v77 hash 998a0d53 holds blob 23b15544 =
  git hash-object of the shipped mp4; served md5 96d2b18a == local. What Cameron will
  watch is byte-identical to what was QC'd.

Board: QC-VERIFY LIVE → QC-OK. $0 (ffmpeg/ffprobe/curl only), 0 pictures touched.
