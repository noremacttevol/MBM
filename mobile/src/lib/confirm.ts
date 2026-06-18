import { Alert, Platform } from 'react-native';

/**
 * Cross-platform confirm dialog.
 *
 * React Native's `Alert.alert` is a NO-OP on react-native-web — so every
 * destructive confirm (Cancel a request, Remove an answer, Delete a conversation)
 * silently did nothing in the web preview, making the buttons look broken. This
 * routes to the browser's window.confirm on web and to the native Alert on a phone,
 * so a confirm works everywhere.
 */
export function confirmAction(
  title: string,
  message: string,
  onConfirm: () => void,
  opts: { confirmLabel?: string; cancelLabel?: string; destructive?: boolean } = {},
) {
  const confirmLabel = opts.confirmLabel ?? 'OK';
  const cancelLabel  = opts.cancelLabel ?? 'Cancel';
  if (Platform.OS === 'web') {
    const ok = typeof window !== 'undefined'
      ? window.confirm(message ? `${title}\n\n${message}` : title)
      : true;
    if (ok) onConfirm();
    return;
  }
  Alert.alert(title, message, [
    { text: cancelLabel, style: 'cancel' },
    { text: confirmLabel, style: opts.destructive === false ? 'default' : 'destructive', onPress: onConfirm },
  ]);
}

/** A simple cross-platform notice (no choice) — web-safe replacement for Alert.alert(title, msg). */
export function notify(title: string, message?: string) {
  if (Platform.OS === 'web') {
    if (typeof window !== 'undefined') window.alert(message ? `${title}\n\n${message}` : title);
    return;
  }
  Alert.alert(title, message ?? '');
}
