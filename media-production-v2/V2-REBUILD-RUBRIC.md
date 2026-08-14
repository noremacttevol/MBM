# MBM V2 — Rebuild Rubric

This is the reusable quality gate for all 200 visual rebuilds. It comes from
Cameron's retained Firebase review history (77 complaint-bearing stories at the
start of this wave), the July audio failure audit, the existing content-care
laws, and the Peter Walks on Water V4 visual test. V4's pictures set the visual
direction, but V4 is rejected as a final because its copied audio was shortened.

## THE TWO META-LAWS (Cameron, 2026-08-05 — read before anything else)

**THE LEARNING LAW.** Cameron: "i am tired of not getting the best quality
product and a video builder that doesnt learn from what i want and the
complaints i keep submitting." Therefore:
- Every session — author OR runner — reads ALL numbered lessons below before
  touching a row. The list grows; never assume you know where it ends.
- Every complaint Cameron files becomes a numbered lesson (with his exact words
  and the rows of record) in the SAME session that reads it. A complaint that
  never became a lesson is a complaint he will have to file again.
- Before shipping a row, list that row's open complaints
  (`python3 media-production-v2/v2_outline.py <row>` shows them on top) in the
  build's QC.md as a **COMPLAINT LEDGER**: one line per complaint, stating
  exactly what in this cut fixes it. The review-card flag tells Cameron his
  complaint was addressed, in plain words, so he can verify in one look.
- A shipped cut that repeats a complaint he already filed is the worst failure
  this pipeline can produce — worse than shipping nothing.

**THE COST LAW.** Cameron: "the cost should get cheaper." The measured baseline
(2026-08-05): $6.10/row average, 19% of spend on rerolls ($44.62 of $236.64).
- Reroll budget: ≤15% of a row's beat count. Two failed rerolls on a beat →
  FIX-WAVE log, keep the best take, move on (never 4–7 pulls on one beat again —
  build-07 b13 took 7).
- Reuse before regenerate: stash plates, promoted anchors, byte-identical
  carryover of passing frames. Never regenerate a frame that already passes.
- Touch each row ONCE: batch every known fix (pictures, captions, complaints)
  into one re-cut. Every re-cut voids Cameron's approval and re-queues the row —
  re-cutting an approved row for a non-complaint reason burns money AND his time.
- Every session logs $/row and reroll % in its SESSION-LOG entry against the
  running average, and explains any overage. The trend must go DOWN.


**THE PROMPT-AUTOPSY LAW (Cameron, 2026-08-11: "you can reverse engineer what
you said in the prompt that was wrong — make it the standard reworking
process").** Every saved prompt is evidence. When a picture is bad, the fix
STARTS by reading the exact original prompt that made it (beats_v2.py +
ASSEMBLED-PROMPTS.txt) and ruling one of three verdicts:
1. The prompt CAUSED it — a wording actively asked for the wrong thing
   (row 15's lock literally ordered "grey and waxy" skin; row 66's beat text
   staged the chaos he complained about). Fix: rewrite the words.
2. The prompt ALLOWED it — nothing forbade the defect (row 13's "seen from
   just above" allowed a grave-shaft; row 23's wide never required the crew).
   Fix: add the missing constraint to must_show/must_not_show.
3. The generator IGNORED it — words were right and it drifted anyway (boat
   sizes, every recurring face). Fix: attach a REFERENCE IMAGE — words never
   pin appearance; only pictures do.
The verdict goes in QC.md; a new defect-wording pattern becomes a
RUNNER-LESSONS line so the same words are never written again. Rerolling
without an autopsy is forbidden — it re-runs the same evidence and hopes.

## What is locked

- Do not modify the mobile app during this work.
- Keep the existing story, script, captions, segment timing, music, and closing
  question unless Cameron reports a specific defect.
- Use the canonical audio from the finished `media-production/build-*/*.mp4`
  read-only. `v2_assemble.py` stream-copies that encoded audio and fails unless
  the V1 and V2 audio-stream hashes match exactly.
  The locked ElevenLabs cast is Brian (narrator), Alexander (Jesus), Bill (God),
  Roger (scripture), and Matilda (woman).
- Never pay to re-voice a picture-only rebuild. Never rebuild an audio mix from
  clips, use a V2-local copy, substitute another MP4, shorten words, or remove a
  segment. The final rendered MP4 itself must pass the encoded-audio hash lock.

## Lessons that apply to every picture

1. **Exact story beat.** The image must show the narrated event, including who is
   present, what they are doing, where they are looking, travel direction, object
   count, time of day, and cause and effect. Attractive generic Bible imagery is
   still a failure when it tells the wrong moment.
2. **Locked cast.** Every recurring person keeps the same face, apparent age,
   build, hair, beard, clothing, and scale. Attach the accepted character image
   reference to every later shot; a text description alone is not enough.
   One person has one canonical identity anchor: never mix a group image whose
   version of that face disagrees with the person's individual anchor. Generating
   each scene independently is not proof of identity, even when every prompt had
   a reference attached.
3. **Human variety.** Disciples and crowds are distinct people, not twins or one
   repeated face. Named people remain recognizable without making everyone else
   look identical.
4. **Anatomy and contact.** One head, two arms, two legs, complete hands and feet,
   natural joints and weight. No fused bodies, new or missing beards, limbs through
   wood, feet through boats, floating knees, pasted-on objects, or impossible
   grips. Inspect contact zones at full resolution.
5. **Scale and space.** Jesus, adults, and children stay proportionate. Nobody
   becomes a giant. Figures share one ground plane. Boats, rooms, furniture,
   waterlines, rigging, doors, scrolls, and tools must form one coherent space.
6. **Historical coherence.** First-century setting, materials, clothing, boats,
   architecture, writing materials, and daily objects. No modern objects and no
   invented scripture props.
7. **V2 visual standard.** Realistic, reverent, cinematic biblical photography
   with natural skin, fabric, wood, stone, water, and light. No cartoon, comic,
   plastic CGI, copied artist style, panels, borders, watermarks, or generated text.
8. **Sacred figures.** Use the locked V2 Jesus reference and exact current Jesus
   lock. Follow `CONTENT-CARE.md` for the Father, violence, grief, children,
   judgment, and adversary scenes. Do not invent theological symbols.
9. **Rendered-product truth.** Inspect the accepted source and the actual final
   video frame after crop, zoom, captions, and encoding. Check caption sync and
   colour, closing-card margins, audio, silence, and tail length in the delivered
   MP4—not just the inputs.
10. **Face-board truth.** Before assembly, group every still by recurring person
    and compare the visible face side-by-side with that person's one canonical
    anchor. Hairline, skull/face shape, eyes, nose, cheekbones, ears, age, beard,
    and skin tone must read as one actor. If a normal viewer can see the actor
    change, the still fails even if its prompt contained the right lock text and
    reference. Correct drift with an identity-preserving edit that changes only
    that person's face/hair, then recheck the entire edited frame for changed crop,
    pose, anatomy, people, props, lighting, and scene geometry. A face fix that
    damages the scene is still a failure.
11. **Copy the good pictures — places are locked by IMAGE, like faces (Cameron,
    2026-08-04).** A recurring setting keeps one look within a story and across
    all 200 videos. `v2_stash.py --wire <build>` attaches an approved plate from
    the stash of shipped stills to every beat of that place; a NEW place gets its
    first good frame promoted (`--promote`) so the rest of the build copies it.
    Text alone re-invents architecture — row 39's colonnade survived four text
    cures; a plate carries the place the way the face reference carries Jesus.
    A place with a plate does not need a new 400-word prose lock, so the shared
    lock tower stops growing. Never hand a Jesus-bearing frame to auto-wiring.
    When one sub-region keeps regrowing a defect through plate + text (row 39:
    battlement teeth on one wall crest survived four renders), stop rerolling —
    use the lesson-10 EDIT method on the otherwise-approved frame: attach it,
    name the one region and the one change, then recheck the complete frame.
12. **Movie coverage, not group portraits (Cameron, 2026-08-05).** Compose every
    frame as the shot a film would actually cut to: it contains ONLY the people
    the narrated moment is about — a single, an over-shoulder two-shot, an
    insert of hands or an object — never the whole cast crowded in because they
    exist in the story. Crowding is what breaks gazes and travel directions
    ("all of them not looking right or going the right way"). Establish the full
    scene at most once per location; cover everything else in singles, two-shots
    and inserts. And a key action SEQUENCE gets a frame per action so it reads
    as motion: John 21 needs "It is the Lord" on the man who says it, Peter
    binding his coat and going over the gunwale, and Peter swimming for shore —
    three frames, never one frame standing in for all three. Authoring asks of
    every segment: which single moment is this, whose moment is it, and does any
    verb in the narration deserve its own frame?

13. **BEARD BOARD (Cameron, 2026-08-05 — row 102: "We need to make a qc
    just for beards dissapeaering or appearing it throws people off the
    story").** Before assembly, run a dedicated beard pass separate from
    the face board: for EVERY recurring person, list their locked beard
    state (full / short / none, and colour) and step through every frame
    they appear in checking ONLY the beard. A beard that appears,
    disappears, changes length or changes colour between frames fails
    the still — even when the face otherwise matches. Complaints of
    record: row 9 (rich man lost his beard at 0:52), row 62 (lost his
    beard in one picture), row 91 (a disciple grew a beard within
    seconds), row 102 (Jacob beardless, then bearded). Fix with the
    lesson-10 identity-edit method, then recheck the full frame.

14. **SCALE GATE (Cameron — rows 56/69/107/112: "Jesus was realy big in
    one of the photos", "John is way too big", "Jesus and John the
    baptist are bigger than the rest", "Jesus was a giant compared to
    the other people").** In every multi-figure frame, compare each
    figure's height against a shared reference (door, boat, the person
    beside them). All adults within natural variation of one another;
    Jesus is an ordinary-sized man — NEVER a giant, NEVER enlarged for
    emphasis. Children are child-sized and STAY the same size across
    frames. Any giant/shrunken figure fails the still even if the face
    and beard pass.

15. **VISION EMBODIMENT — when Cameron ASKS for the Father to be shown
    (Cameron, 2026-08-07 — build-179-stephens-witness, Acts 7: "The vision
    scene (Acts 7:55-56) must clearly show two distinct glorified personages
    in radiant heavenly light: God the Father and His Son Jesus Christ
    standing at the Father's right hand. Portray them as separate embodied
    beings, just as Stephen saw them — not as one figure, not as Jesus only,
    and do not add a dove or Trinitarian symbol. Use a reverent, luminous
    style like official Latter-day Saint gospel art").** The default gate is
    still "God / the Father is never embodied" — BUT where a filed complaint
    explicitly asks to depict the vision of the Father and the Son (Stephen's
    vision, the First Vision, and the like), that complaint GOVERNS that row's
    vision beats and the general gate is overridden THERE ONLY. In such a
    beat: show the Father and the Son as TWO distinct, separate, embodied,
    glorified persons in radiant white light, the Son STANDING at the Father's
    right hand, reverent and luminous like the Latter-day Saint Gospel Art
    Book. NEVER merge them into one figure, NEVER show Jesus only or the
    Father only, and NEVER add a dove, triangle, all-seeing eye, cross or any
    Trinitarian symbol. Everywhere else in the same row there is still no
    divine figure. The drift-word gate bans the literal words halo/glow/
    rim-light, so word the light as radiant/luminous/brilliant white light in
    the SKY, never a ring around a head. A pass that un-embodies such a vision
    (unseen presence, single figure, Jesus-only, or a symbol) RE-OPENS the
    complaint — the worst failure.

16. **GOD-AS-LIGHT READS AS A UFO — embody, don't disc (Cameron, 2026-08-07 —
    row 102 jacobs-ladder: "0:24 looks like a UFO, no God coming to him in a
    dream").** When God/the LORD is present in the beat and a filed complaint
    asks to SEE him (or scripture has him standing/coming — Gen 28:13 "the LORD
    stood ABOVE it"), depict the embodied Father (the GOD lock + god.jpeg,
    byte-identical to build-113 so his look does not change), NOT a shapeless
    brilliance. A "light only / no figure" divine presence at a summit, opening
    or sky renders as a **flying-saucer disc, ring, orb or downward beam** — a
    literal UFO — and also fails the OTHER half of the complaint (there is still
    no God shown). Word any opening as a NATURAL break in the sky filled with
    warm light with the embodied person IN it; ban UFO/disc/saucer/ring/orb/
    portal/craft and halo/glow/rim-light. A partial fix that shows God embodied
    in some summit beats but light-only in others re-triggers row 113's "his look
    changes." The Father-vs-premortal-Christ FACE for OT "LORD" theophanies is
    Cameron's per-passage call (flag it, don't sweep blind — some God-rows are
    voice/light theophanies, e.g. 101 still-small-voice).

17. **PIN TRAVEL DIRECTION TO A FIXED SCREEN SIDE (Cameron, 2026-08-07 — row 104
    boy-samuel: "0:35 Samuel is running the wrong way, same at 0:53"; ties to the
    row-14 law + lesson 1/12).** When a character crosses a space to reach
    someone, "toward the doorway/him" is NOT enough — the model will draw the run
    the wrong way. Establish a FIXED left/right geography in the setting lock (who
    and what is on the LEFT, who is on the RIGHT), state it in the wide
    establishing shot, and in every travel beat say the direction explicitly
    (LEFT→RIGHT / RIGHT→LEFT), with the mover's body, lean, feet and gaze aimed at
    the person AHEAD of them, never away. Repeated trips (Samuel's three runs)
    use the SAME direction each time so the geography is consistent.

18. **JESUS'S EYES ARE CALM — no "crazy eyes" / master-ref eye-cast (Cameron,
    2026-08-07 — row 109 ask-seek-knock: "picture at 1:34 has Jesus with crazy
    eyes").** Jesus's eyes are calm, warm and softly open in every frame — the
    settled master-face gaze — even on a big gesture or strong emotion. NEVER
    wide, wild, bulging, staring, manic, whites-showing, or a lens-stare. A
    beat's energetic action (arms thrown wide, "how much more") must not bleed
    into an excited wide-eye. If a targeted regen with a calm-eyes instruction
    STILL lands a wild gaze, the fault is the **JESUS-V2-REF master face sheet's
    own eye-cast** (systemic, recurs on any Jesus close-up) — stop rerolling
    (≤2), FIX-WAVE, and escalate for a master-ref review rather than churning
    credits one frame at a time.

19. **ROPES / CORDS ARE SOLID PHYSICAL ROPE — no "ghost ropes" (Cameron,
    2026-08-07 — row 13 roof: "1:49 has ghost ropes and a weird room they are
    dropping him into. its a bad picture").** Any rope, cord, binding or line in
    a frame (lowering a mat through a roof, mooring a boat, binding a prisoner,
    a well-rope) must render as SOLID, opaque, physical rope — taut or plainly
    slack, and clearly CONNECTED at BOTH ends (hand-to-mat, post-to-boat, etc.).
    NEVER transparent, faint, see-through, ghostly, glowing, wispy, floating
    free, frayed-into-nothing, or disconnected — a half-rendered rope reads as a
    "ghost rope" and breaks the shot. Whenever a beat's action hangs weight on a
    rope, state the solid-rope requirement in must_show and the ghost-rope ban in
    must_not_show. (Companion to lesson 8 ACTION-LOGIC: a rope that carries no
    visible load, or vanishes mid-span, fails the glance test.)
20. **EYE COLOUR COMES FROM THE REFERENCE IMAGE — the green→brown edits are
    REVERSED (process autopsy, 2026-08-12).** The locked V2 master
    `JESUS-V2-REF/jesus-v2-face.jpeg` is itself **green/hazel-eyed** — that IS
    the approved face (JESUS_LOCK_V5 matches it on purpose; see the recorded
    rationale above the lock in `v2_prompt.py`). In the week of 2026-08-11,
    C-FIX sessions on rows 71, 89, 98, 120 iris-EDITED his green eyes to brown,
    citing the older CLAUDE.md 8(g) "warm brown eyes" — that text is the
    **V1-pipeline standard** (JESUS-MASTER-REF / LOCK v3) and does NOT govern
    V2. Cameron never complained about eye colour. The permanent rule, per his
    own law ("anything that must look the same twice gets locked to a reference
    IMAGE, never a description"): **when prose law text and the active
    reference image disagree, the IMAGE wins — never reroll AND never
    identity-edit a frame AWAY from the ref.** "Weird eyes" complaints are gaze
    geometry (lesson 18), never colour. Restore ref-true eyes on rows
    71/89/98/120 in each row's NEXT touch-once re-cut (never as its own
    re-cut — their shipped complaint fixes are otherwise correct).

21. **NO HEAD TURNED AROUND BACKWARDS — the owl-neck / head-on-backwards
    (Cameron, 2026-08-13 — row 122: "The man's head is turned around backwards
    0:33. same problem for the 5th time"; his 5th filing of this class).** Any
    beat that stages a "glance," a "sideways look," an "over-the-shoulder"
    verdict, or a figure seated with their back to the camera can make the
    generator wrench a face a full ~180° back to the lens over a torso that
    faces away — an anatomically impossible neck. The generic anti-glitch line
    "two arms, two hands and one head" does NOT stop it: "one head" says nothing
    about which way the head faces. PROMPT-AUTOPSY verdict for this class is
    almost always ALLOWED (verdict 2) — the fix is a missing constraint, not a
    reference image. Every such beat's `must_show` puts the glancer in
    three-quarter view with head AND shoulders turned the SAME way (a natural
    glance under ~45°); its `must_not_show` forbids "any head rotated impossibly
    on the neck; owl-neck; a seated figure with back or shoulders to the camera
    while the face is wrenched a full half-turn back to the lens"; and the
    anti-glitch tail becomes "every head sits forward on the neck facing the
    same way as its own shoulders — no one twisted so their face looks back
    over a body that faces away." GATE (belongs in every FULL-CUT pass): on any
    crowd or two-shot with a back-to-camera figure, confirm you see the BACK of
    that head. A figure legitimately facing away (row 122 b01/b02 show the back
    of the same man's head) is CORRECT and must never be "corrected" — the
    defect is only the impossible turn, not the facing-away. Rows of record:
    122 (b06). Extends lesson 4 (anatomy/natural joints) with the specific
    neck-rotation clause that kept slipping through.

22. **MOONLIGHT DRAINS FACES GREY, HIDES HANDS, AND RENDERS NEAR-BLACK — a
    night beat needs three explicit floors or it fails three ways (Cameron,
    2026-08-13 — row 146: "0:40 some bystanders have white faces… 0:47 man has
    multiple arms… 1:19 picture has Jesus missing a hand").** Three distinct
    complaints on one night cut, all PROMPT-AUTOPSY = ALLOWED (missing
    constraints, not bad refs): (a) **grey/white faces** — a moonlit crowd with
    no skin-tone floor washes several faces to ashen/grey/white ("corpse" look);
    FIX: `must_show`/`scene` require every face to keep "warm living olive/tan
    Middle-Eastern skin, softly moonlit," and `must_not_show` bans "grey, ashen,
    pale, white, bluish, desaturated or drained faces." (b) **spare/third arm** —
    the generic "two arms, two hands and one head" line does NOT stop a spare
    limb on a from-behind figure who shoulders a tool while also reaching; when a
    hands/arms beat drifts, recompose to the ACTUAL brief (a TIGHT close of the
    hands doing the one thing) and add "NO extra, third, duplicated, floating or
    disembodied arm or hand — every visible person has exactly two arms both
    joined at the shoulders." (c) **near-black frame** — "moonlight" with no
    readability floor renders unviewable; every night beat needs "clearly VISIBLE
    in soft moonlight — not a near-black or unreadable frame; every face and
    hand plainly lit," still night, not sunset/sunrise. Also here: a beat whose
    prose named "moonlit" rendered golden-day walking-workers instead of the
    briefed close hands-on-branch — recomposing to the brief fixed the arms, the
    time-of-day, AND de-duplicated it from the adjacent frame in one reroll.
    Rows of record: 146 (b04 faces, b09 arms/time, b14 hand/darkness). Extends
    lesson 4 (anatomy) and the time-of-day law with the night-readability floor.

23. **NO BUILDINGS FLOATING IN THE SKY / DUPLICATED VERTICAL CITY LAYERS
    (Cameron, 2026-08-13 — row 44 Pentecost at 1:38: "there are buildings in
    the sky. Same problem again").** An ancient-city place plate plus a tight
    crowd close can be recomposed as two incompatible depths: the real ground
    city behind the people and a second row of rooftops/towers pasted into open
    sky above it, often separated by a pale mist band. This is a stacked-scene
    defect even when there is no hard panel seam. It is always a ship blocker.
    PROMPT-AUTOPSY for row 44 b17 = ALLOWED: the place lock named houses/walls
    beyond while the emotional close did not constrain how much background or
    sky was visible. For an intimate reaction beat, remove the risk instead of
    asking for another city panorama: specify one tight eye-level chest-to-head
    close, **NO SKY VISIBLE**, and one continuous ground-level wall extending
    edge to edge behind the people. Ban skyline, rooftops, towers, distant or
    duplicated buildings, architecture above heads, horizontal fog bands,
    collage/panels, and a second perspective. For a real city wide, inspect the
    entire skyline and require every building to meet visible ground in one
    continuous perspective. Rows of record: 44 b17. Extends the stacked-scene
    and doubled-skyline lessons in `RUNNER-LESSONS.md`.

## Per-story workflow

1. Run `node admin/sync-reviews.mjs` so `REVIEW-LESSONS.json` is current.
2. Run `python3 media-production-v2/v2_outline.py <row>` and read the prior
   complaint shown at the top. An open complaint must be fixed; a resolved one
   must not regress.
3. Read the complete narration and scripture passage. Write a beat map that covers
   every physical event, emotional turn, and important spoken line. Do not reuse
   one vague picture for several different events.
   A complaint naming multiple timestamps is literal: repair and encoded-QC every
   named picture. An adjacent-frame copy or extended hold is not a repair, and
   matching only age/hair does not establish recurring-face identity.
4. Add stable person/setting locks and the right image references. State
   `must_show` and `must_not_show` for every beat.
5. Run `python3 media-production-v2/v2_story_cast.py <build>` (per-story faces)
   and `python3 media-production-v2/v2_stash.py --wire <build>` (place plates
   from the stash of shipped stills). Wire suggested/story-specific plates with
   `--take`; note the reported NEW places — after each one's first good frame
   passes QC, `--promote` it and generate that place's remaining beats with the
   plate attached.
6. Run `v2_prompt.py --check` before generation. Generate at native 2K.
7. Reject any source that misses the beat or violates this rubric. Do not repair a
   visibly wrong idea with crop or captions.
8. Build and inspect the per-character face board. Identity-edit every drifted
   frame against one non-conflicting canonical anchor, and repeat the face-board
   plus full-frame geometry checks until all recurring characters pass.
9. Assemble with `v2_assemble.py`, which reads the canonical V1 audio without
   altering it.
10. Review every rendered beat and run the technical gates.
11. Publish only the candidate to `site/review.html`. Do not replace the app video.
12. Cameron's exact-version approval is the only release decision. A complaint
    remains attached through every replacement cut until he approves the fixed one.
