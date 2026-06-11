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

// ── Constants ───────────────────────────────────────────────────────────────

export const VIEW_CAP = 5;

export const FEED_PROGRESSION: FeedTag[] = [
  'MILK',
  'BRIDGE',
  'RESTORATION',
  'MAINTENANCE',
];

const GRADUATION_THRESHOLD = 4;

// Signals that indicate readiness for restored-gospel / missionary contact.
// Until at least one of these is present, the missionary referral link is hidden.
const RESTORATION_READY_SIGNALS = new Set([
  'open_to_restoration',
  'curious_about_book_of_mormon',
  'believes_in_jesus',
  'drawn_to_jesus',
  'covenant_intent',
  'inactive_member',
]);

export function isRestorationReady(signals: string[]): boolean {
  return signals.some(s => RESTORATION_READY_SIGNALS.has(s));
}

// Hidden signal → feed tag mapping.
// These come from onboard story choice keys (A/B/C/D per story) and free text.
// The user never sees these labels — routing is entirely invisible.
const SIGNAL_TO_TAG: Record<string, FeedTag> = {
  carries_burden:       'MILK',
  searching_for_purpose:'MILK',
  carries_shame:        'MILK',
  carries_grief:        'MILK',
  has_history_with_faith:'MILK',
  skeptical_of_god:     'BRIDGE',
  analytical_doubt:     'BRIDGE',
  open_to_god:          'BRIDGE',
  covenant_intent:      'MAINTENANCE',
};

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

function advanceFeedTag(current: FeedTag): FeedTag {
  const idx = FEED_PROGRESSION.indexOf(current);
  return idx < FEED_PROGRESSION.length - 1 ? FEED_PROGRESSION[idx + 1] : current;
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

// ── Server URL ───────────────────────────────────────────────────────────────
// In dev this points at the local server.
// In production set EXPO_PUBLIC_SERVER_URL to your Railway/Render URL.
const SERVER_URL =
  (process.env.EXPO_PUBLIC_SERVER_URL ?? '').trim() || 'http://localhost:3000';

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
}

interface AppActions {
  // choice = story choice key (A/B/C/D/E), feedTag = direct override from story choice
  completeOnboarding:  (choice: string, freeText?: string, feedTag?: FeedTag) => void;
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

      completeOnboarding(choice, freeText, feedTag) {
        // feedTag comes directly from the story choice object — it's already correct.
        // For free text (E), infer from what the person wrote.
        const tag: FeedTag =
          feedTag ??
          (choice === 'E' && freeText ? inferTagFromText(freeText) : 'MILK');

        const feed            = buildFeed(tag, new Set());
        const currentQuestion = computeNextQuestion([], [], 0);

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
          dialogueSignals:     [],
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
        const { positiveCount, feedTag, seenIds } = get();
        const newCount = positiveCount + 1;
        let newTag     = feedTag;

        if (newCount >= GRADUATION_THRESHOLD) {
          newTag = advanceFeedTag(feedTag);
        }

        const feed = buildFeed(newTag, seenIds);
        set({ positiveCount: newCount, feedTag: newTag, feed });
      },

      bookmark(id) {
        get().thumbsUp(id);
      },

      keepSimple() {
        const feed = buildFeed('MILK', get().seenIds);
        set({
          feedTag:          'MILK',
          feed,
          positiveCount:    0,
          isTimeCapReached: false,
        });
      },

      goDeeper() {
        const { feedTag, seenIds } = get();
        const newTag = advanceFeedTag(feedTag);
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

        const systemPrompt = `You are a gentle, honest spiritual companion on a faith-exploration app called Milk Before Meat. You follow the method of Jesus — meeting people where they are, paying attention, asking questions more than you make statements.

About this person:
- Content level: ${state.feedTag}
- Spiritual traits: ${traitSummary}${signalSentences ? `\n- What we know about them: ${signalSentences}` : ''}${recentJournal ? `\n- From their recent journal: ${recentJournal}` : ''}

Your role:
- Respond warmly but not saccharine. Two to four sentences is usually right. Leave room for them.
- Ask one follow-up question. Let them talk more than you do.
- Lead with Jesus and what he actually said — not with institution or doctrine.
- Do not mention The Church of Jesus Christ of Latter-day Saints unless they ask directly.
- Do not mention the Book of Mormon unless their signals clearly show they are ready for it.
- If they ask whether you are AI, be honest: yes. Tell them there are real people they can submit questions to anonymously.
- If a question feels beyond your confidence — historical, doctrinal, theological detail — say so honestly. Then offer: "I can submit your question and my answer anonymously to a real person who can verify or correct it. Would you like that?"
- If the conversation involves grief, crisis, or serious pain, gently acknowledge it and offer the anonymous question option.
- Never argue. If someone has a belief you think is incomplete, respond with a story or what Jesus said, not a counterargument.

The app is Milk Before Meat: a gospel outreach platform built on the principle that Jesus met people where they were before he asked anything of them.`;

        const history = state.chatMessages.map(m => ({
          role:    m.role,
          content: m.text,
        }));

        try {
          // ── Route through MBM server proxy (API key stays server-side) ────
          const response = await fetch(`${SERVER_URL}/api/chat`, {
            method:  'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              conversation_id: state.conversationId,
              user_id:         state.conversationId,
              user_message:    text,
              history,
              system_prompt:   systemPrompt,
              feed_tag:        state.feedTag,
              trait_scores:    state.traitScores,
              signals:         state.dialogueSignals,
            }),
          });

          if (!response.ok) {
            throw new Error(`Server error ${response.status}`);
          }

          const data  = await response.json();
          const reply = data?.reply ?? '';

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
