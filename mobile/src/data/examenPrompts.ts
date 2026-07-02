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

// ── A word for the walk — scripture that feeds each quality ─────────────────
// This screen is the MEMBER track (opt-in, private), so all four standard works
// belong here — this is the deeper nourishment a Latter-day Saint expects, never
// shown on the seeker side of the app. Short, exact quotations; each reflection
// session opens with one so the examen is fed by the word, not just questions.
export interface QualityVerse {
  ref:  string;   // e.g. 'Mosiah 18:9'
  text: string;   // short exact quotation
}

export const QUALITY_VERSES: Record<TraitKey, QualityVerse[]> = {
  honest_inquiry: [
    { ref: 'John 8:32',    text: 'And ye shall know the truth, and the truth shall make you free.' },
    { ref: 'Psalm 51:6',   text: 'Behold, thou desirest truth in the inward parts.' },
    { ref: 'D&C 93:24',    text: 'Truth is knowledge of things as they are, and as they were, and as they are to come.' },
  ],
  humility: [
    { ref: 'Ether 12:27',  text: 'If men come unto me I will show unto them their weakness… my grace is sufficient for all men that humble themselves before me.' },
    { ref: 'Mosiah 3:19',  text: 'Becometh as a child, submissive, meek, humble, patient, full of love.' },
    { ref: 'Matthew 11:29', text: 'Learn of me; for I am meek and lowly in heart: and ye shall find rest unto your souls.' },
  ],
  compassion: [
    { ref: 'Mosiah 18:9',  text: 'Willing to mourn with those that mourn; yea, and comfort those that stand in need of comfort.' },
    { ref: 'Matthew 25:40', text: 'Inasmuch as ye have done it unto one of the least of these my brethren, ye have done it unto me.' },
    { ref: 'John 13:34',   text: 'A new commandment I give unto you, That ye love one another; as I have loved you.' },
  ],
  courage: [
    { ref: '1 Nephi 3:7',  text: 'I will go and do the things which the Lord hath commanded.' },
    { ref: 'Joshua 1:9',   text: 'Be strong and of a good courage… for the Lord thy God is with thee whithersoever thou goest.' },
    { ref: '2 Timothy 1:7', text: 'For God hath not given us the spirit of fear; but of power, and of love, and of a sound mind.' },
  ],
  hunger: [
    { ref: '2 Nephi 32:3', text: 'Feast upon the words of Christ; for behold, the words of Christ will tell you all things what ye should do.' },
    { ref: 'Matthew 5:6',  text: 'Blessed are they which do hunger and thirst after righteousness: for they shall be filled.' },
    { ref: 'John 6:35',    text: 'I am the bread of life: he that cometh to me shall never hunger.' },
  ],
  openness: [
    { ref: 'D&C 88:63',    text: 'Draw near unto me and I will draw near unto you; seek me diligently and ye shall find me.' },
    { ref: 'Revelation 3:20', text: 'Behold, I stand at the door, and knock: if any man hear my voice, and open the door, I will come in to him.' },
    { ref: '1 Samuel 3:9', text: 'Speak, Lord; for thy servant heareth.' },
  ],
  sincerity: [
    { ref: 'Moroni 10:4',  text: 'Ask with a sincere heart, with real intent, having faith in Christ.' },
    { ref: 'Alma 34:27',   text: 'Let your hearts be full, drawn out in prayer unto him continually.' },
    { ref: 'Matthew 22:37', text: 'Thou shalt love the Lord thy God with all thy heart, and with all thy soul, and with all thy mind.' },
  ],
};

// Pick the verse of the day for a quality — stable within a day (it is "today's
// word", not a slot machine), rotating gently day by day.
export function verseFor(key: TraitKey): QualityVerse {
  const pool = QUALITY_VERSES[key] ?? [];
  if (pool.length === 0) {
    return { ref: 'Psalm 46:10', text: 'Be still, and know that I am God.' };
  }
  const dayIndex = Math.floor(Date.now() / 86_400_000);
  return pool[dayIndex % pool.length];
}
