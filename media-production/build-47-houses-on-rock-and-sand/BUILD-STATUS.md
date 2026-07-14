# BUILD STATUS — #47 Houses on Rock and Sand (Matthew 7:24-27)

**Delivered:** `matthew-7_houses-on-rock-and-sand.mp4` — 1080x1920 H.264 30fps, 3:56, 18.9 MB, crf 20.
**Built:** 2026-07-14 (Machine A). **Status:** waiting on Cameron's yes.

Phase-1 STILLS-ONLY (Law E): 12 painted stills, Ken Burns drift, no AI motion clips.
GREEN / plain-milk story (no CONTENT-CARE flags).

## Art pipeline — FLOW, 0 API cost (the "old faithful" way, now working)

Cameron: use my Flow credits, not the paid API. Done. All 12 stills generated in
**Google Flow (Nano Banana 2, 9:16, 0 credits)** on Browser 1's logged-in Ultra
account. The download blocker from #43 is fixed: with Chrome's "ask where to save"
turned off, downloads land on disk. Pulled all 12 via an in-page fetch + named
download (keeps the image data off the model's context), mapped by content, placed in
assets/. **Cost: $0.** Note: Flow's downloadable image is 768x1376 (its "1K original");
the build supersamples to 2160 then lanczos-downscales to 1080, so on a phone the
softness vs #43's 1536 sources is negligible — but if a crisper master is ever wanted,
the detail-view 2K download is the lever.

## The point (Why-Law)

The misread is "be good or God wrecks you." The point is the opposite and smaller:
**both men heard the same words** (n2, n11) — the only difference was that one went home
and DID them. Study gems: you build in the dry season, and the easy ground is the smooth
sand of a dry riverbed / wadi (n3); the wise man does the slow, unseen work of digging to
bedrock (n4); the winter rains turn those beds into flash floods that hit BOTH houses the
same (n6-n9). The difference was underneath, unseen, until the water came up (n10). Milk
framing: the foolish man is safe on the bank — his life's WORK falls, not him — and it ends
on an open door and an actionable invitation (n12, card).

## Two-voice

Jesus (en-US-ChristopherNeural) speaks exact KJV — the whole parable is his direct speech,
4 lines: **jv24 (7:24, wise/rock — verse card, sacred silence 1)**, **jv25 (7:25, "it fell
not" — sacred silence 2)**, jv26 (7:26, foolish/sand), jv27 (7:27, "great was the fall").
Narrator (en-US-AndrewNeural) modern, never echoes a KJV line. The two sacred silences land
on the two ROCK beats (jv24, jv25); jv26/jv27 (the foolish man and the fall) play UNDER a
soft bed, so the weight stays on the rock, not the fall.

## QC — Self-Revision loop, final pass clean

| Check | Result |
|---|---|
| Face gate on prompt sheet | **PASS** (exit 0) before any image was generated |
| Jesus's face in finished render | Never visible — s1 and s11 only, camera behind him both times |
| Only-Jesus-cream | s1/s11: only the from-behind figure in cream; the whole crowd in dun/brown/olive/blue |
| Phase-1 stills-only | No AI motion clips |
| Ear-check (17 segments) | **All pass** |
| No-dead-air | Worst spoken gap **1.88s** (law ≤2.5s); build RAISES if exceeded |
| Silence scan on final mix | Checker proven to fire; strict -45dB found ONLY the 4.2s closing-card tail |
| Loudness | **-14.8 LUFS** (target -15) |
| Format | 1080x1920, H.264, 30fps, 18.9 MB (<25MB), crf 20 first pass, 697 kbps |
| Captions | Verbatim spoken text; KJV cream italic; box legible on hillside, bright-sand, night-storm and card frames |
| Milk framing | Fall is restrained (man safe on the bank, only the house falls); closing card an actionable invitation, never a fear-question |
| Character consistency | Wise builder (russet + grey-streaked beard) held across s3/s4/s5; foolish builder (sandy-tan) across s7/s8/s9; both houses consistent |

## Shot list (12 stills)

s1 hillside (frame, Jesus from behind) · s2 both men heard · s3 digging to the rock ·
s4 founded on the rock (jv24) · s5 the finished rock house · s6 it fell not — storm (jv25) ·
s7 building on the sand (jv26) · s8 the finished sand house, clouds gathering ·
s9 great was the fall — restrained (jv27) · s10 the morning after, two foundations ·
s11 astonished (frame return, Jesus from behind) · s12 build here — the open door.
