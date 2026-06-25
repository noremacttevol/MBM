#!/usr/bin/env python3
import os, sys, pexpect

env = os.environ.copy()
cwd = "/home/noremacttevol/Desktop/Brain/MBM/mobile"
env["EXPO_ASC_API_KEY_PATH"] = cwd + "/credentials/AuthKey_M73YLWD8YS.p8"
env["EXPO_ASC_KEY_ID"] = "M73YLWD8YS"
env["EXPO_ASC_ISSUER_ID"] = "9aa9c15a-4e7a-4726-928c-566664c43867"
env["EXPO_APPLE_TEAM_ID"] = "GS5KV3DM36"
env["EXPO_APPLE_TEAM_TYPE"] = "INDIVIDUAL"

child = pexpect.spawn(
    "npx eas-cli submit --platform ios --id 2d95853d-cf7a-4f5e-95f7-8117f10b2d51",
    cwd=cwd, env=env, encoding="utf-8", timeout=900, dimensions=(40, 120)
)
child.logfile = sys.stdout

patterns = [
    r"\(Y/n\)",                 # 0 confirm default yes
    r"\(y/N\)",                 # 1 confirm default no -> we say yes (create app)
    r"App name:",               # 2 text prompt, accept default
    r"Language:",               # 3 select, accept default
    r"Company name:",           # 4 text
    r"Apple ID:",               # 5
    r"successfully submitted",  # 6 done
    r"View your submission",    # 7 done URL
    r"Submission failed",       # 8 error
    pexpect.EOF,                # 9
    pexpect.TIMEOUT,            # 10
]

while True:
    i = child.expect(patterns)
    if i in (0, 1):
        child.sendline("y")
    elif i in (2, 3, 4, 5):
        child.sendline("")   # accept default
    elif i in (6, 7):
        child.expect([pexpect.EOF, pexpect.TIMEOUT])
        break
    elif i == 8:
        child.expect([pexpect.EOF, pexpect.TIMEOUT])
        break
    elif i == 9:
        break
    elif i == 10:
        print("\n[TIMEOUT]")
        break

child.close()
print("\n[EXIT STATUS]", child.exitstatus)
