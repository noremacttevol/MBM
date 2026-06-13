/**
 * MBM admin inbox — Cameron's private desk for the "talk to a real person" threads.
 *
 * This is NOT part of the app. It runs only on your machine. It uses the Firebase
 * Admin SDK with a SERVICE ACCOUNT key, which bypasses the Firestore rules so you
 * can read every person's thread and reply to them. That key is the one secret
 * that must never ship in the app or go into git — it lives only here, beside this
 * file, as serviceAccount.json (which .gitignore keeps out of the repo).
 *
 * Run it:   cd admin && npm install && npm start
 * Then open http://localhost:4545 in your browser.
 *
 * What you see: every person who has written in, newest first. Click a person to
 * read their whole thread and write back. Your reply lands in their app live.
 */

import { readFileSync, existsSync } from 'fs';
import http from 'http';
import { initializeApp, cert } from 'firebase-admin/app';
import { getFirestore, FieldValue } from 'firebase-admin/firestore';

const PORT = 4545;
const KEY_PATH = new URL('./serviceAccount.json', import.meta.url);

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

// ── Helpers ───────────────────────────────────────────────────────────────────

function isoOf(v) {
  try {
    if (v && typeof v.toDate === 'function') return v.toDate().toISOString();
  } catch {/* fall through */}
  return new Date().toISOString();
}

function mapDoc(doc) {
  const d = doc.data();
  return {
    id:           doc.id,
    user_id:      d.userId ?? '',
    sender:       d.sender === 'admin' ? 'admin' : 'user',
    body:         d.body ?? '',
    excerpt:      d.excerpt ?? null,
    journey_stage: d.journeyStage ?? null,
    created_at:   isoOf(d.createdAt),
    read_by_admin: !!d.readByAdmin,
    read_by_user:  !!d.readByUser,
  };
}

async function allMessages() {
  const snap = await db.collection(COL).orderBy('createdAt', 'asc').get();
  return snap.docs.map(mapDoc);
}

// Group every message into one thread per person, newest thread first.
async function listThreads() {
  const msgs = await allMessages();
  const byUser = new Map();
  for (const m of msgs) {
    if (!byUser.has(m.user_id)) {
      byUser.set(m.user_id, { uid: m.user_id, messages: [], unread: 0, stage: null });
    }
    const t = byUser.get(m.user_id);
    t.messages.push(m);
    if (m.sender === 'user' && !m.read_by_admin) t.unread += 1;
    if (m.sender === 'user' && m.journey_stage) t.stage = m.journey_stage;
  }
  const threads = [...byUser.values()].map(t => {
    const last = t.messages[t.messages.length - 1];
    return {
      uid:     t.uid,
      unread:  t.unread,
      stage:   t.stage,
      count:   t.messages.length,
      last:    last ? { body: last.body, sender: last.sender, created_at: last.created_at } : null,
    };
  });
  threads.sort((a, b) =>
    (b.last?.created_at ?? '').localeCompare(a.last?.created_at ?? ''));
  return threads;
}

async function getThread(uid) {
  const snap = await db.collection(COL)
    .where('userId', '==', uid)
    .orderBy('createdAt', 'asc')
    .get();
  return snap.docs.map(mapDoc);
}

async function reply(uid, body) {
  const clean = (body ?? '').trim();
  if (!uid || !clean) return false;
  await db.collection(COL).add({
    userId:       uid,
    sender:       'admin',
    body:         clean,
    excerpt:      null,
    journeyStage: null,
    createdAt:    FieldValue.serverTimestamp(),
    readByAdmin:  true,
    readByUser:   false,
  });
  return true;
}

async function markRead(uid) {
  const snap = await db.collection(COL)
    .where('userId', '==', uid)
    .where('sender', '==', 'user')
    .where('readByAdmin', '==', false)
    .get();
  const batch = db.batch();
  snap.docs.forEach(d => batch.update(d.ref, { readByAdmin: true }));
  await batch.commit();
  return snap.size;
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
    if (req.method === 'GET' && url.pathname === '/api/threads') {
      return json(res, 200, await listThreads());
    }
    if (req.method === 'GET' && url.pathname === '/api/thread') {
      const uid = url.searchParams.get('uid') ?? '';
      return json(res, 200, await getThread(uid));
    }
    if (req.method === 'POST' && url.pathname === '/api/reply') {
      const { uid, body } = await readBody(req);
      const ok = await reply(uid, body);
      return json(res, ok ? 200 : 400, { ok });
    }
    if (req.method === 'POST' && url.pathname === '/api/markread') {
      const { uid } = await readBody(req);
      const n = await markRead(uid);
      return json(res, 200, { ok: true, marked: n });
    }
    json(res, 404, { error: 'not found' });
  } catch (e) {
    json(res, 500, { error: String(e?.message ?? e) });
  }
});

server.listen(PORT, () => {
  console.log(`\n  MBM admin inbox running at  http://localhost:${PORT}\n`);
});

// ── The page (dark, quiet, matches the app) ─────────────────────────────────

const PAGE = `<!doctype html>
<html lang="en"><head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>MBM — real-person inbox</title>
<style>
  :root{--bg:#0a0a0f;--card:#111116;--input:#141418;--border:#2a2820;--green:#7ab87a;
        --gold:#d4c89a;--text:#e8e4d8;--mid:#c8bfa8;--dim:#9a9080;--muted:#5a5240;}
  *{box-sizing:border-box;font-family:Georgia,serif;}
  body{margin:0;background:var(--bg);color:var(--text);display:flex;height:100vh;}
  h1{font-size:15px;color:var(--mid);font-weight:normal;margin:0;letter-spacing:.5px;}
  #left{width:320px;border-right:1px solid var(--border);display:flex;flex-direction:column;}
  #head{padding:16px;border-bottom:1px solid var(--border);}
  #sub{font-size:11px;color:var(--muted);margin-top:4px;}
  #threads{overflow-y:auto;flex:1;}
  .t{padding:14px 16px;border-bottom:1px solid var(--border);cursor:pointer;}
  .t:hover{background:#16161c;}
  .t.active{background:#16161c;border-left:2px solid var(--gold);}
  .t .who{font-size:12px;color:var(--dim);display:flex;justify-content:space-between;}
  .t .snip{font-size:13px;color:var(--mid);margin-top:5px;overflow:hidden;
           text-overflow:ellipsis;white-space:nowrap;}
  .dot{background:var(--green);color:#0a0f0a;border-radius:10px;font-size:11px;
       padding:1px 7px;}
  .stage{font-size:10px;color:var(--muted);text-transform:uppercase;letter-spacing:.5px;}
  #right{flex:1;display:flex;flex-direction:column;}
  #conv{flex:1;overflow-y:auto;padding:20px;}
  .empty{color:var(--muted);font-size:14px;padding:40px;text-align:center;}
  .msg{max-width:70%;margin-bottom:14px;}
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
  #composer{border-top:1px solid var(--border);padding:14px;display:flex;gap:10px;}
  textarea{flex:1;background:var(--input);border:1px solid var(--border);border-radius:6px;
           color:var(--mid);font-size:14px;padding:10px;min-height:46px;resize:vertical;}
  button{background:var(--green);color:#0a0f0a;border:none;border-radius:4px;
         padding:0 18px;font-size:13px;font-weight:bold;cursor:pointer;}
  button:disabled{opacity:.5;cursor:default;}
</style></head>
<body>
  <div id="left">
    <div id="head"><h1>Real-person inbox</h1>
      <div id="sub">Every word here is a real person reaching out. Reply gently.</div></div>
    <div id="threads"><div class="empty">Loading…</div></div>
  </div>
  <div id="right">
    <div id="conv"><div class="empty">Pick someone on the left to read their thread.</div></div>
    <div id="composer" style="display:none">
      <textarea id="draft" placeholder="Write back as a real person…"></textarea>
      <button id="send">Send</button>
    </div>
  </div>
<script>
  let current = null;
  const esc = s => (s||'').replace(/[&<>]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));
  const fmt = iso => { const d=new Date(iso); return isNaN(d)?'':d.toLocaleString(); };

  async function loadThreads(){
    const r = await fetch('/api/threads'); const list = await r.json();
    const box = document.getElementById('threads');
    if(!list.length){ box.innerHTML='<div class="empty">No one has written in yet.</div>'; return; }
    box.innerHTML = list.map(t => \`
      <div class="t \${t.uid===current?'active':''}" onclick="openThread('\${t.uid}')">
        <div class="who"><span class="stage">\${esc(t.stage||'')}</span>
          \${t.unread?'<span class="dot">'+t.unread+'</span>':''}</div>
        <div class="snip">\${t.last?(t.last.sender==='admin'?'You: ':'')+esc(t.last.body):''}</div>
      </div>\`).join('');
  }

  async function openThread(uid){
    current = uid;
    const r = await fetch('/api/thread?uid='+encodeURIComponent(uid));
    const msgs = await r.json();
    const conv = document.getElementById('conv');
    conv.innerHTML = msgs.map(m => \`
      <div class="msg \${m.sender}">
        <div class="lbl">\${m.sender==='admin'?'You':'Them'} · \${fmt(m.created_at)}</div>
        <div class="bub">\${m.excerpt?'<div class="ex">'+esc(m.excerpt)+'</div>':''}\${esc(m.body)}</div>
      </div>\`).join('');
    conv.scrollTop = conv.scrollHeight;
    document.getElementById('composer').style.display = 'flex';
    fetch('/api/markread',{method:'POST',headers:{'Content-Type':'application/json'},
      body:JSON.stringify({uid})}).then(loadThreads);
    loadThreads();
  }

  document.getElementById('send').onclick = async () => {
    const ta = document.getElementById('draft');
    const body = ta.value.trim();
    if(!body || !current) return;
    const btn = document.getElementById('send'); btn.disabled = true;
    await fetch('/api/reply',{method:'POST',headers:{'Content-Type':'application/json'},
      body:JSON.stringify({uid:current, body})});
    ta.value=''; btn.disabled=false;
    openThread(current);
  };

  loadThreads();
  setInterval(() => { loadThreads(); if(current) openThread(current); }, 5000);
</script>
</body></html>`;
