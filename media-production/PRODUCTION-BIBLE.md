# MBM PRODUCTION BIBLE — The Permanent Law for Making All 200 Videos

> **READ THIS BEFORE TOUCHING ANY VIDEO WORK. EVERY SESSION. EVERY AI. EVERY PLATFORM.**
> Cameron explained this system once (2026-07-08) and never has to explain it again.
> Any AI helping with MBM media reads this file first and follows it exactly.
> Cameron's job: watch finished videos and say yes or no. That's it.
> The AI's job: everything else — prompting, generating, reviewing, assembling, reporting.
> Cameron NEVER writes prompts, never edits clips, never hunts for errors. If the AI
> finds itself asking Cameron to do any of that, the AI is doing it wrong.

> # 🛑 THE #1 LAW ABOVE ALL OTHERS — NEVER PROMPT JESUS'S FACE (Cameron, 2026-07-11)
> **We do not know what Jesus looked like. No AI helping make these videos may ever
> prompt Google Flow for a still or clip that CONSTRUCTS, reveals, or fixes his face.**
> Every story that invents a face — and a DIFFERENT face each time — pulls the viewer
> onto the artwork instead of the story, and putting a made-up face on the Lord is not
> good worship. He is kept a **mystery figure**: a real, warm, MIDDLE EASTERN human
> presence (never white) seen **from BEHIND, OVER-THE-SHOULDER, or AT A DISTANCE** — you
> see the person, you never see his face. This is not hard for the model to do; it is the
> single most important thing to get right, and it is the thing that keeps getting done
> wrong and wasting Cameron's credits three machines over. Other characters DO show faces
> (kept consistent within a story). Only Jesus's face is withheld — always.
> **Before spending ONE Flow credit, every prompt sheet must PASS the mechanical face gate:**
> `python3 media-production/jesus_face_gate.py --dir <build-folder>` (exit 0 = safe).
> A prompt sheet that fails the gate is not allowed near Flow. Full rule: §1 "The
> Standing Laws" → "How Jesus is depicted."

---

## 0. THE THREE OPERATING LAWS FOR EVERY CLAUDE ON EVERY COMPUTER (Cameron, 2026-07-10 — read before ANY video work)

Cameron runs multiple Claude desktop apps on multiple computers. These three laws
bind every one of them, every session, before a single credit is spent:

**LAW A — One project, different videos, never a collision.**
All Claudes work THE SAME project (the 200-video corpus) but each works a
DIFFERENT video. Before starting ANY video work: (1) `git pull` first, always —
another machine may have moved the board; (2) open
[`VIDEO-ASSIGNMENTS.md`](./VIDEO-ASSIGNMENTS.md) in this folder; (3) if a video
is marked CLAIMED or DONE, do not touch it — pick the lowest-numbered UNCLAIMED
video, mark it CLAIMED with the date and machine, commit and push that claim
IMMEDIATELY (before generating anything) so every other computer sees it. Never
work an unclaimed video, never work someone else's claim, never regenerate
assets for a video another machine owns. If the pull shows your intended video
was just claimed elsewhere, take the next one.

**LAW B — Jesus's FACE is NEVER prompted or shown. He is a real, warm, Middle Eastern human figure seen only from behind / over-the-shoulder / at a distance. (Cameron, 2026-07-11.)**
This is the single most important media law and the one that keeps getting broken
across all three machines. **We do not know what Jesus looked like, so no prompt may
ever build, reveal, or fix his face** — not frontal, not three-quarter, not a profile,
not "his face soft and warm," not eyes/cheek/jaw/mouth. Every invented face — different
in every story — pulls the viewer onto the artwork and is not good worship.
He is NOT a hooded void, black cutout, or "Assassin's Creed" ghost — he IS a real,
painted human PRESENCE, warm MIDDLE EASTERN tan/olive-brown skin (NEVER white/Caucasian),
and his hands and hair may show. The camera simply NEVER renders his face. Hide it by
ANGLE only: from behind, over-the-shoulder (camera behind HIM, the people filling the
frame looking at him), or true distance; partial framing (a sleeve, a hem, a reaching
hand) is welcome; a cold full-back is a last resort, never in a beat where he acts
toward someone. NEVER hide the face with light/glow. Other characters DO show consistent
faces within a story — only Jesus's face is withheld. **Mechanical gate before any
credit:** `python3 media-production/jesus_face_gate.py --dir <build-folder>` must exit 0.
The full rule set is §1 "The Standing Laws"; any Claude that has not read it is not
allowed to write a prompt, and no prompt sheet goes to Flow until the face gate passes.

**LAW C — Never hold Cameron's computer hostage.**
The browser automation moves the real mouse and steals window focus. Cameron
works on the same machines. So: (1) ANNOUNCE each burst of Chrome activity in
the message right before starting it — then START IMMEDIATELY. Do NOT stop and
wait for permission, do NOT ask "say go" — Cameron's standing instruction
(2026-07-10) is that once he has set work in motion, asking again is the
failure. The announcement exists only so he knows his mouse may move; his
protection is rule (4): any message from him stops the browser instantly;
(2) keep bursts SHORT and batched — queue up everything (prompts written, files
prepared, QC scripts ready) BEFORE touching Chrome, then do the clicks in one
tight announced window and get out; (3) between bursts, do all work (writing,
QC on downloaded files, audio, assembly, git) in the terminal/files only — those
never touch his mouse or screen; (4) if Cameron says he is using the computer,
or sends ANY message mid-burst, STOP the browser work immediately and wait;
(5) long renders are Flow's job — never sit in the browser waiting; close out,
work elsewhere, come back in the next announced burst.

**LAW D — Run the whole video to completion; never stop mid-production to check
in (Cameron, 2026-07-11).** Once Cameron has set a video in motion, the AI does
the ENTIRE job end to end — every still, every motion clip, narration, assembly,
QC — and presents ONE finished video. Do NOT stop partway to report progress,
ask "want me to keep going?", or wait for a nudge. Stopping to ask a question
Cameron has already answered ("go") is itself the failure. The ONLY two reasons
to stop are: (1) the video is DONE and ready to show him, or (2) a genuine
blocker the AI truly cannot resolve itself and must ask about — a real question,
not a permission check. Progress updates are given WHILE continuing to work,
never as a reason to halt. (This does NOT override Law C: if Cameron himself
sends any message, still yield the browser instantly — that is HIS interrupt,
not the AI volunteering to stop.)

**LAW E — PHASE 1 IS STILLS-ONLY: NO AI-animated clips for now (Cameron,
2026-07-11 — this REVERSES the earlier LAW E that required motion clips in
every video).** Cameron's directive: every one of the 200 videos is produced
as narrated STILLS — beautiful painted pictures with slow Ken Burns drift —
plus narration, serif captions, the KJV verse card, and the closing question
card, and **NO Veo/Flow motion clips at all**, for now. WHY: the animated clips
are where nearly every error and every hours-long rework has come from (a mat
that rolls itself untouched, a figure rendered as a giant, extra limbs, the
storm redos) — and each clip costs 10 shared credits, while a still costs 0 and
regenerates in seconds. Stills-only = faster videos, near-zero rework, no credit
burn on motion. The goal is to get all 200 done as narrated stills FIRST.
**PHASE 2 (later, only when Cameron says so):** go back through the finished
library and drop animated clips into ONLY the specific beats whose motion the
story genuinely needs — "we will plan on going back through later to have the
AI-made videos placed where they are needed." Until then, a delivery containing
any AI-animated clip is OUT OF SPEC. The Story-Fit Rule's clip counts and the
"money moment" clip guidance in §3 are SUSPENDED for Phase 1 — treat EVERY story
as all-stills. (Videos already delivered with clips keep them; every new or
redone build from 2026-07-11 on is stills-only, including #13 through-the-roof,
whose one remaining clip is being replaced with a still.)

**LAW F — STANDING AUTHORIZATION: never stop to ask for permission you already have
(Cameron, 2026-07-11).** When Cameron has set video work in motion — a claim, an
assignment, or a redo he told you to do — spending Flow credits and running announced
Chrome bursts are ALREADY approved. Do NOT stop to ask "can I spend credits?", "should I
use Chrome?", "is this okay?", or any variation. That approval is standing; asking again
for it is itself the failure (Cameron: "what a dumb question... I need a rule to keep you
from stopping for dumb questions"). Announce the Chrome burst (so he knows his mouse may
move) and START — do not wait for a "go." The ONLY things that may stop you: (1) the work
is DONE, or (2) a genuine TECHNICAL blocker you cannot resolve yourself (e.g. Chrome is
not connected to this machine, a file is missing) — reported with the specific reason and
what you need, never as a permission check. A question Cameron has already answered ("yes,
do it") must never be re-asked.

Wasted credits are wasted money. A Claude that generates before reading this
file and §1, or that collides with another machine's video, is burning
Cameron's credits. Read first, claim first, announce first — then work.

---

## 1. The Mission (unchanged, forever)

Every video exists to show one thing: **Jesus is good.** Story-first, scripture-true,
never argumentative, never preachy. The Jesus Method rules in CLAUDE.md / AGENT-RULES.md
govern all content. The Two-Voice Law applies: narrator speaks modern; Jesus speaks
ONLY exact KJV words. **Jesus's FACE is NEVER shown or prompted** — he is a real, warm,
MIDDLE EASTERN human figure (hands and hair may show, never white) seen only from
behind / over-the-shoulder / at a distance, kept a mystery because we do not know his
face — but still a real, warm, painted human (Middle Eastern hands and hair may show,
never white, never a hooded void). Full detail in §1 "The Standing Laws."
The BOM law holds: these 200 videos stay MILK.

**The Voice Law (Cameron, 2026-07-07 — permanent):** The Jesus voice is AMERICAN,
never British — he was not British. Current voices (edge-tts, placeholders until
Cameron locks finals): narrator `en-US-AndrewNeural`, Jesus
`en-US-ChristopherNeural`. Any future voice change still obeys: American, warm,
low, unhurried, same Jesus voice across all 200 videos.
**NEVER use a "Multilingual" voice model (Cameron, 2026-07-08):** the
`en-US-AndrewMultilingualNeural` narrator drifted into foreign-sounding accents
on ordinary English words (caught on video #6). Plain US models only.

**The Ear-Check Law (Cameron, 2026-07-08 — permanent):** Cameron must never be
the one who catches broken audio. After EVERY narration generation, run the
speech-to-text ear-check (`qc_narration.py`, first built in build-06-two-sons):
it transcribes every mp3 and diffs it word-for-word against the script. Any
segment under 0.93 match is regenerated (reworded if needed) BEFORE assembly.
No video is assembled, let alone shown to Cameron, with unverified narration.
(2026-07-09, video #7: the QC tool ITSELF had two bugs — SequenceMatcher
autojunk collapses long character-string comparisons (a 99% match scored
0.11), and whisper's spelling of homophones/numbers ("knight"/"night",
"5 000"/"five thousand") is not an audio defect. Fixed in
build-07-peter-water/qc_narration.py: word-list comparison with
autojunk=False + an EQUIV normalization table. Copy THAT version forward.)

**The No-Dead-Air Law (Cameron, 2026-07-08 — permanent):** The narrator carries
the story through EVERY scene. No silent "visual beats" — a mid-video stretch
without narration reads as broken to viewers ("it just stops talking"). Verify
with `silencedetect` (no gap >2.5s between first word and last); the only
allowed silences are a short breath before the closing card and the card's tail.

**The Translation Law (Cameron, 2026-07-08 — permanent):** After the Jesus
voice speaks a KJV line, the narrator NEVER re-quotes or echoes the KJV words.
He gives only the plain modern meaning ("He was asking: which of the two did
what his father wanted?"). Jesus's words belong to Jesus alone.

**The Readable-Card Law (Cameron, 2026-07-08):** The closing question card is
held long enough to read comfortably (~13s) AND read aloud by the narrator,
gently. Never cut a text card before a slow reader finishes it.

**The Self-Revision Law (Cameron, 2026-07-08 — permanent; video #6 was the
lesson):** Video #6 took FIVE revisions with Cameron catching the problems
himself. That must never happen again. Before ANY video is presented to
Cameron, the AI runs the complete revision loop itself, as many passes as it
takes:
1. Re-read this entire file and apply EVERY law — they all bind every video,
   not just the one that taught the lesson.
2. Ear-check every narration segment (transcribe + diff against the script).
3. Silence-scan the full mix — no dead air over 2.5s in the spoken body.
4. Frame-strip the full video — every caption on the right scene, KJV in
   cream italic, characters on-model, style painted not cartoon.
5. Watch it as a stranger would: does the story flow start to finish with no
   confusing scene? Would a slow reader finish every card? Does anything look
   AI-weird (things appearing or vanishing, extra objects, odd pacing)?
6. Fix everything found and loop again until a full pass finds NOTHING.
Cameron sees a video ONCE, for the final yes. He is the approver, not the QC
department. Revisions are the AI's job.

**The Full-Story Law (Cameron, 2026-07-07):** Never flatten a story to its
headline moment. Include the surrounding humanity that shows he actually cared —
e.g. for the cloak story: he was already on his way to Jairus's dying daughter,
the crowd made one sick woman nearly invisible, he FELT power go out of him,
asked "Who touched my clothes?" (KJV Mark 5:30), was questioned by his own
disciples, ignored them, and kept looking until he found her. Backstory and
resistance beats make the stop mean something.

**The Approval Law (Cameron, 2026-07-08):** Cameron gives the FINAL yes on
every video — nothing ships without it. Leighton (Cameron's daughter) is a
crew operator: she runs day shifts with the AI, reacts to storyboards and
assets, and can mark a finished video "READY FOR DAD," after which she and
the AI continue to the next story in the queue. Shift handoffs are spoken in
chat: "Leighton is working on it for the day" / "this is cameron again." The
crew's full operating manual is **CREW-GUIDE.md** — any AI doing media work
reads it alongside this file. The AI also teaches while it works (plain-word
explanations, prompts shown before submitting) so the crew grows toward
running Flow themselves with the AI in prompt-only mode.

**The Feedback-Study Law (Cameron, 2026-07-08):** Video #1 v2 is approved to
HOLD as-is and gather real viewer comments. Known self-critique to beat in
future videos: it reads as AI-made and paces slow. Every batch of viewer
comments gets studied and distilled into new QC lines in section 5. Current
improvement targets: (a) tighten pacing — trim dead air between beats, let
strong images breathe less when the narration has already moved; (b) chase
the human feel — vary shot rhythm, favor faces/hands/small human details of
the PEOPLE (never Jesus), let emotion land in the pictures, not just the
words. Nothing here overrides the sacred pause before Jesus's KJV words.

## The Standing Laws — how every video is made

> These are the rules, stated as they are NOW. They used to be a growing numbered
> list, "Correction #1" through "Correction #18," where each new one patched or
> REVERSED an earlier one (#16 reversed #13 and #14, then #18 reversed the face part
> of #16). That changelog format made the rules contradict each other and is exactly
> why the same mistakes kept happening across three machines. The numbering is gone.
> THIS is the single current rulebook. The old numbered history is kept in
> [`CORRECTIONS-HISTORY.md`](./CORRECTIONS-HISTORY.md) for provenance only and is NOT
> law. Every rule below was paid for by a rejected video.

### How Jesus is depicted — the first law, above all others

- **His face is never shown or prompted.** We do not know what Jesus looked like. No
  prompt may build, reveal, or fix his face — no face, eyes, gaze, expression, smile,
  cheek, jaw, nose, mouth, brow, no portrait, no close-up, no "three-quarter" view of
  him, no frontal or side profile. A constructed face — a different one in every story
  — makes people stare at the artwork instead of the story, and putting a made-up face
  on the Lord is not good worship. Enforced mechanically by the face gate (below).
- **He is a real, warm, Middle Eastern man — not a shadow.** He is a painted human
  PRESENCE in the scene: warm Middle Eastern tan / olive-brown skin (NEVER white,
  Caucasian, or European), his hands and hair may show, his robe is real cloth. He is
  NOT a hooded black void, NOT a solid cutout, NOT a robe-and-posture "Assassin's
  Creed" ghost. The answer to "no white Jesus" is that he is unmistakably Middle
  Eastern — not that he is hidden as a silhouette.
- **THE JESUS LOOK STANDARD — the SAME in every scene and every video (Cameron,
  2026-07-11).** He is a FIXED character: his hair and clothing never change from shot
  to shot or story to story. (The #11 storm kept flipping his hair short↔long and his
  robe kept changing — once to a white fur/fleece look — which breaks the spell.
  "We know what he looked like; it's not that hard — standardize it for all the
  videos.") Paste this identical description into EVERY Jesus prompt in EVERY video:
  - **HAIR: LONG, dark brown-black, falling past the shoulders. NEVER short, never
    changing length.**
  - **CLOTHING: one plain, undyed off-white / cream WOOL robe — a simple first-century
    Judean man's tunic with a plain mantle, the SAME garment every time. NOT a white
    fur or fleece, NOT a changing color, cut, or trim.**
  - **SKIN: warm Middle Eastern olive-brown. Never white or pale.**
  - **CAMERA: from BEHIND / the back of his head is the DEFAULT.** Cameron, 2026-07-11:
    a side profile still lets you make out his face — so prefer simply from behind. No
    three-quarter or side angle that lets his facial features be read.
  - **NO glow, halo, or rim-light.**
  Treat this like the wardrobe-lock law, but project-wide: the same Jesus, painted the
  same way, across all 200 videos.
- **THE CREAM ROBE BELONGS TO JESUS ALONE (Cameron's pipeline, 2026-07-13 — video #40,
  caught before delivery).** The Jesus Look Standard identifies him by ONE signature: long
  dark hair past the shoulders + a plain undyed off-white/cream wool robe. That signature
  only works if nobody else wears it. In #40 s1 the prompt correctly dressed the disciples
  in "oatmeal, dun and faded brown" — but the model painted the disciple stepping forward
  in CREAM, bearded, centered, hand open in a teaching posture. That is the Jesus silhouette,
  and a viewer glancing at the frame reads HIM as Jesus and believes he is seeing the Lord's
  face. The face law is not satisfied by a technicality; its whole purpose is that no viewer
  is ever pulled onto a constructed face of Christ. So: **every prompt must dress all other
  characters in colors that are NOT off-white / cream / undyed white** — oatmeal, dun, brown,
  ochre, grey, blue, maroon, olive are all fine. State the other characters' colors
  positively and explicitly in every prompt where Jesus also appears, and QC every frame by
  asking: "could anyone in this picture be mistaken for him?" If yes, regenerate.

- **Hide the face by the CAMERA ANGLE, never by light.** The camera sits BEHIND him,
  OVER his shoulder (the reliable default: camera behind him, the people filling the
  frame looking past the camera straight at him), or at true DISTANCE (a far figure
  whose face can't be read). First-person or third-person "from well behind him" is
  exactly right. Never a rim-light, halo, or glow that outlines his head — that
  highlights him, the opposite of the goal, and is banned.
- **Don't lean on his cold back.** A full back-of-figure reads as Jesus turning AWAY
  from the person, especially in an emotional beat. Prefer over-the-shoulder, distance,
  and partial framing — a sleeve entering the frame, a hem, feet at the edge, a shadow
  falling across the person, light from off-frame. A full back is the last resort,
  never in a beat where he is acting toward someone.
- **He is a whole person in the scene, not a floating body part.** When people respond
  to him — worship, gratitude, awe, companionship — he is present as a full figure
  beside them (face hidden by angle), never a disembodied hand or forearm drifting in
  from off-frame.
- **His reaching hand is right for a touch or rescue.** When the scripture's action IS
  physical rescue or touch (pulling Peter from the water), show the reach itself — a
  hand and forearm in a wool sleeve extending toward the person — face still never
  shown.
- **Orient him toward the person.** When someone comes toward Jesus, he faces them with
  open posture and light pouring toward them — never turned away. Hide the face with
  distance, a light dissolve, or framing, not a cold turned back.

### Compose every scene around the PEOPLE

- **The picture is the people.** In any reaction, witness, or crowd scene, build the
  frame around the responders — their faces, their attention, their leaning-in. Jesus
  is present but de-emphasized (behind, soft, smaller, never centered, never the
  compositional star), placed exactly where every gaze in the frame converges.
- **Every gaze converges on him.** Never a small detached rear-view Jesus off at the
  frame edge while the crowd looks at nothing — every face in frame is visibly turned
  toward him. Over-the-shoulder framing makes this automatic and is the safe default.
- **Witnesses react TO the moment, not at the camera.** Stage witnesses on the far side
  of the scene, faces and bodies reacting to the Jesus-and-person moment — never
  surprised faces aimed straight at the viewer.
- **Enough pictures to carry the story.** Because Phase 1 is pictures only (see
  below), give each beat its own strong picture — never lean on one image to cover a
  long stretch of narration. Every picture must be able to hold the listener's
  attention on its own.

### Tell the story true

- **The whole story, through the final verse.** Never flatten a parable to its headline
  moment; include the surrounding humanity and every character Jesus put in it — the
  waiting father, the older brother, the backstory, the resistance. Half a parable
  sells half the point.
- **Action reads right at a glance.** QC every figure by asking "what does this person
  appear to be DOING?" — if it isn't the story beat, reroll. Bailing throws water OUT
  over the gunwale; ropes connect to rigging inside the boat; nothing reads backwards
  or absurd.
- **Lighting matches the scripture's time of day.** Mark 4:35 is night — limited light,
  moon, stars, lightning, never a sunrise or sunset. Say the time of day explicitly in
  the prompt and reject golden-hour skies in a night story.
- **Figures stay where the scripture puts them.** Everyone is visibly INSIDE the boat —
  deck under their feet, gunwale wrapping around them; nobody stands on the water
  unless the scripture puts them there.
- **A physical trait that IS the story must read — calibrated, never caricatured.**
  State the trait relative to other visible people ("the top of his head level with the
  men's shoulders"), put other figures in solo shots for scale, and QC that it reads
  instantly. Never exaggerate into caricature or dwarfism — a short man is a
  normal-proportioned short adult, kept dignified.
- **Count the anatomy in every frame.** On the QC zoom of every still and every sampled
  clip frame, literally count 2 arms, 2 hands, 5 fingers where legible, 2 legs, 2 feet,
  1 head, and check every limb connects to the right body (climbing, crowd, and table
  scenes hide extra limbs). Any wrong count = regenerate.
- **No fake tears.** No painted teardrop beads sitting on a cheek — emotion lives in the
  eyes, brows, and mouth of the PEOPLE; wet shining eyes at most.
- **Wardrobe and props lock and hold.** Every lock item — cloak color and cut, purse
  type and position, sleeves, key props — goes into the description of every prompt the
  character appears in, and every clip is frame-checked against the banked stills so
  nothing changes mid-story.

### Phase 1: pictures and narration ONLY — no AI motion clips (yet)

**Right now, every video is a slideshow of painted pictures with one narration over
the top — and NO AI-animated (Veo/Flow) motion clips at all.** (Cameron, 2026-07-11 —
this is the current phase; it matches §0 Law E.)

- **Why.** The AI-animated clips are where nearly every error and every hours-long
  rework has come from, and each clip burns shared credits, while a still costs nothing
  and regenerates in seconds. Pictures-only = faster, near-zero rework, no credit burn.
  The goal is to get ALL 200 stories made as picture-and-narration videos FIRST.
- **What a video is.** Strong painted pictures (with a slow, gentle Ken Burns drift in
  assembly — that drift is not an AI clip), narration, serif captions, the KJV verse
  card, and the closing question card. Nothing moves except the gentle drift.
- **Every picture earns its place.** Since motion can't carry a beat anymore, each
  picture must be striking enough to hold the listener on its own. Give every important
  beat its own picture rather than stretching one image over a long stretch of narration.
- **Pull the clips out of what's already built.** Videos already assembled with AI
  motion clips (the delivered ones) get those clips REMOVED and are rebuilt as one
  narration over pictures only.
- **Phase 2, later, only when Cameron says so.** Go back through the finished library
  and add AI motion to the specific beats whose motion the story genuinely needs — piece
  by piece, only when the clip is actually good. Until then, any delivery containing an
  AI-animated clip is out of spec.

### How "done" is defined (nothing skips these)

- **Right the first time.** Every known failure is checked ON PAPER in the production
  pack before a single credit is spent (the pre-flight, §4b). Fixing a script is free;
  fixing a built video costs credits and trust.
- **The face gate is mandatory.** Before any Flow credit:
  `python3 media-production/jesus_face_gate.py --dir <build-folder>` must exit 0. It
  fails any Jesus-face language and any Jesus prompt with no face-hiding camera cue. No
  prompt sheet reaches Flow until it passes; when a new face-leaking phrase slips past
  it, add that phrase to the gate in the same session.
- **The AI runs the full revision loop before Cameron ever sees the video** — re-read
  every law, ear-check the narration against the script, silence-scan the mix,
  frame-strip the whole video, and watch it as a stranger — looping until a full pass
  finds nothing. Cameron sees a video once, for the final yes. He is the approver, not
  the QC department.
- **Run to completion.** Once Cameron says go, build the entire video and present it
  once; never stop mid-production to ask "keep going?" The only reasons to stop are
  "it's done" or a genuine blocker. (If Cameron himself sends any message, still yield
  the browser instantly — that is his interrupt.)
- **Name the file for its scripture** — `book-chapter_story-name.mp4`.

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

> ⛔ **SUSPENDED FOR PHASE 1 (Cameron, 2026-07-11).** See LAW E in §0: right now
> every video is STILLS-ONLY — no AI-animated clips. The clip guidance in this
> section (money moments, Story-Fit clip counts, the motion-budget ceiling)
> applies to PHASE 2 only, when Cameron reopens clips. Build all-stills until then.

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

## 4b. RIGHT-FIRST-TIME PRE-FLIGHT (Cameron, 2026-07-08 — check the PLAN before generating anything)

> Cameron's directive: stop relying on revisions to reach perfect. The Self-Revision
> Law is the safety net, not the method. The method is this pre-flight: every known
> failure from past videos is checked ON PAPER, in the production pack, BEFORE any
> credit is spent or any assembly is run. Fixing a script costs nothing; fixing a
> built video costs time, credits, and trust.

**Before generating ANY audio (check the written narration script):**
- [ ] FULL-STORY check: read the parable's scripture END-TO-END against the
      beat map — every scene and every character Jesus put in the story is in
      the storyboard, through the FINAL verse. Half a parable sells half the
      point (added 2026-07-09, video #2: first cut ended at the feast and
      omitted the older brother — the entire half aimed at the religious men
      the story was told to answer. Cameron caught it, not the loop.)
- [ ] Every scene in the storyboard has a narration line — map beat-by-beat; no
      silent "visual beats" exist anywhere in the plan (No-Dead-Air Law)
- [ ] No narrator line quotes or echoes KJV wording — plain modern meaning only
      (Translation Law); Jesus lines are exact KJV, verified against the passage
- [ ] Read every line ALOUD in your head for TTS traps: clipped phrases
      ("he just went to work"), odd contractions, tongue-twisters — reword now
- [ ] NUMBER / HOMOPHONE STRESS (added 2026-07-11, Cameron — the placeholder
      voice read a sentence-initial "Four" flat, like the unstressed "for").
      The neural voice under-stresses short number words and function-word
      homophones ("four"/"for", "two"/"to", "one"/"won") when they lead a
      sentence. Don't open a sentence with a bare number; word it so the number
      lands as a stressed count — "It took four men to carry him," "There were
      four of them" — not "Four men came." Ear-check specifically that every
      number reads as the number, not its homophone.
- [ ] Voices are `en-US-AndrewNeural` + `en-US-ChristopherNeural` — no
      Multilingual model anywhere (Voice Law)
- [ ] The closing card text is written to be READ ALOUD by the narrator and the
      card is scheduled ~13s (Readable-Card Law)
- [ ] CLARITY / WHY-LAW (added 2026-07-09, video #3: Cameron — "it's very
      confusing, I don't get the point... explain it better, why Jesus would
      do some things"): the script must EXPLAIN, not just narrate. Every
      surprising action gets its WHY in plain words (why the crowd hated him,
      why the act was shocking, why Jesus's response broke the rules). Test:
      a viewer with zero Bible background must be able to say what the point
      was in one sentence.
- [ ] STUDY-GEM TIDBITS (same session): weave in the small insights people
      collect in scripture study — cultural context, word meanings, law-of-
      Moses echoes (e.g. fourfold restitution, "son of Abraham"), and clear
      up famous mix-ups (e.g. Zacchaeus vs Matthew — both tax collectors,
      different men). Small tidbits, where needed, so people can connect —
      never lectures, never breaking the story's flow.

**Before generating ANY image or clip (check the written prompts):**
- [ ] 🛑 FACE GATE PASSES (the face law): run
      `python3 media-production/jesus_face_gate.py --dir <build-folder>` and confirm
      it exits 0 with "RESULT: PASS". Every FAIL (Jesus + face language) and every
      WARN (Jesus staged with no face-hiding camera cue) is a hard stop — rewrite
      the prompt so Jesus is from behind / over-the-shoulder / at a distance with NO
      face words, then re-run until clean. NO Flow credit is spent until this passes.
- [ ] Master Style Block byte-identical, zero added style words (§5b ban #2)
- [ ] No "NEGATIVE PROMPT:" list; every constraint stated positively — exact
      counts, exact emptiness, "one single figure and only him" (§5b ban #1)
- [ ] Character/wardrobe locks and prop locks written into EVERY prompt for
      every scene the character/prop appears in (wardrobe drift, lamp lesson)
- [ ] No beat asks the model for an "AI tell": instant physical changes (sweat
      appearing), objects popping in, anything materializing — plan the beat so
      the risky detail simply isn't requested (video #6 sweat lesson)
- [ ] MUST NEVER SHOW items from the scripture card confirmed against each prompt
- [ ] RELATIVE-PHYSICALITY LOCK (added 2026-07-09, video #3: Cameron —
      "make sure the video actually portrays him as short the entire time,
      because sometimes the pictures were tall... it doesn't make a lot of
      sense"): when a physical trait IS the story (Zacchaeus short, blind
      Bartimaeus's eyes, the withered hand), every prompt must state it
      RELATIVE to other visible people ("barely chest-high to the adults
      around him"), solo shots of that character must include other figures
      for scale, and the QC zoom on every frame verifies the trait reads
      instantly. A lock written in text but invisible in the picture is a
      broken lock.
- [ ] PHYSICALITY CALIBRATION (added 2026-07-09, video #3 v2 rejection:
      Cameron — "you took the short man too far and he looks like a midget
      everywhere and is kind of demeaning. it's too much"): a relative trait
      must be CALIBRATED, never exaggerated into caricature. Short means a
      short ADULT with completely normal adult proportions — roughly a head
      to head-and-shoulders below the people around him, about shoulder-high
      to them — NEVER dwarfism, child-sized, or stylized-tiny. Prompts must
      state the calibration positively ("a short grown man of normal adult
      build, the top of his head level with the shoulders of the men beside
      him") and the QC zoom must confirm BOTH that the trait reads AND that
      it stays dignified. Exaggerating a person's body for legibility is
      demeaning and breaks the Gospel Principles; the fix for "trait doesn't
      read" is scale references in frame, never a bigger distortion.
- [ ] ANATOMY-COUNT QC (added 2026-07-09, video #3 v2 rejection: Cameron —
      "he's got three feet in the tree he climbed. these are simple things
      you should be able to watch for"): on the QC zoom of EVERY still and
      every sampled motion frame, literally COUNT the anatomy of every
      visible figure — 2 arms, 2 hands, 5 fingers where fingers are legible,
      2 legs, 2 feet, 1 head — and check that limbs connect to the right
      bodies (climbing/crowd/table scenes are the highest risk: tangled poses
      and overlapping figures are where extra limbs hide). Any wrong count is
      an automatic regenerate, no matter how good the rest of the frame is.
      This count is a named line item in the QC pass, not an implied one.

**Before assembly (check the timing math):**
- [ ] Measure real durations of every generated audio file; recompute all
      offsets from measurements, never from estimates
- [ ] On-paper silence map: no gap >2.5s between segments in the spoken body
- [ ] Measure the silent TAIL inside each mp3 (TTS files can carry ~1s+ of
      trailing silence); compute every breath/gap from the SPOKEN end, not the
      file end — verify with silencedetect after the mix (added 2026-07-08,
      video #2: j1's 1.2s internal tail stretched a planned 2s breath to 3.5s)
- [ ] Music bed scheduled to reach full silence BEFORE the peak KJV line

**Assembly craft laws (added 2026-07-09 — Cameron: "it just seems like a video
made by ai, it glitches" — every one of these was a real, found defect):**
- [ ] ANTI-SHIMMER: never render zoompan straight at delivery resolution.
      zoompan rounds its crop to whole pixels each frame — at 1080 that
      stepping is visible on slow drifts (the "AI slideshow" jitter). Render
      the move supersampled (≥4x input, 2x output) and lanczos down to
      delivery size so steps land on quarter-pixels. Measured fix: frame-to-
      frame motion variation halved.
- [ ] CAPTION FADES: captions never pop in or out at a cut. Render each
      caption (text + box + shadow) on its own transparent RGBA layer,
      alpha-fade 0.5s in and 0.5s out (gone ~0.1s before the cut), overlay.
- [ ] ENCODE: intermediates near-lossless (crf 16); final pass is the ONLY
      lossy generation — preset veryslow, start crf 21, step up only if the
      <25MB law demands it. Never starve the bitrate to fit (1050k caused
      visible blocking on video #2).
- [ ] LOUDNESS: measure the final mix (EBU R128) and deliver ≈ -15 LUFS via
      static gain + true-peak limiter. Quiet audio reads as amateur.
- [ ] MUSIC BED: no bare sine waves — every voice a slightly detuned pair
      (natural slow beating) through a soft room echo. And no long bone-dry
      stretches unless sacred quiet IS the point of that moment.

**Found by the self-revision loop on video #39 (added 2026-07-13) — three checks
that were missing, each one a real defect that reached the built video:**
- [ ] 🛑 PROVE THE QC TOOL CAN STILL FAIL. `silencedetect`, `volumedetect` and
      `ebur128` all log at ffmpeg's INFO level, so running them with
      `ffmpeg -v error` prints NOTHING — which reads exactly like a clean pass.
      On #39 that false pass hid two real dead-air violations. NEVER trust a QC
      command that returns no output until you have proven it can still report
      something (loosen the threshold and watch it fire). A silent checker is
      presumed broken, not passing.
- [ ] TIMING OFF THE SPOKEN END, ENFORCED IN CODE. The rule above (2026-07-08,
      video #2) was on the list and still got missed, because build.py measured
      `dur_of(mp3)` — the FILE end. The TTS tail is ~0.45s on the narrator but
      ~1.3s on the Jesus voice, so both KJV pauses silently grew past the 2.5s
      law. Don't just measure the tail — make the build FAIL on a >2.5s spoken
      gap so it cannot ship. (build-39/build.py `spoken_of()` is the pattern to
      copy: trim trailing silence with `areverse,silenceremove,areverse`, time
      every beat off THAT, and raise SystemExit if any gap exceeds the law.)
- [ ] CAPTION CONTRAST IS A FUNCTION OF THE STORY'S LIGHT. The caption box
      (`black@0.40`) was tuned on NIGHT stories. On a bright-daylight story —
      #39 is the temple at the morning hour of prayer, pale stone in every
      frame — white text on that light box washes out. Daylight stories use
      `black@0.58`. Check legibility on a full-res frame crop, not a thumbnail.

Only after this pre-flight passes does generation begin. Then the Self-Revision
Law loop runs on the built video — and if the pre-flight was done honestly, that
loop should find nothing. Every time the loop DOES find something, that means a
check is missing from this list: add it, dated, so the next video is right the
first time.

## 5. QC Checklist (every video, before Cameron ever sees it)

- [ ] Every MUST SHOW item from the scripture card appears
- [ ] 🛑 PHASE 1 STILLS-ONLY: the delivery contains NO AI-animated (Veo/Flow) clips —
      only painted pictures with gentle Ken Burns drift + narration (§0 Law E). Any
      already-built video that has clips gets them removed and is rebuilt pictures-only.
- [ ] Zero MUST NEVER SHOW items appear (scrub every image fully)
- [ ] 🛑 FACE GATE passed on the prompt sheet before generation; and in the FINISHED
      render, Jesus's face is never visible in ANY frame at any zoom — audit every
      still and every sampled clip frame. (His Middle Eastern hands and hair MAY show;
      only the FACE is withheld. Other characters' faces are fine and should stay
      consistent within the story.)
- [ ] Style matches the gold-standard reference (palette, texture, tone)
- [ ] No AI text/gibberish baked into any image
- [ ] Narration modern; Jesus voice EXACT KJV only
- [ ] Verse card wording pulled from PAIRING-LIST.md, text fetched not hand-typed
- [ ] Closing question matches the pack's Seed question
- [ ] 9:16, 1080×1920, plays clean start to finish
- [ ] **SCRIPTURE-NAME LAW (Cameron, 2026-07-10):** the final delivered video file is
  named after its place in the Bible — `book-chapter_story-name.mp4` (e.g.
  `john-4_woman-at-the-well.mp4`, `mark-10_rich-young-ruler.mp4`). The filename itself
  teaches the reference. Earlier deliveries get renamed to match; every new build
  delivers under this name from day one.

## 5b. PROMPT FAILURE LOG (banned techniques — every mistake that wasted credits gets written here so no AI repeats it)

**2026-07-08 — The "NEGATIVE PROMPT" cartoon disaster (video #8, Scene 4, 10 credits wasted).**
The clip came back flat-cartoon (big glossy Disney eyes, plastic shading) and clashed
hard with the painted stills around it. Crew verdict: "horrible, way worse." Two causes,
both now BANNED:

1. **NEVER put a "NEGATIVE PROMPT:" list inside a Veo prose prompt.** Veo does not
   honor negative lists. Naming the things you don't want ("two coins", "AI-generated
   look", "3D CGI") puts those words INTO the prompt and can pull them into the video.
   Say what you WANT, positively and only that: "EXACTLY ONE coin — one single coin,
   and only that one coin, in the whole video."
2. **NEVER add or strengthen style words beyond the locked Master Style Block.** Adding
   emphasis like extra "2D animation" wording shoved the output into cartoon land. The
   Master Style Block in section 2 is used byte-identical, every prompt, no additions,
   no paraphrasing. Style drift = automatic redo, so don't invite it.

**2026-07-13 — Video #39: a `REF:` character lock does NOT lock the wardrobe by itself.**
Shot s7 was regenerated with `REF: s4, s6` attached (both showing the tax collector in an
ankle-length, long-sleeved rust robe with a cloth sash) — and Gemini still returned him in a
SHORT-SLEEVED, knee-length tunic with a buckled leather belt. The reference images pin the
FACE reliably; they do not pin the clothes. **Rule: name the garment in the prompt prose —
its length, its sleeves, and how it fastens — in every shot the character appears in, even
when a REF lock is attached.** ("one ANKLE-LENGTH rust-brown robe falling to his sandals,
LONG sleeves to the wrists, a soft cloth sash — no short tunic, no bare knees, no buckled
belt.") Cost: one wasted image. Also caught here: the model happily paints a modern-looking
metal belt buckle if you say "leather belt" — say "cloth sash."

**2026-07-13 — Video #39: check WHICH MODEL gen_stills.py is about to spend money on.**
The first run of the build fired 12 requests at `gemini-2.5-flash-image` and every one came
back `HTTP 429 ... free_tier_requests, limit: 0`, which reads like a dead API key or a
missing billing account. It is neither: that name resolves to a PREVIEW image model that the
tier simply does not carry. `gemini-3-pro-image` — the committed default, and the model the
whole pipeline is tuned for (2K, big enough to supersample the Ken Burns drift) — worked on
the first try. The stale flash default came from a `gen_stills.py` that was replaced by a
newer commit mid-session. **Rule: `git pull --rebase` BEFORE reading the tools you are about
to spend money with (Law A already says pull first — this is why), and if every image 429s
with `limit: 0`, suspect the MODEL before you suspect the key. Prove the key is alive with a
one-line text call; if text works, the key and the billing are fine.**

Standing rule: every future prompt failure that wastes credits gets its own dated entry
here, with the cause and the ban, before any retry is attempted.

## 6. Money & Credits (why this plan is affordable)

- **ACTIVE PLAN (Cameron, 2026-07-08): Google AI Ultra $200 tier = 25,000
  credits/mo.** Bought specifically to produce the corpus at full speed for the
  next month. Use it thoroughly — the constraint is now throughput, not credits.
  Round-the-clock crew shifts (Cameron nights, Leighton days) exist to spend it.
- Stills: 1–2 credits. Veo Fast clip: 10 credits on Ultra.
- Typical video ≈ 25–60 credits. All 200 ≈ ~11,000 credits including retakes —
  the $200 tier covers all 200 in one month with >2x margin. Credits don't roll over.
- The AI reports credit spend in every session log entry so Cameron always knows
  where the month stands. Big-motion stories (3–4 clips) get flagged in the report.

## 7. What Cameron's money is buying (the promise this file enforces)

Same look, same feel, same flow, every video, no matter which AI session makes it —
because the style block is frozen text, the pipeline is frozen steps, the QC list is
frozen checks, and this file is the single source of truth. If any future direction
change is wanted, Cameron says it once, this file gets edited and committed, and the
new law holds from then on. Nothing lives in anyone's memory. Everything lives here.

## 8. Session workflow for any AI picking up media work

1. Read CLAUDE.md chain protocol, START-HERE.md, AGENT-RULES.md — then THIS FILE,
   starting with §0 (the operating laws) and §1 "The Standing Laws" IN FULL.
2. `git pull`, then check SESSION-LOG.md top entry AND VIDEO-ASSIGNMENTS.md.
3. Claim your video on VIDEO-ASSIGNMENTS.md (commit + push the claim) before
   generating anything. Continue the assembly line exactly where it stopped for
   YOUR video only. No re-litigating style or format.
4. Announce every Chrome burst to Cameron before starting it (§0 Law C).
5. End of session: SESSION-LOG.md entry (videos progressed, credits spent/left,
   any QC lessons learned added to section 5), update VIDEO-ASSIGNMENTS.md
   status, commit, push.

---
*Created 2026-07-08 from Cameron's direction. This file outranks any older media doc
where they conflict (00-MASTER-PLAN.md production packs remain valid for story
content, narration scripts, Seeds, and scripture cards — only their photoreal
style blocks are replaced by section 2 above).*
