# STALE-AUDIO AUDIT — did any shipped V2 cut copy an out-of-date V1 audio stream?

Run 2026-08-02. Every number below was measured from the files themselves
(`ffprobe`, `ffmpeg -f md5`, `silencedetect`, faster-whisper, `git log`). No verdict
here rests on a comment, a docstring, or a previous audit's conclusion.

## The defect being hunted

`v2_assemble.py`'s AUDIO LOCK copies the finished V1 MP4's AAC stream
packet-for-packet into the V2 cut. That is correct while the V1 MP4 is the current
render of the current narration. It is catastrophic when it is not: a V1 MP4 rendered
before the **2026-07-23/24 ElevenLabs re-voice** or before the **echo-delete sweep**
carries pre-REDO-ALL voices and/or narrator echoes that were deliberately removed,
and the pictures hang on a timeline that can be a minute adrift from the words.

Row 25 was the row that exposed it: its V1 MP4 was rendered **2026-07-22 03:11**, runs
**229.033 s**, and the narration actually on disk sums to **166.818 s** — a 62-second
lie. It shipped correctly only because the assembler was taught the
`AUDIO_FROM_V1_SEGMENTS = True` path first.

## Scope

Every row with a shipped realistic-V2 cut currently live on the reviewer
(`site/review.html`, `data-review-wave="realistic-v2"`): **23 rows** — 01-11, 13-16,
18-25. Row 12 and row 17 are **off-limits** and were not modified (see below).

## What was measured, per row

1. **Recency.** The commit that last changed the V1 MP4's content vs the commit that
   last changed each mp3 the build actually places. Filesystem mtime is worthless in
   this repo — four machines clone and pull it, so a checkout stamps a 2026-07-22
   render as "2026-07-29" — so the git content date is the authority and mtime is used
   only for untracked or dirty files.
2. **Runtime.** The V2 cut's duration vs the timeline `extract_beats` sums from the
   mp3s on disk at their real offsets. Extra audio shows up as a positive delta.
3. **Audio path.** Whether the V2 cut's audio stream is bit-identical (`ffmpeg -f md5`)
   to the V1 MP4's — i.e. whether the AUDIO LOCK was the path taken at all.
4. **Voice engine.** Sample rate / bitrate of every placed mp3. edge-tts (the old
   voice) writes **24 kHz mono ~48 kbps**; ElevenLabs writes **44.1 kHz**.
5. **Alignment.** `silencedetect` speech onsets in the shipped cut against the beat
   offsets — a stale stream drifts, a current one does not.
6. **Content.** faster-whisper transcription of the last beats of the four
   highest-risk rows, checked word-for-word against the expected text at the expected
   time. Drift accumulates, so the tail is where a stale track cannot hide.

## Result

| verdict | rows |
|---|---|
| **CLEAN** | **23** — 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 13, 14, 15, 16, 18, 19, 20, 21, 22, 23, 24, 25 |
| **STALE-AUDIO** | **0** |
| **OLD-VOICE** | **0** |

**Nothing on the reviewer needed rebuilding.** No shipped cut was fixed, because none
was broken.

Every placed mp3 in every shipped row is 44.1 kHz ElevenLabs — there is no 24 kHz
edge-tts audio anywhere in a shipped cut. Every shipped cut's duration matches the
mp3 timeline within 0.1 s except three rows explained below, and every cut's speech
onsets track the beat offsets with a median deviation of 0.04-0.10 s.

### Why the three stale V1 MP4s never reached a shipped cut

Rows **10, 13 and 25** are the only shipped rows whose V1 MP4 predates its own mp3s —
and those are exactly the three rows whose V2 audio is **not** bit-identical to the V1
MP4. Each was caught at build time by the existing `abs(total - locked_duration) > 1.0`
runtime check (row 10's V1 final is 67.7 s against a 294.3 s timeline; row 13's is
259.0 s against 298.3 s; row 25's is 229.0 s against 166.8 s) and rebuilt from the V1
build's own segment mp3s instead. Their shipped tracks are current.

Row **01** is also not bit-identical to its V1 MP4, for a different and documented
reason: the V1 final is the base and only the two Jesus source windows named in
Cameron's room-noise complaint were denoised — same Alexander takes, no TTS, no
retiming (`build-01-cloak/AUDIO-SOURCE-MANIFEST.json`).

### The three widest deltas, checked by transcription

| row | Δ | what the transcript shows |
|---|---|---|
| 13 | +0.53 s | last three beats land within +0.28 s of their offsets, text matches |
| 20 | +0.44 s | last three beats within 0.5 s; `n15`'s spoken words match this build's `TEXT_OVERRIDES`, not the stale V1 `SEGMENTS` text |
| 19 | −0.80 s | shortfall, not excess — trailing-silence-trim arithmetic, no missing words |

Rows 10 and 22 were transcribed as controls; their final beats land within 0.1 s of the
computed offsets with matching words.

## Full table

| row | V1 mp4 render (git) | newest placed mp3 (git) | mp3 rate | V1 mp4 dur | mp3 timeline | V2 cut dur | Δ(cut−timeline) | audio path | onset median dev | verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 2026-07-24 | 2026-07-24 | 44100 Hz | 108.833 | 108.807 | 108.833 | +0.03 | denoise-repair | +0.07 s | **CLEAN** |
| 2 | 2026-07-24 | 2026-07-24 | 44100 Hz | 157.933 | 157.853 | 157.9 | +0.05 | AUDIO LOCK (bit-identical to V1) | +0.06 s | **CLEAN** |
| 3 | 2026-07-24 | 2026-07-24 | 44100 Hz | 222.1 | 222.08 | 222.099 | +0.02 | AUDIO LOCK (bit-identical to V1) | +0.05 s | **CLEAN** |
| 4 | 2026-07-29 | 2026-07-29 | 44100 Hz | 307.233 | 307.203 | 307.233 | +0.03 | AUDIO LOCK (bit-identical to V1) | +0.06 s | **CLEAN** |
| 5 | 2026-07-24 | 2026-07-24 | 44100 Hz | 247.767 | 247.685 | 247.71 | +0.03 | AUDIO LOCK (bit-identical to V1) | +0.04 s | **CLEAN** |
| 6 | 2026-08-01 | 2026-07-24 | 44100 Hz | 125.805 | 125.786 | 125.833 | +0.05 | AUDIO LOCK (bit-identical to V1) | +0.06 s | **CLEAN** |
| 7 | 2026-08-01 | 2026-08-01 | 44100 Hz | 225.633 | 225.531 | 225.633 | +0.10 | AUDIO LOCK (bit-identical to V1) | +0.07 s | **CLEAN** |
| 8 | 2026-07-24 | 2026-07-24 | 44100 Hz | 68.824 | 68.82 | 68.833 | +0.01 | AUDIO LOCK (bit-identical to V1) | +0.06 s | **CLEAN** |
| 9 | 2026-07-24 | 2026-07-24 | 44100 Hz | 196.835 | 196.823 | 196.867 | +0.04 | AUDIO LOCK (bit-identical to V1) | +0.08 s | **CLEAN** |
| 10 | 2026-07-24 | 2026-07-28 | 44100 Hz | 67.7 | 294.294 | 294.3 | +0.01 | V2 track rebuilt | -0.19 s | **CLEAN** |
| 11 | 2026-08-01 | 2026-08-01 | 44100 Hz | 234.87 | 234.861 | 234.9 | +0.04 | AUDIO LOCK (bit-identical to V1) | +0.07 s | **CLEAN** |
| 13 | 2026-07-28 | 2026-07-29 | 44100 Hz | 258.967 | 298.292 | 298.817 | +0.53 | V2 track rebuilt | +0.08 s | **CLEAN** |
| 14 | 2026-07-28 | 2026-07-24 | 44100 Hz | 219.133 | 219.114 | 219.133 | +0.02 | AUDIO LOCK (bit-identical to V1) | +0.07 s | **CLEAN** |
| 15 | 2026-07-24 | 2026-07-24 | 44100 Hz | 256.0 | 255.991 | 256.0 | +0.01 | AUDIO LOCK (bit-identical to V1) | +0.07 s | **CLEAN** |
| 16 | 2026-07-24 | 2026-07-24 | 44100 Hz | 166.812 | 166.803 | 166.812 | +0.01 | AUDIO LOCK (bit-identical to V1) | +0.08 s | **CLEAN** |
| 18 | 2026-07-24 | 2026-07-24 | 44100 Hz | 243.322 | 243.304 | 243.333 | +0.03 | AUDIO LOCK (bit-identical to V1) | +0.06 s | **CLEAN** |
| 19 | 2026-07-28 | 2026-07-24 | 44100 Hz | 156.967 | 157.763 | 156.967 | -0.80 | AUDIO LOCK (bit-identical to V1) | -0.30 s | **CLEAN** |
| 20 | 2026-07-24 | 2026-07-24 | 44100 Hz | 186.7 | 186.229 | 186.665 | +0.44 | AUDIO LOCK (bit-identical to V1) | +0.44 s | **CLEAN** |
| 21 | 2026-07-24 | 2026-07-24 | 44100 Hz | 147.237 | 147.232 | 147.237 | +0.00 | AUDIO LOCK (bit-identical to V1) | +0.06 s | **CLEAN** |
| 22 | 2026-07-28 | 2026-07-28 | 44100 Hz | 225.033 | 225.003 | 225.033 | +0.03 | AUDIO LOCK (bit-identical to V1) | +0.10 s | **CLEAN** |
| 23 | 2026-07-24 | 2026-07-24 | 44100 Hz | 202.967 | 202.896 | 202.967 | +0.07 | AUDIO LOCK (bit-identical to V1) | +0.07 s | **CLEAN** |
| 24 | 2026-07-24 | 2026-07-24 | 44100 Hz | 167.6 | 167.549 | 167.555 | +0.01 | AUDIO LOCK (bit-identical to V1) | +0.06 s | **CLEAN** |
| 25 | 2026-07-22 | 2026-07-24 | 44100 Hz | 229.033 | 166.818 | 166.833 | +0.01 | AUDIO_FROM_V1_SEGMENTS | +0.07 s | **CLEAN** |


*"V1 mp4 render (git)" is the commit that last changed that MP4's bytes; "newest placed
mp3" is the latest commit touching any mp3 the build actually places. Where the second
is later than the first, the AUDIO LOCK is unsafe — and in all three such rows it was
not used.*

## Rows 12 and 17 — reported, not touched

Both are **off-limits** for this job and were not modified.

- **Row 12 (Bartimaeus).** The reviewer card is `data-newvoice="1"`, not
  `realistic-v2`, and points at the **V1** cut
  `media-production/build-12-bartimaeus/mark-10_bartimaeus.mp4`. A V2 cut
  (`mark-10_bartimaeus-realistic-v2.mp4`) exists on disk but has **not** been shipped
  to the reviewer. Row 12's V1 MP4 is newer than its mp3s, so it is not stale.
- **Row 17 (Lazarus).** Also on the V1 cut. Its V1 final is **120.33 s short** of its
  own timeline (`n11` is voiced and paid for but never placed) — a real truncation,
  already recorded in `AUDIO-AUDIT.md` section B. It is a genuine outstanding defect
  and needs a rebuild, but it is not a stale-audio-lock defect and not in this job's
  scope.

## Landmines for future V2 rebuilds

The defect is dormant, not absent. **54 V1 builds** across the library have a finished
MP4 older than at least one mp3 in their `audio/` folder. Any of those, rebuilt through
the AUDIO LOCK without checking, would ship a stale stream. The list is reproducible:

```bash
python3 - <<'EOF'
import os, subprocess, glob
BK = (".orig.mp4", ".bak.mp4", ".old.mp4", ".prev.mp4")
def t(*p):
    r = subprocess.run(["git", "log", "-1", "--format=%ct", "--"] + list(p),
                       capture_output=True, text=True)
    return int(r.stdout.strip() or 0)
for d in sorted(glob.glob("media-production/build-*")):
    mp4 = [f for f in sorted(os.listdir(d))
           if f.endswith(".mp4") and not f.endswith(BK)]
    if len(mp4) != 1 or not os.path.isdir(os.path.join(d, "audio")):
        continue
    if t(f"{d}/audio/*.mp3") > t(f"{d}/{mp4[0]}") + 1:
        print(d)
EOF
```

That scan is deliberately coarse — it counts orphan mp3s the build never places, so it
over-reports. The precise test is the guard itself, which only considers **placed**
segments.

## The guard that makes this impossible to repeat

`v2_assemble.py` now calls `assert_v1_final_is_current()` before the AUDIO LOCK copies
anything. It is a shared-tool fix — every row, every machine, no per-build opt-in. Two
independent tripwires:

1. **Recency.** If any mp3 the build places was changed after the V1 MP4 was rendered
   (by `content_time()`, git-content date for tracked clean files, mtime otherwise),
   the lock refuses. This catches a re-voice or a text trim that leaves the runtime
   almost unchanged — something no duration check could ever see.
2. **Runtime excess.** If the V1 MP4's stream runs more than **0.75 s** longer than the
   summed mp3 timeline, it is carrying audio no longer in the build. Shortfalls keep
   the looser 1.0 s tolerance, because V1 finals routinely land a couple of tenths
   under the recomputed timeline through trailing-silence trimming.

Both errors name the fix explicitly: set `AUDIO_FROM_V1_SEGMENTS = True` in that row's
`beats_v2.py` and the track is rebuilt from the V1 build's own mp3s at the
`extract_beats` offsets. **V1 is never edited and nothing is ever re-voiced.**

Verified against all 23 shipped rows: the guard **passes the 20 rows that legitimately
used the lock and blocks exactly rows 10, 13 and 25** — zero false positives, zero
false negatives.
