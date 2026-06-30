/**
 * MBM ministry console — the private desk for the "talk to a real person" threads.
 *
 * This is NOT part of the app. It runs only on your machine. It uses the Firebase
 * Admin SDK with a SERVICE ACCOUNT key, which bypasses the Firestore rules so an
 * approved helper can read every person's thread and reply to them. That key is the
 * one secret that must never ship in the app or go into git — it lives only here,
 * beside this file, as serviceAccount.json (which .gitignore keeps out of the repo).
 *
 * Run it:   cd admin && npm install && npm start
 * Then open http://localhost:4545 in your browser.
 *
 * What this desk is for: someone tapped "talk to a real person" and a real person
 * answers — gently, honestly, as themselves. Nothing here scores anyone or judges
 * anyone. It just helps a helper not lose track of who is waiting to be answered.
 *
 * Phase 1 (now): one helper — Cameron — handles everything. Every reply is stamped
 * with who sent it, and every thread carries a simple "needs reply / handled" state.
 * That stamping and triage is the only groundwork Phase 2 needs: when volunteers
 * join, set RESPONDER per login and the same attribution + handled state already
 * tell you who answered whom. No schema change, no rewrite. See RESPONDER-ROADMAP.md.
 *
 * The person's side of the app is untouched by this file. The extra fields written
 * here (responderId / responderName) are ignored by the app's reader; the threadMeta
 * collection is admin-only and is denied to every app client by the default-deny
 * Firestore rule. A person never sees any of this — only the warm reply itself.
 */

import { readFileSync, existsSync } from 'fs';
import http from 'http';
import crypto from 'crypto';
import { initializeApp, cert } from 'firebase-admin/app';
import { getFirestore, FieldValue } from 'firebase-admin/firestore';

const PORT = process.env.PORT || 4545;
const KEY_PATH = new URL('./serviceAccount.json', import.meta.url);

// ── Login (so the hosted desk isn't open to the world) ──────────────────────
// On a host (Railway etc.) set ADMIN_PASSWORD to a shared team password and
// SESSION_SECRET to any long random string. Then the desk shows a login page and
// only lets people in who know the password; each helper types their own NAME at
// login, which is what their replies get signed with. If ADMIN_PASSWORD is unset
// (i.e. running locally), the desk stays open with no login — exactly as before.
const ADMIN_PASSWORD  = (process.env.ADMIN_PASSWORD || '').trim();
const SESSION_SECRET  = (process.env.SESSION_SECRET || 'mbm-local-dev-secret').trim();
const AUTH_ON         = !!ADMIN_PASSWORD;

// The app's AI proxy is folded into this same service: the app posts {system,
// messages} to /api/chat and we add the Anthropic key here, so the key never
// ships inside the downloadable app. PUBLIC (no login) because the app calls it
// directly; every desk route below stays login-gated.
const ANTHROPIC_KEY   = (process.env.ANTHROPIC_API_KEY || '').trim();
const ANTHROPIC_MODEL = (process.env.ANTHROPIC_MODEL || 'claude-haiku-4-5-20251001').trim();

// ── Who is answering right now (Phase 1: just Cameron) ──────────────────────────
// Phase 2: replace this with the logged-in volunteer. Everything downstream — the
// reply stamp and the "handled by" record — already reads from here, so adding more
// helpers is a login change, not a rebuild.
const RESPONDER = { id: 'cameron', name: 'Cameron' };

// Every reply is SIGNED so the person knows a real, named human answered — and so
// a helper can choose to share personal contact info (email, phone) right in the
// reply. Set ADMIN_SIGNATURE in admin/.env to anything you like, e.g.:
//   ADMIN_SIGNATURE=Cameron · cameron@milkb4meat.org · text me anytime
// If unset, it defaults to just the responder's name. In the multi-admin app each
// approved helper will carry their own signature from their profile.
const ADMIN_SIGNATURE = (process.env.ADMIN_SIGNATURE || RESPONDER.name).trim();

// The Firebase service-account key. On a host it can't be a committed file, so we
// also accept it as a base64 env var (FIREBASE_SERVICE_ACCOUNT). Locally it's the
// gitignored admin/serviceAccount.json file — same as always.
let serviceAccount;
if (process.env.FIREBASE_SERVICE_ACCOUNT) {
  serviceAccount = JSON.parse(
    Buffer.from(process.env.FIREBASE_SERVICE_ACCOUNT, 'base64').toString('utf8'),
  );
} else if (existsSync(KEY_PATH)) {
  serviceAccount = JSON.parse(readFileSync(KEY_PATH, 'utf8'));
} else {
  console.error(
    '\n  Missing the Firebase service-account key.\n\n' +
    '  Local: save it as  admin/serviceAccount.json  (gitignored).\n' +
    '  Hosted: set the env var  FIREBASE_SERVICE_ACCOUNT  to the key file,\n' +
    '          base64-encoded (base64 -w0 serviceAccount.json).\n',
  );
  process.exit(1);
}
initializeApp({ credential: cert(serviceAccount) });
const db = getFirestore();
const COL = 'messages';
const META = 'threadMeta'; // admin-only; default-deny rule keeps every app client out

// A person can now hold MANY separate conversations. A thread is identified by the
// person (userId) AND which conversation (threadId). Messages written before
// multi-thread have no threadId and collapse into the 'main' conversation, so the
// original single thread keeps working untouched.
const LEGACY_THREAD = 'main';
const keyOf   = (uid, threadId) => `${uid}||${threadId || LEGACY_THREAD}`;
const parseKey = (key) => {
  const i = (key || '').indexOf('||');
  if (i < 0) return { uid: key || '', threadId: LEGACY_THREAD };
  return { uid: key.slice(0, i), threadId: key.slice(i + 2) || LEGACY_THREAD };
};

// ── Login session helpers ───────────────────────────────────────────────────
// A session is just the helper's name, signed with SESSION_SECRET so it can't be
// forged. Stored in a cookie. No database, no accounts to manage — the shared
// ADMIN_PASSWORD is the gate, the name is who's answering.
function b64url(s) { return Buffer.from(s, 'utf8').toString('base64url'); }
function unb64url(s) { try { return Buffer.from(s, 'base64url').toString('utf8'); } catch { return ''; } }
function signSession(name) {
  const payload = b64url(name);
  const sig = crypto.createHmac('sha256', SESSION_SECRET).update(payload).digest('hex');
  return `${payload}.${sig}`;
}
function verifySession(token) {
  if (!token || token.indexOf('.') < 0) return null;
  const [payload, sig] = token.split('.');
  const expect = crypto.createHmac('sha256', SESSION_SECRET).update(payload).digest('hex');
  if (sig !== expect) return null;
  const name = unb64url(payload).trim();
  return name || null;
}
function cookies(req) {
  const out = {};
  (req.headers.cookie || '').split(';').forEach(p => {
    const i = p.indexOf('=');
    if (i > 0) out[p.slice(0, i).trim()] = decodeURIComponent(p.slice(i + 1).trim());
  });
  return out;
}
// Who is answering this request: the logged-in helper, or — when no login is
// configured (local dev) — the default RESPONDER below.
function responderFor(req) {
  if (!AUTH_ON) return RESPONDER;
  const name = verifySession(cookies(req).mbm_session || '');
  if (!name) return null; // not logged in
  return { id: name.toLowerCase().replace(/[^a-z0-9]+/g, '-') || 'helper', name };
}

// ── Helpers ───────────────────────────────────────────────────────────────────

function isoOf(v) {
  try {
    if (v && typeof v.toDate === 'function') return v.toDate().toISOString();
  } catch {/* fall through */}
  return new Date().toISOString();
}

function isoOrNull(v) {
  try {
    if (v && typeof v.toDate === 'function') return v.toDate().toISOString();
  } catch {/* fall through */}
  return null;
}

function mapDoc(doc) {
  const d = doc.data();
  return {
    id:            doc.id,
    user_id:       d.userId ?? '',
    user_name:     d.userName ?? null,
    faith_note:    d.faithNote ?? null,
    thread_id:     d.threadId ?? LEGACY_THREAD,
    thread_title:  d.threadTitle ?? null,
    sender:        d.sender === 'admin' ? 'admin' : 'user',
    body:          d.body ?? '',
    excerpt:       d.excerpt ?? null,
    journey_stage: d.journeyStage ?? null,
    priority:      d.priority ?? null,
    responder_name: d.responderName ?? null,
    created_at:    isoOf(d.createdAt),
    read_by_admin: !!d.readByAdmin,
    read_by_user:  !!d.readByUser,
  };
}

async function allMessages() {
  const snap = await db.collection(COL).orderBy('createdAt', 'asc').get();
  return snap.docs.map(mapDoc);
}

// The per-thread triage record: { status, handledAt, handledByName, assignedToName }.
// Stored one doc per CONVERSATION (doc id = `${userId}||${threadId}`). Absent means
// "never triaged". Returns a Map keyed by that same composite key.
async function allMeta() {
  const snap = await db.collection(META).get();
  const byKey = new Map();
  snap.docs.forEach(d => {
    const m = d.data();
    byKey.set(d.id, {
      status:           m.status ?? null,
      handled_at:       isoOrNull(m.handledAt),
      handled_by_name:  m.handledByName ?? null,
      assigned_to_name: m.assignedToName ?? null,
    });
  });
  return byKey;
}

// A thread "needs reply" when the newest message is from the person AND it arrived
// after the last time a helper marked it handled. It is "handled" when a helper has
// caught up past the newest person-message. It is "waiting on them" when the helper
// already answered last. This is derived live, so it can never drift out of sync.
function deriveStatus(messages, meta) {
  if (!messages.length) return 'needs_reply';
  const last = messages[messages.length - 1];
  if (last.sender === 'admin') return 'answered'; // helper spoke last
  const lastUserAt = last.created_at;
  const handledAt = meta?.handled_at ?? null;
  if (handledAt && handledAt >= lastUserAt) return 'handled';
  return 'needs_reply';
}

const STATUS_LABEL = {
  needs_reply: 'Needs reply',
  answered:    'Answered',
  handled:     'Handled',
};

// A short, scannable title for a conversation — the stamped thread title if present,
// else the first thing the person said in it, so legacy threads read well too.
function titleOf(messages) {
  const titled = messages.find(m => m.thread_title)?.thread_title;
  if (titled) return titled;
  const firstUser = messages.find(m => m.sender === 'user' && (m.body || '').trim());
  const raw = (firstUser?.body || messages[0]?.body || 'Conversation').replace(/\s+/g, ' ').trim();
  return raw.length > 52 ? raw.slice(0, 52).trim() + '…' : (raw || 'Conversation');
}

// A short, human description of where a person is — enough for a disciple to know
// who they're about to talk to, without exposing the internal routing label raw.
const STAGE_DESC = {
  UNREACHED:              'New here — just looking',
  CURIOUS:                'Curious, starting to ask questions',
  BELIEVES_GOD_GOOD:      'Believes God is good',
  OPEN_TO_RESTORATION:    'Open to there being more',
  SEEKING_TRUTH:          'Actively seeking the truth',
  READY_FOR_MISSIONARIES: 'Ready to meet missionaries',
  BAPTISM:                'Heading toward baptism',
  DISCIPLE_GROWING:       'A member, growing in the gospel',
};

// What to call a person in the list: their name if given, else a stable short ID
// from their device so each anonymous person is still distinguishable.
function personLabel(name, uid) {
  if (name && name.trim()) return name.trim();
  return 'Guest ' + String(uid || '').slice(0, 4).toUpperCase();
}

// A one-line description: humanized stage if we have it, else their own faith note,
// else a gentle default. Never the raw internal code.
function personDesc(stage, faith) {
  if (stage && STAGE_DESC[stage]) return STAGE_DESC[stage];
  if (faith && faith.trim()) return faith.trim();
  return 'Reached out for a real person';
}

// Delete every conversation and its triage record — a full clean slate for testing.
// Batched (Firestore caps a batch at 500 writes). Returns the total docs removed.
async function resetAll() {
  let removed = 0;
  for (const name of [COL, META]) {
    const snap = await db.collection(name).get();
    let batch = db.batch();
    let n = 0;
    for (const d of snap.docs) {
      batch.delete(d.ref);
      n++; removed++;
      if (n === 450) { await batch.commit(); batch = db.batch(); n = 0; }
    }
    if (n > 0) await batch.commit();
  }
  return removed;
}

// Group every message into one thread per CONVERSATION (person + threadId), those
// needing a reply first. Each row carries a composite `key` the rest of the desk
// uses to open, reply, and triage exactly that conversation.
async function listThreads() {
  const msgs = await allMessages();
  const meta = await allMeta();
  const byKey = new Map();
  for (const m of msgs) {
    const key = keyOf(m.user_id, m.thread_id);
    if (!byKey.has(key)) {
      byKey.set(key, { key, uid: m.user_id, threadId: m.thread_id, name: null, faith: null, messages: [], unread: 0, stage: null, crisis: false, cancelled: false });
    }
    const t = byKey.get(key);
    t.messages.push(m);
    // Remember the person's name and self-reported faith note if they've given one
    // (latest wins), so the console can label the conversation, show their own-words
    // faith background beside their name, and greet them properly.
    if (m.sender === 'user' && m.user_name) t.name = m.user_name;
    if (m.sender === 'user' && m.faith_note) t.faith = m.faith_note;
    if (m.sender === 'user' && !m.read_by_admin) t.unread += 1;
    if (m.sender === 'user' && m.journey_stage) t.stage = m.journey_stage;
    // A single crisis-flagged message marks the whole conversation for first triage.
    if (m.sender === 'user' && m.priority === 'crisis') t.crisis = true;
    // The person withdrew this request — they no longer want a reply.
    if (m.sender === 'user' && m.priority === 'cancelled') t.cancelled = true;
  }
  const threads = [...byKey.values()].map(t => {
    const last = t.messages[t.messages.length - 1];
    const tMeta = meta.get(t.key) ?? null;
    const status = deriveStatus(t.messages, tMeta);
    return {
      key:              t.key,
      uid:              t.uid,
      thread_id:        t.threadId,
      person_name:      t.name ?? null,
      person_faith:     t.faith ?? null,
      label:            personLabel(t.name, t.uid),
      desc:             personDesc(t.stage, t.faith),
      title:            titleOf(t.messages),
      unread:           t.unread,
      stage:            t.stage,
      crisis:           t.crisis,
      cancelled:        t.cancelled,
      count:            t.messages.length,
      status,
      status_label:     STATUS_LABEL[status] ?? status,
      handled_by_name:  tMeta?.handled_by_name ?? null,
      last: last ? { body: last.body, sender: last.sender, created_at: last.created_at } : null,
    };
  });
  // Crisis-flagged conversations rise above everything; then needs-reply; within
  // each group, newest activity first.
  const rank = s => (s === 'needs_reply' ? 0 : s === 'answered' ? 1 : 2);
  threads.sort((a, b) => {
    // Cancelled requests sink to the bottom (nothing to act on); crisis rises to top.
    if (a.cancelled !== b.cancelled) return a.cancelled ? 1 : -1;
    if (a.crisis !== b.crisis) return a.crisis ? -1 : 1;
    const r = rank(a.status) - rank(b.status);
    if (r !== 0) return r;
    return (b.last?.created_at ?? '').localeCompare(a.last?.created_at ?? '');
  });
  return threads;
}

// ── Thread-list cache (protects the Firestore read quota) ────────────────────
// Every /api/threads call used to read the ENTIRE messages collection. The desk
// polls on a timer and may be open in several tabs, so an idle inbox could burn
// through a free-tier day of reads in hours. This serves a recent result instead
// of re-reading the database on every poll: the DB is hit at most once per TTL,
// no matter how many polls or tabs ask. Any write (reply/handle/markread/reset)
// clears it immediately so the admin always sees their own action right away.
const THREADS_TTL_MS = 15000; // serve a cached list for up to 15s
let _threadsCache = { at: 0, data: null };
function invalidateThreadsCache() { _threadsCache = { at: 0, data: null }; }
async function listThreadsCached() {
  const now = Date.now();
  if (_threadsCache.data && (now - _threadsCache.at) < THREADS_TTL_MS) {
    return _threadsCache.data;
  }
  const data = await listThreads();
  _threadsCache = { at: now, data };
  return data;
}

async function getThread(key) {
  const { uid, threadId } = parseKey(key);
  // ONE equality query on userId only (single-field, already indexed), then sort
  // and filter to this conversation in JS. We must NOT add .orderBy('createdAt')
  // here: userId + createdAt needs a composite index that isn't created, and if
  // it's missing the query throws and the thread comes back EMPTY (the bug where
  // clicking a conversation showed a blank screen). Sorting in code avoids it.
  const snap = await db.collection(COL)
    .where('userId', '==', uid)
    .get();
  const messages = snap.docs
    .map(mapDoc)
    .filter(m => m.thread_id === threadId)
    .sort((a, b) => +new Date(a.created_at) - +new Date(b.created_at));
  const metaSnap = await db.collection(META).doc(key).get();
  const m = metaSnap.exists ? metaSnap.data() : null;
  const meta = m
    ? {
        status:           m.status ?? null,
        handled_at:       isoOrNull(m.handledAt),
        handled_by_name:  m.handledByName ?? null,
        assigned_to_name: m.assignedToName ?? null,
      }
    : null;
  const userMsgs = messages.filter(x => x.sender === 'user');
  const pName  = [...userMsgs].reverse().find(x => x.user_name)?.user_name ?? null;
  const pFaith = [...userMsgs].reverse().find(x => x.faith_note)?.faith_note ?? null;
  const pStage = [...messages].reverse().find(x => x.sender === 'user' && x.journey_stage)?.journey_stage ?? null;
  return {
    messages,
    title: titleOf(messages),
    person_name:  pName,
    person_faith: pFaith,
    label:        personLabel(pName, uid),
    desc:         personDesc(pStage, pFaith),
    stage: pStage,
    status: deriveStatus(messages, meta),
    handled_by_name: meta?.handled_by_name ?? null,
  };
}

async function reply(key, body, responder = RESPONDER) {
  const clean = (body ?? '').trim();
  const { uid, threadId } = parseKey(key);
  if (!uid || !clean) return false;
  // Each helper signs with their own name (or a custom ADMIN_SIGNATURE if set).
  const signature = (process.env.ADMIN_SIGNATURE || responder.name).trim();
  // The app reader (mobile/src/lib/messaging.ts) ignores responderId/responderName;
  // they exist only so this desk — now and with volunteers later — can show who
  // answered. The reply is stamped with the SAME threadId so it lands in exactly the
  // conversation the person asked in. Nothing about the person's experience changes.
  // Sign the reply so the person sees who answered (and any contact info the
  // helper chose to share). The signature is appended to the message text itself,
  // so it shows in the app regardless of how the bubble is labeled.
  const signed = `${clean}\n\n— ${signature}`;
  await db.collection(COL).add({
    userId:        uid,
    threadId,
    threadTitle:   null,
    sender:        'admin',
    body:          signed,
    excerpt:       null,
    journeyStage:  null,
    responderId:   responder.id,
    responderName: responder.name,
    createdAt:     FieldValue.serverTimestamp(),
    readByAdmin:   true,
    readByUser:    false,
  });
  // Answering a person is itself catching up with them: record it as handled now.
  await db.collection(META).doc(key).set({
    status:        'handled',
    handledAt:     FieldValue.serverTimestamp(),
    handledById:   responder.id,
    handledByName: responder.name,
  }, { merge: true });
  return true;
}

// Mark a conversation handled without sending a message — for when a person's note
// needs no reply (a thank-you, a closing word) but you don't want it nagging the queue.
async function markHandled(key, responder = RESPONDER) {
  if (!key) return false;
  await db.collection(META).doc(key).set({
    status:        'handled',
    handledAt:     FieldValue.serverTimestamp(),
    handledById:   responder.id,
    handledByName: responder.name,
  }, { merge: true });
  return true;
}

async function markRead(key) {
  const { uid, threadId } = parseKey(key);
  const snap = await db.collection(COL)
    .where('userId', '==', uid)
    .where('sender', '==', 'user')
    .where('readByAdmin', '==', false)
    .get();
  // Only this conversation's messages (filtered on the client — no new index).
  const docs = snap.docs.filter(d => (d.data().threadId ?? LEGACY_THREAD) === threadId);
  const batch = db.batch();
  docs.forEach(d => batch.update(d.ref, { readByAdmin: true }));
  await batch.commit();
  return docs.length;
}

// ── HTTP server ─────────────────────────────────────────────────────────────

function json(res, code, data) {
  res.writeHead(code, { 'Content-Type': 'application/json' });
  res.end(JSON.stringify(data));
}

function readBody(req) {
  return new Promise(resolve => {
    let raw = '';
    req.on('data', c => { raw += c; });
    req.on('end', () => {
      try { resolve(JSON.parse(raw || '{}')); } catch { resolve({}); }
    });
  });
}

const server = http.createServer(async (req, res) => {
  const url = new URL(req.url, `http://localhost:${PORT}`);
  try {
    // ── AI proxy (PUBLIC — the app calls this; no login) ─────────────────────
    // Folded in from the old server/index.js so one service serves both the app's
    // AI and the desk. The Anthropic key stays here, never in the app.
    if (url.pathname === '/api/chat') {
      res.setHeader('Access-Control-Allow-Origin', '*');
      res.setHeader('Access-Control-Allow-Headers', 'content-type');
      if (req.method === 'OPTIONS') { res.writeHead(204); return res.end(); }
      if (req.method !== 'POST') return json(res, 405, { error: 'method' });
      if (!ANTHROPIC_KEY) return json(res, 503, { error: 'no_key_configured' });
      const { system, messages, max_tokens } = await readBody(req);
      if (!Array.isArray(messages) || messages.length === 0) {
        return json(res, 400, { error: 'bad_request' });
      }
      try {
        const r = await fetch('https://api.anthropic.com/v1/messages', {
          method: 'POST',
          headers: { 'content-type': 'application/json', 'x-api-key': ANTHROPIC_KEY, 'anthropic-version': '2023-06-01' },
          body: JSON.stringify({
            model: ANTHROPIC_MODEL,
            max_tokens: Math.min(max_tokens || 512, 1024),
            system: String(system || ''),
            messages,
          }),
        });
        if (!r.ok) return json(res, 502, { error: 'upstream_' + r.status });
        const data = await r.json();
        const text = (data.content || []).filter(b => b.type === 'text').map(b => b.text).join('').trim();
        return json(res, 200, { text });
      } catch {
        return json(res, 502, { error: 'upstream_failed' });
      }
    }

    // ── Login / logout (public) ──────────────────────────────────────────────
    if (req.method === 'POST' && url.pathname === '/api/login') {
      const { name, password } = await readBody(req);
      const cleanName = (name || '').trim();
      if (!AUTH_ON || !cleanName || password !== ADMIN_PASSWORD) {
        return json(res, 401, { ok: false, error: 'Wrong password (or no name).' });
      }
      const token = signSession(cleanName);
      res.writeHead(200, {
        'Content-Type': 'application/json',
        // Cookie: HttpOnly, 30 days, SameSite=Lax. Secure on a real https host.
        'Set-Cookie': `mbm_session=${encodeURIComponent(token)}; HttpOnly; Path=/; Max-Age=2592000; SameSite=Lax`,
      });
      return res.end(JSON.stringify({ ok: true, name: cleanName }));
    }
    if (req.method === 'POST' && url.pathname === '/api/logout') {
      res.writeHead(200, {
        'Content-Type': 'application/json',
        'Set-Cookie': 'mbm_session=; HttpOnly; Path=/; Max-Age=0; SameSite=Lax',
      });
      return res.end(JSON.stringify({ ok: true }));
    }

    // ── Auth gate ────────────────────────────────────────────────────────────
    const responder = responderFor(req); // null only when AUTH_ON and not logged in
    if (AUTH_ON && !responder) {
      if (req.method === 'GET' && (url.pathname === '/' || url.pathname === '/login')) {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        return res.end(LOGIN_PAGE);
      }
      return json(res, 401, { error: 'login required' });
    }

    // ── The desk ─────────────────────────────────────────────────────────────
    if (req.method === 'GET' && url.pathname === '/') {
      res.writeHead(200, { 'Content-Type': 'text/html' });
      res.end(PAGE);
      return;
    }
    if (req.method === 'GET' && url.pathname === '/api/me') {
      return json(res, 200, { name: responder.name, authOn: AUTH_ON });
    }
    if (req.method === 'GET' && url.pathname === '/api/threads') {
      return json(res, 200, await listThreadsCached());
    }
    if (req.method === 'GET' && url.pathname === '/api/thread') {
      const key = url.searchParams.get('key') ?? '';
      return json(res, 200, await getThread(key));
    }
    if (req.method === 'POST' && url.pathname === '/api/reply') {
      const { key, body } = await readBody(req);
      const ok = await reply(key, body, responder);
      invalidateThreadsCache(); // the admin just acted — show it on the next poll
      return json(res, ok ? 200 : 400, { ok });
    }
    if (req.method === 'POST' && url.pathname === '/api/handle') {
      const { key } = await readBody(req);
      const ok = await markHandled(key, responder);
      invalidateThreadsCache();
      return json(res, ok ? 200 : 400, { ok });
    }
    if (req.method === 'POST' && url.pathname === '/api/markread') {
      const { key } = await readBody(req);
      const n = await markRead(key);
      invalidateThreadsCache();
      return json(res, 200, { ok: true, marked: n });
    }
    // Wipe EVERYTHING for a clean test — every conversation and its triage record.
    // Triggered only by clicking "Reset everything" in the console (with a
    // confirmation), never automatically. Returns how many docs were removed.
    if (req.method === 'POST' && url.pathname === '/api/reset') {
      const removed = await resetAll();
      invalidateThreadsCache();
      return json(res, 200, { ok: true, removed });
    }
    json(res, 404, { error: 'not found' });
  } catch (e) {
    json(res, 500, { error: String(e?.message ?? e) });
  }
});

server.listen(PORT, () => {
  console.log(`\n  MBM ministry console running on port ${PORT}`);
  console.log(`  Login: ${AUTH_ON ? 'ON (password required)' : 'OFF (local, open)'}\n`);
});

// ── The login page (shown only when a password is configured) ───────────────
const LOGIN_PAGE = `<!doctype html>
<html lang="en"><head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>MBM — sign in</title>
<style>
  body{margin:0;background:#0a0a0f;color:#e8e6df;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
    display:flex;align-items:center;justify-content:center;min-height:100vh;}
  .box{width:320px;max-width:90vw;text-align:center;}
  h1{font-size:22px;font-weight:600;color:#d9b46a;margin:0 0 6px;}
  p{color:#9a958a;font-size:14px;margin:0 0 24px;line-height:1.6;}
  input{width:100%;box-sizing:border-box;background:#141418;border:1px solid #2a2820;border-radius:8px;
    color:#e8e6df;font-size:15px;padding:12px 14px;margin-bottom:12px;}
  button{width:100%;background:#7ab87a;color:#0a0f0a;border:none;border-radius:8px;font-size:15px;
    font-weight:600;padding:12px;cursor:pointer;}
  .err{color:#e5484d;font-size:13px;min-height:18px;margin-top:10px;}
</style></head><body>
  <div class="box">
    <h1>Ministry console</h1>
    <p>Sign in to read and answer the people who reached out.</p>
    <input id="name" placeholder="Your name (shown on your replies)" autocomplete="name" />
    <input id="pw" type="password" placeholder="Team password" autocomplete="current-password" />
    <button id="go">Sign in</button>
    <div class="err" id="err"></div>
  </div>
<script>
  async function login(){
    const name=document.getElementById('name').value.trim();
    const password=document.getElementById('pw').value;
    document.getElementById('err').textContent='';
    const r=await fetch('/api/login',{method:'POST',headers:{'Content-Type':'application/json'},
      body:JSON.stringify({name,password})});
    if(r.ok){ location.href='/'; } else {
      const d=await r.json().catch(()=>({}));
      document.getElementById('err').textContent=d.error||'Sign in failed.';
    }
  }
  document.getElementById('go').onclick=login;
  document.getElementById('pw').addEventListener('keydown',e=>{ if(e.key==='Enter') login(); });
</script>
</body></html>`;

// ── The page (dark, quiet, matches the app) ─────────────────────────────────

const PAGE = `<!doctype html>
<html lang="en"><head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>MBM — ministry console</title>
<style>
  :root{--bg:#0a0a0f;--card:#111116;--input:#141418;--border:#2a2820;--green:#7ab87a;
        --gold:#d4c89a;--text:#e8e4d8;--mid:#c8bfa8;--dim:#9a9080;--muted:#5a5240;
        --amber:#d8a85a;}
  *{box-sizing:border-box;font-family:Georgia,serif;}
  body{margin:0;background:var(--bg);color:var(--text);display:flex;height:100vh;}
  h1{font-size:15px;color:var(--mid);font-weight:normal;margin:0;letter-spacing:.5px;}
  #left{width:340px;border-right:1px solid var(--border);display:flex;flex-direction:column;}
  #head{padding:16px;border-bottom:1px solid var(--border);}
  #sub{font-size:11px;color:var(--muted);margin-top:4px;}
  #who-am-i{font-size:11px;color:var(--gold);margin-top:6px;}
  #tabs{display:flex;border-bottom:1px solid var(--border);}
  .tab{flex:1;text-align:center;padding:9px 0;font-size:12px;color:var(--dim);
       cursor:pointer;border-bottom:2px solid transparent;}
  .tab:hover{color:var(--mid);}
  .tab.on{color:var(--gold);border-bottom-color:var(--gold);}
  .tab .n{font-size:10px;color:var(--muted);}
  #threads{overflow-y:auto;flex:1;}
  .t{padding:14px 16px;border-bottom:1px solid var(--border);cursor:pointer;}
  .t:hover{background:#16161c;}
  .t.active{background:#16161c;border-left:2px solid var(--gold);}
  .t .who{font-size:12px;color:var(--dim);display:flex;justify-content:space-between;
          align-items:center;gap:8px;}
  .t .ttl{font-size:13px;color:var(--gold);margin-top:6px;overflow:hidden;
          text-overflow:ellipsis;white-space:nowrap;}
  .t .snip{font-size:12px;color:var(--dim);margin-top:3px;overflow:hidden;
           text-overflow:ellipsis;white-space:nowrap;}
  .dot{background:var(--green);color:#0a0f0a;border-radius:10px;font-size:11px;
       padding:1px 7px;}
  .stage{font-size:10px;color:var(--muted);text-transform:uppercase;letter-spacing:.5px;}
  .badge{font-size:10px;padding:2px 8px;border-radius:9px;letter-spacing:.3px;
         border:1px solid var(--border);white-space:nowrap;}
  .badge.needs_reply{color:#0a0f0a;background:var(--amber);border-color:var(--amber);}
  .badge.answered{color:var(--green);}
  .badge.handled{color:var(--muted);}
  .t.crisis{border-left:3px solid #e5484d;}
  .crisisbadge{font-size:10px;font-weight:700;color:#fff;background:#e5484d;
         padding:1px 6px;border-radius:8px;letter-spacing:.5px;}
  .t.cancelled{opacity:.55;}
  .cancelbadge{font-size:10px;font-weight:700;color:#0a0f0a;background:var(--muted);
         padding:1px 6px;border-radius:8px;letter-spacing:.5px;}
  #right{flex:1;display:flex;flex-direction:column;}
  #ctx{padding:12px 20px;border-bottom:1px solid var(--border);display:none;
       align-items:center;justify-content:space-between;gap:12px;}
  #ctx .meta{font-size:11px;color:var(--dim);}
  #ctx .meta b{color:var(--mid);font-weight:normal;}
  #conv{flex:1;overflow-y:auto;padding:20px;}
  .empty{color:var(--muted);font-size:14px;padding:40px;text-align:center;line-height:22px;}
  .msg{max-width:72%;margin-bottom:14px;}
  .msg.user{margin-right:auto;}
  .msg.admin{margin-left:auto;}
  .lbl{font-size:10px;color:var(--muted);margin-bottom:4px;}
  .msg.admin .lbl{text-align:right;color:var(--gold);}
  .bub{border:1px solid var(--border);border-radius:12px;padding:11px 13px;
       font-size:14px;line-height:21px;color:var(--mid);}
  .msg.user .bub{background:#0e1a12;border-color:#2a3a28;}
  .msg.admin .bub{background:#1a1812;border-color:var(--border);}
  .ex{font-size:12px;color:var(--dim);font-style:italic;border-left:2px solid var(--border);
      padding-left:8px;margin-bottom:6px;}
  .ghost{background:none;border:1px solid var(--border);color:var(--dim);border-radius:4px;
         padding:6px 12px;font-size:12px;cursor:pointer;}
  .ghost:hover{color:var(--mid);border-color:var(--muted);}
  #composer{border-top:1px solid var(--border);padding:14px;display:flex;gap:10px;}
  textarea{flex:1;background:var(--input);border:1px solid var(--border);border-radius:6px;
           color:var(--mid);font-size:14px;padding:10px;min-height:46px;resize:vertical;}
  button.send{background:var(--green);color:#0a0f0a;border:none;border-radius:4px;
         padding:0 18px;font-size:13px;font-weight:bold;cursor:pointer;}
  button.send:disabled{opacity:.5;cursor:default;}
</style></head>
<body>
  <div id="left">
    <div id="head"><h1>Ministry console</h1>
      <div id="sub">Every word here is a real person reaching out. Reply gently.</div>
      <div id="who-am-i"></div>
      <button id="resetAll" onclick="resetEverything()" title="Delete every conversation — for a clean test"
        style="margin-top:8px;font-size:11px;color:#e5484d;background:none;border:1px solid #e5484d;border-radius:4px;padding:4px 8px;cursor:pointer;">Reset everything</button>
    </div>
    <div id="tabs">
      <div class="tab on" data-filter="needs_reply" onclick="setFilter('needs_reply')">Needs reply <span class="n" id="n-needs"></span></div>
      <div class="tab" data-filter="all" onclick="setFilter('all')">All <span class="n" id="n-all"></span></div>
      <div class="tab" data-filter="handled" onclick="setFilter('handled')">Done <span class="n" id="n-done"></span></div>
    </div>
    <div id="threads"><div class="empty">Loading…</div></div>
  </div>
  <div id="right">
    <div id="ctx">
      <div class="meta" id="ctx-meta"></div>
      <button class="ghost" id="handle" onclick="markHandled()">Mark handled</button>
    </div>
    <div id="conv"><div class="empty">Pick someone on the left to read their thread.</div></div>
    <div id="composer" style="display:none">
      <textarea id="draft" placeholder="Write back as a real person…"></textarea>
      <button class="send" id="send">Send</button>
    </div>
  </div>
<script>
  let current = null;
  let filter = 'needs_reply';
  let lastList = [];
  const esc = s => (s||'').replace(/[&<>]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));
  const fmt = iso => { const d=new Date(iso); return isNaN(d)?'':d.toLocaleString(); };

  async function loadMe(){
    try {
      const r = await fetch('/api/me');
      if(r.status===401){ location.href='/login'; return; }
      const m = await r.json();
      const el = document.getElementById('who-am-i');
      el.textContent = 'Answering as ' + (m.name||'a helper') + '.';
      if(m.authOn){
        const out=document.createElement('a');
        out.textContent=' Sign out';
        out.href='#'; out.style.cssText='color:#9a958a;margin-left:8px;cursor:pointer;';
        out.onclick=async(e)=>{ e.preventDefault(); await fetch('/api/logout',{method:'POST'}); location.href='/login'; };
        el.appendChild(out);
      }
    } catch {/* fine offline */}
  }

  function setFilter(f){
    filter = f;
    document.querySelectorAll('.tab').forEach(t =>
      t.classList.toggle('on', t.dataset.filter === f));
    renderThreads(lastList);
  }

  function counts(list){
    const c = { needs_reply:0, all:list.length, handled:0 };
    list.forEach(t => { if(t.status==='needs_reply') c.needs_reply++;
      if(t.status==='handled'||t.status==='answered') c.handled++; });
    document.getElementById('n-needs').textContent = c.needs_reply ? '('+c.needs_reply+')' : '';
    document.getElementById('n-all').textContent   = c.all ? '('+c.all+')' : '';
    document.getElementById('n-done').textContent  = c.handled ? '('+c.handled+')' : '';
  }

  function renderThreads(list){
    if(!Array.isArray(list)) return;
    counts(list);
    const box = document.getElementById('threads');
    let view = list;
    if(filter==='needs_reply') view = list.filter(t => t.status==='needs_reply');
    else if(filter==='handled') view = list.filter(t => t.status==='handled' || t.status==='answered');
    if(!view.length){
      box.innerHTML = '<div class="empty">' +
        (filter==='needs_reply' ? 'No one is waiting on a reply right now.' :
         filter==='handled' ? 'Nothing answered yet.' :
         'No one has written in yet.') + '</div>';
      return;
    }
    // The list is intentionally just WHO + a short description — name (or a stable
    // Guest ID) and a one-line read on where they are. The actual messages are read
    // by opening the conversation, so the list stays scannable.
    box.innerHTML = view.map(t => \`
      <div class="t \${t.key===current?'active':''} \${t.crisis?'crisis':''} \${t.cancelled?'cancelled':''}" onclick="openThread('\${esc(t.key)}')">
        <div class="who">
          <span class="name">\${t.crisis?'<span class="crisisbadge">⚠ CRISIS</span> ':''}\${t.cancelled?'<span class="cancelbadge">CANCELLED</span> ':''}<b style="color:var(--gold)">\${esc(t.label||'Guest')}</b></span>
          <span style="display:flex;gap:6px;align-items:center;">
            \${t.unread?'<span class="dot">'+t.unread+'</span>':''}
            <span class="badge \${t.status}">\${esc(t.status_label||'')}</span>
          </span>
        </div>
        <div class="desc" style="font-size:12px;color:#79b8ff;margin-top:3px;">\${esc(t.desc||'')}</div>
      </div>\`).join('');
  }

  // ── New-message alerts (sound + desktop notification + tab badge) ──────────
  // The desk polls every 5s; when the total unread COUNT goes up, ping the admin
  // so they don't have to stare at this tab. Works whenever the desk is open in a
  // browser (even in a background tab). Cancelled requests don't count as new.
  let lastUnreadTotal = null;
  const BASE_TITLE = 'MBM — ministry console';
  function beep(){
    try {
      const AC = window.AudioContext || window.webkitAudioContext;
      const ctx = new AC();
      const o = ctx.createOscillator(), g = ctx.createGain();
      o.connect(g); g.connect(ctx.destination);
      o.type = 'sine'; o.frequency.value = 880;
      g.gain.setValueAtTime(0.001, ctx.currentTime);
      g.gain.exponentialRampToValueAtTime(0.25, ctx.currentTime + 0.02);
      g.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.5);
      o.start(); o.stop(ctx.currentTime + 0.5);
    } catch (e) { /* no audio available — the title badge + notification still fire */ }
  }
  function notifyNew(list){
    const total = list.reduce((n, t) => n + (t.cancelled ? 0 : (t.unread || 0)), 0);
    const anyCrisis = list.some(t => t.crisis && t.unread > 0);
    document.title = total > 0 ? '(' + total + ') ' + BASE_TITLE : BASE_TITLE;
    if (lastUnreadTotal !== null && total > lastUnreadTotal) {
      beep();
      try {
        if ('Notification' in window && Notification.permission === 'granted') {
          const n = new Notification(anyCrisis ? '⚠ Someone in crisis just wrote in' : 'New message for the admin team', {
            body: anyCrisis ? 'Open the console and reply right away.' : 'Someone is waiting for a real person. Open the console to reply.',
            requireInteraction: !!anyCrisis,
          });
          n.onclick = () => { window.focus(); };
        }
      } catch (e) { /* notifications unavailable — sound + title badge still work */ }
    }
    lastUnreadTotal = total;
  }

  async function loadThreads(){
    let data, status = 0;
    try {
      const r = await fetch('/api/threads');
      status = r.status;
      data = await r.json();
      if(!r.ok || !Array.isArray(data)){
        const msg = (data && data.error) ? String(data.error) : ('HTTP ' + status);
        showThreadsError(msg);
        return;
      }
    } catch(e) {
      showThreadsError(String(e && e.message ? e.message : e));
      return;
    }
    lastList = data;
    renderThreads(lastList);
    notifyNew(lastList);
  }

  // When the threads call fails, say WHY instead of hanging on "Loading…".
  // The most common cause is the Firestore free-tier daily read limit.
  function showThreadsError(msg){
    const quota = /quota|resource_exhausted/i.test(msg || '');
    const box = document.getElementById('threads');
    box.innerHTML = '<div class="empty" style="color:var(--amber);line-height:1.6;text-align:left;padding:14px">'
      + (quota
          ? '<b>The database hit its daily free-tier limit</b>, so threads cannot load right now.'
            + '<br><br>It resets at midnight Pacific. To stop this from recurring, raise the '
            + 'Firestore quota (upgrade the Firebase project to the Blaze plan) or slow the '
            + 'auto-refresh below 12 reads/min.'
          : ('<b>Could not load threads.</b><br><br>' + esc(msg)))
      + '</div>';
  }

  async function openThread(key){
    // Is this the SAME thread being re-rendered by the 15s auto-refresh, or a brand
    // new one the reader just clicked? On a refresh we must NOT force the pane to the
    // bottom — that was the bug where scrolling up to read the top snapped you back
    // down every 15 seconds.
    const isSameThread = (key === current);
    current = key;
    const r = await fetch('/api/thread?key='+encodeURIComponent(key));
    const data = await r.json();
    const msgs = data.messages || [];

    const ctx = document.getElementById('ctx');
    const nameTxt = data.label ? '<b style="color:var(--gold)">' + esc(data.label) + '</b>  ·  ' : '';
    const descTxt = data.desc ? '<span style="color:#79b8ff">' + esc(data.desc) + '</span>  ·  ' : '';
    const faithTxt = (data.person_faith && data.person_faith !== data.desc) ? '<span style="color:#79b8ff;font-style:italic">“' + esc(data.person_faith) + '”</span>  ·  ' : '';
    const titleTxt = data.title ? '<b>' + esc(data.title) + '</b>  ·  ' : '';
    const stageTxt = data.stage ? '<b>Where they are:</b> ' + esc(data.stage) + '  ·  ' : '';
    const statusTxt = data.status==='needs_reply' ? 'Waiting on a reply'
      : data.status==='handled' ? ('Handled' + (data.handled_by_name ? ' by ' + esc(data.handled_by_name) : ''))
      : 'You answered last';
    document.getElementById('ctx-meta').innerHTML = nameTxt + descTxt + faithTxt + titleTxt + stageTxt + statusTxt;
    ctx.style.display = 'flex';

    const conv = document.getElementById('conv');
    // Remember where the reader was BEFORE we rebuild the messages. If they were
    // already near the bottom we keep them pinned to the newest message; if they had
    // scrolled up to read, we leave them exactly where they were.
    const prevTop = conv.scrollTop;
    const wasNearBottom = (conv.scrollHeight - prevTop - conv.clientHeight) < 60;
    conv.innerHTML = msgs.map(m => \`
      <div class="msg \${m.sender}">
        <div class="lbl">\${m.sender==='admin'?('You'+(m.responder_name?' ('+esc(m.responder_name)+')':'')):'Them'} · \${fmt(m.created_at)}</div>
        <div class="bub">\${m.excerpt?'<div class="ex">'+esc(m.excerpt)+'</div>':''}\${esc(m.body)}</div>
      </div>\`).join('');
    if (!isSameThread || wasNearBottom) {
      // First open of this thread, or the reader was watching the latest message:
      // show the newest message.
      conv.scrollTop = conv.scrollHeight;
    } else {
      // Same thread refreshing while the reader is up reading earlier messages:
      // hold their position so the auto-refresh no longer drags them down.
      conv.scrollTop = prevTop;
    }
    document.getElementById('composer').style.display = 'flex';
    fetch('/api/markread',{method:'POST',headers:{'Content-Type':'application/json'},
      body:JSON.stringify({key})}).then(loadThreads);
    loadThreads();
  }

  async function markHandled(){
    if(!current) return;
    await fetch('/api/handle',{method:'POST',headers:{'Content-Type':'application/json'},
      body:JSON.stringify({key:current})});
    loadThreads();
    openThread(current);
  }

  // Full clean slate — deletes EVERY conversation. Guarded by a typed confirmation
  // so it can never happen by accident. This is the owner doing it on purpose.
  async function resetEverything(){
    if(!window.confirm('Delete EVERY conversation for a clean test? This cannot be undone.')) return;
    const btn = document.getElementById('resetAll');
    if(btn){ btn.disabled = true; btn.textContent = 'Resetting…'; }
    try {
      const r = await fetch('/api/reset',{method:'POST'});
      const d = await r.json();
      current = null;
      document.getElementById('ctx').style.display = 'none';
      document.getElementById('composer').style.display = 'none';
      document.getElementById('conv').innerHTML = '';
      await loadThreads();
      alert('Done — removed ' + (d.removed||0) + ' item(s). The console is now empty.');
    } catch(e){ alert('Reset failed: ' + e.message); }
    if(btn){ btn.disabled = false; btn.textContent = 'Reset everything'; }
  }

  document.getElementById('send').onclick = async () => {
    const ta = document.getElementById('draft');
    const body = ta.value.trim();
    if(!body || !current) return;
    const btn = document.getElementById('send'); btn.disabled = true;
    await fetch('/api/reply',{method:'POST',headers:{'Content-Type':'application/json'},
      body:JSON.stringify({key:current, body})});
    ta.value=''; btn.disabled=false;
    openThread(current);
  };

  // Ask once for permission to show desktop notifications when a message arrives.
  try { if ('Notification' in window && Notification.permission === 'default') Notification.requestPermission(); } catch (e) {}
  loadMe();
  loadThreads();
  // Auto-refresh every 15s. Combined with the server-side thread-list cache this
  // keeps Firestore reads low; new replies you send still appear instantly because
  // sending clears that cache. Lower this only if you truly need faster updates.
  setInterval(() => { loadThreads(); if(current) openThread(current); }, 15000);
</script>
</body></html>`;
