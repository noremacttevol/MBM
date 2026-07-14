# BUILD STATUS — #43 The Wedding Garment (Matthew 22:1-14)

**Delivered:** `matthew-22_wedding-garment.mp4` — 1080x1920 H.264 30fps, 4:45, 20.1 MB, crf 20.
**Built:** 2026-07-14 (Machine A / Dev). **Status:** waiting on Cameron's yes.

Phase-1 STILLS-ONLY (Law E): 14 painted stills, Ken Burns drift, no AI motion clips.

## Art pipeline note (READ THIS — method deviation, 2026-07-14)

Cameron asked to build this the **old faithful way — Chrome + Google Flow**. I drove
Flow on Browser 1 (his logged-in Google AI Ultra account) and it worked for
GENERATION: Nano Banana 2, 9:16, **0 credits**, and the s1 test image came out
excellent and face-safe. **The blocker was getting Flow's images onto disk in this
unattended environment:**
- Flow's in-app **Download** button produces no file — it opens a native "Save As"
  dialog that browser automation cannot dismiss (nothing landed in ~/Downloads or
  anywhere on the filesystem).
- A localhost receiver (page → 127.0.0.1) is **hard-blocked by Chrome's Local Network
  Access** even with the PNA opt-in header ("Failed to fetch"). curl reaches it; the
  page cannot.
- Returning each image as base64 through the tool works but is context-prohibitive at
  14+ images.

So Flow cannot run **unattended** here without a human clicking a Save-As dialog per
image — which defeats the "all machines, get as many done as possible" goal. To keep
#43 moving I generated the 14 stills with the **proven headless pipeline**
(`gen_stills.py`, `gemini-3-pro-image`, the same painted path #38/#39/#40 used),
which needs no browser, honors the REF character-locks, and delivers hands-off.
**14 images, 0 failed, ~$1.88.** If Cameron specifically wants the Flow art, the
prompt sheet is Flow-ready and I can regenerate there once the download path is
sorted (e.g. set Chrome to a fixed download folder / disable "ask where to save").

## The point of this video (Why-Law, and the J care-law)

Told wrong, this parable rebuilds the cruel-God picture the whole project exists to
correct — "dress right or God tortures you forever." The narration carries the MERCY
that is IN the text, out loud, the whole way:
- The invitation goes to **everyone off the highways**, "both bad and good" (n8, n9).
- **THE GARMENT GEM:** nobody dragged in off the road owned wedding clothes, so the
  clean robe was the **king's to give**, handed to every guest at the door (n10). The
  man was not shut out for being poor — everyone there was poor — but for refusing the
  free gift (n11). Grace is the garment.
- The king calls the excluded man **"Friend"** (jv12, n12) — tenderness even here.
- **Outer darkness is a place the man CHOSE**, out of a light left standing open for
  him (n13) — never a fear threat.
- Closing card is an **invitation**, not a fear-question: "What has he been holding
  out for you to put on, that you keep walking past?"

## Two-voice

Jesus (en-US-ChristopherNeural) speaks exact KJV only, 5 lines. Per the #38/#39/#40
precedent, the KING's lines (quoted inside the parable) are the Jesus voice:
jv4 = 22:4 · **jv8_9 = 22:8-9 (grace pivot, verse-card, sacred silence 1)** ·
**jv12 = 22:12 (the tender pivot, sacred silence 2)** · jv13 = 22:13 (exact
contiguous span, trimmed of "weeping and gnashing" — the J-law keeps the image
restrained) · jv14 = 22:14. Narrator (en-US-AndrewNeural) is modern and never echoes
a KJV line back.

**The two sacred silences land on the two MERCY beats (jv8_9, jv12), never on the
judgment** — jv13 (outer darkness) plays UNDER a soft moving bed on purpose, so the
judgment is passed through rather than enshrined.

## QC — Self-Revision loop, final pass clean

| Check | Result |
|---|---|
| Face gate on prompt sheet | **PASS** (exit 0) before any image was generated |
| Jesus's face in finished render | Never visible. Appears in s1 and s13 only, camera behind him both times |
| Only-Jesus-cream | s1/s13: only the from-behind figure in cream; leaders in indigo/maroon/ochre; the king in royal purple |
| Phase-1 stills-only | No AI motion clips |
| Ear-check (22 segments) | **All pass** (jv12 cleared on the medium.en tie-break) |
| No-dead-air | Worst spoken gap **1.88s** (law ≤2.5s); build RAISES if exceeded |
| Silence scan on final mix | **Checker proven to fire** (loose -30dB reported many); strict -45dB found ONLY the 4.2s closing-card tail — no dead air in the body |
| Loudness | **-14.8 LUFS** (target -15) |
| Format | 1080x1920, H.264, 30fps, 20.1 MB (<25MB), crf 20 first pass, 558 kbps |
| Captions | Verbatim spoken text; KJV cream italic; box 0.58 legible on temple, bright-door, warm-hall AND night frames |
| CONTENT-CARE J | Outer darkness = darkness only (man walks out a lit door, no binding/fire/torment shown); city burned = tiny distant glow, no bodies; mercy spoken throughout; closing card an invitation |
| Anatomy count | Spot-checked s8/s9/s10/s11 (crowds + the king-and-man touch): every hand accounted for, no extra limbs |
| Character consistency | REF locks held the king (s2/s7/s10/s11), servants (s3/s4/s8/s9), the un-robed man (s10/s11/s12), leaders (s1/s13) |

## Shot list (14 stills)

s1 temple (frame, Jesus from behind) · s2 king's feast · s3 the summons (jv4) ·
s4 they would not come · s5 made light of it · s6 the city far off (restrained) ·
s7 go to the highways (jv8_9) · s8 out on the roads · s9 clothed at the door (garment
gem) · s10 the king sees him · s11 Friend (jv12) · s12 outer darkness (jv13,
restrained) · s13 many are called (frame return, jv14) · s14 the door is open
(closing invitation).
