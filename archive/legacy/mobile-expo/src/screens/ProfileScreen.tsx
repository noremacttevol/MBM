import React from 'react';
import {
  View,
  Text,
  ScrollView,
  StyleSheet,
  SafeAreaView,
} from 'react-native';
import { StatusBar } from 'expo-status-bar';
import { useAppStore } from '../store/useAppStore';
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

export default function ProfileScreen() {
  const traitScores        = useAppStore(s => s.traitScores);
  const feedTag            = useAppStore(s => s.feedTag);
  const openedIds          = useAppStore(s => s.openedIds);
  const answeredQuestionIds = useAppStore(s => s.answeredQuestionIds);
  const journalEntries     = useAppStore(s => s.journalEntries);
  const dialogueSignals    = useAppStore(s => s.dialogueSignals);

  const interpretation = interpretTraits(traitScores, feedTag);

  const TAG_LABEL: Record<string, string> = {
    MILK:        'Foundation',
    BRIDGE:      'Evidence',
    RESTORATION: 'The Restoration',
    MAINTENANCE: 'Discipleship',
  };

  return (
    <SafeAreaView style={styles.safe}>
      <StatusBar style="light" />

      <ScrollView
        style={styles.scroll}
        contentContainerStyle={styles.container}
        showsVerticalScrollIndicator={false}
      >
        {/* ── Header ──────────────────────────────────────────────────── */}
        <Text style={styles.header}>Your journey</Text>

        {/* ── AI interpretation paragraph ─────────────────────────────── */}
        <View style={styles.interpretCard}>
          <Text style={styles.interpretLabel}>WHAT WE SENSE ABOUT YOU</Text>
          <Text style={styles.interpretText}>{interpretation}</Text>
        </View>

        {/* ── Trait bars ──────────────────────────────────────────────── */}
        <View style={styles.traitsCard}>
          <Text style={styles.sectionLabel}>SPIRITUAL TRAITS</Text>
          <Text style={styles.sectionNote}>
            Built from your dialogue answers. Updates as you engage.
          </Text>

          {TRAIT_ORDER.map(key => {
            const score  = traitScores[key] ?? 5;
            const pct    = Math.round((score / 10) * 100);
            return (
              <View key={key} style={styles.traitRow}>
                <View style={styles.traitMeta}>
                  <Text style={styles.traitName}>{TRAIT_LABELS[key]}</Text>
                  <Text style={styles.traitDesc}>{TRAIT_DESCRIPTIONS[key]}</Text>
                </View>
                <View style={styles.barTrack}>
                  <View style={[styles.barFill, { width: `${pct}%` as any }]} />
                </View>
                <Text style={styles.traitScore}>{score.toFixed(1)}</Text>
              </View>
            );
          })}
        </View>

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

        {/* ── Current feed tier ───────────────────────────────────────── */}
        <View style={styles.tierCard}>
          <Text style={styles.tierLabel}>CURRENT PATHWAY</Text>
          <Text style={styles.tierValue}>{TAG_LABEL[feedTag] ?? feedTag}</Text>
          {dialogueSignals.length > 0 && (
            <Text style={styles.tierNote}>
              {dialogueSignals.length} signal{dialogueSignals.length !== 1 ? 's' : ''} active
            </Text>
          )}
        </View>

        {/* ── Footer note ─────────────────────────────────────────────── */}
        <Text style={styles.footerNote}>
          This profile is private and lives only on your device.
          It exists to serve you, not to route you like a package.
        </Text>

        <View style={{ height: spacing.xl }} />
      </ScrollView>
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

  interpretCard: {
    borderWidth:     1,
    borderColor:     colors.borderDim,
    backgroundColor: colors.bgCard,
    borderRadius:    radius.lg,
    padding:         spacing.md,
    marginBottom:    spacing.md,
  },
  interpretLabel: {
    fontSize:      10,
    letterSpacing: 1.5,
    color:         colors.textMuted,
    fontFamily:    'Georgia',
    marginBottom:  spacing.sm,
  },
  interpretText: {
    fontSize:   15,
    fontFamily: 'Georgia',
    color:      colors.textDim,
    lineHeight: 24,
    fontStyle:  'italic',
  },

  traitsCard: {
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
    marginBottom:  spacing.xs,
  },
  sectionNote: {
    fontSize:     11,
    fontFamily:   'Georgia',
    fontStyle:    'italic',
    color:        colors.textMuted,
    marginBottom: spacing.md,
  },

  traitRow: {
    flexDirection: 'row',
    alignItems:    'center',
    marginBottom:  spacing.sm + 2,
    gap:           spacing.sm,
  },
  traitMeta: {
    width: 110,
  },
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

  tierCard: {
    borderWidth:     1,
    borderColor:     colors.borderDim,
    backgroundColor: colors.bgCard,
    borderRadius:    radius.md,
    padding:         spacing.md,
    marginBottom:    spacing.md,
  },
  tierLabel: {
    fontSize:      10,
    letterSpacing: 1.5,
    color:         colors.textMuted,
    fontFamily:    'Georgia',
    marginBottom:  spacing.xs,
  },
  tierValue: {
    fontSize:   16,
    fontFamily: 'Georgia',
    color:      colors.gold,
  },
  tierNote: {
    fontSize:   11,
    fontFamily: 'Georgia',
    color:      colors.textMuted,
    marginTop:  spacing.xs,
    fontStyle:  'italic',
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
