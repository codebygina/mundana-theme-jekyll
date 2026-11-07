# GitHub-Native Publication Workflow — Runbook

Everything runs inside this repository: the form is a GitHub issue form, the
automation is a GitHub Action using the built-in `GITHUB_TOKEN` (no PAT, no
secrets to rotate), and each submission's status is tracked on its issue via
labels and comments.

## 1. How to submit a publication (contributor guide)

1. Go to **Issues → New issue → Publication Submission** (direct link:
   `https://github.com/AAII-Axom/AAII-Axom.github.io/issues/new/choose`).
2. Fill the form — title, authors, venue, type, year are required; DOI/URL/PDF/
   abstract/keywords optional (but at least one of DOI/URL/PDF is needed).
3. Submit. Within a minute the automation comments on the issue:
   - ✅ **Pull request created** + link → a maintainer reviews it; or
   - ⚠️ **needs fixes** (missing/invalid fields) → open a corrected new issue; or
   - 🔁 **possible duplicate** → a maintainer checks manually.
4. When the PR is merged, the issue is closed and labeled `published`, and the
   publication appears on `/publications.html` after the Pages rebuild (~1–2 min).

## 2. What the automation does (per submission)

| Step | Detail |
|---|---|
| Detect | Only issues containing the issue-form marker header are processed. |
| Validate | title/authors/venue/type/year present; year matches `(19|20)\d\d`; ≥1 of DOI/URL/PDF. A missing DOI alone never rejects. |
| Deduplicate | Against `_data/publications.yml` on the base branch: normalized DOI → normalized title → first author + year. Matches **flag** (`publication/duplicate`), never silently reject. |
| Branch | `publication/issue-<N>-<title-slug>` — unique per issue, so retried or identical titles can never collide. |
| Commit | Entry appended to the end of `_data/publications.yml`, schema-exact, quoting-safe (punctuation, Assamese, multi-line abstracts). Existing content is never touched. |
| PR | Title `[New Publication] <title> (<year>)`, body follows the standard template, references and closes the submission issue. |
| Merge | On PR merge: issue closed + labeled `publication/published`, head branch deleted, submitter notified. On close-without-merge: issue stays open with a note. |

Runs are serialized (`concurrency` group), so simultaneous submissions cannot
race on the data file.

## 3. One-time setup

Nothing is required to *build* — merging this branch is the setup. Two optional
settings:

- **Base branch variable** — the PR target is `test/publications` by default.
  At go-live set **Settings → Secrets and variables → Actions → Variables →
  New repository variable**: name `PUBLICATION_BASE_BRANCH`, value `master`.
  No code change needed.
- **Branch auto-delete** (cosmetic; the workflow deletes head branches anyway):
  Settings → General → Pull Requests → *Automatically delete head branches*.

The four `publication/*` labels are created automatically on first run.

## 4. Testing (before go-live)

Works entirely on `test/publications` — nothing can reach the live site:

1. Merge this scaffold branch into `master` (needs owner approval — see §5).
   The workflow is inert until someone opens a publication issue, and PRs
   target `test/publications` until the variable is flipped.
2. Open a test submission issue with a tricky title (quotes, punctuation,
   non-Latin author names) and full optional fields.
3. Expect within a minute: PR comment on the issue, `publication/pr-open`
   label, PR open against `test/publications` whose diff touches only
   `_data/publications.yml` with one appended entry.
4. Error paths: file a second issue with the **same DOI** (expect
   `publication/duplicate`, no PR) and one missing required fields (expect
   `publication/invalid` with reasons).
5. Review + merge the test PR → issue auto-closes with the 🎉 comment and
   `publication/published` label.
6. Render check: locally `git fetch && git checkout test/publications &&
   bundle exec jekyll serve` → `/publications.html` shows the entry grouped by
   year.
7. Clean up: delete the test issue (or close it) and the merged branch — or
   keep them as the first real examples.

## 5. Go-live

1. Ensure §4 passed (with the scaffold already on `master`).
2. Set `PUBLICATION_BASE_BRANCH=master` (§3) — from this moment every
   submission PR targets the live branch.
3. Smoke-test once more with a real publication; merging it publishes it.
4. Announce the issue-form link to faculty/collaborators.

## 6. Maintainer guide

| Situation | Action |
|---|---|
| PR needs a correction | Either push a commit to the PR branch, or close the PR (issue re-opens itself for re-review) and ask for a corrected submission. |
| `publication/duplicate` flagged wrongly | Remove the label, open the PR manually from the flagged issue's data (or resubmit), and explain in a comment. |
| Submitter has no GitHub account | A maintainer opens the issue form on their behalf and puts their name in *Submitted by* — the entry records that name. |
| Automation run failed (red ✗ on an issue) | Check the run log (Actions tab). The issue comment explains nothing was lost — fix and re-open a new issue, or rerun the failed job. |
| Editing a published entry | Ordinary PR against `_data/publications.yml` — schema is documented in the file header. |

## 7. Security notes

- Submitter input is escaped into YAML via JSON-string quoting — quotes,
- colons, newlines, and non-Latin scripts are safe; injected `### ` headers can
  at most truncate a textarea field.
- The workflow token is scoped job-implicitly to `contents`, `issues`,
  `pull-requests` — write access is limited to this repository.
- Issue bodies are read from the event file (`GITHUB_EVENT_PATH`), not shell
  interpolation, so submission text cannot inject workflow commands.
