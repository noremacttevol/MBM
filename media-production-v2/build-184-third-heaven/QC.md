# build-184-third-heaven — QC / runner handoff (2 Corinthians 12:2-4,9)

**AUTHORED 2026-08-07, Machine A `Dev` (Fable-5 author lane, $0).** 16-beat V2 map,
`v2_prompt.py --check` PASS (0 warnings), windows contiguous+monotonic 0.400→66.687
(=card_start), every segment onset in-window, audio OK. Picture-only rebuild — do
NOT re-voice.

---

## COMPLAINT LEDGER (LEARNING LAW)

**OPEN complaint:** *"only Jesus's words in red."*

**What in this cut fixes it:** exactly ONE segment is red, and it is Jesus's own
words. The red-letter is **j1** — *"My grace is sufficient for thee: for my strength
is made perfect in weakness"* (b12/b13) — the Lord's answer to Paul, placed on the
risen LORD JESUS speaking to Paul (RED caption). Paul's own written account **s1**
("I knew a man in Christ...", b02-b04) and **s2** ("caught up into paradise... "
unspeakable words", b07/b08) are **SCRIPTURE → LIGHT-BLUE**, never red — they are
Paul's words, not the Lord's. Every narrator segment (n0-n3, card, all other beats) is
**WHITE**. make_narration.py already carries this map (only j1 = JESUS).

**Runner MUST verify in the rendered mp4:** j1 (≈0:48-0:55) renders RED; s1 (≈0:07)
and s2 (≈0:27) render LIGHT-BLUE, NOT red; everything else white.

**Review card MUST tell Cameron:** *"Only Jesus's words are in red now — just 'My
grace is sufficient for thee...' Paul's own account of the vision is in the blue
scripture colour."*

---

## ✅ RUNNER SHIP NOTE — REALISTIC-V2 FIRST CUT (2026-08-13, Opus runner headless, Machine A `Dev`)

**BUILT & SHIPPED.** 16 realistic painted stills @ native 2K, AUDIO LOCK PASS
SHA256=`6ede9fa385994cee9953a7967d4df63bd032c6185f1b509a34589c48801b6718`, 74.9s
(= V1 mp4 duration, byte-identical narration — nothing re-voiced), 20.3 MB.
**0 rerolls (0% vs 15% budget), ~$2.28 (16 beats + 1 PAUL portrait × $0.134).**

**COMPLAINT LEDGER — verified in the RENDERED mp4 (§6b FULL-CUT GATE):**
- OPEN complaint *"only Jesus's words in red"* → **FIXED & VERIFIED.** Extracted
  one frame per beat from the delivered mp4: the ONLY red caption is **j1**
  ("My grace is sufficient for thee: for my strength is made perfect in
  weakness") on b12/b13, the risen Lord speaking to Paul. **s1** (b02/b03/b04,
  "I knew a man in Christ…") and **s2** (b07/b08, "caught up into paradise…
  unspeakable words") render **LIGHT-BLUE scripture, NOT red**. Every narrator
  line (n0-n3, b01/b05/b06/b09-b11/b14-b16, card) renders **WHITE**.

**FULL-CUT GATE 16/16 beats + question card PASS** (rendered-mp4 frames, not just
assets): HARD GATE — the vision (b02-b08) shows ONLY Paul borne up in radiant
light; NO God/Father, NO throne/divine figure, NO paradise interior, NO rendered
words ("into paradise" = brilliant light hiding all it holds; "unspeakable words"
= Paul keeping silence, hand on heart). Jesus embodied ONLY on b12/b13 — exactly
ONE cream-robed Jesus, locked V2 face consistent across both, calm eyes, no
halo/glow/rim-light, ordinary scale; Paul in brown (cream-only-Jesus holds). PAUL
one consistent balding dark-bearded ~50 man on all 14 of his beats (face-board +
beard-board pass); PAUL text-lock only (no image REFS — author's deliberate
cross-video byte-identical choice, matching builds 138/155/166/171; held clean
across 14 beats). PAUL-ROOM plate promoted from b01 (NON-Jesus), HEAVENLY-ASCENT
from b02. Captions bottom-band only; question card clean (no box glyphs).
Realistic photography throughout (Law 14), no modern objects, anatomy/hands/scale
clean, no owl-neck. Drop-check: concat_base 16 clips == 16 beats, card_start
66.599 > b16 window 61.400 (no dropped beat).

---

## 🅿️ RUNNER — do this (picture-only build on the locked audio)

1. **Audio:** default AUDIO LOCK stream-copy (board Audio = OK). No re-voice, no flag.
2. **Places are NEW — promote-first (lesson 11):**
   - `PAUL-ROOM` → generate **b01** (establishing wide, NON-Jesus) first, QC it,
     `--promote build-184-third-heaven PAUL-ROOM <b01 frame>`, then b09, b10, b11,
     b14, b15, b16 — and b12/b13 (the Jesus beats) with the plate attached.
     **Promote from b01, NEVER from a Jesus-bearing frame** (b12/b13).
   - `HEAVENLY-ASCENT` → generate **b02** (establishing wide of the ascent) first,
     QC it, `--promote ... HEAVENLY-ASCENT <b02 frame>`, then b03-b08.
3. **SPEAKER-LAW / RED-LETTER (the complaint):** ONLY b12/b13 (j1) are red on Jesus.
   b02-b04 (s1) and b07/b08 (s2) are LIGHT-BLUE scripture. All else white. Verify the
   colours in the delivered mp4 (see COMPLAINT LEDGER).
4. **Jesus (b12/b13 only):** the assembler injects JESUS LOCK v5 + the master REF
   (jesus=True, ref=True). Jesus is the ONE locked face, cream-only, NO halo/glow/
   rim-light. Run the face gate (`jesus_face_gate.py --dir build-184-third-heaven`
   must exit 0) before any credit. Jesus does NOT appear anywhere else.
5. **HARD GATE — the vision does NOT depict God / paradise / the words.** The ascent
   beats (b02-b08) show ONLY Paul borne up through radiant light — NEVER God the
   Father, a throne, any divine/heavenly figure or being, the interior/contents of
   paradise, or any text/symbol/scene of the "unspeakable words" (2 Cor 12:4 forbids
   uttering them, so they are not shown). Reject any reroll that adds a figure, a
   gate/garden/city interior, or rendered words to the vision.
6. **CONTENT-CARE:** reverent wonder, no fear/horror. Paul's "weakness" (b11/b15) is
   humility, NOT sickness/wounds — no thorn-in-the-flesh literalism, no gore.
7. **Face / scale board (lessons 2/10/14):** PAUL is the SAME wiry ~50 balding
   dark-bearded man (byte-identical to builds 138/155/166/171) on every beat; Jesus
   the one locked face on b12/b13; both ordinary-sized on b12/b13. Identity-edit
   drift, recheck the whole frame.
8. **Drift-word gate:** no halo/glow/rim-light — light is radiant/luminous/brilliant
   in the heights, never a ring around a head.
9. **Assemble** with `v2_assemble.py` (AUDIO LOCK stream-copy must pass), verify
   captioned length ≈ card_start (66.687) + card, decodes 0 errors, realistic-only
   (Law 14) on all 16. Ship to the reviewer with the complaint-answer card.

## Coverage / windows
16 beats, ~4.1 s/pic. Contiguous window starts: b01 0.400 · b02 6.445 · b03 10.500 ·
b04 15.500 · b05 20.040 · b06 23.500 · b07 26.600 · b08 30.500 · b09 34.636 ·
b10 40.580 · b11 43.560 · b12 48.347 · b13 51.800 · b14 55.184 · b15 57.730 ·
b16 61.400 · (hold to card_start 66.687).
Arc: Paul writes of a man caught up → "I knew a man in Christ" → in body or out, God
knows → the third heaven → could not say → carried further → to paradise's threshold
(contents hidden in light) → hears unspeakable words (never shown) → keeps the silence
→ had the credentials → pointed to his weakness → the Lord: "My grace is sufficient"
→ "made perfect in weakness" → what I give is enough → strength in weak places → still
pointed back to grace.
