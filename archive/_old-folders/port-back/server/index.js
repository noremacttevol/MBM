// MBM key proxy + delivery server (Phase 1)
// Holds the Anthropic key SERVER-SIDE so it never ships in the app bundle,
// delivers connect requests to the owner, and receives fact-check submissions.
// Deploy: Railway/Render/Fly (server/railway.json already exists in the repo).
//   env: ANTHROPIC_API_KEY (required), ADMIN_TOKEN (required), PORT (optional)

const express = require('express');
const fs = require('fs');
const path = require('path');

const app = express();
app.use(express.json({ limit: '1mb' }));
app.use((req, res, next) => { // CORS for the Expo app / web preview
  res.set('Access-Control-Allow-Origin', '*');
  res.set('Access-Control-Allow-Headers', 'content-type, x-admin-token');
  if (req.method === 'OPTIONS') return res.sendStatus(204);
  next();
});

const KEY = (process.env.ANTHROPIC_API_KEY || '').trim();
const ADMIN_TOKEN = (process.env.ADMIN_TOKEN || '').trim();
const DB = path.join(__dirname, 'queue.json');
const readQ = () => { try { return JSON.parse(fs.readFileSync(DB, 'utf8')); } catch { return { connects: [], factchecks: [] }; } };
const writeQ = (q) => fs.writeFileSync(DB, JSON.stringify(q, null, 2));

// ── Chat proxy: the app sends {system, messages}; the key never leaves here ──
app.post('/api/chat', async (req, res) => {
  if (!KEY) return res.status(503).json({ error: 'no_key_configured' });
  const { system, messages, max_tokens } = req.body || {};
  if (!Array.isArray(messages) || messages.length === 0) return res.status(400).json({ error: 'bad_request' });
  try {
    const r = await fetch('https://api.anthropic.com/v1/messages', {
      method: 'POST',
      headers: { 'content-type': 'application/json', 'x-api-key': KEY, 'anthropic-version': '2023-06-01' },
      body: JSON.stringify({
        model: 'claude-haiku-4-5-20251001',
        max_tokens: Math.min(max_tokens || 512, 1024),
        system: String(system || ''),
        messages,
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
  const { note, journeyStage, conversationId } = req.body || {};
  const q = readQ();
  q.connects.unshift({ id: Date.now().toString(36), note: String(note || '').slice(0, 2000), journeyStage, conversationId, at: new Date().toISOString(), handled: false });
  writeQ(q);
  res.json({ ok: true });
});

// ── Anonymous fact-check submissions ─────────────────────────────────────────
app.post('/api/factcheck', (req, res) => {
  const { question, ai_answer } = req.body || {};
  const q = readQ();
  q.factchecks.unshift({ id: Date.now().toString(36), question: String(question || '').slice(0, 2000), ai_answer: String(ai_answer || '').slice(0, 4000), at: new Date().toISOString(), reviewed: false });
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
