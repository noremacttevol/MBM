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
