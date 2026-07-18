// Reset every approval to zero for a new production wave. Complaints are LEFT
// alone (they auto-clear via version-lock when a video is redone).
import admin from 'firebase-admin';
import { readFileSync } from 'fs';
import { fileURLToPath } from 'url'; import { dirname, join } from 'path';
const here=dirname(fileURLToPath(import.meta.url));
admin.initializeApp({credential:admin.credential.cert(JSON.parse(readFileSync(join(here,'serviceAccount.json'),'utf8')))});
const db=admin.firestore();
const snap=await db.collection('reviews').get();
let n=0;
for(const doc of snap.docs){
  if(doc.data().approved===true){
    await db.collection('reviews').doc(doc.id).set({approved:false, approvedHash:''},{merge:true});
    n++;
  }
}
console.log('approvals cleared:',n);
process.exit(0);
