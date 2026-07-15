# FLOW-BUILD-PLAYBOOK — the fast, low-token way to build one video ($0)

> Written 2026-07-15 (Machine C) after building #91 Gethsemane, #121 Salt & Light, and a
> full betrayal-kiss set. This is the **proven, efficient procedure** distilled so the
> next session spends less context / fewer tokens / less time for the SAME quality.
> It changes NO pipeline file — it just records what already works. Read it once after
> CREW-GUIDE + PRODUCTION-BIBLE laws + build-47 BUILD-STATUS, then follow it.
>
> Non-negotiables still bind: face-never, only-Jesus-cream, two-voice exact-KJV,
> stills-only, night/day matches scripture, 30MB cap, closing card = invitation.

---

## The whole loop, in order (one video ≈ this and nothing more)

1. `git pull --rebase`. In QUEUE.md find the lowest row **in your machine's range**
   (FACTORY-ORDERS) with Built ⬜ and Claim empty. `mkdir build-NN-slug/assets`,
   stamp `CLAIMED Machine X <date>` in that row, commit + push **before generating**.
2. Read the KJV passage. Check CONTENT-CARE by **story name** (its number table can lag a
   catalog renumber — trust the name, not the row number).
3. Write `PROMPTS.md` from a template (copy `build-48` or `build-41`). 8–12 stills.
   Master Style Block byte-identical. Character/wardrobe locks in every prompt a
   character appears in.
4. `python3 media-production/jesus_face_gate.py --dir build-NN-slug` → **exit 0**.
   Common trips: any facial word next to a Jesus token (`his cheek/beard/eyes/jaw/…`,
   `profile`, `close-up`); and **header/law paragraphs that name "Jesus" but have no
   hiding cue** — add "seen only from behind, his face never shown" to those too.
5. **Flow burst** (below) — generate + QC + download each still.
6. `python3 make_narration.py` (copy a template; two voices, exact-KJV lines).
7. `python3 build.py` (copy a template; see the build.py notes below).
8. QC the render: extract 3–4 frames with the bundled ffmpeg, `Read` them (KJV caption
   exact + cream-italic + legible, face hidden, closing card an invitation).
9. Tick **Prep+Built** in QUEUE.md (leave Appr — that's the monitor's job). Add the
   title to `gen_site_index.py` TITLES, run it (see PATH note), commit index.html.
10. `git add -A`, commit, `git pull --rebase`, `git push`. SESSION-LOG entry. Done.
    **One video per chat** — then open a fresh chat and say "Continue".

---

## Flow $0 — the exact settings and the reliable download

- One project, reused across the whole video (and even across videos — the download
  logic below always grabs the newest, so a mixed gallery is fine).
- Bottom prompt bar → set once: **Image · 9:16 · 1x · Nano Banana 2** → the chip must read
  "🍌 Nano Banana 2 · 1x" (0 credits — the default for ordinary stills). CORRECTED
  2026-07-15: Nano Banana **Pro and credit-costing models are ALLOWED and encouraged**
  where they buy quality or fewer rerolls (master face, Jesus close-ups, crowds) —
  Cameron's Flow credits are prepaid and expire monthly. Only the paid Gemini API
  stays banned. Keep a video roughly under 150 credits; note spend in the queue row.
- Per still: click the prompt box, `type` the FULL prompt on ONE line (no embedded
  newlines — Enter submits), click the submit arrow, `wait 10s`.

**Download (clean jpeg, no zip, low-token):** the gallery thumbnails are a *virtualized*
list — the `<img>` elements only mount when scrolled into view.
1. Click **Images** (left nav), then **scroll the gallery down ~3 ticks** so thumbnails
   mount. (Flow's own download button gives a `.zip` — avoid it.)
2. JS (returns a value, so you can read it):
   ```js
   [...document.querySelectorAll('img')].filter(i=>i.src.includes('getMediaUrl'))
     .map(i=>new URL(i.src).searchParams.get('name').slice(0,8))
   ```
   The **newest generation is index 0**. Confirm it differs from the last one you saved.
3. JS download by that name (side-effect only; tool shows `{}` — that's fine):
   ```js
   (async()=>{const img=[...document.querySelectorAll('img')].find(i=>i.src.includes('<name8>'));
   const b=await(await fetch(img.src)).blob();const u=URL.createObjectURL(b);
   const a=document.createElement('a');a.href=u;a.download='sN-slug.jpeg';
   document.body.appendChild(a);a.click();a.remove();})()
   ```
4. `mv ~/Downloads/sN-slug.jpeg assets/` then **`Read` the file to QC** (Read renders the
   image — far cheaper and sharper than browser screenshots; the JS query already tells
   you the image exists, so **skip the per-step screenshot** — that's the token hog).
   Chrome's "ask where to save" is OFF, so downloads land straight in `~/Downloads`.

**Reroll rules (Nano Banana 2 quirks):**
- **Panels/triptychs**: intimate 2-figure scenes and wide landscapes often come back
  split into stacked halves or a comic strip. Prepend **"ONE single unbroken full-frame
  picture, no panels, no comic strip, no triptych, no dividing lines"** and reroll.
- **Face leak on prayer/bowing**: "bowed forward over a rock, hands pressing" pulls the
  camera to his FRONT and shows facial planes. Use **UPRIGHT kneeling seen strictly from
  behind** ("camera behind, his back and the back of his head to us, face into the dark
  ahead"). This composition is reliably face-safe.
- **Hood consistency**: the model sometimes drapes a hood; the standard is **bare-headed,
  long hair flowing loose**. Say "bare-headed, NO hood, hair worn loose and uncovered"
  if it recurs.
- Incidental pale robes on **headless / short-haired** background figures don't break the
  only-cream law (the law guards the *two signatures together* — long hair + cream). Only
  reroll if a figure could actually be mistaken for Jesus.

---

## make_narration.py / build.py — copy, change only story content

- Both are ~identical every video. Copy `build-48-new-wine-old-bottles/` (short) or
  `build-41-counting-the-cost/` (30MB-cap build.py). Change: filenames, SEGMENTS text,
  BEATS list, the KJV set, and the two sacred-silence beat names. Nothing else.
- **ffmpeg is NOT on PATH on every machine.** A static build ships at
  `media-production/bin/ffmpeg` + `ffprobe`. In build.py set
  `FF/FPROBE = os.path.join(os.path.dirname(__file__),'..','bin','ffmpeg'|'ffprobe')`
  (absolute). For `gen_site_index.py` (which calls bare `ffprobe`), run it as
  `PATH="$(pwd)/bin:$PATH" python3 gen_site_index.py` from `media-production/`.
- **Caption box alpha = pick from the LIGHTEST frame.** Night videos: `boxcolor=black@0.5`.
  Bright daylight videos: `black@0.6` (else white/cream captions wash out on sunlit
  frames). Long narrator captions sit in the lower band; box stays translucent so the
  scene reads above it.
- 30MB cap numbers: `vcap = int(29.5*8000/total) - 96 - 20`; step CRF 20→24 until
  `size <= 29.5`. A 3–5 min video lands ~18–23MB at crf 20 — never starve the bitrate.
- Run build.py in the background and wait on the `DONE:` line; the `>>` command echoes are
  noise — `grep -v '^>>'` them.

---

## Git — routine multi-machine friction (don't panic)

- 4 machines push constantly. `git pull --rebase` will conflict on exactly two files:
  **`gen_site_index.py` (the TITLES dict)** and **`index.html`**.
  - TITLES: keep ALL machines' entries + yours (union the dict), drop the conflict markers.
  - index.html: it's generated — don't hand-merge; resolve `gen_site_index.py`, then
    **re-run `gen_site_index.py`** (all mp4s are on disk after the rebase) and `git add`
    the fresh index.html.
- If push is rejected: `git pull --rebase` then push again. If push says
  "could not read Username", the machine's GitHub token expired → tell Cameron to run
  `gh auth login` (only he can).
- A big binary branch (old mp4 history) can make a push time out; normal per-video
  commits (a dozen jpegs + one mp4) push fine.

---

## Where the tokens actually go — cut these

- **Browser screenshots** are the #1 cost. The JS query proves the image rendered, so you
  do NOT need a screenshot every step. Screenshot only when you must re-locate a moved UI
  control. QC by `Read`-ing the downloaded jpeg, not by screenshotting the canvas.
- Don't re-read big law files mid-build — read each once at the start.
- Type prompts as one line (retyping after a stray-newline submit wastes a full round-trip).
- Keep it to **one video per chat**; context past ~2 videos degrades quality — which is the
  whole reason for the rule.

## Dated lessons (append-only)

- 2026-07-15 (C): **Catalog can renumber mid-session.** If FACTORY-ORDERS shows a THE-200
  migration, your in-flight build's row number may change or the story may be dropped. A
  `git pull --rebase` will auto-rename tracked folders to the new number, but leftover
  `build-OLD-*` dirs (untracked pycache/assets, or committed PROMPTS) survive and will
  COLLIDE with the new row and get published under the wrong number by gen_site_index.
  Fix: after any renumber, `git rm`/`rm -rf` the orphan `build-OLD-*` folders before
  building the new row. Reconcile by story NAME, not row number (CONTENT-CARE's flag
  table lags the renumber too — trust the name).

## Homograph fix pattern (2026-07-15, from the #135 "bow" reject)
edge-tts reads homographs wrong ("bow" in Gen 9 came out like taking a bow).
Keep captions exact-KJV; steer ONLY the audio with a respelled TTS string:
```python
SPOKEN = {"jv13": "I do set my beau in the cloud"}   # TTS-only respelling
...
text_for_tts = SPOKEN.get(name, text)                # in the save loop
```
(build.py captions still read SEGMENTS text, so the screen stays true KJV.)
Ear-check list before assembly: bow, wound, wind, tears, lead, sow, live(s),
read, dove, bass, minute, use(d), close. Listen to any segment containing one.
- 2026-07-15 (D): **Windows: ffmpeg font path must have NO colon.** A `C:/Windows/Fonts/…ttf`
  path breaks ffmpeg's `-filter_complex` parser (`No option name near '/Windows/…'`) because
  `:` separates filter options. Copy the font to a colon-free RELATIVE path at build time
  (`_ensure_fonts()` → `serif.ttf`/`serif_italic.ttf`; gitignore them — Georgia is proprietary).
  Also: if no bundled `bin/ffmpeg`, install once with `winget install Gyan.FFmpeg` and resolve
  it via a winget-Packages glob. See build-135/161 build.py.
- 2026-07-15 (D): **Downloads only reach THIS disk from the LOCAL Windows Chrome.** The
  extension writes blob downloads to the *browser's* host — a remote/Linux browser (even one
  labelled isLocal on another machine) saves to that machine, not here. Verify once with a
  throwaway download + a REAL check (`find … && echo` ALWAYS prints — false positive; use
  `ls <path>` or a PowerShell time-filtered search). If the local Chrome drops out of
  `list_connected_browsers`, restart it from the shell (`Stop-Process chrome; chrome
  --restore-last-session <url>`) — that re-establishes the extension relay; then select it.
- 2026-07-15 (D): **Aspect resets to 16:9 every new project — set 9:16 + 1x explicitly and
  verify.** And never write "landscape" or "wide … painting" in a prompt: Nano Banana flips
  to 16:9 even with 9:16 selected. Say "one single tall upright vertical painting, one
  continuous scene". A 1376×768 still can't fill 9:16 and a blurred-bar reframe fails QC.
- 2026-07-15 (D): **Chrome throttles repeated auto-downloads.** A batch loop (one JS exec,
  sequential awaits ~900ms apart) lands many at once, but an extra single download afterward
  may silently fail. Fix: reload the Flow page (the first download after a fresh load is always
  allowed) and grab it first, or fire it from an on-page button click (a real user gesture).
- 2026-07-15 (D): **MEMBER verse-videos (rows 151–200):** copy build-161-called-of-god. The
  KJV *verse* is the centerpiece, read by the scripture voice (Christopher, cream italic,
  sacred silence); narrator gives modern meaning. Closing card carries a small one-line
  `GL_POINTER = "Learn more — Gospel Library: <Topic>"` (topic from THE-200 `→ GL:`). Christ
  may be referenced but never depicted — use a light/veil image and gate-safe "never shown".

## Lessons — Machine A, 2026-07-15 (append-only, newest at bottom)

- **Stage EXPLICIT files, never `git add -A` / `git add build-*`.** The wildcard sweeps in
  multi-MB `qc/*.png` scratch frames, and pushing them stalls/times out the push. Add only
  `PROMPTS.md build.py make_narration.py BUILD-STATUS.md the.mp4 assets/ audio/` + QUEUE +
  gen_site_index + index.html. (Supersedes the `git add -A` in step 10 above.)
- **Letterbox-panorama miss (distinct from stacked panels):** Nano Banana sometimes puts the
  subject in a thin central band with blurred sky+foreground, so it reads tiny in 9:16.
  Fix: reword "a wide view" → "an upright/vertical view filling the frame from base to
  crown," and reroll. (Hit on #42 s10 and #46 s3.)
- **Chrome extension can drop mid-session** (`list_connected_browsers` → `[]`). Only the
  operator can reopen Chrome + re-enable the extension. When it happens: commit WIP, write
  the resume point into the build folder / NEXT-SESSION-KICKOFF, hand off — don't burn turns
  retrying the connection.
- **Face-gate also trips on incidental Jesus tokens in non-staging lines:** "the mother of
  Jesus" in a character-lock or a shot where he isn't present → rename to "Mary the mother";
  and never write "face" in the same sentence as "Jesus" without a hiding cue/negation.

## Caption v2 + "live" (2026-07-15, Cameron's rejects)
- "live"/"lived" is the most common TTS misread (says /lyve/). Ear-check every
  segment containing live/lives/lived/liveth; fix with SPOKEN override "liv".
- Captions: copy chunk_caption()/caption_layers()/build_still() from
  build-48-new-wine-old-bottles/build.py (caption v2). Wide bottom strip, 2 lines
  max (3 KJV), chunks swap with the narration. Old builds get re-assembled with it
  in the remediation sweep — stills and most audio untouched, so it costs $0.

## flow_driver.py status (2026-07-15, Machine A session end — HONEST STATE)
Extension-free driver is ~90% working: login/profile/project ✅, settings+credit
check ✅, download logic ✅ (same JS as this playbook). STILL BROKEN: getting the
prompt text registered in Flow's prompt box (hidden-decoy textarea; contenteditable
targeting untested-in-anger). NEXT SESSION: give it a 15-MINUTE budget — try
coordinate click at the prompt bar (bottom-center) + page.keyboard.insert_text,
verify chars, submit via the arrow_forward button JS click. If still failing after
15 min, STOP — use the Claude-extension path (proven, this playbook) and move on.
Never let driver debugging block video production again.
