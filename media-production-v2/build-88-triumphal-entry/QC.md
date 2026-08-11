# QC / RUNNER HANDOFF — build-88-triumphal-entry (Matthew 21:1-11)

## ✅ AUDIO FIX DONE — STALE-V1-FINAL lock cleared, HANDED TO PICTURE RUNNER (2026-08-06, Machine A `Dev`, headless AUDIO-FIX lane)

Class = STALE-V1-FINAL, BOTH tripwires, no open Cameron complaint (`v2_outline.py 88`).
Parked on the AUDIO LOCK: timeline 118.564s vs V1 mp4 117.100s (|Δ|=1.464s) AND all 15
mp3s newer than the V1 mp4. Fix ($0, no new TTS): set `AUDIO_FROM_V1_SEGMENTS = True` in
beats_v2.py so the assembler rebuilds from this build's own 15 mp3 segments (present in the
V1 audio/ dir) instead of copying the stale V1 mp4 AAC. 0 V2 stills → per PROMPT-AUDIO-FIX.md
step 6, ship nothing visual: board → AUTHORED / Audio OK / Ready ✅, claim cleared, picture
runner assembles on the corrected audio. No Gemini spend.

Lesson-12 + complaint-corpus pass done 2026-08-05 (Machine A). `--check`
PASSES, zero WARNs. 20 beats, ~112 s.

## Same occasion as row 83 — different stagings on purpose

Row 83 owns the OVERLOOK vista (the weeping); this row lives at crowd
level: Bethphage lane, the branch-strewn road, the gate. Do not
introduce panorama compositions here — if a render looks like row 83's
valley view, it missed this row's staging. Row 83's approved OVERLOOK
frame may still seed this row's distant-city glimpses if any.

## Coverage shape

Five true wides with stated geometry: b01 (the sending in profile),
b11 (the carpeting — camera low behind the colt's advance), b13 (the
hosanna flood — rider and river of branches in profile), b16 (the
gate — camera INSIDE the city behind the turning heads), b20 (the
closing — meek rider amid it all, in profile). Eight flips.

## THE COLT (the animal laws)

- TWO animals: grey MOTHER DONKEY + darker grey COLT (count law); the
  COLT is ridden, the mother led alongside. If any frame swaps which
  animal carries him, reject (scripture-exactness).
- The colt is SMALL and never-ridden — Jesus on it reads humble-low,
  feet near the ground: meekness as geometry (and the no-giant gate
  matters doubly on a small mount).
- Handled gently in every frame; cloaks-as-saddle (garments, not
  tack — row-7 class: no leather saddle, no bridle hardware).

## Other checks

- The carpeting is CLOAKS + CUT BRANCHES on the road — both visible,
  the road transformed frame by frame (bare → strewn: one direction).
- Direction (row-83's law on its sibling row): the whole procession
  descends TOWARD the in-frame gate/city; nobody walks against it.
- The crowd is joyful, never mob-like; "WHO IS THIS?" plays on
  city faces at windows (b15) vs the procession's answer (b19).
- TWO disciples on the errand (count law) — same two men through
  b01-b07.
- ROAD wired from build-38. COLT is an animal lock — no plate; LANE
  promote-first from b03's lane frame if needed.
- Only Jesus wears cream.


## ✅ PICTURE RUNNER — BUILT (A-auto Machine A `Dev`, 2026-08-07, Opus runner) — 20 stills, 0 rerolls

Audio fix confirmed live before spending: `grep AUDIO_FROM_V1_SEGMENTS beats_v2.py` = **True**
(assembler rebuilds narration from this build's own 15 V1-dir mp3 segments at the timeline
offsets — nothing re-voiced). `v2_prompt.py --check` PASS, zero WARNs. No open Cameron
complaint (`v2_outline.py 88` shows none).

**COMPLAINT LEDGER: none open.** (Row 88 has no filed Cameron complaint; the AUDIO-FIX
lane's STALE-V1-FINAL park was mechanical, not a Cameron complaint, and is resolved by the
`AUDIO_FROM_V1_SEGMENTS=True` flag — proven at ship by AUDIO LOCK PASS.)

**Generation:** `v2_gen_api.py --ceiling 497`, 20/20 stills at native 2K, $2.68 this run,
meter $467.79 → $470.47. Places LANE + ROAD wired from build-38 plates (PLACE-REF present,
no fresh place gen). 0 portraits (story-cast reuse). **0 rerolls (0% — well under the 15%
COST-LAW budget).**

**Light QC — all 20 frames viewed once against beats + RUNNER-LESSONS:**
- Anchors QC'd first/hardest — LANE (s01/s03/s05/s06) + ROAD (s07/s09/s11/s12/s13/s15/s16/
  s18/s19/s20) plates propagated clean, no inherited defect.
- Count laws HELD: TWO disciples (green + blue-grey, same two men b01→b07), TWO donkeys
  (grey mother + darker-grey colt, colt ridden / mother led alongside — s03/s06/s08/s09).
- Jesus: face-locked and consistent, warm tan skin, cream robe, ONLY Jesus in cream in every
  crowd frame; proportionate — the humble-colt geometry (feet near the ground on the small
  mount) is the author's intended meekness read, NOT a giant/shrunk defect; no halo/glow.
- Realism: every frame photographic — NO cartoon/CGI/mixed frame (Law 14 clean).
- Crowd frames (s11/s13/s14/s16/s17/s20): joyful/fervent worship, cloaks + cut branches on
  the road, procession descends toward the in-frame gate — never mob-like, no weapons.
- No modern hard objects, no second cream robe, no dead lens-stare, no headless/extra-limb,
  no collage/panel, no modern skyline behind the ancient walls, no power-line across sky.

**FIX-WAVE (subtle background drift — deliberately NOT rerolled per COST-LAW; a later fix
wave's job, not obvious garbage):**
- s05: the laundry line's pegs read as possibly modern-style clothespins, and one faint
  fair-haired woman in the deep background — both background, non-subject, borderline.
- s14: one faint fair-haired woman at the far-left crowd edge.
(These are the exact "subtle drift" the runner is told to leave to the fix wave; no reroll
spent chasing them.)

## RUNNER PARK (A-auto Machine A `Dev`, 2026-08-06) — NEEDS-AUDIO / STALE-V1-FINAL — $0 SPENT — ✅ RESOLVED 2026-08-07 (flag set by AUDIO-FIX lane; picture runner built above)
Pre-flighted at step 2 BEFORE any credit (no stills generated, nothing to reuse-waste).

**BLOCKER — v2_assemble AUDIO LOCK will fail:** timeline total = 118.564s vs authoritative V1 mp4 `matthew-21_triumphal-entry.mp4` = 117.100s.
Tripwire(s): RUNTIME |Δ|=1.464s > 1.0 (line 531); RECENCY 15 mp3(s) newer than V1 mp4. V1 mp4 SHORTER than timeline (trailing-silence shortfall).
The AUDIO LOCK copies the finished V1 mp4's AAC stream packet-for-packet; it refuses when the mp4 does not match the recomputed timeline.

**Why the runner cannot fix it:** the fix is `AUDIO_FROM_V1_SEGMENTS = True` in this build's beats_v2.py (rebuilds the track from this build's OWN mp3s at the timeline offsets — nothing re-voiced, V1 stays read-only). Editing beats_v2.py is outside the runner's allowed writes (art / QC.md / boards / SESSION-LOG / review card / mp4 only — PROMPT-OPUS-RUNNER.md hard rails). Same class as parked rows 69/74/77/78/80/82/83.

**FIX (author):** set `AUDIO_FROM_V1_SEGMENTS = True` in beats_v2.py (and note: the {newer}-mp3 recency tripwire also needs a re-rendered V1 mp4 OR the segment-rebuild path, which the flag provides) then this row builds normally.

**RESUME after fix:**
```
python3 media-production-v2/v2_story_cast.py build-88-triumphal-entry --ceiling <c>
python3 media-production-v2/v2_gen_api.py build-88-triumphal-entry --ceiling <c>
python3 media-production-v2/v2_assemble.py 88
```

## 🔎 QC-VERIFY (FULL-CUT GATE) 2026-08-11 — Machine A `Dev`, unattended/headless — ONE defect found + fixed in ONE touch-once re-cut

Per PROMPT-OPUS-RUNNER.md §6b: extracted ONE frame per beat (mid-window) from the RENDERED
mp4 and viewed all 20 content frames + closing card against the defect checklist +
RUNNER-LESSONS. Row 88 had NO open Cameron complaint (verify pass on a BUILT row sitting in
the Unwatched queue before his eyes).

**19 of 20 frames + card: CLEAN.** Jesus face-locked/cream-only/tan/dark-hair/full-beard/
no-halo in every appearance; TWO disciples (green+blue) and TWO donkeys (grey mother + darker
colt, colt ridden / mother alongside) held the count law; gazes converge on Jesus in every wide;
cloaks+cut-branches carpet the road; crowds joyful not mob-like; procession toward the in-frame
gate; captions bottom-band only (white narrator / red Jesus-words / blue KJV-scripture, a
consistent 3-colour convention); closing reflection card clean. Realistic photography throughout —
no cartoon/mixed frame (Law 14 clean). Zoom-checked the other crowd close-ups (s11/s13/s17) for
the same artifact — all clean skin, correct joy.

**DEFECT — s14 (beat v2-r088-b14, "Hosanna means save us now"): BLOOD/WOUNDS on a crowd member
in a JOY beat.** Zoomed on the shouting old man center: a bleeding gash on his forehead, a red
cut/wound under his eye, and raw reddish abrasions across his chest/neck; the weeping woman beside
him carried a red streak reading as a bloody tear. This is a triumphal Hosanna celebration — a
bloodied/wounded figure reads as injury/violence at a glance and is exactly a Cameron complaint
(glance-read + no-gore). The prompt text is clean (no wounds); the model over-rendered the beat's
"taxed / tired / occupied / the word's real cargo" framing into visible injuries. The picture
runner's light-QC (2026-08-07) logged only "one faint fair-haired woman" for s14 and MISSED this —
the exact miss §6b's FULL-CUT GATE exists to catch.

**FIX (touch-once, $0.13, 1 reroll = 5% of 20 beats, well under the 15% COST-LAW budget):**
`v2_gen_api.py --only v2-r088-b14 --redo --ceiling 572`. New s14: old man clean skin (no gash, no
cut, no abrasions), weeping woman clean (tears, no blood), whole crowd joyful/fervent waving
palms+olive, only Jesus in cream at the right edge, every figure two-arms/one-head, realistic, no
halo. Verified in the RENDERED mp4 at t=75.82 with the correct white narrator caption.

**AUDIO: untouched.** Re-assembled via AUDIO_FROM_V1_SEGMENTS=True → AUDIO REBUILD PASS
SHA256=dda84afd… (rebuilt byte-identical from the same 15 V1 segment mp3s; 118.138s unchanged →
no window/caption drift). Only the s14 picture changed.

RUNNER-LESSONS fed: new one-line defect class (joy-beat blood/wound over-render).
