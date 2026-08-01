# MBM V2 — Rebuild Rubric

This is the reusable quality gate for all 200 visual rebuilds. It comes from
Cameron's retained Firebase review history (77 complaint-bearing stories at the
start of this wave), the July audio failure audit, the existing content-care
laws, and the Peter Walks on Water V4 visual test. V4's pictures set the visual
direction, but V4 is rejected as a final because its copied audio was shortened.

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

## Per-story workflow

1. Run `node admin/sync-reviews.mjs` so `REVIEW-LESSONS.json` is current.
2. Run `python3 media-production-v2/v2_outline.py <row>` and read the prior
   complaint shown at the top. An open complaint must be fixed; a resolved one
   must not regress.
3. Read the complete narration and scripture passage. Write a beat map that covers
   every physical event, emotional turn, and important spoken line. Do not reuse
   one vague picture for several different events.
4. Add stable person/setting locks and the right image references. State
   `must_show` and `must_not_show` for every beat.
5. Run `v2_prompt.py --check` before generation. Generate at native 2K.
6. Reject any source that misses the beat or violates this rubric. Do not repair a
   visibly wrong idea with crop or captions.
7. Build and inspect the per-character face board. Identity-edit every drifted
   frame against one non-conflicting canonical anchor, and repeat the face-board
   plus full-frame geometry checks until all recurring characters pass.
8. Assemble with `v2_assemble.py`, which reads the canonical V1 audio without
   altering it.
9. Review every rendered beat and run the technical gates.
10. Publish only the candidate to `site/review.html`. Do not replace the app video.
11. Cameron's exact-version approval is the only release decision. A complaint
    remains attached through every replacement cut until he approves the fixed one.
