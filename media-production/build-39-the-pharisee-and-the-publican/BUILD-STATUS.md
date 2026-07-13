# Build #39 — The Pharisee and the Publican — BUILT ✅

**Date:** 2026-07-13 · **Machine:** Dev · **Scripture:** Luke 18:9–14
**Delivery:** `luke-18_pharisee-and-publican.mp4` — 4:33, 20.8 MB, 1080×1920 H.264 30fps
**Cost:** 17 images × $0.134 (gemini-3-pro-image, 2K) = **$2.28** (14 kept + 3 regenerated)
**State:** finished, QC-clean, **waiting on Cameron's yes.**

---

## What it is

14 painted stills with slow Ken Burns drift, two-voice narration, verbatim serif captions,
KJV lines in cream italic, and the closing question card. **Zero AI motion clips** (Law E).

The whole story, v9 through v14: who Jesus told it to and why (v9 — the men who trusted in
themselves), both men going *up* to the temple, **why the Pharisee was genuinely admired**
(one fast a year was commanded; he fasted twice a week), **why the publican was genuinely
hated** (a traitor with a money box), both prayers, the verdict, and the invitation — Jesus
told this to the good men not to shame them but to let them in too.

**The point, in one sentence:** the man who had everything right went home wrong, and the
man who had everything wrong went home right — because one came to God with a résumé and
the other came with the truth.

**Two sacred silences:** the music dies to true silence for *"God be merciful to me a
sinner"* and again for the verdict. The narrator never stops; only the music does.

---

## QC — every check, and what it caught

| Check | Result |
|---|---|
| 🛑 **FACE GATE** (`jesus_face_gate.py`) | **PASS, exit 0** — passed on the first run |
| 🛑 **Face audit of the finished render** | Jesus is in only s1 and s9, both from directly behind. His face does not appear in any frame at any zoom. |
| 🛑 **EAR-CHECK** (every mp3 vs script) | **18/18 pass** (3 needed the medium.en tie-break, all clean) |
| **No-Dead-Air** | worst spoken gap **2.03s** (law: ≤2.5s). The build now *hard-fails* above 2.5s. |
| Loudness | **−14.8 LUFS** (target ≈ −15) |
| Size / format | **20.8 MB** (<25), 1080×1920, H.264, plays clean |
| Stills-only | 14 images, no Veo/Flow clips |
| Anatomy count, every still | pass (one regenerate — see below) |
| Captions on the right scene | verified on a 15-frame strip across the whole runtime |
| Baked-in text/gibberish | none |
| Time of day | bright morning in every still — the hour of prayer and sacrifice |

### Five real defects the self-revision loop caught and fixed — Cameron saw none of them

1. **Dead air after both KJV lines** (2.76s and 2.73s, over the 2.5s law). The TTS files
   carry a silent tail — ~1.3s on the Jesus voice — and timing off the *file* end adds it to
   every pause. Now every beat is timed off the **spoken** end and the build refuses to
   produce a video with a gap over 2.5s.
2. **A teardrop on the publican's cheek** in s7 — a direct No-Fake-Tears violation.
   Regenerated with the grief carried in the eyes, brows and mouth.
3. **s2 read backwards.** The narration says both men went *up* to the temple; the picture
   had them walking *down* the steps toward us — the opposite beat, and it would have killed
   the contrast with s10 (the publican going *down* justified). Restaged with the camera at
   the top of the stairs so they climb toward the viewer.
4. **Wardrobe drift in s7** — he came back in a short-sleeved knee-length tunic with a
   buckled belt while every other shot has an ankle-length long-sleeved robe. A `REF:`
   character lock pins the face, not the clothes; the garment now has to be named in prose.
5. **An extra hand in s5b** — a second hand fused to a single raised wrist with no arm
   behind it. Pose simplified to one clearly-supported raised arm.

*(A sixth defect was in my own QC tooling: `ffmpeg -v error` suppresses `silencedetect`,
which logs at INFO — so my first silence scan reported "nothing found," a false pass created
by the checking command. Re-run properly, it immediately exposed defect 1. All three lessons
are now written into PRODUCTION-BIBLE §4b so the next video gets them for free.)*

---

## Files

- `PROMPTS.md` — 14 shot prompts, Master Style Block byte-identical, `REF:` character locks
- `make_narration.py` — 18 segments (Andrew narrator / Christopher for the KJV lines)
- `qc_narration.py` — the ear-check
- `build.py` — assembly; times every beat off the spoken end and fails on dead air
- `assets/` — the 14 stills · `audio/` — the 18 mp3s · `qc/` — the QC frames
