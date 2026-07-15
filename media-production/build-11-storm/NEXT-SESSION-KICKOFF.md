# #11 Calming the Storm — v3 REDO resume point (Machine A, 2026-07-15)

## State
- **PROMPTS.md**: fully rewritten to FACE LAW v3 (face-shown Jesus, byte-identical
  JESUS LOCK v3 + `REF: jesus-master-ref` on every Jesus shot). **Face gate PASSES.**
- **build.py**: caption-v2 ported in (chunk_caption / caption_layers / spoken_of /
  new build_still). CARD_TEXT changed from the old fear-question to an INVITATION.
- **make_narration.py**: n10 closing card changed to the invitation; `audio/n10.mp3`
  regenerated to match.
- **assets/s1-evening-shore.jpeg**: REGENERATED face-shown v3 (Flow, Nano Banana 2,
  9:16, text-locked, QC-passed — Jesus face matches master, only-Jesus-in-cream). ✅

## What is LEFT (needs a working Flow submit)
Regenerate these **6 Jesus stills** FACE-SHOWN, text-only (no ref attach), from the
prompts already written in PROMPTS.md, then QC each (Read the jpeg: single scene not a
panel, face matches JESUS-MASTER-REF/jesus-face.jpeg, only Jesus in cream, night):
- s4-asleep-in-stern
- s5-carest-thou-not
- s6-peace-be-still
- s7-great-calm
- s8-turned-to-them
- s9-what-manner-of-man

The current on-disk copies of s3–s7 are the OLD face-NEVER Fable-5 regens and MUST be
overwritten (s3 "the storm" has no Jesus and can stay). s8/s9 on disk are old
face-never too.

Then: `python3 build.py` (already caption-v2 + invitation card), QC 3–4 frames, tick
**Built** in QUEUE row 11 + note "v3 REDONE 2026-07-15", add to gen_site_index if not
present, commit the 6 stills + mp4 + QUEUE + index.html, push.

## BLOCKER that stopped this session (READ before touching Flow)
Flow's composer **contenteditable DIV does not register CDP-typed or JS-injected text
with React** in the claude-in-chrome environment on this machine: the `arrow_forward`
submit stays `aria-disabled="true"`, and a submit fires "Prompt must be provided".
Tried and FAILED: `type` action, JS `innerText`, native textarea value-setter +
`input` event, `execCommand('insertText')` on the focused div, physical space+backspace
nudge (React reverted the box to its empty controlled value, len→30). s1 generated only
as a fluke on the very first fresh-load interaction. Per the anti-spin order I stopped
after exhausting these. **Next attempt: either (a) a human pastes the 6 prompts into
the already-logged-in Flow window, or (b) find the React fiber/onChange the composer
actually listens to and dispatch through it.** Do NOT blind-retry the same submit path.
