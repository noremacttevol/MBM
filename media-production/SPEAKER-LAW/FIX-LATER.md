# FIX-LATER — approved builds that still violate the speaker/caption law

These builds have `approved: true` in approvals.json, so their delivered cuts are
LOCKED (approved-lock, 2026-07-21). Every one of them is still on pre-speaker-law
sources (old Jesus voice Christopher, colors from the retired `KJV` red set), so
they DO violate the color/voice law — but they must NOT be rebuilt or shipped over
until Cameron un-approves them or asks for the pass to include them.

When cleared: run `python3 run_batch.py <build>` from SPEAKER-LAW/ (plans already
exist and are validated for all of them).

- build-06-two-sons
- build-11-storm
- build-12-bartimaeus
- build-15-centurion
- build-16-mary-martha
- build-92-peters-denial
- build-99-flesh-and-bone-thomas
- build-100-the-ascension
- build-103-peters-confession
- build-105-face-to-face
- build-106-god-spake-by-prophets
- build-110-lords-prayer
- build-136-healed-in-two-touches
- build-138-his-offspring
- build-139-lamp-on-a-stand
- build-141-bread-of-life
- build-142-light-of-the-world
- build-143-i-am-the-door
- build-144-resurrection-and-the-life
- build-145-way-truth-life
- build-200-gospel-to-all-the-world
- build-152-revealeth-his-secret — SHIPPED under speaker law but segcheck proves
  its kv7/kv8 scripture beats render WHITE, not blue (the rest of the build is
  correct). Approved, so the fix waits with the rest of this list.

Also excluded from the pass on standing instruction: build-17-lazarus (skip #17).

Generated 2026-07-21 during the full-library caption/voice-law verification.
