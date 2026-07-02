// MBM key proxy + delivery server (Phase 1) — HARDENED 2026-07-02
// Holds the Anthropic key SERVER-SIDE so it never ships in the app bundle,
// delivers connect requests to the owner, and receives fact-check submissions.
// Deploy: Railway (server/railway.json).
//
// env:
//   ANTHROPIC_API_KEY  (required) — the key; never leaves this server
//   ADMIN_TOKEN        (required) — protects the owner inbox
//   MBM_APP_TOKEN      (optional) — shared token future app builds send as x-mbm-app
//   REQUIRE_APP_TOKEN  (optional) — set to "1" ONLY after all live builds send the
//                                   token; until then unknown clients are allowed
//                                   so the build already in Apple review keeps working
//   CHAT_PER_MIN       (optional) — per-IP chat requests/minute   (default 10)
//   CHAT_PER_DAY       (optional) — per-IP chat requests/day      (default 300)
//   CHAT_GLOBAL_DAY    (optional) — TOTAL chat requests/day, all users combined —
//                                   the wallet fuse (default 5000)
//   PORT               (optional)
//
// What the hardening stops:
//   1. Strangers using the Anthropic key as their free AI (rate limits + global
//      daily fuse + size caps + app token once enforced).
//   2. Spam-flooding the connect/fact-check inbox (rate limits + queue caps).
//   3. Oversized requests running up token costs (system/message size caps).

const express = require('express');
const fs = require('fs');
const path = require('path');

const app = express();
app.set('trust proxy', 1); // Railway sits in front; use the real client IP
app.use(express.json({ limit: '256kb' }));
app.use((req, res, next) => { // CORS for the Expo app / web preview
  res.set('Access-Control-Allow-Origin', '*');
  res.set('Access-Control-Allow-Headers', 'content-type, x-admin-token, x-mbm-app');
  if (req.method === 'OPTIONS') return res.sendStatus(204);
  next();
});

const KEY = (process.env.ANTHROPIC_API_KEY || '').trim();
const ADMIN_TOKEN = (process.env.ADMIN_TOKEN || '').trim();
const APP_TOKEN = (process.env.MBM_APP_TOKEN || '').trim();
const REQUIRE_APP_TOKEN = (process.env.REQUIRE_APP_TOKEN || '').trim() === '1';
const CHAT_PER_MIN = Math.max(1, parseInt(process.env.CHAT_PER_MIN || '10', 10) || 10);
const CHAT_PER_DAY = Math.max(1, parseInt(process.env.CHAT_PER_DAY || '300', 10) || 300);
const CHAT_GLOBAL_DAY = Math.max(1, parseInt(process.env.CHAT_GLOBAL_DAY || '5000', 10) || 5000);

const DB = path.join(__dirname, 'queue.json');
const QUEUE_CAP = 500; // per list; oldest unhandled items beyond this are dropped
const readQ = () => { try { return JSON.parse(fs.readFileSync(DB, 'utf8')); } catch { return { connects: [], factchecks: [] }; } };
const writeQ = (q) => {
  q.connects = (q.connects || []).slice(0, QUEUE_CAP);
  q.factchecks = (q.factchecks || []).slice(0, QUEUE_CAP);
  fs.writeFileSync(DB, JSON.stringify(q, null, 2));
};

// ── Rate limiting (in-memory sliding windows; resets on redeploy, which is fine
//    for abuse protection — an attacker cannot force a redeploy) ───────────────
// Railway's edge sets x-forwarded-for to the real client; req.ip behind the
// hop proved unreliable (each request could count under a different bucket),
// so take the first x-forwarded-for entry, falling back to req.ip.
const clientIp = (req) =>
  ((req.get('x-forwarded-for') || '').split(',')[0].trim()) || req.ip || 'unknown';

const minuteHits = new Map(); // ip -> [timestamps within last 60s]
const dayHits = new Map();    // ip -> { day: 'YYYY-MM-DD', n }
let globalDay = { day: '', n: 0 };
const today = () => new Date().toISOString().slice(0, 10);

function prune() { // keep the maps from growing unbounded
  const cutoff = Date.now() - 60_000;
  for (const [ip, arr] of minuteHits) {
    const kept = arr.filter((t) => t > cutoff);
    if (kept.length === 0) minuteHits.delete(ip); else minuteHits.set(ip, kept);
  }
  const d = today();
  for (const [ip, rec] of dayHits) if (rec.day !== d) dayHits.delete(ip);
}
setInterval(prune, 5 * 60_000).unref();

// Returns null if allowed, or an HTTP status to reject with.
function rateLimit(ip, perMin, perDay, countGlobal) {
  const now = Date.now();
  const d = today();

  if (countGlobal) {
    if (globalDay.day !== d) globalDay = { day: d, n: 0 };
    if (globalDay.n >= CHAT_GLOBAL_DAY) return 503; // wallet fuse blown for today
  }

  const m = (minuteHits.get(ip) || []).filter((t) => t > now - 60_000);
  if (m.length >= perMin) return 429;

  let rec = dayHits.get(ip);
  if (!rec || rec.day !== d) rec = { day: d, n: 0 };
  if (rec.n >= perDay) return 429;

  m.push(now); minuteHits.set(ip, m);
  rec.n += 1; dayHits.set(ip, rec);
  if (countGlobal) globalDay.n += 1;
  return null;
}

// App-token check. Enforcement is OFF until REQUIRE_APP_TOKEN=1 so builds that
// predate the token (including the one in Apple review) keep working.
function appTokenOk(req) {
  if (!REQUIRE_APP_TOKEN) return true;
  if (!APP_TOKEN) return true; // never lock everyone out by misconfiguration
  return req.get('x-mbm-app') === APP_TOKEN;
}

// ── Chat proxy: the app sends {system, messages}; the key never leaves here ──
const MAX_MESSAGES = 40;        // one conversation, not a bulk pipeline
const MAX_MSG_CHARS = 8_000;    // any single message
const MAX_TOTAL_CHARS = 60_000; // whole conversation
const MAX_SYSTEM_CHARS = 24_000;

app.post('/api/chat', async (req, res) => {
  if (!KEY) return res.status(503).json({ error: 'no_key_configured' });
  if (!appTokenOk(req)) return res.status(401).json({ error: 'unauthorized' });
  const rl = rateLimit(clientIp(req), CHAT_PER_MIN, CHAT_PER_DAY, true);
  if (rl) return res.status(rl).json({ error: rl === 429 ? 'rate_limited' : 'daily_capacity_reached' });

  const { system, messages, max_tokens } = req.body || {};
  if (!Array.isArray(messages) || messages.length === 0 || messages.length > MAX_MESSAGES) {
    return res.status(400).json({ error: 'bad_request' });
  }
  let total = 0;
  for (const m of messages) {
    if (!m || (m.role !== 'user' && m.role !== 'assistant') || typeof m.content !== 'string') {
      return res.status(400).json({ error: 'bad_request' });
    }
    if (m.content.length > MAX_MSG_CHARS) return res.status(400).json({ error: 'message_too_long' });
    total += m.content.length;
  }
  if (total > MAX_TOTAL_CHARS) return res.status(400).json({ error: 'conversation_too_long' });
  const sys = String(system || '');
  if (sys.length > MAX_SYSTEM_CHARS) return res.status(400).json({ error: 'system_too_long' });

  try {
    const r = await fetch('https://api.anthropic.com/v1/messages', {
      method: 'POST',
      headers: { 'content-type': 'application/json', 'x-api-key': KEY, 'anthropic-version': '2023-06-01' },
      body: JSON.stringify({
        model: 'claude-haiku-4-5-20251001', // model is locked server-side; clients cannot pick a pricier one
        max_tokens: Math.min(max_tokens || 512, 1024),
        system: sys,
        messages: messages.map((m) => ({ role: m.role, content: m.content })),
      }),
    });
    if (!r.ok) return res.status(502).json({ error: 'upstream_' + r.status });
    const data = await r.json();
    const text = (data.content || []).filter((b) => b.type === 'text').map((b) => b.text).join('').trim();
    res.json({ text });
  } catch (e) {
    res.status(502).json({ error: 'upstream_failed' });
  }
});

// ── Connect-request delivery: closes the "human one tap away" promise ───────
app.post('/api/connect', (req, res) => {
  if (!appTokenOk(req)) return res.status(401).json({ error: 'unauthorized' });
  const rl = rateLimit(clientIp(req), 5, 30, false);
  if (rl) return res.status(429).json({ error: 'rate_limited' });
  const { note, journeyStage, conversationId } = req.body || {};
  const q = readQ();
  q.connects.unshift({
    id: Date.now().toString(36),
    note: String(note || '').slice(0, 2000),
    journeyStage: String(journeyStage || '').slice(0, 100),
    conversationId: String(conversationId || '').slice(0, 100),
    at: new Date().toISOString(),
    handled: false,
  });
  writeQ(q);
  res.json({ ok: true });
});

// ── Anonymous fact-check submissions ─────────────────────────────────────────
app.post('/api/factcheck', (req, res) => {
  if (!appTokenOk(req)) return res.status(401).json({ error: 'unauthorized' });
  const rl = rateLimit(clientIp(req), 5, 30, false);
  if (rl) return res.status(429).json({ error: 'rate_limited' });
  const { question, ai_answer } = req.body || {};
  const q = readQ();
  q.factchecks.unshift({
    id: Date.now().toString(36),
    question: String(question || '').slice(0, 2000),
    ai_answer: String(ai_answer || '').slice(0, 4000),
    at: new Date().toISOString(),
    reviewed: false,
  });
  writeQ(q);
  res.json({ ok: true });
});

// ── Owner inbox (token-protected). Open in a browser to triage. ─────────────
app.get('/api/admin/queue', (req, res) => {
  if (!ADMIN_TOKEN || req.get('x-admin-token') !== ADMIN_TOKEN) return res.status(401).json({ error: 'unauthorized' });
  res.json(readQ());
});

app.get('/health', (_, res) => res.json({ ok: true, key: !!KEY }));
app.listen(process.env.PORT || 3000, () => console.log('MBM proxy up'));
