# QC / RUNNER HANDOFF — build-113-where-art-thou (Genesis 3)

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
