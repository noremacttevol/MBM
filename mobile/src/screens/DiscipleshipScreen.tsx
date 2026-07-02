/**
 * DiscipleshipScreen — "My Discipleship", the members-only "Walk with Christ"
 * reflection companion (Cameron, June 2026).
 *
 * Four flows, all private, all opt-in, fully decoupled from the feed / routing /
 * readiness logic:
 *   1. Today's Examen  — one gentle prompt tied to a Christlike quality; free
 *      journaling + a short personal blessing spoken back.
 *   2. My Walk with Christ — a private timeline of past reflections + an on-demand
 *      grace-first narrative summary of where Christ has been at work.
 *   3. Your Fruit Garden — the MEMBER's OWN self-ratings of the seven qualities
 *      (never an AI score), fully hideable.
 *   4. Rule of Life — 2–4 personal rhythms, gently tracked, no punishing streaks.
 *
 * Tone law: grace-first, inspiring, never guilt-inducing. No numbers from the AI,
 * no bars that judge, no streaks that shame, no comparison.
 */
import React, { useState } from 'react';
import {
  View, Text, TextInput, TouchableOpacity, ScrollView,
  StyleSheet, KeyboardAvoidingView, Platform, ActivityIndicator,
} from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { StatusBar } from 'expo-status-bar';
import { useNavigation } from '@react-navigation/native';
import { useAppStore } from '../store/useAppStore';
import { TraitKey } from '../data/questionBank';
import { QUALITIES, QUALITY_BY_KEY, promptFor, verseFor } from '../data/examenPrompts';
import { colors, spacing, radius } from '../theme';

function fmtDate(ts: number): string {
  return new Date(ts).toLocaleDateString('en-US', { month: 'short', day: 'numeric' });
}
const todayStr = () => new Date().toISOString().slice(0, 10);

export default function DiscipleshipScreen() {
  const navigation = useNavigation<any>();

  const enabled            = useAppStore(s => s.discipleshipEnabled);
  const enableDiscipleship = useAppStore(s => s.enableDiscipleship);
  const examenEntries      = useAppStore(s => s.examenEntries);
  const addExamenReflection = useAppStore(s => s.addExamenReflection);
  const deleteExamenEntry  = useAppStore(s => s.deleteExamenEntry);
  const fruitRatings       = useAppStore(s => s.fruitRatings);
  const setFruitRating     = useAppStore(s => s.setFruitRating);
  const fruitGardenHidden  = useAppStore(s => s.fruitGardenHidden);
  const toggleFruitGarden  = useAppStore(s => s.toggleFruitGarden);
  const ruleItems          = useAppStore(s => s.ruleItems);
  const addRuleItem        = useAppStore(s => s.addRuleItem);
  const removeRuleItem     = useAppStore(s => s.removeRuleItem);
  const toggleRuleDoneToday = useAppStore(s => s.toggleRuleDoneToday);
  const summary            = useAppStore(s => s.discipleshipSummary);
  const summaryLoading     = useAppStore(s => s.discipleshipSummaryLoading);
  const refreshSummary     = useAppStore(s => s.refreshDiscipleshipSummary);

  // Today's examen: a chosen quality + a prompt for it. Rotates on tap.
  const [qKey,    setQKey]    = useState<TraitKey>(QUALITIES[0].key);
  const [prompt,  setPrompt]  = useState<string>(() => promptFor(QUALITIES[0].key));
  const [draft,   setDraft]   = useState('');
  const [saving,  setSaving]  = useState(false);
  const [justKept, setJustKept] = useState(false);   // warm moment right after a save
  const [ruleDraft, setRuleDraft] = useState('');

  // Today's word — scripture for the chosen quality, stable through the day.
  const verse = verseFor(qKey);

  function pickQuality(key: TraitKey) {
    setQKey(key);
    setPrompt(promptFor(key));
  }
  function newPrompt() { setPrompt(promptFor(qKey, prompt)); }

  async function saveReflection() {
    const text = draft.trim();
    if (!text || saving) return;
    setSaving(true);
    await addExamenReflection(qKey, prompt, text);
    setDraft('');
    setSaving(false);
    setJustKept(true);   // stays until they begin something new — a moment, not a timer
  }

  // ── Not opted in yet: a warm, pressure-free invitation ──────────────────────
  if (!enabled) {
    return (
      <SafeAreaView style={styles.safe} edges={['top', 'left', 'right']}>
        <StatusBar style="light" />
        <Header onBack={() => navigation.goBack()} />
        <ScrollView contentContainerStyle={styles.introWrap} showsVerticalScrollIndicator={false}>
          <Text style={styles.introTitle}>A private place to walk with Christ</Text>
          <Text style={styles.introBody}>
            This is just for you — a quiet companion to help you notice how Christ is at
            work in your actual life. No scores, no streaks, no one watching. Only
            reflection, a little scripture, and grace.
          </Text>
          <Text style={styles.introBody}>
            Write a short examen each day, keep a private timeline of your walk, tend a
            few personal rhythms — whatever helps you keep your eyes on Him. You can turn
            it off anytime, and nothing here ever affects the rest of the app.
          </Text>
          <TouchableOpacity style={styles.primaryBtn} activeOpacity={0.85} onPress={enableDiscipleship}>
            <Text style={styles.primaryBtnText}>Turn on my reflection companion</Text>
          </TouchableOpacity>
        </ScrollView>
      </SafeAreaView>
    );
  }

  const orderedEntries = [...examenEntries].sort((a, b) => b.ts - a.ts);

  return (
    <SafeAreaView style={styles.safe} edges={['top', 'left', 'right']}>
      <StatusBar style="light" />
      <Header onBack={() => navigation.goBack()} />
      <KeyboardAvoidingView
        style={{ flex: 1 }}
        behavior={Platform.OS === 'ios' ? 'padding' : undefined}
      >
        <ScrollView contentContainerStyle={styles.container} showsVerticalScrollIndicator={false} keyboardShouldPersistTaps="handled">

          {/* ── 1. TODAY'S EXAMEN ─────────────────────────────────────────── */}
          <View style={styles.card}>
            <Text style={styles.sectionLabel}>TODAY'S EXAMEN</Text>

            {/* A word before the questions — the examen is fed by scripture,
                not just prompts. Follows the chosen quality; rotates daily. */}
            <View style={styles.verseBox}>
              <Text style={styles.verseText}>“{verse.text}”</Text>
              <Text style={styles.verseRef}>{verse.ref}</Text>
            </View>

            <Text style={styles.sectionNote}>
              Pick what you'd like to reflect on. There's no right answer — just notice.
            </Text>

            <View style={styles.chipRow}>
              {QUALITIES.map(q => (
                <TouchableOpacity
                  key={q.key}
                  style={[styles.chip, q.key === qKey && styles.chipActive]}
                  activeOpacity={0.8}
                  onPress={() => pickQuality(q.key)}
                >
                  <Text style={[styles.chipText, q.key === qKey && styles.chipTextActive]}>{q.label}</Text>
                </TouchableOpacity>
              ))}
            </View>

            <Text style={styles.promptText}>{prompt}</Text>
            <TouchableOpacity activeOpacity={0.7} onPress={newPrompt}>
              <Text style={styles.subLink}>Another prompt →</Text>
            </TouchableOpacity>

            <TextInput
              style={styles.input}
              value={draft}
              onChangeText={t => { setDraft(t); if (justKept) setJustKept(false); }}
              placeholder="Write as much or as little as you like…"
              placeholderTextColor={colors.textMuted}
              multiline
              textAlignVertical="top"
            />
            <TouchableOpacity
              style={[styles.primaryBtn, (!draft.trim() || saving) && styles.btnDim]}
              activeOpacity={0.85}
              onPress={saveReflection}
              disabled={!draft.trim() || saving}
            >
              {saving
                ? <ActivityIndicator color={colors.onAccent ?? '#0a0f0a'} size="small" />
                : <Text style={styles.primaryBtnText}>Save reflection</Text>}
            </TouchableOpacity>

            {justKept && (
              <Text style={styles.keptNote}>
                Kept. It's part of your walk now — look below in a moment for a word
                spoken back over what you wrote.
              </Text>
            )}
          </View>

          {/* ── 2. MY WALK WITH CHRIST (timeline + narrative summary) ──────── */}
          <View style={styles.card}>
            <Text style={styles.sectionLabel}>MY WALK WITH CHRIST</Text>
            <Text style={styles.sectionNote}>
              A private record of where you've seen Him lately. Ask for a reflection on
              how your walk has been going whenever you'd like.
            </Text>

            {orderedEntries.length > 0 && (
              // A gathering, never a grade: how much walk has been kept here.
              <Text style={styles.walkGlance}>
                {orderedEntries.length} {orderedEntries.length === 1 ? 'reflection' : 'reflections'} kept
                {' · '}walking here since {fmtDate(orderedEntries[orderedEntries.length - 1].ts)}
              </Text>
            )}

            <TouchableOpacity
              style={[styles.secondaryBtn, summaryLoading && styles.btnDim]}
              activeOpacity={0.85}
              onPress={() => { if (!summaryLoading) refreshSummary(); }}
              disabled={summaryLoading}
            >
              {summaryLoading
                ? <ActivityIndicator color={colors.gold} size="small" />
                : <Text style={styles.secondaryBtnText}>
                    {summary ? 'Refresh my walk so far →' : 'See my walk so far →'}
                  </Text>}
            </TouchableOpacity>

            {summary && (
              <View style={styles.summaryBox}>
                <Text style={styles.summaryText}>{summary.text}</Text>
                <Text style={styles.summaryMeta}>Reflection from {fmtDate(summary.ts)}</Text>
              </View>
            )}

            {orderedEntries.length === 0 ? (
              <Text style={styles.emptyNote}>Your reflections will gather here, newest first.</Text>
            ) : (
              orderedEntries.map(e => (
                <View key={e.id} style={styles.entry}>
                  <View style={styles.entryHead}>
                    <Text style={styles.entryQuality}>{QUALITY_BY_KEY[e.quality]?.label ?? 'Reflection'}</Text>
                    <Text style={styles.entryDate}>{fmtDate(e.ts)}</Text>
                  </View>
                  <Text style={styles.entryPrompt}>{e.prompt}</Text>
                  <Text style={styles.entryText}>{e.text}</Text>
                  {!!e.blessing && (
                    <View style={styles.blessingBox}>
                      <Text style={styles.blessingText}>{e.blessing}</Text>
                    </View>
                  )}
                  <TouchableOpacity activeOpacity={0.7} onPress={() => deleteExamenEntry(e.id)}>
                    <Text style={styles.deleteLink}>Remove</Text>
                  </TouchableOpacity>
                </View>
              ))
            )}
          </View>

          {/* ── 3. YOUR FRUIT GARDEN (self-rated, hideable) ────────────────── */}
          <View style={styles.card}>
            <View style={styles.gardenHead}>
              <Text style={styles.sectionLabel}>YOUR FRUIT GARDEN</Text>
              <TouchableOpacity activeOpacity={0.7} onPress={toggleFruitGarden}>
                <Text style={styles.subLink}>{fruitGardenHidden ? 'Show' : 'Hide'}</Text>
              </TouchableOpacity>
            </View>
            {!fruitGardenHidden && (
              <>
                <Text style={styles.sectionNote}>
                  Only you see this. Tap to mark how much each fruit has been growing in you
                  lately — for your own eyes, not a grade. Tap again to clear.
                </Text>
                {QUALITIES.map(q => {
                  const val = fruitRatings[q.key] ?? 0;
                  return (
                    <View key={q.key} style={styles.fruitRow}>
                      <View style={styles.fruitMeta}>
                        <Text style={styles.fruitName}>{q.label}</Text>
                        <Text style={styles.fruitBlurb}>{q.blurb}</Text>
                      </View>
                      <View style={styles.dots}>
                        {[1, 2, 3, 4, 5].map(n => (
                          <TouchableOpacity
                            key={n}
                            activeOpacity={0.7}
                            onPress={() => setFruitRating(q.key, n)}
                            style={[styles.dot, n <= val && styles.dotOn]}
                          />
                        ))}
                      </View>
                    </View>
                  );
                })}
              </>
            )}
          </View>

          {/* ── 4. RULE OF LIFE (personal rhythms) ─────────────────────────── */}
          <View style={styles.card}>
            <Text style={styles.sectionLabel}>RULE OF LIFE</Text>
            <Text style={styles.sectionNote}>
              A few simple rhythms you want to keep — like daily honest prayer, or a weekly
              act of kindness. Mark one done when you do it. Missing a day is no failure;
              just begin again.
            </Text>

            {ruleItems.map(r => {
              const doneToday = r.doneDates.includes(todayStr());
              return (
                <View key={r.id} style={styles.ruleRow}>
                  <TouchableOpacity
                    style={[styles.checkbox, doneToday && styles.checkboxOn]}
                    activeOpacity={0.7}
                    onPress={() => toggleRuleDoneToday(r.id)}
                  >
                    {doneToday && <Text style={styles.checkmark}>✓</Text>}
                  </TouchableOpacity>
                  <View style={styles.ruleMain}>
                    <Text style={styles.ruleText}>{r.text}</Text>
                    {r.doneDates.length > 0 && (
                      <Text style={styles.ruleCount}>
                        Kept {r.doneDates.length} {r.doneDates.length === 1 ? 'time' : 'times'} so far
                      </Text>
                    )}
                  </View>
                  <TouchableOpacity activeOpacity={0.7} onPress={() => removeRuleItem(r.id)}>
                    <Text style={styles.deleteLink}>✕</Text>
                  </TouchableOpacity>
                </View>
              );
            })}

            {ruleItems.length < 4 && (
              <View style={styles.ruleAddRow}>
                <TextInput
                  style={[styles.input, styles.ruleInput]}
                  value={ruleDraft}
                  onChangeText={setRuleDraft}
                  placeholder="Add a rhythm…"
                  placeholderTextColor={colors.textMuted}
                  onSubmitEditing={() => { addRuleItem(ruleDraft); setRuleDraft(''); }}
                  returnKeyType="done"
                />
                <TouchableOpacity
                  style={[styles.addBtn, !ruleDraft.trim() && styles.btnDim]}
                  activeOpacity={0.85}
                  onPress={() => { if (ruleDraft.trim()) { addRuleItem(ruleDraft); setRuleDraft(''); } }}
                  disabled={!ruleDraft.trim()}
                >
                  <Text style={styles.addBtnText}>＋</Text>
                </TouchableOpacity>
              </View>
            )}
            {ruleItems.length >= 4 && (
              <Text style={styles.emptyNote}>Four rhythms is plenty — keep them simple and doable.</Text>
            )}
          </View>

          <Text style={styles.footerNote}>
            Private to you. Nothing here is scored, shared, or used anywhere else in the app.
          </Text>
        </ScrollView>
      </KeyboardAvoidingView>
    </SafeAreaView>
  );
}

function Header({ onBack }: { onBack: () => void }) {
  return (
    <View style={styles.header}>
      <TouchableOpacity activeOpacity={0.7} onPress={onBack} style={styles.backBtn}>
        <Text style={styles.backText}>‹ Back</Text>
      </TouchableOpacity>
      <Text style={styles.headerTitle}>My Discipleship</Text>
      <View style={styles.backBtn} />
    </View>
  );
}

const styles = StyleSheet.create({
  safe: { flex: 1, backgroundColor: colors.bg },
  header: {
    flexDirection: 'row', alignItems: 'center', justifyContent: 'space-between',
    paddingHorizontal: spacing.md, paddingTop: spacing.sm, paddingBottom: spacing.sm,
    borderBottomWidth: 1, borderBottomColor: colors.borderDim,
  },
  backBtn: { minWidth: 56 },
  backText: { color: colors.textDim, fontSize: 14, fontFamily: 'Jost_400Regular' },
  headerTitle: { fontSize: 18, fontFamily: 'Jost_400Regular', color: colors.textMid },

  introWrap: { padding: spacing.lg, gap: spacing.md },
  introTitle: { fontSize: 22, fontFamily: 'Jost_400Regular', color: '#e8e0c8', lineHeight: 30, marginBottom: spacing.xs },
  introBody: { fontSize: 14, fontFamily: 'Jost_400Regular', color: colors.textDim, lineHeight: 22 },

  container: { padding: spacing.md, paddingBottom: spacing.xl },
  card: {
    backgroundColor: colors.bgCard, borderWidth: 1, borderColor: colors.border,
    borderRadius: radius.md, padding: spacing.md, marginBottom: spacing.sm + 4,
  },
  sectionLabel: {
    fontSize: 11, color: colors.textMuted, letterSpacing: 1.4,
    textTransform: 'uppercase', fontFamily: 'Jost_400Regular', marginBottom: 6,
  },
  sectionNote: { fontSize: 13, color: colors.textDim, fontFamily: 'Jost_400Regular', lineHeight: 20, marginBottom: spacing.sm },

  chipRow: { flexDirection: 'row', flexWrap: 'wrap', gap: 6, marginBottom: spacing.sm },
  chip: { borderWidth: 1, borderColor: colors.borderDim, borderRadius: 14, paddingVertical: 5, paddingHorizontal: 11 },
  chipActive: { borderColor: colors.gold, backgroundColor: (colors.gold ?? '#caa75a') + '1c' },
  chipText: { fontSize: 12, color: colors.textDim, fontFamily: 'Jost_400Regular' },
  chipTextActive: { color: colors.gold },

  // Today's word — a quiet setting for the scripture that opens the examen.
  verseBox: {
    borderLeftWidth: 2, borderLeftColor: colors.gold, paddingLeft: spacing.sm + 2,
    marginBottom: spacing.sm, marginTop: 2,
  },
  verseText: { fontSize: 15, color: '#e8e0c8', fontFamily: 'Jost_400Regular', fontStyle: 'italic', lineHeight: 23 },
  verseRef:  { fontSize: 11, color: colors.gold, fontFamily: 'Jost_400Regular', letterSpacing: 0.6, marginTop: 4 },

  // The warm moment after a reflection is saved.
  keptNote: {
    fontSize: 12, color: colors.gold, fontFamily: 'Jost_400Regular', fontStyle: 'italic',
    lineHeight: 18, textAlign: 'center', marginTop: spacing.sm,
  },

  // The gathering line — how much walk is kept here. A record, never a score.
  walkGlance: {
    fontSize: 12, color: colors.gold, fontFamily: 'Jost_400Regular',
    letterSpacing: 0.4, marginBottom: spacing.sm,
  },

  promptText: { fontSize: 15, color: '#e0d8c0', fontFamily: 'Jost_400Regular', lineHeight: 23, marginBottom: 4 },
  subLink: { color: colors.blue, fontSize: 12, fontStyle: 'italic', fontFamily: 'Jost_400Regular', marginTop: 2 },

  input: {
    borderWidth: 1, borderColor: '#1e1c18', borderRadius: 6, backgroundColor: colors.bgInput,
    color: '#d0c8b0', fontSize: 14, fontFamily: 'Jost_400Regular', padding: spacing.sm,
    minHeight: 90, marginTop: spacing.sm, marginBottom: spacing.sm, lineHeight: 21,
  },
  primaryBtn: {
    backgroundColor: colors.gold, borderRadius: radius.md, paddingVertical: 12,
    alignItems: 'center', justifyContent: 'center',
  },
  primaryBtnText: { color: '#0a0f0a', fontSize: 14, fontFamily: 'Jost_400Regular' },
  secondaryBtn: {
    borderWidth: 1, borderColor: colors.gold, borderRadius: radius.md, paddingVertical: 10,
    alignItems: 'center', justifyContent: 'center', marginBottom: spacing.sm,
  },
  secondaryBtnText: { color: colors.gold, fontSize: 13, fontFamily: 'Jost_400Regular' },
  btnDim: { opacity: 0.5 },

  summaryBox: {
    borderLeftWidth: 2, borderLeftColor: colors.gold, paddingLeft: spacing.sm + 2,
    marginBottom: spacing.sm,
  },
  summaryText: { fontSize: 14, color: '#ded6be', fontFamily: 'Jost_400Regular', lineHeight: 23 },
  summaryMeta: { fontSize: 10, color: colors.textMuted, fontFamily: 'Jost_400Regular', marginTop: 4 },

  emptyNote: { fontSize: 13, color: colors.textMuted, fontStyle: 'italic', fontFamily: 'Jost_400Regular', marginTop: 4 },

  entry: { borderTopWidth: 1, borderTopColor: colors.borderDim, paddingTop: spacing.sm, marginTop: spacing.sm },
  entryHead: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', marginBottom: 4 },
  entryQuality: { fontSize: 11, color: colors.gold, letterSpacing: 0.6, textTransform: 'uppercase', fontFamily: 'Jost_400Regular' },
  entryDate: { fontSize: 11, color: colors.textMuted, fontFamily: 'Jost_400Regular' },
  entryPrompt: { fontSize: 12, color: colors.textMuted, fontStyle: 'italic', fontFamily: 'Jost_400Regular', lineHeight: 18, marginBottom: 4 },
  entryText: { fontSize: 14, color: '#d0c8b0', fontFamily: 'Jost_400Regular', lineHeight: 21 },
  blessingBox: { borderLeftWidth: 2, borderLeftColor: colors.blue, paddingLeft: spacing.sm, marginTop: 8 },
  blessingText: { fontSize: 13, color: colors.blue, fontStyle: 'italic', fontFamily: 'Jost_400Regular', lineHeight: 20 },
  deleteLink: { fontSize: 11, color: colors.textMuted, fontFamily: 'Jost_400Regular', marginTop: 8 },

  gardenHead: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center' },
  fruitRow: { flexDirection: 'row', alignItems: 'center', justifyContent: 'space-between', marginTop: spacing.sm },
  fruitMeta: { flex: 1, paddingRight: spacing.sm },
  fruitName: { fontSize: 14, color: '#e0d8c0', fontFamily: 'Jost_400Regular' },
  fruitBlurb: { fontSize: 11, color: colors.textMuted, fontFamily: 'Jost_400Regular', lineHeight: 16 },
  dots: { flexDirection: 'row', gap: 6, alignItems: 'center' },
  dot: { width: 16, height: 16, borderRadius: 8, borderWidth: 1, borderColor: colors.borderDim },
  dotOn: { backgroundColor: colors.gold, borderColor: colors.gold },

  ruleRow: { flexDirection: 'row', alignItems: 'center', marginTop: spacing.sm },
  checkbox: {
    width: 24, height: 24, borderRadius: 6, borderWidth: 1, borderColor: colors.borderDim,
    alignItems: 'center', justifyContent: 'center', marginRight: spacing.sm,
  },
  checkboxOn: { backgroundColor: colors.gold, borderColor: colors.gold },
  checkmark: { color: '#0a0f0a', fontSize: 14 },
  ruleMain: { flex: 1 },
  ruleText: { fontSize: 14, color: '#d8d0b8', fontFamily: 'Jost_400Regular' },
  ruleCount: { fontSize: 11, color: colors.textMuted, fontFamily: 'Jost_400Regular' },
  ruleAddRow: { flexDirection: 'row', alignItems: 'center', gap: spacing.sm },
  ruleInput: { flex: 1, minHeight: 44 },
  addBtn: {
    width: 44, height: 44, borderRadius: radius.md, backgroundColor: colors.gold,
    alignItems: 'center', justifyContent: 'center', marginTop: spacing.sm, marginBottom: spacing.sm,
  },
  addBtnText: { color: '#0a0f0a', fontSize: 20 },

  footerNote: { fontSize: 11, color: colors.textMuted, fontStyle: 'italic', fontFamily: 'Jost_400Regular', textAlign: 'center', marginTop: spacing.xs },
});
