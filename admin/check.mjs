import admin from 'firebase-admin';
import { readFileSync } from 'fs';
import { execSync } from 'child_process';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';
const here=dirname(fileURLToPath(import.meta.url)); const REPO=join(here,'..');
admin.initializeApp({credential:admin.credential.cert(JSON.parse(readFileSync(join(here,'serviceAccount.json'),'utf8')))});
const db=admin.firestore(); const hashes={};
execSync('git ls-tree -r HEAD -- media-production',{cwd:REPO}).toString().split('\n').forEach(l=>{
  const [meta,path]=l.split('\t'); if(!path)return; const h=(meta||'').split(/\s+/)[2];
  const m=path.match(/build-(\d+)-.*\/[0-9a-z]+-\d+_.*\.mp4$/); if(m)hashes[+m[1]]=h;});
const snap=await db.collection('reviews').get();
const ok=[],mismatch=[];
snap.forEach(doc=>{const n=+doc.id,d=doc.data(); if(d.approved!==true)return;
  (d.approvedHash===hashes[n]?ok:mismatch).push(n);});
console.log('approved AND showing correctly:',ok.length, ok.sort((a,b)=>a-b).join(','));
console.log('approved BUT rebuilt again since (getting kicked out):',mismatch.length, mismatch.sort((a,b)=>a-b).join(','));
process.exit(0);
