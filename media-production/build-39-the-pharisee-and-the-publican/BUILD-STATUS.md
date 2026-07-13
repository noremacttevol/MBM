# Build #39 — The Pharisee and the Publican — STATUS

**Date:** 2026-07-13 · **Machine:** Dev · **State:** everything done except the pictures.
**Blocked on:** the Gemini image API key has **no image quota** (see below). This is the
only thing standing between this build and a finished video.

---

## 🛑 THE BLOCKER (Cameron has to do this — it is 2 minutes, in a browser)

`gen_stills.py` calls the official Gemini image API. Every image model returns:

```
HTTP 429  RESOURCE_EXHAUSTED
Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests,
limit: 0, model: gemini-2.5-flash-preview-image
```

**Read that carefully: `limit: 0`.** This is NOT "we used up today's allowance." It means the
allowance is *zero*. **Image generation on the Gemini API is a paid feature — the free tier
does not include it at all.** The key itself is fine: the same key generates *text* without a
complaint, so it is valid, live, and correctly loaded. Only images are refused, and they are
refused because the Google Cloud project behind the key has **no billing account attached**.

Verified on 2026-07-13 against `gemini-2.5-flash-image`, `gemini-3.1-flash-image` and
`gemini-3-pro-image` — all three return the same `limit: 0`. There is no second key, no
`gcloud` install, and no other credential anywhere on this machine.

**The fix:** open <https://aistudio.google.com/apikey>, find the project this key belongs to,
and click **"Set up billing"** (or attach the key to a project that already has billing).
Nothing else changes — no code, no prompts, no re-planning.

**What it will cost:** 14 stills × $0.039 = **$0.55** for this whole video. (~$0.55/video ×
200 videos ≈ $110 for the entire corpus, on the cheap model.)

An AI session cannot do this step: it needs Cameron's Google account and a payment method.
That is the definition of a genuine blocker under Law D/F — everything else was run to
completion.

---

## ✅ DONE AND VERIFIED (nothing here needs redoing)

| Step | State | Evidence |
|------|-------|----------|
| Luke 18:9–14 studied in full context | ✅ | Pack §1 — incl. why v9 and v14 cannot be cut |
| Production pack + scripture card | ✅ | `../39-pharisee_publican-production-pack.md` |
| Storyboard — 14 stills, 18 segments | ✅ | Pack §3 |
| Prompt sheet, Master Style Block byte-identical | ✅ | `PROMPTS.md`, 14 shots parse clean |
| 🛑 **FACE GATE** | ✅ **PASS, exit 0** | `jesus_face_gate.py --dir .` — passed first run |
| Narration (Andrew + Christopher, no Multilingual) | ✅ | `audio/*.mp3`, 18 segments |
| 🛑 **EAR-CHECK** (every segment vs script) | ✅ **18/18 pass** | `qc_narration.py` — worst 0.96 after tie-break |
| Assembly script | ✅ **rehearsed end-to-end** | `build.py` — ran clean on placeholder frames |
| No-Dead-Air scan | ✅ **worst gap 2.03s** (law: ≤2.5s) | build.py now *fails the build* if any gap >2.5s |
| Loudness | ✅ **−14.8 LUFS** (target ≈ −15) | `ebur128` on the rehearsal mix |
| File size / format | ✅ **9.8 MB**, 1080×1920, H.264 | under the 25 MB law with room to spare |
| Runtime | ✅ **4.55 min** | in line with #11 storm (4.5 min) |
| Caption + card typography | ✅ | KJV cream italic; card cream #F7F2E9, held 14.4s |

The rehearsal used flat colour placeholders purely to prove the timing, captions, mix and
encode. **It was deleted afterwards** — there is no video in this folder and nothing here
can be mistaken for a deliverable.

### Two real defects the self-revision loop caught and fixed (before Cameron ever saw them)

1. **Dead air after both KJV lines.** The pauses after j2 and j3 measured **2.76s and 2.73s**
   — over the 2.5s law. Cause: the TTS files carry a silent tail (~1.3s on the Jesus voice,
   ~0.45s on the narrator), and timing off the *file* end silently adds that tail to every
   pause. This is the same defect the PRODUCTION-BIBLE records from video #2. `build.py` now
   measures the **spoken** end of every mp3 and computes all gaps from that, and it *hard-fails
   the build* if any spoken gap exceeds 2.5s. Worst gap is now 2.03s.
2. **A caption wall and an overloaded still.** Segment n8 was 75 words — a 13-line caption (and
   captions are verbatim) — and still `s5` was carrying 47 seconds of narration on one picture,
   against "never lean on one image to cover a long stretch." n8 was split into n8a/n8b and two
   stills were added (`s5b-the-list`, `s7b-the-lamb`), which also gave the atonement gem its
   own image.

*(A third defect was in my own QC tooling: `ffmpeg -v error` suppresses `silencedetect` and
`volumedetect`, which log at INFO. My first silence scan reported "no silence found" — a false
pass produced by the checking command, not by the video. Re-run with default verbosity, it
immediately exposed defect 1. Worth remembering: a QC tool that reports nothing is suspicious
until you prove it can still report something.)*

---

## ▶ TO FINISH THIS VIDEO (after billing is on — three commands, ~10 minutes)

```bash
cd /home/noremacttevol/Desktop/Brain/MBM

# 1. the pictures (~$0.55) — the face gate re-runs automatically first
python3 media-production/gen_stills.py --dir media-production/build-39-the-pharisee-and-the-publican

# 2. QC every still: anatomy count, action reads right, morning light, painted
#    style, no baked-in text, and the face audit — Jesus appears ONLY in
#    s1-the-certain-men and s9-the-verdict, both from directly behind.
#    Regenerate any miss:
#    python3 media-production/gen_stills.py --dir <...> --only s7-be-merciful

# 3. assemble (prints the runtime, the silence map and the loudness)
cd media-production/build-39-the-pharisee-and-the-publican && python3 build.py
```

Then: tick `Built` for row 39 in `media-production/QUEUE.md`, commit, push, show Cameron.

**The QC pass on the generated stills is the one piece of work still genuinely outstanding** —
it cannot be done before the images exist. Everything else is finished and checked.
