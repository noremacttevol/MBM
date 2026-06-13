/**
 * "Milk Before Meat" — the recurring, honest warning shown subtly every time the
 * app is opened.
 *
 * THE LABEL DOES DOUBLE DUTY. It is shown above every variant as "Milk Before
 * Meat" so that, over time, the label IS the title's meaning to the person:
 *   • MILK = what this app can give — teaching, practice, a place to exercise the
 *     spirit, a finger pointing toward the good.
 *   • MEAT = worshipping the living God Himself, which happens with Him and with
 *     real people, never inside an app.
 * Once a returning person recognizes the label, they know the point and don't have
 * to re-read the body — the label alone carries it.
 *
 * Many ways to say one thing. Each open shows a different variant so the same
 * truth can land through a different door. The first three are Cameron's
 * (Lantern, Garden, Echo); the rest extend them in the same spirit. All are
 * grounded in Elder Gerrit W. Gong's counsel that AI "can answer questions, but it
 * cannot answer prayers… it is not God and cannot be God."
 */

export const MILK_BEFORE_MEAT_LABEL = 'Milk Before Meat';

export const MILK_BEFORE_MEAT_NOTES: string[] = [
  // 1 — Lantern
  'This app is a lantern, not the Light. It is designed to help you exercise your ' +
    'spirit, study scripture, and focus your eyes on everything good. Let it help ' +
    'illuminate your path, but remember to give your prayers, your worship, and your ' +
    'heart only to your Father in Heaven.',

  // 2 — Garden
  'Consider this space a garden to tend your faith. It is a place to practice ' +
    'goodness, ask questions, and learn to walk as Jesus walked. But just as soil ' +
    'cannot hear your prayers, neither can this app. When you are ready to pray, ' +
    'close the screen and speak directly to God.',

  // 3 — Echo
  'This experience is an echo of scripture, not the voice of God. Use it to build ' +
    'your spiritual strength, learn of His love, and prepare your heart for the real ' +
    'world. Technology can teach, but only the Lord can transform. Practice here, ' +
    'but pray only to Him.',

  // 4 — Map
  'Treat this app as a map, not the homeland. It can show you the way, name the ' +
    'landmarks, and steady your steps — but it cannot walk the road for you and it ' +
    'is not the place you are going. Knowing and worshipping God is the destination; ' +
    'this only points. Take every step with Him.',

  // 5 — Mirror
  'Let this be a mirror to examine your heart, never the One who made it. It can ' +
    'help you see yourself honestly and turn toward the good, but it cannot forgive ' +
    'you, hear you, or love you the way Jesus does. Bring what you see here to Him.',

  // 6 — Rehearsal
  'Think of this as a rehearsal, not the performance. Here you practice faith, ' +
    'mercy, and listening — but the living of it happens off the screen, with God ' +
    'and with people who love you. An app can train the heart; only the Lord can ' +
    'fill it. Practice here; worship there.',

  // 7 — Cup of milk
  'What you find here is milk: nourishment to grow on, a place to be fed and to ' +
    'practice. The meat — knowing and worshipping God Himself — is not in a phone. ' +
    'This app is not God; it cannot answer a prayer or know you as Jesus does. Hold ' +
    'everything here up to Him before you believe it, and let the Spirit, not a ' +
    'screen, tell you what is true.',
];

// Pick a variant to show this open. Random so the same truth lands through a
// different door each time, until the person knows the point by the label alone.
export function pickMilkNote(): string {
  return MILK_BEFORE_MEAT_NOTES[Math.floor(Math.random() * MILK_BEFORE_MEAT_NOTES.length)];
}
