# ops/ — one-time fixes that need Cameron's credentials

## Install the Pages deploy workflow (fixes the frozen Reviewer/site)

The legacy GitHub-Pages builder clones the ENTIRE repo and dies on our
committed video mass ("Page build failed" all morning of 2026-08-31, again —
see docs/.nojekyll for the last time). The permanent fix is deploying docs/
via Actions with a sparse checkout, but pushing a workflow file requires the
`workflow` OAuth scope, which the machine tokens don't have.

**Cameron (or any terminal with his GitHub login), run once from the repo:**

```bash
mkdir -p .github/workflows && cp ops/pages-workflow-INSTALL-ME.yml .github/workflows/pages.yml && git add .github/workflows/pages.yml && git commit -m "Pages: deploy docs/ via Actions (sparse checkout)" && git push
```

Then any session (or Cameron) flips Pages to workflow builds:

```bash
gh api -X PUT repos/noremacttevol/MBM/pages -f build_type=workflow
```

Until that lands, the live reviewer serves its last good deploy (the 200
cards work; the new GREAT PLAN folder doesn't show). Interim: open
`~/Desktop/MBM-REVIEWER-FRESH.html` — the identical page from a local file;
Approve/Report and all videos work exactly the same (Firestore + raw GitHub
don't depend on Pages).
