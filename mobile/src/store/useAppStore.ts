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
  missionaryReferralReady as engineMissionaryReady,
  isMember as engineIsMember,
  assessJourney,
  assessConnection,
} from '../engine/connect';
import { MINISTER_SYSTEM_PROMPT, MINISTER_MODEL } from '../engine/minister';
import {
  harvestSignals,
  stripSignalReport,
  SIGNAL_REPORT_INSTRUCTION,
  FAITH_ID_RE,
} from '../engine/chatEar';
import {
  EXERCISES,
  pickExercise,
  SpiritualExercise,
} from '../engine/exercises';

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

// Silently choose the content level that fits the signals a person has revealed.
// Invisible: the user never sees a tier name or a gate. The milk law is absolute —
// RESTORATION is only ever chosen once both readiness signals exist.
function routeFeedTag(signals: string[]): FeedTag {
  if (engineIsMember(signals)) return 'MAINTENANCE';

  const analytical = ['skeptical_of_god', 'analytical_doubt', 'honest_inquiry', 'losing_faith'];
  const hasAnalytic = signals.some(s => analytical.includes(s));

  // Meat only after milk: restored-gospel content is gated on both readiness signals.
  if (engineMayReferenceLds(signals)) return 'RESTORATION';
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

function buildFeed(tag: FeedTag, seenIds: Set<number>): ContentItem[] {
  const pool   = CONTENT.filter(c => c.tag === tag);
  const unseen = pool.filter(c => !seenIds.has(c.id));
  const source = unseen.length >= 5 ? unseen : pool;
  return [...source].sort(() => Math.random() - 0.5).slice(0, 5);
}

// User-initiated "show me something more substantive" — a preference, not a gate.
// It still obeys the milk law: it will not jump to RESTORATION unless the person's
// signals have opened that door. It nudges one honest step (MILK→BRIDGE), and only
// reaches RESTORATION when both readiness signals are present.
function deeperFeedTag(current: FeedTag, signals: string[]): FeedTag {
  if (engineIsMember(signals)) return 'MAINTENANCE';
  if (current === 'MILK') return 'BRIDGE';
  if (current === 'BRIDGE') {
    return engineMayReferenceLds(signals) ? 'RESTORATION' : 'BRIDGE';
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

// ── Anthropic (local-first: the app calls Claude directly) ───────────────────
// Per CLAUDE.md the app is local-first and runs with no server terminal. The key
// is read from EXPO_PUBLIC_ANTHROPIC_API_KEY (mobile/.env, which is gitignored).
const ANTHROPIC_API_KEY = (process.env.EXPO_PUBLIC_ANTHROPIC_API_KEY ?? '').trim();
const ANTHROPIC_URL     = 'https://api.anthropic.com/v1/messages';
const ANTHROPIC_MODEL   = MINISTER_MODEL;
const ANTHROPIC_VERSION = '2023-06-01';
const MAX_REPLY_TOKENS  = 512;

function generateId(): string {
  return Math.random().toString(36).slice(2) + Date.now().toString(36);
}

// Blessing pools — encouragement in WORDS, never numbers. The way Jesus affirmed
// people: specific, warm, right after the reach. Ported verbatim from the prototype.
export const BLESS_DIALOGUE = [
  'Thank you for letting yourself be asked.',
  'Most people never answer that honestly. You just did.',
  'Your courage is showing.',
  'Noticing that about yourself is its own kind of light.',
];
export const BLESS_HEART = [
  'What moves you says something good about you.',
  'Kept. What resonates with you is worth following.',
  'Good eye. That one matters.',
];
export const JOURNAL_BLESS = [
  'Some things only become clear once they are said. You just said one.',
  'You said the true thing. That takes more courage than it looks.',
  'That is yours now — named, and a little lighter for it.',
];

function pickLine(pool: string[]): string {
  return pool[Math.floor(Math.random() * pool.length)] ?? '';
}

// Small, clamped trait nudge — the way the prototype's nudgedTraits worked.
function nudgeTraits(scores: TraitScores, deltas: Partial<TraitScores>): TraitScores {
  const next: TraitScores = { ...scores };
  for (const [k, d] of Object.entries(deltas)) {
    const key = k as keyof TraitScores;
    const cur = next[key] ?? 5;
    next[key] = Math.round(Math.max(TRAIT_MIN, Math.min(TRAIT_MAX, cur + (d ?? 0))) * 1000) / 1000;
  }
  return next;
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
  dialogueSignals:     string[];
  answeredQuestionIds: number[];
  traitScores:         TraitScores;
  currentQuestion:     DialogueQuestion | null;

  // Journal
  journalEntries:      JournalEntry[];
  answeredPromptIds:   string[];

  // Chat
  chatMessages:        ChatMessage[];
  chatLoading:         boolean;

  // Human connection requests, captured on-device (Phase 1)
  connectRequests:     ConnectRequest[];

  // The person, in their own words — never labels, never numbers shown to them
  name:                string | null;
  faithWords:          FaithWord[];
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

  // A blessing toast — words only, shown briefly after a meaningful act.
  blessing:            string | null;

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
  refreshFeed:         () => void;
  resetSession:        () => void;
  answerQuestion:      (questionId: number, answerValue: string, answerText?: string) => void;
  addJournalEntry:     (promptId: string, promptText: string, text: string) => void;
  sendChatMessage:     (text: string) => Promise<void>;
  setChatLoading:      (loading: boolean) => void;
  appendAssistantMessage: (text: string) => void;
  submitConnectRequest: (note: string) => void;
  setName:             (name: string) => void;
  recordFaithBackground: (choiceKey: string, text: string) => void;
  addMoment:           (title: string, text: string) => void;
  acceptExercise:      (ex: SpiritualExercise) => void;
  passExercise:        (ex: SpiritualExercise) => void;
  answerFollowUp:      (value: 'something' | 'good' | 'nothing' | 'not_yet', note?: string) => void;
  reflectOnContent:    (item: ContentItem, text: string) => void;
  prefillChat:         (text: string) => void;
  clearChatDraft:      () => void;
  bless:               (pool: string[]) => void;
  clearBlessing:       () => void;
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
  answeredQuestionIds: [],
  traitScores:         { ...DEFAULT_TRAITS },
  currentQuestion:     null,
  journalEntries:      [],
  answeredPromptIds:   [],
  chatMessages:        [],
  chatLoading:         false,
  connectRequests:     [],
  name:                null,
  faithWords:          [],
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

type PersistedState = Omit<AppState, 'seenIds' | 'openedIds' | 'chatLoading' | 'conversationId' | 'blessing'> & {
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
          dialogueSignals:     seedSignals,
          answeredQuestionIds: [],
          traitScores:         { ...DEFAULT_TRAITS },
          currentQuestion,
          journalEntries:      [],
          answeredPromptIds:   [],
          chatMessages:        [],
          chatLoading:         false,
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
        get().bless(BLESS_HEART);
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

      refreshFeed() {
        // "Show me more →" — rebuild WITHIN the current track only. Never a gate,
        // never a jump: the same kind of content, freshly drawn. Routing stays
        // invisible and obeys the milk law because the track does not change.
        const { feedTag, seenIds } = get();
        set({ feed: buildFeed(feedTag, seenIds) });
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
          dialogueSignals,
          traitScores,
          openedIds,
        } = get();

        const question = QUESTION_BANK.find(q => q.id === questionId);
        if (!question) return;

        const newTraits: TraitScores = { ...traitScores };
        const newSignals = new Set(dialogueSignals);
        let deltas: Partial<TraitScores> = {};

        if (question.answerType === 'CHOICE' || question.answerType === 'YES_NO') {
          const opt = question.answerOptions.find(o => o.value === answerValue);
          if (opt) {
            deltas = opt.traitSignals ?? {};
            (opt.signals ?? []).forEach(s => newSignals.add(s));
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
          // from what they type here, not only from chat.
          if (answerText) {
            harvestSignals(answerText).forEach(s => newSignals.add(s));
          }
        }

        for (const [k, delta] of Object.entries(deltas)) {
          const key     = k as keyof TraitScores;
          const current = newTraits[key] ?? 5.0;
          newTraits[key] = Math.round(
            Math.max(TRAIT_MIN, Math.min(TRAIT_MAX, current + (delta ?? 0))) * 1000,
          ) / 1000;
        }

        const newAnsweredIds = [...answeredQuestionIds, questionId];
        const newSignalsArr  = Array.from(newSignals);

        const currentQuestion = computeNextQuestion(
          newAnsweredIds,
          newSignalsArr,
          openedIds.size,
        );

        // Keep a verbatim faith self-description if the free-text answer is one.
        const faithCapture =
          question.answerType === 'FREE_TEXT' && answerText && FAITH_ID_RE.test(answerText)
            ? { text: answerText.slice(0, 140), ts: Date.now() }
            : null;

        // Emergent routing: re-derive the feed track from what they've now shown
        // (still milk-law-obeying). Only rebuild the feed if the track moved.
        const { feedTag: prevTag, seenIds, feed: prevFeed, faithWords } = get();
        const nextTag    = routeFeedTag(newSignalsArr);
        const trackMoved = nextTag !== prevTag;

        set({
          answeredQuestionIds: newAnsweredIds,
          dialogueSignals:     newSignalsArr,
          traitScores:         newTraits,
          currentQuestion,
          feedTag:             trackMoved ? nextTag : prevTag,
          feed:                trackMoved ? buildFeed(nextTag, seenIds) : prevFeed,
          faithWords:          faithCapture ? [faithCapture, ...faithWords] : faithWords,
        });
        get().bless(BLESS_DIALOGUE);
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
        const heur       = harvestSignals(text);
        const { dialogueSignals, answeredQuestionIds, openedIds, feedTag: prevTag, seenIds, feed: prevFeed } = get();
        const merged     = mergeSignals(dialogueSignals, heur);
        const nextTag    = routeFeedTag(merged);
        const trackMoved = nextTag !== prevTag;

        set(s => ({
          journalEntries:    [entry, ...s.journalEntries],
          answeredPromptIds: [...s.answeredPromptIds, promptId],
          dialogueSignals:   merged,
          feedTag:           trackMoved ? nextTag : prevTag,
          feed:              trackMoved ? buildFeed(nextTag, seenIds) : prevFeed,
          currentQuestion:   s.currentQuestion
            ?? computeNextQuestion(answeredQuestionIds, merged, openedIds.size),
        }));
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

        const faithSignals = [...meta.signals, ...(clean ? harvestSignals(clean) : [])];
        const { dialogueSignals, answeredQuestionIds, openedIds } = get();
        const merged = mergeSignals(dialogueSignals, faithSignals);

        const newWords: FaithWord[] = [];
        if (meta.label && choiceKey !== 'private') newWords.push({ text: meta.label, ts: Date.now() });
        if (clean) newWords.push({ text: clean.slice(0, 140), ts: Date.now() });

        const newAnswered = (choiceKey && choiceKey !== 'private' && !answeredQuestionIds.includes(2.5))
          ? [...answeredQuestionIds, 2.5]
          : answeredQuestionIds;

        const momentDetail = `“${(clean || meta.label).slice(0, 90)}”`;
        const nextTag = routeFeedTag(merged);
        set(s => ({
          faithWords:      [...newWords, ...s.faithWords],
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

      addMoment(title, text) {
        const t = (title ?? '').trim().slice(0, 60);
        const b = (text ?? '').trim().slice(0, 280);
        if (!b) return;
        set(s => ({ moments: [{ title: t || 'A moment', text: b, ts: Date.now() }, ...s.moments] }));
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
        const { activeExercise, doneExerciseIds, traitScores, dialogueSignals,
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
        const heard    = mergeSignals(dialogueSignals, [...o.signals, ...harvestSignals(trimmed)]);
        const nextTag  = routeFeedTag(heard);
        const moved    = nextTag !== prevTag;
        const traitDeltas = trimmed ? { ...o.traits, sincerity: (o.traits.sincerity ?? 0) + 0.1 } : o.traits;

        set(s => ({
          activeExercise:  null,
          acceptedSession: null,
          doneExerciseIds: s.doneExerciseIds.includes(ex.id) ? s.doneExerciseIds : [...s.doneExerciseIds, ex.id],
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
        const { traitScores, dialogueSignals, feedTag: prevTag, seenIds, feed: prevFeed } = get();
        const heard   = mergeSignals(dialogueSignals, harvestSignals(t));
        const nextTag = routeFeedTag(heard);
        const moved   = nextTag !== prevTag;
        set(s => ({
          journalEntries:  [entry, ...s.journalEntries],
          dialogueSignals: heard,
          traitScores:     nudgeTraits(traitScores, { sincerity: 0.2, hunger: 0.1 }),
          feedTag:         moved ? nextTag : prevTag,
          feed:            moved ? buildFeed(nextTag, seenIds) : prevFeed,
          moments: [
            { title: `You sat with “${item.title}”`, text: `“${t.slice(0, 80)}${t.length > 80 ? '…' : ''}”`, ts: Date.now() },
            ...s.moments,
          ],
        }));
        get().bless(['Kept — in your journal now.', 'Sitting with a thing is how it takes root.']);
      },

      prefillChat(text) {
        set({ chatDraft: text });
      },

      clearChatDraft() {
        set({ chatDraft: '' });
      },

      bless(pool) {
        const line = pickLine(pool);
        if (!line) return;
        set({ blessing: line });
        setTimeout(() => {
          // Only clear if this same blessing is still showing.
          if (get().blessing === line) set({ blessing: null });
        }, 3400);
      },

      clearBlessing() {
        set({ blessing: null });
      },

      async sendChatMessage(text) {
        const userMsg: ChatMessage = {
          id:        Date.now().toString(),
          role:      'user',
          text,
          timestamp: Date.now(),
        };

        // ── The ear: harvest signals from THIS message BEFORE the prompt ─────
        // so the milk gate can open mid-conversation and the guidance below is
        // built from everything the person has revealed, including just now.
        const heur            = harvestSignals(text);
        const priorSignals    = get().dialogueSignals;
        const combinedSignals = mergeSignals(priorSignals, heur);

        // Keep faith self-descriptions VERBATIM in the person's faith record.
        const newFaithWord: FaithWord | null = FAITH_ID_RE.test(text)
          ? { text: text.slice(0, 140), ts: Date.now() }
          : null;

        set(s => ({
          chatMessages: [...s.chatMessages, userMsg],
          chatLoading:  true,
          dialogueSignals: combinedSignals,
          faithWords:  newFaithWord ? [newFaithWord, ...s.faithWords] : s.faithWords,
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
          `hunger for truth: ${traits.hunger.toFixed(1)}/10`,
          `openness: ${traits.openness.toFixed(1)}/10`,
          `sincerity: ${traits.sincerity.toFixed(1)}/10`,
          `courage: ${traits.courage.toFixed(1)}/10`,
        ].join(', ');

        const recentJournal = state.journalEntries
          .slice(0, 2)
          .map(e => `"${e.text.slice(0, 120)}"`)
          .join(' / ');

        // Live guidance derived from the connection engine — the milk gate, where
        // they are on the journey, and whether a missionary referral is appropriate.
        // Built from combinedSignals so the gate reflects what was just said.
        const conn       = assessConnection(combinedSignals, text);
        const mayLds     = isRestorationReady(combinedSignals);

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
- May you reference the restored gospel / The Church of Jesus Christ of Latter-day Saints / the Book of Mormon yet? ${mayLds ? 'YES — both readiness signals are present. You may do so gently, honestly, never as a pitch.' : 'NO — the milk-before-meat law is in force. Give only milk: the Jesus and the good God of the Bible. Do not mention the Church, Joseph Smith, the Restoration, the Book of Mormon, or missionaries.'}
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

        const systemPrompt = `${MINISTER_SYSTEM_PROMPT}

[ABOUT THIS PERSON — what the app has quietly learned. Never read these labels back to them.]
- Spiritual traits: ${traitSummary}${nameLine}${signalSentences ? `\n- What they have shown: ${signalSentences}` : ''}${faithLine}${storyMoments}${recentJournal ? `\n- From their recent journal: ${recentJournal}` : ''}${ministeringPlan}${exerciseLine}
${guidance}${SIGNAL_REPORT_INSTRUCTION}`;

        // history already ends with the user's latest message — exactly the
        // shape Anthropic's `messages` array expects (alternating, user-first).
        const history = state.chatMessages.map(m => ({
          role:    m.role,
          content: m.text,
        }));

        if (!ANTHROPIC_API_KEY) {
          get().appendAssistantMessage(
            "I'm not connected to my voice right now. Whatever you were thinking — it's worth writing down in the journal while you wait.",
          );
          return;
        }

        try {
          // ── Call Anthropic directly (local-first) ─────────────────────────
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
          const rawReply = Array.isArray(data?.content)
            ? data.content
                .filter((b: any) => b?.type === 'text')
                .map((b: any) => b?.text ?? '')
                .join('')
                .trim()
            : '';

          // ── The ear, part two: strip the model's hidden signal report and
          // fold what it heard into the engine. The gate can open right here.
          const { reply, found } = stripSignalReport(rawReply ?? '');
          const heardSignals     = mergeSignals(combinedSignals, found);

          // Re-derive the feed track from everything now heard (still milk-law-
          // obeying via routeFeedTag). Only rebuild the feed if the track moved.
          const prevTag  = get().feedTag;
          const nextTag  = routeFeedTag(heardSignals);
          const trackMoved = nextTag !== prevTag;

          // Recompute the next dialogue question if there isn't one queued.
          const nextQuestion = get().currentQuestion
            ?? computeNextQuestion(get().answeredQuestionIds, heardSignals, get().openedIds.size);

          set(s => ({
            dialogueSignals: heardSignals,
            feedTag:         trackMoved ? nextTag : s.feedTag,
            feed:            trackMoved ? buildFeed(nextTag, s.seenIds) : s.feed,
            currentQuestion: nextQuestion,
          }));

          if (reply) {
            get().appendAssistantMessage(reply);
          } else {
            get().appendAssistantMessage(
              "Something went quiet on my end. Would you like to try again, or write something in the journal instead?",
            );
          }
        } catch {
          get().appendAssistantMessage(
            "I wasn't able to connect right now. If you have an internet connection, try again in a moment. Whatever you were thinking — it's worth writing down.",
          );
        }
      },
    }),
    {
      name: 'mbm-app-store-v1',
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
        answeredQuestionIds: state.answeredQuestionIds,
        traitScores:         state.traitScores,
        currentQuestion:     state.currentQuestion,
        journalEntries:      state.journalEntries,
        answeredPromptIds:   state.answeredPromptIds,
        chatMessages:        state.chatMessages,
        connectRequests:     state.connectRequests,
        name:                state.name,
        faithWords:          state.faithWords,
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
        const signals = (p.dialogueSignals as string[] | undefined) ?? [];
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
          feedTag:    healedTag,
          feed:       healedFeed,
          seenIds:    seenSet,
          openedIds:  new Set<number>((p.openedIds as number[] | undefined) ?? []),
          chatLoading: false, // never persist a loading spinner
          blessing:    null,  // never restore a stale toast
          // A new launch is a new session — a follow-up only becomes "due" after
          // the person went away and came back (prototype's session counter).
          sessionCount: ((p.sessionCount as number | undefined) ?? 1) + 1,
        };
      },
    },
  ),
);
