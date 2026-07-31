# Peter Walks on Water — Source Picture QC

| Shot | Result | Primary checks |
|---|---|---|
| 01 | Pass | Locked cast, Jesus in cream, grounded shore, intact boat |
| 02 | Pass | Jesus alone, hands correct, knees grounded |
| 03 | Pass | Deep-water scale, intact hull/rigging, distinct crew |
| 04 | Pass | Distant non-glowing Jesus, intact boat, no intersections |
| 05 | Pass | Locked Jesus, correct hand, no camera gaze or glow |
| 06 | Pass | Locked Peter, two correct hands on gunwale |
| 07 | Pass | Locked Jesus, open hand, no camera gaze |
| 08 | Pass | One leg over solid rail, one inside, no hull intersection |
| 09 | Pass | Active stride, deep sea, planted/lifted feet legible |
| 10 | Pass | Above-water balance, one planted and one lifted foot |
| 11 | Pass | Waist-level sinking, two arms/hands, coherent waterline |
| 12 | Pass | Chest-deep, one complete raised arm/hand, raw expression |
| 13 | Pass | Immediate rescue, coherent grip, real weight |
| 14 | Pass | Locked faces, gentle expression, no false wading view |
| 15 | Pass | Supported return, boat ahead, risky waterline cropped out |
| 16 | Pass | Solid gunwale, body passes over rather than through it |
| 17 | Pass | One boat, one moon, calm reflection, intact rigging |
| 18 | Pass | Jesus grounded on deck, Peter and disciples kneeling |

Hard rejections during this test included the original hull-intersection frame,
a posed first walking attempt, two return shots that read as ankle-deep wading,
and one return shot where Jesus looked toward the camera.

## V5 rendered-video review

All 26 rendered picture slots and the closing card were extracted after the
final crop, Ken Burns motion, and caption burn-in. They passed:

- story/shot correspondence
- Peter and Jesus continuity
- hands, feet, knees, and body/object intersections
- boat hull and gunwale geometry
- deep-water walking versus wading
- caption placement, wrapping, speaker colour, and legibility
- closing-card wrapping and safe margins
- Peter's complete request is present and captioned before Jesus says “Come”

## Technical verification

- Full video/audio decode: passed
- Resolution: 1080×1920
- Frame rate: 30 fps
- Video/audio codecs: H.264/AAC
- Runtime: 225.167 seconds
- File size: 19,092,099 bytes
- Silence longer than 2.5 seconds: none
- V1 audio-stream SHA-256:
  `7602933755c1b8716ca3a2614565674a635c3d3766bacba56021976a6908b2bd`
- V5 audio-stream SHA-256:
  `7602933755c1b8716ca3a2614565674a635c3d3766bacba56021976a6908b2bd`
- V5 file SHA-256:
  `1fdf4caa578ac7df23cf6a225821ee2b8de8560333e1d3572d23ac0774fe2c3e`

The matching audio-stream hashes prove the delivered V5 contains the exact
authoritative final audio packets. No voice, word, pause, gain, or encoding was
changed by the visual rebuild.

## V6 lamp correction and rendered-video review

V6 removes the modern glass/artificial boat lamps from shots 03, 04, 06, 08,
16, 17, and 18. Each edit was compared with its prior source before assembly.
The accepted edits retain the people, faces, limbs, clothing, boat geometry,
weather, and framing while reconstructing only the lamp area. Moonlight is the
only visible light source.

Rendered frames from all seven affected picture slots were extracted after the
final crop, motion, and captions. They contain no glass lamp or artificial
orange lamp glow. Shot 08 still shows Peter's leg passing cleanly over the
gunwale, and shot 16 still shows two complete legs without a hull intersection.

### V6 technical verification

- Full video/audio decode: passed
- Resolution: 1080×1920
- Frame rate: 30 fps
- Video/audio codecs: H.264/AAC
- Runtime: 225.167 seconds
- File size: 19,153,727 bytes
- Black interval longer than 0.5 seconds: none
- Silence longer than 2.5 seconds: none
- V6 audio-stream SHA-256:
  `7602933755c1b8716ca3a2614565674a635c3d3766bacba56021976a6908b2bd`
- V6 file SHA-256:
  `b621f7cb6b2962a5815f714f9c45897055276133b3ddca6063fe5628c3fff15d`

The V1, V5, and V6 audio-stream hashes match exactly. V6 changes pictures only.

## Jesus voice verification

The three current Story 7 Jesus clips (`j1`, `j2`, and `j3`) are the exact files
committed in the 2026-07-24 Story 7 voice render. That render's voice mapping is
Alexander (`UMnEnzK9QLLdRwnUyxMW`), and the ElevenLabs account history records
the same three lines under Alexander immediately before the files were
committed. The repository-wide Jesus voice audit also records all three Story 7
lines as Alexander matches.
