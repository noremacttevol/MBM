import React, { useState, useRef, useEffect } from 'react';
import {
  View,
  Text,
  TextInput,
  TouchableOpacity,
  ScrollView,
  StyleSheet,
  KeyboardAvoidingView,
  Platform,
  Animated,
  Modal,
} from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { StatusBar } from 'expo-status-bar';
import { useNavigation } from '@react-navigation/native';
import { confirmAction } from '../lib/confirm';
import { useAppStore, generateBlessing, NoteSource } from '../store/useAppStore';
import { getCurrentPrompt, getPromptSuggestions, JournalPrompt } from '../data/journalPrompts';
import { colors, spacing, radius } from '../theme';

// The open invitation shown in freestyle mode — no question, just space.
const FREESTYLE_TEXT =
  'Write freely — anything on your mind, your heart, your day, or a prayer. There is no prompt here, only space.';

// How many kept notes to show before the "Show all" link appears.
const RECENT_NOTES = 5;

// A short, human label for where a note came from — shown above each note.
const NOTE_SOURCE_LABEL: Record<NoteSource, string> = {
  feed:     'From a reading',
  chat:     'From a conversation',
  blessing: 'A word you kept',
  story:    'From a story',
  dialogue: 'From a question',
};

export default function JournalScreen() {
  const feedTag          = useAppStore(s => s.feedTag);
  const dialogueSignals  = useAppStore(s => s.dialogueSignals);
  const journalEntries   = useAppStore(s => s.journalEntries);
  const answeredPromptIds = useAppStore(s => s.answeredPromptIds);
  const addJournalEntry  = useAppStore(s => s.addJournalEntry);

  const learnedNotes     = useAppStore(s => s.learnedNotes);
  const pendingNoteId    = useAppStore(s => s.pendingNoteId);
  const clearPendingNote = useAppStore(s => s.clearPendingNote);
  const prefillChat      = useAppStore(s => s.prefillChat);
  const deleteNote       = useAppStore(s => s.deleteNote);
  const deleteJournalEntry = useAppStore(s => s.deleteJournalEntry);
  const editJournalEntry = useAppStore(s => s.editJournalEntry);
  const navigation       = useNavigation<any>();

  const [editingEntryId, setEditingEntryId] = useState<string | null>(null);
  const [editEntryDraft, setEditEntryDraft] = useState('');

  function confirmDelete(label: string, onDelete: () => void) {
    confirmAction(`Delete this ${label}?`, 'It will be removed for good.', onDelete, { confirmLabel: 'Delete' });
  }

  // Carry a KEPT NOTE (something the person clipped from the feed, a story, a
  // chat line) into a fresh chat. Framed as "something I kept" — which is true
  // for notes, but NOT for journal answers (see talkAboutEntry).
  function talkAbout(what: string) {
    const clean = (what || '').replace(/\s+/g, ' ').trim();
    if (!clean) return;
    prefillChat(`I'd like to talk about something I kept: “${clean}”. What do you make of it, and what would you ask me about it?`);
    navigation.navigate('Chat');
  }

  // Carry a JOURNAL ENTRY into chat. Crucial difference from talkAbout: a journal
  // entry is the person's ANSWER to a prompt — so we MUST carry the prompt too,
  // and frame it as a reflection they wrote, not a clipping they "kept." Without
  // the prompt the AI sees a bare answer (e.g. "how?") with no context and rambles.
  function talkAboutEntry(promptText: string | undefined, text: string) {
    const answer = (text || '').replace(/\s+/g, ' ').trim();
    if (!answer) return;
    const prompt = (promptText || '').replace(/\s+/g, ' ').trim();
    const msg = prompt
      ? `In my journal I was reflecting on this prompt: “${prompt}” — and what I wrote was: “${answer}”. Can we talk about it? What do you make of my answer, and what would you ask me about it?`
      : `In my journal I wrote this freely: “${answer}”. Can we talk about it? What do you make of it, and what would you ask me about it?`;
    prefillChat(msg);
    navigation.navigate('Chat');
  }

  // The active prompt = a chosen one (from suggestions) ?? the next computed one.
  // Freestyle replaces the prompt with an open invitation.
  const [freestyle,      setFreestyle]      = useState(false);
  const [chosenPrompt,   setChosenPrompt]   = useState<JournalPrompt | null>(null);
  const [showSuggestions, setShowSuggestions] = useState(false);

  const computedPrompt = getCurrentPrompt(feedTag, dialogueSignals, answeredPromptIds);
  const activePrompt   = chosenPrompt ?? computedPrompt;
  const promptText     = freestyle ? FREESTYLE_TEXT : activePrompt.text;
  const promptId       = freestyle ? 'freestyle' : activePrompt.id;
  const suggestions    = getPromptSuggestions(feedTag, dialogueSignals, answeredPromptIds, 6);

  const [text,      setText]      = useState('');
  const [submitted, setSubmitted] = useState(false);
  const [blessLine, setBlessLine] = useState('');
  // Saved entries show as title links that expand to the full text on tap
  // (Cameron's ask) — the list stays scannable, the full note is one tap away.
  const [expandedIds, setExpandedIds] = useState<Set<string>>(new Set());
  const toggleEntry = (id: string) =>
    setExpandedIds(prev => {
      const next = new Set(prev);
      next.has(id) ? next.delete(id) : next.add(id);
      return next;
    });
  const fadeAnim  = useRef(new Animated.Value(1)).current;
  const thankAnim = useRef(new Animated.Value(0)).current;

  // Kept-notes view state: which note is expanded, and whether to show them all.
  const [expandedNoteId, setExpandedNoteId] = useState<string | null>(null);
  const [showAllNotes,   setShowAllNotes]   = useState(false);

  // The scroll position of the notes section, so arriving from a "Save" can
  // bring the person straight to the note they just kept.
  const scrollRef  = useRef<ScrollView>(null);
  const notesYRef  = useRef(0);

  // When the person saved a note elsewhere and was carried here, open to it:
  // expand it, scroll to the notes section, then clear the one-time target.
  useEffect(() => {
    if (!pendingNoteId) return;
    setExpandedNoteId(pendingNoteId);
    setShowAllNotes(false);
    const id = setTimeout(() => {
      scrollRef.current?.scrollTo({ y: Math.max(notesYRef.current - 12, 0), animated: true });
    }, 250);
    clearPendingNote();
    return () => clearTimeout(id);
  }, [pendingNoteId]);

  const visibleNotes = showAllNotes ? learnedNotes : learnedNotes.slice(0, RECENT_NOTES);

  function toggleNote(id: string) {
    setExpandedNoteId(cur => (cur === id ? null : id));
  }

  function handleSubmit() {
    if (!text.trim()) return;
    const written = text.trim();
    addJournalEntry(promptId, promptText, written);
    // A blessing in words after the truest thing is said — never numbers, and
    // never a canned line. The disciple reads what they actually wrote and either
    // speaks one personal blessing or stays silent. It is handed every line it has
    // said before, so it never repeats itself; a spoken line is remembered too.
    setBlessLine('');
    generateBlessing('journal', written, useAppStore.getState().blessingHistory).then(line => {
      if (line) {
        setBlessLine(line);
        useAppStore.getState().recordBlessing(line);
      }
    });

    Animated.sequence([
      Animated.timing(fadeAnim, { toValue: 0, duration: 300, useNativeDriver: true }),
      Animated.timing(thankAnim, { toValue: 1, duration: 400, useNativeDriver: true }),
    ]).start(() => {
      setSubmitted(true);
    });
  }

  // Return to the write view in a chosen mode. This is what makes "write again"
  // actually work — and gives a fresh prompt, a free page, or a list to pick from.
  function reopenWriting(mode: 'another' | 'free' | 'pick') {
    setText('');
    setSubmitted(false);
    fadeAnim.setValue(1);
    thankAnim.setValue(0);
    if (mode === 'free') {
      setFreestyle(true);
      setChosenPrompt(null);
      setShowSuggestions(false);
    } else if (mode === 'pick') {
      // Back to a normal write view, with the topic picker popped open over it.
      setFreestyle(false);
      setChosenPrompt(null);
      setShowSuggestions(true);
    } else {
      // 'another' — a fresh computed prompt (answeredPromptIds grew, so it rotates)
      setFreestyle(false);
      setChosenPrompt(null);
      setShowSuggestions(false);
    }
  }

  function chooseSuggestion(p: JournalPrompt) {
    setChosenPrompt(p);
    setFreestyle(false);
    setSubmitted(false);
    setShowSuggestions(false);
  }

  function formatDate(ts: number) {
    const d = new Date(ts);
    return d.toLocaleDateString('en-US', { month: 'short', day: 'numeric' });
  }

  return (
    <SafeAreaView style={styles.safe} edges={['top', 'left', 'right']}>
      <StatusBar style="light" />

      <KeyboardAvoidingView
        style={{ flex: 1 }}
        behavior={Platform.OS === 'ios' ? 'padding' : 'height'}
      >
        <ScrollView
          ref={scrollRef}
          style={styles.scroll}
          contentContainerStyle={styles.container}
          showsVerticalScrollIndicator={false}
          keyboardShouldPersistTaps="handled"
        >
          {/* ── Header ──────────────────────────────────────────────────── */}
          <Text style={styles.header}>Journal</Text>

          {/* ── Current prompt ──────────────────────────────────────────── */}
          <View style={styles.promptCard}>
            <Text style={styles.promptLabel}>
              {freestyle ? 'FREE WRITE' : "TODAY'S PROMPT"}
            </Text>

            {/* Thank-you state — now a real fork: another prompt, a free page,
                or a list to pick from. This is the "write again" that works. */}
            <Animated.View
              style={[styles.thankBlock, { opacity: thankAnim }]}
              pointerEvents={submitted ? 'auto' : 'none'}
            >
              <Text style={styles.thankText}>Saved.</Text>
              {blessLine ? <Text style={styles.blessLine}>{blessLine}</Text> : null}
              <View style={styles.writeAgainRow}>
                <TouchableOpacity onPress={() => reopenWriting('another')} activeOpacity={0.7}>
                  <Text style={styles.writeMoreText}>Another prompt →</Text>
                </TouchableOpacity>
                <TouchableOpacity onPress={() => reopenWriting('free')} activeOpacity={0.7}>
                  <Text style={styles.writeMoreText}>Write freely →</Text>
                </TouchableOpacity>
                <TouchableOpacity onPress={() => reopenWriting('pick')} activeOpacity={0.7}>
                  <Text style={styles.writeMoreText}>Pick a topic →</Text>
                </TouchableOpacity>
              </View>
            </Animated.View>

            {/* Active prompt / freestyle. While the "Saved." overlay is showing
                (submitted), this view is faded AND made untappable so the three
                links above actually receive the taps (they sit beneath it). */}
            <Animated.View
              style={{ opacity: fadeAnim }}
              pointerEvents={submitted ? 'none' : 'auto'}
            >
              <Text style={styles.promptText}>{promptText}</Text>

              <TextInput
                style={styles.input}
                value={text}
                onChangeText={setText}
                placeholder={freestyle ? 'Write whatever comes…' : 'Write what comes…'}
                placeholderTextColor={colors.textMuted}
                multiline
                numberOfLines={6}
                textAlignVertical="top"
                editable={!submitted}
              />

              <View style={styles.modeLinks}>
                {freestyle ? (
                  <TouchableOpacity onPress={() => reopenWriting('another')} activeOpacity={0.7}>
                    <Text style={styles.modeLink}>Use a prompt</Text>
                  </TouchableOpacity>
                ) : (
                  <TouchableOpacity onPress={() => reopenWriting('free')} activeOpacity={0.7}>
                    <Text style={styles.modeLink}>Write freely</Text>
                  </TouchableOpacity>
                )}
                <TouchableOpacity onPress={() => setShowSuggestions(true)} activeOpacity={0.7}>
                  <Text style={styles.modeLink}>Pick a topic</Text>
                </TouchableOpacity>
              </View>

              <TouchableOpacity
                style={[styles.submitBtn, !text.trim() && styles.submitBtnDisabled]}
                activeOpacity={0.7}
                onPress={handleSubmit}
                disabled={!text.trim() || submitted}
              >
                <Text style={styles.submitBtnText}>Save →</Text>
              </TouchableOpacity>
            </Animated.View>
          </View>

          {/* ── Pick a topic ─ a popup you scroll through and choose one from ── */}
          <Modal
            visible={showSuggestions}
            transparent
            animationType="fade"
            onRequestClose={() => setShowSuggestions(false)}
          >
            <View style={styles.modalBackdrop}>
              <View style={styles.modalCard}>
                <View style={styles.modalHeader}>
                  <Text style={styles.modalTitle}>Pick a topic</Text>
                  <TouchableOpacity
                    onPress={() => setShowSuggestions(false)}
                    activeOpacity={0.7}
                    hitSlop={{ top: 12, bottom: 12, left: 12, right: 12 }}
                  >
                    <Text style={styles.modalClose}>✕</Text>
                  </TouchableOpacity>
                </View>

                <ScrollView
                  style={styles.modalScroll}
                  showsVerticalScrollIndicator
                  keyboardShouldPersistTaps="handled"
                >
                  {suggestions.map(s => (
                    <TouchableOpacity
                      key={s.id}
                      style={styles.suggestRow}
                      activeOpacity={0.7}
                      onPress={() => chooseSuggestion(s)}
                    >
                      <Text style={styles.suggestText}>{s.text}</Text>
                    </TouchableOpacity>
                  ))}
                </ScrollView>

                <TouchableOpacity
                  onPress={() => { setShowSuggestions(false); reopenWriting('free'); }}
                  activeOpacity={0.7}
                  style={styles.modalFreeBtn}
                >
                  <Text style={styles.modeLink}>…or just write freely →</Text>
                </TouchableOpacity>
              </View>
            </View>
          </Modal>

          {/* ── Notes you kept ──────────────────────────────────────────── */}
          <View onLayout={e => { notesYRef.current = e.nativeEvent.layout.y; }}>
            <View style={styles.sectionDivider} />
            <Text style={styles.sectionLabel}>NOTES YOU KEPT</Text>

            {learnedNotes.length === 0 ? (
              <Text style={styles.notesEmpty}>
                When something is worth remembering — a reading, a line from a
                conversation, a story — tap “Save to my notes” and it will be kept
                for you right here.
              </Text>
            ) : (
              <>
                {visibleNotes.map(note => {
                  const open = expandedNoteId === note.id;
                  return (
                    <TouchableOpacity
                      key={note.id}
                      activeOpacity={0.8}
                      onPress={() => toggleNote(note.id)}
                      style={[styles.noteCard, open && styles.noteCardOpen]}
                    >
                      <View style={styles.noteMeta}>
                        <Text style={styles.noteSource}>{NOTE_SOURCE_LABEL[note.source]}</Text>
                        <Text style={styles.noteDate}>{formatDate(note.timestamp)}</Text>
                      </View>

                      <Text style={styles.noteTitle} numberOfLines={open ? undefined : 2}>
                        {note.title}
                      </Text>

                      <Text style={styles.noteSummary}>
                        {note.summary}
                        {note.pending ? '  ·  summarizing…' : ''}
                      </Text>

                      {open && note.body && note.body !== note.summary && (
                        <View style={styles.noteBodyBox}>
                          <Text style={styles.noteBodyLabel}>WHAT YOU KEPT</Text>
                          <Text style={styles.noteBody}>{note.body}</Text>
                        </View>
                      )}

                      <Text style={styles.noteToggle}>
                        {open ? 'Show less' : 'Read what you kept →'}
                      </Text>
                      {open && (
                        <View style={styles.entryActions}>
                          <TouchableOpacity activeOpacity={0.7} onPress={() => talkAbout(note.body || note.summary || note.title)}>
                            <Text style={styles.talkLink}>Talk About It →</Text>
                          </TouchableOpacity>
                          <TouchableOpacity activeOpacity={0.7} onPress={() => confirmDelete('note', () => deleteNote(note.id))}>
                            <Text style={styles.deleteLink}>Delete</Text>
                          </TouchableOpacity>
                        </View>
                      )}
                    </TouchableOpacity>
                  );
                })}

                {learnedNotes.length > RECENT_NOTES && (
                  <TouchableOpacity
                    activeOpacity={0.7}
                    onPress={() => setShowAllNotes(v => !v)}
                    style={styles.allNotesBtn}
                  >
                    <Text style={styles.allNotesText}>
                      {showAllNotes
                        ? 'Show fewer notes'
                        : `Show all ${learnedNotes.length} notes →`}
                    </Text>
                  </TouchableOpacity>
                )}
              </>
            )}
          </View>

          {/* ── Past entries ────────────────────────────────────────────── */}
          {journalEntries.length > 0 && (
            <>
              <View style={styles.sectionDivider} />
              <Text style={styles.sectionLabel}>PAST ENTRIES</Text>

              {journalEntries.map(entry => {
                const open = expandedIds.has(entry.id);
                return (
                  <TouchableOpacity
                    key={entry.id}
                    style={styles.entryCard}
                    activeOpacity={0.7}
                    onPress={() => toggleEntry(entry.id)}
                  >
                    <Text style={styles.entryDate}>{formatDate(entry.timestamp)}</Text>
                    <View style={styles.entryTitleRow}>
                      <Text style={[styles.entryPrompt, { flex: 1 }]}>
                        {entry.promptText || 'A note'}
                      </Text>
                      <Text style={styles.entryChevron}>{open ? '▾' : '▸'}</Text>
                    </View>
                    {open ? (
                      editingEntryId === entry.id ? (
                        <>
                          <TextInput
                            style={styles.editInput}
                            value={editEntryDraft}
                            onChangeText={setEditEntryDraft}
                            multiline
                            textAlignVertical="top"
                            autoFocus
                          />
                          <View style={styles.entryActions}>
                            <TouchableOpacity activeOpacity={0.7} onPress={() => { editJournalEntry(entry.id, editEntryDraft); setEditingEntryId(null); }}>
                              <Text style={styles.talkLink}>Save</Text>
                            </TouchableOpacity>
                            <TouchableOpacity activeOpacity={0.7} onPress={() => setEditingEntryId(null)}>
                              <Text style={styles.deleteLink}>Cancel</Text>
                            </TouchableOpacity>
                          </View>
                        </>
                      ) : (
                        <>
                          <Text style={styles.entryText}>{entry.text}</Text>
                          <View style={styles.entryActions}>
                            <TouchableOpacity activeOpacity={0.7} onPress={() => talkAboutEntry(entry.promptText, entry.text)}>
                              <Text style={styles.talkLink}>Talk About It →</Text>
                            </TouchableOpacity>
                            <TouchableOpacity activeOpacity={0.7} onPress={() => { setEditingEntryId(entry.id); setEditEntryDraft(entry.text); }}>
                              <Text style={styles.editLink}>Edit</Text>
                            </TouchableOpacity>
                            <TouchableOpacity activeOpacity={0.7} onPress={() => confirmDelete('entry', () => deleteJournalEntry(entry.id))}>
                              <Text style={styles.deleteLink}>Delete</Text>
                            </TouchableOpacity>
                          </View>
                        </>
                      )
                    ) : (
                      <Text style={styles.entryPreview} numberOfLines={1}>{entry.text}</Text>
                    )}
                  </TouchableOpacity>
                );
              })}
            </>
          )}

          {journalEntries.length === 0 && (
            <Text style={styles.emptyNote}>
              Your entries will appear here. This is only for you.
            </Text>
          )}

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

  promptCard: {
    borderWidth:     1,
    borderColor:     colors.borderDim,
    backgroundColor: colors.bgCard,
    borderRadius:    radius.lg,
    padding:         spacing.md,
    marginBottom:    spacing.lg,
    minHeight:       220,
  },
  promptLabel: {
    fontSize:      10,
    letterSpacing: 1.5,
    color:         colors.textMuted,
    fontFamily:    'Jost_400Regular',
    marginBottom:  spacing.sm,
  },
  promptText: {
    fontSize:     16,
    fontFamily:   'Jost_400Regular',
    color:        colors.textMid,
    lineHeight:   26,
    marginBottom: spacing.md,
  },

  thankBlock: {
    position:       'absolute',
    top:            40,
    left:           0,
    right:          0,
    alignItems:     'center',
    justifyContent: 'center',
    gap:            spacing.sm,
    paddingVertical: spacing.xl,
  },
  thankText: {
    fontSize:   18,
    fontFamily: 'Jost_400Regular',
    color:      colors.gold,
    fontStyle:  'italic',
  },
  blessLine: {
    fontSize:   13,
    fontFamily: 'Jost_400Regular',
    fontStyle:  'italic',
    color:      colors.textDim,
    textAlign:  'center',
    lineHeight: 20,
    paddingHorizontal: spacing.md,
  },
  writeMoreText: {
    fontSize:   14,
    fontFamily: 'Jost_400Regular',
    color:      colors.gold,
    paddingVertical: 5,
  },
  writeAgainRow: {
    alignItems: 'center',
    gap:        2,
    marginTop:  spacing.xs,
  },

  // Mode links under the input: "Write freely" / "Use a prompt" / "Other prompts"
  modeLinks: {
    flexDirection: 'row',
    gap:           spacing.md,
    marginBottom:  spacing.sm,
  },
  modeLink: {
    fontSize:   12,
    fontFamily: 'Jost_400Regular',
    color:      colors.blue,
    paddingVertical: 4,
  },

  // ── Pick-a-topic popup ────────────────────────────────────────────────
  modalBackdrop: {
    flex:            1,
    backgroundColor: 'rgba(0,0,0,0.6)',
    justifyContent:  'center',
    paddingHorizontal: spacing.lg,
  },
  modalCard: {
    backgroundColor: colors.bgCard,
    borderWidth:     1,
    borderColor:     colors.border,
    borderRadius:    radius.lg,
    padding:         spacing.md,
    maxHeight:       '70%',
  },
  modalHeader: {
    flexDirection:  'row',
    justifyContent: 'space-between',
    alignItems:     'center',
    marginBottom:   spacing.sm,
  },
  modalTitle: {
    fontSize:   16,
    fontFamily: 'Jost_400Regular',
    color:      colors.textMid,
  },
  modalClose: {
    fontSize:   16,
    color:      colors.textMuted,
    fontFamily: 'Jost_400Regular',
  },
  modalScroll: { flexGrow: 0 },
  modalFreeBtn: {
    marginTop:  spacing.sm,
    alignItems: 'center',
  },

  // Suggestion rows (pick something to write about)
  suggestRow: {
    borderWidth:     1,
    borderColor:     colors.borderDim,
    backgroundColor: colors.bgInput,
    borderRadius:    radius.md,
    paddingVertical: 10,
    paddingHorizontal: 12,
    marginBottom:    spacing.sm,
  },
  suggestText: {
    fontSize:   13,
    fontFamily: 'Jost_400Regular',
    color:      colors.textMid,
    lineHeight: 20,
  },

  input: {
    borderWidth:     1,
    borderColor:     colors.border,
    borderRadius:    radius.sm,
    backgroundColor: colors.bgInput,
    color:           colors.text,
    fontFamily:      'Jost_400Regular',
    fontSize:        14,
    padding:         spacing.sm,
    minHeight:       120,
    marginBottom:    spacing.sm,
  },
  submitBtn: {
    alignSelf:         'flex-end',
    borderWidth:       1,
    borderColor:       colors.gold,
    borderRadius:      4,
    paddingVertical:   8,
    paddingHorizontal: 16,
  },
  submitBtnDisabled: {
    borderColor: colors.borderDim,
  },
  submitBtnText: {
    color:      colors.gold,
    fontFamily: 'Jost_400Regular',
    fontSize:   13,
  },

  sectionDivider: {
    height:          1,
    backgroundColor: colors.borderDim,
    marginBottom:    spacing.md,
  },
  sectionLabel: {
    fontSize:      10,
    letterSpacing: 1.5,
    color:         colors.textMuted,
    fontFamily:    'Jost_400Regular',
    marginBottom:  spacing.md,
  },

  // ── Kept notes ─────────────────────────────────────────────────────────
  notesEmpty: {
    fontSize:   13,
    fontFamily: 'Jost_400Regular',
    fontStyle:  'italic',
    color:      colors.textMuted,
    lineHeight: 21,
    marginBottom: spacing.md,
  },
  noteCard: {
    backgroundColor: colors.bgCard,
    borderWidth:     1,
    borderColor:     colors.border,
    borderRadius:    radius.md,
    padding:         spacing.md,
    marginBottom:    spacing.sm,
  },
  noteCardOpen: {
    borderColor: colors.gold,
  },
  noteMeta: {
    flexDirection:  'row',
    justifyContent: 'space-between',
    alignItems:     'center',
    marginBottom:   6,
  },
  noteSource: {
    fontSize:      10,
    letterSpacing: 1.2,
    textTransform: 'uppercase',
    color:         colors.textMuted,
    fontFamily:    'Jost_400Regular',
  },
  noteDate: {
    fontSize:   10,
    color:      colors.textMuted,
    fontFamily: 'Jost_400Regular',
    letterSpacing: 0.8,
  },
  noteTitle: {
    fontSize:     15,
    fontFamily:   'Jost_400Regular',
    color:        '#e8e0c8',
    lineHeight:   22,
    marginBottom: 6,
  },
  noteSummary: {
    fontSize:   13,
    fontFamily: 'Jost_400Regular',
    color:      colors.textDim,
    lineHeight: 21,
  },
  noteBodyBox: {
    marginTop:       spacing.sm,
    paddingTop:      spacing.sm,
    borderTopWidth:  1,
    borderTopColor:  colors.borderDim,
  },
  noteBodyLabel: {
    fontSize:      9,
    letterSpacing: 1.2,
    color:         colors.textMuted,
    fontFamily:    'Jost_400Regular',
    marginBottom:  4,
  },
  noteBody: {
    fontSize:   13,
    fontFamily: 'Jost_400Regular',
    fontStyle:  'italic',
    color:      colors.textMid,
    lineHeight: 21,
  },
  noteToggle: {
    fontSize:   11,
    fontFamily: 'Jost_400Regular',
    fontStyle:  'italic',
    color:      colors.blue,
    marginTop:  spacing.sm,
  },
  allNotesBtn: {
    alignSelf:         'center',
    paddingVertical:   8,
    paddingHorizontal: 12,
    marginTop:         spacing.xs,
    marginBottom:      spacing.md,
  },
  allNotesText: {
    fontSize:   12,
    fontFamily: 'Jost_400Regular',
    color:      colors.gold,
  },

  entryCard: {
    borderWidth:     1,
    borderColor:     colors.borderDim,
    borderRadius:    radius.md,
    padding:         spacing.md,
    marginBottom:    spacing.sm,
  },
  entryDate: {
    fontSize:      10,
    color:         colors.textMuted,
    fontFamily:    'Jost_400Regular',
    letterSpacing: 0.8,
    marginBottom:  spacing.xs,
  },
  entryPrompt: {
    fontSize:     12,
    fontFamily:   'Jost_400Regular',
    fontStyle:    'italic',
    color:        colors.textMuted,
    lineHeight:   18,
    marginBottom: spacing.xs,
  },
  entryText: {
    fontSize:   14,
    fontFamily: 'Jost_400Regular',
    color:      colors.textDim,
    lineHeight: 22,
  },
  entryTitleRow: {
    flexDirection:  'row',
    alignItems:     'flex-start',
    justifyContent: 'space-between',
  },
  entryChevron: {
    fontSize:    12,
    color:       colors.textMuted,
    marginLeft:  spacing.sm,
    marginTop:   1,
  },
  entryPreview: {
    fontSize:   13,
    fontFamily: 'Jost_400Regular',
    color:      colors.textMuted,
    lineHeight: 18,
  },
  talkLink: {
    fontSize:   12,
    fontFamily: 'Jost_400Regular',
    color:      colors.gold,
    marginTop:  8,
  },
  entryActions: {
    flexDirection: 'row', alignItems: 'center', justifyContent: 'space-between', marginTop: 8,
  },
  deleteLink: {
    fontSize: 12, fontFamily: 'Jost_400Regular', fontStyle: 'italic', color: colors.textMuted,
  },
  editLink: {
    fontSize: 12, fontFamily: 'Jost_400Regular', fontStyle: 'italic', color: colors.blue,
  },
  editInput: {
    backgroundColor: colors.bgInput, borderWidth: 1, borderColor: colors.border,
    borderRadius: radius.md, color: colors.text, fontSize: 14, fontFamily: 'Jost_400Regular',
    padding: 10, minHeight: 70, lineHeight: 20, marginTop: 4,
  },

  emptyNote: {
    fontSize:   13,
    fontFamily: 'Jost_400Regular',
    fontStyle:  'italic',
    color:      colors.textMuted,
    textAlign:  'center',
    marginTop:  spacing.xl,
  },
});
