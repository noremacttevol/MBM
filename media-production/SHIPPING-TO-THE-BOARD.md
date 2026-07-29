# Shipping a rebuilt video to the review board

**Read this before you touch `site/story-videos/` or run a deploy.**
Written 2026-07-19 after 147 finished rebuilds sat invisible on this machine
while Cameron kept saying the videos had not changed.

---

## The one thing that goes wrong

`gen_site_index.py` points each card at **GitHub raw** unless the row is listed
in `site/fixed/SERVE-LOCAL.txt` **and** `site/fixed/<row>.mp4` exists. Stage into
`site/fixed/` — **never** `site/story-videos/`, which the app's compression
pipeline rewrites and which clobbered these fixes once already (2026-07-19).
The repo is ~39 GB and the push backlog
has been failing for days — so a card pointing at GitHub shows the **old cut**,
no matter how many times the video was rebuilt and verified locally.

A build being `shipped` in `SPEAKER-LAW/batch-log.json` means it RENDERED.
It does **not** mean Cameron can see it.

## Never strip a SERVE-LOCAL row on faith

The file's old header said "remove a number once its commit lands on GitHub."
Rows were removed while the commits had **not** landed, which silently rolled
135 cards back to the old-voice cuts. Only remove a row after comparing bytes:

```bash
local=$(stat -c%s media-production/build-NN-x/book-ch_slug.mp4)
raw=$(curl -sIL https://github.com/noremacttevol/MBM/raw/main/media-production/build-NN-x/book-ch_slug.mp4 \
      | awk -F': ' 'tolower($1)=="content-length"{print $2}' | tr -d '\r' | tail -1)
[ "$local" = "$raw" ] && echo SAFE-TO-REMOVE || echo STILL-STALE
```

## Deploy: three traps, all hit in one night

1. **`FIREBASE_HOSTING_UPLOAD_CONCURRENCY=4` is mandatory.** firebase-tools
   defaults to **200** parallel uploads. With 20 MB videos on a home uplink that
   fails every time, and the CLI reports it as the useless
   `TypeError: Converting circular structure to JSON`. At 4 it goes through.
2. **Prune first.** Free-tier hosting storage caps at 10 GB and each deploy
   stores a full copy of `site/`. When it 429s, run
   `python3 media-production/prune_hosting_versions.py`.
3. **Temp files kill a deploy.** Firebase lists the folder, then dies with
   `ENOENT` when another session's atomic copy renames its temp away
   mid-upload. `firebase.json` now ignores `**/*.tmp` and `**/*.tmp.*` —
   keep any staging temp name under those patterns.

The working invocation:

```bash
cd ~/Desktop/MBM
python3 media-production/gen_site_index.py
python3 media-production/prune_hosting_versions.py
FIREBASE_HOSTING_UPLOAD_CONCURRENCY=4 npx firebase deploy --only hosting
```

Retry on failure — each pass resumes from what already uploaded. It took 6
passes on a 3.3 GB site.

## Not done until the live bytes match

```bash
curl -sIL https://milk-b4-meat.web.app/story-videos/NN.mp4 | grep -i content-length
```

must equal the local file size, for **every** row in SERVE-LOCAL.txt. Anything
else and Cameron is watching a stale cut.
