// Publish firebase/firestore.rules to the live project via the Firebase Rules
// REST API, authenticated with the same admin service account the inbox uses.
// Usage: node deploy-rules.mjs
// Why not `firebase deploy`? The CLI insists on a serviceusage permission the
// adminsdk account doesn't have; the Rules API itself is fully permitted.
import { readFileSync } from 'fs';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';
import { GoogleAuth } from 'google-auth-library';

const here = dirname(fileURLToPath(import.meta.url));
const PROJECT = 'milk-b4-meat';
const RULES_PATH = join(here, '..', 'firebase', 'firestore.rules');
const API = 'https://firebaserules.googleapis.com/v1';

const auth = new GoogleAuth({
  keyFile: join(here, 'serviceAccount.json'),
  scopes: ['https://www.googleapis.com/auth/firebase', 'https://www.googleapis.com/auth/cloud-platform'],
});
const client = await auth.getClient();
const { token } = await client.getAccessToken();
const headers = { authorization: `Bearer ${token}`, 'content-type': 'application/json' };

const source = readFileSync(RULES_PATH, 'utf8');

// 1) Create a new ruleset from the local file.
const rsRes = await fetch(`${API}/projects/${PROJECT}/rulesets`, {
  method: 'POST',
  headers,
  body: JSON.stringify({ source: { files: [{ name: 'firestore.rules', content: source }] } }),
});
if (!rsRes.ok) { console.error('ruleset create failed:', rsRes.status, await rsRes.text()); process.exit(1); }
const ruleset = await rsRes.json();
console.log('created ruleset:', ruleset.name);

// 2) Point the cloud.firestore release at it (this is the "Publish" button).
const releaseName = `projects/${PROJECT}/releases/cloud.firestore`;
const relRes = await fetch(`${API}/${releaseName}`, {
  method: 'PATCH',
  headers,
  body: JSON.stringify({ release: { name: releaseName, rulesetName: ruleset.name } }),
});
if (!relRes.ok) { console.error('release update failed:', relRes.status, await relRes.text()); process.exit(1); }
const release = await relRes.json();
console.log('LIVE:', release.name, '->', release.rulesetName, '@', release.updateTime);
