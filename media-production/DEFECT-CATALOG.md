# MBM — COMPLETE VIDEO DEFECT CATALOG (for Claude's repair pass)

**Source:** PRODUCTION-BIBLE.md §4b, §5, §5b (the laws Cameron paid for via rejected videos). Every item below is a real, named failure mode. Claude should check ALL of these on EVERY one of the 200 videos.

**How to use:** For each video, walk every still + sampled frame + the full audio. Mark each item PASS / FAIL. Any FAIL = that video goes to the fix queue.

---

## A. CAPTIONS (your #1 repeated complaint)
1. Caption covers more than the bottom quarter of the picture (any frame) — FAIL.
2. Long caption not SPLIT — should swap halves in sync with narration, never blanket the image.
3. Font shrunk to cram a long caption instead of splitting — FAIL.
4. Tofu / missing-font squares (empty boxes) in any caption or end card — FAIL (seen on #7).
5. End card text renders with wrong/missing glyphs — FAIL.

## B. AUDIO
6. Background HUM / synthetic music bed under narration (constant tone ~110/165/220/330 Hz) — FAIL. Audio = narration + silence ONLY.
7. Dead-air gap > 2.5s mid-video (no spoken gap over 2.5s) — FAIL. (18 videos flagged: #7,30,32,128,137,145-150,171,172,173,174,175,187,195.)
8. TTS misreads a homograph: live/lives/lived (/liv/), bow (/boh/), wound, wind, tears (/teerz/), lead, sow, read, dove, bass, minute, use/used, close — caption keeps KJV word, only SPOKEN audio respelled. Misread = FAIL.
9. Narrator quotes KJV (narrator must be plain modern English; only Jesus voice quotes KJV) — FAIL.
10. Jesus voice departs from EXACT KJV — FAIL.
11. Spoken gap inside a sentence > 2.5s — FAIL.

## C. JESUS FACE (FACE-SHOWN LAW — final as of 2026-07-15; the old "face withheld" law was REVERSED)
> The `jesus_face_gate.py` is a PRE-PAINTING prompt check (locks prompts to JESUS-MASTER-REF, blocks face-leaking language). It is NOT a rule that the finished video hides his face. The finished videos SHOW his face — that is correct and expected. When QC-ing a built video, seeing Jesus's face is right.
12. Jesus's face MISSING where the story calls for it (FACE-SHOWN is the current law) — FAIL.
13. Jesus face NOT consistent across frames (must be the SAME man, locked to JESUS-MASTER-REF/jesus-face.jpeg) — FAIL.
14. Jesus depicted caucasian / pale / blue-eyed / blond / not Middle-Eastern (warm tan skin, dark brown-black shoulder-length hair, full dark beard, warm BROWN eyes) — FAIL (hard ban).
15. Halo / glowing ring around Jesus's head — FAIL (seen subtle on #136 s5).
16. Brown mantle / non-cream robe variance over the cream robe — FAIL (noted #111, #138).

## D. ANATOMY & FIGURES
17. Wrong anatomy count: not 2 arms, 2 hands, 5 fingers (where legible), 2 legs, 2 feet, 1 head per figure; limbs connect to right body — FAIL. (Climbing/crowd/table scenes highest risk.)
18. Duplicate named character in one frame (model reuses a locked character as crowd filler) — FAIL (Zacchaeus twice).
19. Character-look drift: hairline (receding vs full), hair length/color, beard, face shape/age, build, wardrobe changes between stills — FAIL.
20. Physical trait that IS the story not reading (Zacchaeus short, Bartimaeus blind eyes, withered hand) — FAIL.
21. Trait exaggerated into caricature / dwarfism / demeaning (short man must be normal-proportioned short adult, head at others' shoulders) — FAIL.
22. Scale wrong: a figure dwarves or giants next to others unintentionally (lepers as giants vs Jesus, #14) — FAIL.

## E. ACTION & LOGIC
23. ON-THE-WATER LAW: sea figure not standing ON the surface (waist-deep/wading) except Peter sinking beat — FAIL (#7).
24. Figure direction/facing contradicts the narration at that moment — FAIL (#7 noted).
25. Action reads wrong at a glance (bailing throws water in, ropes not connected, backwards) — FAIL.
26. Lighting wrong for scripture time of day (night story with golden-hour sky) — FAIL.
27. Figure outside where scripture puts them (standing on water when not scriptural) — FAIL.

## F. CONTENT-CARE
28. Gore / wounds in focus (crucifixion reverence-distance; no wet CGI; at most one painted teardrop, never wet beads) — FAIL.
29. Embodied Satan / devils / creatures shown — FAIL.
30. Shame framing on D (judgment) stories; mercy NOT spoken aloud in J stories — FAIL.
31. Closing question is fear-based, not an invitation — FAIL.
32. Child-in-peril image — FAIL.
33. "Would a parent let a 10-year-old see this frame?" = no — FAIL.

## G. STYLE & RENDER
34. Style drift: photoreal, 3D-render look, cartoon-comedy, different palette vs gold-standard — FAIL.
35. AI-animated (Veo/Flow) clip present in a Phase-1 stills-only video — FAIL (clips must be removed).
36. AI text / gibberish baked into any image — FAIL.
37. Modern objects in a 1st-century scene — FAIL.
38. Reference image copied as portrait instead of composing the scene (ref-dominance collapse) — FAIL.

## H. SCRIPTURE & FORMAT
39. A MUST-SHOW item from the scripture card missing — FAIL.
40. A MUST-NEVER-SHOW item present — FAIL.
41. Verse card wording not from PAIRING-LIST.md (hand-typed not fetched) — FAIL.
42. Closing question doesn't match the pack's Seed question — FAIL.
43. File not named `book-chapter_story-name.mp4` (SCRIPTURE-NAME LAW) — FAIL.
44. Not 9:16 / 1080×1920, or doesn't play clean start to finish — FAIL.
45. Over 30MB (or starved bitrate to fit) — FAIL.

## I. NARRATION CONTENT
46. Narrator voice not plain modern English — FAIL.
47. Whole story not carried to its final verse — FAIL.
48. Sacred-silence beat missing where the law/spec calls for one — FAIL.

---

**Tier 1 (Cameron-confirmed):** #7, #17, #32.
**Tier 2 (dead-air, 95%):** #30,32,128,137,145,146,147,148,149,150,171,172,173,174,175,187,195.
**Full per-video results:** QC-REVIEW-LIST-2026-07-17.md
