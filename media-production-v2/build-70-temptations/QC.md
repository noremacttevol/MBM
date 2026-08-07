# QC / RUNNER HANDOFF — build-70-temptations (Matthew 4:1-11)

Lesson-12 + complaint-corpus pass done 2026-08-05 (Machine A). `--check`
PASSES, zero WARNs. 42 beats, ~237 s.

## ⚑ A-LAW — THE ADVERSARY IS NEVER DEPICTED (the row's absolute law)

No figure, no shadow-shape, no silhouette, no voice-form, no red glow,
no serpent, no second man — EVER. The temptations arrive as the build
authored them: wrongness in the light, pressure in the silence, the
framing of the offers (stones, the drop, the vista). If any render
contains a second figure in a temptation beat, it is an automatic
reject. The only non-Jesus figures in the row are the two blue-robed
MINISTERS after the victory (b33-b35, restrained: robed figures with
bread and water — reverent, wingless, human-scaled).

## Coverage shape — SOLITUDE IS THE STORY

ONE true wide (b33 — the ministers arriving, three figures in profile:
the tide turning is the one moment company exists). TEN former wides
were Jesus ALONE against vastness (the waste, the pinnacle, the black
summit) — the phantom-people trap at its absolute worst; every one is
re-flagged and the emptiness now rides in the prose. If a render adds
anyone to a solo frame, reject.

## The three temptations (framing laws)

1. STONES (desert): real desert stones that resemble loaves at his
   feet — the resemblance is the temptation; no talking figure.
2. PINNACLE: the temple parapet with the REAL drop below — city small,
   vertigo honest; he never wavers on the edge.
3. SUMMIT: the world's glory as a vista — kingdoms as far lights and
   distant splendors, never a floating montage or globe.
   The dismissal (b31): his arm flung toward the empty air — command
   with no visible addressee, exactly like row 65's b24.

## Other checks

- The fast shows: b05 onward Jesus is visibly leaner, wind-worn,
  sun-dark — but never emaciated-horror (row-15 dignity law); the
  hunger is real and borne.
- Direction (row-83): b01 UP from the green valley into the waste;
  b42 BACK DOWN toward the green at dawn — the arc closes.
- All four places promote-first (DESERT b04, PINNACLE b18, SUMMIT b26
  from their first solo frames; MINISTERS is CAST — no plate).
- Wilderness is Judean badlands — brown, broken; distinct from row
  54's leper wilds and row 59's Decapolis slope (three wildernesses,
  three plates — never cross them).
- Only Jesus wears cream.

---

## ✅ AUDIO FIX DONE — AUDIO-FIX session, Machine A, 2026-08-06

**Both of Cameron's row-70 audio complaints are CLOSED. $0 spent** (edge-tts is
free; no Gemini, no ElevenLabs). Audio is now new-voice-clean and the row is
handed to the picture runner to build on the corrected narration (0 V2 stills
existed, so nothing visual was shipped — same handoff as rows 50/51).

**COMPLAINT LEDGER (picture runner: surface this on the review card when you ship):**
> Cameron: *"The narrator spells out 'I-S' instead of pronouncing the word like
> it should. Also it mispronounced 'proceedeth' it should be pro-see-duhth."*
- **"I-S" spelled out** → FIXED. n2's emphasis-caps `IS`/`IF` ("this **IS** my
  Son", "the little word **IF**") were read letter-by-letter by edge-tts
  (whisper heard caps "IS" as "I asked"). Build-local `SPOKEN` now lowercases
  them **for the TTS only** — the caption still shows the caps. Re-voiced n2
  (narrator/Andrew); whisper now hears "this **is** my son", "the word **if**".
- **"proceedeth" mispronounced (wants pro-see-duhth)** → FIXED. j1 (Jesus/Eric)
  respelled `proceedeth`→`proceeduth` in `SPOKEN`; measured with
  check_pronunciation — "proceeduth" round-trips 100% back to "proceedeth" and
  lands the pro-SEE-duhth target. Caption still shows "proceedeth".

**New audio baseline (audio-immutability sanctioned re-voice — ONLY the two
complained segments changed; the other 20 mp3s are byte-identical, untouched):**

| seg | voice | old md5 | new md5 | old dur | new dur |
|---|---|---|---|---|---|
| n2 | narrator (AndrewNeural) | cbe712b38ed12326241f0978ac837913 | 9167d7ef38376b852737f14df29db716 | 18.437s | 19.891s |
| j1 | jesus (EricNeural)      | 1d777bf6cae1e447fe41dc56a6f8f17e | 730bc3aad189af17efee3925a532ef2a | 7.802s  | 8.928s  |

`SPOKEN = {"IS": "is", "IF": "if", "proceedeth": "proceeduth"}` in
`make_narration.py`. Same voices, same wording, same timing everywhere except
the two fixed segments (which run slightly longer — the runner recomputes the
timeline from the mp3s at assemble time, exactly as it does for a fresh build).
`v2_prompt.py build-70-temptations --check` still PASSES (42 beats). Board:
NEEDS-AUDIO → AUTHORED / Audio OK / Ready ✅, claim cleared.

---

## 🅿️ RUNNER PARK — A-auto Machine A, 2026-08-06 (AUDIO RE-VOICE, out of runner scope) — RESOLVED ABOVE

**Do NOT build this row until the narration is re-voiced.** The lowest-Ready
runner reached row 70 and stopped here on the LEARNING LAW.

**Open reviewer complaint (from `v2_outline.py 70`):**
> "The narrator spells out 'I-S' instead of pronouncing the word like it should.
> Also it mispronounced 'proceedeth' it should be pro-see-duhth"

**Why the runner cannot fix it.** The V2 pipeline ships **byte-identical V1
narration** (v2_assemble.py AUDIO LOCK assembles from the existing mp3s; nothing
is re-voiced or resynthesised). The two defects are baked into those mp3s:

1. `make_narration.py` segment **n2** narration source contains all-caps
   **"this IS my Son"** — the TTS reads the emphasis-caps token `IS` as the
   letters *I-S*. The build's local override dict is **`SPOKEN = {}` (empty)**,
   so nothing respells it. (The lowercase `if`/`is` in the same line are fine;
   only the caps `IS` breaks.)
2. Segment **j1** `"...every word that proceedeth out of the mouth of God."` has
   **no pronunciation override** for `proceedeth` → the voice mispronounces it.

Fixing either one requires **regenerating the narration mp3s** (add a build-local
`SPOKEN` / pronounce override: caps `IS`→`is` respell, `proceedeth`→a `pro-SEE-duhth`
respell, then re-run `make_narration.py` and re-hash the AUDIO LOCK). That is a
re-voice — outside the runner's allowed writes (art / QC / boards / log / review /
mp4 only) and the exact class that parked rows 50 and 51.

**Resume (author/audio track, NOT the runner):**
1. In `build-70-temptations/make_narration.py` add:
   `SPOKEN = {"IS": "is", "proceedeth": "pro-SEE-duhth"}` (tune the proceedeth
   respell against the voice with `mbm_pronounce.audit`; verify caps-IS is only in
   n2 — grep confirms it is).
2. Re-generate n2 + j1 (or the whole track), re-establish the AUDIO LOCK source,
   ear-check both segments (`I-S`→"is"; proceedeth = pro-SEE-duhth), set
   AUTHOR-BOARD Audio back to **OK** + Ready **✅**.
3. Runner then builds normally: `v2_prompt.py build-70-temptations --check` already
   PASSES (42 beats); art has not been generated yet, so no spend was wasted.

Nothing was generated and no credit was spent on row 70 this session.
