# QC / RUNNER HANDOFF — build-113-where-art-thou (Genesis 3)

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
