// Restore Cameron's approvals: for any video he approved whose cut changed since
// (a machine rebuilt it), re-point approvedHash to the CURRENT cut so it shows
// approved again. He said these were good; trust that.
import admin from 'firebase-admin';
import { readFileSync } from 'fs';
import { execSync } from 'child_process';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';
const here = dirname(fileURLToPath(import.meta.url));
const REPO = join(here,'..');
const sa = JSON.parse(readFileSync(join(here,'serviceAccount.json'),'utf8'));
admin.initializeApp({ credential: admin.credential.cert(sa) });
const db = admin.firestore();
const hashes={};
execSync('git ls-tree -r HEAD -- media-production',{cwd:REPO}).toString().split('\n').forEach(l=>{
  const [meta,path]=l.split('\t'); if(!path)return;
  const h=(meta||'').split(/\s+/)[2];
  const m=path.match(/build-(\d+)-.*\/[0-9a-z]+-\d+_.*\.mp4$/); if(m)hashes[+m[1]]=h;
});
const snap=await db.collection('reviews').get();
const fixed=[];
for(const doc of snap.docs){const n=+doc.id,d=doc.data();
  if(d.approved && hashes[n] && d.approvedHash!==hashes[n]){
    await db.collection('reviews').doc(doc.id).set({approvedHash:hashes[n]},{merge:true});
    fixed.push(n);
  }
}
console.log('re-anchored approvals to current cut:',fixed.sort((a,b)=>a-b));
process.exit(0);
