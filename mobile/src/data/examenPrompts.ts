// examenPrompts.ts — gentle daily reflection prompts for the members-only
// "My Discipleship" companion. Modeled on the Ignatian examen: not a quiz or a
// score, just an invitation to notice where Christ was at work in the real
// moments of the day. Each prompt is tied to one of the seven Christlike
// qualities the app already tracks privately, but here the QUALITIES are only a
// way to vary the reflection — the member never sees a number, only the question.
//
// Tone law (Cameron, June 2026): grace-first, inspiring, never guilt-inducing.
// Celebrate effort and repentance. These are companions for a faithful member's
// walk — never a report card.

import { TraitKey } from './questionBank';

export interface QualityMeta {
  key:         TraitKey;
  label:       string;   // warm, member-facing name (NOT the "Christlike X" capped label)
  blurb:       string;   // one line on what this looks like, grace-first
}

// The seven, in the order they read most naturally for a disciple.
export const QUALITIES: QualityMeta[] = [
  { key: 'honest_inquiry', label: 'Honesty',           blurb: 'Telling the truth — to God, to others, and to yourself.' },
  { key: 'humility',       label: 'Humility',          blurb: 'Holding your certainties loosely; letting God be God.' },
  { key: 'compassion',     label: 'Compassion',        blurb: 'Seeing people the way Christ sees them, and acting on it.' },
  { key: 'courage',        label: 'Courage',           blurb: 'Doing the right, hard thing in His strength.' },
  { key: 'hunger',         label: 'Hunger for Truth',  blurb: 'Reaching for more of God than you had yesterday.' },
  { key: 'openness',       label: 'Openness',          blurb: 'Staying soft to the Spirit, even when it would be easier to close.' },
  { key: 'sincerity',      label: 'Sincerity',         blurb: 'Meaning what you say to God; a whole heart, not a performance.' },
];

export const QUALITY_BY_KEY: Record<TraitKey, QualityMeta> =
  QUALITIES.reduce((acc, q) => { acc[q.key] = q; return acc; }, {} as Record<TraitKey, QualityMeta>);

// Several prompts per quality. The screen rotates through them and lets the
// member tap for a new one. Phrasing is reflective and kind — it asks them to
// NOTICE grace, not to grade themselves.
export const EXAMEN_PROMPTS: Record<TraitKey, string[]> = {
  honest_inquiry: [
    'Where today did you have a chance to be honest — with God, someone else, or yourself? How did it go?',
    'Was there a moment you were tempted to shade the truth? What happened, and what would Christ have done?',
    'What is one true thing you have been avoiding saying — to God or to someone you love?',
  ],
  humility: [
    'Where did you let God be God today, instead of needing to be right or in control?',
    'Was there a moment pride got the better of you? You can bring it here honestly — no shame.',
    'Who did you learn something from today that you might once have overlooked?',
  ],
  compassion: [
    'Who needed kindness from you today? How did you respond — and how do you feel about it now?',
    'Where did you see someone the way Christ sees them? Where did you miss it?',
    'Whose burden could you help carry tomorrow, even in a small way?',
  ],
  courage: [
    'What small brave thing did you do today — or wish you had?',
    'Where did fear hold you back, and what might trusting God look like there?',
    'What is one hard-but-right step Christ might be inviting you toward?',
  ],
  hunger: [
    'Where did you reach for more of God today — in scripture, prayer, or a quiet turning of your heart?',
    'What stirred your longing for Him lately? Sit with it a moment.',
    'What part of the gospel are you most hungry to understand more deeply right now?',
  ],
  openness: [
    'Where did you stay soft to the Spirit today, even when closing off would have been easier?',
    'Was there a nudge you felt and set aside? What was it?',
    'What is God gently inviting you to reconsider or open your hands around?',
  ],
  sincerity: [
    'Where was your heart whole with God today — not performing, just real?',
    'Was there a place your words and your heart drifted apart? Bring it here honestly.',
    'What would it look like to pray tonight with nothing held back?',
  ],
};

// Pick a prompt for a quality, avoiding an immediate repeat where possible.
export function promptFor(key: TraitKey, avoid?: string): string {
  const pool = EXAMEN_PROMPTS[key] ?? [];
  if (pool.length === 0) return 'Where did you notice God at work in your day?';
  const fresh = pool.filter(p => p !== avoid);
  const from = fresh.length ? fresh : pool;
  return from[Math.floor(Math.random() * from.length)];
}
