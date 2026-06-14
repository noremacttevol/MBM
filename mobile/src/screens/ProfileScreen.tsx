/**
 * ProfileScreen — a mirror of the person's own words + their growing virtues.
 *
 * Owner amendments (Law 4): routing state — the feed track, the milk gate, the
 * count of active signals — is OWNER-ONLY, forever. None of it appears here.
 * What the person sees is theirs: what we sense about them, the virtues growing
 * in them, their faith in their own words, and the story they have told so far.
 */

import React, { useState } from 'react';
import {
  View,
  Text,
  TextInput,
  ScrollView,
  TouchableOpacity,
  StyleSheet,
  KeyboardAvoidingView,
  Platform,
} from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { StatusBar } from 'expo-status-bar';
import { useNavigation } from '@react-navigation/native';
import { useAppStore, isMemberSignal } from '../store/useAppStore';
import { TraitKey } from '../data/questionBank';
import { christlikeCap } from '../engine/connect';
import { colors, spacing, radius } from '../theme';

// The settled standard: every dimension is named as a CHRISTLIKE measure, so the
// label always matches what the number means — "how close to Christ's own," never
// a bare verdict on whether someone is a good person. This is the rename that makes
// the scale honest. Keep the "Christlike" prefix on every one.
const TRAIT_LABELS: Record<TraitKey, string> = {
  honest_inquiry: 'Christlike Honesty',
  openness:       'Christlike Openness',
  humility:       'Christlike Humility',
  hunger:         'Christlike Hunger for Truth',
  compassion:     'Christlike Compassion',
  courage:        'Christlike Courage',
  sincerity:      'Christlike Sincerity',
};

const TRAIT_DESCRIPTIONS: Record<TraitKey, string> = {
  honest_inquiry: "How fully your honesty reflects Christ's own — sitting with hard questions in truth",
  openness:       "How fully your openness reflects Christ's own — receptive to what God might reveal",
  humility:       "How fully your humility reflects Christ's own — holding your certainties loosely",
  hunger:         "How fully your hunger for truth reflects Christ's own — longing for the fullness He offers",
  compassion:     "How fully your compassion reflects Christ's own — feeling what others carry",
  courage:        "How fully your courage reflects Christ's own — facing and saying the true thing",
  sincerity:      "How fully your sincerity reflects Christ's own — your heart and your life in one",
};

const TRAIT_ORDER: TraitKey[] = [
  'hunger', 'sincerity', 'openness', 'honest_inquiry',
  'courage', 'humility', 'compassion',
];

function interpretTraits(scores: Record<TraitKey, number>, feedTag: string): string {
  const hunger    = scores.hunger ?? 0;
  const sincerity = scores.sincerity ?? 0;
  const courage   = scores.courage ?? 0;
  const openness  = scores.openness ?? 0;
  const humility  = scores.humility ?? 0;

  const dominant = TRAIT_ORDER
    .map(k => ({ key: k, val: scores[k] ?? 0 }))
    .sort((a, b) => b.val - a.val)
    .slice(0, 2)
    .map(t => TRAIT_LABELS[t.key].toLowerCase());

  // Internal routing context only — the tag name is NEVER shown to the person.
  const tagContext: Record<string, string> = {
    MILK:        'You seem to be someone who has felt something — in a quiet moment, in a loss, in the way beauty sometimes arrives uninvited.',
    BRIDGE:      'You carry real questions and you take them seriously. That kind of honesty is rarer than it looks.',
    RESTORATION: 'Something in the story of the restoration has caught your attention. That is worth following.',
    MAINTENANCE: 'You have covenants you are trying to keep. The fact that you are still here, still asking — that means something.',
  };

  const opening = tagContext[feedTag] ?? tagContext['MILK'];

  const traitLine = dominant.length >= 2
    ? `What stands out most is your ${dominant[0]} and your ${dominant[1]}.`
    : `What stands out most is your ${dominant[0]}.`;

  let closing = '';
  if (hunger >= 7) {
    closing = "You are looking for something real. That longing is not accidental.";
  } else if (sincerity >= 7) {
    closing = "You mean what you say. That kind of sincerity is what genuine faith is built on.";
  } else if (courage >= 7) {
    closing = "You are willing to face things most people avoid. Keep going.";
  } else if (openness >= 7) {
    closing = "You are staying open even when it would be easier to close. That matters.";
  } else if (humility >= 7) {
    closing = "You hold your certainties loosely. That is exactly the posture faith requires.";
  } else {
    closing = "You are still here, still asking. That is enough to start with.";
  }

  return `${opening} ${traitLine} ${closing}`;
}

// "A faith you grew up in…" — describes their faith from signals WITHOUT ever
// naming a track or a category to them. Member self-ID is honored, in their words.
// ── The faith-background ladder (the binding standard, Track 1) ──────────────
// An honest, transparent description of where a person stands in BELIEF — shown to
// them, explained, and counting NO ONE out. It is never a verdict on worth; it just
// names, respectfully, the path they're on. It climbs on real steps the person
// takes (accepting the invitation → investigator; telling us they're a member).
type FaithRung =
  | 'TAKING_SHAPE' | 'ATHEIST' | 'AGNOSTIC' | 'OTHER_FAITH'
  | 'JESUS_BELIEVER' | 'INVESTIGATOR' | 'MEMBER' | 'MEAT';

const FAITH_LADDER: { key: FaithRung; label: string; blurb: string }[] = [
  { key: 'ATHEIST',        label: 'Not yet sure God is there',       blurb: 'Honest about the doubt — welcome exactly as you are.' },
  { key: 'AGNOSTIC',       label: 'Open, but unsure',                blurb: 'Holding the question gently. No rush.' },
  { key: 'OTHER_FAITH',    label: 'Walking another path of faith',   blurb: 'Honored — there is real light in where you are.' },
  { key: 'JESUS_BELIEVER', label: 'A believer in Jesus',            blurb: 'Christ at the center — churched or not.' },
  { key: 'INVESTIGATOR',   label: 'A friend of the restored gospel', blurb: 'You opened the door to learn more. Glad to walk it with you.' },
  { key: 'MEMBER',         label: 'A Latter-day Saint',              blurb: 'You told us yourself.' },
  { key: 'MEAT',           label: 'Growing deep in the gospel',      blurb: 'Pressing toward the fullness, together.' },
];

function faithRung(signals: string[], faithText: string): FaithRung {
  if (isMemberSignal(signals)) return 'MEMBER';
  if (signals.includes('curious_about_book_of_mormon') ||
      signals.includes('wants_to_join') ||
      signals.includes('asking_how_to_belong')) return 'INVESTIGATOR';
  if (signals.includes('believes_in_jesus') ||
      /\b(jesus|christ|christian|baptist|catholic|methodist|presbyterian|pentecostal|evangelical|lutheran|orthodox)\b/.test(faithText)) return 'JESUS_BELIEVER';
  if (/\b(muslim|islam|hindu|jewish|judaism|buddhist|sikh)\b/.test(faithText)) return 'OTHER_FAITH';
  if (/\bagnostic\b/.test(faithText)) return 'AGNOSTIC';
  if (/\batheist\b/.test(faithText) || signals.includes('skeptical_of_god')) return 'ATHEIST';
  return 'TAKING_SHAPE';
}

function fmtDate(ts: number): string {
  return new Date(ts).toLocaleDateString('en-US', { month: 'short', day: 'numeric' });
}

export default function ProfileScreen() {
  const traitScores         = useAppStore(s => s.traitScores);
  const feedTag             = useAppStore(s => s.feedTag);
  const openedIds           = useAppStore(s => s.openedIds);
  const answeredQuestionIds = useAppStore(s => s.answeredQuestionIds);
  const journalEntries      = useAppStore(s => s.journalEntries);
  const dialogueSignals     = useAppStore(s => s.dialogueSignals);
  const faithWords          = useAppStore(s => s.faithWords);
  const moments             = useAppStore(s => s.moments);
  const prefillChat         = useAppStore(s => s.prefillChat);
  const editFaithWord       = useAppStore(s => s.editFaithWord);
  const addFaithWord        = useAppStore(s => s.addFaithWord);

  const navigation = useNavigation<any>();

  // Editable faith — Law 4: anything we collect and show, a person can change anytime.
  const [editingIndex, setEditingIndex] = useState<number | null>(null);
  const [editDraft,    setEditDraft]    = useState('');
  const [adding,       setAdding]       = useState(false);
  const [addDraft,     setAddDraft]     = useState('');

  const interpretation = interpretTraits(traitScores, feedTag);
  // The Christlike ceiling: the score shown is never above what the person has
  // earned the right to reach by where they stand toward the restored gospel's God.
  // The raw climb is kept underneath (it drives the readiness gate); this only
  // bounds what's displayed, so the number and the "Christlike" label always agree.
  const christlikeCeiling = christlikeCap(dialogueSignals);
  // The faith-background ladder: where they stand in belief, named honestly and
  // shown to them, climbing on real steps they take. Counts no one out.
  const faithText   = faithWords.map(w => w.text).join(' ').toLowerCase();
  const currentRung = faithRung(dialogueSignals, faithText);
  const currentRungInfo = FAITH_LADDER.find(r => r.key === currentRung);

  function askAbout(title: string, detail?: string) {
    const what = (detail && detail.trim()) ? detail.trim() : title;
    prefillChat(
      `Earlier in my story I shared this: “${what}”. Can we talk about it — what do you make of it, and what would you ask me about it?`,
    );
    navigation.navigate('Chat');
  }

  function talkAboutTrait(key: TraitKey) {
    const label = TRAIT_LABELS[key].toLowerCase();
    const score = Math.min(traitScores[key] ?? 0, christlikeCeiling).toFixed(1);
    prefillChat(
      `My ${label} level is at ${score} out of 10. Be honest with me — what have you seen in me that put it there, and what would actually help it grow?`,
    );
    navigation.navigate('Chat');
  }

  function startEdit(index: number, current: string) {
    setEditingIndex(index);
    setEditDraft(current);
    setAdding(false);
  }

  function saveEdit() {
    if (editingIndex === null) return;
    editFaithWord(editingIndex, editDraft);
    setEditingIndex(null);
    setEditDraft('');
  }

  function cancelEdit() {
    setEditingIndex(null);
    setEditDraft('');
  }

  function removeEntry(index: number) {
    // Saving an empty string removes the entry (store handles the splice).
    editFaithWord(index, '');
    if (editingIndex === index) cancelEdit();
  }

  function saveAdd() {
    if (!addDraft.trim()) { setAdding(false); setAddDraft(''); return; }
    addFaithWord(addDraft);
    setAdding(false);
    setAddDraft('');
  }

  return (
    <SafeAreaView style={styles.safe} edges={['top', 'left', 'right']}>
      <StatusBar style="light" />

      <KeyboardAvoidingView
        style={{ flex: 1 }}
        behavior={Platform.OS === 'ios' ? 'padding' : 'height'}
      >
      <ScrollView
        style={styles.scroll}
        contentContainerStyle={styles.container}
        showsVerticalScrollIndicator={false}
        keyboardShouldPersistTaps="handled"
      >
        <Text style={styles.header}>Your journey</Text>

        {/* ── WHAT WE SENSE ABOUT YOU ─────────────────────────────────── */}
        <View style={styles.card}>
          <Text style={styles.sectionLabel}>WHAT WE SENSE ABOUT YOU</Text>
          <Text style={styles.interpretText}>{interpretation}</Text>
        </View>

        {/* ── YOUR FAITH, AS YOU'VE TOLD IT ───────────────────────────── */}
        {/* Always editable — a person can fix a typo or add context anytime. */}
        <View style={styles.card}>
          <Text style={styles.sectionLabel}>YOUR FAITH, AS YOU'VE TOLD IT</Text>
          <Text style={styles.faithStatus}>
            {currentRungInfo ? currentRungInfo.label : 'Still taking shape — in your words below.'}
          </Text>
          {currentRungInfo && (
            <Text style={styles.interpretText}>{currentRungInfo.blurb}</Text>
          )}
          {/* The ladder, shown openly — where this can grow, counting no one out. */}
          <View style={{ marginTop: spacing.sm, marginBottom: spacing.xs }}>
            {FAITH_LADDER.map(r => {
              const here = r.key === currentRung;
              return (
                <Text
                  key={r.key}
                  style={{
                    color: here ? colors.gold : colors.textMuted,
                    fontWeight: here ? '700' : '400',
                    fontSize: 13,
                    paddingVertical: 1,
                  }}
                >
                  {here ? '› ' : '    '}{r.label}
                </Text>
              );
            })}
          </View>

          {faithWords.map((w, i) => (
            <View key={`${w.ts}-${i}`} style={styles.faithRow}>
              {editingIndex === i ? (
                <>
                  <TextInput
                    style={styles.faithInput}
                    value={editDraft}
                    onChangeText={setEditDraft}
                    placeholder="In your own words…"
                    placeholderTextColor={colors.textMuted}
                    multiline
                    autoFocus
                    maxLength={140}
                  />
                  <View style={styles.editActions}>
                    <TouchableOpacity activeOpacity={0.7} onPress={saveEdit}>
                      <Text style={styles.editSave}>Save</Text>
                    </TouchableOpacity>
                    <TouchableOpacity activeOpacity={0.7} onPress={cancelEdit}>
                      <Text style={styles.editCancel}>Cancel</Text>
                    </TouchableOpacity>
                    <TouchableOpacity activeOpacity={0.7} onPress={() => removeEntry(i)}>
                      <Text style={styles.editRemove}>Remove</Text>
                    </TouchableOpacity>
                  </View>
                </>
              ) : (
                <TouchableOpacity activeOpacity={0.7} onPress={() => startEdit(i, w.text)}>
                  <Text style={styles.faithWordText}>"{w.text}"</Text>
                  <View style={styles.faithRowFoot}>
                    <Text style={styles.faithWordDate}>{fmtDate(w.ts)}</Text>
                    <Text style={styles.faithEditHint}>Edit →</Text>
                  </View>
                </TouchableOpacity>
              )}
            </View>
          ))}

          {/* Add another in-their-words entry */}
          {adding ? (
            <View style={styles.faithRow}>
              <TextInput
                style={styles.faithInput}
                value={addDraft}
                onChangeText={setAddDraft}
                placeholder="Add more about your faith, in your own words…"
                placeholderTextColor={colors.textMuted}
                multiline
                autoFocus
                maxLength={140}
              />
              <View style={styles.editActions}>
                <TouchableOpacity activeOpacity={0.7} onPress={saveAdd}>
                  <Text style={styles.editSave}>Save</Text>
                </TouchableOpacity>
                <TouchableOpacity
                  activeOpacity={0.7}
                  onPress={() => { setAdding(false); setAddDraft(''); }}
                >
                  <Text style={styles.editCancel}>Cancel</Text>
                </TouchableOpacity>
              </View>
            </View>
          ) : (
            <TouchableOpacity
              activeOpacity={0.7}
              style={styles.addFaithBtn}
              onPress={() => { setAdding(true); setEditingIndex(null); }}
            >
              <Text style={styles.addFaithText}>+ Add more in your own words</Text>
            </TouchableOpacity>
          )}
        </View>

        {/* ── WHAT'S GROWING IN YOU (the virtues belong to the person) ─── */}
        <View style={styles.card}>
          <Text style={styles.sectionLabel}>WHAT'S GROWING IN YOU</Text>
          <Text style={styles.sectionNote}>
            An honest reading of your heart, the way Jesus saw people truly. These rise when you show real honesty, humility, or courage — and they can dip too. Tap any one to talk it through.
          </Text>

          {TRAIT_ORDER.map(key => {
            const score = Math.min(traitScores[key] ?? 0, christlikeCeiling);
            const pct   = Math.round((score / 10) * 100);
            return (
              <View key={key} style={styles.traitRow}>
                <View style={styles.traitMeta}>
                  <Text style={styles.traitName}>{TRAIT_LABELS[key]}</Text>
                  <Text style={styles.traitDesc}>{TRAIT_DESCRIPTIONS[key]}</Text>
                  <TouchableOpacity activeOpacity={0.7} onPress={() => talkAboutTrait(key)}>
                    <Text style={styles.askText}>Talk about this →</Text>
                  </TouchableOpacity>
                </View>
                <View style={styles.barTrack}>
                  <View style={[styles.barFill, { width: `${pct}%` as any }]} />
                </View>
                <Text style={styles.traitScore}>{score.toFixed(1)}</Text>
              </View>
            );
          })}
        </View>

        {/* ── YOUR STORY SO FAR ───────────────────────────────────────── */}
        {moments.length > 0 && (
          <View style={styles.card}>
            <Text style={styles.sectionLabel}>YOUR STORY SO FAR</Text>
            <Text style={styles.sectionNote}>
              Every step you've taken here, kept for you. Ask about any of them.
            </Text>
            {moments.map((m, i) => (
              <View key={`${m.ts}-${i}`} style={styles.momentRow}>
                <View style={styles.momentHead}>
                  <Text style={styles.momentTitle}>{m.title}</Text>
                  <Text style={styles.momentDate}>{fmtDate(m.ts)}</Text>
                </View>
                <Text style={styles.momentDetail}>{m.text}</Text>
                <TouchableOpacity activeOpacity={0.7} onPress={() => askAbout(m.title, m.text)}>
                  <Text style={styles.askText}>Ask about this →</Text>
                </TouchableOpacity>
              </View>
            ))}
          </View>
        )}

        {/* ── Session stats ───────────────────────────────────────────── */}
        <View style={styles.statsRow}>
          <View style={styles.statCard}>
            <Text style={styles.statValue}>{openedIds.size}</Text>
            <Text style={styles.statLabel}>Articles opened</Text>
          </View>
          <View style={styles.statCard}>
            <Text style={styles.statValue}>{answeredQuestionIds.length}</Text>
            <Text style={styles.statLabel}>Questions answered</Text>
          </View>
          <View style={styles.statCard}>
            <Text style={styles.statValue}>{journalEntries.length}</Text>
            <Text style={styles.statLabel}>Journal entries</Text>
          </View>
        </View>

        {/* ── Footer note ─────────────────────────────────────────────── */}
        <Text style={styles.footerNote}>
          This profile is private and lives only on your device.
          It exists to serve you, not to route you like a package.
        </Text>

        <View style={{ height: spacing.xl }} />
      </ScrollView>
      </KeyboardAvoidingView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safe: {
    flex:            1,
    backgroundColor: colors.bg,
  },
  scroll: { flex: 1 },
  container: {
    paddingHorizontal: spacing.md,
    paddingTop:        spacing.lg,
    paddingBottom:     spacing.xxl,
  },

  header: {
    fontSize:     22,
    fontFamily:   'Georgia',
    color:        colors.textMid,
    marginBottom: spacing.lg,
  },

  card: {
    borderWidth:     1,
    borderColor:     colors.borderDim,
    backgroundColor: colors.bgCard,
    borderRadius:    radius.lg,
    padding:         spacing.md,
    marginBottom:    spacing.md,
  },
  sectionLabel: {
    fontSize:      10,
    letterSpacing: 1.5,
    color:         colors.textMuted,
    fontFamily:    'Georgia',
    marginBottom:  spacing.sm,
  },
  sectionNote: {
    fontSize:     11,
    fontFamily:   'Georgia',
    fontStyle:    'italic',
    color:        colors.textMuted,
    lineHeight:   17,
    marginBottom: spacing.md,
  },
  interpretText: {
    fontSize:   15,
    fontFamily: 'Georgia',
    color:      colors.textDim,
    lineHeight: 24,
    fontStyle:  'italic',
  },

  faithStatus: {
    fontSize:     14,
    fontFamily:   'Georgia',
    color:        colors.textMid,
    lineHeight:   22,
    marginBottom: spacing.sm,
  },
  faithRow: {
    borderTopWidth: 1,
    borderTopColor: colors.border,
    paddingVertical: spacing.sm,
  },
  faithWordText: {
    fontSize:   13,
    fontFamily: 'Georgia',
    color:      colors.textDim,
    lineHeight: 20,
    fontStyle:  'italic',
  },
  faithWordDate: {
    fontSize:  10,
    fontFamily: 'Georgia',
    color:     colors.textMuted,
    marginTop: 2,
  },
  faithRowFoot: {
    flexDirection:  'row',
    justifyContent: 'space-between',
    alignItems:     'center',
    marginTop:      2,
  },
  faithEditHint: {
    fontSize:   10,
    fontFamily: 'Georgia',
    fontStyle:  'italic',
    color:      colors.blue,
  },
  faithInput: {
    borderWidth:     1,
    borderColor:     colors.border,
    borderRadius:    radius.sm,
    backgroundColor: colors.bgInput,
    color:           colors.text,
    fontFamily:      'Georgia',
    fontSize:        13,
    lineHeight:      20,
    padding:         spacing.sm,
    minHeight:       60,
    textAlignVertical: 'top',
  },
  editActions: {
    flexDirection: 'row',
    gap:           spacing.md,
    marginTop:     spacing.sm,
  },
  editSave: {
    fontSize:   12,
    fontFamily: 'Georgia',
    color:      colors.gold,
  },
  editCancel: {
    fontSize:   12,
    fontFamily: 'Georgia',
    color:      colors.textMuted,
  },
  editRemove: {
    fontSize:   12,
    fontFamily: 'Georgia',
    color:      colors.textMuted,
    marginLeft: 'auto',
  },
  addFaithBtn: {
    borderTopWidth:  1,
    borderTopColor:  colors.border,
    paddingTop:      spacing.sm,
    marginTop:       spacing.xs,
  },
  addFaithText: {
    fontSize:   12,
    fontFamily: 'Georgia',
    fontStyle:  'italic',
    color:      colors.blue,
  },

  traitRow: {
    flexDirection: 'row',
    alignItems:    'center',
    marginBottom:  spacing.sm + 2,
    gap:           spacing.sm,
  },
  traitMeta: { width: 110 },
  traitName: {
    fontSize:   12,
    fontFamily: 'Georgia',
    color:      colors.textMid,
    lineHeight: 16,
  },
  traitDesc: {
    fontSize:   10,
    fontFamily: 'Georgia',
    color:      colors.textMuted,
    lineHeight: 14,
  },
  barTrack: {
    flex:            1,
    height:          4,
    backgroundColor: colors.border,
    borderRadius:    2,
    overflow:        'hidden',
  },
  barFill: {
    height:          4,
    backgroundColor: colors.gold,
    borderRadius:    2,
  },
  traitScore: {
    fontSize:   11,
    fontFamily: 'Georgia',
    color:      colors.textMuted,
    width:      28,
    textAlign:  'right',
  },

  momentRow: {
    borderTopWidth:  1,
    borderTopColor:  colors.border,
    paddingVertical: spacing.sm + 4,
  },
  momentHead: {
    flexDirection:  'row',
    justifyContent: 'space-between',
    gap:            spacing.sm,
    marginBottom:   spacing.xs,
  },
  momentTitle: {
    flex:       1,
    fontSize:   13,
    fontFamily: 'Georgia',
    color:      colors.textMid,
    lineHeight: 19,
  },
  momentDate: {
    fontSize:  10,
    fontFamily: 'Georgia',
    color:     colors.textMuted,
    paddingTop: 3,
  },
  momentDetail: {
    fontSize:   12,
    fontFamily: 'Georgia',
    color:      colors.textDim,
    lineHeight: 18,
    fontStyle:  'italic',
    marginBottom: 6,
  },
  askText: {
    fontSize:   11,
    fontFamily: 'Georgia',
    fontStyle:  'italic',
    color:      colors.blue,
  },

  statsRow: {
    flexDirection: 'row',
    gap:           spacing.sm,
    marginBottom:  spacing.md,
  },
  statCard: {
    flex:            1,
    borderWidth:     1,
    borderColor:     colors.borderDim,
    backgroundColor: colors.bgCard,
    borderRadius:    radius.md,
    padding:         spacing.sm,
    alignItems:      'center',
  },
  statValue: {
    fontSize:     22,
    fontFamily:   'Georgia',
    color:        colors.gold,
    marginBottom: 2,
  },
  statLabel: {
    fontSize:   10,
    fontFamily: 'Georgia',
    color:      colors.textMuted,
    textAlign:  'center',
  },

  footerNote: {
    fontSize:   12,
    fontFamily: 'Georgia',
    fontStyle:  'italic',
    color:      colors.textMuted,
    textAlign:  'center',
    lineHeight: 18,
    paddingHorizontal: spacing.md,
    marginTop:  spacing.md,
  },
});
