/**
 * connect.ts — the human-relationship ladder + journey toward Christ, in the app.
 *
 * This is the TypeScript port of connect.py (the Python source of truth used by the
 * learning harness). The app is a HELPER that builds human relationships — not a
 * destination. Its whole job is to make it easier to find Christ by leading a person
 * from talking to the AI, to a human-approved answer, to a real person (Cameron in
 * Phase 1), and — only when they are genuinely ready — to a missionary referral.
 *
 * THE LAW (CLAUDE.md):
 *   - A real human is ALWAYS one tap away. Never buried. Never gated. Always there.
 *   - Milk before meat: nothing about the restored gospel / missionaries appears until
 *     the person has shown BOTH readiness signals on their own:
 *       (a) they believe God is fundamentally GOOD, and
 *       (b) they are open to the idea that God might still speak today.
 *   - Let people walk away. The missionary rung is offered, never pushed.
 *
 * Keep this in sync with connect.py. When the Python logic changes, change it here.
 */

// ── Phase 1 contact ─────────────────────────────────────────────────────────
// The human help is ALWAYS named "the admin team" — never a personal name. The
// email is only used for the Phase-1 mailto fallback; it is never shown as a name.

export const HUMAN_CONTACT = {
  name:  'the admin team',
  email: 'noremacttevol@gmail.com',
};

// The official "request a visit" form. Overridable via env for testing.
export const MISSIONARY_CONTACT_URL =
  (process.env.EXPO_PUBLIC_MISSIONARY_URL ?? '').trim() ||
  'https://www.churchofjesuschrist.org/comeuntochrist/requests/missionaries';

// ── Connection ladder ───────────────────────────────────────────────────────
// Every rung except the last is ALWAYS available. The last (missionary) is the
// only one gated — and it is gated by readiness the person reveals, never by a
// wall they can see.

export type ConnectionLevel =
  | 'AI_ONLY'            // talking to the app
  | 'HUMAN_APPROVED'     // ask for an answer a real person has reviewed
  | 'HUMAN_CONVERSATION' // talk to a real person (Cameron in Phase 1)
  | 'MISSIONARY_REFERRAL'; // recommend missionaries + send the contact form

export const CONNECTION_LEVELS: ConnectionLevel[] = [
  'AI_ONLY',
  'HUMAN_APPROVED',
  'HUMAN_CONVERSATION',
  'MISSIONARY_REFERRAL',
];

// ── Journey toward Christ ────────────────────────────────────────────────────

export type SeekerStage =
  | 'UNREACHED'
  | 'CURIOUS'
  | 'BELIEVES_GOD_GOOD'
  | 'OPEN_TO_RESTORATION'
  | 'SEEKING_TRUTH'
  | 'READY_FOR_MISSIONARIES'
  | 'BAPTISM';

export const SEEKER_STAGES: SeekerStage[] = [
  'UNREACHED',
  'CURIOUS',
  'BELIEVES_GOD_GOOD',
  'OPEN_TO_RESTORATION',
  'SEEKING_TRUTH',
  'READY_FOR_MISSIONARIES',
  'BAPTISM',
];

export type MemberStage = 'DISCIPLE_GROWING';

// ── Signal sets ──────────────────────────────────────────────────────────────
// These mirror the readiness logic in knowing_engine.py / connect.py, expressed
// over the app's dialogue/onboard signal strings.

// (a) believes God is fundamentally good.
// ONE CLICK IS NEVER IDENTITY (owner law, 2026-06-11): 'covenant_intent' from a
// single story tap ("I'm committed but I hold back") is a believer HINT only —
// it counts toward signal (a) but can never mark someone a member.
const GOD_GOOD_SIGNALS = new Set<string>([
  'believes_god_good',
  'believes_in_jesus',
  'drawn_to_jesus',
  'open_to_god',
  'had_spiritual_experience',
  'covenant_intent',
]);

// (b) open to the idea that God might still speak today / there could be more
const OPEN_TO_MORE_SIGNALS = new Set<string>([
  'open_to_restoration',
  'curious_about_book_of_mormon',
]);

// Active / less-active Latter-day Saints — a separate track from seekers.
// Membership comes ONLY from explicit self-identification in the person's own
// words (chat or dialogue). A single onboarding tap (covenant_intent) is NEVER
// membership — that misroute lost a tester (CLAUDE.md Law 8).
const MEMBER_SIGNALS = new Set<string>([
  'inactive_member',
  'active_member',
]);

// Language that shows a person reaching toward the formal/visible church on their
// own — baptism, joining, "how do I become part of this." NEVER a fast-track past
// the milk: missionary readiness still requires both readiness signals as well.
const SEEKING_FORMAL_SIGNALS = new Set<string>([
  'wants_baptism',
  'wants_to_join',
  'asking_how_to_belong',
]);

function hasAny(signals: string[], set: Set<string>): boolean {
  return signals.some(s => set.has(s));
}

// ── Public predicates ────────────────────────────────────────────────────────

export function isMember(signals: string[]): boolean {
  return hasAny(signals, MEMBER_SIGNALS);
}

/**
 * ONE HINT IS NEVER BELIEF (owner law, 2026-06-11). "In the mouth of two or
 * three witnesses shall every word be established" (2 Cor 13:1):
 *  - A harsh-God picture OR a framework that carries one (Reformed determinism —
 *    election, damnation decreed for God's glory; the creation-dilemma: a God who
 *    creates from nothing owns the evil that follows) BLOCKS the signal even when
 *    the person loyally SAYS "God is good." Only their own-words rejection of the
 *    harsh picture, together with the affirmation, opens it.
 *  - A non-theistic framework ("God is the universe / not a person") blocks until
 *    they affirm a good personal God explicitly, in their own words.
 *  - Otherwise an explicit good-God statement counts; absent one, two independent
 *    soft witnesses are required. This discernment is INTERNAL — never spoken.
 */
export function believesGodGood(signals: string[]): boolean {
  const sset = new Set(signals);
  const blocked =
    sset.has('pictures_harsh_god') ||
    sset.has('pictures_distant_god') ||
    sset.has('reformed_framework');
  if (blocked) {
    return sset.has('rejects_harsh_god') && sset.has('believes_god_good');
  }
  if (sset.has('nontheistic_framework')) return sset.has('believes_god_good');
  if (sset.has('believes_god_good')) return true;
  const SOFT = [
    'open_to_god', 'drawn_to_jesus', 'had_spiritual_experience',
    'believes_in_jesus', 'covenant_intent', 'rejects_harsh_god',
  ];
  return SOFT.filter((x) => sset.has(x)).length >= 2;
}

export function openToMore(signals: string[]): boolean {
  return hasAny(signals, OPEN_TO_MORE_SIGNALS);
}

/**
 * The milk-before-meat gate. True only when BOTH readiness signals are present —
 * God is good AND God might still speak. Members are on the discipleship track and
 * are never "referred" to missionaries.
 */
export function mayReferenceLds(signals: string[]): boolean {
  if (isMember(signals)) return false;
  return believesGodGood(signals) && openToMore(signals);
}

// ── The seven-spirit-levels readiness gate ──────────────────────────────────
// The restored gospel is "meat." Cameron's design (2026-06-13): the seven spirit
// levels are the measurement for WHEN the church may be named. A person's words
// raise the levels through honest, open, hungry engagement; only when the
// readiness levels have genuinely been EARNED is the restored gospel revealed.
// Every soul starts at 0/10 and climbs by proving the virtue, so reaching these
// thresholds (around the 5ish midpoint, exactly as Cameron specified) means the
// person has DEMONSTRATED readiness in the conversation — not merely said a
// keyword. This is what holds the gospel back until it is actually earned, and it
// never asks the AI to push: the gate simply stays quiet until then.
//
// Only the readiness virtues gate the gospel — openness (to more / to revelation),
// hunger (for truth), and honest_inquiry (genuine seeking, not testing), with a
// teachable-humility floor folded into the average. Compassion, courage, and
// sincerity are part of who the person is but are not what makes someone ready to
// hear about continuing revelation, so they do not gate timing.

export interface SpiritLevels {
  honest_inquiry: number;
  openness:       number;
  humility:       number;
  hunger:         number;
  compassion:     number;
  courage:        number;
  sincerity:      number;
}

// On a 0→10 climb, "ready" is the ~5ish midpoint Cameron named: the person has
// earned roughly half the scale on the readiness virtues by proving them through
// the conversation. High enough that a single keyword can't open the gate, low
// enough that a genuine seeker reaches it by really engaging.
export const SPIRIT_GATE = {
  opennessMin:      5.5,
  hungerMin:        5.0,
  honestInquiryMin: 4.5,
  readinessAvgMin:  5.0, // average of openness, hunger, honest_inquiry, humility
};

/**
 * Has the person risen far enough on the readiness virtues to be ready to hear
 * the restored gospel? Returns false until the levels are genuinely earned.
 */
export function spiritReady(levels: SpiritLevels | null | undefined): boolean {
  if (!levels) return false;
  const { openness, hunger, honest_inquiry, humility } = levels;
  const avg = (openness + hunger + honest_inquiry + humility) / 4;
  return (
    openness       >= SPIRIT_GATE.opennessMin &&
    hunger         >= SPIRIT_GATE.hungerMin &&
    honest_inquiry >= SPIRIT_GATE.honestInquiryMin &&
    avg            >= SPIRIT_GATE.readinessAvgMin
  );
}

/**
 * The full restored-gospel gate: the belief signals (milk-before-meat) AND the
 * spirit levels both have to be ready. This is what the app should ask before it
 * lets the minister name the Church / Book of Mormon / Restoration. Stricter than
 * mayReferenceLds alone, on purpose — it is the fix for mentioning the church too
 * early. Members never run this gate (they already hold the gospel).
 */
export function restorationReady(
  signals: string[],
  levels: SpiritLevels | null | undefined,
): boolean {
  if (isMember(signals)) return false;
  return mayReferenceLds(signals) && spiritReady(levels);
}

// ── The Christlike ceiling (Cameron's call, recorded in the binding file) ────
// On this app the seven Christlike virtues are "how close to Christ's own, as the
// restored gospel measures it." So the score a person can reach is capped by where
// they stand toward that standard — and because every dimension carries the word
// "Christlike," the cap is honest, not a verdict on their bare character:
//   - a member / one saved and believing the restored gospel: uncapped (up to 10),
//   - someone not yet there but willing: tops out at 7,
//   - someone who won't even examine it (declined the invitation): tops out at 5.
// The cap never blocks the readiness gate (which only needs ~5) — it only sets how
// high the celestial-striving score itself can climb.
export const CHRISTLIKE_CAP = { member: 10, willing: 7, unwilling: 5 };

export function christlikeCap(signals: string[]): number {
  if (isMember(signals)) return CHRISTLIKE_CAP.member;
  // "Declined the invitation to even look" — set when a person turns down the
  // open, named invitation to the restored gospel (see the invitation flow).
  if (signals.includes('declined_restoration')) return CHRISTLIKE_CAP.unwilling;
  return CHRISTLIKE_CAP.willing;
}

// Clamp every Christlike level to the person's earned ceiling. Used when the score
// is shown or read, so no one is ever shown above their cap. The raw climb is kept
// underneath (it still drives the readiness gate); this only bounds what's shown.
export function capLevels(levels: SpiritLevels, signals: string[]): SpiritLevels {
  const cap = christlikeCap(signals);
  const c = (v: number) => Math.min(v, cap);
  return {
    honest_inquiry: c(levels.honest_inquiry),
    openness:       c(levels.openness),
    humility:       c(levels.humility),
    hunger:         c(levels.hunger),
    compassion:     c(levels.compassion),
    courage:        c(levels.courage),
    sincerity:      c(levels.sincerity),
  };
}

export function seekingFormal(signals: string[]): boolean {
  return hasAny(signals, SEEKING_FORMAL_SIGNALS);
}

/**
 * Missionary referral is ready ONLY when the milk gate is open AND the person is
 * reaching toward the formal church on their own. Asking "how do I get baptized"
 * with no readiness signals does NOT fast-track anyone past the milk.
 */
export function missionaryReferralReady(signals: string[]): boolean {
  if (isMember(signals)) return false;
  return mayReferenceLds(signals) && seekingFormal(signals);
}

// ── Journey assessment ───────────────────────────────────────────────────────

export function assessJourney(signals: string[]): SeekerStage | MemberStage {
  if (isMember(signals)) return 'DISCIPLE_GROWING';
  if (missionaryReferralReady(signals)) return 'READY_FOR_MISSIONARIES';
  if (seekingFormal(signals)) return 'SEEKING_TRUTH';
  if (mayReferenceLds(signals)) return 'OPEN_TO_RESTORATION';
  if (believesGodGood(signals)) return 'BELIEVES_GOD_GOOD';
  if (signals.length > 0) return 'CURIOUS';
  return 'UNREACHED';
}

// ── Detecting an explicit request to escalate ────────────────────────────────

const HUMAN_REQUEST_PHRASES = [
  'talk to a real person', 'talk to a person', 'talk to someone real',
  'talk to a human', 'speak to someone', 'speak to a person', 'real person',
  'can i talk to', 'is there a person', 'someone i can talk to',
];

const APPROVE_REQUEST_PHRASES = [
  'human approved', 'human-approved', 'is that true', 'are you sure',
  'can a person check', 'verify that', 'fact check', 'fact-check',
  'who can confirm', 'double check',
];

const SEEKING_FORMAL_PHRASES = [
  'how do i get baptized', 'how do i join', 'how do i become', 'baptized',
  'join the church', 'become a member', 'talk to a missionary', 'missionaries',
];

export function detectConnectionRequest(text: string): ConnectionLevel | null {
  const lower = (text || '').toLowerCase();
  if (SEEKING_FORMAL_PHRASES.some(p => lower.includes(p))) {
    return 'MISSIONARY_REFERRAL';
  }
  if (HUMAN_REQUEST_PHRASES.some(p => lower.includes(p))) {
    return 'HUMAN_CONVERSATION';
  }
  if (APPROVE_REQUEST_PHRASES.some(p => lower.includes(p))) {
    return 'HUMAN_APPROVED';
  }
  return null;
}

// ── Connection state ─────────────────────────────────────────────────────────

export interface ConnectionState {
  journeyStage:     SeekerStage | MemberStage;
  isMember:         boolean;
  humanAvailable:   boolean;        // ALWAYS true — a human is always one tap away
  requested:        ConnectionLevel | null;
  recommendedLevel: ConnectionLevel;
  missionaryReady:  boolean;
  missionaryUrl:    string | null;  // only present when missionaryReady
  rationale:        string;
}

export function assessConnection(
  signals: string[],
  latestText: string = '',
): ConnectionState {
  const member        = isMember(signals);
  const journey       = assessJourney(signals);
  const requested     = detectConnectionRequest(latestText);
  const missionReady  = missionaryReferralReady(signals);

  // What the app should naturally offer next, absent an explicit request.
  let recommended: ConnectionLevel = 'AI_ONLY';
  let rationale = 'Staying present as a companion; a human is always available.';

  if (missionReady) {
    recommended = 'MISSIONARY_REFERRAL';
    rationale = 'Both readiness signals present and reaching toward the church — gently offer missionaries.';
  } else if (member) {
    recommended = 'AI_ONLY';
    rationale = 'A disciple growing — nourish, and a human is always available.';
  }

  // An explicit request always wins, but the missionary rung still respects the
  // milk gate: asking about baptism without readiness routes to a real person
  // (Cameron), not a fast-tracked missionary referral.
  let resolved: ConnectionLevel = recommended;
  if (requested) {
    if (requested === 'MISSIONARY_REFERRAL' && !missionReady) {
      resolved = 'HUMAN_CONVERSATION';
      rationale = 'Reaching toward the formal church, but not yet through the milk — connect them to a real person first.';
    } else {
      resolved = requested;
      rationale = `Person explicitly asked to ${requested.replace('_', ' ').toLowerCase()}.`;
    }
  }

  return {
    journeyStage:     journey,
    isMember:         member,
    humanAvailable:   true,
    requested,
    recommendedLevel: resolved,
    missionaryReady:  missionReady,
    missionaryUrl:    missionReady ? MISSIONARY_CONTACT_URL : null,
    rationale,
  };
}

// ── Offer copy ───────────────────────────────────────────────────────────────

export function buildHumanOffer(): string {
  // NEVER name the admin in chat-facing copy. A real PERSON is always one tap
  // away — but who that person is stays out of the conversation. (Cameron's
  // personal name leaking into chat was a real failure; keep it generic.)
  return (
    `Whenever you'd like, you can talk to a real person — someone reads these ` +
    `themselves. No agenda, no pressure. They're one tap away.`
  );
}

export function buildMissionaryReferral(): string {
  return (
    `It sounds like you might be ready to talk with someone who can walk this road with ` +
    `you in person. If you'd like, you can ask for a visit — there's a short form, and ` +
    `real people who would be glad to sit with your questions. Only if and when you want to.`
  );
}

// ── The smart handoff (the "Talk to a real person" button's brain) ───────────
// Mirror of resolve_handoff in connect.py. When a person REACHES — for a real
// person, for a human to verify what the AI said, or toward the formal next step —
// the app does exactly one of two things:
//   1. READY  -> hand them the missionary referral link (door out to real ministry).
//   2. ELSE   -> notify Cameron / the MBM admin team so a real person steps in,
//                either to talk with them or to verify/correct what the AI said.
// This is the whole validity metric: did they logically reach, and did the reach
// route to the right kind of real human help? Keep this in sync with connect.py.

export type HandoffAction = 'MISSIONARY_LINK' | 'NOTIFY_ADMIN' | 'NONE';

export type AdminReason =
  | 'verify_ai_answer'      // check/correct what the AI said
  | 'wants_human'           // they asked to talk to a real person
  | 'reaching_not_ready';   // reaching toward the church, not yet through the milk

export interface AdminNotification {
  to:                  string;
  reason:              AdminReason;
  journeyStage:        SeekerStage | MemberStage;
  personSaid:          string;
  aiAnswerToVerify:    string | null;
  whatToDo:            string;
}

export interface HandoffDecision {
  reached:            boolean;
  action:             HandoffAction;
  missionaryUrl:      string | null;       // only when action === 'MISSIONARY_LINK'
  adminNotification:  AdminNotification | null; // only when action === 'NOTIFY_ADMIN'
  rationale:          string;
}

function buildAdminNotification(
  reason: AdminReason,
  signals: string[],
  latestText: string,
  lastAiAnswer: string,
): AdminNotification {
  let whatToDo: string;
  if (reason === 'verify_ai_answer') {
    whatToDo =
      'A person wants a real human to confirm what the app told them. Read the AI\u2019s ' +
      'answer below, verify or correct it, and reply to them.';
  } else if (reason === 'reaching_not_ready') {
    whatToDo =
      'A person is reaching toward the church but hasn\u2019t yet shown both readiness ' +
      'signals. Don\u2019t send missionaries yet \u2014 reach out as a real person, meet them ' +
      'where they are, and walk with them.';
  } else {
    whatToDo =
      'A person asked to talk to a real person. Reach out to them directly \u2014 no agenda, ' +
      'no pressure. Just be present.';
  }
  return {
    to:               'the MBM admin team',
    reason,
    journeyStage:     assessJourney(signals),
    personSaid:       latestText,
    aiAnswerToVerify: reason === 'verify_ai_answer' ? lastAiAnswer : null,
    whatToDo,
  };
}

/**
 * Decide what the "Talk to a real person" button does for THIS person right now.
 * Mirror of resolve_handoff in connect.py.
 */
export function resolveHandoff(
  signals: string[],
  latestText: string = '',
  lastAiAnswer: string = '',
): HandoffDecision {
  const requested      = latestText ? detectConnectionRequest(latestText) : null;
  const reachingFormal =
    seekingFormal(signals) || SEEKING_FORMAL_PHRASES.some(p => (latestText || '').toLowerCase().includes(p));
  const reached = !!requested || reachingFormal;

  if (!reached) {
    return {
      reached: false, action: 'NONE', missionaryUrl: null, adminNotification: null,
      rationale: "The person hasn't reached for a real person or a next step yet.",
    };
  }

  // READY: both readiness signals + reaching toward the church, and not a member.
  if (missionaryReferralReady(signals)) {
    return {
      reached: true, action: 'MISSIONARY_LINK',
      missionaryUrl: MISSIONARY_CONTACT_URL, adminNotification: null,
      rationale:
        'Both readiness signals present and reaching toward the church \u2014 hand them the ' +
        'missionary referral link. Their choice to use it.',
    };
  }

  // NOT READY (or verifying): notify a real person to step in.
  let reason: AdminReason;
  let why: string;
  if (requested === 'HUMAN_APPROVED') {
    reason = 'verify_ai_answer';
    why = 'They want a human to verify what the app said \u2014 alert the team to check it.';
  } else if (reachingFormal) {
    reason = 'reaching_not_ready';
    why =
      'Reaching toward the church but not yet through the milk \u2014 alert a real person to ' +
      'walk with them; do NOT fast-track missionaries.';
  } else {
    reason = 'wants_human';
    why = 'They asked to talk to a real person \u2014 alert the team to reach out.';
  }

  return {
    reached: true, action: 'NOTIFY_ADMIN', missionaryUrl: null,
    adminNotification: buildAdminNotification(reason, signals, latestText, lastAiAnswer),
    rationale: why,
  };
}

// Phase-1 mailto for reaching Cameron directly.
export function humanContactMailto(): string {
  return (
    `mailto:${HUMAN_CONTACT.email}` +
    '?subject=MBM%20Connect%20Request' +
    '&body=Hi%2C%20I%20was%20using%20the%20Milk%20Before%20Meat%20app%20and%20would%20love%20to%20talk%20to%20a%20real%20person.'
  );
}
