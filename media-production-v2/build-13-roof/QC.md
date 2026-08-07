# Story 13 Realistic V3 QC — The Man Through the Roof

Final candidate: `mark-2_man-through-the-roof-realistic-v3.mp4`

## Delivery proof

- 45 realistic 9:16 source pictures, normalized to 1882×3344 JPEG.
- Final: 1080×1920 H.264, 30 fps, 298.817007 seconds, 21,581,743 bytes.
- Final Git blob SHA-1: `069c50869a43e29d7eba902445adf0ccd028aa84`.
- Final SHA-256: `432a11dfffe90367f155c8f4944a3df2897f9ab6b468c039be22445d6fdbb49f`.
- Encoded-audio packet SHA-256: `1f7b80dfc50649b95e935efe939161f3b3f4b56965e6c219da84b8a4fb8b46a8`.
- `admin/verify-mp4.sh`: PASS; video and audio both reach 298.817007 seconds.
- Six recurring identities pass the hash-backed face-board gate: the paralysed
  man, all four distinct friends, and Jesus.

## Audio and script fidelity

- No narration was generated, shortened, substituted, or rewritten for this
  rebuild. The complete timeline contains all 23 existing tracked source clips,
  including all three Jesus sayings, both Scripture clips, and the full closing
  question. `AUDIO-SOURCE-MANIFEST.json` records each source hash and position.
- The checked-in V1 MP4 is a stale 258.967-second render, so it cannot be the
  complete audio authority. The existing source clips form the complete
  298.817-second timeline; the final copies that locked AAC master unchanged.
- Jesus is **Alexander**, not Chris. At commit `e0542b134` the shared engine maps
  Jesus to Alexander (`UMnEnzK9QLLdRwnUyxMW`), and that commit's `j1`, `j2`, and
  `j3` files have exactly the same SHA-256 hashes as the current source clips.
  A later non-ancestral branch did generate Chris, but those blobs are not in
  the current source set and are not in this cut.
- Punctuation is present in the Alexander take. Signal measurement finds 0.567s,
  0.878s, and 0.416s internal pauses in `j2`, plus a 0.625s pause in `j3`.

## Story and continuity proof

- The four friends are the same four distinguishable men throughout. Exactly
  four carry the mat, one per corner; all four work on and remain on the roof.
- The paralysed man keeps the same face, dark grey-brown clothing, and reed mat.
  The mat is carried level, lowered on four functional ropes, remains under him,
  is rolled only after Jesus' command, and is carried out by the healed man.
- The house remains a small dark-basalt Galilean house with a plausible flat
  packed-clay, reed, and beam roof. The hole admits daylight, dust, and straw.
- The scribes reason silently with closed mouths. Forgiveness occurs before
  physical healing; Jesus answers the unspoken reasoning; motion progresses
  from first effort to trembling stand, mat roll, and walking out.
- Jesus is not surrounded by an artificial worship circle. The crowded room has
  natural sightlines and actions, with the four friends separated above.
- Full-resolution checks rejected and replaced wrong headcounts, changing faces,
  missing roof friends, an airborne mat, misplaced indoor friends, premature mat
  movement, a duplicate paralytic, and a wrong standing identity.
- Late identity repairs corrected all four bearers in `s10`, all four roof faces
  and Jesus in `s17`, Jesus beneath the four-rope mat in `s15`, and the same four
  friends celebrating in `s44`.
- One decoded frame from each of all 45 final beat windows was inspected after
  crop, captions, and encoding. The command, first standing, mat roll, exit,
  Scripture close, and closing card occur in the right order and timing.

The reviewer replacement hash returns Story 13 to **Unwatched** while retaining
the prior picture complaint for comparison. The mobile app and app-feed video
remain unchanged.

## OPEN CAMERON COMPLAINT — gate before rebuild

"1:37 picture is missing the man on the mat" → beat v2-r013-b18
rewritten: shot from low inside the room so the man on his mat lies
soft in the near foreground UNDER the hole while the four faces ring
it above. The mat man must be PRESENT in the frame — his absence is
an automatic reject.

## COMPLAINT LEDGER (C-FIX 2026-08-07, Machine A Dev) — CLOSED

- OPEN complaint (only one on this row): **"1:37 picture is missing the
  man on the mat."** FIX: beat **v2-r013-b18** (`s18-the-four-sweat-streaked-faces.jpeg`,
  displays 103.4–108.5s) was rerolled ONCE against the author's rewritten
  scene. The new frame is shot from low inside the room: **the paralysed man
  lies on his reed mat across the near foreground**, ropes trailing from the
  mat corners, and all four dust-caked friends ring him from above under the
  broken roof hole. Verified in the RENDERED mp4 at 105.5s — the mat man is
  now the foreground subject; his absence (the exact defect Cameron named) is
  gone. Realistic, four friends (correct count), no Jesus in frame, no modern
  objects, caption in the bottom band.
- Rerolls this row: **1 / 45 beats = 2.2%** (well under the 15% COST-LAW budget).
- Touch-once: this was the only open complaint on the row; nothing else was
  changed. Every other still is byte-identical.

## AUDIO — unchanged, rebuilt from the identical V1 source clips

The checked-in V1 mp4 (`media-production/build-13-roof/mark-2_man-through-the-roof.mp4`)
is a **stale 258.967s** render, so the AUDIO LOCK's default copy-from-V1-mp4 path
refuses (STALE-V1-FINAL guard). Set `AUDIO_FROM_V1_SEGMENTS = True`: the
narration is rebuilt from the V1 build's OWN 23 mp3 segments at the extract_beats
offsets (same mechanism shipped on rows 61 and 69). `v2_assemble.py 13` prints
**AUDIO REBUILD PASS**. Nothing was re-voiced, re-timed, or resynthesised — same
words, same voices, same offsets. Both the old shipped v3 and this new cut measure
**-15.1 LUFS** integrated loudness; the only difference is 0.5s of trailing card
tail (298.3s vs the old 298.8s). The audio Cameron already heard is unchanged.
