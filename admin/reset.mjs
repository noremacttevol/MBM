/**
 * MBM reset — wipe the ministry-console data for a clean test.
 *
 * This PERMANENTLY DELETES every conversation: all docs in `messages` and
 * `threadMeta`. It does NOT touch your Firebase project, rules, or auth — only the
 * stored chats. The app side (a person's on-device profile) is reset separately by
 * the persist-key bump in mobile/src/store/useAppStore.ts, which clears local data
 * the next time the app loads.
 *
 * Safety: it will NOT run unless you pass --yes, so it can never fire by accident.
 *
 *   cd admin
 *   node reset.mjs            # shows what it WOULD delete, then stops
 *   node reset.mjs --yes      # actually deletes
 */

import { readFileSync, existsSync } from 'fs';
import { initializeApp, cert } from 'firebase-admin/app';
import { getFirestore } from 'firebase-admin/firestore';

const KEY_PATH = new URL('./serviceAccount.json', import.meta.url);
if (!existsSync(KEY_PATH)) {
  console.error('\n  Missing serviceAccount.json — put your Firebase key at admin/serviceAccount.json.\n');
  process.exit(1);
}

initializeApp({ credential: cert(JSON.parse(readFileSync(KEY_PATH, 'utf8'))) });
const db = getFirestore();
const CONFIRMED = process.argv.includes('--yes');

async function wipe(collectionName) {
  const snap = await db.collection(collectionName).get();
  if (snap.empty) { console.log(`  ${collectionName}: already empty.`); return 0; }
  if (!CONFIRMED) { console.log(`  ${collectionName}: ${snap.size} doc(s) would be deleted.`); return snap.size; }
  // Delete in batches of 450 (Firestore caps a batch at 500 writes).
  let deleted = 0;
  let batch = db.batch();
  let n = 0;
  for (const doc of snap.docs) {
    batch.delete(doc.ref);
    n++; deleted++;
    if (n === 450) { await batch.commit(); batch = db.batch(); n = 0; }
  }
  if (n > 0) await batch.commit();
  console.log(`  ${collectionName}: deleted ${deleted} doc(s).`);
  return deleted;
}

(async () => {
  console.log(`\n  MBM ministry-console reset ${CONFIRMED ? '(LIVE — deleting)' : '(dry run — nothing deleted)'}\n`);
  const a = await wipe('messages');
  const b = await wipe('threadMeta');
  if (!CONFIRMED) {
    console.log(`\n  Nothing was deleted. To actually wipe ${a + b} doc(s), run:\n    node reset.mjs --yes\n`);
  } else {
    console.log('\n  Done. The ministry console is now empty. Reload it to confirm.\n');
  }
  process.exit(0);
})().catch(e => { console.error('  reset failed:', e.message); process.exit(1); });
