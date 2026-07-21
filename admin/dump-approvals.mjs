// One-off: dump EVERY review doc's approval state straight from Firestore,
// ignoring the version-lock filter in sync-reviews.mjs — we need the approved
// hashes even for videos whose current cut no longer matches (regressions).
import admin from 'firebase-admin';
import { readFileSync } from 'fs';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';

const here = dirname(fileURLToPath(import.meta.url));
const sa = JSON.parse(readFileSync(join(here, 'serviceAccount.json'), 'utf8'));
admin.initializeApp({ credential: admin.credential.cert(sa) });
const db = admin.firestore();

const snap = await db.collection('reviews').get();
const out = {};
snap.forEach((doc) => {
  const d = doc.data();
  out[doc.id] = {
    approved: !!d.approved,
    approvedHash: d.approvedHash || null,
    approvedAt: d.approvedAt && d.approvedAt.toDate ? d.approvedAt.toDate().toISOString() : null,
    complaint: d.complaint || null,
    complaintHash: d.complaintHash || null,
  };
});
console.log(JSON.stringify(out, null, 2));
process.exit(0);
