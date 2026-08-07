// Seed / refresh the posting tracker's "In the app" column on the review page.
// Reads media-production-v2/PUBLISH-LEDGER.json (the app-publish record) and sets
// social.app = true on reviews/<row> for every row whose current v2.x version is
// live on an app platform. Rerun any time — it only merges the one field.
//   cd admin && node seed-social-app-status.mjs
import admin from 'firebase-admin';
import { readFileSync } from 'fs';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';

const here = dirname(fileURLToPath(import.meta.url));
const sa = JSON.parse(readFileSync(join(here, 'serviceAccount.json'), 'utf8'));
admin.initializeApp({ credential: admin.credential.cert(sa) });
const db = admin.firestore();

const led = JSON.parse(readFileSync(
  join(here, '..', 'media-production-v2', 'PUBLISH-LEDGER.json'), 'utf8')).rows;

let batch = db.batch(), n = 0;
for (const [row, r] of Object.entries(led)) {
  const v2 = (r.versions || []).filter(v => String(v.version || '').startsWith('2'));
  const inApp = v2.some(v => (v.where || []).some(w => String(w.platform || '').startsWith('app')));
  if (!inApp) continue;
  batch.set(db.collection('reviews').doc(String(row)), { social: { app: true } }, { merge: true });
  n++;
}
await batch.commit();
console.log(`social.app=true merged onto ${n} review docs`);
process.exit(0);
