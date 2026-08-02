# Story 35 Realistic V2 QC — The Great Banquet (Luke 14:16-24)

Final: `luke-14_great-banquet.mp4` — 1080×1920 H.264, 30 fps, **141.700 s**, 21.2 MB.

- 40 realistic 9:16 pictures at native 2K (1536×2752), against V1's SEVEN.
- Encoded-audio SHA-256 `8df704364c8bd7419841a5a917d3842ff021e3d40d510dc86832373302e2c0a5`
  — **AUDIO LOCK PASS**, byte-identical to the authoritative V1 final. No narration,
  voice, line, pause or closing audio was regenerated, shortened or replaced.
- New shared setting locks earned by this build: **BANQUET-HALL** and the
  **SANDAL-CONSTRUCTION** clause inside PERIOD-MATERIALS.

## What V1 actually did (verified from the artefact, not the prose)

- ONE picture held **27 s** across all three excuses — the man with the field, the man
  with the oxen and the man just married, three different men in three different
  places, all on a single image.
- Another held **31 s** across "go out into the highways and hedges" and the entire
  closing application, which therefore had no picture of its own.

Every line now has its own frame: the sabbath table where Jesus tells it, the hall laid
and waiting, the servant sent out, each excuse in its own place, the empty room, the
lamplit streets, the poor and the lame and the blind brought in, the road beyond the
town, and the table filled.

## Content care

- Nothing of heaven, hell, throne, crown, judgement or angels is painted — the
  narration does not state them. It is a real supper in a real house.
- God is never depicted as any figure, face, form, light or presence.
- "Compel them to come in" is staged as **open-handed welcome, never force**: nobody is
  seized, gripped, dragged or restrained anywhere in the cut.
- Nobody poor, lame or blind is drawn grotesque, comic or pitiable; each is a real
  person with dignity.
- Jesus carries only the frames he actually speaks in. The host is a parable nobleman
  and never reads as Christ; he wears deep madder red and deep indigo, never cream.

---

## 2026-08-02 — CONTINUITY FIX, one image, reshipped

**Defect.** `s04-he-made-a-great-supper.jpeg` — the HOST anchor frame, on screen
**7.947–11.370 s** — was generated *before* this build's house-hanging cure existed and
came back with a **PALE GOLD, softly pleated, modern-looking drape** in the doorway.
Every later frame of the same room (s05, s06, s17, s19 …) shows the **dark goat-hair
hanging**. Cameron has rejected finished videos for exactly this class of defect
("the clothes keep changing", "he lost his beard in one of the pictures"), so the room
changing colour between two shots four seconds apart is a real failure, not a nit.

**Why the lock did not catch it.** The `HOUSE` lock's dark-hanging clause — "NO HANGING,
CURTAIN, DRAPE OR PANEL ANYWHERE IN THIS BUILDING IS CREAM, OFF-WHITE, IVORY, BUFF,
BEIGE, PALE GOLD…" — was written *after* s04 had already been generated and accepted.
The frame simply predates its own cure. Nothing was wrong with the lock.

**How it was fixed — composition-level, not a correction pass.**
`--redo` was deliberately NOT used: it re-attaches the defective frame itself as the
rough reference, which preserves the very drape that has to go. Instead:

1. The beat's `must_not_show` gained the pale-gold / pleated-curtain clause.
2. The beat's **scene text** gained a POSITIVE statement of what the hanging IS and
   where it sits — per the row-10 geometry lesson, a prohibition alone does not hold:
   *a heavy panel of coarse undyed goat-hair cloth in near-black charcoal and deep
   umber, pushed hard against the FAR jamb and knotted back on itself in a thick dark
   bundle so the opening stands clear for the light*, hung from a hewn timber pole.
3. The file was **deleted**, which also makes `_have()` withhold it from `REFS`, so the
   anchor could not reference its own defective self.
4. One fresh generation. **One image, no reroll.**

**Result.** The doorway hanging is now near-black goat-hair, tied back with a fibre
cord, hung from a hewn timber pole — matching every other opening in the house. Host
identity holds against the rest of the video: same greying dark-brown hair, same full
dark beard, same deep madder red tunic and deep indigo mantle, strict side-on profile,
one visible eye travelling off the LEFT edge, pupils nowhere near the lens.

**Verification of the reshipped artefact (frames extracted and looked at, not inferred).**

- Real frames pulled at 8.5 s and 10.5 s: dark hanging present in the cut itself.
- Frame at 60.0 s: the host is visibly the same man as the new anchor — no face drift
  introduced by regenerating the anchor.
- Captions are drawn, in the bottom band only, never over the art; white narrator.
- Frame at 139.0 s: the closing card carries its words.
- `silencedetect -45dB`: true silence windows throughout (1.52 s, 1.76 s and more) —
  **proves there is no music or tone bed**.
- `AUDIO LOCK PASS` — audio still byte-identical to V1 after the rebuild.

**Cost of the fix:** 1 image (~$0.134) + one reassembly.

New final Git blob SHA-1: `c34f72cc01516b9d5716d6ddd1f6247d62a682eb`
(previous: `d755198770cd1fe0524c857f3e8b88638c39ecff`).

## Lesson for later rows

When a lock is strengthened part-way through a build, **the frames generated before that
moment are not covered by it.** Grep the build for every frame that shares the cured
setting and re-inspect them in the same pass, rather than trusting that the lock was
always there. A cure applied at beat 20 protects beats 20-40 and nothing behind it.
