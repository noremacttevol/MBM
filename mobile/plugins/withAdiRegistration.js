// Android developer-verification proof file.
//
// Google Play's "Manage package keys" asks us to prove we control the signing
// key for com.mbm.app. To do that, it gives an account-unique snippet that must
// live in the APK at  assets/adi-registration.properties , signed with our key.
// This plugin writes that file into the Android build at prebuild time so the
// EAS-built (preview) APK contains it. We then upload that signed APK to Google
// and it confirms ownership.
//
// The snippet below comes from Play Console → Android developer verification →
// Manage package keys → "How to sign an APK" (step 1, the copy box).

const { withDangerousMod } = require('@expo/config-plugins');
const fs = require('fs');
const path = require('path');

const SNIPPET = 'DHPVKH2O3WRY6AAAAAAAAAAAAA';

module.exports = function withAdiRegistration(config) {
  return withDangerousMod(config, [
    'android',
    (cfg) => {
      const assetsDir = path.join(
        cfg.modRequest.platformProjectRoot,
        'app', 'src', 'main', 'assets',
      );
      fs.mkdirSync(assetsDir, { recursive: true });
      fs.writeFileSync(
        path.join(assetsDir, 'adi-registration.properties'),
        SNIPPET + '\n',
      );
      return cfg;
    },
  ]);
};
