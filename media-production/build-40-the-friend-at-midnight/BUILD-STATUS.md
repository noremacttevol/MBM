# BUILD STATUS — #40 The Friend at Midnight (Luke 11:1-13)

**Delivered:** `luke-11_friend-at-midnight.mp4` — 1080x1920 H.264, 5:56, 20.3 MB, crf 20.
**Built:** 2026-07-13 (Dev). **Status:** waiting on Cameron's yes.
**In the gallery:** https://noremacttevol.github.io/MBM/

Phase-1 STILLS-ONLY (Law E): 16 painted stills, Ken Burns drift, no AI motion clips.
Art: Gemini `gemini-3-pro-image`, 23 images generated (16 keepers + 7 regenerations)
≈ **$3.08**.

---

## The point of this video (the Why-Law)

This parable is misread more than almost any other, and the misreading is cruel:
people hear *"pester God until he caves"* and come away with a God who is reluctant,
irritated and asleep. **Jesus is arguing the exact opposite.** The neighbour is a
CONTRAST, not a portrait — a lesser-to-greater argument. If even a man with every
good reason to say no (barred door, kids asleep in the one bed with him) will finally
get up, **how much more** the Father who was never asleep at all. Beats n14a/n14b say
this out loud. Without them the video would do harm.

Full unit through v13, because the parable is only one part of one answer to one
question ("Lord, teach us to pray"): the prayer that opens on **Father** → the parable
→ ask/seek/knock → the father-and-son argument → and the final gift, which is not
bread but the **Holy Spirit**. God giving himself.

## Two-voice

Jesus (en-US-ChristopherNeural) speaks exact KJV only, six lines: j0 = 11:2 ·
j1 = 11:5b-6 · j2 = 11:7 · **j3 = 11:8 (the verse-card line)** · j4 = 11:9 ·
**j5 = 11:13**. Narrator (en-US-AndrewNeural) is modern throughout and never echoes
a KJV line back. Two sacred silences: the music dies to true silence for **j3** (the
verdict) and **j5** (the payoff).

## Study gems woven in

- People travelled at night (the heat could kill), so a midnight guest is real.
- Hospitality was a **village** duty — the shame of an unfed guest fell on everyone.
- **anaideia** (v8) appears nowhere else in the NT. It does not mean persistence. It
  means **shamelessness**. Placed BEFORE Jesus says it, so the KJV word lands already
  understood and the narrator never has to re-quote him (Translation Law).
- Each pair in vv11-12 is a **lookalike** — a river stone looks like a flat loaf, a
  scorpion curls up pale and round like an egg. A father handing his child a counterfeit.
- The man at the door **never asks for himself**. He begs for bread he will not eat.

---

## QC — Self-Revision loop, final pass clean

| Check | Result |
|---|---|
| Face gate on prompt sheet | **PASS** (exit 0) before any image was generated |
| Jesus's face in finished render | Never visible. He appears in 4 stills (s1, s2, s12, s15), camera behind him every time |
| Phase-1 stills-only | No AI motion clips |
| Ear-check (27 segments) | **All pass**, lowest 0.94 |
| No-dead-air | Worst spoken gap **1.88s** (law: ≤2.5s); build RAISES if exceeded |
| Silence scan on final mix | Only the closing-card tail (4.15s) — checker proven able to fire |
| Loudness | **-14.8 LUFS** (target -15) |
| Format | 1080x1920, H.264, 30fps, 20.3 MB (<25MB) |
| Captions | Verbatim spoken text; KJV in cream italic; box 0.58 legible on night AND golden-morning frames |
| Time of day | Parable (s3-s11, s16) deep midnight; frame (s1,s2,s12-s15) morning |
| Anatomy count | Every still counted; 3 regenerated for defects |

## What the QC loop caught and fixed (7 regenerations)

1. **s1, s12, s15 — a second cream-robed bearded man reading as Jesus.** The model
   dressed a disciple in near-white, centred and gesturing, right beside the real
   (faceless) Jesus. The face gate cannot catch this — every word was legal — but it
   is a face-law failure in spirit. Fix: **only Jesus wears cream**; every other man
   in dun/faded brown/olive. Now a build law and a PRODUCTION-BIBLE entry.
2. **s11, s15 — painted teardrops** on cheeks (banned). The no-tears rule was in the
   sheet's header, but a header never reaches the model — only the shot prose does.
   Fix: the dry-face sentence now lives inside every emotional shot's own prose.
3. **s3 — a third arm** on the householder (lamp hand + gripping hand + a spare
   sleeve hanging between the two men). Fix: assign every hand a job in prose.
4. **s13 — the door read as closed** with light leaking round it, killing the
   "opened before she finished knocking" beat; the reroll then added a **modern round
   doorknob and lock plate** (style block bans modern objects). Both fixed.

## The real blocker, and the bug behind it

The first cut ran **7:05**. At that length the <25MB law forces the video down to
~326 kbps, which would band visibly across the nine night-sky frames — and the
PRODUCTION-BIBLE explicitly forbids starving the bitrate. Two things were wrong:

- **The script was too long.** Trimmed twice (narrator flab only — every beat, all six
  KJV lines, every study gem and verse 13 are intact). 7:05 → 5:56.
- **`build.py`'s bitrate cap was wrong, and had been all along.** The old formula
  (`24.3*8000/total - 130`) never subtracted the actual audio track from the container
  budget, so on any long video it asked for more bits than 25MB allows and the encode
  loop just climbed CRF until something fit — silently degrading quality. It now
  computes the video budget honestly (`24MB - audio - mux`) and **raises** if a script
  is too long to look good, instead of quietly shipping a blocky video. Audio dropped
  to 96k AAC (transparent for dry narration). Result: **423 kbps, crf 20, first pass,
  20.3 MB.**
