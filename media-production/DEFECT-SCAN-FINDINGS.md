# DEFECT SCAN — machine pass over all delivered videos (2026-07-17, ASSEMBLY-C)

Ran `scan_defects.py` over the **197 delivered mp4s**. It checks the ~9
defect types from [DEFECT-CATALOG.md](./DEFECT-CATALOG.md) that a machine can
judge on a finished file; the other ~40 need eyes and are left as `EYES` in
[DEFECT-SCAN.csv](./DEFECT-SCAN.csv) (200×48 checklist, prefilled).

To re-run after fixes: `python3 media-production/scan_defects.py`

## Result: 174 auto-PASS · 3 real defects · 20 borderline pauses

### 🔴 3 HARD FAILS — real, fix these

| Row | Video | Problem |
|-----|-------|---------|
| 8 | luke-15_lost-coin | **56s (under the >60s floor)** AND a **10.85s dead-air stretch** mid-body (29.7→40.6s), plus 3.1s and 3.5s gaps earlier. This one is genuinely broken — long silent holes. Rebuild the timing. |
| 137 | acts-7_stephen-sees-him-standing | **4.44s dead-air** mid-body |
| 142 | john-8_i-am-the-light-of-the-world | **4.13s dead-air** mid-body |

### 🟡 20 MINOR — 2.5–3.5s pauses, verify (almost all intentional sacred silence)

All are early videos (rows 7–38). Each has a single spoken gap of 2.5–2.84s
(row 14 = 3.35s) — these are the **sacred-silence pauses around the KJV lines**
that grew a hair past the 2.5s mechanical law in the earliest builds (the exact
"KJV pause silently grew" issue the Bible warns about, before `spoken_of()` gap
enforcement was added). They read as reverent, not broken, but a timing-tighten
pass would bring them under the law:

`7, 9, 11, 14, 15, 16, 19, 20, 21, 23, 24, 25, 27, 29, 30, 32, 33, 35, 36, 38`

### ✅ Confirmed clean library-wide (0 flags)

- **Hum (#6):** zero. After fixing a false positive (the first pass mis-read the
  narrator's closing-card *voice* — whose fundamental sits at 110–330 Hz — as
  hum), every video's true-silence window is quiet. The 2026-07-16 hum purge
  held across the whole library.
- **Filename law (#43):** all `book-chapter_slug.mp4`.
- **Format (#44):** all 1080×1920, 9:16, play clean.
- **Size/bitrate (#45):** all under 30MB, none starved.
- **Loudness:** all near −15 LUFS.

## What still needs EYES (the other ~40 defects)

The CSV marks these `EYES` per video — they can't be machine-judged:
captions (taste/split/coverage), tofu glyphs, face consistency & ethnicity,
anatomy & duplicates, look-drift, action logic (on-the-water, direction vs
narration), content-care (gore, embodied Satan, shame, fear-cards, child-in-
peril), style drift, gibberish text, modern objects, must-show/must-never-show,
verse-card source, seed-question match. Fastest path: builders open the CSV,
filter to their rows, and tick these columns as they watch.
