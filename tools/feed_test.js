// MBM feed + link test. Run from MBM root: node tools/feed_test.js
// Proves Cameron's standard: scrolling the feed never repeats an item until ALL
// have been seen, the milk/meat counts are exact, and every link is well-formed.
// The pool/buildFeed/refreshFeed logic below MIRRORS src/store/useAppStore.ts.
const fs = require('fs');
const path = require('path');

const CONTENT = JSON.parse(fs.readFileSync(path.join(__dirname, 'content.data.json'), 'utf8'));

let failures = 0;
const ok   = (m) => console.log('  PASS  ' + m);
const fail = (m) => { console.log('  FAIL  ' + m); failures++; };
const check = (cond, m) => cond ? ok(m) : fail(m);

// ── engine mirror ───────────────────────────────────────────────────────────
function shuffle(arr) {
  const a = [...arr];
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}
function poolForTag(tag) {
  const milk = CONTENT.filter(c => c.track === 'MILK');
  const meat = CONTENT.filter(c => c.track === 'MEAT');
  const meatReady = tag === 'MAINTENANCE' || tag === 'RESTORATION';
  if (milk.length === 0 && meat.length === 0) return CONTENT.filter(c => c.tag === tag);
  return meatReady ? [...milk, ...meat] : milk;
}
function buildFeed(tag, seen) {
  const pool = poolForTag(tag);
  const unseen = pool.filter(c => !seen.has(c.id));
  const source = unseen.length > 0 ? unseen : pool;
  return shuffle(source).slice(0, 5);
}

// ── 1. counts ───────────────────────────────────────────────────────────────
const milk = CONTENT.filter(c => c.track === 'MILK');
const meat = CONTENT.filter(c => c.track === 'MEAT');
const common = milk.filter(c => c.milkTrack === 'common');
const restoration = milk.filter(c => c.milkTrack === 'restoration');
console.log('\nCounts');
check(common.length === 50, `milk "common" = 50 (got ${common.length})`);
check(restoration.length === 50, `milk "restoration" = 50 (got ${restoration.length})`);
check(milk.length === 100, `milk total = 100 (got ${milk.length})`);
// Meat is authored next; this asserts the standard once it lands.
check(meat.length === 0 || meat.length === 100, `meat = 0 (pending) or 100 (got ${meat.length})`);

// ── 2. unique ids, titles, valid links ──────────────────────────────────────
console.log('\nIntegrity');
check(new Set(CONTENT.map(c => c.id)).size === CONTENT.length, 'all ids unique');
check(new Set(CONTENT.map(c => c.title)).size === CONTENT.length, 'all titles unique');
let badLinks = 0;
for (const c of CONTENT) {
  const bibleOk = /^https:\/\/www\.biblegateway\.com\/passage\/\?search=.+&version=KJV$/.test(c.url);
  const ldsOk   = /^https:\/\/www\.churchofjesuschrist\.org\/study\/scriptures\/.+\/\d+$/.test(c.url);
  if (!(bibleOk || ldsOk)) { badLinks++; if (badLinks <= 5) console.log('      bad url: ' + c.title + ' -> ' + c.url); }
}
check(badLinks === 0, `every link well-formed (${badLinks} bad)`);
check(restoration.every(c => c.ldsLens && c.ldsLens.length > 10), 'every restoration item has an ldsLens hint');

// ── 3. NO-REPEAT until exhausted — Cameron's scroll test ─────────────────────
// Simulate: open the feed (page 1), then tap "Show me more" until the pool is
// exhausted. Every item must be brand-new until all have been seen exactly once.
function simulate(tag, label) {
  const pool = poolForTag(tag);
  const total = pool.length;
  let seen = new Set();
  let feed = buildFeed(tag, seen);
  feed.forEach(c => seen.add(c.id));          // page 1 shown
  const shownOrder = [...feed.map(c => c.id)];
  let pages = 1;
  const pagesNeeded = Math.ceil(total / 5);
  while (seen.size < total && pages < pagesNeeded + 2) {
    // refreshFeed(): current page folded into seen, then next page drawn
    feed = buildFeed(tag, seen);
    feed.forEach(c => { shownOrder.push(c.id); seen.add(c.id); });
    pages++;
  }
  const firstCycle = shownOrder.slice(0, total);
  const distinct = new Set(firstCycle).size;
  console.log(`\nNo-repeat cycle — ${label} (${total} items, ${pagesNeeded} pages of 5)`);
  check(distinct === total, `first ${total} shown are all distinct — no repeat until all seen (got ${distinct} distinct)`);
  check(pages <= pagesNeeded + 1, `pool exhausted in ~${pagesNeeded} scrolls (took ${pages})`);
  // After exhaustion, a fresh cycle is allowed to repeat.
  const next = buildFeed(tag, seen);
  check(next.length === 5, 'a fresh cycle begins after all seen (feed not empty)');
}
simulate('MILK', 'seeker feed');
if (meat.length === 100) simulate('MAINTENANCE', 'meat-ready feed');
else console.log('\n(meat-ready 200-item cycle test will run once the 100 meat items are authored)');

console.log(`\n${failures === 0 ? 'ALL CHECKS PASSED' : failures + ' CHECK(S) FAILED'}`);
process.exit(failures === 0 ? 0 : 1);
