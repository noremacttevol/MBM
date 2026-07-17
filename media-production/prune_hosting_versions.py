#!/usr/bin/env python3
"""Free Firebase Hosting storage so `firebase deploy` stops 429-ing.

WHY: site/ is ~650MB (story-videos the app streams). Every deploy stores a
full copy as a new hosting version; the free tier caps total version storage
at 10GB, so ~15 deploys (across ALL assembly sessions) fill it and every
later deploy fails with HTTP 429 "exceeded the Hosting storage quota".

WHAT IT DOES: deletes every FINALIZED version except the one the live
channel currently serves (the site stays up), using the firebase-tools CLI's
own stored credentials. Run it whenever a deploy 429s, then deploy again:

    python3 media-production/prune_hosting_versions.py && firebase deploy --only hosting

(ASSEMBLY-D, 2026-07-17. The live channel also has retainedReleaseCount=3
set, but versions from rapid multi-session deploys pile up faster than that
prunes them.)
"""
import json
import os
import urllib.parse
import urllib.request

SITE = "milk-b4-meat"
# firebase-tools' public OAuth client (embedded in the open-source CLI)
CLIENT_ID = "563584335869-fgrhgmd47bqnekij5i8b5pr03ho849e6.apps.googleusercontent.com"
CLIENT_SECRET = "j9iVZfS8kkCEFUPaAeJV0sAi"


def access_token():
    cfg = json.load(open(os.path.expanduser(
        "~/.config/configstore/firebase-tools.json")))
    data = urllib.parse.urlencode({
        "client_id": CLIENT_ID, "client_secret": CLIENT_SECRET,
        "refresh_token": cfg["tokens"]["refresh_token"],
        "grant_type": "refresh_token"}).encode()
    return json.load(urllib.request.urlopen(urllib.request.Request(
        "https://oauth2.googleapis.com/token", data=data)))["access_token"]


def main():
    tok = access_token()

    def api(path, method="GET"):
        req = urllib.request.Request(
            "https://firebasehosting.googleapis.com/v1beta1/" + path,
            method=method,
            headers={"Authorization": "Bearer " + tok,
                     "Content-Type": "application/json"})
        r = urllib.request.urlopen(req)
        body = r.read()
        return json.loads(body) if body else {}

    live_ver = api(f"sites/{SITE}/channels/live")["release"]["version"]["name"]
    versions, page = [], None
    while True:
        q = f"sites/{SITE}/versions?pageSize=100" + (f"&pageToken={page}" if page else "")
        r = api(q)
        versions += r.get("versions", [])
        page = r.get("nextPageToken")
        if not page:
            break
    deleted = 0
    for v in versions:
        if v["status"] == "FINALIZED" and v["name"] != live_ver:
            api(v["name"], method="DELETE")
            deleted += 1
    print(f"pruned {deleted} old versions; live version kept: {live_ver.split('/')[-1]}")


if __name__ == "__main__":
    main()
