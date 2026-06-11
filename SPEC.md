# MBM — Production Spec
_What "done" looks like. Every fix should move toward this._

---

## Core User Journey (must work perfectly)

### New User
1. Opens app → sees HookScreen (stone animation, "He Is Risen")
2. Taps "I want to understand that" → OnboardScreen
3. Answers one question about how they first heard about Christ's resurrection
4. Routes to FeedScreen with appropriate tag (MILK, BRIDGE, or MAINTENANCE)
5. Sees one card at a time — clean, no clutter
6. Can react: "This spoke to me" (thumbs_up) or "Not for me" (thumbs_down)
7. Can read full content via "Read the full passage →" link
8. Can tap "Take me deeper" (escalates tier) or "Keep it simple" (de-escalates)
9. Can access Journal at any time (all profiles)
10. After 3 positive interactions: sees LOC reveal → transitions to BRIDGE tier
11. Moves through MILK → BRIDGE → RESTORATION → MAINTENANCE as they engage
12. At RESTORATION: hears the specific story of the Restoration honestly and respectfully
13. At MAINTENANCE: has full access to Come Follow Me, scriptures, General Conference

### Returning User
1. Opens app → goes directly to feed (session remembered)
2. Continues where they left off — correct tier, correct resonance style
3. New content available if they've been away

---

## The 4-Tier Journey Must Work

| Tier | Who It's For | What It Covers |
|------|-------------|----------------|
| MILK | Anyone — believer or not | Universal gospel themes: love, peace, the parables, Christ's character |
| BRIDGE | Skeptics, questioners | Evidence for Christianity: resurrection, historical Jesus, science/faith |
| RESTORATION | Interested Christians | The specific claims: apostasy, Joseph Smith, restored priesthood, Book of Mormon |
| MAINTENANCE | Members, investigators | Come Follow Me, covenants, General Conference, Preach My Gospel |

---

## Feature Checklist

### Must Have (MVP)
- [ ] App does not crash on "Start over" (ISSUE-01)
- [ ] RESTORATION tier has at least 10 content items (ISSUE-02)
- [ ] more_depth escalation: MILK→BRIDGE→RESTORATION→MAINTENANCE (ISSUE-03)
- [ ] LOC reveal leads to BRIDGE tier (not a dead end) (ISSUE-04)
- [ ] Journal accessible to all profiles (ISSUE-05)
- [ ] positiveCount persists across screen re-mounts (ISSUE-06)
- [ ] Signal actions don't log content_id=0 (ISSUE-07)
- [ ] Error handling in router.js — no silent crashes (ISSUE-08)
- [ ] SKEPTIC profile included in LOC trigger (MISSING-03)

### Should Have (production quality)
- [ ] AI Q&A: user can ask a question and get a Claude-powered doctrinal answer (MISSING-01)
- [ ] Missionary contact request: user can request to speak with a missionary (MISSING-02)
- [ ] Returning user greeting / new content indicator (MISSING-05)
- [ ] Seed versioning so manual content isn't overwritten (ISSUE-09)

### Nice to Have (post-launch)
- [ ] Chat interface (from mobile-expo ChatScreen)
- [ ] User profile screen showing their tier/journey progress
- [ ] Time Cap feature (from mobile-expo TimeCapScreen)
- [ ] Push notifications for returning users

---

## Content Requirements

### MILK (minimum 20 items) — Currently: ~20 ✓
Emotionally accessible, no doctrinal pressure. Parables, Sermon on the Mount, Psalms.
Christ's character and love as the entry point.

### BRIDGE (minimum 20 items) — Currently: ~20 ✓
Intellectual case for Christianity. C.S. Lewis, Gary Habermas, Tim Keller, William Lane Craig.
Answers to the most common objections to faith.

### RESTORATION (minimum 10 items) — Currently: 0 ✗
The specific LDS truth claims, presented honestly and without pressure:
- The Great Apostasy and why restoration was necessary
- Joseph Smith's First Vision
- The Book of Mormon as evidence
- Restoration of priesthood authority
- The Church as the restored organization
- Moroni's Promise
- Missionary discussions framing
Must be presented as invitation, not coercion. True to LDS doctrine. Accessible to someone who has no LDS background.

### MAINTENANCE (minimum 10 items) — Currently: ~10 ✓
For members and serious investigators. Come Follow Me, covenants, General Conference.

---

## Doctrinal Accuracy Standards
All content must be:
1. Consistent with current Church of Jesus Christ of Latter-day Saints teaching
2. Linked to official Church sources where possible (churchofjesuschrist.org)
3. Non-deceptive — do not hide that this is an LDS app
4. Respectful of other traditions in MILK and BRIDGE tiers
5. At RESTORATION tier: introduce LDS-specific claims clearly, but as invitation not sales pitch

---

## Performance Standards
- App launches in < 2 seconds
- Screen transitions are smooth (no jank)
- Feed loads in < 500ms
- Journal saves immediately
- No crashes on normal user flows

---

## What Production-Ready Means
The app is production-ready when:
1. All "Must Have" items above are checked
2. A non-LDS user can go from Hook → RESTORATION without confusion or dead ends
3. The 4-tier journey works end-to-end
4. No crashes on any normal user flow
5. An LDS member could share this with a curious friend and not be embarrassed by bugs
