# Publication Submission Workflow

The publication pipeline is **GitHub-native**: an issue form is the submission
form, a GitHub Action is the automation, and the issue itself is the status
tracker. No external services, credentials, or quotas.

```
Submission issue (form) ──▶ GitHub Action: validate + dedupe ──▶ branch + commit + PR
        │                        │                                       │
        │                   invalid / duplicate                         │ maintainer reviews
        │                   comment + label                             ▼
        ▼                                                     PR merged into base branch
 issue labeled pr-open ◀── PR link comment                          │
        │                                                            ▼
        └───── merge event: issue closed + labeled published ── GitHub Pages rebuild
                                                                    │
                                                                    ▼
                                                    live /publications.html
```

## Files

| File | Purpose |
|---|---|
| [`.github/ISSUE_TEMPLATE/publication-submission.yml`](../../.github/ISSUE_TEMPLATE/publication-submission.yml) | The submission form (GitHub issue form). |
| [`.github/workflows/publication-pr.yml`](../../.github/workflows/publication-pr.yml) | The automation triggers. |
| [`scripts/publication_workflow.py`](../../scripts/publication_workflow.py) | Validation, duplicate detection, entry formatting, PR creation, merge handling. |
| [`_data/publications.yml`](../../_data/publications.yml) | Canonical publication list (entries appended by the automation). |
| [`_pages/publications.html`](../../_pages/publications.html) | Publications page, grouped by year, newest first. |

## Documentation

- **[github-native-workflow.md](github-native-workflow.md)** — how to submit, maintain,
  test, and go live. Start here.
- **Alternative architecture (kept for reference):** the Google Form → Google Sheet →
  Make.com pipeline is fully documented in
  [01-google-form-setup.md](01-google-form-setup.md),
  [02-make-scenario-1.md](02-make-scenario-1.md),
  [03-make-scenario-2.md](03-make-scenario-2.md), and
  [04-testing-and-activation.md](04-testing-and-activation.md). Use it only if
  submitters must not need GitHub accounts and Make.com is preferred over a small
  Apps Script — the two paths are interchangeable behind `_data/publications.yml`.

## Status tracking (issue labels)

| Label | Meaning |
|---|---|
| `publication/pr-open` | Validated, PR created — awaiting review. |
| `publication/published` | PR merged; entry live on the site. |
| `publication/invalid` | Validation failed; reason posted as a comment. |
| `publication/duplicate` | Possible duplicate; flagged for manual review. |

Submitters are notified through GitHub (comments on their issue) — no email
infrastructure needed.
