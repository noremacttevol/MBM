# SPEAKER LAW — where this job stands

> 🔴 **REDO-ALL LAW (Cameron, 2026-07-23): the approved-lock is DEAD.** Every video is
> redone with the new voice AND re-approved — prior approval exempts nothing.
> `FIX-LATER.md` is no longer a lock; its 23 builds (the ones still on the OLD Jesus
> voice) go through the rework now. All old approvals were voided (`approvals.json` → `{}`,
> backup `approvals.json.pre-redo-all-2026-07-23`). Worklist: `SPEAKER-LAW/REDO-ALL-worklist.txt`.


**Read this first if you are picking the job up.** It says what is done, what is
running, how to restart it, and the traps that already cost real hours.

Last updated by the session of 2026-07-18.

**UPDATE 2026-07-21 (caption/voice-law verification session): RENDER HALF DONE.**
All 179 non-approved builds with plans are rebuilt under the speaker law and
verified (batch-log.json: 179 shipped, 0 failed). The 21 approved-but-violating
builds are in FIX-LATER.md (locked by approved-lock); build-17 skipped on
standing instruction. Verification is now two-layer: run_batch gates + 
`segcheck.py` (exact per-segment color proof — use it, verify_colors.py drifts
on custom-pacing builds). The render half had resumed earlier that day. Batch running from `queue.txt` (136 non-approved violators; complaints
65/67/184 done first and shipped). run_batch now SKIPS a build while another
session's process has cwd inside it (busy-guard) — safe alongside the
story-coverage / pronunciation sessions. migrate.py now also rewrites
`name in KJV` pacing/timeline uses (builds 20/27 crashed on it; 21/23/25
silently rendered their NEW segments white through the boolean compat path —
found by `segcheck.py`, the exact per-segment color verifier; use it, not just
verify_colors.py). Approved-but-violating builds are listed in FIX-LATER.md and
must not be rebuilt. Log: batch-capfix3.log.

---

## What the job is

Re-narrate and re-colour all 200 MBM story videos so that **who is speaking**
decides both the voice and the caption colour. The full law is in
`media-production/SPEAKER-LAW.md`. Cameron signed off the voices and colours on
2026-07-18.

| Speaker | Colour | Voice |
|---|---|---|
| narrator | white | en-US-AndrewNeural (unchanged) |
| jesus | red `0xEE3322` | en-US-EricNeural |
| god | green `0x5BE38B` | en-US-ChristopherNeural |
| scripture | light blue `0x8FDCFF` | en-US-SteffanNeural |
| woman | pink `0xFF9EC7` | en-US-MichelleNeural |

---

## Status

- **199/199 speaker plans written and validated.** `plans/*.json`. This is the
  whole judgment half of the job and it is DONE.
- **Videos rendered: see `batch-log.json`** — it is the source of truth, not this
  file. `status: "shipped"` means rendered AND verified.
- **All 16 template-B builds converted** to template A. All 6 template-C handled.
- **Two builds may still need Cameron's call** — see `RULE-CONFLICTS.md`. Both
  were short because their plans were thin; both have since been enriched with
  real scripture, so they may now clear on their own.

Check current state with:

```bash
cd media-production/SPEAKER-LAW
python3 -c "import json;d=json.load(open('batch-log.json'));\
print('rendered',sum(1 for v in d.values() if v['status']=='shipped'),'/199');\
print('failing',[k for k,v in d.items() if v['status']!='shipped'])"
```

---

## How to run it

```bash
cd media-production/SPEAKER-LAW
rm -f .batch.lock                      # only if no run_batch is actually alive
nohup setsid python3 run_batch.py > batch.log 2>&1 < /dev/null &
```

It skips anything already `shipped`, so restarting is always safe. One process
only — the lockfile enforces it.

**To re-do one build:** remove its key from `batch-log.json` and it will be
picked up on the next run. If its `build.py` has been hand-edited or repaired,
restore first, or the edits compound:

```bash
cp build-NNN-x/build.py.pre-speaker build-NNN-x/build.py
python3 -c "import sys;sys.path.insert(0,'.');import migrate as M;M.migrate('build-NNN-x',render=False)"
```

---

## Verification — five gates, and why each exists

`run_batch.verify()` refuses to mark a build shipped unless all pass:

1. **mp4 mtime advanced** — a dark caption band proves nothing; the old captions
   drew one too.
2. **full decode, zero errors** — ffprobe reads duration from the container
   header, so a shredded video stream still reports a plausible length and sails
   past a metadata-only check.
3. **trailing quiet ≤ 3.0s**
4. **no surviving `kjv` use** in build.py
5. **source is genuinely migrated** — `make_narration.py` calls
   `save_speaker_narration` and `build.py` carries a `SPEAKER` map.

Two more run separately and are worth running again at the end:

- `python3 verify_colors.py` — proves each video actually PAINTS the colours it
  declares. Nothing else checks the thing the whole pass exists for.
- `python3 verify_audio.py` — transcribes each segment and compares to the
  caption. This is what caught the "thy house" → "my house" defect.

---

## Traps that already cost hours. Do not re-learn these.

**Never run two batches.** Two concurrent processes rendering the same build
interleave their writes and silently corrupt the mp4 — builds 101 and 102 shipped
with 14025 and 5505 decode errors while reporting OK. The lockfile prevents it.

**`pgrep -f run_batch` lies.** It matches the shell's own command line and
reported 5 processes when one was alive. Use
`ps -eo cmd | awk '$1=="python3" && $2=="run_batch.py"'`.

**Never let git touch the working tree mid-run.** `git pull --rebase`
auto-stashed the render's uncommitted work, rebased, and never restored it —
reverting migrated sources, the rendered mp4s AND `batch-log.json` at once. The
queue then re-rendered 17 builds from pre-speaker sources and they passed every
gate that existed at the time. `batch-log.json` and `shipped-to-board.json` are
gitignored now and must stay that way. `ship_loop.py` uses `--no-autostash` and
refuses to rebase a dirty tree.

**Restart the batch after editing `migrate.py`.** A running process holds the old
code in memory and will keep failing builds you have already fixed.

**Four builds carry a stale second mp4** (09, 16, 22, 30). Never pick "the first
mp4 in the directory" — `migrate.output_mp4()` reads the real filename out of
build.py's own ffmpeg call.

**A build's runtime floor message lies.** Several print "must exceed 60s" while
the code reads `if total < 61.0`.

---

## What still needs a person

**Homographs.** Whisper transcribes both readings of *live*, *close*, *bow*,
*sow* identically, so no automated check can judge them, and a guessed respelling
can make things worse — `klohss` for "close" rendered as **"class"**. Every build
prints the homographs it contains at narration time. These need Cameron's ear.

**The stills backlog.** `STILLS-NEEDED.md` + `stills-needed.json` — 728 stills
now hold more than 16s, 293 hold more than 25s where the Ken Burns drift visibly
stalls. Worst is build-10-well at 71.8s on one image. That is a separate art
session, not this one.

**One autostash still in `git stash list`.** It contains `approvals.json` and
`COMPLAINTS.md`, which are Cameron's files. It has deliberately not been dropped
or applied.
