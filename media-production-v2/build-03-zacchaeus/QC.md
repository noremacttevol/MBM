# Story 3 Realistic V3 QC — Zacchaeus

Final candidate: `luke-19_zacchaeus-realistic-v3.mp4`

## Delivery proof

- 26 realistic 9:16 source pictures in `assets-realistic-v3/`, all
  1536×2752.
- 24 pictures received identity and/or action repairs; `s15` and `s19` remain
  byte-for-byte identical to the existing realistic draft.
- Final: 1080×1920 H.264, 30 fps, AAC mono 44.1 kHz,
  222.099002 seconds, 20,482,187 bytes.
- Final Git blob SHA-1: `39c19f7e284afab4d757a304167e676799a99e0b`.
- Final SHA-256:
  `21c9bdcdf461742b5dc5b3a05614acc85e097a3ed0a9f5c61654c5bade194540`.
- Encoded-audio packet SHA-256:
  `aba5bf8c20a0ff86501a13d8078bd287bcd6b8aa87dcb549851b4b2472db957e`.
- `v2_prompt.py --check`: PASS for all 26 beats under the V4 checklist.
- `v2_identity_board.py --check`: PASS for Jesus and Zacchaeus across all 32
  configured clear face appearances.
- `admin/verify-mp4.sh`: PASS; video and audio are both 222.099002 seconds and
  the moov atom is readable.
- One decoded frame from every beat plus the closing card was inspected in
  `DECODED-QC-V3.jpg`. The longest detected silence is 1.886080 seconds.

## Audio and script fidelity

- The authoritative V1 final is the sole audio source. Its AAC stream was
  copied packet-for-packet into V3; the source and final packet hashes are
  exactly equal.
- No TTS was requested. No word, sentence, pause, music cue, sound composition,
  ordering, duration, or timing was rewritten, removed, shortened, or
  regenerated.
- `media-production/JESUS-VOICE.json` records Story 3 as passing because all
  four Jesus lines match Alexander in the ElevenLabs history. The locked MBM
  Alexander voice ID is `UMnEnzK9QLLdRwnUyxMW`.
- The full invitation remains present before the response: Jesus calls
  Zacchaeus by name, tells him to make haste and come down, and says that he
  must abide at his house. The later vow and restitution therefore remain in
  their intended script order.

## Visual continuity and action

- Jesus is checked against one approved global portrait across 12 clear
  appearances. Zacchaeus is checked against one neutral portrait across 20
  clear appearances; distant backs of heads were excluded rather than treated
  as identity evidence.
- Zacchaeus remains a short, slight adult with normal proportions, the same
  receding hairline, gray-at-chin beard, burgundy robe, and gold woven borders.
- The tax office, Roman collection, public rejection, crowd obstruction, run,
  climb, tree discovery, invitation, joyful welcome, murmuring, meal, vow,
  restitution, salvation declaration, and closing departure all remain in
  script order.
- The run shows both feet airborne and both hands gathering separate garment
  folds. The climb uses separate handholds and a broad load-bearing limb; no
  body part passes through the tree.
- The vow shows no money. The later restitution shows coins leaving the open
  strongbox with exactly three people in frame. The closing room scenes use
  natural witness placement, not a staged worship circle.
- The decoded sheet confirms all speaker-color captions are readable within the
  safe bottom band, and the complete closing invitation card is present.

The new hash is live at `https://milk-b4-meat.web.app/review.html` under
**Unwatched**. A live raw download matches the tested SHA-256 exactly. The
Firestore record still retains Cameron's earlier 1:48 complaint and approved
old-cut hash, while the Reviewer UI keeps this replacement out of Complained
About. The mobile app and app-feed video remain unchanged.
