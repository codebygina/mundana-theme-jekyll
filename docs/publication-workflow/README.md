# Publication Submission Workflow

End-to-end automation that turns Google Form submissions into reviewed GitHub Pull
Requests, and merges them into the AAII-Axom publication list.

```
Google Form ──▶ Google Sheet ──▶ Make.com Scenario 1 ──▶ GitHub branch + commit + PR
                                      │                         │
                                      │ (status: PR Created)    │ maintainers review & merge
                                      ▼                         ▼
                                 Google Sheet ◀── Make.com Scenario 2 (merge webhook)
                                 (status: Merged)              │
                                                              ▼
                                              GitHub Pages rebuilds ──▶ live /publications.html
```

## Repository changes (this branch)

| File | Purpose |
|---|---|
| `_data/publications.yml` | Canonical publication list (YAML). Entries are inserted below the `# ENTRIES (newest first)` marker. |
| `_pages/publications.html` | Jekyll page rendering the list grouped by year, newest first, at `/publications.html`. |
| `_includes/menu-header.html` | Adds a **Publications** nav link. |
| `docs/publication-workflow/` | These runbooks. |

Nothing is ever committed to `master` automatically — every entry arrives via a
Pull Request that a maintainer reviews and merges.

## Documentation index

1. **[01-google-form-setup.md](01-google-form-setup.md)** — create the form, the linked
   response spreadsheet, and the tracking columns.
2. **[02-make-scenario-1.md](02-make-scenario-1.md)** — build *Submission → Pull Request*:
   trigger, validation, duplicate detection, GitHub branch/commit/PR, sheet updates.
3. **[03-make-scenario-2.md](03-make-scenario-2.md)** — build *Merge Tracker*: webhook
   detection of merged PRs, sheet status updates, submitter notification.
4. **[04-testing-and-activation.md](04-testing-and-activation.md)** — end-to-end test plan
   and the production go-live checklist.

## Prerequisites

| Requirement | Detail |
|---|---|
| Make.com account | Free plan works (2 active scenarios = exactly our 2 scenarios; ~480 of 1,000 ops/month at realistic volume). |
| GitHub fine-grained PAT | Scoped to **only** `AAII-Axom/AAII-Axom.github.io` — permissions: *Contents: Read and write*, *Pull requests: Read and write*, *Metadata: Read* (forced). See 02-make-scenario-1.md §2. |
| Google account | Owner of the form + response sheet (Google Sheets and Gmail connections in Make use it). |
| Repo admin (once) | To add one webhook for merge detection (Scenario 2). |

## Free-plan constraints (design decisions)

- **Polling every 2 hours** for new rows (not 15 min): a 15-minute schedule would burn
  ~2,880 ops/month on polling alone; every 2 h costs ~360. Publications are not
  time-critical.
- **Webhook-driven merge tracking** (not polling): merge events cost ~1 op each instead
  of scheduled API calls.
- **MCP note**: scenario *management* tools in Make's MCP server require a paid plan, so
  these runbooks configure everything manually in the Make UI. Every field value is
  spelled out — no guessing.

## Status values written to the sheet

| Status | Meaning |
|---|---|
| *(empty)* | Not yet processed. |
| `PR Created` | Branch, commit and PR exist; awaiting review. |
| `Merged` | PR merged into the base branch; entry is live after the Pages rebuild. |
| `Invalid – needs review` | Validation failed; reason in *Notes*. No PR created. |
| `Duplicate – needs review` | Possible duplicate; reason in *Notes*. No PR created. |
