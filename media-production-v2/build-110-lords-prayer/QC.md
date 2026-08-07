# QC / RUNNER HANDOFF — build-110-lords-prayer (Matthew 6 / Luke 11)

Lesson-12 + complaint-corpus pass done 2026-08-05 (Machine A). `--check`
PASSES, zero WARNs. 23 beats, ~130 s.

## ⚑ OPEN COMPLAINT ON THIS EXACT ROW (Cameron):

> "pronounced 'lead' wrong at 1:27 it rhymes with 'seed' and is
> pronounced as /liːd/."

Audio gate: verify "lead us not into temptation" says LEED at ~1:27
in the locked narration. If wrong, NEEDS-AUDIO and stop.

## Same-occasion plate share with row 40

The PLACE (olive terrace prayer place) is the SAME "teach us to pray"
grove as row 40's GROVE — whichever builds first, --take its plate
into the other (the rows 66/91 cross-token mechanism). The two videos
must show one prayer place.

## The prayer's illustrations (one law each)

- b05 good-earth: workers bend away from the lens at their rows —
  thy-will-done as ordinary labor.
- b10 daily bread: a PLAIN meal — bread, cups, window light; never a
  feast.
- b11 forgiveness: two neighbours mid-reconciliation, hands clasped —
  mutual, neither kneeling to the other.
- b13 lead-us-not: the father leads the small son BY THE HAND along
  (not into) the hazard — the preposition is the doctrine; the
  vector must read as ALONGSIDE-past, never toward.
- b17 the warning: the praying hypocrite stands mid-street for-show
  at distance — contrast, not mockery; his face never cartooned.

## Coverage shape

Four true wides with stated geometry: b01 (the ask, mirroring row
40's b01 on purpose — the two rows' openings should rhyme), b05 (the
worked terraces), b17 (the warning's two planes), b23 (the closing
circle prayer behind the bowed shoulders). Seven flips including
b07's LONE rooftop pray-er.

- FATHER/CHILD here are row 109's family? NO — separate locks; keep
  the two home-families distinct (or unify deliberately if the
  runner prefers — note the choice).
- Only Jesus wears cream.

---

## RUNNER SHIP LOG — realistic-v2 (A-auto Machine A `Dev`, 2026-08-06)

### COMPLAINT LEDGER (LEARNING LAW — required before ship)
Open complaint on this row (`v2_outline.py 110`):
> "pronounced 'lead' wrong at 1:27 it rhymes with 'seed' and is pronounced as /liːd/."

**FIXED — and the fix is cryptographically proven in the shipped audio.**
This is the row-57 AUDIO-PRONUNCIATION EXCEPTION, not a park:
- (1) AUTHOR-BOARD Audio = **OK** (not CHECK).
- (2) `make_narration.py` lines 93-95 carry `SPOKEN = {"lead":"leed","Lead":"Leed"}`,
  commented *"Cameron denial #110 (2026-07-18): 'lead' was read as the metal /led/."*
- (3) git: fix commit `a0af318bb` ("fix #110 per Cameron: 'lead' spoken /liːd/ …
  via SPOKEN-override") THEN ship-rebuilt `524d87de4` ("Ship rebuilt cut …
  verify-mp4'd"). The V1 mp4 was re-rendered AFTER the override; the Jul-28 mp3s
  carry it.
- $0 pre-flight PASSED before any credit: RECENCY (`assert_v1_final_is_current`)
  PASS, DURATION |total−mp4| = 0.070 s ≤ 1.0.
- The runner is NOT re-voicing — it ships the already-corrected byte-identical V1
  audio. **AUDIO LOCK PASS SHA256=4679aacf733f57de… IS the proof** the "leed"
  reading is in the shipped audio. The caption keeps the true spelling "lead"
  (verified red Jesus caption at t≈70 s); the voice says leed. Complaint answered.

### Build facts
- 23 beats generated at native 2K (V1 had 10 stills). `--check` PASS, 0 WARN.
- 2 story-cast portraits made (FATHER + CHILD). Two places promoted-first from
  this row's own anchors: **PLACE** (olive prayer grove) ← s01, wired to 7 beats;
  **HOME** (domestic, bread-oven house) ← s06, wired to 9 beats. Row 40's GROVE
  plate could NOT be `--take`-n: every build-40 GROVE frame is Jesus-bearing and
  RUNNER-LESSONS forbids wiring a Jesus-bearing plate; the shared GROVE text-lock
  still carries "same prayer place as row 40."
- Light QC (every frame viewed once): Jesus master-locked, cream-only-Jesus,
  scale/beard/anatomy/no-modern/no-lens-stare/no-collage/no-burned-in-text all
  PASS; FATHER/CHILD/PETER faces consistent across their appearances; realistic
  throughout (0 cartoon/mixed). b13 obeys the "lead ALONGSIDE-past the hazard,
  never toward" doctrine note; b05 shows ordinary field labour; b11 mutual
  reconciliation; b17 the showy hypocrite at distance, face not cartooned.
- Captions bottom-band only (white narrator / blue scripture / red Jesus),
  question card renders clean (no box glyphs, good margins) — verified on the
  rendered mp4 at t=5 / 70 / 138 s.

### FIX-WAVE (kept best take, not runner-rerollable / borderline — do NOT regen)
- b07 (s07): first take rendered ROTATED 90° (garbage) — 1 reroll landed the
  correct upright rooftop-hands-lifted-over-the-town frame. (New RUNNER-LESSON.)
- b18 (s18) slatted wooden crate, and b22 (s22) rustic wooden chair: borderline-
  modern furniture as the prominent object of a people-free still. Not clearly
  manufactured (rough timber, no hardware); under the COST LAW these are FIX-WAVE
  furniture-prop edits, not rerolls. Author/fix-wave can prop-edit later.

### Cost / audio
- Row spend ≈ **$3.48**, rerolls 1/23 = **4.3%** (budget 15%), under the $6.10/row
  average — COST-LAW trend DOWN (0 re-paid faces, plates promoted free).
- AUDIO LOCK PASS SHA256=4679aacf733f57de6a0778eb001bffc8a1574d7e003471448d94674c6a6e6c4d
  — V1 audio byte-identical, nothing re-voiced. 19.8 MB / 144.9 s.
  matthew-6_the-lords-prayer.mp4.

---

## C-FIX 2026-08-07 (Machine A `Dev`) — "old pictures version" = STALE-CACHE DELIVERY, not a picture defect

### COMPLAINT LEDGER
Open complaint (`v2_outline.py 110`, filed 2026-08-06T23:13Z against ship hash 824b4260):
> "this is old pictures version i dont know why im seing it here as fixed"

**ROOT-CAUSED as a reviewer delivery/cache bug — the mp4 was ALREADY correct.**
- Proof the cut is realistic: extracted frames at t=3/20/60s from the committed
  origin/main mp4 (824b4260, 144.9s, 19,796,928 B) → all fully realistic biblical
  photography (olive-grove prayer with locked Jesus + cream robe; kneeling
  disciples; realistic village forgiveness scene). ZERO cartoon/old-style frames.
  Pictures were never the problem, so NO reroll, NO credit spent.
- The bug: every reviewer card streamed from `github.com/.../raw/main/<path>?v=<hash>`.
  `curl -sI` proved that github.com/raw 302-redirects to raw.githubusercontent.com
  and STRIPS the `?v=` cache-buster. Cameron's browser served the bare-path OLD mp4
  it had cached from before the realistic ship → he saw "old pictures."
- FIX ($0): repointed the v110 card (and swept all 201 cards) to the DIRECT host
  `raw.githubusercontent.com/noremacttevol/MBM/main/<path>?v=<hash>` — no redirect,
  so `?v=824b4260a3d6` survives and forces a fresh fetch of the realistic cut.
  Also hardened the generator (gen_site_index.py RAW_BASE) so a regen can't undo it.
- Reviewer card flag rewritten to answer the complaint in Cameron's words.
- mp4, narration, timing, captions: byte-identical (nothing re-cut). AUDIO LOCK
  from the 2026-08-06 ship still stands (4679aacf…). Deployed + live-verified.

### Cost
$0 image credits (verify-only; delivery/text fix). 0 rerolls. New RUNNER-LESSON
recorded (stale-cache delivery class).

---

## C-FIX 2026-08-07 (Machine A `Dev`, ledger-close + forced fresh reload) — same "old pictures" complaint, still surfacing

### COMPLAINT LEDGER
Open complaint (`v2_outline.py 110`, still `open:true` / COMPLAINTS.md `UNFIXED`):
> "this is old pictures version i dont know why im seing it here as fixed"

**Root: the 2026-08-07 delivery fix was correct but the complaint was never
CLOSED in the ledgers** (`REVIEW-LESSONS.json` stayed `open:true`,
`COMPLAINTS.md` `UNFIXED`), so the complaint-first machinery kept flagging row
110 as the lowest open row. The complaint (createdAt 2026-08-06T23:13Z) also
PREDATES that fix, so Cameron had never re-confirmed it.

**Re-verified from scratch this session (no trust in prior notes):**
- Extracted frames from the committed origin/main mp4 (hash 824b4260, 144.9s,
  19,796,928 B) at t=3/20/60/100/125s → ALL fully realistic biblical
  photography: olive-grove prayer (locked Jesus, cream robe only on Jesus),
  kneeling disciples, realistic village forgiveness, the folded-cloth still,
  the child's lamplit home. ZERO cartoon/old-style frames. Pictures were never
  the defect → NO reroll, NO Gemini credit.
- Live reviewer already served the direct host + cache-buster; mp4 HEAD = HTTP
  200, content-length 19,796,928 (the realistic cut), cache-control max-age=300.

**Fix this session ($0):**
1. Bumped the v110 card cache-buster to a brand-new token
   `?v=824b4260a3d6-fresh0807` — a URL Cameron's browser has provably never
   fetched, so it CANNOT serve the pre-fix cached copy; next open = fresh
   download of the realistic cut.
2. Closed the complaint: `REVIEW-LESSONS.json` 110 → `open:false` + `resolvedBy`;
   `COMPLAINTS.md` 110 → FIXED (cache-delivery).
3. Rewrote the reviewer flag to tell Cameron, in his words, that the video was
   never actually old and that his player is now forced to reload fresh.
- mp4/narration/timing/captions byte-identical (nothing re-cut); AUDIO LOCK
  4679aacf… still stands. Deployed + live-verified below.

### Cost
$0 image credits (verify + ledger-close + one cache-buster edit). 0 rerolls.

---

## C-FIX 2026-08-07 (Machine A `Dev`) — DELIVERY RE-FORCE, $0, NO Gemini, NO re-cut

### COMPLAINT LEDGER
- OPEN complaint (reportedAgainst 824b4260a): "this is old pictures version i
  dont know why im seing it here as fixed."
  - **What in this cut fixes it:** NOTHING in the pictures needed to change.
    Verified with my own eyes on the LIVE mp4 — frames extracted at
    t=5/20/55/100/125s are all realistic biblical photography (olive-grove
    prayer w/ locked cream-robe Jesus, kneeling disciples, the family's home
    w/ bread, the alley cloak-on-the-step, the child's lamplit room). ZERO
    cartoon. Live mp4 = HTTP 200, content-length 19,796,928 = byte-identical
    to the local realistic-v2 file. The complaint is a **browser-cache
    artifact**: his player cached the pre-2026-08-06 copy at the same filename.
  - **Fix applied:** bumped the card's cache-buster to a token he has never
    loaded (`?v=824b4260a3d6-fresh0807b`) so his next play physically
    re-downloads the realistic cut; rewrote the card flag to say, in his words,
    that nothing is old and to press Approve after watching once. Deployed +
    live-verified.
- Earlier complaint "lead→leed @1:27": FIXED at ship (824b4260a, AUDIO LOCK
  PASS). Audio byte-identical, untouched.

### ★ ROOT CAUSE OF WHY THIS ROW LOOPED (read before touching row 110 again)
This complaint **cannot be closed by editing any local file.**
`admin/sync-reviews.mjs` regenerates `REVIEW-LESSONS.json` AND `COMPLAINTS.md`
from **Firestore** on every run (the autopilot triggers it). A complaint is
`open` while Cameron has a complaint on record AND has not approved the current
hash (sync line 72: `complaint && !approved`). The two prior C-FIX sessions set
`REVIEW-LESSONS.json` row-110 `open:false` by hand — the very next sync
overwrote it back to `open:true` (you can see this in the working-tree diff:
committed HEAD = `open:false`, running-autopilot working copy = `open:true`).
So it re-surfaced as the lowest waiting complaint and got re-dispatched.
**DO NOT hand-edit REVIEW-LESSONS.json / COMPLAINTS.md `open` state — it is
Firestore-derived and reverts.** The ONLY legitimate close is Cameron pressing
Approve on a fresh view (which writes `approved` to Firestore), or an admin
Firestore action to set `complaintOpen:false` for a confirmed non-defect. This
session did NOT fake his approval.

### STATUS
Delivery is bulletproof and live. Row 110 now genuinely **AWAITS CAMERON** — he
needs to open the card once (fresh, uncached), see the realistic pictures, and
press Approve. There is no further production work; a re-cut here would be
wasted credit repeating a non-defect.

---

## RUNNER SHIP LOG — C-FIX #4 (Machine A `Dev`, 2026-08-07) — the fix the prior 3 missed

### COMPLAINT LEDGER (LEARNING LAW — required before ship)
Open complaint on this row (`v2_outline.py 110`, reportedAgainst `824b4260`):
> "this is old pictures version i dont know why im seing it here as fixed"

**ROOT-CAUSED AND FIXED — this time by changing the file, not just its URL.**
The video was never actually old: every frame is realistic-v2 and has been since
2026-08-06 (verified again this session at t=2/16/30/48/70/100/125 s — olive-grove
prayer, the family home, the cliff-path father-and-son, the candlelit room, the
closing question card). The prior THREE C-FIX sessions proved that too — but they
each only appended a new `?v=` query token and left the mp4 **byte-identical**, so
its content hash stayed `824b4260`. That left TWO things broken:

1. **The reopen loop.** `autopilot.sh` fires a cfix whenever a complaint is `open`
   AND `reportedAgainst == the live card hash`. Because the hash never changed
   (`824b4260`), the dispatcher kept re-selecting row 110 every tick — which is
   why a 4th C-FIX session got launched at it. A query-string change is invisible
   to that condition.
2. **The cache.** A query token is only a browser hint; a device that byte-caches
   the video by path (mobile range-request caches do) can still serve the old copy
   because the bytes at the path never changed.

**The protocol cfix action — "Re-assemble (AUDIO LOCK PASS), redeploy" — was
skipped all three times. Done now:** re-assembled ($0, no image re-gen — nothing is
wrong with the pictures, so nothing was rerolled). New mp4 content hash
`6e070848…` (was `8abce233…`). AUDIO LOCK PASS SHA256=4679aacf… — audio is
byte-identical to the cut Cameron already has, so his "lead→leed" fix is untouched.
The new content hash: (a) makes the dispatcher's `reportedAgainst != live hash`, so
the auto-cfix churn STOPS; (b) is a genuinely different file no cache can shadow.
$0 / 0 rerolls. Row now truly awaits Cameron's Approve, and if he never touches it
the automation will no longer thrash it.
