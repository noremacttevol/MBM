/**
 * MBM watcher — the piece that makes sure you NEVER miss someone.
 *
 * This is NOT part of the app and never ships in it. It runs quietly in the
 * background (on your computer now, on a host later) and does one job:
 *
 *   The moment a person writes a note to a real human, this:
 *     1. picks who should answer (you, or — when you've approved helpers —
 *        whichever helper is least busy: "auto-distribute"),
 *     2. emails that person the note + a one-tap link to your reply desk.
 *
 * It uses the SAME service-account key as the desk (admin/serviceAccount.json),
 * which bypasses the Firestore rules so it can see every thread. That key never
 * ships in the app and is gitignored. A person never sees any of this — only the
 * warm reply you send back from the desk.
 *
 * It reads/writes the exact same data the desk already uses:
 *   - messages   : one doc per message (we watch for new sender:'user' notes)
 *   - threadMeta : one doc per conversation, id = `${userId}||${threadId}`
 *                  (we set assignedToId / assignedToName here = the auto-split)
 * It adds ONE harmless field to a message when it has alerted on it:
 *   - adminAlertedAt : so the same note is never emailed twice, even across
 *     restarts. The app's reader ignores unknown fields, so the person's side is
 *     untouched.
 *
 * Run it:   cd admin && npm install && npm run start:watch
 * Stop it:  Ctrl-C
 *
 * Setup is ONE key from Resend + your MBM domain — see admin/WATCHER-SETUP.md.
 * Alerts are sent professionally as  MBM <notify@yourdomain>  — no personal email.
 */

import { readFileSync, existsSync } from 'fs';
import { initializeApp, cert } from 'firebase-admin/app';
import { getFirestore, FieldValue, Timestamp } from 'firebase-admin/firestore';

// ── Config (all from environment, with safe defaults) ───────────────────────
const KEY_PATH = new URL('./serviceAccount.json', import.meta.url);

// Where your reply desk lives. Localhost now; change to the hosted address later.
const DESK_URL = (process.env.ADMIN_DESK_URL || 'http://localhost:4545').trim();

// The owner — you. Gets everything when no helpers are approved yet, and is the
// fallback if auto-distribute ever finds nobody available.
const OWNER = {
  id:    (process.env.OWNER_ID    || 'cameron').trim(),
  name:  (process.env.OWNER_NAME  || 'Cameron').trim(),
  email: (process.env.OWNER_EMAIL || 'noremacttevol@gmail.com').trim(),
};

// Professional sending via Resend (https://resend.com): ONE API key, and a "from"
// address on YOUR OWN MBM domain — e.g.  MBM <notify@milkbeforemeat.app>. No Gmail,
// no app password, nothing personal. (See WATCHER-SETUP.md.)
const RESEND_API_KEY = (process.env.RESEND_API_KEY || '').trim();
const ALERT_FROM     = (process.env.ALERT_FROM || 'MBM <onboarding@resend.dev>').trim();

const COL  = 'messages';
const META = 'threadMeta';
const ADMINS = 'admins'; // approved helpers live here; absent/empty => just the owner

const LEGACY_THREAD = 'main';
const keyOf = (uid, threadId) => `${uid}||${threadId || LEGACY_THREAD}`;

// ── Boot checks ─────────────────────────────────────────────────────────────
if (!existsSync(KEY_PATH)) {
  console.error(
    '\n  Missing serviceAccount.json.\n' +
    '  Put your Firebase service-account key at  admin/serviceAccount.json  and run again.\n' +
    '  (Same key the desk uses. It is gitignored — never commit it.)\n',
  );
  process.exit(1);
}

const serviceAccount = JSON.parse(readFileSync(KEY_PATH, 'utf8'));
initializeApp({ credential: cert(serviceAccount) });
const db = getFirestore();

// If the Resend key isn't set yet, the watcher still runs and still does the
// auto-assigning — it just prints the alert to the screen and tells you what to
// add, so nothing is silently lost.
const emailOn = !!RESEND_API_KEY;
if (!emailOn) {
  console.warn(
    '\n  ⚠  Email is not set up yet, so alerts will print here instead of emailing.\n' +
    '     To turn on real branded emails, follow admin/WATCHER-SETUP.md.\n',
  );
}

// ── Small helpers ───────────────────────────────────────────────────────────
const isoOrNow = (v) => {
  try { if (v && typeof v.toDate === 'function') return v.toDate().toISOString(); } catch {}
  return new Date().toISOString();
};

function snippet(text, n = 400) {
  const s = String(text || '').trim();
  return s.length > n ? s.slice(0, n) + '…' : s;
}

// Read the approved, available helpers. Returns [] when you're still solo, which
// makes the owner answer everything — exactly Phase 1.
async function approvedAdmins() {
  try {
    const snap = await db.collection(ADMINS).get();
    return snap.docs
      .map(d => ({ id: d.id, ...d.data() }))
      .filter(a => a.status === 'approved' && a.available !== false && a.email);
  } catch {
    return [];
  }
}

// How many still-open conversations each helper already owns — so auto-distribute
// can hand the next one to whoever is LEAST busy (simple, fair load balancing).
async function openCountsByAdmin() {
  const counts = new Map();
  try {
    const snap = await db.collection(META).get();
    snap.docs.forEach(d => {
      const m = d.data();
      const handled = !!m.handledAt && m.status === 'handled';
      if (!handled && m.assignedToId) {
        counts.set(m.assignedToId, (counts.get(m.assignedToId) || 0) + 1);
      }
    });
  } catch {}
  return counts;
}

// Pick who should answer a NEW conversation: the least-busy approved helper, or
// the owner when there are none. This is the whole "auto-distribute" you chose.
async function chooseResponder() {
  const admins = await approvedAdmins();
  if (admins.length === 0) return OWNER;
  const counts = await openCountsByAdmin();
  admins.sort((a, b) => (counts.get(a.id) || 0) - (counts.get(b.id) || 0));
  const a = admins[0];
  return { id: a.id, name: a.name || a.email, email: a.email };
}

// ── The alert email ─────────────────────────────────────────────────────────
async function sendAlert(to, person, msg) {
  const link = DESK_URL; // later: deep-link straight to the thread
  const stage = person.journeyStage ? `\nWhere they are: ${person.journeyStage}` : '';
  const subject = `MBM — someone is asking for a real person`;
  const text =
    `Someone in MBM just reached out to talk to a real person.\n\n` +
    `Their message:\n“${snippet(msg.body)}”` +
    `${msg.excerpt ? `\n\nAbout this part of their chat:\n“${snippet(msg.excerpt, 200)}”` : ''}` +
    `${stage}\n\n` +
    `Reply to them here:\n${link}\n\n` +
    `— MBM watcher (you're receiving this because you're answering for the team)`;

  if (!emailOn) {
    console.log(`\n──────── ALERT (email off) → ${to.name} <${to.email}> ────────`);
    console.log(text);
    console.log('────────────────────────────────────────────────────────────\n');
    return;
  }
  const res = await fetch('https://api.resend.com/emails', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${RESEND_API_KEY}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ from: ALERT_FROM, to: [to.email], subject, text }),
  });
  if (!res.ok) {
    const detail = await res.text().catch(() => '');
    throw new Error(`Resend ${res.status}: ${detail.slice(0, 200)}`);
  }
  console.log(`  ✉  alerted ${to.name} <${to.email}> about ${person.userId.slice(0, 6)}…`);
}

// ── Handle one new user message ─────────────────────────────────────────────
async function handleUserMessage(doc, startAt) {
  const d = doc.data();
  if (d.sender !== 'user') return;          // only people's notes
  if (d.adminAlertedAt) return;             // already alerted (restart-safe dedup)

  const uid = d.userId || '';
  if (!uid) return;
  const tKey = keyOf(uid, d.threadId);
  const metaRef = db.collection(META).doc(tKey);
  const metaSnap = await metaRef.get();
  const meta = metaSnap.exists ? metaSnap.data() : null;

  // Quiet backfill: any note that already existed BEFORE the watcher started is
  // marked "seen" without emailing. This means starting (or restarting) the
  // watcher never blasts you with a pile of past notes — you only get an email
  // for a note that arrives while it's running. (Hosting it always-on in Step B
  // removes the gap entirely.) Existing notes are still visible on your desk.
  const created = d.createdAt instanceof Timestamp ? d.createdAt : null;
  const isOld = created ? created.toMillis() < startAt.toMillis() : false;
  if (isOld) {
    await doc.ref.update({ adminAlertedAt: FieldValue.serverTimestamp() });
    return;
  }

  // Decide who answers. Keep an existing assignment if the thread already has one
  // (so a returning person stays with the same helper); otherwise auto-distribute.
  let responder;
  if (meta && meta.assignedToId) {
    responder = {
      id: meta.assignedToId,
      name: meta.assignedToName || meta.assignedToId,
      email: meta.assignedToEmail || OWNER.email,
    };
  } else {
    responder = await chooseResponder();
    await metaRef.set({
      assignedToId:    responder.id,
      assignedToName:  responder.name,
      assignedToEmail: responder.email,
      assignedAt:      FieldValue.serverTimestamp(),
      status:          'needs_reply',
    }, { merge: true });
  }

  await sendAlert(responder, { userId: uid, journeyStage: d.journeyStage }, d);
  await doc.ref.update({ adminAlertedAt: FieldValue.serverTimestamp() });
}

// ── Live listener ───────────────────────────────────────────────────────────
function start() {
  const startAt = Timestamp.now();
  console.log('\n  MBM watcher is listening.');
  console.log(`  Desk link in alerts: ${DESK_URL}`);
  console.log(`  Owner (fallback):    ${OWNER.name} <${OWNER.email}>`);
  console.log(`  Email sending:       ${emailOn ? `ON (from ${ALERT_FROM})` : 'OFF (printing to screen)'}\n`);

  // Watch the messages collection. We deliberately do NOT add a where/orderBy
  // combo here — that would require a special Firestore index you'd have to
  // create by hand. Instead we watch everything and ignore non-user notes in
  // code (handleUserMessage returns early for admin replies). Each note is
  // handled once and marked, so restarts never double-send.
  db.collection(COL)
    .onSnapshot(
      (snap) => {
        snap.docChanges().forEach((change) => {
          if (change.type === 'added') {
            handleUserMessage(change.doc, startAt).catch(err =>
              console.error('  ! alert failed:', err.message));
          }
        });
      },
      (err) => {
        console.error('  ! listener error:', err.message);
        console.error('    Reconnecting in 5s…');
        setTimeout(start, 5000);
      },
    );
}

start();
