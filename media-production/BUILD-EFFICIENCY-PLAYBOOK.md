# BUILD EFFICIENCY PLAYBOOK — build MBM videos with the least context/tokens/time

> Written by **Machine B (Windows laptop)** 2026-07-15 after building rows 71, 72, 84
> and diagnosing the #91 Gethsemane fix. This is the "do it fast, get it right the first
> time" companion to FACTORY-ORDERS.md and FLOW-BUILD-PLAYBOOK.md. Everything below was
> paid for in wasted tokens/regens — follow it and a whole video is ~1 focused session.

---

## 0. The golden rules for a cheap session

1. **Read the LAW files at most once** (FACTORY-ORDERS + the queue). Do NOT re-read prior
   build logs, SESSION-LOG, or other builds' PROMPTS. Copy a recent same-shape build's
   `make_narration.py` + `build.py` as templates and change only the story content.
2. **Never screenshot Flow to watch progress.** Screenshots are the #1 token sink and
   time sink. Poll the DOM with a tiny **synchronous** JS snippet instead (below), and
   QC by `Read`-ing the downloaded jpeg, not the browser.
3. **One git push per finished video** = the notification AND a durable checkpoint. If
   context runs out mid-range, the next session just pulls and continues — nothing lost.
4. **Do all non-browser prep before touching Chrome** (claim, storyboard, PROMPTS.md,
   face gate, narration, and even a placeholder build to prove the toolchain). Bundle any
   real blocker into ONE message.

## 1. Per-video pipeline (order matters)

```
git pull --rebase → claim row in QUEUE (commit+push BEFORE generating)
 → write build-NN-slug/PROMPTS.md (12 shots)  → jesus_face_gate.py --dir  MUST exit 0
 → write make_narration.py + build.py from a template  → python make_narration.py
 → Flow: 12 stills (loop below)  → python build.py  → QC frames  → tick Built
 → add title to gen_site_index.py → python gen_site_index.py → commit + pull --rebase + push
```

Storyboard shape that works every time: **12 stills**, ~13 narrator lines + the KJV
line(s) + a closing card. Jesus's spoken KJV = cream-italic caption + a "sacred silence"
(music bed dies). Narrator = white serif, modern paraphrase, never re-quotes the KJV.
Closing card is an **invitation, never a fear-question**.

## 2. The $0 Flow loop (repeat 12×) — this is the whole browser cost

Settings persist across projects: **Image · 9:16 · 1x · Nano Banana 2 → "0 credits"**.
Verify once at the start of a session; then per still:

1. Click the prompt box, type the FULL prompt (style block + body) as ONE line, click the
   → arrow. (If the box may have stale text, `ctrl+a` before typing.)
2. **Poll for completion** with a SYNC snippet (async IIFEs return `{}` — the tool can't
   read a promise's value). Keep a running `known` array of every UUID you've seen:
   ```js
   (() => { const known=[/* all prior UUIDs */];
     const n=[...document.querySelectorAll('img')].map(i=>i.src)
       .filter(s=>s.includes('getMediaUrlRedirect')).map(s=>s.split('name=')[1]);
     return {fresh:n.filter(x=>!known.includes(x))}; })()
   ```
   Newest generation is FIRST in DOM order. Re-run until `fresh` is non-empty (usually
   1–3 polls). A fresh project starts with an empty feed, so `known=[]` for still 1.
3. **Download without a save dialog and without image bytes in context** (Chrome
   "ask where to save" is OFF, files land in `~/Downloads`):
   ```js
   (async()=>{const r=await fetch("https://labs.google/fx/api/trpc/media.getMediaUrlRedirect?name=<UUID>");
     const b=await r.blob();const a=document.createElement('a');
     a.href=URL.createObjectURL(b);a.download='sN-slug.jpeg';
     document.body.appendChild(a);a.click();a.remove();})()
   ```
4. `mv -f ~/Downloads/sN-slug.jpeg <build>/assets/` then **`Read` the jpeg** to QC
   (full-res, this is your only per-still "look"). Downloaded res is 768×1376 (Flow's 1K);
   build.py supersamples to 2160 then lanczos-downscales, so it's fine.

Tip: start a NEW Flow project per video so the feed (and your `known` set) starts empty.

## 3. QC in one look per still — regenerate on any of these

- **Face-law (the #1 law):** Jesus's face NEVER visible. Watch two silent failure modes:
  (a) **infant/holy-figure faces** — a nativity baby must be swaddled + turned away
  (shoot from the FOOT of the manger / from behind the parents / at distance); "face
  turned away and softly shadowed" is NOT enough, it still shows a face — demand "head
  turned entirely away, no face, no cheek, no features." (b) **background Jesus** — a
  room/doorway scene where your prompt didn't stage him can still paint a face-forward
  Jesus at a far table; force the background to "an indistinct warm blur, no readable
  faces, no cream/white robe, the teacher not in this frame."
- **Only Jesus in cream/off-white.** Everyone else in darker earth colors, stated
  positively in every prompt he appears in. (Nativity swaddling linen is the one
  exception — it wraps him.) Ask "could anyone here be mistaken for him?"
- **No baked-in text.** Scrolls/decrees come back with legible English ("Roman Decree").
  Add "only faint indistinct marks, NO readable letters/words/captions anywhere."
- **No storybook border / no oil-paint drift.** Add to every body: "flat clean
  illustrated storybook look, not a heavy textured oil painting; fills the entire frame
  edge to edge with no border, no frame and no cream margin."
- **Anatomy / extra limbs** in crowd or two-person scenes: "only these N people, no third
  person, no extra arms/hands/legs anywhere."
- **Wardrobe/hair/style consistency** across the set. (Hair especially: Jesus is LONG but
  keep it the SAME moderate length every shot — a lone scene with hair cascading to the
  lower back reads as an error and gets the whole video rejected.)

Final render QC: extract ~4 frames with ffmpeg (`-ss T -frames:v 1`) — the KJV caption
frame(s) + closing card + any Jesus beat — and `Read` them. build.py already enforces
≤2.5s dead-air and −15 LUFS; just confirm format 1080×1920 H.264+AAC and size <30MB.

## 4. Diagnosing a REJECTED build fast (don't read 12 stills one by one)

Build a montage and `Read` it once:
```bash
cd <build>/assets
ffmpeg -y -v error -i s1.jpeg -i s2.jpeg ... -i s12.jpeg -filter_complex \
 "[0:v]scale=300:538[a];[1:v]scale=300:538[b];...;[a][b]...[l]xstack=inputs=12:\
 layout=0_0|300_0|600_0|900_0|0_538|300_538|600_538|900_538|0_1076|300_1076|600_1076|900_1076[out]" \
 -map "[out]" "<SCRATCHPAD>/montage.jpg"      # write to the scratchpad, NOT /tmp (Read can't see git-bash /tmp)
```
One `Read` of the montage shows all 12 side-by-side to spot the odd frame. Fix ONLY the
offending still (regen that one asset) + rebuild — never redo the whole video.

## 5. Windows / Machine-B specifics (save an hour of confusion)

- `python` (not `python3`). ffmpeg/ffprobe/edge-tts are on PATH. **PIL is NOT installed
  and not needed** — build.py draws captions with ffmpeg `drawtext`.
- **Fonts:** the template build.py hardcodes Linux serif paths. Make it cross-platform:
  Linux paths if they exist, else copy `%WINDIR%\Fonts\georgia.ttf` + `georgiai.ttf` into
  `segs/` as `serif.ttf`/`serif_bi.ttf` and reference them **relatively** (a bare
  `C:\...` path makes ffmpeg drawtext choke on the drive-colon). See build-91 for the
  pattern. Also make bundled `bin/ffmpeg` optional (fall back to system PATH).
- **gen_site_index.py** must emit forward-slash video paths: `os.path.relpath(...)
  .replace(os.sep, "/")` — Windows backslashes break the live gallery's relative URLs.
  (Already patched in the repo; don't regress it.)
- **git + OneDrive is hazardous.** OneDrive locks `.git/rebase-merge`
  ("error: could not remove '.git/rebase-merge'") and can corrupt a `pull --rebase`
  mid-flight → detached HEAD / stale `main`. Habits: after any pull/rebase run
  `rm -rf .git/rebase-merge .git/rebase-apply`; verify `git rev-parse HEAD` ==
  `git ls-remote origin -h refs/heads/main`; push with the explicit refspec
  `git push origin HEAD:refs/heads/main` (plain `git push origin main` was flaky here);
  and BACK UP a finished build folder to the scratchpad before any `reset --hard`.
- **Commit subjects must NOT start with `#`** — git strip-cleanup during `rebase
  --continue` deletes a leading-`#` subject line. Lead with "Build row NN ..." instead.
- **4 machines push constantly** → expect rebase conflicts in QUEUE.md / index.html /
  gen_site_index.py. index.html is generated (just re-run gen_site_index and re-add);
  in the TITLES map keep BOTH sides' keys; in QUEUE keep both sides' row edits.

## 6. Cost envelope (so you can plan a session)

One clean video ≈ 12 stills, expect **1–3 regenerations** (usually face-law, baked-in
text, or a border/oil-paint drift). A single video is a large fraction of one context
window — so **push after each** and let a fresh session pick up the next row. Don't try to
carry many videos in one context; carry the PLAYBOOK (this file) instead.
