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
import { colors, spacing, radius } from '../theme';

const TRAIT_LABELS: Record<TraitKey, string> = {
  honest_inquiry: 'Honest Inquiry',
  openness:       'Openness',
  humility:       'Humility',
  hunger:         'Hunger',
  compassion:     'Compassion',
  courage:        'Courage',
  sincerity:      'Sincerity',
};

const TRAIT_DESCRIPTIONS: Record<TraitKey, string> = {
  honest_inquiry: 'Willingness to sit with hard questions',
  openness:       'Receptivity to what you might not expect',
  humility:       'Ability to hold your certainties loosely',
  hunger:         'Longing for something more than what you have',
  compassion:     'Capacity to feel what others carry',
  courage:        'Willingness to say and face the true thing',
  sincerity:      'Alignment between what you feel and what you do',
};

const TRAIT_ORDER: TraitKey[] = [
  'hunger', 'sincerity', 'openness', 'honest_inquiry',
  'courage', 'humility', 'compassion',
];

function interpretTraits(scores: Record<TraitKey, number>, feedTag: string): string {
  const hunger    = scores.hunger ?? 5;
  const sincerity = scores.sincerity ?? 5;
  const courage   = scores.courage ?? 5;
  const openness  = scores.openness ?? 5;
  const humility  = scores.humility ?? 5;

  const dominant = TRAIT_ORDER
    .map(k => ({ key: k, val: scores[k] ?? 5 }))
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
function faithStatusLine(signals: string[]): string {
  if (isMemberSignal(signals)) return 'A Latter-day Saint — you told us yourself.';
  if (signals.includes('active_faith_tradition')) return 'Part of a faith community today — in your words below.';
  if (signals.includes('has_history_with_faith')) return 'A faith you grew up in, at some distance now — in your words below.';
  return 'Still taking shape — in your words below.';
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

  function askAbout(title: string) {
    prefillChat(
      `I want to ask about something from my story here — ${title} — what did you make of that about me?`,
    );
    navigation.navigate('Chat');
  }

  function talkAboutTrait(key: TraitKey) {
    const label = TRAIT_LABELS[key].toLowerCase();
    const score = (traitScores[key] ?? 5).toFixed(1);
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
          <Text style={styles.faithStatus}>{faithStatusLine(dialogueSignals)}</Text>

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
            const score = traitScores[key] ?? 5;
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
                <TouchableOpacity activeOpacity={0.7} onPress={() => askAbout(m.title)}>
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
