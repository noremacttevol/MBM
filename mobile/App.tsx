import React from 'react';
import { registerRootComponent } from 'expo';
import { Text, TextInput } from 'react-native';
import { SafeAreaProvider } from 'react-native-safe-area-context';
import {
  useFonts,
  Jost_400Regular,
  Jost_400Regular_Italic,
  Jost_600SemiBold,
} from '@expo-google-fonts/jost';
import AppNavigator from './src/navigation/AppNavigator';

// Jost is the app's typeface. Its lowercase "t" is a straight vertical with a
// flat bottom — no curve/hook (Cameron's ask). Set as the default on Text and
// TextInput so any text that doesn't name a font picks it up too.
function setDefaultFont() {
  const T = Text as unknown as { defaultProps?: { style?: unknown } };
  T.defaultProps = T.defaultProps || {};
  T.defaultProps.style = [{ fontFamily: 'Jost_400Regular' }, T.defaultProps.style];
  const TI = TextInput as unknown as { defaultProps?: { style?: unknown } };
  TI.defaultProps = TI.defaultProps || {};
  TI.defaultProps.style = [{ fontFamily: 'Jost_400Regular' }, TI.defaultProps.style];
}
setDefaultFont();

function App() {
  // Load Jost (embedded in native builds via expo-font, loaded at runtime on web).
  // We render regardless of the loaded flag so there's never a blank screen — text
  // shows in the system face for a beat, then snaps to Jost.
  useFonts({ Jost_400Regular, Jost_400Regular_Italic, Jost_600SemiBold });

  // SafeAreaProvider supplies the real device insets (status bar at the top,
  // the gesture/button nav bar at the bottom) so nothing the app draws hides
  // behind the system UI. Phones without an on-screen nav bar simply report a
  // zero bottom inset, so the same code uses the full screen there.
  return (
    <SafeAreaProvider>
      <AppNavigator />
    </SafeAreaProvider>
  );
}

registerRootComponent(App);

export default App;
