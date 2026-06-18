import { create } from 'zustand';
import { persist, createJSONStorage } from 'zustand/middleware';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { CONTENT, ContentItem, FeedTag } from '../data/content';
import {
  DialogueQuestion,
  TraitScores,
  DEFAULT_TRAITS,
  TRAIT_MIN,
  TRAIT_MAX,
  computeNextQuestion,
  QUESTION_BANK,
} from '../data/questionBank';
import {
  mayReferenceLds as engineMayReferenceLds,
  restorationReady as engineRestorationReady,
  spiritReady as engineSpiritReady,
  missionaryReferralReady as engineMissionaryReady,
  isMember as engineIsMember,
  assessJourney,
  assessConnection,
} from '../engine/connect';
import { MINISTER_SYSTEM_PROMPT, MINISTER_MODEL, CREATION_DILEMMA_REASONING } from '../engine/minister';
import {
  harvestSignals,
  stripSignalReport,
  stripTraitReport,
  stripIdentity,
  identityOnly,
  detectCrisis,
  SIGNAL_REPORT_INSTRUCTION,
  TRAIT_REPORT_INSTRUCTION,
  FAITH_ID_RE,
} from '../engine/chatEar';
import {
  EXERCISES,
  pickExercise,
  SpiritualExercise,
} from '../engine/exercises';
import {
  sendMessage as cloudSendMessage,
  fetchThread as cloudFetchThread,
  markRepliesRead as cloudMarkRead,
  subscribeToThread as cloudSubscribe,
  isMessagingConfigured,
  InboxMessage,
  LEGACY_THREAD_ID,
} from '../lib/messaging';

// ── Constants ───────────────────────────────────────────────────────────────

/**
 * INVISIBLE EMERGENT ROUTING — there is no ladder the user climbs.
 *
 * The retired FEED_PROGRESSION gate system (MILK→BRIDGE→RESTORATION→MAINTENANCE
 * with graduation thresholds and "you haven't unlocked this yet" buttons) was a
 * pharisaical hurdle, not Jesus's method. It is gone. Routing now happens silently
 * from the signals a person reveals, and it ALWAYS obeys the milk-before-meat law:
 * RESTORATION content never surfaces until both readiness signals are present.
 *
 * `keepSimple` / `goDeeper` remain as ungated USER preferences (gentler vs. more
 * substantive) — never as spiritual gates a person must pass.
 */

// Re-exported so screens have one source of truth for the milk gate + journey.
// isRestorationReady === the milk gate (both readiness signals present).
export const isRestorationReady = engineMayReferenceLds;
export const isMissionaryReady  = engineMissionaryReady;
export const isMemberSignal     = engineIsMember;
export { assessJourney, assessConnection };

// EXPLICIT CONSENT (Cameron, June 2026): even once the readiness signals are
// present, restoration-tagged content NEVER auto-surfaces in the feed. The Minister
// AI asks the person, in plain words, whether they want the restored perspective;
// only an affirmative "yes" flips this. This is what keeps the whole thing grace,
// not hidden leading — the person chooses to walk through the door. It is a module
// flag (not threaded through every call site) kept in sync with the persisted
// `restorationConsent` by the store: set on rehydrate and on grant/decline.
export type RestorationConsent = 'unknown' | 'granted' | 'declined';
let restorationConsentGranted = false;
export function setRestorationConsentGranted(v: boolean) { restorationConsentGranted = v; }

// Silently choose the content level that fits the signals a person has revealed.
// Invisible: the user never sees a tier name or a gate. The milk law is absolute —
// RESTORATION is only ever chosen once both readiness signals exist AND the person
// has explicitly consented to the restored perspective.
function routeFeedTag(signals: string[]): FeedTag {
  if (engineIsMember(signals)) return 'MAINTENANCE';

  const analytical = ['skeptical_of_god', 'analytical_doubt', 'honest_inquiry', 'losing_faith'];
  const hasAnalytic = signals.some(s => analytical.includes(s));

  // Meat only after milk AND after the person has said yes to the restored view.
  // Until they consent we keep them on the gentlest fitting milk track (never
  // RESTORATION), so nothing restoration-tagged appears before they choose it.
  if (engineMayReferenceLds(signals) && restorationConsentGranted) return 'RESTORATION';
  if (hasAnalytic) return 'BRIDGE';
  return 'MILK'; // default: start gentle, always
}

// The new onboard choices carry a feedTag directly on the choice object.
// completeOnboarding now accepts feedTag directly from the story choice.
// For free-text (key='E'), we infer from language.
function inferTagFromText(text: string): FeedTag {
  const lower = text.toLowerCase();

  const memberKw      = ['lds', 'latter', 'member', 'temple', 'ward', 'mission', 'covenant', 'priesthood', 'Relief Society'];
  const bridgeKw      = ['doubt', 'science', 'evidence', 'proof', 'atheist', 'skeptic', 'question', 'wonder', 'not sure', 'religion'];
  const burdenKw      = ['lost', 'alone', 'broken', 'hurt', 'pain', 'grief', 'heavy', 'scared', 'desperate', 'struggling'];
  const maintenanceKw = ['deepen', 'grow', 'stronger', 'scripture', 'faith', 'believe', 'gospel', 'church'];

  let mScore = 0, bScore = 0, burdenScore = 0, maintScore = 0;
  memberKw.forEach(kw      => { if (lower.includes(kw)) mScore++; });
  bridgeKw.forEach(kw      => { if (lower.includes(kw)) bScore++; });
  burdenKw.forEach(kw      => { if (lower.includes(kw)) burdenScore++; });
  maintenanceKw.forEach(kw => { if (lower.includes(kw)) maintScore++; });

  const max = Math.max(mScore, bScore, burdenScore, maintScore);
  if (max === 0) return 'MILK'; // default: start gentle
  if (mScore === max)      return 'MAINTENANCE';
  if (maintScore === max)  return 'MAINTENANCE';
  if (bScore === max)      return 'BRIDGE';
  return 'MILK';
}

// ── Feed helpers ─────────────────────────────────────────────────────────────

// Fair shuffle (Fisher–Yates) — an even mix, no bias from sort-comparator tricks.
function shuffle<T>(arr: T[]): T[] {
  const a = [...arr];
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

// The pool a track draws from — the milk/meat standard. Meat-ready tracks (a
// member, or someone the restored gospel has been opened to) see the FULL table:
// the 100 milk AND the 100 meat (200 in all). Everyone else sees the 100 milk.
// Legacy tags map onto the two tracks: MILK/BRIDGE -> milk; RESTORATION/
// MAINTENANCE -> milk + meat.
function poolForTag(tag: FeedTag): ContentItem[] {
  const milk = CONTENT.filter(c => c.track === 'MILK');
  const meat = CONTENT.filter(c => c.track === 'MEAT');
  const meatReady = tag === 'MAINTENANCE' || tag === 'RESTORATION';
  // Fallback: if track isn't set on any item (older data), use the legacy tag pool
  // so the feed is never empty.
  if (milk.length === 0 && meat.length === 0) return CONTENT.filter(c => c.tag === tag);
  return meatReady ? [...milk, ...meat] : milk;
}

// Draw the next 5 cards. THE HARD RULE (Cameron's standard): never show an item
// the person has already seen until they have seen them ALL. Only once every item
// in the pool has been seen does a fresh cycle begin. 'seenIds' holds everything
// already shown; callers fold the shown page into it (see refreshFeed/markOpened).
function buildFeed(tag: FeedTag, seenIds: Set<number>): ContentItem[] {
  const pool   = poolForTag(tag);
  const unseen = pool.filter(c => !seenIds.has(c.id));
  // Exhausted -> begin a new cycle from the whole pool; otherwise only the unseen.
  const source = unseen.length > 0 ? unseen : pool;
  return shuffle(source).slice(0, 5);
}

// User-initiated "show me something more substantive" — a preference, not a gate.
// It still obeys the milk law: it will not jump to RESTORATION unless the person's
// signals have opened that door. It nudges one honest step (MILK→BRIDGE), and only
// reaches RESTORATION when both readiness signals are present.
function deeperFeedTag(current: FeedTag, signals: string[]): FeedTag {
  if (engineIsMember(signals)) return 'MAINTENANCE';
  if (current === 'MILK') return 'BRIDGE';
  if (current === 'BRIDGE') {
    // Even "show me deeper" cannot reach RESTORATION without explicit consent.
    return (engineMayReferenceLds(signals) && restorationConsentGranted) ? 'RESTORATION' : 'BRIDGE';
  }
  return current;
}

// ── Journal & Chat types ─────────────────────────────────────────────────────

export interface JournalEntry {
  id:        string;
  promptId:  string;
  promptText: string;
  text:      string;
  timestamp: number;
}

export interface ChatMessage {
  id:        string;
  role:      'user' | 'assistant';
  text:      string;
  timestamp: number;
  // 'meta' = a quiet system note shown in the thread (e.g. a spirit-level change)
  // that is NOT part of the conversation sent to the model.
  kind?:     'meta';
}

/**
 * A saved past conversation, kept so the person can reopen any of them from a
 * history dropdown on the Ask page (Cameron's ask). The live conversation stays
 * in `chatMessages`; when they start a new chat or open an old one, the current
 * thread is archived here as a titled ChatSession.
 */
export interface ChatSession {
  id:        string;
  title:     string;   // the first thing they said, trimmed — a scannable title
  createdAt: number;
  updatedAt: number;
  messages:  ChatMessage[];
}

// Fire a notification when a real person replies. On web this uses the browser
// Notification API (asking permission once); on native it is a no-op for now —
// true background phone push needs a push service + device tokens (Phase 2), which
// is a separate backend build. This at least alerts the person while the app's open.
function notifyRealPersonReply(body: string) {
  try {
    const N: any = (globalThis as any).Notification;
    if (!N) return;
    const show = () => { try { new N('A real person replied', { body: (body || '').slice(0, 140) }); } catch {/* noop */} };
    if (N.permission === 'granted') show();
    else if (N.permission !== 'denied') N.requestPermission().then((p: string) => { if (p === 'granted') show(); });
  } catch {/* notifications unavailable — fine */}
}

// A short, scannable title for a saved conversation, auto-made from the first
// thing said in it — cleaned of quotes and the "talk about it" lead-ins, capped,
// so the history list reads like a list of topics, not raw message text.
function titleFromText(t: string): string {
  let clean = (t || '').replace(/\s+/g, ' ').trim();
  clean = clean
    .replace(/^earlier in my story i shared this:\s*/i, '')
    .replace(/^i was talking with the app and asked:\s*/i, '')
    .replace(/^[“"']+/, '')
    .trim();
  const firstSentence = clean.split(/[.?!]\s/)[0] || clean;
  const capped = firstSentence.length > 56 ? firstSentence.slice(0, 56).trim() + '…' : firstSentence;
  return capped.replace(/[“"']+$/, '').trim() || 'Conversation';
}

// A fresh id for a brand-new real-person conversation.
function newRealThreadId(): string {
  return `t_${Date.now().toString(36)}_${Math.random().toString(36).slice(2, 7)}`;
}

/**
 * A single real-person conversation, summarized for the history list. The person
 * can now hold MANY separate threads with a real human (Cameron's ask) — each one
 * titled, each one with its own unread count, the most recently active on top.
 */
export interface RealThread {
  id:        string;
  title:     string;
  messages:  InboxMessage[];
  lastBody:  string;
  lastAt:    string;       // ISO of the newest message
  lastSender: 'user' | 'admin';
  unread:    number;       // admin replies the person hasn't seen yet, this thread
}

// Group the flat message list into per-conversation threads, newest activity first.
// Title comes from the first message that carries a thread_title; otherwise the
// first thing the person said in that thread, so legacy threads read well too.
export function selectRealThreads(messages: InboxMessage[]): RealThread[] {
  const byThread = new Map<string, InboxMessage[]>();
  for (const m of messages) {
    const tid = m.thread_id || LEGACY_THREAD_ID;
    if (!byThread.has(tid)) byThread.set(tid, []);
    byThread.get(tid)!.push(m);
  }
  const threads: RealThread[] = [];
  byThread.forEach((msgs, id) => {
    const ordered = [...msgs].sort((a, b) => +new Date(a.created_at) - +new Date(b.created_at));
    const titled  = ordered.find(m => !!m.thread_title)?.thread_title;
    const firstUser = ordered.find(m => m.sender === 'user' && m.body.trim());
    const title   = titled || titleFromText(firstUser?.body || ordered[0]?.body || 'Conversation');
    const last    = ordered[ordered.length - 1];
    threads.push({
      id,
      title,
      messages:   ordered,
      lastBody:   last?.body || '',
      lastAt:     last?.created_at || new Date().toISOString(),
      lastSender: last?.sender === 'admin' ? 'admin' : 'user',
      unread:     ordered.filter(m => m.sender === 'admin' && !m.read_by_user).length,
    });
  });
  threads.sort((a, b) => +new Date(b.lastAt) - +new Date(a.lastAt));
  return threads;
}

/**
 * A request to talk to a real person, captured ON-DEVICE.
 *
 * Phase 1 holds these locally and honestly tells the person a real human will
 * reach out — instead of throwing them into a blank email draft (a dead-end
 * mailto link). The real delivery channel (a small send service to Cameron's
 * inbox / an admin queue) slots in here later WITHOUT changing the UI: this is
 * the queue that channel will read from.
 */
export interface ConnectRequest {
  id:           string;
  note:         string;          // what the person wants to say (may be empty)
  journeyStage: string;          // where they are, for triage in admin
  conversationId: string;        // ties the request to this install/user
  timestamp:    number;
  delivered:    boolean;         // flips true once a real channel sends it
}

// A faith self-description, kept VERBATIM in the person's own words. Never a
// label — the exact phrase they used. Surfaced back to them in the profile
// ("YOUR FAITH, AS YOU'VE TOLD IT") so they feel heard, never categorized.
export interface FaithWord {
  text: string;
  ts:   number;
  // The routing signals THIS line taught the engine. Stored so that editing or
  // removing the line can take its signals back — the app un-learns honestly,
  // instead of holding onto what a person has since deleted. Legacy lines saved
  // before provenance existed have no signals and simply contribute nothing.
  signals?: string[];
}

// A recorded shift in what the person believes — kept so a changed mind is HONORED
// and stays visible, not silently overwritten (Cameron's #7). When someone revises
// a faith line, the old wording and the new are both held, with a date.
export interface BeliefChange {
  from: string;
  to:   string;
  ts:   number;
}

// A titled fragment of the person's story, in their own words — "YOUR STORY SO
// FAR". The minister is told these exist so it can never claim it cannot see
// their story.
export interface StoryMoment {
  title: string;
  text:  string;
  ts:    number;
}

// Lightweight return-visit memory so a person is never met with a cold restart.
export interface SessionMemory {
  lastSeen:  number;
  lastWords: string;  // the last thing they said, to gently recall on return
}

// A note the person CHOSE to keep — clipped from anywhere they were learning
// (a feed reading, something the minister said in chat, a story, a blessing).
// The app summarizes what was learned into a short `summary` clip so the notes
// page reads like a record of growth, while `body` keeps the full original so
// they can expand and re-read it. Saving a note carries them to the Journal,
// which opens to the new note.
export type NoteSource = 'feed' | 'chat' | 'blessing' | 'story' | 'dialogue';

export interface LearnedNote {
  id:        string;
  source:    NoteSource;
  title:     string;       // short heading — the content's title, or where it came from
  summary:   string;       // the clip: what they can take from it (AI; excerpt offline)
  body:      string;       // the full original text, kept so they can expand and re-read
  timestamp: number;
  pending:   boolean;      // true while the AI summary is still being written
}

// ── AI voice (key-safe: the app NEVER holds the Anthropic key) ───────────────
// The key lives only on the server (server/index.js, /api/chat). The app posts
// {system, messages} to the proxy and the proxy adds the key. The proxy URL is
// NOT a secret, so it is a normal public env var (mobile/.env):
//   EXPO_PUBLIC_MBM_API_URL=https://your-app.up.railway.app
// A direct-to-Anthropic key is supported ONLY for local dev and is never shipped.
const MBM_API_URL       = (process.env.EXPO_PUBLIC_MBM_API_URL ?? '').trim().replace(/\/+$/, '');
const ANTHROPIC_API_KEY = (process.env.EXPO_PUBLIC_ANTHROPIC_API_KEY ?? '').trim();
const ANTHROPIC_URL     = 'https://api.anthropic.com/v1/messages';
const ANTHROPIC_MODEL   = MINISTER_MODEL;
const ANTHROPIC_VERSION = '2023-06-01';
const MAX_REPLY_TOKENS  = 512;

function generateId(): string {
  return Math.random().toString(36).slice(2) + Date.now().toString(36);
}

// Avoid handing back the same blessing twice in a row, so the encouragement
// never feels canned. Tracks only the last line shown, across all pools.
let lastBlessing = '';
function pickLine(pool: string[]): string {
  if (pool.length === 0) return '';
  const fresh = pool.filter(l => l !== lastBlessing);
  const choices = fresh.length > 0 ? fresh : pool;
  const line = choices[Math.floor(Math.random() * choices.length)] ?? '';
  lastBlessing = line;
  return line;
}

// ── Personalized blessings — one honest word, or silence ─────────────────────
// There is NO fixed list of compliments and NO instant pre-show. The AI (as a
// disciple) reads what the person ACTUALLY said and gives ONE of three honest
// responses: a warm, specific affirmation; a firm, loving correction if they
// were proud or cruel; or nothing at all if it was a non-answer. It is handed
// every blessing it has ever spoken so it never repeats itself or sounds canned.
export type BlessKind = 'dialogue' | 'heart' | 'journal';

// A blessing now stays on screen until the person swipes it — left to dismiss,
// right to carry it into chat. So it must remember WHAT it was about (the
// question and their answer), not just the line, so a tap-to-talk opens a real
// conversation about that exact moment.
export interface BlessingCard {
  line:      string;       // the one honest word (affirmation or loving correction)
  kind:      BlessKind;
  question?: string;       // what prompted it — the dialogue question / content kept
  answer?:   string;       // what the person actually said or chose, if anything
}

const BLESS_KIND_FRAME: Record<BlessKind, string> = {
  dialogue: 'just answered a tender, honest question about their life and faith',
  heart:    'was moved by something they read here and chose to keep it',
  journal:  'wrote something true and vulnerable in their private journal',
};

// Tidy the model's line: strip wrapping quotes, any leaked label, collapse
// whitespace, drop a trailing question (a blessing affirms, it does not ask),
// cap the length, AND honor the model choosing silence (the lone word NONE).
function cleanBlessing(raw: string): string {
  let s = (raw || '').trim();
  s = s.replace(/^["'“”\s]+|["'“”\s]+$/g, '').trim();
  s = s.replace(/\s+/g, ' ');
  if (!s) return '';
  if (/^\(?\s*none[\s.)]*$/i.test(s)) return '';   // the disciple chose silence
  if (s.length > 220) s = s.slice(0, 217).trimEnd() + '…';
  if (/\?$/.test(s)) return '';            // never end a blessing on a question
  return s;
}

export async function generateBlessing(
  kind: BlessKind,
  context: string,
  recentLines: string[] = [],
): Promise<string | null> {
  const useProxy = !!MBM_API_URL;
  if (!useProxy && !ANTHROPIC_API_KEY) return null;   // offline → say nothing

  // Working memory: the disciple sees what it has already said and must not
  // repeat any of it, in wording, shape, or opening — so it never sounds rehearsed.
  const recent = recentLines.filter(Boolean).slice(-40);
  const memoryNote = recent.length
    ? '\n\nYou have ALREADY spoken these blessings before. Do NOT repeat any of them, ' +
      'and do not reuse their wording, sentence shape, or opening — say something genuinely ' +
      'new:\n- ' + recent.map(l => l.replace(/\s+/g, ' ').trim()).join('\n- ')
    : '';

  const system =
    'You are a disciple of Jesus — the honest friend who just watched a person who ' +
    BLESS_KIND_FRAME[kind] + '. Read what they ACTUALLY said and respond the way Jesus ' +
    'would to THAT person in THAT moment. Never a generic compliment.\n\n' +
    'Choose ONE of three honest responses:\n' +
    '1) GENUINE — if they were honest, searching, or vulnerable even a little: speak ONE ' +
    'short sentence (two at most) that affirms THEM specifically, naming the real good you ' +
    'saw in what they said. Tender, personal, unrehearsed.\n' +
    '2) PROUD — if what they wrote was self-righteous, contemptuous, cruel, or twists God ' +
    'into a weapon (the spirit of the Pharisee): do NOT flatter them. Speak ONE firm, ' +
    'loving, truthful sentence that gently exposes it, the way Jesus answered the proud. ' +
    'Honest — never cruel in return.\n' +
    '3) HOLLOW — if it was lazy, evasive, joking, or simply not a real answer: output ' +
    'exactly NONE and nothing else. Silence is the right and normal response to a ' +
    'non-answer; never manufacture praise no one reached for.\n\n' +
    'This line now STAYS on their screen until they choose to swipe it away — and they ' +
    'can swipe it INTO a conversation to talk about it with you. So it is read slowly, ' +
    'sat with, and may open a real talk. Weigh it accordingly: an affirmation must be ' +
    'true enough to rest on, and a correction must be careful, respectful, and worth ' +
    'opening a conversation over — the way Jesus weighed what He said to a person He ' +
    'knew would carry it. Make it land honestly and be worth remembering; never careless.\n\n' +
    'Never quote chapter and verse, never preach, never give a to-do, never ask a question. ' +
    'Speak straight to them as "you". No greeting, no preamble, no quotation marks, no ' +
    'emojis, no numbers. Output ONLY the single line — or the lone word NONE.' +
    memoryNote;
  const ctx = (context || '').trim().slice(0, 280);
  // Be ACCURATE about what the context is, per kind — a heart is content they
  // kept, not words they wrote, so the disciple never praises them for authoring
  // something they only reached for.
  const userText = ctx
    ? (kind === 'heart'
        ? 'The piece that moved them, which they chose to keep: "' + ctx + '"'
        : 'What they just said, in their own words: "' + ctx + '"')
    : 'They took a step here but said almost nothing about it.';

  try {
    let raw = '';
    if (useProxy) {
      const r = await fetch(`${MBM_API_URL}/api/chat`, {
        method: 'POST',
        headers: { 'content-type': 'application/json' },
        body: JSON.stringify({ system, messages: [{ role: 'user', content: userText }], max_tokens: 120 }),
      });
      if (!r.ok) return null;
      const d = await r.json();
      raw = typeof d?.text === 'string' ? d.text : '';
    } else {
      const r = await fetch(ANTHROPIC_URL, {
        method: 'POST',
        headers: {
          'content-type': 'application/json',
          'x-api-key': ANTHROPIC_API_KEY,
          'anthropic-version': ANTHROPIC_VERSION,
          'anthropic-dangerous-direct-browser-access': 'true',
        },
        body: JSON.stringify({
          model: ANTHROPIC_MODEL,
          max_tokens: 120,
          system,
          messages: [{ role: 'user', content: userText }],
        }),
      });
      if (!r.ok) return null;
      const d = await r.json();
      raw = Array.isArray(d?.content)
        ? d.content.filter((b: any) => b?.type === 'text').map((b: any) => b?.text ?? '').join('')
        : '';
    }
    const cleaned = cleanBlessing(raw);
    return cleaned || null;
  } catch {
    return null;
  }
}

// ── Note summaries — a short, honest "what you can take from this" ───────────
// When a person keeps a note, the app reads the source and writes ONE or TWO
// plain sentences naming what is worth remembering. Never flowery, never a
// sermon. Offline, the note simply keeps a trimmed excerpt instead (see
// excerptFallback), so a saved note is always useful even with no connection.
function excerptFallback(body: string): string {
  const s = (body || '').replace(/\s+/g, ' ').trim();
  if (s.length <= 160) return s;
  return s.slice(0, 157).trimEnd() + '…';
}

const NOTE_SOURCE_FRAME: Record<NoteSource, string> = {
  feed:     'a scripture-based reading they were studying',
  chat:     'something said in their conversation with the app',
  blessing: 'a word of encouragement that landed on them',
  story:    'a story about Jesus they just experienced',
  dialogue: 'a tender question about their faith they just answered',
};

// Strip wrapping quotes / a leaked label, collapse whitespace, cap the length.
function cleanSummary(raw: string): string {
  let s = (raw || '').trim();
  s = s.replace(/^["'“”\s]+|["'“”\s]+$/g, '').trim();
  s = s.replace(/\s+/g, ' ');
  if (!s) return '';
  if (s.length > 240) s = s.slice(0, 237).trimEnd() + '…';
  return s;
}

export async function generateNoteSummary(
  source: NoteSource,
  title: string,
  body: string,
): Promise<string | null> {
  const useProxy = !!MBM_API_URL;
  if (!useProxy && !ANTHROPIC_API_KEY) return null;   // offline → keep the excerpt

  const system =
    'A person is keeping a note so they can remember something they were learning ' +
    'in a gospel app. The source is ' + NOTE_SOURCE_FRAME[source] + '. Read it and ' +
    'write ONE or TWO plain sentences that capture what is worth remembering — the ' +
    'truth, comfort, or lesson in it — in warm, simple language they would be glad ' +
    'to reread later. Speak to them as "you." Do NOT add scripture they did not ' +
    'mention, do not preach, do not greet, and do not use quotation marks. Just the ' +
    'note itself, nothing else.';

  const userText =
    (title ? 'Title: ' + title + '\n\n' : '') +
    'What they kept:\n"' + (body || '').trim() + '"';

  try {
    let raw = '';
    if (useProxy) {
      const r = await fetch(`${MBM_API_URL}/api/chat`, {
        method: 'POST',
        headers: { 'content-type': 'application/json' },
        body: JSON.stringify({ system, messages: [{ role: 'user', content: userText }], max_tokens: 160 }),
      });
      if (!r.ok) return null;
      const d = await r.json();
      raw = typeof d?.text === 'string' ? d.text : '';
    } else {
      const r = await fetch(ANTHROPIC_URL, {
        method: 'POST',
        headers: {
          'content-type': 'application/json',
          'x-api-key': ANTHROPIC_API_KEY,
          'anthropic-version': ANTHROPIC_VERSION,
          'anthropic-dangerous-direct-browser-access': 'true',
        },
        body: JSON.stringify({
          model: ANTHROPIC_MODEL,
          max_tokens: 160,
          system,
          messages: [{ role: 'user', content: userText }],
        }),
      });
      if (!r.ok) return null;
      const d = await r.json();
      raw = Array.isArray(d?.content)
        ? d.content.filter((b: any) => b?.type === 'text').map((b: any) => b?.text ?? '').join('')
        : '';
    }
    const cleaned = cleanSummary(raw);
    return cleaned || null;
  } catch {
    return null;
  }
}

// Small, clamped trait nudge — the way the prototype's nudgedTraits worked.
function nudgeTraits(scores: TraitScores, deltas: Partial<TraitScores>): TraitScores {
  const next: TraitScores = { ...scores };
  for (const [k, d] of Object.entries(deltas)) {
    const key = k as keyof TraitScores;
    const cur = next[key] ?? 0;
    next[key] = Math.round(Math.max(TRAIT_MIN, Math.min(TRAIT_MAX, cur + (d ?? 0))) * 1000) / 1000;
  }
  return next;
}

// Plain-English names for the spirit levels, used when telling the person — to
// their face — that the judge just moved one, so a deduction is never silent.
// Settled in the design-tab conversation (the binding standard): every dimension
// is named as a CHRISTLIKE measure, so the label and the number always agree — the
// score reads as "how close to Christ's own," never a bare verdict on a person's
// worth. This is the rename that makes the capped scale honest. Do not drop the
// "Christlike" prefix from any of these.
const TRAIT_DISPLAY: Record<keyof TraitScores, string> = {
  honest_inquiry: 'Christlike honesty',
  openness:       'Christlike openness',
  humility:       'Christlike humility',
  hunger:         'Christlike hunger for truth',
  compassion:     'Christlike compassion',
  courage:        'Christlike courage',
  sincerity:      'Christlike sincerity',
};

// Format a level change for display: a real minus sign, no trailing ".0".
function fmtDelta(d: number): string {
  const v = Math.round(Math.abs(d) * 10) / 10;
  const num = Number.isInteger(v) ? String(v) : v.toFixed(1);
  return (d > 0 ? '+' : '−') + num;
}

// Merge newly-heard signals into the existing set without duplicates. The engine
// laws (two-witnesses for god-good, framework blocking, member-only self-ID) all
// live in connect.ts and read the full set — so a plain union is safe here: a
// single hint can never by itself open a gate.
function mergeSignals(existing: string[], incoming: string[]): string[] {
  const set = new Set(existing);
  incoming.forEach(s => { if (s) set.add(s); });
  return Array.from(set);
}

// ── Signal provenance ────────────────────────────────────────────────────────
// dialogueSignals is no longer the source of truth — it is DERIVED. Two sources
// feed it:
//   • baseSignals      — everything NOT from a faith self-description (onboarding
//                        choices, dialogue answers, journal, exercise outcomes,
//                        the model's signal report). These are sticky: the app
//                        does not un-hear what a person freely showed elsewhere.
//   • each FaithWord's signals — what that specific faith line taught.
// dialogueSignals = baseSignals ∪ (every faith line's signals). When a person
// edits or removes a faith line, its signals leave the union, so the routing can
// honestly settle back to what their remaining words justify (it may move the
// feed toward milk again — that is correct, not a bug). A signal that ALSO came
// from a non-faith source stays, because it still lives in baseSignals.
function faithSignalUnion(words: FaithWord[]): string[] {
  const out: string[] = [];
  for (const w of words) {
    for (const s of w.signals ?? []) {
      if (s && !out.includes(s)) out.push(s);
    }
  }
  return out;
}

function composeSignals(baseSignals: string[], words: FaithWord[]): string[] {
  return mergeSignals(baseSignals, faithSignalUnion(words));
}

// Faith IDENTITY (who someone is with regard to faith) never lives in the sticky
// base set — it is owned by the person's own faith words so it can change when
// they do. When identity arrives through a dialogue choice or a chat self-ID,
// capture it onto a verbatim faith line so it stays visible AND removable.
function captureIdentityWord(verbatim: string, signals: string[]): FaithWord | null {
  const identity = identityOnly(signals);
  if (!identity.length) return null;
  const text = (verbatim ?? '').trim().slice(0, 140);
  if (!text) return null;
  return { text, ts: Date.now(), signals: identity };
}

// Plain-language faith line for an identity token — used only by the legacy
// migration, to re-home identity that older builds left stuck in the flat
// signal set. Phrased in the first person so it reads as the person's own line
// on the faith card, where they can correct or remove it like any other.
const IDENTITY_LABELS: Record<string, string> = {
  active_member:          "I'm a Latter-day Saint.",
  inactive_member:        'I grew up Latter-day Saint.',
  active_faith_tradition: "I'm part of a church or faith community.",
  has_history_with_faith: 'I have a history with faith.',
  believes_in_jesus:      'I believe in Jesus.',
};

// Turn orphaned legacy identity tokens into one synthesized faith line so the
// person can SEE and REMOVE what the app thinks of them. Returns null if none.
function identityWordFromTokens(tokens: string[]): FaithWord | null {
  const identity = identityOnly(tokens);
  if (!identity.length) return null;
  const text = identity.map(t => IDENTITY_LABELS[t]).filter(Boolean).join(' ').slice(0, 140);
  if (!text) return null;
  return { text, ts: Date.now(), signals: identity };
}

// ── State shape ──────────────────────────────────────────────────────────────

interface AppState {
  // Session
  onboardingComplete: boolean;
  onboardingChoice:   string | null;
  conversationId:     string;   // stable ID per install — ties all messages to one user in admin

  // Feed
  feedTag:           FeedTag;
  feed:              ContentItem[];
  seenIds:           Set<number>;
  openedIds:         Set<number>;
  positiveCount:     number;

  // UI state
  showTalkToSomeone: boolean;

  // Dialogue engine
  dialogueSignals:     string[];   // DERIVED: baseSignals ∪ every faith line's signals
  baseSignals:         string[];   // non-faith signals (see composeSignals)
  answeredQuestionIds: number[];
  traitScores:         TraitScores;
  currentQuestion:     DialogueQuestion | null;

  // Explicit consent for the restored perspective. 'granted' is the ONLY value that
  // ever lets restoration-tagged content into the feed (on top of the readiness
  // signals). The Minister AI asks; the person answers; this records their choice.
  restorationConsent:  RestorationConsent;

  // Journal
  journalEntries:      JournalEntry[];
  answeredPromptIds:   string[];

  // Notes the person kept from around the app (feed, chat, stories, blessings).
  // `pendingNoteId` is the note the Journal should open to right after a save —
  // ephemeral nav state, never persisted.
  learnedNotes:        LearnedNote[];
  pendingNoteId:       string | null;

  // Chat
  chatMessages:        ChatMessage[];   // the live, currently-open conversation
  chatLoading:         boolean;
  // A stable id for the live conversation, so an in-flight AI answer can be routed
  // back to the chat it was asked in — even if the person started or opened a
  // different chat while it was loading (fixes the cross-populated-answer bug).
  activeChatId:        string;
  chatSessions:        ChatSession[];   // saved past conversations, newest first

  // Every blessing line ever spoken — the disciple's working memory, so it
  // never repeats a compliment or sounds rehearsed.
  blessingHistory:     string[];

  // Human connection requests, captured on-device (Phase 1). This is the OFFLINE
  // fallback queue; when the cloud inbox is configured and reachable, messages go
  // there too so a real person can reply back INTO the app.
  connectRequests:     ConnectRequest[];

  // The two-way human inbox (server-sourced, never persisted — reloaded on open).
  // `inboxMessages` holds EVERY message across ALL of this person's real-person
  // conversations; the app groups them into separate threads with selectRealThreads.
  inboxMessages:       InboxMessage[];
  inboxLoading:        boolean;
  inboxUnread:         number;   // admin replies the person hasn't seen yet (all threads)
  // Which real-person conversation is currently open. null = show the thread list /
  // start a new one. A fresh id here (not yet in inboxMessages) means "new chat."
  activeRealThreadId:  string | null;

  // The person, in their own words — never labels, never numbers shown to them
  name:                string | null;
  faithWords:          FaithWord[];
  beliefHistory:       BeliefChange[];   // honored record of changed minds (#7)
  moments:             StoryMoment[];

  // Spiritual exercises (invite → try → report → learn)
  activeExercise:      SpiritualExercise | null;
  acceptedSession:     number | null;   // which session # the active exercise was accepted in
  doneExerciseIds:     string[];

  // Session counter — increments once per app launch, so a follow-up becomes "due"
  // only after the person went away and came back (prototype's `session`).
  sessionCount:        number;

  // Return-visit memory (no cold restarts)
  session:             SessionMemory | null;

  // A blessing card — words only. Stays until the person swipes it (left to
  // dismiss, right to carry it into chat).
  blessing:            BlessingCard | null;

  // A draft pre-filled into Chat from a "Talk about it" / "Ask about this" tap.
  chatDraft:           string;
}

interface AppActions {
  // choice = story choice key (A/B/C/D/E), feedTag = direct override from story choice
  completeOnboarding:  (choice: string, freeText?: string, feedTag?: FeedTag, signal?: string) => void;
  markOpened:          (id: number) => void;
  thumbsUp:            (id: number) => void;
  bookmark:            (id: number) => void;
  keepSimple:          () => void;
  goDeeper:            () => void;
  grantRestorationConsent:   () => void;
  declineRestorationConsent: () => void;
  refreshFeed:         () => void;
  resetSession:        () => void;
  answerQuestion:      (questionId: number, answerValue: string, answerText?: string) => void;
  addJournalEntry:     (promptId: string, promptText: string, text: string) => void;
  // Keep a note from anywhere in the app. Returns the new note's id so the caller
  // can navigate to the Journal, which opens to it. The AI summary fills in after.
  saveLearnedNote:     (input: { source: NoteSource; title: string; body: string }) => string;
  clearPendingNote:    () => void;
  sendChatMessage:     (text: string) => Promise<void>;
  setChatLoading:      (loading: boolean) => void;
  appendAssistantMessage: (text: string) => void;
  appendAssistantToChat: (chatId: string, text: string, kind?: 'meta') => void;
  appendMetaMessage:   (text: string) => void;
  // Conversation history: archive the live thread and start fresh, or reopen a
  // past conversation from the history dropdown on the Ask page.
  newChat:             () => void;
  openChat:            (id: string) => void;
  submitConnectRequest: (note: string) => void;
  // Two-way human inbox (now multi-thread)
  sendConnectMessage:  (note: string, excerpt?: string, priority?: string) => Promise<void>;
  // Start a brand-new, separate conversation with a real person. Returns its id.
  newRealPersonThread: () => string;
  // Open one of the existing real-person conversations from the history list.
  openRealPersonThread: (id: string) => void;
  // Back out to the conversation list (no conversation open).
  closeRealPersonThread: () => void;
  // Carry the CURRENT ai conversation to a real person: summarize the AI's answer,
  // open a NEW titled real-person thread with it, and leave it waiting for a reply.
  escalateToRealPerson: () => Promise<boolean>;
  loadInbox:           () => Promise<void>;
  markInboxRead:       () => void;
  startInboxSubscription: () => () => void;
  setName:             (name: string) => void;
  recordFaithBackground: (choiceKey: string, text: string) => void;
  editFaithWord:       (index: number, text: string) => void;
  removeFaithWord:     (index: number) => void;
  addFaithWord:        (text: string) => void;
  deleteBeliefChange:  (ts: number) => void;
  addMoment:           (title: string, text: string) => void;
  // Keep the person dynamic, never boxed: everything learned or saved can be
  // edited or deleted. Deleting truly forgets it (un-learns that piece).
  deleteMoment:        (ts: number) => void;
  deleteNote:          (id: string) => void;
  deleteJournalEntry:  (id: string) => void;
  editJournalEntry:    (id: string, text: string) => void;
  deleteChatSession:   (id: string) => void;
  acceptExercise:      (ex: SpiritualExercise) => void;
  passExercise:        (ex: SpiritualExercise) => void;
  answerFollowUp:      (value: 'something' | 'good' | 'nothing' | 'not_yet', note?: string) => void;
  reflectOnContent:    (item: ContentItem, text: string) => void;
  prefillChat:         (text: string) => void;
  clearChatDraft:      () => void;
  bless:               (pool: string[]) => void;
  showBlessing:        (card: BlessingCard) => void;
  blessPersonalized:   (kind: BlessKind, context?: string, meta?: { question?: string; answer?: string }) => void;
  recordBlessing:      (line: string) => void;
  clearBlessing:       () => void;
  openBlessingInChat:  () => void;
}

// ── Initial state ─────────────────────────────────────────────────────────────

const initialState: AppState = {
  onboardingComplete:  false,
  onboardingChoice:    null,
  conversationId:      generateId(),
  feedTag:             'MILK',
  feed:                [],
  seenIds:             new Set(),
  openedIds:           new Set(),
  positiveCount:       0,
  showTalkToSomeone:   false,
  dialogueSignals:     [],
  baseSignals:         [],
  answeredQuestionIds: [],
  traitScores:         { ...DEFAULT_TRAITS },
  currentQuestion:     null,
  restorationConsent:  'unknown',
  journalEntries:      [],
  answeredPromptIds:   [],
  learnedNotes:        [],
  pendingNoteId:       null,
  chatMessages:        [],
  chatLoading:         false,
  activeChatId:        generateId(),
  chatSessions:        [],
  blessingHistory:     [],
  connectRequests:     [],
  inboxMessages:       [],
  inboxLoading:        false,
  inboxUnread:         0,
  activeRealThreadId:  null,
  name:                null,
  faithWords:          [],
  beliefHistory:       [],
  moments:             [],
  activeExercise:      null,
  acceptedSession:     null,
  doneExerciseIds:     [],
  sessionCount:        1,
  session:             null,
  blessing:            null,
  chatDraft:           '',
};

// ── Persisted state shape (Sets become arrays for JSON storage) ───────────────

type PersistedState = Omit<AppState,
  'seenIds' | 'openedIds' | 'chatLoading' | 'conversationId' | 'blessing'
  | 'inboxMessages' | 'inboxLoading' | 'inboxUnread' | 'activeRealThreadId' | 'pendingNoteId'> & {
  conversationId: string;
  seenIds:   number[];
  openedIds: number[];
};

// ── Store ─────────────────────────────────────────────────────────────────────

export const useAppStore = create<AppState & AppActions>()(
  persist(
    (set, get) => ({
      ...initialState,

      completeOnboarding(choice, freeText, feedTag, signal) {
        // The onboarding story choice carries a hidden signal (e.g. 'carries_grief',
        // 'open_to_god'). Seed it into dialogueSignals so the milk gate and the
        // connection ladder receive what the person revealed from the very first
        // screen — routing then stays invisible and emergent from here on.
        const seedSignals = signal ? [signal] : [];

        // A fresh start means no restored-perspective consent yet.
        setRestorationConsentGranted(false);

        // Route the feed from the signal (invisible, milk-law-obeying). The feedTag
        // passed from the story is a hint; routeFeedTag is the source of truth so
        // RESTORATION can never surface from onboarding alone.
        const tag: FeedTag =
          seedSignals.length > 0
            ? routeFeedTag(seedSignals)
            : (choice === 'E' && freeText ? inferTagFromText(freeText) : (feedTag ?? 'MILK'));

        const feed            = buildFeed(tag, new Set());
        const currentQuestion = computeNextQuestion([], seedSignals, 0);

        set({
          onboardingComplete:  true,
          onboardingChoice:    choice,
          feedTag:             tag,
          feed,
          seenIds:             new Set(feed.map(c => c.id)),
          openedIds:           new Set(),
          positiveCount:       0,
          showTalkToSomeone:   false,
          baseSignals:         stripIdentity(seedSignals),
          dialogueSignals:     stripIdentity(seedSignals),
          answeredQuestionIds: [],
          traitScores:         { ...DEFAULT_TRAITS },
          currentQuestion,
          restorationConsent:  'unknown',
          journalEntries:      [],
          answeredPromptIds:   [],
          learnedNotes:        [],
          pendingNoteId:       null,
          chatMessages:        [],
          chatSessions:        [],
          chatLoading:         false,
          blessingHistory:     [],
          activeExercise:      null,
          acceptedSession:     null,
          doneExerciseIds:     [],
          chatDraft:           '',
          blessing:            null,
          // YOUR STORY SO FAR begins the moment they walk in.
          moments: [{ title: 'You walked in', text: 'You came, and you stayed long enough to be met.', ts: Date.now() }],
        });
      },

      markOpened(id) {
        // No time cap, no lockout (Law 5). Opening content only deepens what the
        // app knows and keeps the feed fresh — it never counts down to a wall.
        const { openedIds, seenIds, feedTag, dialogueSignals, answeredQuestionIds } = get();
        const newOpenedIds = new Set(openedIds).add(id);
        const newSeenIds   = new Set(seenIds).add(id);
        const openCount    = newOpenedIds.size;

        const showTalkToSomeone = openCount >= 3;

        const currentQuestion = computeNextQuestion(
          answeredQuestionIds,
          dialogueSignals,
          openCount,
        );

        set({
          openedIds: newOpenedIds,
          seenIds:   newSeenIds,
          feed:      buildFeed(feedTag, newSeenIds),
          showTalkToSomeone,
          currentQuestion,
        });
      },

      thumbsUp(id) {
        // A thumbs up is a signal of resonance, not a graduation credit. Routing
        // stays invisible and emergent: we re-derive the fitting content level from
        // the signals the person has actually revealed (which always obeys the milk
        // law), rather than climbing a hidden counter toward RESTORATION.
        const { positiveCount, feedTag, seenIds, dialogueSignals } = get();
        const newCount = positiveCount + 1;
        const newTag   = routeFeedTag(dialogueSignals) === 'MILK' ? feedTag
                                                                  : routeFeedTag(dialogueSignals);
        const feed = buildFeed(newTag, seenIds);
        set({ positiveCount: newCount, feedTag: newTag, feed });
        // Personalize from the very thing that moved them, if we can name it.
        const item = CONTENT.find(c => c.id === id);
        const heartCtx = item ? `${item.title} — ${item.description}` : '';
        get().blessPersonalized('heart', heartCtx, {
          question: item ? `${item.title} (${item.scriptureRef})` : undefined,
          answer:   item ? 'You kept this — it moved you.' : undefined,
        });
      },

      bookmark(id) {
        get().thumbsUp(id);
      },

      keepSimple() {
        // Ungated user preference: go gentler. Always available.
        const feed = buildFeed('MILK', get().seenIds);
        set({
          feedTag:          'MILK',
          feed,
          positiveCount:    0,
        });
      },

      goDeeper() {
        // Ungated user preference: one honest step more substantive. Always available,
        // but still obeys the milk law — it will not reach RESTORATION until the
        // person's own signals have opened that door.
        const { feedTag, seenIds, dialogueSignals } = get();
        const newTag = deeperFeedTag(feedTag, dialogueSignals);
        const feed   = buildFeed(newTag, seenIds);
        set({ feedTag: newTag, feed, positiveCount: 0 });
      },

      grantRestorationConsent() {
        // The person said yes to the restored perspective. This is the ONLY thing
        // that lets restoration-tagged content into the feed (on top of the readiness
        // signals). Flip the flag, record the choice, and re-route the feed so the
        // restored milk they just consented to can begin to surface. If their signals
        // do not yet justify it, routeFeedTag simply keeps them where they are.
        setRestorationConsentGranted(true);
        const { dialogueSignals, seenIds, feedTag } = get();
        const nextTag = routeFeedTag(dialogueSignals);
        set({
          restorationConsent: 'granted',
          feedTag: nextTag,
          feed:    nextTag !== feedTag ? buildFeed(nextTag, seenIds) : get().feed,
        });
      },

      declineRestorationConsent() {
        // The person would rather stay with the plain biblical view. Honor it
        // completely: no restoration content surfaces, and we do not ask again
        // unless THEY reopen the door. Keep them gently on the milk track.
        setRestorationConsentGranted(false);
        set({ restorationConsent: 'declined' });
      },

      refreshFeed() {
        // "Show me more →" — advance to the NEXT five. The current page is folded
        // into seenIds first, so the next draw is always brand-new content until
        // the whole track is exhausted (then a fresh cycle begins). This is what
        // makes "scroll and never see the same one twice until you've seen them
        // all" true. Stays within the current track — never a gate, never a jump.
        const { feedTag, seenIds, feed } = get();
        const shown = new Set(seenIds);
        feed.forEach(c => shown.add(c.id));
        set({ seenIds: shown, feed: buildFeed(feedTag, shown) });
      },

      resetSession() {
        set({
          ...initialState,
          seenIds:         new Set(),
          openedIds:       new Set(),
          traitScores:     { ...DEFAULT_TRAITS },
          currentQuestion: computeNextQuestion([], [], 0),
        });
      },

      answerQuestion(questionId, answerValue, answerText) {
        const {
          answeredQuestionIds,
          baseSignals,
          traitScores,
          openedIds,
        } = get();

        const question = QUESTION_BANK.find(q => q.id === questionId);
        if (!question) return;

        const newTraits: TraitScores = { ...traitScores };
        // Engagement signals go to the sticky base set; faith IDENTITY is split
        // off and ridden on a faith word so it stays editable and can be unlearned.
        const newBase = new Set(baseSignals);
        let deltas: Partial<TraitScores> = {};
        // Identity harvested from a free-text faith self-description rides its own
        // faith line, so removing the line later truly un-learns it.
        let faithHarvest: string[] = [];
        // A multiple-choice faith answer ("I grew up in a faith but drifted") is
        // itself a self-description — capture its identity verbatim, removable.
        let optionFaith: FaithWord | null = null;

        if (question.answerType === 'CHOICE' || question.answerType === 'YES_NO') {
          const opt = question.answerOptions.find(o => o.value === answerValue);
          if (opt) {
            deltas = opt.traitSignals ?? {};
            const optSignals = opt.signals ?? [];
            stripIdentity(optSignals).forEach(s => newBase.add(s));
            optionFaith = captureIdentityWord(opt.text, optSignals);
          }
        } else if (question.answerType === 'FREE_TEXT') {
          const base = question.traitSignals;
          for (const [k, v] of Object.entries(base)) {
            const key = k as keyof TraitScores;
            deltas[key] = Math.round((v ?? 0) * 0.7 * 1000) / 1000;
          }
          if (answerText && answerText.length > 120) {
            deltas.sincerity = Math.round(((deltas.sincerity ?? 0) + 0.15) * 1000) / 1000;
          }
          // The ear listens to free-text dialogue answers too — the gate can open
          // from what they type here, not only from chat. Engagement → base,
          // identity → the faith line built from their own words.
          if (answerText) {
            const harvested = harvestSignals(answerText);
            stripIdentity(harvested).forEach(s => newBase.add(s));
            faithHarvest = identityOnly(harvested);
          }
        }

        for (const [k, delta] of Object.entries(deltas)) {
          const key     = k as keyof TraitScores;
          const current = newTraits[key] ?? 0.0;
          newTraits[key] = Math.round(
            Math.max(TRAIT_MIN, Math.min(TRAIT_MAX, current + (delta ?? 0))) * 1000,
          ) / 1000;
        }

        const newAnsweredIds = [...answeredQuestionIds, questionId];
        // Safety net: identity must never persist in the base set.
        const newBaseArr     = stripIdentity(Array.from(newBase));

        // Keep a verbatim faith self-description if the free-text answer is one
        // (named a tradition, or harvested identity) — carrying only the identity
        // it taught, so it can be un-learned on removal.
        const faithCapture: FaithWord | null =
          question.answerType === 'FREE_TEXT' && answerText &&
          (FAITH_ID_RE.test(answerText) || faithHarvest.length > 0)
            ? { text: answerText.slice(0, 140), ts: Date.now(), signals: faithHarvest }
            : null;

        const { feedTag: prevTag, seenIds, feed: prevFeed, faithWords } = get();
        const nextWords     = [optionFaith, faithCapture, ...faithWords]
          .filter((w): w is FaithWord => w !== null);
        const newSignalsArr = composeSignals(newBaseArr, nextWords);

        const currentQuestion = computeNextQuestion(
          newAnsweredIds,
          newSignalsArr,
          openedIds.size,
        );

        // Emergent routing: re-derive the feed track from what they've now shown
        // (still milk-law-obeying). Only rebuild the feed if the track moved.
        const nextTag    = routeFeedTag(newSignalsArr);
        const trackMoved = nextTag !== prevTag;

        set({
          answeredQuestionIds: newAnsweredIds,
          baseSignals:         newBaseArr,
          dialogueSignals:     newSignalsArr,
          traitScores:         newTraits,
          currentQuestion,
          feedTag:             trackMoved ? nextTag : prevTag,
          feed:                trackMoved ? buildFeed(nextTag, seenIds) : prevFeed,
          faithWords:          nextWords,
        });
        // Personalize the blessing from what they actually answered (the free-text
        // they wrote, or the option they chose), so it speaks to THIS moment.
        const chosen = question.answerOptions.find(o => o.value === answerValue);
        const answerSaid = (answerText && answerText.trim()) || chosen?.text || '';
        const blessCtx = answerSaid || question.questionText;
        get().blessPersonalized('dialogue', blessCtx, {
          question: question.questionText,
          answer:   answerSaid || undefined,
        });
      },

      addJournalEntry(promptId, promptText, text) {
        const entry: JournalEntry = {
          id:         Date.now().toString(),
          promptId,
          promptText,
          text,
          timestamp:  Date.now(),
        };

        // The ear listens to journal saves too — what a person writes privately
        // is often the truest thing they say. The gate can open from here.
        // A journal entry is not a faith record, so its signals are sticky base.
        const heur       = stripIdentity(harvestSignals(text));
        const { baseSignals, faithWords, answeredQuestionIds, openedIds, feedTag: prevTag, seenIds, feed: prevFeed } = get();
        const newBase    = mergeSignals(baseSignals, heur);
        const merged     = composeSignals(newBase, faithWords);
        const nextTag    = routeFeedTag(merged);
        const trackMoved = nextTag !== prevTag;

        // Honest proof from reflection — not just from chat questions (Cameron's
        // ask). Sitting down to write something true about your own life is real
        // sincerity, and a longer, searching entry shows honest inquiry and hunger.
        // Length-gated so a one-word entry earns nothing and the scale can't be
        // farmed; small and one-directional (reflection is never penalized — it is
        // the kind of honest doubt/grief the judge is told never to dock).
        const words = text.trim().split(/\s+/).filter(Boolean).length;
        const journalDeltas: Partial<TraitScores> =
          words >= 25 ? { sincerity: 0.2, honest_inquiry: 0.15, hunger: 0.15 }
          : words >= 6 ? { sincerity: 0.2 }
          : {};

        set(s => ({
          journalEntries:    [entry, ...s.journalEntries],
          answeredPromptIds: [...s.answeredPromptIds, promptId],
          baseSignals:       newBase,
          dialogueSignals:   merged,
          feedTag:           trackMoved ? nextTag : prevTag,
          feed:              trackMoved ? buildFeed(nextTag, seenIds) : prevFeed,
          traitScores:       nudgeTraits(s.traitScores, journalDeltas),
          currentQuestion:   s.currentQuestion
            ?? computeNextQuestion(answeredQuestionIds, merged, openedIds.size),
        }));
      },

      saveLearnedNote({ source, title, body }) {
        const clean = (body ?? '').trim();
        const id = generateId();
        // Save immediately with an excerpt so the note is useful even offline and
        // the Journal can open to it at once. Mark it pending while the AI writes
        // the real "what you can take from this" summary in the background.
        const note: LearnedNote = {
          id,
          source,
          title:     (title ?? '').trim() || 'A note to keep',
          summary:   excerptFallback(clean),
          body:      clean,
          timestamp: Date.now(),
          pending:   true,
        };
        set(s => ({
          learnedNotes:  [note, ...s.learnedNotes].slice(0, 200),
          pendingNoteId: id,
          // Choosing to KEEP something is itself a sign of hunger for truth and
          // sincerity — the person cared enough to hold onto it. The app learns from
          // the ACT of saving, not just the words (Cameron's #6). The note text is
          // also handed to the minister as context, so it isn't double-counted as a
          // separate story moment.
          traitScores:   nudgeTraits(s.traitScores, { hunger: 0.3, sincerity: 0.2 }),
        }));

        // Fill in the AI clip after the fact; never block the save on the network.
        generateNoteSummary(source, note.title, clean).then(summary => {
          set(s => ({
            learnedNotes: s.learnedNotes.map(n =>
              n.id === id
                ? { ...n, summary: summary || n.summary, pending: false }
                : n,
            ),
          }));
        });

        return id;
      },

      clearPendingNote() {
        set({ pendingNoteId: null });
      },

      setChatLoading(loading) {
        set({ chatLoading: loading });
      },

      appendAssistantMessage(text) {
        const msg: ChatMessage = {
          id:        Date.now().toString(),
          role:      'assistant',
          text,
          timestamp: Date.now(),
        };
        set(s => ({
          chatMessages: [...s.chatMessages, msg],
          chatLoading:  false,
        }));
      },

      // Deliver an AI message to the chat it was ASKED in (chatId), even if the
      // person has since switched to or started another chat. If that chat is still
      // open, it lands live; otherwise it's appended to its archived session — so a
      // pending answer never spills into a different conversation.
      appendAssistantToChat(chatId, text, kind) {
        const msg: ChatMessage = {
          id:        Date.now().toString() + (kind === 'meta' ? '-m' : ''),
          role:      'assistant',
          text,
          timestamp: Date.now(),
          ...(kind === 'meta' ? { kind: 'meta' as const } : {}),
        };
        set(s => {
          if (s.activeChatId === chatId) {
            return { chatMessages: [...s.chatMessages, msg], chatLoading: false };
          }
          // Routed to a chat the person has navigated away from: append to its
          // archived session and leave the current chat (and its loading) alone.
          return {
            chatSessions: s.chatSessions.map(sess =>
              sess.id === chatId
                ? { ...sess, messages: [...sess.messages, msg], updatedAt: Date.now() }
                : sess,
            ),
          };
        });
      },

      // A quiet, centered note in the thread (e.g. "humility −1.5") that the
      // person can see and ask about — but which is NEVER sent back to the model
      // as conversation. Honest about what the judge just did.
      appendMetaMessage(text) {
        const clean = (text ?? '').trim();
        if (!clean) return;
        const msg: ChatMessage = {
          id:        Date.now().toString() + '-m',
          role:      'assistant',
          text:      clean,
          timestamp: Date.now(),
          kind:      'meta',
        };
        set(s => ({ chatMessages: [...s.chatMessages, msg] }));
      },

      // Archive the live thread (if it has real content) as a titled session, so
      // it can be reopened later. Returns the archive list with it prepended.
      newChat() {
        set(s => {
          const real = s.chatMessages.filter(m => m.kind !== 'meta' && m.text.trim());
          // Always move to a fresh chat id (and drop any spinner from the old one),
          // so a still-loading answer is routed back to the chat it was asked in.
          const freshId = generateId();
          if (real.length === 0) {
            return { activeChatId: freshId, chatLoading: false };  // nothing worth saving
          }
          const firstUser = s.chatMessages.find(m => m.role === 'user');
          const session: ChatSession = {
            id:        s.activeChatId,   // archive under the SAME id the answer targets
            title:     titleFromText(firstUser?.text ?? real[0].text),
            createdAt: s.chatMessages[0]?.timestamp ?? Date.now(),
            updatedAt: Date.now(),
            messages:  s.chatMessages,
          };
          return {
            chatSessions: [session, ...s.chatSessions],
            chatMessages: [],
            activeChatId: freshId,
            chatLoading:  false,
          };
        });
      },

      // Reopen a saved conversation: archive whatever is currently open first (so
      // nothing is lost), then load the chosen one as the live thread.
      openChat(id) {
        set(s => {
          const target = s.chatSessions.find(x => x.id === id);
          if (!target) return {};
          const rest = s.chatSessions.filter(x => x.id !== id);
          const real = s.chatMessages.filter(m => m.kind !== 'meta' && m.text.trim());
          let archive = rest;
          if (real.length > 0) {
            const firstUser = s.chatMessages.find(m => m.role === 'user');
            archive = [{
              id:        s.activeChatId,   // archive under the id its pending answer targets
              title:     titleFromText(firstUser?.text ?? real[0].text),
              createdAt: s.chatMessages[0]?.timestamp ?? Date.now(),
              updatedAt: Date.now(),
              messages:  s.chatMessages,
            }, ...rest];
          }
          // Becoming the live chat means its own id is now the active target.
          return {
            chatSessions: archive,
            chatMessages: target.messages,
            activeChatId: target.id,
            chatLoading:  false,
          };
        });
      },

      submitConnectRequest(note) {
        // Capture the request ON-DEVICE. The on-device queue is the source of
        // truth — Cameron reviews it in admin (Phase 1). A real human is always
        // one tap away.
        const { dialogueSignals, conversationId } = get();
        const entry: ConnectRequest = {
          id:             generateId(),
          note:           (note ?? '').trim(),
          journeyStage:   assessJourney(dialogueSignals),
          conversationId,
          timestamp:      Date.now(),
          delivered:      false,
        };
        set(s => ({ connectRequests: [entry, ...s.connectRequests] }));
      },

      // Send the person's words to a real human via the cloud inbox, AND keep the
      // on-device copy as a durable fallback. The note goes into the CURRENTLY OPEN
      // conversation; if none is open, a fresh one is started. The first message of
      // a conversation carries its title, so the history list reads like topics.
      // If the cloud isn't configured or is unreachable, the on-device queue still
      // holds it — the promise stays honest.
      async sendConnectMessage(note, excerpt, priority) {
        const state = get();
        const stage = assessJourney(state.dialogueSignals);
        // Auto-flag crisis from the note itself if the caller didn't already — this
        // covers a person writing the admin team directly with distress language.
        const pri = priority ?? (detectCrisis(note) ? 'crisis' : undefined);
        // Always keep the local record (offline-safe).
        get().submitConnectRequest(note);
        if (!isMessagingConfigured) return;

        // Resolve which conversation this belongs to; open a new one if none active.
        let threadId = state.activeRealThreadId;
        if (!threadId) {
          threadId = newRealThreadId();
          set({ activeRealThreadId: threadId });
        }
        // Stamp a title only on the FIRST message of this conversation.
        const isFirst = !state.inboxMessages.some(m => m.thread_id === threadId);
        const threadTitle = isFirst
          ? titleFromText(note || excerpt || 'Conversation')
          : undefined;

        set({ inboxLoading: true });
        const saved = await cloudSendMessage(note, {
          threadId,
          threadTitle,
          excerpt,
          journeyStage: stage,
          priority: pri,
        });
        if (saved) {
          set(s => ({
            inboxMessages: [...s.inboxMessages, saved],
            inboxLoading:  false,
          }));
        } else {
          set({ inboxLoading: false });
        }
      },

      // Start a brand-new, separate conversation with a real person. The next
      // sendConnectMessage will open it for real with a stamped title.
      newRealPersonThread() {
        const id = newRealThreadId();
        set({ activeRealThreadId: id });
        return id;
      },

      // Open an existing conversation from the history list. Opening it clears that
      // conversation's unread replies (locally and on the server).
      openRealPersonThread(id) {
        set({ activeRealThreadId: id });
        const hasUnread = get().inboxMessages.some(
          m => m.thread_id === id && m.sender === 'admin' && !m.read_by_user,
        );
        if (hasUnread) get().markInboxRead();
      },

      // Back out to the conversation list — no conversation open.
      closeRealPersonThread() {
        set({ activeRealThreadId: null });
      },

      // Carry the current AI conversation to a real person. Summarizes the last
      // question and the AI's answer, opens a NEW titled conversation with it as the
      // opening context, and leaves it waiting for a human reply. The AI chat itself
      // is untouched. Returns true if there was something to send.
      async escalateToRealPerson() {
        const msgs = get().chatMessages.filter(m => m.kind !== 'meta' && m.text.trim());
        const lastUser = [...msgs].reverse().find(m => m.role === 'user');
        const lastAI   = [...msgs].reverse().find(m => m.role === 'assistant');
        if (!lastUser && !lastAI) return false;
        const note =
          (lastUser ? `I was talking with the app and asked:\n"${lastUser.text}"\n\n` : '') +
          (lastAI ? `The app answered:\n"${lastAI.text}"\n\n` : '') +
          `I'd love a real person's thoughts on this.`;
        // Crisis triage: if anything the PERSON said in this conversation carries
        // severe-distress / self-harm language, mark this escalation high-priority so
        // the admin team sees and reaches out first. (Only the person's own words are
        // checked — never the AI's reply.)
        const crisis = msgs.some(m => m.role === 'user' && detectCrisis(m.text));
        // Each escalation is its own conversation, titled from the person's question.
        get().newRealPersonThread();
        // The excerpt carries the AI's answer so the human sees the context at a glance.
        await get().sendConnectMessage(note, lastAI?.text, crisis ? 'crisis' : undefined);
        return true;
      },

      // Pull EVERY human message for this device and compute unread admin replies.
      // The app groups them into separate conversations on the client.
      async loadInbox() {
        if (!isMessagingConfigured) return;
        set({ inboxLoading: true });
        const thread = await cloudFetchThread();
        const unread = thread.filter(m => m.sender === 'admin' && !m.read_by_user).length;
        set(s => {
          // If the open conversation no longer exists (or none was open), default to
          // the most recently active one — but only when there's a single thread, so
          // multi-thread users land on the list and choose.
          let active = s.activeRealThreadId;
          const groups = selectRealThreads(thread);
          if (active && !thread.some(m => m.thread_id === active)) active = null;
          if (!active && groups.length === 1) active = groups[0].id;
          return { inboxMessages: thread, inboxUnread: unread, inboxLoading: false, activeRealThreadId: active };
        });
      },

      // The person opened a conversation — clear its unread replies locally (so the
      // per-thread dot updates at once) and on the server. With no active thread,
      // every unread reply is cleared.
      markInboxRead() {
        const { activeRealThreadId, inboxMessages } = get();
        const cleared = inboxMessages.map(m =>
          m.sender === 'admin' && !m.read_by_user &&
          (!activeRealThreadId || m.thread_id === activeRealThreadId)
            ? { ...m, read_by_user: true }
            : m,
        );
        const unread = cleared.filter(m => m.sender === 'admin' && !m.read_by_user).length;
        set({ inboxMessages: cleared, inboxUnread: unread });
        if (isMessagingConfigured) cloudMarkRead(activeRealThreadId ?? undefined);
      },

      // Live updates: a real person's reply lands in the app the moment it's sent.
      // Returns an unsubscribe fn for the caller to clean up.
      startInboxSubscription() {
        if (!isMessagingConfigured) return () => {};
        return cloudSubscribe(msg => {
          let replied = false;
          set(s => {
            if (s.inboxMessages.some(m => m.id === msg.id)) return s;  // de-dupe
            const isAdminReply = msg.sender === 'admin' && !msg.read_by_user;
            replied = isAdminReply;
            return {
              inboxMessages: [...s.inboxMessages, msg],
              inboxUnread:   isAdminReply ? s.inboxUnread + 1 : s.inboxUnread,
            };
          });
          // A real person replied — notify them and let it rise to the top.
          if (replied) notifyRealPersonReply(msg.body);
        });
      },

      setName(name) {
        const clean = (name ?? '').trim().slice(0, 60);
        set({ name: clean.length ? clean : null });
      },

      recordFaithBackground(choiceKey, text) {
        // The FAITH BACKGROUND onboarding page (a disciple asks openly — Law 9,
        // names no church for them). The chosen option seeds routing signals; the
        // words are kept VERBATIM; question 2.5 is marked answered. Their own words
        // can carry anything — including a legitimate member self-ID.
        const FAITH_META: Record<string, { signals: string[]; label: string }> = {
          active:       { signals: ['active_faith_tradition'], label: "I'm part of a church or faith community now." },
          stepped_away: { signals: ['has_history_with_faith'], label: 'I grew up in one, but I have stepped away.' },
          none:         { signals: [], label: "I've never really had one." },
          complicated:  { signals: [], label: "It's complicated." },
          private:      { signals: [], label: '' },
        };
        const meta  = FAITH_META[choiceKey] ?? FAITH_META.private;
        const clean = (text ?? '').trim();

        const { baseSignals, faithWords, answeredQuestionIds, openedIds } = get();

        // The chosen option's identity rides on the LABEL line; the free-text's
        // identity rides on the words line — so removing either un-learns its part.
        // Any non-identity engagement the free text reveals goes to the sticky base.
        const cleanHarvest = clean ? harvestSignals(clean) : [];
        const newBase = mergeSignals(baseSignals, stripIdentity(cleanHarvest));

        const newWords: FaithWord[] = [];
        if (meta.label && choiceKey !== 'private') newWords.push({ text: meta.label, ts: Date.now(), signals: meta.signals });
        if (clean) newWords.push({ text: clean.slice(0, 140), ts: Date.now(), signals: identityOnly(cleanHarvest) });

        const nextWords = [...newWords, ...faithWords];
        const merged    = composeSignals(newBase, nextWords);

        const newAnswered = (choiceKey && choiceKey !== 'private' && !answeredQuestionIds.includes(2.5))
          ? [...answeredQuestionIds, 2.5]
          : answeredQuestionIds;

        const momentDetail = `“${(clean || meta.label).slice(0, 90)}”`;
        const nextTag = routeFeedTag(merged);
        set(s => ({
          faithWords:      nextWords,
          baseSignals:     newBase,
          dialogueSignals: merged,
          answeredQuestionIds: newAnswered,
          feedTag:         nextTag,
          feed:            buildFeed(nextTag, s.seenIds),
          currentQuestion: computeNextQuestion(newAnswered, merged, openedIds.size),
          moments: newWords.length > 0
            ? [{ title: 'Your faith, as you told it', text: momentDetail, ts: Date.now() }, ...s.moments]
            : s.moments,
        }));
      },

      editFaithWord(index, text) {
        // The person's own faith words are theirs to revise at any time — fix a
        // typo, add context, or remove a line entirely (empty text = remove).
        // Each line carries the signals it taught; re-deriving from base + the
        // remaining lines means a correction or removal honestly un-learns what
        // that line had taught (the feed may settle back toward milk — correct).
        const clean = (text ?? '').trim().slice(0, 140);
        const { faithWords, baseSignals } = get();
        if (index < 0 || index >= faithWords.length) return;

        // The line owns only its IDENTITY (so removing it un-learns who the app
        // thinks they are); any engagement it reveals stays sticky in the base.
        const harvested = clean ? harvestSignals(clean) : [];
        const newBase   = mergeSignals(baseSignals, stripIdentity(harvested));
        const nextWords = [...faithWords];
        const oldText   = faithWords[index]?.text ?? '';
        // A genuine change of wording (not a removal, not a no-op) is HONORED:
        // keep the old and new together so a changed mind stays visible (#7).
        const isRealChange = !!clean && clean !== oldText.trim();
        if (!clean) {
          nextWords.splice(index, 1);
        } else {
          nextWords[index] = { text: clean, ts: Date.now(), signals: identityOnly(harvested) };
        }

        const merged  = composeSignals(newBase, nextWords);
        const nextTag = routeFeedTag(merged);
        set(s => ({
          faithWords:      nextWords,
          beliefHistory:   isRealChange
            ? [{ from: oldText, to: clean, ts: Date.now() }, ...s.beliefHistory].slice(0, 50)
            : s.beliefHistory,
          baseSignals:     newBase,
          dialogueSignals: merged,
          feedTag:         nextTag,
          feed:            nextTag !== s.feedTag ? buildFeed(nextTag, s.seenIds) : s.feed,
        }));
      },
      deleteBeliefChange(ts) {
        set(s => ({ beliefHistory: s.beliefHistory.filter(b => b.ts !== ts) }));
      },

      addFaithWord(text) {
        // Add a new line to "YOUR FAITH, AS YOU'VE TOLD IT", newest first. The
        // line owns only its IDENTITY so it can be un-learned if later removed;
        // any engagement it reveals stays sticky in the base.
        const clean = (text ?? '').trim().slice(0, 140);
        if (!clean) return;
        const { baseSignals, faithWords } = get();
        const harvested = harvestSignals(clean);
        const newBase   = mergeSignals(baseSignals, stripIdentity(harvested));
        const nextWords = [{ text: clean, ts: Date.now(), signals: identityOnly(harvested) }, ...faithWords];
        const merged    = composeSignals(newBase, nextWords);
        const nextTag   = routeFeedTag(merged);
        set(s => ({
          faithWords:      nextWords,
          baseSignals:     newBase,
          dialogueSignals: merged,
          feedTag:         nextTag,
          feed:            nextTag !== s.feedTag ? buildFeed(nextTag, s.seenIds) : s.feed,
        }));
      },

      addMoment(title, text) {
        const t = (title ?? '').trim().slice(0, 60);
        const b = (text ?? '').trim().slice(0, 280);
        if (!b) return;
        set(s => ({ moments: [{ title: t || 'A moment', text: b, ts: Date.now() }, ...s.moments] }));
      },

      // ── Edit / delete: keep the person dynamic, never boxed ─────────────────
      // A faith word removed un-learns its identity (editFaithWord already does
      // this when handed empty text).
      removeFaithWord(index) {
        get().editFaithWord(index, '');
      },
      deleteMoment(ts) {
        set(s => ({ moments: s.moments.filter(m => m.ts !== ts) }));
      },
      deleteNote(id) {
        set(s => ({ learnedNotes: s.learnedNotes.filter(n => n.id !== id) }));
      },
      deleteJournalEntry(id) {
        set(s => ({ journalEntries: s.journalEntries.filter(e => e.id !== id) }));
      },
      editJournalEntry(id, text) {
        const clean = (text ?? '').trim();
        set(s => ({
          journalEntries: clean
            ? s.journalEntries.map(e => (e.id === id ? { ...e, text: clean } : e))
            : s.journalEntries.filter(e => e.id !== id),   // emptied = deleted
        }));
      },
      deleteChatSession(id) {
        set(s => ({ chatSessions: s.chatSessions.filter(x => x.id !== id) }));
      },

      acceptExercise(ex) {
        // They said "I'll try it." Hold it as active, stamp the session it was
        // accepted in (so a follow-up only becomes due on a LATER launch), and
        // keep a moment of the step they took. Bless it — words only.
        set(s => ({
          activeExercise:  ex,
          acceptedSession: s.sessionCount,
          moments: [
            { title: 'An invitation you accepted', text: `“${ex.text.slice(0, 80)}…”`, ts: Date.now() },
            ...s.moments,
          ],
        }));
        get().bless([
          'That is the kind of step most people never take.',
          'Quietly trying is its own kind of faith.',
          'No one is watching. That is what makes it real.',
        ]);
      },

      passExercise(ex) {
        // Left free, no guilt — just don't offer the same one again soon.
        set(s => ({
          doneExerciseIds: s.doneExerciseIds.includes(ex.id)
            ? s.doneExerciseIds
            : [...s.doneExerciseIds, ex.id],
        }));
      },

      answerFollowUp(value, note) {
        const { activeExercise, doneExerciseIds, traitScores, baseSignals, faithWords,
                feedTag: prevTag, seenIds, feed: prevFeed, sessionCount } = get();
        const ex = activeExercise;
        if (!ex) return;
        const trimmed = (note ?? '').trim();

        if (value === 'not_yet') {
          // No rush — re-arm it for next time, gentle nudge to sincerity.
          set({
            activeExercise:  ex,
            acceptedSession: sessionCount,
            traitScores:     nudgeTraits(traitScores, { sincerity: 0.05 }),
          });
          get().bless(['No rush. It will keep.']);
          return;
        }

        const OUTCOME: Record<string, { signals: string[]; traits: Partial<TraitScores>; detail: string }> = {
          something: { signals: ['had_spiritual_experience', 'open_to_god'], traits: { openness: 0.35, hunger: 0.3, sincerity: 0.2 }, detail: 'Something came back you could not quite name.' },
          good:      { signals: ['open_to_god'], traits: { sincerity: 0.25, openness: 0.2 }, detail: 'Quieter than expected — but good.' },
          nothing:   { signals: [], traits: { honest_inquiry: 0.3, courage: 0.2 }, detail: 'Nothing came back — and you said so honestly.' },
        };
        const o      = OUTCOME[value] ?? OUTCOME.nothing;
        const detail = trimmed ? `“${trimmed.slice(0, 90)}${trimmed.length > 90 ? '…' : ''}”` : o.detail;

        // Their own words about what came back are the richest signal of all.
        // An exercise report is not a faith record — its signals are sticky base.
        const newBase  = mergeSignals(baseSignals, stripIdentity([...o.signals, ...harvestSignals(trimmed)]));
        const heard    = composeSignals(newBase, faithWords);
        const nextTag  = routeFeedTag(heard);
        const moved    = nextTag !== prevTag;
        const traitDeltas = trimmed ? { ...o.traits, sincerity: (o.traits.sincerity ?? 0) + 0.1 } : o.traits;

        set(s => ({
          activeExercise:  null,
          acceptedSession: null,
          doneExerciseIds: s.doneExerciseIds.includes(ex.id) ? s.doneExerciseIds : [...s.doneExerciseIds, ex.id],
          baseSignals:     newBase,
          dialogueSignals: heard,
          traitScores:     nudgeTraits(traitScores, traitDeltas),
          feedTag:         moved ? nextTag : prevTag,
          feed:            moved ? buildFeed(nextTag, seenIds) : prevFeed,
          moments: [
            { title: `You tried it: ${ex.ref.split(' —')[0]}`, text: detail, ts: Date.now() },
            ...s.moments,
          ],
        }));

        get().bless(value === 'nothing'
          ? ['Honest nothing is worth more than a performed something.', 'Thank you for telling the truth about it.']
          : ['Pay attention to that. It usually is not nothing.', 'Worth keeping. Worth following.']);
      },

      reflectOnContent(item, text) {
        // "Reflect on this →" — save the reflection to the journal, keep a moment,
        // harvest its signals, and bless. The truest things are said quietly.
        const t = (text ?? '').trim();
        if (!t) return;
        const entry: JournalEntry = {
          id:         Date.now().toString(),
          promptId:   'content_' + item.id,
          promptText: `Reflecting on “${item.title}” (${item.scriptureRef})`,
          text:       t,
          timestamp:  Date.now(),
        };
        const { traitScores, baseSignals, faithWords, feedTag: prevTag, seenIds, feed: prevFeed } = get();
        const newBase = mergeSignals(baseSignals, stripIdentity(harvestSignals(t)));
        const heard   = composeSignals(newBase, faithWords);
        const nextTag = routeFeedTag(heard);
        const moved   = nextTag !== prevTag;
        // The reflection is SAVED as a journal entry (the person chose to keep it),
        // so it must NOT also be copied into Profile "your story so far" — that was
        // the double-count (Cameron's #6). Story-so-far is only for things the app
        // holds that the person did NOT already save themselves. The act of saving
        // still feeds the trait read below.
        set(s => ({
          journalEntries:  [entry, ...s.journalEntries],
          baseSignals:     newBase,
          dialogueSignals: heard,
          traitScores:     nudgeTraits(traitScores, { sincerity: 0.2, hunger: 0.1 }),
          feedTag:         moved ? nextTag : prevTag,
          feed:            moved ? buildFeed(nextTag, seenIds) : prevFeed,
        }));
        get().blessPersonalized('journal', t, {
          question: `Reflecting on “${item.title}” (${item.scriptureRef})`,
          answer:   t,
        });
      },

      prefillChat(text) {
        // A "talk about it" / "ask about this" tap SPARKS A NEW conversation rather
        // than piling onto the current one — the old thread is archived into history.
        get().newChat();
        set({ chatDraft: text });
      },

      clearChatDraft() {
        set({ chatDraft: '' });
      },

      showBlessing(card) {
        const clean = (card?.line ?? '').trim();
        if (!clean) return;
        // No timer. The blessing STAYS until the person swipes it — left to
        // dismiss, right to carry it into chat. Reading is theirs to pace, and
        // the absence, when it goes, is theirs to feel.
        set({ blessing: { ...card, line: clean } });
      },

      bless(pool) {
        get().showBlessing({ line: pickLine(pool), kind: 'heart' });
      },

      // ONE blessing, ever — and only if the disciple has something true to say.
      // No instant pool pre-show (that was the second box, and the source of the
      // repeats). The AI reads what they actually did and may answer with a warm
      // word, a firm correction, or silence (no popup at all). It is handed every
      // line it has spoken before, so it never repeats itself. Fire-and-forget.
      blessPersonalized(kind, context, meta) {
        generateBlessing(kind, context ?? '', get().blessingHistory).then(line => {
          if (!line) return;            // silence is a valid, honest response
          // Carry WHAT it was about (the question and their answer), so a
          // swipe-right opens a real conversation about that exact moment.
          get().showBlessing({
            line,
            kind,
            question: meta?.question,
            answer:   meta?.answer ?? ((context ?? '').trim() || undefined),
          });
          get().recordBlessing(line);
        });
      },

      // Remember a spoken blessing so it is never repeated. Capped so memory
      // stays bounded but deep enough to keep every line fresh.
      recordBlessing(line) {
        const clean = (line ?? '').trim();
        if (!clean) return;
        set(s => ({ blessingHistory: [...s.blessingHistory, clean].slice(-80) }));
      },

      clearBlessing() {
        set({ blessing: null });
      },

      // Swipe-right: carry the blessing — the question, the answer, AND the word
      // spoken over it — into chat, so a quiet moment can become a real talk.
      // We pre-fill an opening line in the person's input and clear the card; the
      // Chat screen reads chatDraft and seeds the box (they still choose to send).
      openBlessingInChat() {
        const card = get().blessing;
        if (!card) return;
        const parts: string[] = [];
        if (card.question) parts.push(`You asked me: “${card.question.trim()}”`);
        if (card.answer)   parts.push(`I said: “${card.answer.trim()}”`);
        if (card.line)     parts.push(`Then this came back to me: “${card.line.trim()}”`);
        parts.push('Can we talk about it?');
        // Start fresh — carrying a moment into chat opens a NEW conversation.
        get().newChat();
        set({ chatDraft: parts.join('\n'), blessing: null });
      },

      async sendChatMessage(text) {
        // Remember which chat this question belongs to, so the answer comes back
        // here even if the person switches chats while it loads.
        const sendChatId = get().activeChatId;
        const userMsg: ChatMessage = {
          id:        Date.now().toString(),
          role:      'user',
          text,
          timestamp: Date.now(),
        };

        // ── The ear: harvest signals from THIS message BEFORE the prompt ─────
        // so the milk gate can open mid-conversation and the guidance below is
        // built from everything the person has revealed, including just now.
        const heur    = harvestSignals(text);
        const isFaith = FAITH_ID_RE.test(text);
        const prior   = get();

        // A faith self-description is kept VERBATIM AND carries the signals it
        // taught, so removing it later un-learns them. Any other message's signals
        // are sticky base — the app does not un-hear what was freely said in chat.
        // A faith self-description carries its IDENTITY onto a faith word (so
        // removing it un-learns who the app thinks they are); any engagement it
        // also reveals (grief, hunger) still goes to the sticky base. A non-faith
        // message contributes only engagement — identity is never minted from it.
        const newFaithWord: FaithWord | null = isFaith
          ? { text: text.slice(0, 140), ts: Date.now(), signals: identityOnly(heur) }
          : null;
        const nextWords       = newFaithWord ? [newFaithWord, ...prior.faithWords] : prior.faithWords;
        const newBase         = mergeSignals(prior.baseSignals, stripIdentity(heur));
        const combinedSignals = composeSignals(newBase, nextWords);

        // Did THIS message just reveal they are a Latter-day Saint (when the app
        // didn't know it before)? If so we fast-track them to the member track and
        // say so out loud — being dynamic with their faith instead of silently
        // carrying on with milk (Cameron's ask).
        const becameMember = engineIsMember(combinedSignals) && !engineIsMember(prior.dialogueSignals);

        set(s => ({
          chatMessages: [...s.chatMessages, userMsg],
          chatLoading:  true,
          baseSignals:     newBase,
          dialogueSignals: combinedSignals,
          faithWords:      nextWords,
          session:     { lastSeen: Date.now(), lastWords: text.slice(0, 140) },
        }));

        const state = get();

        // ── Build system prompt with full user context ──────────────────────

        // SIGNAL_LABELS — every signal the engine can hear, in plain English for
        // the model's context. Kept in sync with mbm-data.js SIGNAL_LABELS.
        const signalLabels: Record<string, string> = {
          had_spiritual_experience:    'has had an unexplained spiritual experience',
          has_history_with_faith:      'has a past with faith',
          skeptical_of_god:            'is skeptical about God',
          open_to_god:                 'feels open to God',
          hurt_by_church:              'has been hurt by a church or its people',
          prayed_before:               'has prayed before',
          carries_grief:               'is carrying grief or loss',
          struggles_with_habits:       'is wrestling with a difficult habit',
          lonely:                      'is experiencing loneliness',
          searching_for_purpose:       'is searching for meaning and purpose',
          drawn_to_jesus:              'feels drawn to Jesus personally',
          believes_in_jesus:           'believes in Jesus',
          open_to_restoration:         'is open to the idea that God still speaks today',
          curious_about_book_of_mormon: 'is curious about the Book of Mormon',
          inactive_member:             'is a less-active Latter-day Saint',
          active_member:               'is an active Latter-day Saint',
          covenant_intent:             'already holds faith dear and wants to go deeper',
          pictures_harsh_god:          'carries a picture of a harsh, score-keeping, or disappointed God (use the comparison method gently)',
          pictures_distant_god:        'pictures a God who is not paying attention to them',
          reformed_framework:          'comes from a Reformed/Calvinist framework (the framework itself carries a harsh God — examine the picture gently; NEVER say this analysis to them)',
          rejects_harsh_god:           'has rejected the harsh picture of God in their own words',
          nontheistic_framework:       'does not (yet) conceive of God as a person — warm spirituality is not yet trust in a good personal God',
          active_faith_tradition:      'is part of a faith community today',
          losing_faith:                'is experiencing a faith crisis',
        };

        const signalSentences = combinedSignals
          .filter(s => signalLabels[s])
          .map(s => signalLabels[s])
          .join('; ');

        const traits = state.traitScores;
        const traitSummary = [
          `honest inquiry: ${traits.honest_inquiry.toFixed(1)}/10`,
          `openness: ${traits.openness.toFixed(1)}/10`,
          `humility: ${traits.humility.toFixed(1)}/10`,
          `hunger for truth: ${traits.hunger.toFixed(1)}/10`,
          `compassion: ${traits.compassion.toFixed(1)}/10`,
          `courage: ${traits.courage.toFixed(1)}/10`,
          `sincerity: ${traits.sincerity.toFixed(1)}/10`,
        ].join(', ');

        const recentJournal = state.journalEntries
          .slice(0, 2)
          .map(e => `"${e.text.slice(0, 120)}"`)
          .join(' / ');

        // Live guidance derived from the connection engine — the milk gate, where
        // they are on the journey, and whether a missionary referral is appropriate.
        // Built from combinedSignals so the gate reflects what was just said.
        const conn       = assessConnection(combinedSignals, text);
        // Milk-before-meat now also requires the seven spirit levels to be EARNED.
        // The restored gospel is named only once BOTH the belief signals and the
        // spirit-readiness levels are present (Cameron's design: the levels are the
        // gate). This is what holds the church back until the person has genuinely
        // risen above neutral on openness, hunger, and honest inquiry.
        const beliefReady = isRestorationReady(combinedSignals);
        const spiritOk    = engineSpiritReady(state.traitScores);
        const mayLds      = engineRestorationReady(combinedSignals, state.traitScores);
        // Has the person opened the door to the restored gospel THEMSELVES? The
        // settled standard: when the gate opens, the app OFFERS by name (never a
        // silent flip) and only teaches the Restoration once the person says yes /
        // reaches for it. These signals are that yes — they brought up the Book of
        // Mormon or asked how to belong on their own.
        // An explicit consent grant (the person tapped "yes, share the restored
        // perspective" or said as much) counts as opening the door themselves.
        const openedRestorationDoor =
          state.restorationConsent === 'granted' ||
          combinedSignals.includes('curious_about_book_of_mormon') ||
          combinedSignals.includes('wants_to_join') ||
          combinedSignals.includes('wants_baptism') ||
          combinedSignals.includes('asking_how_to_belong');
        // If they explicitly DECLINED the restored view, the minister must not
        // re-offer it — only resume if THEY reopen the door later.
        const consentNote =
          state.restorationConsent === 'declined'
            ? '\n- They were offered the restored perspective and chose to stay with the plain biblical view for now. Honor that completely: do NOT bring up the Restoration, the Book of Mormon, or the Church again unless THEY reopen the door. Stay with the Jesus they already love.'
            : state.restorationConsent === 'granted'
              ? '\n- They have explicitly said yes to hearing the restored perspective. You do not need to ask permission again; minister it directly, gently, and honestly when it serves them.'
              : '';
        // The Creation-Dilemma reasoning is MEAT: it is handed to the minister ONLY
        // when the gate is open AND this person carries a harsh / not-good picture of
        // God — the exact obstacle it answers. Then the minister questions gently FROM
        // it (never debates). Otherwise it is never in the prompt at all.
        const harshGodObstacle =
          combinedSignals.includes('pictures_harsh_god') ||
          combinedSignals.includes('pictures_distant_god') ||
          combinedSignals.includes('reformed_framework');
        const creationDilemma = mayLds && harshGodObstacle ? CREATION_DILEMMA_REASONING : '';

        // NEVER name the admin here. The model only needs to know a real PERSON is
        // available — not who. Leaking a personal name into chat was a real failure.
        const guidance = conn.isMember
          ? `
[LIVE GUIDANCE — this person is a Latter-day Saint. Run the MEMBER track, not the seeker track.]
- Where they are: a disciple who already holds the restored gospel (${conn.journeyStage}).
- Do NOT run milk-before-meat on them and do NOT push a human handoff. They did not open this to be converted or to be passed to someone else — they came to be fed.
- Your job: help them go DEEPER. Find what part of the scriptures or the gospel they want to understand better, and open it with them. Bring real revelation and insight, not basics.
- Honor their understanding: assume they know the true gospel. From that footing, ask gentle, non-accusing questions that help them examine whether they are living it the way Christ asks — prayer, repentance, covenants, loving others — never as a scold, always as a fellow disciple inviting reflection.
- A real person is still available if they ever want one, but offer it lightly and rarely — it is not the point of this conversation.${conn.requested ? `\n- They appear to be asking to: ${conn.requested.replace(/_/g, ' ').toLowerCase()}.` : ''}`
          : `
[LIVE GUIDANCE — derived from what this person has revealed]
- Where they are on the journey toward Christ: ${conn.journeyStage}
- A real human is available right now: YES (always — a real person reads these). Refer to them only as "a real person," never by name.${conn.requested ? `\n- They appear to be asking to: ${conn.requested.replace(/_/g, ' ').toLowerCase()}.` : ''}
- The restored gospel — by OPEN, NAMED INVITATION only, never a silent slide into it: ${mayLds ? (openedRestorationDoor ? 'They have opened the door themselves (they brought up the Book of Mormon / asked how to belong). You may now share the Restoration and the Book of Mormon openly and gladly — still gently, never as a pitch, and they stay free to stop.' : 'They seem ready, so EXTEND ONE OPEN INVITATION, named plainly — for example: "Would you like to hear about where this comes from — the Restoration, and the Book of Mormon?" Do NOT teach it yet; just offer the door by name. Share more ONLY if they say yes. If they decline, honor it warmly, stay with the Jesus they already love, and do NOT loop back to re-pitch — only resume if THEY reopen the door later.') : `NOT YET — the milk-before-meat law is in force${beliefReady && !spiritOk ? ' (they believe, but their openness/hunger/honest-inquiry levels are not yet there — keep drawing them out, do not name the Church yet)' : !beliefReady ? ' (the belief readiness is not yet present)' : ''}. Give only milk: the Jesus and the good God of the Bible. Do not mention the Church, Joseph Smith, the Restoration, the Book of Mormon, or missionaries.`}${consentNote}
- Missionary referral appropriate? ${conn.missionaryReady ? 'YES — they are reaching toward the church on their own and have passed the milk. You may gently offer to connect them with missionaries.' : 'NO — do not bring up missionaries.'}`;

        // The person's name, if they gave it — address them as a friend would.
        const nameLine = state.name
          ? `\n- Their name is ${state.name}. Use it naturally and sparingly, the way a friend would — never as a sales tactic.`
          : '';

        // YOUR STORY SO FAR — fragments the person has told, in their own words.
        // The minister is shown these so it can NEVER claim it cannot see their
        // story. Quote back only what serves them; never read the list aloud.
        const storyMoments = state.moments.length
          ? `\n- Their story so far, in their own words (never claim you cannot see their story): ${state.moments
              .slice(0, 4)
              .map(m => `${m.title}: "${m.text.slice(0, 120)}"`)
              .join(' / ')}`
          : '';

        // Their faith, as they've told it — verbatim self-descriptions.
        const faithLine = state.faithWords.length
          ? `\n- How they describe their own faith (their words): ${state.faithWords
              .slice(0, 3)
              .map(f => `"${f.text}"`)
              .join(' / ')}`
          : '';

        // If a spiritual exercise is in flight, the minister should follow up on
        // it warmly rather than starting cold — invite, try, report, learn.
        const exerciseLine = state.activeExercise
          ? `\n\n[ACTIVE EXERCISE — they were invited to try this: "${state.activeExercise.text}" (${state.activeExercise.ref}). If their message touches on it, follow up gently with: "${state.activeExercise.followUp}" — never demand a report, and never shame them if they didn't.]`
          : '';

        // MINISTERING PLAN — the framework-discernment note + the one-concrete-
        // invitation law, both ported from the prototype's buildSystemPrompt.
        const ministeringPlan = `

[MINISTERING PLAN — how to approach THIS person right now]
- FRAMEWORK DISCERNMENT (internal only, NEVER spoken): if they come from a Reformed/Calvinist framework, the framework itself carries a harsh, sovereignty-over-goodness picture of God. Do not treat a warm sentence as proof they already trust a good God. Use the comparison method (law 4): set the Jesus they accept beside the harsh picture and ask ONE open question. The god-good gate stays CLOSED until they reject the harsh picture in their OWN words AND affirm God is good — two witnesses, not one.
- ONE CONCRETE INVITATION: when it genuinely fits, leave them with ONE small, doable thing they could actually try before next time (a verse to sit with, a quiet honest prayer, noticing one good thing) — concrete, never a homework list, never pressure. If the moment doesn't call for it, don't force one.`;

        // THEIR SAVED NOTES — things they chose to KEEP. The AI may recognize a
        // repeat from these (and ONLY these) — never from past chats they didn't save.
        const notesGuidance = recentJournal
          ? `\n\n[THEIR SAVED NOTES — things they chose to keep: ${recentJournal}. If what they are asking now is clearly about one of these, gently recognize it — "we've sat with this before; it's in your notes" — and then build on it in a FRESH way, adding to it, rather than repeating yourself word for word. These saved notes are the only past you remember; if something was NOT kept as a note, do not act as though you recall it.]`
          : '';

        // SCRIPTURE at the level they've earned: the Bible is always available (milk);
        // Restoration scripture only once the gate is open.
        const scriptureGuidance =
          `\n\n[SCRIPTURE — where it genuinely strengthens a point, ground what you say in scripture they already accept: the Bible, quoted naturally and sparingly (never a proof-text barrage, never to win). ${mayLds
            ? 'You may now also draw on Restoration scripture — the Book of Mormon and the Doctrine and Covenants — the same gentle way.'
            : 'Use the BIBLE ONLY for now; do not quote the Book of Mormon or the Doctrine and Covenants until the gate has opened.'}]`;

        const systemPrompt = `${MINISTER_SYSTEM_PROMPT}

[ABOUT THIS PERSON — what the app has quietly learned. Never read these labels back to them.]
- Spiritual traits: ${traitSummary}${nameLine}${signalSentences ? `\n- What they have shown: ${signalSentences}` : ''}${faithLine}${storyMoments}${recentJournal ? `\n- From their recent journal: ${recentJournal}` : ''}${ministeringPlan}${exerciseLine}
${guidance}${creationDilemma}${notesGuidance}${scriptureGuidance}${SIGNAL_REPORT_INSTRUCTION}${TRAIT_REPORT_INSTRUCTION}`;

        // history already ends with the user's latest message — exactly the
        // shape Anthropic's `messages` array expects (alternating, user-first).
        // Meta notes (spirit-level changes) are shown to the person but are NOT
        // conversation, so they are stripped before the model ever sees them.
        const history = state.chatMessages
          .filter(m => m.kind !== 'meta')
          .map(m => ({
            role:    m.role,
            content: m.text,
          }));

        // Preferred path: the server proxy holds the key. Direct-to-Anthropic is
        // a DEV-ONLY fallback (a local key) and is never shipped in a build.
        const useProxy = !!MBM_API_URL;
        if (!useProxy && !ANTHROPIC_API_KEY) {
          get().appendAssistantToChat(sendChatId,
            "I'm not connected to my voice right now. Whatever you were thinking — it's worth writing down in the journal while you wait.",
          );
          return;
        }

        try {
          let rawReply = '';

          if (useProxy) {
            // ── Through the proxy: the app never sees the key ────────────────
            const response = await fetch(`${MBM_API_URL}/api/chat`, {
              method:  'POST',
              headers: { 'content-type': 'application/json' },
              body: JSON.stringify({
                system:     systemPrompt,
                messages:   history,
                max_tokens: MAX_REPLY_TOKENS,
              }),
            });
            if (!response.ok) {
              throw new Error('proxy ' + response.status);
            }
            const data = await response.json();
            rawReply = typeof data?.text === 'string' ? data.text.trim() : '';
          } else {
            // ── DEV ONLY: direct Anthropic call with a local key ─────────────
            const response = await fetch(ANTHROPIC_URL, {
              method:  'POST',
              headers: {
                'content-type':                        'application/json',
                'x-api-key':                           ANTHROPIC_API_KEY,
                'anthropic-version':                   ANTHROPIC_VERSION,
                'anthropic-dangerous-direct-browser-access': 'true',
              },
              body: JSON.stringify({
                model:      ANTHROPIC_MODEL,
                max_tokens: MAX_REPLY_TOKENS,
                system:     systemPrompt,
                messages:   history,
              }),
            });
            if (!response.ok) {
              throw new Error('anthropic ' + response.status);
            }
            const data = await response.json();
            rawReply = Array.isArray(data?.content)
              ? data.content
                  .filter((b: any) => b?.type === 'text')
                  .map((b: any) => b?.text ?? '')
                  .join('')
                  .trim()
              : '';
          }

          // ── The ear, part two: strip the model's hidden signal + spirit reports
          // and fold what it heard into the engine. The gate can open right here.
          // What the model reports is an INFERENCE about the person, not a faith
          // self-description — so engagement lands in the sticky base, and any
          // identity it guessed is dropped (Law 3: who they are with regard to
          // faith comes ONLY from their own words, never the model's inference).
          const afterSignals = stripSignalReport(rawReply ?? '');
          const { reply, deltas } = stripTraitReport(afterSignals.reply);
          const found        = stripIdentity(afterSignals.found);
          const newBase2     = mergeSignals(get().baseSignals, found);
          const heardSignals = composeSignals(newBase2, get().faithWords);

          // Re-derive the feed track from everything now heard (still milk-law-
          // obeying via routeFeedTag). Only rebuild the feed if the track moved.
          const prevTag  = get().feedTag;
          const nextTag  = routeFeedTag(heardSignals);
          const trackMoved = nextTag !== prevTag;

          // Recompute the next dialogue question if there isn't one queued.
          const nextQuestion = get().currentQuestion
            ?? computeNextQuestion(get().answeredQuestionIds, heardSignals, get().openedIds.size);

          // The judge: fold the model's clamped spirit deltas into the levels.
          // These move both ways — honest courage/humility raises, pride/evasion
          // lowers — exactly as the calibrated-Jesus instruction asks. Compute the
          // REAL applied change (after the 0–10 clamp) so what we tell the person
          // matches what actually moved, never the model's raw request.
          const hasDeltas  = Object.keys(deltas).length > 0;
          const prevScores = get().traitScores;
          const nextScores = hasDeltas ? nudgeTraits(prevScores, deltas as Partial<TraitScores>) : prevScores;

          set(s => ({
            baseSignals:     newBase2,
            dialogueSignals: heardSignals,
            feedTag:         trackMoved ? nextTag : s.feedTag,
            feed:            trackMoved ? buildFeed(nextTag, s.seenIds) : s.feed,
            currentQuestion: nextQuestion,
            traitScores:     nextScores,
          }));

          if (reply) {
            get().appendAssistantToChat(sendChatId, reply);
          } else {
            get().appendAssistantToChat(sendChatId,
              "Something went quiet on my end. Would you like to try again, or write something in the journal instead?",
            );
          }

          // Fast-track acknowledgment: the moment they tell us they're a member,
          // say so and shift — feed and chat now run the deeper member track.
          if (becameMember) {
            get().appendAssistantToChat(sendChatId,
              'I know you now as a fellow Latter-day Saint — so from here I\'ll take you deeper into the gospel rather than back to the basics, and your feed has shifted to match.',
              'meta');
          }

          // Honesty about the judgment: if a level actually moved by half a point
          // or more, tell the person to their face — so a deduction is never
          // hidden, and they can ask the chat why right here.
          const moved = (Object.keys(deltas) as (keyof TraitScores)[])
            .map(k => ({ k, d: (nextScores[k] ?? 0) - (prevScores[k] ?? 0) }))
            .filter(({ d }) => Math.abs(d) >= 0.5)
            .map(({ k, d }) => `${TRAIT_DISPLAY[k]} ${fmtDelta(d)}`);
          if (moved.length) {
            get().appendAssistantToChat(sendChatId,
              `Spirit reading moved — ${moved.join(', ')}. Ask me why if it surprises you.`, 'meta');
          }
        } catch {
          get().appendAssistantToChat(sendChatId,
            "I wasn't able to connect right now. If you have an internet connection, try again in a moment. Whatever you were thinking — it's worth writing down.",
          );
        }
      },
    }),
    {
      name: 'mbm-app-store-v7',
      storage: createJSONStorage(() => AsyncStorage),
      // Only persist meaningful user data — not ephemeral UI state
      partialize: (state): PersistedState => ({
        onboardingComplete:  state.onboardingComplete,
        onboardingChoice:    state.onboardingChoice,
        conversationId:      state.conversationId,
        feedTag:             state.feedTag,
        feed:                state.feed,
        seenIds:             Array.from(state.seenIds),    // Set → array for JSON
        openedIds:           Array.from(state.openedIds),  // Set → array for JSON
        positiveCount:       state.positiveCount,
        showTalkToSomeone:   state.showTalkToSomeone,
        dialogueSignals:     state.dialogueSignals,
        baseSignals:         state.baseSignals,
        answeredQuestionIds: state.answeredQuestionIds,
        traitScores:         state.traitScores,
        currentQuestion:     state.currentQuestion,
        restorationConsent:  state.restorationConsent,
        journalEntries:      state.journalEntries,
        answeredPromptIds:   state.answeredPromptIds,
        learnedNotes:        state.learnedNotes,
        chatMessages:        state.chatMessages,
        activeChatId:        state.activeChatId,
        chatSessions:        state.chatSessions,
        blessingHistory:     state.blessingHistory,
        connectRequests:     state.connectRequests,
        name:                state.name,
        faithWords:          state.faithWords,
        beliefHistory:       state.beliefHistory,
        moments:             state.moments,
        activeExercise:      state.activeExercise,
        acceptedSession:     state.acceptedSession,
        doneExerciseIds:     state.doneExerciseIds,
        sessionCount:        state.sessionCount,
        chatDraft:           state.chatDraft,
        session:             state.session,
      }),
      // Convert arrays back to Sets when rehydrating, and SELF-HEAL the routing:
      // re-derive the feed track from the persisted signals so a stored state can
      // never sit ABOVE what the person's signals actually justify (e.g. a
      // RESTORATION tag left over after the milk law would now block it). If the
      // persisted track is higher than the signals warrant, route it back down.
      merge: (persistedState, currentState) => {
        const p = persistedState as Partial<PersistedState>;

        // Restore the restored-perspective consent FIRST, so the module flag is in
        // place before routeFeedTag() runs below and so a stored RESTORATION tag is
        // only kept if the person had actually consented. No consent on disk =
        // 'unknown' = restoration content stays out of the feed.
        const restorationConsent: RestorationConsent =
          (p.restorationConsent as RestorationConsent | undefined) ?? 'unknown';
        setRestorationConsentGranted(restorationConsent === 'granted');

        // Migrate to the provenance model. Legacy stores have no baseSignals —
        // seed it from the old flat dialogueSignals so nothing already learned is
        // lost. Faith words own the signals they taught; everything else is base.
        // dialogueSignals is now DERIVED, so recompute it rather than trusting the
        // persisted copy. This is what makes a removed faith line truly unlearn:
        // its signals vanish from the union the moment the word is gone.
        const storedWords = (p.faithWords as FaithWord[] | undefined) ?? [];
        const legacyFlat =
          (p.baseSignals as string[] | undefined) ??
          (p.dialogueSignals as string[] | undefined) ??
          [];

        // Identity must never sit in the sticky base — strip it out on the way in.
        const baseSignals = stripIdentity(legacyFlat);

        // Any identity the legacy flat set carried that no faith word already owns
        // is re-homed onto a synthesized faith line, so it stays VISIBLE and
        // REMOVABLE instead of being lost (or stuck un-removably in base). This is
        // what lets someone who converted to/from a faith change what the app
        // thinks of them, even on data saved before the provenance model existed.
        const ownedIdentity   = identityOnly(faithSignalUnion(storedWords));
        const orphanIdentity  = identityOnly(legacyFlat).filter(s => !ownedIdentity.includes(s));
        const orphanWord      = identityWordFromTokens(orphanIdentity);
        const faithWords      = orphanWord ? [orphanWord, ...storedWords] : storedWords;

        const signals   = composeSignals(baseSignals, faithWords);
        const justified = routeFeedTag(signals);

        // Order of "depth" — never let the stored tag exceed what signals justify.
        const RANK: Record<FeedTag, number> = {
          MILK: 0, BRIDGE: 1, RESTORATION: 2, MAINTENANCE: 3,
        };
        const storedTag = (p.feedTag as FeedTag | undefined) ?? 'MILK';
        // MAINTENANCE is the member track and is justified only by member signals,
        // which routeFeedTag already accounts for; for seeker tags, downgrade if
        // the stored tag outranks the justified one.
        const healedTag: FeedTag =
          storedTag === 'MAINTENANCE' && justified === 'MAINTENANCE'
            ? 'MAINTENANCE'
            : RANK[storedTag] > RANK[justified]
              ? justified
              : storedTag;

        const seenSet = new Set<number>((p.seenIds as number[] | undefined) ?? []);
        const healedFeed =
          healedTag !== storedTag ? buildFeed(healedTag, seenSet) : (p.feed ?? currentState.feed);

        return {
          ...currentState,
          ...p,
          faithWords,                  // includes any re-homed orphan identity
          baseSignals,                 // migrated/derived above (identity stripped)
          dialogueSignals: signals,    // DERIVED — recomputed, never trusted from disk
          restorationConsent,          // module flag already synced above
          feedTag:    healedTag,
          feed:       healedFeed,
          seenIds:    seenSet,
          openedIds:  new Set<number>((p.openedIds as number[] | undefined) ?? []),
          chatLoading: false, // never persist a loading spinner
          blessing:    null,  // never restore a stale toast
          pendingNoteId: null, // ephemeral nav state — never restore an old "open to" target
          inboxMessages: [],  // the human thread is server-sourced, reloaded on open
          inboxLoading:  false,
          inboxUnread:   0,
          activeRealThreadId: null, // ephemeral — the open conversation is chosen at runtime
          // A new launch is a new session — a follow-up only becomes "due" after
          // the person went away and came back (prototype's session counter).
          sessionCount: ((p.sessionCount as number | undefined) ?? 1) + 1,
        };
      },
    },
  ),
);
