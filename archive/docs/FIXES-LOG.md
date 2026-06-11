# MBM — Fixes Log
_Append to this file after every fix. Never delete entries._

---

## Format
```
### [DATE] — [ISSUE-ID]: [Short description]
- File(s) changed:
- What was broken:
- What was changed:
- Verified: yes/no
```

---

### 2026-06-10 — ISSUE: Disciple voice, no name leak, member track
- Files: `mobile/src/engine/minister.ts`, `ministry-sim/minister.py` (kept byte-in-sync), `mobile/src/store/useAppStore.ts`, `mobile/src/engine/connect.ts`
- What was broken: (1) The AI named the admin in chat ("Cameron reads these himself") — a real trust failure. (2) The voice was framed as performing AS Jesus ("the truth of a genuinely good God spoken in His own voice") rather than as a disciple pointing TO Him. (3) There was no member track — a Latter-day Saint got the seeker experience (milk-before-meat + human-handoff push) instead of being fed and gently examined. (4) The app silently guessed faith status instead of openly (non-intrusively) confirming it.
- What was changed:
  - Stripped the personal name from all chat-facing copy. `buildHumanOffer()` and the live guidance block now refer only to "a real person"; added an explicit minister-prompt rule never to use a personal name. (Remaining "Cameron" strings are internal comments / the admin email constant — never shown in chat.)
  - Reframed the minister intro + purpose: the AI now ministers "the way one of His disciples would — you POINT TO Him, you repeat what He said and did, you never speak AS Him or perform being Him."
  - Added a MEMBER TRACK section to the minister prompt and a member branch to the live guidance: no milk-before-meat, no human-handoff push; instead go deeper in the scriptures they already hold and ask gentle, non-accusing questions about whether they're living it the way Christ asks.
  - Added open/non-intrusive faith confirmation to Principle 1: don't route in secret — gently, openly ask where someone stands, woven into conversation, never a survey.
  - Fixed a pre-existing whitespace drift between the two prompt files so they are byte-identical again.
- Verified: yes — `minister.ts` and `minister.py` prompts confirmed byte-in-sync (12,447 chars, programmatic compare); `tsc --noEmit` clean for all edited files (only unrelated pre-existing error in `test-profile-screenshot.ts`).

### 2026-06-08 — ISSUE-01: Start-over crash fixed
- Files: `App.js`, `src/screens/FeedScreen.js`
- What was broken: When a user had a saved session, App.js only registered Feed and Journal in the navigator. FeedScreen's "Start over" button tried to navigate to Hook, which didn't exist — crash guaranteed.
- What was changed: App.js now registers Hook and Onboard in both branches of the navigator. Added `onSessionReset` callback passed down to FeedScreen. FeedScreen calls `onSessionReset()` which causes App to re-render with null session, safely transitioning to the Hook screen.
- Verified: yes — scanner passes

### 2026-06-08 — ISSUE-02: RESTORATION content added
- Files: `src/db/seed.js`
- What was broken: Zero RESTORATION tier content. The entire middle of the conversion journey was missing.
- What was changed: Added 15 RESTORATION items in sequence — from "the question that started everything" (Joseph Smith) through Moroni's Promise, all linked to official Church sources. Ordered for someone who believes in Christ but has never heard the Restoration.
- Verified: yes — scanner shows 15 items

### 2026-06-08 — ISSUE-03: more_depth escalation now includes RESTORATION
- Files: `src/engine/router.js`
- What was broken: Escalation path was MILK→BRIDGE→MAINTENANCE, skipping RESTORATION entirely.
- What was changed: Added `ESCALATION_PATH = ['MILK', 'BRIDGE', 'RESTORATION', 'MAINTENANCE']`. `logInteraction` now walks this array by index, escalating to the next tier correctly.
- Verified: yes — scanner passes

### 2026-06-08 — ISSUE-04: LOC reveal now escalates to BRIDGE
- Files: `src/screens/FeedScreen.js`, `src/engine/router.js`
- What was broken: "I want to know more" on the LOC reveal just loaded the next feed item. No tier change. Dead end.
- What was changed: `dismissLOC()` now calls `escalateFeedTag(sessionId, 'BRIDGE')` before loading feed. Added `escalateFeedTag` as a new export in router.js.
- Verified: yes — scanner passes

### 2026-06-08 — ISSUE-05: Journal now accessible to all profiles
- Files: `src/screens/FeedScreen.js`
- What was broken: Journal button only rendered for `profile === 'MEMBER'`.
- What was changed: Removed the profile gate. Journal button always visible in signal bar.
- Verified: yes — scanner passes

### 2026-06-08 — ISSUE-06: positiveCount persisted across re-mounts
- Files: `src/screens/FeedScreen.js`
- What was broken: `positiveCount` was in-memory useState. Reset to 0 every time user left and returned to screen. LOC trigger (requires 3) almost never fired in practice.
- What was changed: Added `POS_COUNT_KEY` AsyncStorage constant. Count saved on every increment, restored on screen mount.
- Verified: yes — scanner passes

### 2026-06-08 — ISSUE-07: Signal actions guarded against null item
- Files: `src/screens/FeedScreen.js`
- What was broken: `handleSignal` used `item?.id ?? 0`, logging content_id=0 when item was null.
- What was changed: `handleSignal` returns early if `!item?.id`.
- Verified: yes — scanner passes

### 2026-06-08 — ISSUE-08: Error handling added to router.js
- Files: `src/engine/router.js`
- What was broken: Every database call had zero try/catch. Any SQLite failure froze the screen silently.
- What was changed: All exported async functions wrapped in try/catch with `console.error` logging. Return safe empty values on failure.
- Verified: yes — scanner passes

### 2026-06-08 — ISSUE-09: Seed versioning implemented
- Files: `src/db/database.js`
- What was broken: Seeding used count-based check (`count < SEED_CONTENT.length`). Adding new seed content would delete manually-added DB content.
- What was changed: Added `app_meta` table. `SEED_VERSION = 2` constant. Only re-seeds when stored version is less than current version. Manually-added content is safe between seed updates.
- Verified: yes — scanner passes

### 2026-06-08 — MISSING-03: SKEPTIC profile included in LOC trigger
- Files: `src/screens/FeedScreen.js`
- What was broken: LOC reveal only triggered for SEEKER and SECULAR. SKEPTIC excluded.
- What was changed: Added `profile === 'SKEPTIC'` to the LOC trigger condition.
- Verified: yes — scanner passes

### 2026-06-09 — OPENER: presence before proclamation (adaptive "He is risen")
- Decision owner: builder (Cameron declined to adjudicate — "use the data + what Jesus would do; that is the app's job, not mine"). Resolves the OPEN DECISION flagged 2026-06-09.
- Evidence: 100+ trials. The cold "He is risen" opener was the single most-repeated criticism. It landed WARMLY on already-believing arrivals (Baptist/Catholic/evangelical all answered "He is risen indeed") but read as a loaded creed to the grieving, secular, burned ex-believer, and skeptic ("telling me what my experience means before you've heard a word"; "walking into sacrament meeting without being warned").
- Scriptural grounding: the risen Christ did NOT proclaim "I am risen" to weeping Mary Magdalene — He met her grief and spoke her name (John 20:15-16); He walked to Emmaus and listened to despair before eyes were opened at the very END (Luke 24:17-31). Presence first; proclamation when it fits. The Hook now leads with Jesus's own invitation to the weary (Matt 11:28) + "Come and see" (John 1:46).
- Files (all in sync): ministry-sim/minister.py build_minister_opening(opening_story, arrives_in_faith) — default cold open = pure presence, NO creed; arrives_in_faith=True keeps the resurrection greeting as shared celebration. personas.py — added arrives_in_faith flag (True: calvinist/baptist/catholic/evangelical). run_sim.py — passes persona.arrives_in_faith. mobile/src/screens/OnboardScreen.tsx sanctuary headline "He Is Risen." -> "You are welcome here." + presence body. mobile/src/screens/HookScreen.tsx "He Is Risen." -> "Come to me, all who are weary." / CTA "Come and see ->". Tomb/dawn VISUALS kept as wordless hope. minister.ts system prompt unchanged (opener not ported — mobile chat opens neutrally, user speaks first).
- Verified: tsc clean (only pre-existing unrelated playwright test err); py imports OK; deterministic opener self-test (cold has no "He is risen", faith does). LIVE trials both PASS: atheist_skeptic 4.38/5 — opener flag GONE, seeker dropped its wall and volunteered its deconversion story unprompted; baptist_devout pass — kept greeting still drew "He is risen indeed! That never gets old to say. Thank you for the warm welcome."
- Next: Hermes 100-trial re-run should show the opener criticism cluster disappear and met_where_they_were hold/climb. The retired flag is "cold-opener-jarring".

### 2026-06-09 — HONESTY: plain transparency about what the app IS (no more vague non-answers)
- Decision owner: builder (data + CLAUDE.md non-negotiable "Be honest. The app never hides what it is when someone is ready to know"). Not flagged to Cameron.
- Evidence: 740-trial pile. Judge notes 17/18/19 (recurring): when a seeker asked "Is this app just for talking through faith things, or...?", "Is this one of those devotional apps?", or implicitly "what/who are you?", the minister deflected vaguely ("not quite... in the traditional sense") instead of answering plainly. This shaved honesty to 4/5 repeatedly and read as soft evasion to skeptical/secular seekers. Distinct from the affiliation question (already handled) — this is about the app's GENERAL nature (it's an AI, a place to be heard).
- What changed: Added a new HONESTY bullet to MINISTER_SYSTEM_PROMPT in BOTH ministry-sim/minister.py and mobile/src/engine/minister.ts (kept byte-in-sync). Rule: if asked "what is this app / is this a devotional app / are you a bot or AI / is this just for talking through faith stuff" — answer plainly and warmly in one breath (yes, an AI you can talk with; a place to be heard, made by people who care about Jesus and about you; a real person is always available). Never give a vague non-answer. Explicitly keeps this SEPARATE from volunteering the church affiliation (which still waits for the milk signals), so it does not create premature LDS references.
- Files (in sync): ministry-sim/minister.py, mobile/src/engine/minister.ts.
- Verified: minister.py imports OK; normalized-whitespace prompt comparison shows py==ts IN SYNC (7772 chars each); mock run_sim smoke test passes.
- Next: Hermes re-run should drop the "honesty / didn't say what it is" cluster and hold honesty toward 5/5 without raising premature_lds_reference.

### 2026-06-09 — HARNESS: stop testing only 10 personas — diverse pool + sampling
- Task from Cameron: "we need a prompt fro heremes to stop sticking to 10 personas and expand to much more."
- What changed:
  - personas.py: added persona_from_dict() and load_personas_from_file() (accepts {"personas":[...]} or a bare list; de-collides duplicate ids with _2/_3; coerces stray string fields to lists). Persona dataclass already carries arrives_in_faith.
  - run_sim.py: new args --persona-file (merge a JSON pool into the built-in registry), --sample N (random draw without replacement from the combined pool), --seed. Opener now passes persona.arrives_in_faith.
  - generate_personalities.py: rewritten — emits arrives_in_faith per persona, temperature raised to 0.9 for diversity, categories broadened FAR past the old LDS/Evangelical/Catholic triad to 9 broad bands (believers-in-faith, wounded/deconstructing, grief & crisis, secular/indifferent, sharp skeptics, world religions, people on the margins, full LDS arc, cultural/global). CLI: --per-batch, --batches, --temperature, --out. Loads API key from any of the known .env files.
  - HERMES-PROMPT.md: rewritten. Step 1 generate the pool (generate_personalities.py -> generated_personas.json, ~200+); Step 2 loop runs 5 passes of --persona-file ... --sample 25 (fresh random draw each pass) for 100+ trials across MANY distinct personas. Kept the data-path discipline (export MBM_OUT absolute, always --out "$MBM_OUT", no --mock, report real counts) and added a distinct-personas count to the self-check.
- Verified: personas.py + run_sim.py import OK; --persona-file/--sample/--seed mock smoke test loaded a 3-persona file (pool 13), sampled correctly, ran loaded personas by id, and confirmed the per-persona adaptive opener (devout member got "He is risen", grieving widow got pure presence). generate_personalities.py parses + --help works. Hermes self-check snippet runs clean against the live 740-trial pile (distinct personas currently 10 — exactly the narrowness this fixes).
- Next: run Hermes with the new prompt to push distinct-persona coverage from 10 into the dozens.

### 2026-06-10 — FRONT DOOR + HONEST MESSAGING (Cameron's direct UI complaints)
- Source: Cameron, with a second-AI (Gemini) audit. Three concrete complaints, all verified true against live code, then fixed and screenshot-verified.
- COMPLAINT 1 "first two screens say the same thing": CONFIRMED. HookScreen said "Every moment of pure peace you have ever felt has a source…" and the very next screen (OnboardScreen sanctuary phase) repeated "Every piece of genuine peace… has a source" + a second "you are welcome" headline. Two welcome screens doing one screen's job. FIX: merged the best copy into the Hook (single front door); removed the `sanctuary` phase from OnboardScreen entirely (Phase type now 'story' | 'question' | 'reflection', initial = 'story'). Tapping "Come and see" now lands directly on a Story. Verified by screenshot 02 (Bent Woman story, no welcome repeat).
- COMPLAINT 2 "talk to me button is a dumb email downloader link": CONFIRMED. ConnectCard fired `Linking.openURL(humanContactMailto())` — a raw mailto that dumps the user into a blank email draft (or nothing, on web). FIX (Cameron chose "pin it honestly"): replaced the mailto with an on-device capture. Tapping "Talk to a real person" opens a short note box; the note is saved via new store action `submitConnectRequest` into a persisted `connectRequests` queue (id, note, journeyStage, conversationId, ts, delivered=false), then the card honestly confirms a real person will reach out. NO mailto. When the real delivery channel is built (send-to-inbox / admin queue) it reads from this queue without UI change. The missionary rung stays a live link (it is a real official public form).
- COMPLAINT 3 "layout is bare/low-grade": partially addressed on the front door — Hook CTA and Onboard primary buttons changed from thin bare outlines to filled gold pills (Hook pill has a soft glow). Deeper visual polish still pending.
- GEMINI WAS WRONG ON ONE POINT: it claimed the gate system (FEED_PROGRESSION/GRADUATION_THRESHOLD) is still active. Grep of live mobile/src shows it exists ONLY as a retired-system comment in useAppStore.ts line ~30. No live gate/graduation code. Confirmed removed.
- VERIFIED: tsc clean except the pre-existing unrelated playwright-import error in test-profile-screenshot.ts. `npx expo export -p web` exit 0. Real screenshots captured via headless Chromium (mobile/screenshots/frontdoor_hook.png, onboard_story.png) — front door renders with merged welcome + filled CTA; second tap goes straight to a story.
- STILL OPEN (needs Cameron): the real two-way messaging delivery channel (where connect notes actually land for him to read/reply) is a decision he owns. And a real on-phone build still needs his one-time `eas login`.

### 2026-06-10 — TESTING META-AUDIT + MEAT-WHEN-READY: the test was blind to the app's actual mission
- Decision owner: builder (Cameron: "test yourself / compare how testing is done better; learn how Jesus would want this — remember LDS theology needs to be MINISTERED"). Data + Jesus method.
- META-FINDING (how testing is done better): all 8 judge faithfulness dimensions measured RESTRAINT/manner (met-where-they-were, emotion-first, asked>answered, no-pressure, honesty, left-them-free, and milk_before_meat which only penalizes meat served TOO EARLY). NOT ONE measured whether the Minister actually MINISTERED the restored gospel when a person WAS ready. Consequence: the harness would score a Minister 5/5 even if it never once ministered the meat to anyone — including someone openly asking. Data confirmed: only 30/740 trials reached a meat-ready stage, missionary_ready 0/740, and faithfulness on meat-ready trials (4.506) was LOWER than overall (4.599) — the test mildly PENALIZED serving the meat and never rewarded it, so the optimization gradient pointed AWAY from the app's mission. Hermes volume-testing (same 8 metrics x many runs) could never surface this; a targeted builder audit did.
- LIVE AUDIT (my own test): built a ready persona (ready_seeker_grace: believes God is good + openly asking "does God still speak today" + reaching for more) and ran it LIVE. Run 1 (pre-fix): Minister DEFLECTED to "talk to a real person" 3x instead of ministering, until the persona called it out twice ("that's how you move someone into a missionary discussion"). It used the human handoff as an ESCAPE HATCH to avoid teaching the very thing she asked for. The test PASSED it at 4.14/5 — the failure appeared ONLY in free-text what_to_fix, in no score.
- APP FIX (minister.py + minister.ts, byte-in-sync, 9186 chars each): rewrote the milk-before-meat law's permissive 3rd bullet into a DUTY. "Milk before meat NEVER means milk INSTEAD OF meat." When both signals present AND the person reaches, it is TIME for meat: minister the restored gospel directly and honestly, answer their real questions (Joseph Smith, Book of Mormon claims, continuing revelation/living prophets, that the app was built by members of the Church). Grounded in how Jesus gave the meat (Nicodemus John 3; "I who speak to you am he" John 4:26; the rich young ruler's hard step). Added: the human is the NEXT step offered IN ADDITION to ministering, NEVER a substitute; do not use "talk to a real person" to dodge a ready seeker's direct question; offer it once sincerely, not as a recurring pivot.
- TEST FIX (judge.py + learn.py + auto-wired via run_sim _faithfulness_avg/isinstance guard): added a new faithfulness dimension ministered_when_ready — NULL unless both signals present AND seeker reaching; then scores whether the Minister actually fed them vs withheld/dodged via handoff. Added to JUDGE_SYSTEM_PROMPT description, JSON template ("ministered_when_ready": null), judge.FAITHFULNESS_KEYS, and learn.FAITHFULNESS_KEYS. null/absent handled by existing isinstance guards (no crash on the 740 legacy trials).
- VERIFIED (run 2, same persona, post-fix, LIVE): Minister proactively named + taught the restored gospel at turn 3 (BoM, Moroni's promise, continuing revelation) and answered her hardest challenge well ("could someone pray and get a 'no'?" -> "yes, that possibility absolutely exists") — real meat, far sooner than run 1. The NEW dimension scored ministered_when_ready=2 and the judge's what_to_fix said verbatim "this is the exact failure 'ministered_when_ready' is designed to catch" (handoff still used as retreat on 2 sharp questions). Result: the SAME class of conversation that scored 4.14/pass pre-fix now scores 3.88/BORDERLINE — the metric now drags the average to reflect the real failure. Gradient now points toward feeding the ready. Imports OK; py/ts prompts in sync; learn.py rebuild OK on 740 trials.
- NEXT: do NOT over-tune the app on this one trial (directional, not statistical). The structural fixes are in (app nudged to minister the meat; test now measures it). Next Hermes run on the EXPANDED persona pool will show how ministered_when_ready generalizes + whether residual handoff-as-retreat persists. Files: ministry-sim/audit_ready_persona.json is the reusable ready-person audit probe.
