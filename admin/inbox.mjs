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
import { initializeApp, cert } from 'firebase-admin/app';
import { getFirestore, FieldValue } from 'firebase-admin/firestore';

const PORT = 4545;
const KEY_PATH = new URL('./serviceAccount.json', import.meta.url);

// ── Who is answering right now (Phase 1: just Cameron) ──────────────────────────
// Phase 2: replace this with the logged-in volunteer. Everything downstream — the
// reply stamp and the "handled by" record — already reads from here, so adding more
// helpers is a login change, not a rebuild.
const RESPONDER = { id: 'cameron', name: 'Cameron' };

if (!existsSync(KEY_PATH)) {
  console.error(
    '\n  Missing serviceAccount.json.\n\n' +
    '  Get it from the Firebase console:\n' +
    '    Project settings (gear) -> Service accounts -> Generate new private key.\n' +
    '  Save the downloaded file as  admin/serviceAccount.json  and run again.\n' +
    '  (It is gitignored — it must never be committed.)\n',
  );
  process.exit(1);
}

const serviceAccount = JSON.parse(readFileSync(KEY_PATH, 'utf8'));
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
      byKey.set(key, { key, uid: m.user_id, threadId: m.thread_id, messages: [], unread: 0, stage: null, crisis: false, cancelled: false });
    }
    const t = byKey.get(key);
    t.messages.push(m);
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

async function getThread(key) {
  const { uid, threadId } = parseKey(key);
  // One equality query on userId (the existing index), then filter to this
  // conversation on the client — so no extra composite index is needed.
  const snap = await db.collection(COL)
    .where('userId', '==', uid)
    .orderBy('createdAt', 'asc')
    .get();
  const messages = snap.docs.map(mapDoc).filter(m => m.thread_id === threadId);
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
  return {
    messages,
    title: titleOf(messages),
    stage: [...messages].reverse().find(x => x.sender === 'user' && x.journey_stage)?.journey_stage ?? null,
    status: deriveStatus(messages, meta),
    handled_by_name: meta?.handled_by_name ?? null,
  };
}

async function reply(key, body) {
  const clean = (body ?? '').trim();
  const { uid, threadId } = parseKey(key);
  if (!uid || !clean) return false;
  // The app reader (mobile/src/lib/messaging.ts) ignores responderId/responderName;
  // they exist only so this desk — now and with volunteers later — can show who
  // answered. The reply is stamped with the SAME threadId so it lands in exactly the
  // conversation the person asked in. Nothing about the person's experience changes.
  await db.collection(COL).add({
    userId:        uid,
    threadId,
    threadTitle:   null,
    sender:        'admin',
    body:          clean,
    excerpt:       null,
    journeyStage:  null,
    responderId:   RESPONDER.id,
    responderName: RESPONDER.name,
    createdAt:     FieldValue.serverTimestamp(),
    readByAdmin:   true,
    readByUser:    false,
  });
  // Answering a person is itself catching up with them: record it as handled now.
  await db.collection(META).doc(key).set({
    status:        'handled',
    handledAt:     FieldValue.serverTimestamp(),
    handledById:   RESPONDER.id,
    handledByName: RESPONDER.name,
  }, { merge: true });
  return true;
}

// Mark a conversation handled without sending a message — for when a person's note
// needs no reply (a thank-you, a closing word) but you don't want it nagging the queue.
async function markHandled(key) {
  if (!key) return false;
  await db.collection(META).doc(key).set({
    status:        'handled',
    handledAt:     FieldValue.serverTimestamp(),
    handledById:   RESPONDER.id,
    handledByName: RESPONDER.name,
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
    if (req.method === 'GET' && url.pathname === '/') {
      res.writeHead(200, { 'Content-Type': 'text/html' });
      res.end(PAGE);
      return;
    }
    if (req.method === 'GET' && url.pathname === '/api/me') {
      return json(res, 200, { name: RESPONDER.name });
    }
    if (req.method === 'GET' && url.pathname === '/api/threads') {
      return json(res, 200, await listThreads());
    }
    if (req.method === 'GET' && url.pathname === '/api/thread') {
      const key = url.searchParams.get('key') ?? '';
      return json(res, 200, await getThread(key));
    }
    if (req.method === 'POST' && url.pathname === '/api/reply') {
      const { key, body } = await readBody(req);
      const ok = await reply(key, body);
      return json(res, ok ? 200 : 400, { ok });
    }
    if (req.method === 'POST' && url.pathname === '/api/handle') {
      const { key } = await readBody(req);
      const ok = await markHandled(key);
      return json(res, ok ? 200 : 400, { ok });
    }
    if (req.method === 'POST' && url.pathname === '/api/markread') {
      const { key } = await readBody(req);
      const n = await markRead(key);
      return json(res, 200, { ok: true, marked: n });
    }
    json(res, 404, { error: 'not found' });
  } catch (e) {
    json(res, 500, { error: String(e?.message ?? e) });
  }
});

server.listen(PORT, () => {
  console.log(`\n  MBM ministry console running at  http://localhost:${PORT}`);
  console.log(`  Answering as: ${RESPONDER.name}\n`);
});

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
      <div id="who-am-i"></div></div>
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
    try { const r = await fetch('/api/me'); const m = await r.json();
      document.getElementById('who-am-i').textContent = 'Answering as ' + (m.name||'a helper') + '.';
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
    box.innerHTML = view.map(t => \`
      <div class="t \${t.key===current?'active':''} \${t.crisis?'crisis':''} \${t.cancelled?'cancelled':''}" onclick="openThread('\${esc(t.key)}')">
        <div class="who">
          <span class="stage">\${t.crisis?'<span class="crisisbadge">⚠ CRISIS</span> ':''}\${t.cancelled?'<span class="cancelbadge">CANCELLED</span> ':''}\${esc(t.stage||'')}</span>
          <span style="display:flex;gap:6px;align-items:center;">
            \${t.unread?'<span class="dot">'+t.unread+'</span>':''}
            <span class="badge \${t.status}">\${esc(t.status_label||'')}</span>
          </span>
        </div>
        <div class="ttl">\${esc(t.title||'Conversation')}</div>
        <div class="snip">\${t.last?(t.last.sender==='admin'?'You: ':'')+esc(t.last.body):''}</div>
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
    const r = await fetch('/api/threads'); lastList = await r.json();
    renderThreads(lastList);
    notifyNew(lastList);
  }

  async function openThread(key){
    current = key;
    const r = await fetch('/api/thread?key='+encodeURIComponent(key));
    const data = await r.json();
    const msgs = data.messages || [];

    const ctx = document.getElementById('ctx');
    const titleTxt = data.title ? '<b>' + esc(data.title) + '</b>  ·  ' : '';
    const stageTxt = data.stage ? '<b>Where they are:</b> ' + esc(data.stage) + '  ·  ' : '';
    const statusTxt = data.status==='needs_reply' ? 'Waiting on a reply'
      : data.status==='handled' ? ('Handled' + (data.handled_by_name ? ' by ' + esc(data.handled_by_name) : ''))
      : 'You answered last';
    document.getElementById('ctx-meta').innerHTML = titleTxt + stageTxt + statusTxt;
    ctx.style.display = 'flex';

    const conv = document.getElementById('conv');
    conv.innerHTML = msgs.map(m => \`
      <div class="msg \${m.sender}">
        <div class="lbl">\${m.sender==='admin'?('You'+(m.responder_name?' ('+esc(m.responder_name)+')':'')):'Them'} · \${fmt(m.created_at)}</div>
        <div class="bub">\${m.excerpt?'<div class="ex">'+esc(m.excerpt)+'</div>':''}\${esc(m.body)}</div>
      </div>\`).join('');
    conv.scrollTop = conv.scrollHeight;
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
  setInterval(() => { loadThreads(); if(current) openThread(current); }, 5000);
</script>
</body></html>`;
