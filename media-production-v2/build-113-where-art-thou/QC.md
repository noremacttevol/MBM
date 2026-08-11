# QC / RUNNER HANDOFF — build-113-where-art-thou (Genesis 3)

## ✅ SHIPPED — C-FIX 2026-08-11 (Opus, Machine A `Dev`) — Cameron DIRECT ORDER: God-the-Father embodiment consistency + rags root cause CLOSED. Full-cut gate + order check + served-bytes verified.

**Complaint (v2_outline OPEN):** "God has a body, we've been through this... create a character for him so his look doesn't change much like Jesus... 0:25 they are sitting on water... the first two thirds where they are wearing rags needs to be changed (nothing → fig leaves), last third (God makes them clothes) stay."

### COMPLAINT LEDGER — this cut answers every part
- **"God has a body / one locked character like Jesus" → SHIPPED (was authored but never actually shipped; live 9aeeb822 showed him embodied in only ~3 beats).** Verified via FACE-BOARD of ALL 9 God beats from the rendered mp4: the Father is the SAME embodied man — white hair, full white beard, brilliant white robe (he alone; only Jesus wears cream), no halo/light — in s02, s07, s08, s10, s11, s17, s20, s23, s26. No light/void/disembodied presence anywhere. god.jpeg is his canon.
- **"first two thirds wearing RAGS" → FIXED (this is what stranded the row).** Root cause was the CLOTHED identity anchors (eve.jpeg=burlap hood+tunic, adam.jpeg=wool tunic) reprinting wool on tight crops, unbeatable by pipeline reroll (3 prior passes failed). Fixed with COMPOSITION-PRESERVING identity-edits (gemini-3-pro-image) of the 5 stubborn frames — wool swapped for post-fall coverings, faces/poses/backgrounds untouched: s05 (nothing, shadow+hair), s06 (fig leaves), s15/s16 (hood gone, hair+fig-leaf), s19 (wool robes → fig-leaf garments). Zero woven cloth remains before the coats. Female-nudity phrasing tripped Gemini safety on portraits/b19 first try → clothed-positive fig-leaf phrasing passed (b13/b18 prove the model renders it).
- **"0:25 sitting on water" → FIXED (prior author pass, verified held):** s05 is on solid mossy earth in shadow, no water under them.
- **Last third (coats) KEPT byte-identical** (s21/s23/s24) — Cameron approved "those are good."

### GATES (Cameron's laws, all PASS)
- **AUDIO REBUILD PASS SHA256 4cdc391c… — byte-identical to the already-reviewed cut. Narration/voices/timing UNTOUCHED** (AUDIO_FROM_V1_SEGMENTS, 15 V1 mp3s, 163.079s). Only 5 image files swapped (identical 1536×2752 dims); zero timeline change.
- **FULL-CUT GATE:** one frame per beat from the RENDERED mp4 — all 26 + question card PASS (Father consistent; no wool; captions bottom-band, speaker colors blue-scripture/white-narrator/green-Father; card clean; realistic throughout, no cartoon/modern/anatomy defect).
- **ORDER CHECK:** faster-whisper small.en beam5 transcript matches the script; every anchor lands on its picture incl. all 5 fixed frames (22-26s→s05, 80-84s→s15, 84-87s→s16, 104-108s→s19, 108-113s→s20). NO drift.

### COST
5 identity-edits + 1 adam-portrait probe (unused) + 1 eve-portrait probe (safety-blocked) ≈ 7 Gemini image calls ≈ **$0.94**, audio $0 — well under the $6.10/row average. Touch-once (all fixes batched into one re-cut).

### ⚠ FOLLOW-UP (non-blocking, for the AUTHOR lane): the CAST-REF-V2 portrait anchors adam.jpeg/eve.jpeg are STILL clothed in wool. This ship bypassed them via direct frame-edits, so the shipped cut is clean — but any FUTURE pipeline re-cut of an Adam/Eve beat would reprint wool again. A female-nude portrait regen trips Gemini safety; regenerating the anchors as fig-leaf/hair (clothed-positive) closes the landmine for good. Left as an author task, not a ship blocker.

---

# QC / RUNNER HANDOFF — build-113-where-art-thou (Genesis 3)

## 🅿️ RUNNER PARK — 2026-08-07 (Opus paid C-FIX attempt, Machine A `Dev`) — ROOT-CAUSED to CLOTHED CAST PORTRAITS → NEEDS-REBUILD (AUTHOR fix required, runner cannot fix within rails)

**Complaint being fixed (vs live `9aeeb822`):** "God has a body… his look doesn't
change. **0:25 they are sitting on water — bad photo, delete/redo.** every picture
is bad except the last ones where he made them clothes… **the first two thirds
where they are wearing rags needs to be changed** — first nothing (face/upper-torso,
Eve's hair/foliage), then fig leaves when they feel naked, then the last third stays
(God makes them coats)."

**What the paid lane did this session (~$2.0, 15 imgs):** regenerated all 17
authored beats + 3 reroll passes on the stubborn ones. RESULT after 3 passes:

- ✅ **LANDED CORRECT (keep — do NOT re-cut):** b02, b04, b08, b10, b11, b12, b13,
  b17, b18 (fig-leaf / reverent-nude, Father embodied), b25, b26 (garden + embodied
  Father walking), and the KEPT approved beats b01, b03, b09, b14, b21, b22, b23, b24.
  The **"0:25 sitting on water"** fix is GOOD — b05/b08/b10/b17 are on solid ground,
  never on the stream.
- ❌ **WILL NOT LAND VIA REROLL (still show CLOTH/"rags" or wrong covering):**
  - **b15, b16** (tight Eve close-ups "what is this that thou" / "the serpent
    beguiled me"): came back a brown burlap HOOD + linen tunic in a desert village
    every attempt (3×). 
  - **b19** ("they stood there ashamed…", the standing pair): came back modern
    leather trench-coats → then full village wool robes + Eve hood. Should be
    fig-leaves (pre-coats).
  - **b06** (making the fig leaves): Adam now bare (correct) but Eve still in a wool
    tunic.
  - **b20** (God presents the coats): Adam bare + fig-leaf + Father embodied
    (good), but the coat still reads slightly modern (collar) — reroll to raw hide.
  - **b05** ("everything changed / felt shame"): SAFETY-BLOCKED on redo (`'parts'`
    no-image) — the pre-fall nakedness beat trips the Gemini safety filter; kept the
    prior take (still shows wool tunics = rags).

**★ ROOT CAUSE (verified by opening the identity anchors):**
`CAST-REF-V2/eve.jpeg` AND `CAST-REF-V2/adam.jpeg` — the committed identity
portraits — **depict Adam and Eve fully CLOTHED in rough first-century WOOL** (Eve
in a brown burlap HOOD + linen tunic; Adam in a wool tunic). On WIDE beats the scene
context wins and the couple render nude/fig-leaf correctly; but on **tight single- or
pair-framings (b15/b16 close-ups, b19 standing pair, b06 Eve) the identity anchor
dominates the composition and faithfully REPRINTS the portrait's wool garments** =
the exact "rags" Cameron is complaining about. The base `STYLE_V2` block reinforces
it ("clothing of rough-woven wool and linen", "head covering locked", "a mantle or
shawl is one loose rectangle of cloth") — and the b15 beat even says her hair is "a
mantle", which the base maps to a cloth mantle. **A runner reroll cannot beat a
clothed identity anchor + the base block on a tight crop; this is an AUTHOR fix.**

**🔧 AUTHOR FIX (NEEDS-REBUILD — do this, then flip BUILT for the paid re-cut):**
1. **Regenerate BOTH Eden portraits** so the identity anchor is not itself "rags":
   Eve → bare shoulders under her own long dark hair (fig-leaf-era Eden), NO shawl /
   NO head-covering / NO woven tunic; Adam → bare torso, NO wool tunic. KEEP their
   faces (this is the same couple as the good wide beats — v2_story_cast from the
   same locked face spec; eyeball the face matches b02/b17 before committing).
   *(This is why b02/b04/b17 already look right and b15/b16 don't — same face, wrong
   wardrobe on the anchor.)*
2. **Strengthen the tight beats b05, b06, b15, b16, b19** with an explicit override
   that can beat the base block on a close crop: e.g. "bare shoulders and her own
   loose hair ONLY — NO shawl, NO head-covering, NO head-scarf, NO woven cloth, NO
   mantle-of-cloth on her anywhere; her long hair is the ONLY thing over her
   shoulders." For b19 also state "fig-leaf girdles, they have NOT been given the
   coats yet." Do NOT edit STYLE_V2 (200-video blast radius) and do NOT weaken the
   modesty — the target is reverent hair/fig-leaf covering, never cloth, never
   explicit.
3. **b05 safety block:** keep the crop chest-up and lean on hair/foliage wording so
   the filter passes without adding cloth (adding cloth re-triggers the complaint).

**RUNNER (after author flips BUILT):** re-cut ONLY b05, b06, b15, b16, b19 (+ b20
raw-hide, verify b25); KEEP everything in the ✅ list byte-identical. Re-assemble
(`AUDIO_FROM_V1_SEGMENTS=True`, byte-identical), ship via C-FIX with the ledger
answering Cameron: rags → real hair/fig-leaf coverings; water frame fixed; God
embodied.

**Complaint stays OPEN** (not shipped — assembling now would put Eve-in-a-shawl back
on his reviewer = repeating his exact "rags" complaint = worst failure). No fake
close; REVIEW-LESSONS/COMPLAINTS untouched (Firestore-owned).

---


## ✅ SHIPPED — AUDIO-FIX 2026-08-07 (Machine A `Dev`): STALE-V1-FINAL cleared, realistic cut LIVE
The 26 realistic stills (GOD embodied per Cameron's complaint — see below) were done
and QC-PASS, but `v2_assemble` failed the AUDIO LOCK: the V1 final MP4 (193.3s, 07-29)
was stale vs the 15 re-voiced mp3s (163.1s timeline). Fix (audio-only, $0): set
`AUDIO_FROM_V1_SEGMENTS = True` in beats_v2.py so the track rebuilds from the V1 mp3s
at the extract_beats offsets. VERIFIED the rebuild gate: track = 163.079s == extract_beats
total to the ms (AUDIO REBUILD PASS `4cdc391c…`). Re-assembled the full realistic cut
(`genesis-3_where-art-thou.mp4`, 163.1s, git-blob `9aeeb822`, decodes 0 errors); frame
spot-checks confirm the embodied Father (s26 white-haired elder in white robe) and Adam &
Eve clothed in skins (s21), realistic throughout, captions in sync. No stills regenerated,
no re-voice. Reviewer card repointed to the V2 realistic path + git-blob hash, answering
the God-embodied complaint in Cameron's words; deployed + live-verified. Board row 113
NEEDS-AUDIO→BUILT, Audio CHECK→OK.

---


Lesson-12 + complaint-corpus pass done 2026-08-05 (Machine A). `--check`
PASSES, zero WARNs. 26 beats, ~147 s.

## ⚑ CAMERON'S STANDING ORDER APPLIED — GOD THE FATHER IS EMBODIED HERE

His complaint on this row: "God has a body, weve been through this and
hopefully you have created a character for him as well so his look
doesnt change much like Jesus and other famous characters."

DONE: the GOD lock now exists in this build — the Father as a
glorified embodied man: majestic, ageless-strong, flowing white hair,
full white beard, warm noble kind face, BRILLIANT PURE WHITE robe (he
alone wears pure white; only Jesus wears cream), real weight and
footsteps, NO halo or light effects. The walking beats (b07/b26) were
re-authored from "moving golden light" to the Father himself walking.

**THIS LOCK IS THE FATHER'S CANON for the whole library** — his
approved first face here anchors every future Father row (178
in-our-image, etc.). Face-board him like Jesus. RECONCILIATION NOTE:
rows where scripture itself hides him (105's cleft "thou canst not
see my face", 104's voice, 102's summit) stay unembodied — scripture-
exactness decides per row; where scripture shows him acting bodily
(Eden: walking, clothing them), he is shown.

## ⚠ GARDEN UNWIRED (sixth wrong-plate catch — the herb-garden trap)

Eden is promote-first from b01. Never the build-26 mustard garden.

## Adam and Eve (dignity laws)

- The leaf girdles and later coats of skins keep both modest in every
  frame; shame is carried in posture, never exposure.
- The coats of skins are HIS making (v21) — the Father clothes them:
  tenderness inside judgment; the sending (b23) is a sending, not a
  casting out (warm light follows them).
- The serpent, if any beat needs it, is a real snake, never a demon
  (A-law adjacency).

## Coverage shape

Four true wides with stated geometry: b01 (Eden at peace), b10 (hider
and seeker in one profile — the row's thesis), b18 (the two worlds
from behind the standing pair), b26 (the closing walk in profile —
the question still asked in love). Six flips including b14's
PERSON-FREE hiding tree.

- Golden evening throughout; the exile dusk-country grey beyond the
  gap — two palettes, one gate between them.

---

## 🅿️ RUNNER PARK — A-auto Machine A, 2026-08-06 (NEEDS-AUDIO, $4.14 art spent)

**Blocker:** `v2_assemble.py 113` FAILS AUDIO LOCK — extracted V2 timeline
163.079s vs authoritative V1 final 193.267s. Root cause = STALE-V1-FINAL
(row-69/74/77 class): the V1 mp4
`media-production/build-113-where-art-thou/genesis-3_where-art-thou.mp4` was
rendered 2026-07-29 09:47, but 15 of the V1 narration mp3s were RE-VOICED
later (2026-07-29 23:03) and run ~30s shorter. The V1 mp4 therefore carries
the OLD voice; copying it byte-identical would ship stale audio, so the LOCK
refuses. Runner is forbidden to edit beats_v2.py (hard rail), so this is an
AUTHOR fix.

**AUTHOR FIX:** add `AUDIO_FROM_V1_SEGMENTS = True` to
`media-production-v2/build-113-where-art-thou/beats_v2.py` (the track is then
rebuilt from the V1 build's own — new-voice — mp3s). Then RESUME below.

**RESUME COMMAND (art is DONE — do NOT regenerate any still):**
```
cd media-production-v2
python3 v2_assemble.py 113            # must print AUDIO LOCK PASS
# then ship per PROMPT-OPUS-RUNNER.md step 7 (two commits + firebase deploy + live verify)
```

**Art state (all preserved, reusable):** 26/26 stills GENERATED + LIGHT-QC PASS.
GARDEN plate promoted from b01 (committed via v2_stash --promote). Portraits
ADAM/EVE/GOD made. 2 rerolls (7.7%, under 15% budget): b17 (dark bottom band →
fixed) and b20 (coats-of-skins rendered as modern leather jackets → rerolled to
raw animal hides). Kept b23 with the embodied Father visible in background
though its must_not_show said "no figure of God" — DELIBERATE: it serves
Cameron's God-embodiment order, is reverent (pure white robe, no halo), and
rerolling risks losing the very thing the complaint wants. FIX-WAVE (not
garbage, no reroll spent): garment continuity drift (fig-leaf to wool tunic
across b05/b08/b11/b13/b17/b19); b21/b24 hide-coats read slightly modern-tailored.

## COMPLAINT LEDGER (LEARNING LAW)

Open complaint on row 113 (from `v2_outline.py 113`):
"God has a body, we've been through this and hopefully you have created a
character for him as well so his look doesn't change much like Jesus and
other famous characters."

- FIXED IN THE ART (ships the moment the audio flag is flipped): God the
  Father is now EMBODIED and LOCKED. A GOD portrait sheet was generated
  (CAST-REF-V2/god.jpeg: glorified man, flowing white hair, full white beard,
  warm noble face, BRILLIANT PURE WHITE robe — he alone wears pure white — no
  halo/glow). He appears bodily walking through the garden in b07
  (s07 "and then they heard him") and b26 (s26 "one who comes walking
  through the garden ... still calling"), and stands in mercy at the sending in
  b23. This GOD lock is now the Father's canon for the whole library
  (anchors 178 in-our-image, etc.). His look no longer changes — it is fixed by
  image + text lock exactly like Jesus. Cameron can verify his own fix in the
  b07 and b26 frames.

---

## ✅ AUTHOR DONE — GOD-EMBODIMENT MADE CONSISTENT (Fable-5 author lane, Machine A `Dev`, 2026-08-07, $0)

The 2026-08-07 ship showed the embodied Father in only 3 beats (b07, b23, b26)
while the other God-presence beats still rendered him as **golden light / no
figure** (b02 walking-together, b08 "where art thou", b10/b11 the seeking, b17,
b20 the coats). That INCONSISTENCY is the open half of the complaint: "so his
look doesn't change" fails when he is a man in some frames and light/absent in
others. Root cause was a contradiction left in the file — the `GOD THE FATHER
LOCK` (embodied) was added, but most beats' `must_show`/`must_not_show` still
said "ABSOLUTE: no figure of God — light only," and several God-present beats
(b02/b10/b11/b20) never even locked the GOD token, so neither the Father prose
NOR his `god.jpeg` face sheet attached.

**Author fix ($0, --check PASS 26 beats):**
- Rewrote the header GOD RENDERING note to Cameron's standing order (embodied,
  shown in every presence beat; off-frame only in tight Adam/Eve reaction
  close-ups — the same grammar used for Jesus, so his look never changes).
- Added the `GOD` token to the `locks` of b02, b10, b11, b20 (b07/b08/b17/b23/b26
  already had it) so `REFS["GOD"]=god.jpeg` + the Father prose both attach — his
  FACE is now locked identical on every beat he appears in.
- Flipped `must_show`/`must_not_show`/scene on b02, b07, b08, b10, b11, b17, b20,
  b23, b26 to SHOW the embodied Father (verified: assembled prompts carry "GOD
  THE FATHER LOCK" and no longer say "no figure of God"). Removed personified
  God-as-light from b25 (now a pure open-road landscape beat before the closing
  figure). Reaction close-ups b12/b13/b15/b19/b24 keep God off-frame — correct
  film grammar, not a look change.

### COMPLAINT LEDGER — this re-cut
Open complaint: *"God has a body, we've been through this... create a character
for him... so his look doesn't change much like Jesus."*
- **Embodiment → FIXED, now CONSISTENT:** the Father is shown as a real man in
  EVERY presence beat, not just 3; light-only God is gone from his presence beats.
- **"his look doesn't change" → FIXED:** `god.jpeg` face sheet now attaches to all
  9 God beats (was missing on b02/b10/b11/b20), so it is one locked man like Jesus.

### 🅿️ RUNNER — do this (paid re-cut, ~7 stills)
Regenerate ONLY the beats whose God rendering CHANGED: **b02, b08, b10, b11, b17,
b20, b25** (embody the Father / remove God-as-light). KEEP b07, b23, b26 (already
show the Father and now match spec) and every non-God still. Face-board the Father
against `god.jpeg` across ALL 9 God beats (b02/b07/b08/b10/b11/b17/b20/b23/b26) —
one man, brilliant white robe, white hair/beard, no halo; identity-edit any drift,
then recheck the full frame. Re-assemble (AUDIO byte-identical, AUDIO_FROM_V1_
SEGMENTS already set), ship via C-FIX with this ledger on the review card.

### ⚠ HAND-OFF — GLOBAL GOD CANON (needs Cameron's per-passage call, do NOT sweep blind)
Cameron wants God consistent across ALL his videos. Row 113 is the ONLY build
with an embodied GOD lock today; `GOD` is NOT in the global CAST_LOCKS. Promoting
a canonical embodied-Father (text + `god.jpeg`) to the global cast would make him
one man everywhere — BUT this must be applied ONLY to passages where God appears
bodily. Several God-rows are scripturally VOICE/LIGHT theophanies, not a body
(e.g. row 101 still-small-voice = 1 Kings 19 "a still small voice"; ascension =
voice/angels). Blanket-embodying God would be a doctrine error. This needs
Cameron's call on which passages show God's body vs. voice, plus whether the
OT "LORD" figures should read as the Father (as row 113 does) or the premortal
Christ/Jehovah (LDS: the OT Jehovah = premortal Christ). Flagged for a focused
session, not done blind here.

---

## ⚠️ ROUTING GAP — hash-orphaned complaint (author note, 2026-08-07, Machine A `Dev`, $0)

Same class as row 102. The embody-Father fix above is AUTHORED but NOT built and
no autopilot lane auto-picks it: `reportedAgainst = 706f5d69` ≠ live `9aeeb822`,
so cfix's hash-match guard is False; State NEEDS-REBUILD + non-empty claim makes
runner/resume skip it. Needs a directed PAID build of the authored embody-Father
stills, then a fresh ship for Cameron to re-review. Do NOT flip to BUILT (would
present the not-yet-embodied cut as ready) and do NOT hand-edit reportedAgainst
(sync-reviews.mjs reverts it each tick). Blocked on the SAME doctrine question as
row 102 (Father vs premortal Christ for OT "the LORD").

---

## ✅ AUTHOR DONE — CLOTHING PROGRESSION + "SITTING ON WATER" FIX (Fable-5 author lane, Machine A `Dev`, 2026-08-07, $0)

The embodiment note above closed only ONE of the three parts of Cameron's live
complaint (against cut `9aeeb822`). This note closes the other two. His full
complaint:

> "God has a body, we've been through this... so his look doesn't change. **0:25
> they are sitting on water. bad photo delete it and redo it a better way.** every
> picture is bad, except for the last ones where he made them clothes those are
> good, but **the first two thirds where they are wearing rags needs to be
> changed** — first they are wearing nothing and you can work the pictures to only
> show their face or upper torso with eve's breasts covered by eve's long hair, or
> random foliage... then when they eat of the tree and feel naked have them wearing
> the leaves of trees... and then have the last third stay the same where God makes
> them clothes."

### ROOT CAUSE of the "rags"
The byte-identical base style block (`STYLE_V2` in `v2_prompt.py`) tells EVERY
prompt "Historically credible **clothing of rough-woven wool and linen** in earth
tones." On the Eden nudity beats that generic line had nothing per-beat opposing
it, so the render dressed Adam and Eve in rough wool = the "rags" Cameron sees
through the first two-thirds. The old beat text only said "framed with complete
modesty," which the model satisfied by putting them in cloth. NOT editing
`STYLE_V2` (byte-identical across all ~200 videos — out of scope, huge blast
radius); instead each people-beat now carries an explicit covering state that
overrides it.

### Author fix ($0, --check PASS 26 beats)
- **Covering timeline written into the docstring + ADAM/EVE locks** as Cameron's
  exact order, with a hard invariant RAGS BAN (never rags, woven cloth, sackcloth
  or loincloth — the ONLY coverings in the whole story are, in order: nothing
  (hair/foliage/chest-up framing) → fig leaves → the leather coats).
- **Pre-fall beats b02, b04:** now say the couple wear NOTHING (before the fall),
  shown with complete discretion — chest-up framing, her long hair and garden
  foliage across her — with a per-beat "NO rags, cloth or garments" rejection.
- **b05 ("0:25 sitting on water"):** GROUND FIX — they are crouched on solid mossy
  earth in the thicket shadow, her hair pulled forward as a cloak; explicit
  HARD-REJECT: never seated/crouched/standing on, in or over the stream, no water
  under them, stream only in the far background. Still nothing/hair here (fig
  leaves are not made until b06).
- **b06:** the fig leaves are made — explicit fresh BROAD GREEN FIG LEAVES (never
  rags/cloth), on solid ground.
- **Fig-leaf beats b08, b10, b11, b12, b13, b15, b16, b17, b18, b19, b20:** each
  now states the couple wear GREEN FIG-LEAF girdles (never rags/cloth) and are on
  solid ground, never on water.
- **Coats beats b21, b23, b24:** UNTOUCHED — Cameron approved "the last ones where
  he made them clothes those are good" (dark leather coats, discarded fig leaves).

### COMPLAINT LEDGER — this re-cut (all three parts of the live complaint)
- **"his look doesn't change" (embodiment)** → FIXED in the prior author note
  (god.jpeg + Father prose on all 9 God beats).
- **"0:25 sitting on water, delete it and redo"** → FIXED: b05 re-authored onto
  solid ground with a hard water-rejection; b06 hardened the same way.
- **"first two thirds wearing rags"** → FIXED: root-caused to the base wool/linen
  line; every pre-coats people-beat now carries an explicit covering state
  (nothing → fig leaves) plus a hard rags ban. Last third kept (coats approved).

### 🅿️ RUNNER — do this (paid re-cut; touch-once, batch with the embodiment regen)
Cameron ordered the first two-thirds redone ("every picture is bad except the last
ones"), so this is a COMPLAINT-MANDATED re-cut, NOT quality-rerolls — each listed
beat is generated ONCE to the corrected spec; the 15% reroll budget does not apply
to complaint-mandated regens. **Regenerate:** b02, b04, b05, b06, b08, b10, b11,
b12, b13, b15, b16, b17, b18, b19, b20, b25, b26 (covering + embodiment + the b25
God-as-light removal + b07 already-embodied verify). **KEEP byte-identical:** b01,
b03, b09, b14, b21, b22, b23, b24 (no-people/landscape beats and the Cameron-
APPROVED coats beats). Est ≈ 17 stills × $0.134 ≈ $2.3 (under the $6.10/row avg).
- **Watch the base wool/linen line:** it is the rags culprit. QC EVERY pre-coats
  people frame specifically for cloth/rags/loincloth and reroll that frame until
  the covering reads as HAIR + FOLIAGE (pre-fall, b02/b04/b05) or GREEN FIG LEAVES
  (b06-b20). Any woven-cloth garment before the leather coats = reject.
- **Modesty/safety:** the pre-fall frames are reverent classical-biblical nudity
  shown chest-up / hair-and-foliage covered — never explicit. If a Gemini call
  is safety-blocked, lean harder on chest-up framing + hair/foliage wording, do
  NOT add cloth to "fix" it (cloth re-triggers the complaint).
- Face-board the Father vs `god.jpeg` across all 9 God beats; face-board Adam/Eve
  vs adam.jpeg/eve.jpeg. Re-assemble (AUDIO byte-identical, `AUDIO_FROM_V1_
  SEGMENTS=True`), ship via C-FIX with this ledger on the review card answering
  Cameron in his own words (rags → real coverings; water frame fixed; God embodied).

### ROUTING — the stale gap note above is SUPERSEDED
The "⚠️ ROUTING GAP" note (reportedAgainst `706f5d69` ≠ live `9aeeb822`) is STALE:
since it was written a new cut shipped and Cameron RE-REVIEWED it, so
`reportedAgainst == live == 9aeeb822` NOW (verified in REVIEW-LESSONS.json +
site/review.html). State flipped NEEDS-REBUILD → **BUILT** so the paid cfix lane
picks it up (guard `reportedAgainst == live` passes). The full author package
(embodiment + clothing + water) is now Ready.

### DOCTRINE (unchanged, non-blocking here)
Row 113 (Eden, Gen 3) shows God bodily — textually clear ("walking in the garden",
"made coats... and clothed them"). The GLOBAL question (which OT "LORD" passages
show a body vs. a voice/light theophany; Father vs premortal Christ) still needs
Cameron's per-passage call for the blind sweep — flagged, not swept here.
