// Load .env manually so it works regardless of which directory node is invoked from
const fs = require('fs');
const envPath = require('path').join(__dirname, '.env');
if (fs.existsSync(envPath)) {
  fs.readFileSync(envPath, 'utf8').split('\n').forEach(line => {
    const eq = line.indexOf('=');
    if (eq > 0) {
      const k = line.slice(0, eq).trim();
      const v = line.slice(eq + 1).trim();
      if (k && !process.env[k]) process.env[k] = v;
    }
  });
}
const express  = require('express');
const cors     = require('cors');
const fetch    = require('node-fetch');
const Database = require('better-sqlite3');
const path     = require('path');
const crypto   = require('crypto');

const app  = express();
const PORT = process.env.PORT || 3000;
const ADMIN_PASSWORD = process.env.ADMIN_PASSWORD || 'mbm-admin-2024';
const ANTHROPIC_KEY  = process.env.ANTHROPIC_API_KEY || '';

// ── Database ─────────────────────────────────────────────────────────────────

const db = new Database(path.join(__dirname, 'conversations.db'));

db.exec(`
  CREATE TABLE IF NOT EXISTS conversations (
    id          TEXT PRIMARY KEY,
    user_id     TEXT NOT NULL,
    created_at  INTEGER NOT NULL,
    feed_tag    TEXT,
    trait_scores TEXT,
    signals     TEXT
  );

  CREATE TABLE IF NOT EXISTS messages (
    id              TEXT PRIMARY KEY,
    conversation_id TEXT NOT NULL,
    role            TEXT NOT NULL,
    content         TEXT NOT NULL,
    created_at      INTEGER NOT NULL,
    status          TEXT DEFAULT 'sent',
    edited_content  TEXT,
    FOREIGN KEY (conversation_id) REFERENCES conversations(id)
  );

  CREATE TABLE IF NOT EXISTS pending_responses (
    id              TEXT PRIMARY KEY,
    conversation_id TEXT NOT NULL,
    user_message_id TEXT NOT NULL,
    suggested_reply TEXT NOT NULL,
    created_at      INTEGER NOT NULL,
    status          TEXT DEFAULT 'pending',
    final_reply     TEXT,
    reviewed_at     INTEGER,
    FOREIGN KEY (conversation_id) REFERENCES conversations(id)
  );

  CREATE TABLE IF NOT EXISTS fact_checks (
    id           TEXT PRIMARY KEY,
    question     TEXT NOT NULL,
    ai_answer    TEXT NOT NULL,
    created_at   INTEGER NOT NULL,
    status       TEXT DEFAULT 'pending',
    correction   TEXT,
    reviewed_at  INTEGER
  );
`);

// ── Prepared statements ───────────────────────────────────────────────────────

const insertConv = db.prepare(`
  INSERT OR IGNORE INTO conversations (id, user_id, created_at, feed_tag, trait_scores, signals)
  VALUES (@id, @user_id, @created_at, @feed_tag, @trait_scores, @signals)
`);

const upsertConv = db.prepare(`
  INSERT INTO conversations (id, user_id, created_at, feed_tag, trait_scores, signals)
  VALUES (@id, @user_id, @created_at, @feed_tag, @trait_scores, @signals)
  ON CONFLICT(id) DO UPDATE SET
    feed_tag     = excluded.feed_tag,
    trait_scores = excluded.trait_scores,
    signals      = excluded.signals
`);

const insertMsg = db.prepare(`
  INSERT OR IGNORE INTO messages (id, conversation_id, role, content, created_at, status)
  VALUES (@id, @conversation_id, @role, @content, @created_at, @status)
`);

const insertPending = db.prepare(`
  INSERT INTO pending_responses (id, conversation_id, user_message_id, suggested_reply, created_at, status)
  VALUES (@id, @conversation_id, @user_message_id, @suggested_reply, @created_at, 'pending')
`);

// ── Middleware ────────────────────────────────────────────────────────────────

app.use(cors());
app.use(express.json({ limit: '2mb' }));
app.use(express.static(path.join(__dirname, 'public')));

// Simple session store for admin auth
const adminSessions = new Set();

function requireAdmin(req, res, next) {
  const token = req.headers['x-admin-token'] || req.query.token;
  if (token && adminSessions.has(token)) return next();
  res.status(401).json({ error: 'Unauthorized' });
}

// ── API: Fact-check submission (anonymous, from in-app AI) ────────────────────
// When the AI is uncertain, it offers to submit the Q&A anonymously for Cameron
// to fact-check or correct. No user identity is stored.

app.post('/api/factcheck', (req, res) => {
  const { question, ai_answer } = req.body;
  if (!question || !ai_answer) {
    return res.status(400).json({ error: 'question and ai_answer required' });
  }
  const id = crypto.randomUUID();
  db.prepare(`
    INSERT INTO fact_checks (id, question, ai_answer, created_at, status)
    VALUES (?, ?, ?, ?, 'pending')
  `).run(id, question.slice(0, 2000), ai_answer.slice(0, 4000), Date.now());

  res.json({ ok: true, id });
});

// ── API: Admin — get fact checks ──────────────────────────────────────────────

app.get('/api/admin/factchecks', requireAdmin, (req, res) => {
  const rows = db.prepare(
    'SELECT * FROM fact_checks ORDER BY created_at DESC LIMIT 100'
  ).all();
  res.json(rows);
});

app.post('/api/admin/factchecks/:id/review', requireAdmin, (req, res) => {
  const { correction } = req.body;
  db.prepare(`
    UPDATE fact_checks SET status='reviewed', correction=?, reviewed_at=? WHERE id=?
  `).run(correction || '', Date.now(), req.params.id);
  res.json({ ok: true });
});

// ── API: Admin login ──────────────────────────────────────────────────────────

app.post('/api/admin/login', (req, res) => {
  const { password } = req.body;
  if (password === ADMIN_PASSWORD) {
    const token = crypto.randomBytes(32).toString('hex');
    adminSessions.add(token);
    res.json({ token });
  } else {
    res.status(401).json({ error: 'Wrong password' });
  }
});

// ── API: Chat proxy ───────────────────────────────────────────────────────────
// The mobile app posts here instead of calling Anthropic directly.
// This keeps the API key server-side and lets us store every message.

app.post('/api/chat', async (req, res) => {
  const {
    conversation_id,
    user_id,
    user_message,
    history,
    system_prompt,
    feed_tag,
    trait_scores,
    signals,
  } = req.body;

  if (!conversation_id || !user_message) {
    return res.status(400).json({ error: 'conversation_id and user_message required' });
  }

  const now = Date.now();

  // Upsert conversation record
  upsertConv.run({
    id:          conversation_id,
    user_id:     user_id || 'anonymous',
    created_at:  now,
    feed_tag:    feed_tag || 'MILK',
    trait_scores: JSON.stringify(trait_scores || {}),
    signals:     JSON.stringify(signals || []),
  });

  // Store user message
  const userMsgId = crypto.randomUUID();
  insertMsg.run({
    id:              userMsgId,
    conversation_id,
    role:            'user',
    content:         user_message,
    created_at:      now,
    status:          'sent',
  });

  // Call Anthropic
  try {
    const messages = [
      ...(history || []),
      { role: 'user', content: user_message },
    ];

    const response = await fetch('https://api.anthropic.com/v1/messages', {
      method:  'POST',
      headers: {
        'Content-Type':      'application/json',
        'x-api-key':         ANTHROPIC_KEY,
        'anthropic-version': '2023-06-01',
      },
      body: JSON.stringify({
        model:      'claude-haiku-4-5-20251001',
        max_tokens: 800,
        system:     system_prompt || '',
        messages,
      }),
    });

    if (!response.ok) {
      const err = await response.text();
      throw new Error(`Anthropic ${response.status}: ${err}`);
    }

    const data  = await response.json();
    const reply = data?.content?.[0]?.text || '';

    // Store AI reply
    const aiMsgId = crypto.randomUUID();
    insertMsg.run({
      id:              aiMsgId,
      conversation_id,
      role:            'assistant',
      content:         reply,
      created_at:      Date.now(),
      status:          'sent',
    });

    // Also log as a pending review so Cameron sees it in admin
    insertPending.run({
      id:              crypto.randomUUID(),
      conversation_id,
      user_message_id: userMsgId,
      suggested_reply: reply,
      created_at:      Date.now(),
    });

    res.json({ reply, message_id: aiMsgId, conversation_id });

  } catch (err) {
    console.error('Chat error:', err.message);
    res.status(500).json({ error: err.message });
  }
});

// ── API: Admin — list conversations ──────────────────────────────────────────

app.get('/api/admin/conversations', requireAdmin, (req, res) => {
  const convs = db.prepare(`
    SELECT
      c.*,
      COUNT(m.id)                          AS message_count,
      MAX(m.created_at)                    AS last_activity,
      SUM(CASE WHEN m.role='user' THEN 1 ELSE 0 END) AS user_messages
    FROM conversations c
    LEFT JOIN messages m ON m.conversation_id = c.id
    GROUP BY c.id
    ORDER BY last_activity DESC
  `).all();

  res.json(convs.map(c => ({
    ...c,
    trait_scores: JSON.parse(c.trait_scores || '{}'),
    signals:      JSON.parse(c.signals      || '[]'),
  })));
});

// ── API: Admin — get one conversation ─────────────────────────────────────────

app.get('/api/admin/conversations/:id', requireAdmin, (req, res) => {
  const conv = db.prepare('SELECT * FROM conversations WHERE id = ?').get(req.params.id);
  if (!conv) return res.status(404).json({ error: 'Not found' });

  const messages = db.prepare(
    'SELECT * FROM messages WHERE conversation_id = ? ORDER BY created_at ASC'
  ).all(req.params.id);

  const pending = db.prepare(
    "SELECT * FROM pending_responses WHERE conversation_id = ? AND status = 'pending' ORDER BY created_at DESC"
  ).all(req.params.id);

  res.json({
    ...conv,
    trait_scores: JSON.parse(conv.trait_scores || '{}'),
    signals:      JSON.parse(conv.signals      || '[]'),
    messages,
    pending,
  });
});

// ── API: Admin — approve/edit pending response ────────────────────────────────

app.post('/api/admin/pending/:id/approve', requireAdmin, (req, res) => {
  const { edited_reply } = req.body;
  const pending = db.prepare('SELECT * FROM pending_responses WHERE id = ?').get(req.params.id);
  if (!pending) return res.status(404).json({ error: 'Not found' });

  const finalReply = (edited_reply || '').trim() || pending.suggested_reply;

  db.prepare(`
    UPDATE pending_responses
    SET status = 'approved', final_reply = ?, reviewed_at = ?
    WHERE id = ?
  `).run(finalReply, Date.now(), req.params.id);

  res.json({ ok: true, final_reply: finalReply });
});

// ── API: Admin — stats ────────────────────────────────────────────────────────

app.get('/api/admin/stats', requireAdmin, (req, res) => {
  const stats = {
    total_conversations: db.prepare('SELECT COUNT(*) as n FROM conversations').get().n,
    total_messages:      db.prepare('SELECT COUNT(*) as n FROM messages').get().n,
    pending_reviews:     db.prepare("SELECT COUNT(*) as n FROM pending_responses WHERE status='pending'").get().n,
    pending_factchecks:  db.prepare("SELECT COUNT(*) as n FROM fact_checks WHERE status='pending'").get().n,
    users_today:         db.prepare(
      'SELECT COUNT(DISTINCT user_id) as n FROM conversations WHERE created_at > ?'
    ).get(Date.now() - 86400000).n,
  };
  res.json(stats);
});

// ── Serve admin dashboard for all /admin routes ───────────────────────────────

app.get('/admin*', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'admin.html'));
});

// ── Start ─────────────────────────────────────────────────────────────────────

app.listen(PORT, () => {
  console.log(`MBM server running on port ${PORT}`);
  console.log(`Admin dashboard: http://localhost:${PORT}/admin`);
});
