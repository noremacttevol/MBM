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

// ── Constants ───────────────────────────────────────────────────────────────

export const VIEW_CAP = 5;

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

// ── Anthropic API (direct, on-device) ────────────────────────────────────────
// Local-first architecture: the app talks to Claude directly when online.
// The key is read from EXPO_PUBLIC_ANTHROPIC_API_KEY (mobile/.env).
const ANTHROPIC_API_KEY = (process.env.EXPO_PUBLIC_ANTHROPIC_API_KEY ?? '').trim();
const ANTHROPIC_URL     = 'https://api.anthropic.com/v1/messages';
const ANTHROPIC_MODEL   = MINISTER_MODEL;
const ANTHROPIC_VERSION = '2023-06-01';
const MAX_REPLY_TOKENS  = 512;

function generateId(): string {
  return Math.random().toString(36).slice(2) + Date.now().toString(36);
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
  isTimeCapReached:  boolean;
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
}

interface AppActions {
  // choice = story choice key (A/B/C/D/E), feedTag = direct override from story choice
  completeOnboarding:  (choice: string, freeText?: string, feedTag?: FeedTag, signal?: string) => void;
  markOpened:          (id: number) => void;
  thumbsUp:            (id: number) => void;
  bookmark:            (id: number) => void;
  keepSimple:          () => void;
  goDeeper:            () => void;
  resetSession:        () => void;
  answerQuestion:      (questionId: number, answerValue: string, answerText?: string) => void;
  addJournalEntry:     (promptId: string, promptText: string, text: string) => void;
  sendChatMessage:     (text: string) => Promise<void>;
  setChatLoading:      (loading: boolean) => void;
  appendAssistantMessage: (text: string) => void;
  submitConnectRequest: (note: string) => void;
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
  isTimeCapReached:    false,
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
};

// ── Persisted state shape (Sets become arrays for JSON storage) ───────────────

type PersistedState = Omit<AppState, 'seenIds' | 'openedIds' | 'chatLoading' | 'conversationId'> & {
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
          isTimeCapReached:    false,
          showTalkToSomeone:   false,
          dialogueSignals:     seedSignals,
          answeredQuestionIds: [],
          traitScores:         { ...DEFAULT_TRAITS },
          currentQuestion,
          journalEntries:      [],
          answeredPromptIds:   [],
          chatMessages:        [],
          chatLoading:         false,
        });
      },

      markOpened(id) {
        const { openedIds, seenIds, feedTag, dialogueSignals, answeredQuestionIds } = get();
        const newOpenedIds = new Set(openedIds).add(id);
        const newSeenIds   = new Set(seenIds).add(id);
        const openCount    = newOpenedIds.size;

        const isTimeCapReached  = openCount >= VIEW_CAP;
        const showTalkToSomeone = openCount >= 3;

        const currentQuestion = computeNextQuestion(
          answeredQuestionIds,
          dialogueSignals,
          openCount,
        );

        const feed = isTimeCapReached
          ? get().feed
          : buildFeed(feedTag, newSeenIds);

        set({
          openedIds: newOpenedIds,
          seenIds:   newSeenIds,
          feed:      isTimeCapReached ? get().feed : feed,
          isTimeCapReached,
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
          isTimeCapReached: false,
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

        set({
          answeredQuestionIds: newAnsweredIds,
          dialogueSignals:     newSignalsArr,
          traitScores:         newTraits,
          currentQuestion,
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
        set(s => ({
          journalEntries:    [entry, ...s.journalEntries],
          answeredPromptIds: [...s.answeredPromptIds, promptId],
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
        // Capture the request ON-DEVICE and honestly tell the person a real human
        // will reach out. No mailto, no dead-end email draft. When the real
        // delivery channel is built, it reads from this queue and flips delivered.
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

      async sendChatMessage(text) {
        const userMsg: ChatMessage = {
          id:        Date.now().toString(),
          role:      'user',
          text,
          timestamp: Date.now(),
        };

        set(s => ({
          chatMessages: [...s.chatMessages, userMsg],
          chatLoading:  true,
        }));

        const state = get();

        // ── Build system prompt with full user context ──────────────────────

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
          losing_faith:                'is experiencing a faith crisis',
        };

        const signalSentences = state.dialogueSignals
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
        const conn       = assessConnection(state.dialogueSignals, text);
        const mayLds     = isRestorationReady(state.dialogueSignals);

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

        const systemPrompt = `${MINISTER_SYSTEM_PROMPT}

[ABOUT THIS PERSON — what the app has quietly learned. Never read these labels back to them.]
- Spiritual traits: ${traitSummary}${signalSentences ? `\n- What they have shown: ${signalSentences}` : ''}${recentJournal ? `\n- From their recent journal: ${recentJournal}` : ''}
${guidance}`;

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
          // ── Call Claude directly (local-first, on-device) ─────────────────
          const response = await fetch(ANTHROPIC_URL, {
            method:  'POST',
            headers: {
              'content-type':     'application/json',
              'x-api-key':        ANTHROPIC_API_KEY,
              'anthropic-version': ANTHROPIC_VERSION,
              // Required for the browser/web preview (CORS); harmless on native.
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
            throw new Error(`Anthropic error ${response.status}`);
          }

          const data = await response.json();
          const reply = Array.isArray(data?.content)
            ? data.content
                .filter((block: { type?: string }) => block?.type === 'text')
                .map((block: { text?: string }) => block?.text ?? '')
                .join('')
                .trim()
            : '';

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
        isTimeCapReached:    state.isTimeCapReached,
        showTalkToSomeone:   state.showTalkToSomeone,
        dialogueSignals:     state.dialogueSignals,
        answeredQuestionIds: state.answeredQuestionIds,
        traitScores:         state.traitScores,
        currentQuestion:     state.currentQuestion,
        journalEntries:      state.journalEntries,
        answeredPromptIds:   state.answeredPromptIds,
        chatMessages:        state.chatMessages,
        connectRequests:     state.connectRequests,
      }),
      // Convert arrays back to Sets when rehydrating
      merge: (persistedState, currentState) => {
        const p = persistedState as Partial<PersistedState>;
        return {
          ...currentState,
          ...p,
          seenIds:    new Set<number>((p.seenIds   as number[] | undefined) ?? []),
          openedIds:  new Set<number>((p.openedIds as number[] | undefined) ?? []),
          chatLoading: false, // never persist a loading spinner
        };
      },
    },
  ),
);
