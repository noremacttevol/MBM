import React, { useState, useRef, useEffect } from 'react';
import {
  View, Text, TextInput, TouchableOpacity, ScrollView,
  StyleSheet, KeyboardAvoidingView, Platform,
  ActivityIndicator, Alert, Animated,
} from 'react-native';
import { SafeAreaView, useSafeAreaInsets } from 'react-native-safe-area-context';
import { StatusBar } from 'expo-status-bar';
import { useAppStore, isRestorationReady } from '../store/useAppStore';
import ConnectCard from '../components/ConnectCard';
import SaveNoteLink from '../components/SaveNoteLink';
import { colors, spacing, radius } from '../theme';

// Does this minister message read as the explicit-consent question about the
// restored perspective? We only ever check this when the person is already
// restoration-ready (see showConsentChips), so the match stays safe and specific:
// a question that names the Restoration / restored gospel / Book of Mormon, or the
// "stay with the plain biblical view" offer the prompt is told to use.
function asksForRestorationConsent(text: string): boolean {
  if (!text || !text.includes('?')) return false;
  const t = text.toLowerCase();
  const namesRestoration =
    t.includes('restored gospel') || t.includes('restoration') ||
    t.includes('book of mormon')  || t.includes('where this comes from') ||
    t.includes('restored perspective') || t.includes('restored view');
  const offersChoice =
    t.includes('would you like') || t.includes('would it help') ||
    t.includes('rather stay')    || t.includes('biblical view') ||
    t.includes('stay with the');
  return namesRestoration && offersChoice;
}

// Server URL — the same proxy the store uses for chat. Public, not a secret.
const SERVER_URL =
  (process.env.EXPO_PUBLIC_MBM_API_URL ?? process.env.EXPO_PUBLIC_SERVER_URL ?? '')
    .trim()
    .replace(/\/+$/, '');

export default function ChatScreen() {
  const chatMessages    = useAppStore(s => s.chatMessages);
  const chatLoading     = useAppStore(s => s.chatLoading);
  const sendChatMessage = useAppStore(s => s.sendChatMessage);
  const chatDraft       = useAppStore(s => s.chatDraft);
  const clearChatDraft  = useAppStore(s => s.clearChatDraft);
  const chatSessions    = useAppStore(s => s.chatSessions);
  const newChat         = useAppStore(s => s.newChat);
  const openChat        = useAppStore(s => s.openChat);
  const escalateToRealPerson = useAppStore(s => s.escalateToRealPerson);
  const inboxMessages   = useAppStore(s => s.inboxMessages);
  const inboxUnread     = useAppStore(s => s.inboxUnread);
  const deleteChatSession = useAppStore(s => s.deleteChatSession);
  const closeRealPersonThread = useAppStore(s => s.closeRealPersonThread);
  const dialogueSignals     = useAppStore(s => s.dialogueSignals);
  const restorationConsent  = useAppStore(s => s.restorationConsent);
  const grantRestorationConsent   = useAppStore(s => s.grantRestorationConsent);
  const declineRestorationConsent = useAppStore(s => s.declineRestorationConsent);

  function confirmDeleteSession(id: string, title: string) {
    Alert.alert(
      'Delete this conversation?',
      `"${title || 'Conversation'}" will be removed for good.`,
      [
        { text: 'Cancel', style: 'cancel' },
        { text: 'Delete', style: 'destructive', onPress: () => deleteChatSession(id) },
      ],
    );
  }

  const [draft,          setDraft]          = useState('');
  const [submittingFC,   setSubmittingFC]   = useState(false);
  const [showConnect,    setShowConnect]    = useState(false);
  const [showHistory,    setShowHistory]    = useState(false);
  const [escalated,      setEscalated]      = useState(false);
  const escalateAnim = useRef(new Animated.Value(0)).current;
  const scrollRef = useRef<ScrollView>(null);
  const insets = useSafeAreaInsets();

  useEffect(() => {
    scrollRef.current?.scrollToEnd({ animated: true });
  }, [chatMessages, chatLoading]);

  // A "Talk about it →" / "Ask about this →" tap elsewhere fills the chat draft.
  // Pull it into the input the moment it arrives, then clear the store copy.
  useEffect(() => {
    if (chatDraft) {
      // A "talk about it" tap ALWAYS takes priority: close any open real-person or
      // history view so the fresh topic chat is what the person sees. The new chat
      // was already started in the store (prefillChat -> newChat), so nothing is lost.
      setShowConnect(false);
      setShowHistory(false);
      setDraft(chatDraft);
      clearChatDraft();
    }
  }, [chatDraft]);

  async function handleSend() {
    const text = draft.trim();
    if (!text || chatLoading) return;
    setDraft('');
    await sendChatMessage(text);
  }

  // Explicit consent for the restored perspective (Step 5). When the minister has
  // asked, the person answers with a tap — a clear yes opens the restored milk in
  // the feed and tells the AI it may minister it; a no keeps them on the Bible view
  // and the AI will not bring it up again unless they reopen the door themselves.
  async function handleConsentYes() {
    if (chatLoading) return;
    grantRestorationConsent();
    await sendChatMessage('Yes — I’d like to hear the restored perspective on this.');
  }
  async function handleConsentNo() {
    if (chatLoading) return;
    declineRestorationConsent();
    await sendChatMessage('I’d rather stay with the plain biblical view for now, thank you.');
  }

  // Start a fresh AI conversation — the current one is archived into history.
  function handleNewChat() {
    newChat();
    setDraft('');
    setShowHistory(false);
    setShowConnect(false);
  }

  function fmtDay(ts: number) {
    return new Date(ts).toLocaleDateString('en-US', { month: 'short', day: 'numeric' });
  }

  // Submit the last Q&A pair anonymously for Cameron to fact-check
  // Bring THIS conversation to a real person: summarize the AI's answer, send it
  // into the separate real-person thread, and leave it waiting for their reply.
  // Bring THIS conversation to a real person — a quiet, one-button backend action.
  // It copies the conversation into the separate real-person thread (findable in
  // History, waiting for a reply) and stays right here on the chat. It NEVER opens a
  // panel that covers the chat, never navigates away, and never implies a reply has
  // already come back — it has only been sent.
  function flashCopiedBanner() {
    setEscalated(true);
    escalateAnim.setValue(0);
    Animated.sequence([
      Animated.timing(escalateAnim, { toValue: 1, duration: 280, useNativeDriver: true }),
      Animated.delay(2800),
      Animated.timing(escalateAnim, { toValue: 0, duration: 420, useNativeDriver: true }),
    ]).start(() => setEscalated(false));
  }

  async function handleFactCheck() {
    if (chatMessages.length < 2 || submittingFC) return;
    setSubmittingFC(true);
    const ok = await escalateToRealPerson();
    setSubmittingFC(false);
    if (ok) {
      // Open the NEW real-person conversation so the question + the AI's answer are
      // right there to read while the person writes more to a human (Cameron's #2).
      setShowHistory(false);
      setShowConnect(true);
      flashCopiedBanner();
    } else {
      Alert.alert('Nothing to send yet', 'Ask something first, then bring it to our admin team.');
    }
  }

  function formatTime(ts: number) {
    return new Date(ts).toLocaleTimeString('en-US', { hour: 'numeric', minute: '2-digit' });
  }

  const isEmpty = chatMessages.length === 0;
  const canFactCheck = chatMessages.length >= 2 && !submittingFC;

  // Show the yes/no consent chips only when the person is genuinely restoration-
  // ready, hasn't already answered, and the minister's most recent message is the
  // consent question. Triple-gated so the chips never appear out of context.
  const lastMsg = chatMessages[chatMessages.length - 1];
  const showConsentChips =
    !chatLoading &&
    restorationConsent === 'unknown' &&
    isRestorationReady(dialogueSignals) &&
    !!lastMsg && lastMsg.role === 'assistant' &&
    asksForRestorationConsent(lastMsg.text);

  return (
    <SafeAreaView style={styles.safe} edges={['top', 'left', 'right']}>
      <StatusBar style="light" />

      {/* ── Header ────────────────────────────────────────────────────────── */}
      <View style={styles.header}>
        <Text style={styles.headerTitle}>Talk About It</Text>
        <View style={styles.headerActions}>
          <TouchableOpacity style={styles.headerBtn} activeOpacity={0.75} onPress={handleNewChat}>
            <Text style={styles.headerBtnText}>+ New</Text>
          </TouchableOpacity>
          <TouchableOpacity
            style={styles.headerBtn}
            activeOpacity={0.75}
            onPress={() => { setShowHistory(v => !v); setShowConnect(false); }}
          >
            <Text style={styles.headerBtnText}>History ▾</Text>
          </TouchableOpacity>
          {/* A real person is ALWAYS one tap away — never gated (CLAUDE.md law).
              Opening it lands on the real-person conversation LIST (its own history,
              with its own + New), kept entirely separate from the AI history above. */}
          <TouchableOpacity
            style={[styles.headerBtn, styles.personBtn]}
            activeOpacity={0.75}
            onPress={() => {
              const next = !showConnect;
              setShowConnect(next);
              setShowHistory(false);
              if (next) closeRealPersonThread(); // open to the list, not a stale thread
            }}
          >
            <Text style={[styles.headerBtnText, styles.personBtnText]}>Real person</Text>
          </TouchableOpacity>
        </View>
      </View>

      {/* A quiet, animated confirmation that the conversation was copied to a real
          person and tucked into History — the chat below stays exactly where it was. */}
      {escalated && (
        <Animated.View style={[styles.copiedBanner, { opacity: escalateAnim }]}>
          <Text style={styles.copiedBannerText}>
            ✓ Sent to our admin team — it's in your History ▾, waiting for their reply.
          </Text>
        </Animated.View>
      )}

      {/* History dropdown — past "Talk About It" (AI) conversations only. The
          real-person history lives under its own "Real person" button, kept
          separate so the two are never tangled together. */}
      {showHistory && (
        <View style={styles.historyPanel}>
          <Text style={styles.historyHeading}>Past conversations</Text>
          <ScrollView style={styles.historyScroll} nestedScrollEnabled keyboardShouldPersistTaps="handled">
          {chatSessions.length === 0 && (
            <Text style={styles.historyEmpty}>No past conversations yet.</Text>
          )}
          {chatSessions.map(sess => (
            <TouchableOpacity
              key={sess.id}
              style={styles.historyRow}
              activeOpacity={0.7}
              onPress={() => { openChat(sess.id); setShowHistory(false); setShowConnect(false); }}
            >
              <Text style={styles.historyTitle} numberOfLines={1}>{sess.title || 'Conversation'}</Text>
              <Text style={styles.historyDate}>{fmtDay(sess.updatedAt)}</Text>
              <TouchableOpacity
                onPress={() => confirmDeleteSession(sess.id, sess.title)}
                hitSlop={{ top: 10, bottom: 10, left: 10, right: 10 }}
              >
                <Text style={styles.historyDelete}>×</Text>
              </TouchableOpacity>
            </TouchableOpacity>
          ))}
          </ScrollView>
        </View>
      )}

      {/* The real-person thread — its OWN scrollable view (full, not a cramped box),
          so the whole conversation is readable and you can keep writing back. */}
      {showConnect && (
        <ScrollView
          style={styles.connectScroll}
          contentContainerStyle={styles.connectScrollContent}
          keyboardShouldPersistTaps="handled"
        >
          <ConnectCard />
        </ScrollView>
      )}

      {/* ── The AI chat — hidden while the real-person thread is open ───────── */}
      {!showConnect && (
      <KeyboardAvoidingView
        style={{ flex: 1 }}
        behavior="padding"
        keyboardVerticalOffset={insets.top + 52}
      >
        <ScrollView
          ref={scrollRef}
          style={styles.messageList}
          contentContainerStyle={styles.messageListContent}
          showsVerticalScrollIndicator={false}
          keyboardShouldPersistTaps="handled"
        >
          {isEmpty && (
            <View style={styles.emptyState}>
              <Text style={styles.emptyTitle}>What's on your mind?</Text>
              <Text style={styles.emptyBody}>
                Ask about what you've been reading, a question that won't leave you alone,
                or anything you're working through.{'\n\n'}
                There are no wrong questions here.
              </Text>
              <Text style={styles.emptySub}>
                I'll be honest when I'm not sure about something — and I can always
                submit your question anonymously to our admin team, who can check it.
              </Text>
            </View>
          )}

          {chatMessages.map(msg => (
            msg.kind === 'meta' ? (
              <View key={msg.id} style={styles.metaNote}>
                <Text style={styles.metaText}>{msg.text}</Text>
              </View>
            ) : msg.role === 'assistant' ? (
              // Assistant message + a quiet "Keep this →" so the person can clip
              // what the minister said into a note and find it later in the Journal.
              <View key={msg.id} style={styles.assistantBlock}>
                <View style={[styles.bubble, styles.bubbleAssistant]}>
                  <Text selectable style={[styles.bubbleText, styles.bubbleTextAssistant]}>{msg.text}</Text>
                  <Text style={styles.bubbleTime}>{formatTime(msg.timestamp)}</Text>
                </View>
                <View style={styles.keepRow}>
                  <SaveNoteLink
                    source="chat"
                    title="From a conversation"
                    body={msg.text}
                    label="Keep this →"
                  />
                </View>
              </View>
            ) : (
              <View key={msg.id} style={[styles.bubble, styles.bubbleUser]}>
                <Text selectable style={[styles.bubbleText, styles.bubbleTextUser]}>{msg.text}</Text>
                <Text style={styles.bubbleTime}>{formatTime(msg.timestamp)}</Text>
              </View>
            )
          ))}

          {chatLoading && (
            <View style={[styles.bubble, styles.bubbleAssistant, styles.loadingBubble]}>
              <ActivityIndicator color={colors.textMuted} size="small" />
            </View>
          )}
        </ScrollView>

        {/* ── Fact-check bar — appears after first exchange ─────────────── */}
        {canFactCheck && (
          <TouchableOpacity
            style={styles.factCheckBar}
            activeOpacity={0.75}
            onPress={handleFactCheck}
          >
            <Text style={styles.factCheckText}>
              {submittingFC
                ? 'Bringing this to our admin team…'
                : 'Want a real person on our admin team to weigh in? Bring this conversation to them →'}
            </Text>
          </TouchableOpacity>
        )}

        {/* ── Consent chips — the explicit yes/no for the restored perspective ── */}
        {showConsentChips && (
          <View style={styles.consentRow}>
            <TouchableOpacity
              style={[styles.consentChip, styles.consentYes]}
              activeOpacity={0.8}
              onPress={handleConsentYes}
            >
              <Text style={styles.consentYesText}>Yes, share the restored perspective</Text>
            </TouchableOpacity>
            <TouchableOpacity
              style={[styles.consentChip, styles.consentNo]}
              activeOpacity={0.8}
              onPress={handleConsentNo}
            >
              <Text style={styles.consentNoText}>No, stay with the Bible view for now</Text>
            </TouchableOpacity>
          </View>
        )}

        {/* ── Input bar ─────────────────────────────────────────────────── */}
        <View style={styles.inputBar}>
          <TextInput
            style={styles.input}
            value={draft}
            onChangeText={setDraft}
            placeholder="Say something…"
            placeholderTextColor={colors.textMuted}
            multiline
            maxLength={1000}
            returnKeyType="default"
          />
          <TouchableOpacity
            style={[styles.sendBtn, (!draft.trim() || chatLoading) && styles.sendBtnDisabled]}
            activeOpacity={0.7}
            onPress={handleSend}
            disabled={!draft.trim() || chatLoading}
          >
            <Text style={styles.sendBtnText}>→</Text>
          </TouchableOpacity>
        </View>
      </KeyboardAvoidingView>
      )}
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safe: { flex: 1, backgroundColor: colors.bg },

  header: {
    paddingHorizontal: spacing.md, paddingTop: spacing.md, paddingBottom: spacing.sm,
    borderBottomWidth: 1, borderBottomColor: colors.borderDim,
    flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center',
  },
  headerTitle: { fontSize: 18, fontFamily: 'Jost_400Regular', color: colors.textMid },

  headerActions: { flexDirection: 'row', alignItems: 'center', gap: spacing.xs },
  headerBtn: {
    borderWidth: 1, borderColor: colors.borderDim, borderRadius: 4,
    paddingVertical: 5, paddingHorizontal: 9,
  },
  headerBtnText: { color: colors.textDim, fontSize: 11, fontFamily: 'Jost_400Regular' },
  // The real-person action is blue, matching the blue of a real person's replies.
  personBtn: { borderColor: colors.blue },
  personBtnText: { color: colors.blue },

  historyPanel: {
    paddingHorizontal: spacing.md, paddingTop: spacing.sm, paddingBottom: spacing.xs,
    borderBottomWidth: 1, borderBottomColor: colors.borderDim,
  },
  historyHeading: {
    fontSize: 10, fontFamily: 'Jost_400Regular', color: colors.textMuted,
    textTransform: 'uppercase', letterSpacing: 0.5, marginBottom: spacing.xs,
  },
  historyRow: {
    flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center',
    paddingVertical: 8, borderBottomWidth: 1, borderBottomColor: colors.borderDim,
  },
  historyTitle: { flex: 1, color: colors.textMid, fontSize: 13, fontFamily: 'Jost_400Regular' },
  historyDate: { color: colors.textMuted, fontSize: 11, fontFamily: 'Jost_400Regular', marginLeft: spacing.sm },
  historyEmpty: { color: colors.textMuted, fontSize: 12, fontFamily: 'Jost_400Regular', fontStyle: 'italic', paddingVertical: 6 },
  historyScroll: { maxHeight: 300 },
  historyDelete: { color: colors.textMuted, fontSize: 18, marginLeft: spacing.sm, paddingHorizontal: 4 },

  copiedBanner: {
    marginHorizontal: spacing.md, marginTop: spacing.sm,
    backgroundColor: '#0d1b2e', borderWidth: 1, borderColor: colors.blue,
    borderRadius: radius.md, paddingVertical: 9, paddingHorizontal: 12,
  },
  copiedBannerText: { color: colors.blue, fontSize: 12, fontFamily: 'Jost_400Regular', lineHeight: 17 },

  connectPanel: {
    paddingHorizontal: spacing.md, paddingTop: spacing.sm,
  },
  connectScroll: { flex: 1 },
  connectScrollContent: { paddingHorizontal: spacing.md, paddingTop: spacing.md, paddingBottom: spacing.xl },

  messageList: { flex: 1 },
  messageListContent: {
    paddingHorizontal: spacing.md, paddingVertical: spacing.md, flexGrow: 1,
  },

  emptyState: {
    flex: 1, alignItems: 'center', justifyContent: 'center',
    paddingTop: spacing.xxl, paddingHorizontal: spacing.lg,
  },
  emptyTitle: {
    fontSize: 18, fontFamily: 'Jost_400Regular', color: colors.textMid,
    marginBottom: spacing.md, textAlign: 'center',
  },
  emptyBody: {
    fontSize: 14, fontFamily: 'Jost_400Regular', color: colors.textDim,
    lineHeight: 22, textAlign: 'center', marginBottom: spacing.lg,
  },
  emptySub: {
    fontSize: 12, fontFamily: 'Jost_400Regular', fontStyle: 'italic',
    color: colors.textMuted, textAlign: 'center',
  },

  bubble: {
    maxWidth: '90%', borderRadius: radius.lg,
    padding: spacing.sm + 4, marginBottom: spacing.sm,
  },
  bubbleUser: {
    alignSelf: 'flex-end', backgroundColor: '#1a1a12',
    borderWidth: 1, borderColor: colors.border,
  },
  bubbleAssistant: {
    alignSelf: 'flex-start', backgroundColor: colors.bgCard,
    borderWidth: 1, borderColor: colors.borderDim,
  },
  // Wraps an assistant bubble + its "Keep this →" link, kept left-aligned.
  assistantBlock: { alignSelf: 'flex-start', maxWidth: '90%' },
  keepRow: { paddingLeft: 4, marginTop: -2, marginBottom: spacing.sm },

  loadingBubble: { paddingVertical: spacing.md, paddingHorizontal: spacing.lg },
  bubbleText: { fontSize: 14, fontFamily: 'Jost_400Regular', lineHeight: 22 },
  bubbleTextUser: { color: colors.textMid },
  bubbleTextAssistant: { color: colors.textDim },
  bubbleTime: {
    fontSize: 10, fontFamily: 'Jost_400Regular', color: colors.textMuted,
    marginTop: 4, alignSelf: 'flex-end',
  },

  // A quiet, centered note (e.g. a spirit-level change) — not a chat bubble.
  metaNote: {
    alignSelf: 'center', maxWidth: '88%',
    paddingVertical: 4, paddingHorizontal: 8, marginVertical: 2,
  },
  metaText: {
    fontSize: 11, fontFamily: 'Jost_400Regular', fontStyle: 'italic',
    color: colors.textMuted, textAlign: 'center', lineHeight: 16,
  },

  factCheckBar: {
    marginHorizontal: spacing.md, marginBottom: spacing.xs,
    borderWidth: 1, borderColor: colors.blue, borderRadius: radius.md,
    paddingVertical: 8, paddingHorizontal: 12,
  },
  factCheckText: {
    fontSize: 11, fontFamily: 'Jost_400Regular', color: colors.blue,
    fontStyle: 'italic', lineHeight: 16,
  },

  // The explicit-consent chips: a warm, unpressured yes/no. The "yes" is gently
  // emphasized; the "no" is equally easy to choose — declining must never feel
  // like the lesser option.
  consentRow: {
    flexDirection: 'row', flexWrap: 'wrap', gap: spacing.xs,
    marginHorizontal: spacing.md, marginBottom: spacing.xs,
  },
  consentChip: {
    flexGrow: 1, flexBasis: '47%',
    borderWidth: 1, borderRadius: radius.md,
    paddingVertical: 10, paddingHorizontal: 12,
  },
  consentYes:     { borderColor: colors.blue, backgroundColor: colors.blue + '14' },
  consentNo:      { borderColor: colors.borderDim },
  consentYesText: { fontSize: 12, fontFamily: 'Jost_400Regular', color: colors.blue, textAlign: 'center' },
  consentNoText:  { fontSize: 12, fontFamily: 'Jost_400Regular', color: colors.textDim, textAlign: 'center' },

  inputBar: {
    flexDirection: 'row', alignItems: 'flex-end',
    paddingHorizontal: spacing.md, paddingVertical: spacing.sm,
    borderTopWidth: 1, borderTopColor: colors.borderDim,
    gap: spacing.sm, backgroundColor: colors.bg,
  },
  input: {
    flex: 1, backgroundColor: colors.bgInput, borderWidth: 1,
    borderColor: colors.border, borderRadius: radius.md,
    color: colors.text, fontFamily: 'Jost_400Regular', fontSize: 14,
    paddingHorizontal: spacing.sm, paddingVertical: spacing.sm, maxHeight: 100,
  },
  sendBtn: {
    backgroundColor: colors.bgCard, borderWidth: 1, borderColor: colors.gold,
    borderRadius: radius.md, width: 40, height: 40,
    alignItems: 'center', justifyContent: 'center',
  },
  sendBtnDisabled: { borderColor: colors.borderDim },
  sendBtnText: { color: colors.gold, fontSize: 18, fontFamily: 'Jost_400Regular' },
});
