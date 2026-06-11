import { FeedTag } from './content';

export interface JournalPrompt {
  id:        string;
  text:      string;
  tag:       FeedTag | 'ANY';
  signal?:   string;     // only show if this signal is active
}

// Prompts are selected based on active signals first, then feed tag, then ANY.
// They rotate so the user sees a fresh one each session.

export const JOURNAL_PROMPTS: JournalPrompt[] = [

  // ── Signal-specific — shown only when the signal is active ──────────────

  {
    id: 'grief_1',
    text: "What do you wish you could say to them now — knowing they would hear it completely?",
    tag: 'ANY',
    signal: 'carries_grief',
  },
  {
    id: 'grief_2',
    text: "What part of that loss are you still carrying that you haven't let yourself name out loud?",
    tag: 'ANY',
    signal: 'carries_grief',
  },
  {
    id: 'purpose_1',
    text: "If you woke up tomorrow and everything made sense — what would you do first?",
    tag: 'ANY',
    signal: 'searching_for_purpose',
  },
  {
    id: 'purpose_2',
    text: "What does a life that feels like yours actually look like — not what anyone else would call successful, just what would make you feel like you arrived?",
    tag: 'ANY',
    signal: 'searching_for_purpose',
  },
  {
    id: 'lonely_1',
    text: "What would it feel like to be fully known — not just liked — by someone who still chose to stay?",
    tag: 'ANY',
    signal: 'lonely',
  },
  {
    id: 'habit_1',
    text: "What do you think you're actually reaching for when you go back to the thing you said you'd stop?",
    tag: 'ANY',
    signal: 'struggles_with_habits',
  },
  {
    id: 'history_1',
    text: "When you think back on your faith history — what do you miss, and what are you glad to have left behind?",
    tag: 'ANY',
    signal: 'has_history_with_faith',
  },
  {
    id: 'skeptic_1',
    text: "What's the one thing about God, if it turned out to be true, that would change everything for you?",
    tag: 'ANY',
    signal: 'skeptical_of_god',
  },
  {
    id: 'restoration_1',
    text: "If the original church Jesus established was actually restored — what's the first question you'd want answered?",
    tag: 'ANY',
    signal: 'open_to_restoration',
  },
  {
    id: 'jesus_1',
    text: "Of everything Jesus taught — what's the one thing you find hardest to argue with, even if you're not sure what to do with it?",
    tag: 'ANY',
    signal: 'drawn_to_jesus',
  },
  {
    id: 'prayer_1',
    text: "If you were going to say something to God right now — just between you and him — what would it be?",
    tag: 'ANY',
    signal: 'prayed_before',
  },
  {
    id: 'inactive_1',
    text: "What would it take for the faith you grew up in to feel like a home again, instead of a place you left?",
    tag: 'ANY',
    signal: 'inactive_member',
  },

  // ── Feed-tag specific ────────────────────────────────────────────────────

  {
    id: 'milk_1',
    text: "When did you last feel genuinely at peace — not because things were good, but because something deeper was okay?",
    tag: 'MILK',
  },
  {
    id: 'milk_2',
    text: "What's one thing in your life right now that feels like it might actually be grace — even if you wouldn't call it that?",
    tag: 'MILK',
  },
  {
    id: 'milk_3',
    text: "Is there someone in your life who loves you the way you want to be loved — and what does that feel like?",
    tag: 'MILK',
  },
  {
    id: 'milk_4',
    text: "What's something you've been carrying alone that you haven't told anyone?",
    tag: 'MILK',
  },
  {
    id: 'bridge_1',
    text: "What's the question about God or faith that you keep coming back to — the one that won't leave you alone?",
    tag: 'BRIDGE',
  },
  {
    id: 'bridge_2',
    text: "Is there a version of God you could believe in — and what would that God have to be like?",
    tag: 'BRIDGE',
  },
  {
    id: 'bridge_3',
    text: "What would have to be true — provably, undeniably true — for you to take faith seriously as more than a coping mechanism?",
    tag: 'BRIDGE',
  },
  {
    id: 'restoration_2',
    text: "If God still speaks today through living prophets — what do you think he'd say to the world right now?",
    tag: 'RESTORATION',
  },
  {
    id: 'restoration_3',
    text: "What would it mean for you personally if the Book of Mormon was exactly what it claims to be?",
    tag: 'RESTORATION',
  },
  {
    id: 'maintenance_1',
    text: "Where has your discipleship felt most alive recently — and where has it felt most like going through the motions?",
    tag: 'MAINTENANCE',
  },
  {
    id: 'maintenance_2',
    text: "What's a covenant you've made that has actually changed how you live — and one that hasn't yet?",
    tag: 'MAINTENANCE',
  },
  {
    id: 'maintenance_3',
    text: "Who in your ward or community do you sense needs something right now — and what's stopping you from reaching out?",
    tag: 'MAINTENANCE',
  },

  // ── Universal ────────────────────────────────────────────────────────────

  {
    id: 'any_1',
    text: "What's one thing you believe today that you didn't believe a year ago — and what changed it?",
    tag: 'ANY',
  },
  {
    id: 'any_2',
    text: "When you imagine the best version of your life — what's present in it that isn't present now?",
    tag: 'ANY',
  },
  {
    id: 'any_3',
    text: "What do you most want to be remembered for — and is the way you're living pointing toward that?",
    tag: 'ANY',
  },
  {
    id: 'any_4',
    text: "Is there a moment in your past you'd go back and do differently — and what does that tell you about who you're becoming?",
    tag: 'ANY',
  },
  {
    id: 'any_5',
    text: "What's one thing you're grateful for today that you almost missed noticing?",
    tag: 'ANY',
  },
];

export function getCurrentPrompt(
  feedTag:         FeedTag,
  activeSignals:   string[],
  answeredPrompts: string[],
): JournalPrompt {
  const signalSet = new Set(activeSignals);

  // Signal-specific prompts first (highest relevance)
  const signalMatches = JOURNAL_PROMPTS.filter(
    p => p.signal && signalSet.has(p.signal) && !answeredPrompts.includes(p.id),
  );
  if (signalMatches.length > 0) return signalMatches[0];

  // Feed-tag prompts next
  const tagMatches = JOURNAL_PROMPTS.filter(
    p => !p.signal && p.tag === feedTag && !answeredPrompts.includes(p.id),
  );
  if (tagMatches.length > 0) return tagMatches[0];

  // Universal prompts fallback
  const anyMatches = JOURNAL_PROMPTS.filter(
    p => !p.signal && p.tag === 'ANY' && !answeredPrompts.includes(p.id),
  );
  if (anyMatches.length > 0) return anyMatches[0];

  // If all answered, cycle back to tag prompts
  return JOURNAL_PROMPTS.find(p => p.tag === feedTag || p.tag === 'ANY') ?? JOURNAL_PROMPTS[0];
}
