// exercises.ts — spiritual exercises: invite → try → report → learn.
// Jesus gave people things to DO. The follow-up is where the engine learns.
// Port of the prototype's verified implementation.

export interface SpiritualExercise {
  id: string;
  requires: string[];   // signals that select this exercise (empty = universal floor)
  text: string;
  ref: string;
  followUp: string;
}

export const EXERCISES: SpiritualExercise[] = [
  {
    id: 'quiet_honesty',
    requires: [],
    text: "Tonight, when it's quiet, say what is actually on your mind — out loud or just in your head — as if someone who already knows everything about you is listening anyway. Don't perform. Just say the true thing once.",
    ref: 'Matthew 6:6 — Pray to your Father who is in secret.',
    followUp: 'You said you might try saying the true thing into the quiet. Did you get a chance — and did anything come back?',
  },
  {
    id: 'notice_alive',
    requires: ['carries_burden', 'carries_grief', 'lonely', 'pictures_distant_god'],
    text: "Once today, stop for one full minute and watch something alive — a bird, a tree in the wind, anything that is kept alive without trying. While you watch, ask yourself one question: if something keeps that alive, is it really nothing that I'm still here too?",
    ref: 'Matthew 6:26 — Look at the birds of the air.',
    followUp: 'You were going to stop and watch something alive for a minute. What did you notice?',
  },
  {
    id: 'read_mark1',
    requires: ['drawn_to_jesus', 'open_to_scripture', 'searching_for_purpose', 'honest_inquiry'],
    text: 'Read just the first chapter of Mark — ten minutes, no commitment. Watch what Jesus actually does in a single day. Notice the one moment that surprises you.',
    ref: 'Mark 1 — the first day of his ministry.',
    followUp: 'You were going to read the first chapter of Mark. Did anything in it surprise you?',
  },
  {
    id: 'small_forgive',
    requires: ['carries_shame', 'hurt_by_church', 'carries_grief', 'pictures_harsh_god'],
    text: "Pick the smallest debt someone owes you — an unanswered text, a slight, a chore left undone — and quietly cancel it. Just that one. Tell no one. Notice what it costs you, and what it hands back.",
    ref: 'Matthew 18 — the unpayable debt, forgiven first.',
    followUp: 'You were going to quietly cancel one small debt. Did you manage it — and what did it cost or hand back?',
  },
  {
    id: 'ask_direct',
    requires: ['open_to_restoration'],
    text: "You've wondered whether God might still speak. So ask him something — a real question you actually carry, said plainly, tonight. Then pay attention for three days: to what you read, what you feel, what shows up. Not proof. Just attention.",
    ref: 'Matthew 7:7 — Ask, and it will be given to you.',
    followUp: 'You asked God a real question and said you would pay attention. Has anything shown up — in what you read, felt, or noticed?',
  },
];

// Most specific match wins; the universal one is the floor.
export function pickExercise(signals: string[], doneIds: string[]): SpiritualExercise | null {
  const sset = new Set(signals);
  const eligible = EXERCISES.filter((e) => !doneIds.includes(e.id));
  const matched = eligible.filter((e) => e.requires.length > 0 && e.requires.some((r) => sset.has(r)));
  if (matched.length > 0) return matched[matched.length - 1];
  return eligible.find((e) => e.requires.length === 0) || null;
}
