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
