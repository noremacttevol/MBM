#!/usr/bin/env python3
import os
import sys
import pexpect

env = os.environ.copy()
cwd = "/home/noremacttevol/Desktop/MBM/mobile"
env["EXPO_ASC_API_KEY_PATH"] = cwd + "/credentials/AuthKey_M73YLWD8YS.p8"
env["EXPO_ASC_KEY_ID"] = "M73YLWD8YS"
env["EXPO_ASC_ISSUER_ID"] = "9aa9c15a-4e7a-4726-928c-566664c43867"
env["EXPO_APPLE_TEAM_ID"] = "GS5KV3DM36"
env["EXPO_APPLE_TEAM_TYPE"] = "INDIVIDUAL"
env["EAS_BUILD_NO_EXPO_GO_WARNING"] = "true"

child = pexpect.spawn(
    "npx eas-cli build --platform ios --profile production --no-wait",
    cwd=cwd, env=env, encoding="utf-8", timeout=600, dimensions=(40, 120)
)
child.logfile = sys.stdout

patterns = [
    r"\(Y/n\)",                       # 0 confirm yes-default
    r"\(y/N\)",                       # 1 confirm no-default
    r"Build details:",               # 2 success marker (URL printed)
    r"https://expo\.dev/accounts",   # 3 build queued URL
    r"Waiting for build",            # 4
    pexpect.EOF,                      # 5
    pexpect.TIMEOUT,                  # 6
]

while True:
    i = child.expect(patterns)
    if i in (0, 1):
        child.sendline("y")
    elif i in (2, 3, 4):
        # build was queued; keep reading until EOF
        child.expect([pexpect.EOF, pexpect.TIMEOUT])
        break
    elif i == 5:
        break
    elif i == 6:
        print("\n[TIMEOUT waiting for prompt]")
        break

child.close()
print("\n[EXIT STATUS]", child.exitstatus)
