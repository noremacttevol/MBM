# MBM PRODUCTION BIBLE — The Permanent Law for Making All 200 Videos

> **READ THIS BEFORE TOUCHING ANY VIDEO WORK. EVERY SESSION. EVERY AI. EVERY PLATFORM.**
> Cameron explained this system once (2026-07-08) and never has to explain it again.
> Any AI helping with MBM media reads this file first and follows it exactly.
> Cameron's job: watch finished videos and say yes or no. That's it.
> The AI's job: everything else — prompting, generating, reviewing, assembling, reporting.
> Cameron NEVER writes prompts, never edits clips, never hunts for errors. If the AI
> finds itself asking Cameron to do any of that, the AI is doing it wrong.

---

## 1. The Mission (unchanged, forever)

Every video exists to show one thing: **Jesus is good.** Story-first, scripture-true,
never argumentative, never preachy. The Jesus Method rules in CLAUDE.md / AGENT-RULES.md
govern all content. The Two-Voice Law applies: narrator speaks modern; Jesus speaks
ONLY exact KJV words. Jesus's face is NEVER shown — light, silhouette, hem, feet,
hands-never-visible. The BOM law holds: these 200 videos stay MILK.

**The Voice Law (Cameron, 2026-07-07 — permanent):** The Jesus voice is AMERICAN,
never British — he was not British. Current voices (edge-tts, placeholders until
Cameron locks finals): narrator `en-US-AndrewMultilingualNeural`, Jesus
`en-US-ChristopherNeural`. Any future voice change still obeys: American, warm,
low, unhurried, same Jesus voice across all 200 videos.

**The Full-Story Law (Cameron, 2026-07-07):** Never flatten a story to its
headline moment. Include the surrounding humanity that shows he actually cared —
e.g. for the cloak story: he was already on his way to Jairus's dying daughter,
the crowd made one sick woman nearly invisible, he FELT power go out of him,
asked "Who touched my clothes?" (KJV Mark 5:30), was questioned by his own
disciples, ignored them, and kept looking until he found her. Backstory and
resistance beats make the stop mean something.

## 2. THE LOCKED LOOK — Master Style Block (never change without Cameron's explicit word)

Every image and every video clip for all 200 videos begins with this exact text:

```
Beautiful hand-painted 2D animation style, reverent and warm, like a classic
illustrated storybook of scripture brought to life. Soft painterly brushstroke
textures, glowing golden light, muted earth tones with warm gold highlights.
First-century Judea. Slow, tender movement. Sacred, hushed tone. Not
photorealistic. No text or captions in the image. Historically modest clothing:
rough-woven wool and linen in undyed earth colors. No modern objects.
```

(For stills, drop the "Slow, tender movement" line.)

- **Approved reference:** the clip "Woman touches cloak hem" in Flow project
  "MBM Story Videos — Wave One" (generated 2026-07-08, Veo 3.1 Fast) is the visual
  gold standard. Every new generation is compared against it. When Flow's
  Ingredients/reference-image feature is available, use frames from approved clips
  as style anchors to hold consistency.
- **Consistency check (every asset):** same palette (warm gold/earth), same painted
  texture, same reverent lighting. If a generation drifts toward photorealism,
  3D-render look, cartoon-comedy look, or a different palette — reject and
  regenerate. Style drift is a QC failure equal to a scripture error.
- The photoreal live-action direction is DEAD (Cameron, 2026-07-08). Never revive it.

## 3. The Hybrid Pipeline (stills + motion, story decides the mix)

**The format:** narrated storybook videos. Beautiful painted stills carry most of the
runtime with slow camera drift (Ken Burns) added in assembly. Real animated video
clips are used ONLY where the story's power demands motion — the "money moments."

**THE STORY-FIT RULE (Cameron's law):** there is NO fixed ratio. The story decides.
- A quiet parable told mostly by the narrator may be ALL stills (0 video clips).
- A standard story: ~10–14 stills + 1–2 animated clips for its money moments.
- A story whose heart IS motion (calming the storm, walking on water) may earn
  3–4 animated clips. That's the ceiling without flagging it to Cameron in the
  session report (not asking permission — just visibility on credit spend).
- Every story gets a STORYBOARD first (section 4) that declares which beats are
  stills and which earn motion, with one line of why.

**Validation sequence (locked):** the first two full productions after video #1 are
LOW-ANIMATION stories (mostly/entirely stills) to prove the cheap end of the format
works. Then scale the motion budget per story as the Story-Fit Rule allows.

## 4. Per-Video Assembly Line (the AI runs every step)

1. **Scripture card.** Pull the exact KJV passage. Derive two lists from the text
   alone: MUST SHOW (facts the text states) and MUST NEVER SHOW (things the text
   contradicts + the standing rules: Jesus's face never, Jesus's hands never,
   Jesus never touches first in stories where the person reached for him, etc.).
   The card is written into the video's production pack before any generation.
2. **Storyboard.** 8–16 beats. Each beat marked STILL or MOTION with a one-line
   reason. Narration line drafted per beat. Jesus's KJV words (if any) placed.
3. **Generate stills** in Flow (Image mode, 9:16, master style block + beat prompt
   + the card's MUST NEVER SHOW items as explicit "no ..." lines). 1–2 credits each.
   Review each against the card at a glance; regenerate misses immediately.
4. **Generate motion clips** (Veo Fast, 9:16, 1x, 8s) for money moments only.
   Same style block + card prohibitions in the prompt. Review IN THE PLAYER,
   not just the thumbnail — scrub start/middle/end. (Lesson learned: a wrong
   hand hid in motion once. Never approve from a thumbnail again.)
5. **Assemble locally** (ffmpeg/editor on Cameron's machine — costs nothing):
   drift moves over stills, clips cut in at their beats, narration track,
   serif captions, KJV verse card, closing question card (6s, cream #F7F2E9),
   music bed cut to silence at the sacred line. Export 1080×1920 H.264 <25MB.
6. **QC pass (checklist below), then present the finished video to Cameron.**
   He watches and says yes/no. On yes → delivery pipeline (Firebase Hosting
   /story-videos/, expo-video key per THE-200 id). On no → AI fixes and re-presents.

## 5. QC Checklist (every video, before Cameron ever sees it)

- [ ] Every MUST SHOW item from the scripture card appears
- [ ] Zero MUST NEVER SHOW items appear (scrub every motion clip fully)
- [ ] Jesus's face never visible in any frame; his hands never visible
- [ ] Style matches the gold-standard reference (palette, texture, tone)
- [ ] No AI text/gibberish baked into any image
- [ ] Narration modern; Jesus voice EXACT KJV only
- [ ] Verse card wording pulled from PAIRING-LIST.md, text fetched not hand-typed
- [ ] Closing question matches the pack's Seed question
- [ ] 9:16, 1080×1920, plays clean start to finish

## 6. Money & Credits (why this plan is affordable)

- Stills: 1–2 credits. Veo Fast clip: 20 credits on Pro, 10 on Ultra.
- Typical video ≈ 25–60 credits. All 200 ≈ ~11,000 credits including retakes.
- Plans (verified 2026-07-08): Pro $19.99 = 1,000 credits/mo; Ultra $100 tier =
  10,000/mo; Ultra $200 tier = 25,000/mo. The $200 Ultra tier covers all 200 in
  one month with >2x margin; the $100 tier covers it lean. Credits don't roll over.
- The AI reports credit spend in every session log entry so Cameron always knows
  where the month stands. Big-motion stories (3–4 clips) get flagged in the report.

## 7. What Cameron's money is buying (the promise this file enforces)

Same look, same feel, same flow, every video, no matter which AI session makes it —
because the style block is frozen text, the pipeline is frozen steps, the QC list is
frozen checks, and this file is the single source of truth. If any future direction
change is wanted, Cameron says it once, this file gets edited and committed, and the
new law holds from then on. Nothing lives in anyone's memory. Everything lives here.

## 8. Session workflow for any AI picking up media work

1. Read CLAUDE.md chain protocol, START-HERE.md, AGENT-RULES.md — then THIS FILE.
2. Check SESSION-LOG.md top entry for where production stands (which video, credits left).
3. Continue the assembly line exactly where it stopped. No re-litigating style or format.
4. End of session: SESSION-LOG.md entry (videos progressed, credits spent/left,
   any QC lessons learned added to section 5), commit, push.

---
*Created 2026-07-08 from Cameron's direction. This file outranks any older media doc
where they conflict (00-MASTER-PLAN.md production packs remain valid for story
content, narration scripts, Seeds, and scripture cards — only their photoreal
style blocks are replaced by section 2 above).*
