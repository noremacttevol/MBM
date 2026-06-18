#!/usr/bin/env node
/**
 * kjv_test.js — verify the inline KJV bundle (milk track) is complete and clean.
 *
 * Checks:
 *   1. Every MILK content item has bundled KJV text.
 *   2. No MEAT item has bundled text (we never embed copyrighted scripture).
 *   3. Every verse has a non-empty ref and text.
 *   4. No leftover source markup ("#" paragraph marks or "[ ]" italics brackets).
 *
 * Run: node tools/kjv_test.js
 */
const fs   = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const data = require(path.join(ROOT, 'tools', 'content.data.json'));
const arr  = Array.isArray(data) ? data : (data.CONTENT || data.content || []);

// Pull the KJV_TEXT object out of the generated TS file without a TS loader.
const tsSrc = fs.readFileSync(path.join(ROOT, 'mobile', 'src', 'data', 'kjvText.ts'), 'utf8');
const m = tsSrc.match(/export const KJV_TEXT[^=]*=\s*(\{[\s\S]*?\});\s*\n\nexport function/);
if (!m) { console.error('Could not parse KJV_TEXT from kjvText.ts'); process.exit(1); }
const KJV_TEXT = JSON.parse(m[1]);

const milk = arr.filter(c => c.track === 'MILK');
const meat = arr.filter(c => c.track === 'MEAT');

let pass = 0, fail = 0;
const check = (cond, label) => { if (cond) { pass++; console.log('  PASS ', label); }
                                 else      { fail++; console.log('  FAIL ', label); } };

console.log('Inline KJV bundle');
const milkWithText = milk.filter(c => Array.isArray(KJV_TEXT[c.id]) && KJV_TEXT[c.id].length > 0);
check(milkWithText.length === milk.length,
  `every MILK item has inline text (${milkWithText.length}/${milk.length})`);

const meatWithText = meat.filter(c => KJV_TEXT[c.id]);
check(meatWithText.length === 0,
  `no MEAT item embeds text (${meatWithText.length} found — want 0)`);

let emptyVerses = 0, markers = 0, totalVerses = 0;
for (const id of Object.keys(KJV_TEXT)) {
  for (const v of KJV_TEXT[id]) {
    totalVerses++;
    if (!v.ref || !v.text || !v.text.trim()) emptyVerses++;
    if (/[#\[\]]/.test(v.text)) markers++;
  }
}
check(emptyVerses === 0, `no empty verses (${emptyVerses} empty of ${totalVerses})`);
check(markers === 0,     `no leftover source markup #/[] (${markers} found)`);

console.log(`\n${fail === 0 ? 'ALL CHECKS PASSED' : fail + ' CHECK(S) FAILED'}  — ${pass} passed, ${fail} failed, ${totalVerses} verses bundled`);
process.exit(fail === 0 ? 0 : 1);
