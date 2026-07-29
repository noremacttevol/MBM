# KICKOFF — PUT THE ALREADY-FIXED PICTURES INTO THE MOVIES (paste into a new chat)

You are the **re-render session**. One job, and it is not creative work:

> Dozens of pictures were repainted correctly, committed, and pushed — and then never
> made it into the finished video, because nobody re-rendered. **Cameron has been
> watching videos that still show defects he reported and we already fixed.**
> Your job is to find every one of those and re-render it, and to PROVE it landed.

Paint nothing. Redesign nothing. Just make the movies match the pictures.

---

## 0. FIRST ACTIONS
1. `hostname` → look it up in `MACHINE-IDENTITY.md`. Never trust a "this machine is X"
   note inside a shared file — all four computers read the same files.
2. Read the top entry of `SESSION-LOG.md`, `git log --oneline -5`, confirm its commit is
   present. First message to Cameron = one-line recap + that hash.
3. `git pull --rebase origin main`.

---

## 1. GET THE REAL LIST — look at pixels, never at dates

```
python3 still_in_movie.py --all        # ~30 min of ffmpeg, the authoritative answer
```

It samples frames from each finished mp4 and reports which wired stills are genuinely
absent. **Do not substitute a git-based check.** One was tried and it was wrong:
`picture_render_status.py` reported "0 stranded" while 50+ stills were missing, because a
commit timestamp records when a file was saved, never what was on disk when ffmpeg ran. A
machine that pulls once at the start of a long batch commits brand-new mp4s built from
days-old stills. **#112 is the proof case: re-rendered and committed at 02:10, 42 minutes
after the fix, and the movie still carried a five-day-old picture.**

Known stale as of 2026-07-28 (19 videos, 50 stills — expect the `--all` sweep to find more,
because this list came from the narrower git-flagged set that missed #112):

| video | stills missing |
|---|---|
| build-10-well | 11 |
| build-89-the-last-supper | 7 |
| build-92-peters-denial | 5 |
| build-63-man-born-blind | 3 |
| build-132-forbid-him-not, build-15-centurion, build-162-keys-of-kingdom, build-163-apostles-prophets, build-185-many-mansions-member, build-193-the-comforter, build-197-sons-and-daughters-prophesy, build-200-gospel-to-all-the-world, build-88-triumphal-entry | 2 each |
| build-100-the-ascension, build-164-unity-of-faith, build-61-syrophoenician-woman, build-67-the-transfiguration, build-90-washing-feet, build-96-it-is-finished | 1 each |
| build-112-beatitudes | 1 — **git says current, pixels say stale** |

---

## 2. CLAIM BEFORE YOU RENDER — this is the one that can destroy work

Another session is running the REDO-ALL voice sweep and re-rendering videos continuously.
**Two machines rendering the same build at once corrupts a 250MB file.** Rendering is the
only genuinely destructive operation in this whole pipeline.

Before each build: add a row to `RERENDER-CLAIMS.md` with the build, your machine and the
time, **commit and push the claim FIRST**. If the push is rejected, someone took it —
pull and move to the next one. Remove your row when the build is done and pushed.

Also check the claim is still sane: `git log --oneline -5 -- <build>/*.mp4`. If another
machine committed that mp4 in the last few minutes, skip it and come back.

---

## 3. THE RENDER LOOP (one build at a time, never in parallel — ffmpeg is CPU-bound)

```
git pull --rebase origin main      # IMMEDIATELY before each build, not once per batch.
                                   # This is the exact mistake that created the backlog.
cd build-NN-slug && python3 build.py
rm -rf segs/                       # ~400MB scratch dir
```

**Never leave a half-written video.** If build.py is killed or errors, restore the
committed one with `git checkout -- <the mp4>` before doing anything else.

Verify the file is whole:
```
ffprobe -v error -show_entries format=duration -of csv=p=0 <mp4>
```

---

## 4. PROVE IT — the step whose absence caused all of this

```
python3 still_in_movie.py --dir build-NN-slug
```
Must come back clean for that build. If it still reports the still as missing, the render
did not pick it up — check that the slug actually appears in `build.py`'s BEATS
(`grep <slug> build.py`). **A still that is not wired into BEATS will never appear no
matter how many times you rebuild** — that is the assembly session's job, not yours; say
so plainly instead of rebuilding again.

Then commit and push. **Pushing video is slow (~250MB) and a piped push can report success
while actually being rejected** — always confirm with:
```
git rev-list --count origin/main..HEAD     # must be 0
```
If another machine pushed mid-upload, `git pull --rebase` and push again.

---

## 5. KNOWN BLOCKERS — do not fight these
- **build-92-peters-denial will not render.** Its own guard reports
  `DEAD AIR: 2.78s gap before n5c` (limit 2.5s). Five stranded stills are waiting behind
  it. This is an AUDIO TIMING problem for the audio/assembly session. Do not hack past the
  no-dead-air law and do not disable the guard — hand it over and move on.
- **Machine C cannot deploy** (no `node`/firebase), so it cannot publish to
  milk-b4-meat.web.app. Re-rendered videos go to git; a node machine deploys them.
- Two genuine build.py bugs were found and fixed this way before (build-99's `s[4]`→`s[2]`
  on 3-long tuples, build-181's dead `n1b` beat). If you hit a provable crash of that
  class, fix it, say exactly what you changed and why, and verify by rendering. Otherwise
  leave build.py alone — it belongs to the assembly session.

---

## 6. WHAT TO TELL CAMERON AT THE END
Plain words, no jargon: **which videos he can now re-watch, and what changed in each.**
He has been re-reporting defects that were already fixed, so the useful sentence is of the
form "#10 the well — the 11 corrected pictures are now actually in the video."
Then add a `SESSION-LOG.md` entry at the top, commit, push.
