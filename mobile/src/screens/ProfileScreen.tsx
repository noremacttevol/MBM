/**
 * ProfileScreen — a mirror of the person's own words.
 *
 * NO SOUL-SCORING (Cameron, June 2026): the app does NOT grade anyone's
 * Christlikeness or assign virtue scores — not to seekers, not to members. Every
 * piece of information the app keeps to know the person is shown here openly and
 * can be read, edited, or removed. Owner-only routing internals (the feed track,
 * the milk gate) are not shown; everything the app recorded ABOUT THE PERSON is.
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
import { confirmAction } from '../lib/confirm';
import { useAppStore, isMemberSignal, humanizeSignal } from '../store/useAppStore';
import { colors, spacing, radius } from '../theme';

// A warm "we are paying attention" reflection — built only from where the person
// is and what they have said in their own words. It NEVER ranks or scores them.
function interpretJourney(feedTag: string, signals: string[]): string {
  // Internal routing context only — the tag name is NEVER shown to the person.
  const tagContext: Record<string, string> = {
    MILK:        'You seem to be someone who has felt something — in a quiet moment, in a loss, in the way beauty sometimes arrives uninvited.',
    BRIDGE:      'You carry real questions and you take them seriously. That kind of honesty is rarer than it looks.',
    RESTORATION: 'Something in the story of the restoration has caught your attention. That is worth following.',
    MAINTENANCE: 'You have covenants you are trying to keep. The fact that you are still here, still asking — that means something.',
  };

  const opening = tagContext[feedTag] ?? tagContext['MILK'];

  let closing = '';
  if (signals.includes('searching') || signals.includes('wants_more')) {
    closing = "You are looking for something real. That longing is not accidental.";
  } else if (signals.includes('carrying_burden') || signals.includes('grieving')) {
    closing = "You are carrying something heavy, and you are still here. That takes more than people know.";
  } else if (signals.includes('open_to_god')) {
    closing = "You are staying open even when it would be easier to close. That matters.";
  } else {
    closing = "You are still here, still asking. That is enough to start with.";
  }

  return [opening, closing].filter(Boolean).join(' ');
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
  const feedTag             = useAppStore(s => s.feedTag);
  const openedIds           = useAppStore(s => s.openedIds);
  const answeredQuestionIds = useAppStore(s => s.answeredQuestionIds);
  const journalEntries      = useAppStore(s => s.journalEntries);
  const dialogueSignals     = useAppStore(s => s.dialogueSignals);
  const faithWords          = useAppStore(s => s.faithWords);
  const moments             = useAppStore(s => s.moments);
  const deleteMoment        = useAppStore(s => s.deleteMoment);
  const answeredQuestions   = useAppStore(s => s.answeredQuestions);
  const editAnsweredQuestion   = useAppStore(s => s.editAnsweredQuestion);
  const removeAnsweredQuestion = useAppStore(s => s.removeAnsweredQuestion);
  const prefillChat         = useAppStore(s => s.prefillChat);
  const editFaithWord       = useAppStore(s => s.editFaithWord);
  const addFaithWord        = useAppStore(s => s.addFaithWord);
  const beliefHistory       = useAppStore(s => s.beliefHistory);
  const deleteBeliefChange  = useAppStore(s => s.deleteBeliefChange);
  const forgetSignal        = useAppStore(s => s.forgetSignal);
  const aiConsent           = useAppStore(s => s.aiConsent);
  const grantAIConsent      = useAppStore(s => s.grantAIConsent);
  const declineAIConsent    = useAppStore(s => s.declineAIConsent);
  const honoredVideoIds     = useAppStore(s => s.honoredVideoIds);
  const learnedNotes        = useAppStore(s => s.learnedNotes);
  const openPageRef         = useAppStore(s => s.openPageRef);
  const confirmedTakeaways  = useAppStore(s => s.confirmedTakeaways);
  // "Reflect on this" lands here (Rev 1 §5 — routing is by button); "Save it" goes to the Journal.
  const profileRecords      = learnedNotes.filter(n => n.dest === 'profile');

  const navigation = useNavigation<any>();

  // Editable faith — Law 4: anything we collect and show, a person can change anytime.
  const [editingIndex, setEditingIndex] = useState<number | null>(null);
  const [editDraft,    setEditDraft]    = useState('');
  const [adding,       setAdding]       = useState(false);
  // Editing an answered question's answer (inline).
  const [editingQId, setEditingQId] = useState<string | null>(null);
  const [editQDraft, setEditQDraft] = useState('');

  // Carry an answered question + the person's answer into a fresh "Talk About It"
  // chat, with full context so the AI knows it was THEIR answer to THAT question.
  function talkAboutAnswered(prompt: string, answer: string) {
    const p = (prompt || '').replace(/\s+/g, ' ').trim();
    const a = (answer || '').replace(/\s+/g, ' ').trim();
    prefillChat(
      `Earlier you asked me: “${p}” — and I answered: “${a || '(I didn’t say much)'}”. Can we talk about it? What do you make of my answer, and what would you ask me about it?`,
    );
    navigation.navigate('Chat');
  }
  const [addDraft,     setAddDraft]     = useState('');

  // The private member discipleship companion (self-chosen examen / reflection)
  // is offered ONLY to self-identified Latter-day Saints. It is the member's own
  // self-reflection tool — NOT the app scoring anyone.
  const isMember = isMemberSignal(dialogueSignals);
  // A warm reflection of where they are, in their own words — never a score.
  const interpretation = interpretJourney(feedTag, dialogueSignals);
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

        {/* ── WHERE YOU ARE RIGHT NOW ─────────────────────────────────── */}
        <View style={styles.card}>
          <Text style={styles.sectionLabel}>WHERE YOU ARE RIGHT NOW</Text>
          <Text style={styles.interpretText}>{interpretation}</Text>
        </View>

        {/* ── ABOUT YOU (Law 4 — nothing hidden) ─────────────────────────
            Cameron, June 2026: do NOT frame this as "what the app has NOTICED
            about you" — that reads as surveillance. Just list, plainly, what the
            app keeps to personalize the experience, fully editable/removable.
            Removing a line truly un-learns it: it stops shaping what you're shown. */}
        {dialogueSignals.length > 0 && (
          <View style={styles.card}>
            <Text style={styles.sectionLabel}>ABOUT YOU</Text>
            <Text style={styles.sectionNote}>
              This is everything the app keeps to personalize what you see. It's all here, and you can edit or remove anything anytime — removing a line means the app stops using it.
            </Text>
            {dialogueSignals.map(sig => (
              <View key={sig} style={styles.noticedRow}>
                <Text style={styles.noticedText}>{humanizeSignal(sig)}</Text>
                <TouchableOpacity
                  activeOpacity={0.7}
                  onPress={() => confirmAction(
                    'Remove this?',
                    'The app will stop using this to personalize what you see.',
                    () => forgetSignal(sig),
                    { confirmLabel: 'Remove' },
                  )}
                >
                  <Text style={styles.removeText}>Remove</Text>
                </TouchableOpacity>
              </View>
            ))}
          </View>
        )}

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
          {/* Jesus met people where they were — He did not hand them a ladder showing
              the whole route and where they ranked on it. So we reflect ONLY where a
              person is right now, warmly, in their own words. We never lay out the
              rungs ahead (especially the restored-gospel ones) — that would front-load
              the destination and turn a quiet walk into a visible agenda. The journey
              unfolds through relationship, not a progress chart. (FAITH_LADDER still
              names the current standing above; the upward list is intentionally gone.) */}

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

        {/* ── HOW YOUR THINKING HAS CHANGED (#7 — a changed mind is honored) ─── */}
        {beliefHistory.length > 0 && (
          <View style={styles.card}>
            <Text style={styles.sectionLabel}>HOW YOUR THINKING HAS CHANGED</Text>
            <Text style={styles.sectionNote}>
              When you revise something, the app keeps the old and the new — your
              growth is yours, and it's honored, not erased.
            </Text>
            {beliefHistory.map(b => (
              <View key={b.ts} style={styles.beliefRow}>
                <Text style={styles.beliefFrom}>Before: "{b.from}"</Text>
                <Text style={styles.beliefTo}>Now: "{b.to}"</Text>
                <View style={styles.beliefFoot}>
                  <Text style={styles.beliefDate}>{fmtDate(b.ts)}</Text>
                  <TouchableOpacity
                    activeOpacity={0.7}
                    onPress={() => confirmAction(
                      'Remove this record?',
                      'The app will stop keeping this change in your history.',
                      () => deleteBeliefChange(b.ts),
                      { confirmLabel: 'Remove' },
                    )}
                  >
                    <Text style={styles.removeText}>Remove</Text>
                  </TouchableOpacity>
                </View>
              </View>
            ))}
          </View>
        )}

        {/* ── MY DISCIPLESHIP (members only) — the private "Walk with Christ" ── */}
        {isMember && (
          <TouchableOpacity
            style={[styles.card, styles.discipleCard]}
            activeOpacity={0.85}
            onPress={() => navigation.navigate('Discipleship')}
          >
            <Text style={styles.sectionLabel}>MY DISCIPLESHIP</Text>
            <Text style={styles.discipleTitle}>Your walk with Christ →</Text>
            <Text style={styles.sectionNote}>
              A private companion for noticing how Christ is at work in your life — daily
              examen, a record of your walk, and a few personal rhythms. Just for you.
            </Text>
          </TouchableOpacity>
        )}

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
                <View style={styles.momentActions}>
                  <TouchableOpacity activeOpacity={0.7} onPress={() => askAbout(m.title, m.text)}>
                    <Text style={styles.askText}>Talk About It →</Text>
                  </TouchableOpacity>
                  <TouchableOpacity
                    activeOpacity={0.7}
                    onPress={() => confirmAction(
                      'Remove this from your story?',
                      'It will be deleted and the app will stop holding it for you.',
                      () => deleteMoment(m.ts),
                      { confirmLabel: 'Remove' },
                    )}
                  >
                    <Text style={styles.removeText}>Remove</Text>
                  </TouchableOpacity>
                </View>
              </View>
            ))}
          </View>
        )}

        {/* ── QUESTIONS YOU'VE ANSWERED ───────────────────────────────────
            The open record of the questions the person has answered in the app —
            held for them to read, edit, remove, or Talk About. (Journal notes and
            scripture reflections are NOT here; they live in the Journal tab and are
            never repeated — but can still be talked about there.) */}
        {answeredQuestions.length > 0 && (
          <View style={styles.card}>
            <Text style={styles.sectionLabel}>QUESTIONS YOU'VE ANSWERED</Text>
            <Text style={styles.sectionNote}>
              Everything you've answered here, remembered and held for you. Read it, change it, let it go, or talk any of it through.
            </Text>
            {answeredQuestions.map(q => (
              <View key={q.id} style={styles.momentRow}>
                <View style={styles.momentHead}>
                  <Text style={[styles.momentTitle, { flex: 1 }]}>{q.prompt}</Text>
                  <Text style={styles.momentDate}>{fmtDate(q.ts)}</Text>
                </View>
                {editingQId === q.id ? (
                  <>
                    <TextInput
                      style={styles.faithInput}
                      value={editQDraft}
                      onChangeText={setEditQDraft}
                      placeholder="In your own words…"
                      placeholderTextColor={colors.textMuted}
                      multiline
                      autoFocus
                      maxLength={400}
                    />
                    <View style={styles.momentActions}>
                      <TouchableOpacity activeOpacity={0.7} onPress={() => { editAnsweredQuestion(q.id, editQDraft); setEditingQId(null); }}>
                        <Text style={styles.askText}>Save</Text>
                      </TouchableOpacity>
                      <TouchableOpacity activeOpacity={0.7} onPress={() => setEditingQId(null)}>
                        <Text style={styles.removeText}>Cancel</Text>
                      </TouchableOpacity>
                    </View>
                  </>
                ) : (
                  <>
                    <Text style={styles.momentDetail}>{q.answer || '—'}</Text>
                    <View style={styles.momentActions}>
                      <TouchableOpacity activeOpacity={0.7} onPress={() => talkAboutAnswered(q.prompt, q.answer)}>
                        <Text style={styles.askText}>Talk About It →</Text>
                      </TouchableOpacity>
                      <TouchableOpacity activeOpacity={0.7} onPress={() => { setEditingQId(q.id); setEditQDraft(q.answer); }}>
                        <Text style={styles.editLink}>Edit</Text>
                      </TouchableOpacity>
                      <TouchableOpacity
                        activeOpacity={0.7}
                        onPress={() => confirmAction(
                          'Remove this answer?',
                          'It will be taken off your profile, and the app may gently ask it again sometime.',
                          () => removeAnsweredQuestion(q.id),
                          { confirmLabel: 'Remove' },
                        )}
                      >
                        <Text style={styles.removeText}>Remove</Text>
                      </TouchableOpacity>
                    </View>
                  </>
                )}
              </View>
            ))}
          </View>
        )}

        {/* ── Feed 2.0: watched stories + reflections (Rev 1 §5) ─────────────
            Every credited watch is counted here, and every "Reflect on this"
            lands on this record — short title, their words, and a link back to
            where the item lives in the feed. */}
        {(honoredVideoIds.length > 0 || profileRecords.length > 0 || confirmedTakeaways.length > 0) && (
          <View style={styles.card}>
            <Text style={styles.sectionLabel}>YOUR RECORD</Text>
            {honoredVideoIds.length > 0 && (
              <Text style={styles.sectionNote}>
                Stories watched all the way through: {honoredVideoIds.length}.
              </Text>
            )}
            {confirmedTakeaways.length > 0 && (
              <Text style={styles.sectionNote}>
                Truths you've confirmed along the way: {confirmedTakeaways.length}.
              </Text>
            )}
            {profileRecords.map(n => (
              <View key={n.id} style={styles.momentRow}>
                <View style={styles.momentHead}>
                  <Text style={[styles.momentTitle, { flex: 1 }]}>{n.title}</Text>
                  <Text style={styles.momentDate}>{fmtDate(n.timestamp)}</Text>
                </View>
                {n.body ? <Text style={styles.momentDetail}>{n.body}</Text> : null}
                {n.pageRef && (
                  <TouchableOpacity
                    activeOpacity={0.7}
                    onPress={() => { openPageRef(n.pageRef!); navigation.navigate('Feed'); }}
                  >
                    <Text style={styles.askText}>Open where this lives →</Text>
                  </TouchableOpacity>
                )}
              </View>
            ))}
          </View>
        )}

        {/* ── AI CONVERSATION — the person's standing choice, changeable any
            time (Apple 5.1.1(i)/5.1.2(i), and plain honesty about what we do). */}
        <View style={styles.card}>
          <Text style={styles.sectionLabel}>AI CONVERSATION</Text>
          <Text style={styles.sectionNote}>
            The written conversation can be powered by AI. When it's on, what
            you write is sent securely — not tied to your name — so the
            responses can speak to you personally. Nothing is sold, and nothing
            is used for ads or tracking; the privacy policy has every detail.
            When it's off, everything you write stays on this device and the
            app speaks in its offline voice.
          </Text>
          <Text style={styles.aiConsentState}>
            {aiConsent === 'granted'
              ? 'Currently ON — the conversation is powered by AI.'
              : 'Currently OFF — everything you write stays on this device.'}
          </Text>
          <TouchableOpacity
            style={styles.aiConsentBtn}
            activeOpacity={0.75}
            onPress={() => {
              if (aiConsent === 'granted') {
                confirmAction(
                  'Turn off the AI conversation?',
                  'Nothing you write will leave this device. The chat, blessings, and summaries will use the offline voice until you turn it back on.',
                  () => declineAIConsent(),
                  { confirmLabel: 'Turn off' },
                );
              } else {
                grantAIConsent();
              }
            }}
          >
            <Text style={styles.aiConsentBtnText}>
              {aiConsent === 'granted' ? 'Turn it off' : 'Turn it on'}
            </Text>
          </TouchableOpacity>
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

        {/* ── Footer note ─────────────────────────────────────────────── */}
        <Text style={styles.footerNote}>
          This profile is private and lives only on your device.
          It exists to serve you, not to route you like a package.
        </Text>

        <Text style={styles.disclaimerNote}>
          This app is not officially affiliated with, endorsed by, or
          sponsored by any church. It is an independent space to explore
          who Jesus is. What you do with it is between you and God.
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
    fontFamily:   'Jost_400Regular',
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
    fontFamily:    'Jost_400Regular',
    marginBottom:  spacing.sm,
  },
  discipleCard: {
    borderColor: colors.gold,
  },
  aiConsentState: {
    fontSize:     12,
    fontFamily:   'Jost_400Regular',
    color:        colors.textMid,
    fontStyle:    'italic',
    marginBottom: spacing.sm,
  },
  aiConsentBtn: {
    alignSelf:       'flex-start',
    borderWidth:     1,
    borderColor:     colors.borderDim,
    borderRadius:    18,
    paddingVertical: 8,
    paddingHorizontal: 18,
  },
  aiConsentBtnText: {
    fontSize:   13,
    fontFamily: 'Jost_400Regular',
    color:      colors.textDim,
  },
  discipleTitle: {
    fontSize:     17,
    fontFamily:   'Jost_400Regular',
    color:        colors.gold,
    marginBottom: 6,
  },
  sectionNote: {
    fontSize:     11,
    fontFamily:   'Jost_400Regular',
    fontStyle:    'italic',
    color:        colors.textMuted,
    lineHeight:   17,
    marginBottom: spacing.md,
  },
  interpretText: {
    fontSize:   15,
    fontFamily: 'Jost_400Regular',
    color:      colors.textDim,
    lineHeight: 24,
    fontStyle:  'italic',
  },

  faithStatus: {
    fontSize:     14,
    fontFamily:   'Jost_400Regular',
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
    fontFamily: 'Jost_400Regular',
    color:      colors.textDim,
    lineHeight: 20,
    fontStyle:  'italic',
  },
  faithWordDate: {
    fontSize:  10,
    fontFamily: 'Jost_400Regular',
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
    fontFamily: 'Jost_400Regular',
    fontStyle:  'italic',
    color:      colors.blue,
  },
  faithInput: {
    borderWidth:     1,
    borderColor:     colors.border,
    borderRadius:    radius.sm,
    backgroundColor: colors.bgInput,
    color:           colors.text,
    fontFamily:      'Jost_400Regular',
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
    fontFamily: 'Jost_400Regular',
    color:      colors.gold,
  },
  editCancel: {
    fontSize:   12,
    fontFamily: 'Jost_400Regular',
    color:      colors.textMuted,
  },
  editRemove: {
    fontSize:   12,
    fontFamily: 'Jost_400Regular',
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
    fontFamily: 'Jost_400Regular',
    fontStyle:  'italic',
    color:      colors.blue,
  },

  noticedRow: {
    flexDirection:  'row',
    alignItems:     'center',
    justifyContent: 'space-between',
    gap:            spacing.sm,
    borderTopWidth: 1,
    borderTopColor: colors.border,
    paddingVertical: spacing.sm,
  },
  noticedText: {
    flex:       1,
    fontSize:   13,
    fontFamily: 'Jost_400Regular',
    color:      colors.textDim,
    lineHeight: 19,
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
    fontFamily: 'Jost_400Regular',
    color:      colors.textMid,
    lineHeight: 19,
  },
  momentDate: {
    fontSize:  10,
    fontFamily: 'Jost_400Regular',
    color:     colors.textMuted,
    paddingTop: 3,
  },
  momentDetail: {
    fontSize:   12,
    fontFamily: 'Jost_400Regular',
    color:      colors.textDim,
    lineHeight: 18,
    fontStyle:  'italic',
    marginBottom: 6,
  },
  askText: {
    fontSize:   11,
    fontFamily: 'Jost_400Regular',
    fontStyle:  'italic',
    color:      colors.blue,
  },
  momentActions: {
    flexDirection: 'row', alignItems: 'center', justifyContent: 'space-between', marginTop: 4,
  },
  removeText: {
    fontSize: 11, fontFamily: 'Jost_400Regular', fontStyle: 'italic', color: colors.textMuted,
  },
  editLink: {
    fontSize: 11, fontFamily: 'Jost_400Regular', fontStyle: 'italic', color: colors.textDim,
  },

  beliefRow: {
    borderTopWidth: 1, borderTopColor: colors.borderDim,
    paddingTop: spacing.sm, marginTop: spacing.sm,
  },
  beliefFrom: {
    fontSize: 13, fontFamily: 'Jost_400Regular', fontStyle: 'italic',
    color: colors.textMuted, lineHeight: 20, textDecorationLine: 'line-through',
  },
  beliefTo: {
    fontSize: 14, fontFamily: 'Jost_400Regular', color: colors.textMid,
    lineHeight: 21, marginTop: 2,
  },
  beliefFoot: {
    flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', marginTop: 4,
  },
  beliefDate: {
    fontSize: 10, fontFamily: 'Jost_400Regular', color: colors.textMuted,
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
    fontFamily:   'Jost_400Regular',
    color:        colors.gold,
    marginBottom: 2,
  },
  statLabel: {
    fontSize:   10,
    fontFamily: 'Jost_400Regular',
    color:      colors.textMuted,
    textAlign:  'center',
  },

  footerNote: {
    fontSize:   12,
    fontFamily: 'Jost_400Regular',
    fontStyle:  'italic',
    color:      colors.textMuted,
    textAlign:  'center',
    lineHeight: 18,
    paddingHorizontal: spacing.md,
    marginTop:  spacing.md,
  },

  disclaimerNote: {
    fontSize:   11,
    fontFamily: 'Jost_400Regular',
    color:      colors.textMuted,
    textAlign:  'center',
    lineHeight: 16,
    paddingHorizontal: spacing.md,
    marginTop:  spacing.sm,
    opacity:    0.8,
  },
});
