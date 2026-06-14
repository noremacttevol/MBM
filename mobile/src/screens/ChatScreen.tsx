import React, { useState, useRef, useEffect } from 'react';
import {
  View, Text, TextInput, TouchableOpacity, ScrollView,
  StyleSheet, KeyboardAvoidingView, Platform,
  ActivityIndicator, Alert,
} from 'react-native';
import { SafeAreaView, useSafeAreaInsets } from 'react-native-safe-area-context';
import { StatusBar } from 'expo-status-bar';
import { useAppStore } from '../store/useAppStore';
import ConnectCard from '../components/ConnectCard';
import SaveNoteLink from '../components/SaveNoteLink';
import { colors, spacing, radius } from '../theme';

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

  const [draft,          setDraft]          = useState('');
  const [submittingFC,   setSubmittingFC]   = useState(false);
  const [showConnect,    setShowConnect]    = useState(false);
  const [showHistory,    setShowHistory]    = useState(false);
  const scrollRef = useRef<ScrollView>(null);
  const insets = useSafeAreaInsets();

  useEffect(() => {
    scrollRef.current?.scrollToEnd({ animated: true });
  }, [chatMessages, chatLoading]);

  // A "Talk about it →" / "Ask about this →" tap elsewhere fills the chat draft.
  // Pull it into the input the moment it arrives, then clear the store copy.
  useEffect(() => {
    if (chatDraft) {
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
  async function handleFactCheck() {
    if (chatMessages.length < 2) return;
    setSubmittingFC(true);
    const ok = await escalateToRealPerson();
    setSubmittingFC(false);
    if (ok) {
      setShowConnect(true);   // open the real-person thread (the blue one)
      setShowHistory(false);
      Alert.alert(
        'Sent to a real person',
        "I've carried this conversation to a real person and left it waiting for them. When they reply, you'll see it here in blue — and it'll jump to the top of your conversations.",
        [{ text: 'OK' }],
      );
    } else {
      Alert.alert('Nothing to send yet', 'Ask something first, then bring it to a real person.');
    }
  }

  function formatTime(ts: number) {
    return new Date(ts).toLocaleTimeString('en-US', { hour: 'numeric', minute: '2-digit' });
  }

  const isEmpty = chatMessages.length === 0;
  const canFactCheck = chatMessages.length >= 2 && !submittingFC;

  return (
    <SafeAreaView style={styles.safe} edges={['top', 'left', 'right']}>
      <StatusBar style="light" />

      {/* ── Header ────────────────────────────────────────────────────────── */}
      <View style={styles.header}>
        <Text style={styles.headerTitle}>Ask anything.</Text>
        <View style={styles.headerActions}>
          <TouchableOpacity style={styles.headerBtn} activeOpacity={0.75} onPress={handleNewChat}>
            <Text style={styles.headerBtnText}>+ New</Text>
          </TouchableOpacity>
          {chatSessions.length > 0 && (
            <TouchableOpacity
              style={styles.headerBtn}
              activeOpacity={0.75}
              onPress={() => { setShowHistory(v => !v); setShowConnect(false); }}
            >
              <Text style={styles.headerBtnText}>History ▾</Text>
            </TouchableOpacity>
          )}
          {/* A real person is ALWAYS one tap away — never gated (CLAUDE.md law). */}
          <TouchableOpacity
            style={[styles.headerBtn, styles.personBtn]}
            activeOpacity={0.75}
            onPress={() => { setShowConnect(v => !v); setShowHistory(false); }}
          >
            <Text style={[styles.headerBtnText, styles.personBtnText]}>Real person</Text>
          </TouchableOpacity>
        </View>
      </View>

      {/* History dropdown — past conversations as titles, newest first. */}
      {showHistory && (
        <View style={styles.historyPanel}>
          <Text style={styles.historyHeading}>Past conversations</Text>
          {/* The real-person thread sits at the TOP, and a new reply is flagged in
              blue — so a human's answer always rises to the top of the list. */}
          {inboxMessages.length > 0 && (
            <TouchableOpacity
              style={styles.historyRow}
              activeOpacity={0.7}
              onPress={() => { setShowConnect(true); setShowHistory(false); }}
            >
              <Text style={[styles.historyTitle, { color: colors.blue }]} numberOfLines={1}>
                A real person{inboxUnread > 0 ? ' — new reply' : ''}
              </Text>
              {inboxUnread > 0 && (
                <Text style={[styles.historyDate, { color: colors.blue }]}>{inboxUnread} new</Text>
              )}
            </TouchableOpacity>
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
            </TouchableOpacity>
          ))}
        </View>
      )}

      {/* In-app human-connect capture — saved on-device, no mailto (Phase 1). */}
      {showConnect && (
        <View style={styles.connectPanel}>
          <ConnectCard compact />
        </View>
      )}

      {/* ── Message list ──────────────────────────────────────────────────── */}
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
                submit your question anonymously to a real person who can check it.
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
                  <Text style={[styles.bubbleText, styles.bubbleTextAssistant]}>{msg.text}</Text>
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
                <Text style={[styles.bubbleText, styles.bubbleTextUser]}>{msg.text}</Text>
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
                ? 'Bringing this to a real person…'
                : 'Want a real person to weigh in? Bring this conversation to them →'}
            </Text>
          </TouchableOpacity>
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
  headerTitle: { fontSize: 18, fontFamily: 'Georgia', color: colors.textMid },

  headerActions: { flexDirection: 'row', alignItems: 'center', gap: spacing.xs },
  headerBtn: {
    borderWidth: 1, borderColor: colors.borderDim, borderRadius: 4,
    paddingVertical: 5, paddingHorizontal: 9,
  },
  headerBtnText: { color: colors.textDim, fontSize: 11, fontFamily: 'Georgia' },
  // The real-person action is blue, matching the blue of a real person's replies.
  personBtn: { borderColor: colors.blue },
  personBtnText: { color: colors.blue },

  historyPanel: {
    paddingHorizontal: spacing.md, paddingTop: spacing.sm, paddingBottom: spacing.xs,
    borderBottomWidth: 1, borderBottomColor: colors.borderDim,
  },
  historyHeading: {
    fontSize: 10, fontFamily: 'Georgia', color: colors.textMuted,
    textTransform: 'uppercase', letterSpacing: 0.5, marginBottom: spacing.xs,
  },
  historyRow: {
    flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center',
    paddingVertical: 8, borderBottomWidth: 1, borderBottomColor: colors.borderDim,
  },
  historyTitle: { flex: 1, color: colors.textMid, fontSize: 13, fontFamily: 'Georgia' },
  historyDate: { color: colors.textMuted, fontSize: 11, fontFamily: 'Georgia', marginLeft: spacing.sm },

  connectPanel: {
    paddingHorizontal: spacing.md, paddingTop: spacing.sm,
  },

  messageList: { flex: 1 },
  messageListContent: {
    paddingHorizontal: spacing.md, paddingVertical: spacing.md, flexGrow: 1,
  },

  emptyState: {
    flex: 1, alignItems: 'center', justifyContent: 'center',
    paddingTop: spacing.xxl, paddingHorizontal: spacing.lg,
  },
  emptyTitle: {
    fontSize: 18, fontFamily: 'Georgia', color: colors.textMid,
    marginBottom: spacing.md, textAlign: 'center',
  },
  emptyBody: {
    fontSize: 14, fontFamily: 'Georgia', color: colors.textDim,
    lineHeight: 22, textAlign: 'center', marginBottom: spacing.lg,
  },
  emptySub: {
    fontSize: 12, fontFamily: 'Georgia', fontStyle: 'italic',
    color: colors.textMuted, textAlign: 'center',
  },

  bubble: {
    maxWidth: '80%', borderRadius: radius.lg,
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
  assistantBlock: { alignSelf: 'flex-start', maxWidth: '80%' },
  keepRow: { paddingLeft: 4, marginTop: -2, marginBottom: spacing.sm },

  loadingBubble: { paddingVertical: spacing.md, paddingHorizontal: spacing.lg },
  bubbleText: { fontSize: 14, fontFamily: 'Georgia', lineHeight: 22 },
  bubbleTextUser: { color: colors.textMid },
  bubbleTextAssistant: { color: colors.textDim },
  bubbleTime: {
    fontSize: 10, fontFamily: 'Georgia', color: colors.textMuted,
    marginTop: 4, alignSelf: 'flex-end',
  },

  // A quiet, centered note (e.g. a spirit-level change) — not a chat bubble.
  metaNote: {
    alignSelf: 'center', maxWidth: '88%',
    paddingVertical: 4, paddingHorizontal: 8, marginVertical: 2,
  },
  metaText: {
    fontSize: 11, fontFamily: 'Georgia', fontStyle: 'italic',
    color: colors.textMuted, textAlign: 'center', lineHeight: 16,
  },

  factCheckBar: {
    marginHorizontal: spacing.md, marginBottom: spacing.xs,
    borderWidth: 1, borderColor: colors.blue, borderRadius: radius.md,
    paddingVertical: 8, paddingHorizontal: 12,
  },
  factCheckText: {
    fontSize: 11, fontFamily: 'Georgia', color: colors.blue,
    fontStyle: 'italic', lineHeight: 16,
  },

  inputBar: {
    flexDirection: 'row', alignItems: 'flex-end',
    paddingHorizontal: spacing.md, paddingVertical: spacing.sm,
    borderTopWidth: 1, borderTopColor: colors.borderDim,
    gap: spacing.sm, backgroundColor: colors.bg,
  },
  input: {
    flex: 1, backgroundColor: colors.bgInput, borderWidth: 1,
    borderColor: colors.border, borderRadius: radius.md,
    color: colors.text, fontFamily: 'Georgia', fontSize: 14,
    paddingHorizontal: spacing.sm, paddingVertical: spacing.sm, maxHeight: 100,
  },
  sendBtn: {
    backgroundColor: colors.bgCard, borderWidth: 1, borderColor: colors.gold,
    borderRadius: radius.md, width: 40, height: 40,
    alignItems: 'center', justifyContent: 'center',
  },
  sendBtnDisabled: { borderColor: colors.borderDim },
  sendBtnText: { color: colors.gold, fontSize: 18, fontFamily: 'Georgia' },
});
