import React from 'react';
import { registerRootComponent } from 'expo';
import { Text, TextInput } from 'react-native';
import { SafeAreaProvider } from 'react-native-safe-area-context';
import { useFonts } from 'expo-font';
import AppNavigator from './src/navigation/AppNavigator';

// The cross font is the single, forced typeface for the whole app. Every "t"
// renders as a Latin cross — Cameron's signature. We force it as the default on
// BOTH Text and TextInput so any text that doesn't name a font still gets it,
// and there is no user setting anywhere to turn it off. Icon components set
// their own (icon) fontFamily explicitly, so those are untouched.
const CROSS = 'MBMCross';

function forceCrossFont() {
  const T = Text as unknown as { defaultProps?: { style?: unknown } };
  T.defaultProps = T.defaultProps || {};
  T.defaultProps.style = [{ fontFamily: CROSS }, T.defaultProps.style];
  const TI = TextInput as unknown as { defaultProps?: { style?: unknown } };
  TI.defaultProps = TI.defaultProps || {};
  TI.defaultProps.style = [{ fontFamily: CROSS }, TI.defaultProps.style];
}
forceCrossFont();

function App() {
  // Embedded via the expo-font config plugin for native builds; useFonts is the
  // runtime guarantee for web / Expo Go. We render regardless — if the font is
  // still resolving, the system face shows for a beat, then snaps to the cross.
  useFonts({ [CROSS]: require('./assets/fonts/MBMCross-Regular.ttf') });

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
