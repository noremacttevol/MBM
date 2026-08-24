# QC / RUNNER HANDOFF — build-190-faith-without-works

**Row 190 · James 2:14-26 · "faith without works is dead."** State: **AUTHORED / Ready ✅**
(picture map authored, `--check` PASS, audio OK, no open complaint). Fable-5 author lane,
Machine A `Dev`, 2026-08-07, $0.

---

## ✅ AUTHOR DONE — 12-beat V2 map, `--check` PASS, windows contiguous 0.000→45.480 (=card)

Fresh movie-coverage beat map (NEEDS-BEATS → AUTHORED). 12 pictures over 45.480 s ≈
3.79 s/pic. JAMES writing the letter is the frame; his teaching is illustrated by everyday
need, by Abraham on the altar, and by Rahab at the window; ONE recurring BELIEVER carries
the human arc from DEAD faith (idle, gives nothing) → LIVING faith (rises and serves).

Beat spine:
- b01 James writes (establishing, JAMES-ROOM promote) · b02 idle believer ("only in the head")
- b03 the poor brother & sister, no clothes/food (TOWN-DOORWAY promote) · b04 believer
  wishes them well but gives nothing · b05 **s1 SCRIPTURE (blue)** — faith alone is dead
- b06 Abraham on the altar (MORIAH-ALTAR promote) · b07 offering Isaac — **reverent
  obedience, Isaac unharmed, NO blade/blood/terror**
- b08 Rahab hides the spies (JERICHO-WINDOW promote) · b09 lowers them by the scarlet cord
- b10 **s26 SCRIPTURE (blue)** — the LIVING answer: believer clothes & feeds the poor ·
  b11 belief that moves (rises to serve) · b12 closing — faith and life joined

**SPEAKER LAW (James's epistle):** s1 (2:17) and s26 (2:26) = SCRIPTURE → **light-blue**
captions; all else narrator → white. **NO red-letter, NO God-voice. JESUS IS NOT IN THIS
STORY — every beat jesus=False and NO ONE wears cream or white** (cream is reserved for
Jesus, absent here).

**HARD GATE — GOD/FATHER NEVER EMBODIED.** Abraham's and Rahab's scenes are carried by the
people and their acts + natural daylight; no divine figure/hand/beam/symbol. Drift-word
gate clean (no halo/glow/rim-light). The b05/b09/b11/b12 `--check` "cream" WARNs are
benign — each says explicitly "(not cream)"; kept intentionally.

**CONTENT-CARE — Abraham/Isaac (b07):** Isaac bound but calm and UNHARMED; Abraham obedient
with eyes to heaven; NO knife at a throat, NO raised blade, NO blood, NO wound, NO terror.
Rahab (b08/b09): concealment + rescue, no violence shown.

---

## 🅿️ RUNNER — build the 12 stills (0 exist today)

**NEW places — promote each from its first NON-Jesus frame (all frames here are NON-Jesus):**
| Place | Promote from | Reuse on |
|---|---|---|
| JAMES-ROOM | **b01** | b02 |
| TOWN-DOORWAY | **b03** | b04, b05, b10, b11, b12 |
| MORIAH-ALTAR | **b06** | b07 · (or `v2_stash.py --wire` an existing build-114/115 Moriah/altar plate if suggested) |
| JERICHO-WINDOW | **b08** | b09 |

Gates before assembly: face/beard board on JAMES, BELIEVER (idle→serving = same man),
NEEDY-PAIR, ABRAHAM, ISAAC, RAHAB, SPIES; SCALE gate; content-care gate on b07 (no
violence/blood — reverent obedience only) and the sacred-figure gate (no God figure
anywhere); realistic-only Law 14 (no cartoon/mixed); NO ONE in cream/white; drift-word
checks. Then `v2_assemble` (AUDIO LOCK stream-copy, byte-identical — do NOT re-voice),
re-audit, ship. COMPLAINT LEDGER: none open.

---

## ✅ RUNNER SHIPPED (2026-08-24, Machine A `Dev`, Claude session)

Fresh build: 5 portraits + all 12 stills. **ZERO plate clones** — rubric lesson
26 applied before the first roll (8 beats given distinct cameras; the
6-beat TOWN-DOORWAY lane family was the risk and came back fully varied).
**2 rerolls / 12 = 16.7%. Cost $2.55 (19 gens: 12 stills + 5 portraits + 2 rerolls).**

**Reroll ledger (both on b02, and the second one is my own process error):**
- `v2_story_cast` generated all five portraits but the map had been authored
  with `REFS = {}` ("No image REFS — carried by text locks"), and the cast
  script did NOT wire them. So the whole first pass generated UNANCHORED and the
  BELIEVER drifted in b02 into a different, older grey-bearded man (rubric
  lesson 2 — a text lock alone is not enough). Fixed by wiring all five REFS.
- The first b02 reroll was WASTED ($0.13): my wiring edit asserted and failed,
  but I fired the reroll in the same command, so it regenerated still
  unanchored. **Verify the edit landed before spending** — the same trap logged
  on row 156. The second reroll ran with `[+1 char ref: BELIEVER]` and matches
  the canonical portrait.

**FULL-CUT GATE — 12 beats + card viewed on the ENCODED mp4: PASS.** SPEAKER
LAW: s1 (b05) + s26 (b10) LIGHT-BLUE; narrator white; no red, no green; **no
Jesus, nobody in cream/white**. GOD NEVER EMBODIED. CONTENT-CARE held: Abraham
and Isaac is reverent obedience — Isaac calm and unharmed, **no blade, no blood,
no terror**; Rahab is concealment and rescue by the scarlet cord, no violence.
The believer's arc reads (idle → gives bread → carries blanket → stands with
them). Card clean.

**AUDIO — diagnosed, not assumed:** stream-copy refused on a 16-second gap
(V1 68.767s vs extract 52.662s), too large for spacing. Verified by full
transcription that the V1 mp4 contains EXACTLY the 9 segment texts and nothing
more, and that all 9 mp3s are ElevenLabs new-voice (44100/128k) written 57
seconds AFTER the mp4 — i.e. the mp4 carries the OLD slower voice. Rebuilding
from the segments therefore loses no content and ships the NEW voice.
**AUDIO REBUILD PASS SHA256=3e61318544…**, 52.7s, 19.7 MB; the encoded cut was
re-transcribed and carries every line through the closing card.
