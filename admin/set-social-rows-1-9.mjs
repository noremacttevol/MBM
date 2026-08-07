// One-off: rows 1-9 posted on YT/FB/TT/IG (Cameron, 2026-08-07) — set the chips.
import admin from 'firebase-admin';
import { readFileSync } from 'fs';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';
const here = dirname(fileURLToPath(import.meta.url));
const sa = JSON.parse(readFileSync(join(here, 'serviceAccount.json'), 'utf8'));
admin.initializeApp({ credential: admin.credential.cert(sa) });
const db = admin.firestore();
const batch = db.batch();
for (let n = 1; n <= 9; n++) {
  batch.set(db.collection('reviews').doc(String(n)),
    { social: { yt: true, fb: true, tt: true, ig: true } }, { merge: true });
}
await batch.commit();
console.log('chips set on rows 1-9 (yt/fb/tt/ig)');
process.exit(0);
