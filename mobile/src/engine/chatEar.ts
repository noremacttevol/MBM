// chatEar.ts — the ear: harvest signals from a person's own words (chat,
// journal, free-text answers) + the model-side signal report protocol.
// Verified by 270 engine-sim trials (see SIM-REPORT.md): per-sentence hearing,
// negation guards, framework markers. Wire into useAppStore per INSTALL.md.

export const VALID_REPORT_TOKENS = new Set([
  'believes_god_good', 'open_to_god', 'drawn_to_jesus', 'believes_in_jesus',
  'had_spiritual_experience', 'open_to_restoration', 'curious_about_book_of_mormon',
  'carries_grief', 'lonely', 'searching_for_purpose', 'skeptical_of_god',
  'hurt_by_church', 'has_history_with_faith', 'struggles_with_habits',
  'wants_baptism', 'wants_to_join', 'asking_how_to_belong',
  'inactive_member', 'active_member', 'losing_faith',
  'pictures_harsh_god', 'pictures_distant_god', 'reformed_framework',
  'rejects_harsh_god', 'nontheistic_framework',
  // BRIDGE acceptances — distinctively-Latter-day-Saint positions a non-member can
  // come to accept on their OWN (Cameron, 2026-06-26). Accepting any of these is
  // what moves a seeker out of plain milk and into the bridge between milk and meat.
  // These are AFFIRMATIONS of a restored truth, not mere curiosity:
  //   - accepts_ongoing_revelation: God still speaks / revelation continues today
  //     (vs. a closed canon). rejects_harsh_god already carries "God does not damn
  //     people for His glory." rejects_creation_ex_nihilo: matter & intelligence are
  //     eternal — God organized what already was, He did not make it from nothing.
  'accepts_ongoing_revelation', 'rejects_creation_ex_nihilo',
  // A firm refusal to even examine the restored gospel — the "won't look" posture.
  // The minister honors it and does not re-offer. A soft "not right now" must NOT be
  // reported as this; only a clear refusal to look.
  'declined_restoration',
]);

// FAITH-IDENTITY signals describe WHO a person is with regard to faith — their
// standing, tradition, or history. Unlike engagement signals (grief, hunger,
// doubt) which accumulate, identity is a fact about the person that can CHANGE:
// they convert, they leave, they come back. So identity is never kept in the
// sticky base set — it is owned entirely by the person's own faith words, and
// re-derived whenever they edit them. Edit or remove the faith line and the app
// honestly stops thinking it. This is what makes conversion to/from a faith real.
export const IDENTITY_SIGNALS = new Set([
  'active_member', 'inactive_member',
  'active_faith_tradition', 'has_history_with_faith',
  'believes_in_jesus',
]);

// Drop any identity tokens from a signal list. Used everywhere engagement
// signals are written to the base set, so identity can only ever come from
// (and be removed with) the person's own faith words.
export function stripIdentity(signals: string[]): string[] {
  return signals.filter(s => !IDENTITY_SIGNALS.has(s));
}

// Pull just the identity tokens out of a signal list — used to capture identity
// that arrived through chat onto a faith word so it stays visible and removable.
export function identityOnly(signals: string[]): string[] {
  return signals.filter(s => IDENTITY_SIGNALS.has(s));
}

// CRISIS DETECTION — a deliberately careful, high-precision check for language of
// severe distress / self-harm / suicidal ideation / acute crisis. Used ONLY to
// mark an escalation to the admin team as high-priority so a real person triages
// it first; it never changes what the user sees and never diagnoses. We keep it
// tight (clear phrases, not single ambiguous words) to avoid false alarms — a
// person merely saying "I'm tired" or "this is killing me [funny]" must not trip
// it. Err toward precision; the Minister prompt's crisis rule handles nuance live.
const CRISIS_PATTERNS: RegExp[] = [
  /\bkill (?:myself|me)\b/,
  /\b(?:end|ending|take) (?:my|my own) life\b/,
  /\bend it all\b/,
  /\bwant to die\b/,
  /\bdon'?t want to (?:be here|live|wake up|exist)\b/,
  /\bbetter off (?:dead|without me)\b/,
  /\bsuicid/,                                  // suicide, suicidal
  /\bself[-\s]?harm\b/,
  /\b(?:cut|cutting|hurt|hurting) myself\b/,
  /\bno (?:reason|point) (?:to|in) (?:living|going on|carry on)\b/,
  /\bcan'?t (?:go on|do this anymore|take (?:it|this) anymore)\b/,
  /\bnothing (?:left|to live for)\b/,
  /\bgive up on (?:life|everything)\b/,
];
export function detectCrisis(text: string): boolean {
  if (!text) return false;
  const t = text.toLowerCase();
  return CRISIS_PATTERNS.some(re => re.test(t));
}

export const SIGNAL_REPORT_INSTRUCTION =
  '\n\n[SIGNAL REPORT — system instruction. The person never sees this.]\n' +
  'After your reply, on its own final line, output <signals>token,token</signals> ' +
  'with zero or more of EXACTLY these tokens for what THIS message genuinely revealed ' +
  'in the person\u2019s own words: ' + Array.from(VALID_REPORT_TOKENS).join(', ') + '. ' +
  'Be conservative — report only what their words clearly show, never what you hope. ' +
  'If none, output <signals>none</signals>. This line is stripped before display; ' +
  'never mention it and never let it change your tone.';

export function stripSignalReport(raw: string): { reply: string; found: string[] } {
  const found: string[] = [];
  const reply = (raw || '').replace(/<signals>([\s\S]*?)<\/signals>/gi, (_m, body: string) => {
    body.split(/[\s,]+/).forEach((tok) => {
      const k = tok.trim().toLowerCase();
      if (VALID_REPORT_TOKENS.has(k)) found.push(k);
    });
    return '';
  }).trim();
  return { reply, found };
}

// NO SOUL-SCORING (Cameron, June 2026): the former "judge" — a hidden instruction
// that asked the model to grade seven spirit levels and emit <traits> deltas — has
// been removed entirely. The app does not score anyone's Christlikeness. Routing
// comes only from the plain signals a person reveals (harvestSignals + the model's
// <signals> report), and everything recorded is shown openly on the Profile.

// Conservative keyword harvest — the fast, free backstop. The model report
// does the nuanced reading; this guarantees the engine hears even without it.
export function harvestSignals(text: string): string[] {
  const lower = (text || '').toLowerCase();
  const found: string[] = [];
  const sentences = lower.split(/[.!?\n]+/);

  // Per-sentence: the rejection must never silence the affirmation
  // ("a god who does that is not good. God is good though — the real one.")
  const NEG_GOOD = /\b(not|isn't|isnt|never|no)\s+good\b/;
  if (sentences.some((sn) =>
    /\bgod is good\b|\bhe sounds good\b|\bhe is good\b|\bgood god\b|\bknow that he was good\b/.test(sn) && !NEG_GOOD.test(sn)
  )) found.push('believes_god_good');

  if (/\bi want to believe\b|\bwant to know (him|god)\b|\bsee if there is a god that is good\b|\bwould love to know\b|\bshow me who (he|god) is\b/.test(lower)) found.push('open_to_god');

  // Per-sentence with negation guard: "I DON'T think God still speaks" is not openness.
  if (sentences.some((sn) =>
    (/\bstill speaks?\b|\bspeak today\b|\bis there more\b|\bmore than (the bible|i was (told|taught|handed))\b|\bwhat (do|does) (you|the people|they) (actually )?believe\b|\bwhy would (he|god) (ever )?(have )?stop\b/.test(sn)) &&
    !/\b(don'?t|doesn'?t|never|stopped|no longer|won'?t|isn'?t|not)\b/.test(sn)
  )) found.push('open_to_restoration');

  // A firm refusal to even examine the restored gospel — the "won't look" posture.
  // Conservative on purpose: only a clear refusal, never a soft "not right now."
  const refusesRestoration = /\b(i (won'?t|will not|am not going to|refuse to) (read|look at|open|consider|touch))\b|\bnot interested in (reading |looking at )?(the )?(book of mormon|joseph smith|your church|the restoration)\b|\bi don'?t (want|care) to (read|see|hear about) (it|that|the book|the book of mormon)\b/.test(lower);
  if (refusesRestoration) found.push('declined_restoration');
  // Curiosity about the Book of Mormon — but never when they are refusing it.
  if (/\bbook of mormon\b/.test(lower) && !refusesRestoration) found.push('curious_about_book_of_mormon');
  if (/\bdrawn to jesus\b|\bjesus sounds\b|\bi like jesus\b/.test(lower)) found.push('drawn_to_jesus');
  if (/\bget baptized\b|\bjoin the church\b|\bbecome a member\b/.test(lower)) found.push('wants_to_join');
  if (/\bgrie(f|ving)\b|\blost (my|someone)\b|\bpassed away\b/.test(lower)) found.push('carries_grief');
  if (/\bso lonely\b|\bi('m| am) (so )?alone\b/.test(lower)) found.push('lonely');

  // Frameworks (internal discernment — the framework, not the affirmation,
  // is the live picture of God; never spoken to the person):
  if (/\bcalvinis|\breformed\b|\bpredestin|\bthe elect\b|\btotal depravity\b|\bsovereign grace\b|\bunconditional election\b/.test(lower)) found.push('reformed_framework');
  if (/\ba god who (does|would do|did) that is not good\b|\bthat('s| is) not the god i\b|\bgod (is not|isn't|wouldn't be|would never be) like that\b|\bi (can('t|not)|don('t|not)) believe in a god who\b/.test(lower)) found.push('rejects_harsh_god');
  if (/\b(don'?t|do not) think of god as a person\b|\bgod (is|'s) not a person\b|\bno personal god\b|\bgod is (the universe|energy|everything|a force)\b/.test(lower)) found.push('nontheistic_framework');

  // BRIDGE ACCEPTANCES — only a clear AFFIRMATION counts, each guarded against
  // negation. These are the distinctively-LDS truths a seeker can reach on their
  // own; accepting one moves them from milk into the bridge (Cameron, 2026-06-26).
  // Continuing revelation — God still speaks today / the canon is open. (This is
  // an affirmation; the softer "is there more?" question stays open_to_restoration.)
  if (sentences.some((sn) =>
    (/\bgod still speaks?\b|\bstill speaking\b|\b(continuing|ongoing|modern|present.?day) revelation\b|\bspeaks? through (living )?prophets?( today)?\b|\bprophets? (still|today)\b|\bcanon is(n'?t| not) closed\b|\bnew (scripture|revelation)\b|\bgod (can|could|does) (still )?reveal\b|\brevelation (continues|hasn'?t stopped|never stopped)\b/.test(sn)) &&
    !/\b(don'?t|doesn'?t|do not|does not|never|stopped|no longer|won'?t|isn'?t|is not|not)\b/.test(sn)
  )) found.push('accepts_ongoing_revelation');
  // Rejection of creation ex nihilo — matter & intelligence are eternal; God
  // organized what already was rather than making it from nothing.
  if (sentences.some((sn) =>
    (/\b(matter|intelligence|our spirits?|our souls?|we) (is|are|were) eternal\b|\bwe existed before\b|\bpre.?mortal\b|\bpremortal\b|\b(lived|existed) before (this life|we were born|birth)\b|\bnot created (out )?of nothing\b|\b(creation|created|making something) (out )?of nothing (doesn'?t|does not|makes no|never made)\b|\bgod organized\b|\bex.?nihilo (doesn'?t|does not|makes no|can'?t|never)\b|\b(don'?t|do not) believe (in )?creation (out )?of nothing\b/.test(sn)) &&
    !/\bgod (created|made) everything (out )?of nothing\b/.test(sn)
  )) found.push('rejects_creation_ex_nihilo');

  // A named Christian tradition = a believer in Jesus (milk that fits them):
  if (/\b(baptist|catholic|methodist|presbyterian|pentecostal|evangelical|lutheran|orthodox|non.?denominational|christian church)\b/.test(lower)) found.push('believes_in_jesus');

  // Membership ONLY from the person's own self-identification (Law 3), and only
  // in the FIRST person about THEMSELVES. "my wife is a member", "I'm NOT a
  // member", or "I used to be" must never mint membership (a misroute lost a
  // tester — CLAUDE.md Law 8). We read the honest ways a Latter-day Saint says
  // who they are, then strip out negations and third-person mentions.
  const memberSelfId =
    /\b(i'?m|i am) (a |an )?(latter.?day saint|lds|mormon)\b/.test(lower) ||
    /\b(i'?m|i am) (a |an )?member of (the )?(church of jesus christ|lds church|restored church)/.test(lower) ||
    /\bi (belong to|am part of|am a part of|attend|go to) (the )?(church of jesus christ( of latter.?day saints)?|lds church|restored church)/.test(lower) ||
    // Unambiguously Latter-day Saint cultural markers ONLY. We deliberately do NOT
    // match bare "served a mission" or "hold the priesthood" — those are used by
    // other faiths too, and member status flips the WHOLE app, so it must be certain.
    // Member detection looks for exactly ONE religion's membership (Cameron, 2026-06-26):
    // every other tradition stays in the same non-member track and is treated the same.
    /\bmy ward\b|\brelief society\b|\bmy temple recommend\b|\bmy elders quorum\b|\bmy stake\b|\bsacrament meeting\b|\bcome.?follow.?me\b|\bserved a (full.?time )?mission for the church\b|\bi hold the (melchizedek|aaronic) priesthood\b/.test(lower);
  const memberNegated =
    /\b(not|never|no longer|isn'?t|aren'?t|wasn'?t|used to be|don'?t want to be)\b[^.!?]*\b(member|latter.?day saint|lds|mormon)\b/.test(lower) ||
    /\b(my|his|her|their|a) (wife|husband|spouse|friend|mom|mum|mother|dad|father|parents?|family|son|daughter|kids?|neighbou?r|coworker|boss|sister|brother) (is|was|are|were) (a |an )?(member|latter.?day saint|lds|mormon)\b/.test(lower);
  if (memberSelfId && !memberNegated) found.push('active_member');
  if ((/\b(grew up|raised) (as )?(lds|mormon|latter.?day saint|in the church)\b|\bless.?active\b|\binactive member\b|\b(i'?m|i am) (a |an )?(less.?active|inactive)\b|\bi left the church\b/.test(lower)) && !memberNegated) found.push('inactive_member');

  return found;
}

// Faith self-descriptions are kept verbatim in the person's faith record.
export const FAITH_ID_RE = /(calvinis|reformed|presbyterian|baptist|catholic|methodist|pentecostal|evangelical|lutheran|orthodox|non.?denominational|latter.day saint|\blds\b|mormon|my ward|atheist|agnostic|muslim|jewish|buddhist|hindu)/i;
