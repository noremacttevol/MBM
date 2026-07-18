// Full audit of Cameron's review board: every video he ever tapped, what state
// it's in now, and when. Shows approvals that were later undone/lost.
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
const everTapped=[], approvedNow=[], approvedFlagFalse=[], complained=[];
snap.forEach(doc=>{ const n=+doc.id, d=doc.data();
  everTapped.push(n);
  if(d.approved===true) approvedNow.push(n);
  if(d.approved===false && d.approvedHash) approvedFlagFalse.push(n); // approved at some point, now off
  if(d.complaint) complained.push(n);
});
console.log('TOTAL videos you have ever tapped (any action):', everTapped.length);
console.log('  approved = TRUE right now:', approvedNow.length, approvedNow.sort((a,b)=>a-b).join(','));
console.log('  approved flag now FALSE but has an approval stamp (undone/toggled off):', approvedFlagFalse.length, approvedFlagFalse.sort((a,b)=>a-b).join(','));
console.log('  have a complaint recorded:', complained.length, complained.sort((a,b)=>a-b).join(','));
process.exit(0);
