# 04 — End-to-End Testing & Production Activation

## Part A — Preconditions checklist

Before test 1, confirm:

- [ ] Branch `test/publications` exists in the repo with `_data/publications.yml`,
      `_pages/publications.html`, the nav link, and these docs (the scaffold this
      workflow shipped on).
- [ ] Google Form + response sheet exist with columns A–S exactly as in
      doc 01 (tracking headers `Status`…`Notes` in N–S).
- [ ] Scenario 1 and Scenario 2 are fully built in Make.
- [ ] **Scheduling is OFF for both scenarios** — testing uses *Run once*.
- [ ] Fine-grained PAT created and pasted into the five HTTP header sets of Scenario 1.
- [ ] Webhook added in GitHub and the M1 data structure determined (doc 03 §1).
- [ ] Both scenarios' base-branch references still say `test/publications`.

All test PRs target `test/publications`, so **nothing here can reach the live site**.
Merging test PRs into `test/publications` is pre-approved; merging anything into
`master` is not — that happens only in Part C with the owner's explicit go-ahead.

## Part B — Test pass (maps to the 10 required checks)

| # | Test | Steps | Expected result |
|---|---|---|---|
| 1 | Form → Sheet | Fill the form with a realistic sample (title with punctuation, e.g. `A "Quoted" Study of Speech Models`, several authors, DOI, URL, PDF, abstract, keywords) and submit | Row appears in `Form Responses 1` with A–M filled, N–S empty |
| 2 | Detection + validation | Scenario 1 → **Run once** | Run processes 1 row; inspector shows F1 passed, M2 `issues` empty; row `Status` still empty until Route 3 completes |
| 3 | PR creation | Continue inspecting modules 3→14 | Branch `publication/<timestamp>-a-quoted-study-of-speech-models…` exists in GitHub; commit message `Add publication: …`; PR open against `test/publications`; **Files changed shows only `_data/publications.yml`, one appended entry**; row now `PR Created` with number/URL/branch |
| 4 | YAML integrity | Open the PR's file diff | Entry matches the schema: quoted strings, unquoted 4-digit year, keys in canonical order, quotes in the title intact; previous content unchanged |
| 5 | Duplicate detection | Submit the **same DOI** again (any title) → Run once | No branch/PR; row `Duplicate – needs review`, Notes names the DOI match. Also try the same title with a different DOI — expect a duplicate flag from the title rule |
| 6 | Invalid data | Submit with venue blank and year `25` (Form validation blocks bad years in UI — submit via the form's "edit response" or temporarily relax to test the backstop) → Run once | No branch/PR; row `Invalid – needs review`, Notes lists both problems |
| 7 | Missing-DOI acceptance | Submit a valid paper with **no DOI** but a URL → Run once | PR **is** created (missing DOI alone never rejects) |
| 8 | Optional fields | Submit a minimal paper (no DOI/URL/PDF/abstract/keywords except one URL) | PR created; entry omits absent optional keys entirely |
| 9 | Merge flow | Review + merge the PR from tests 3/7/8 into `test/publications` | Scenario 2 fires within seconds; row `Merged` with merge time in Notes; optional submitter email received |
| 10 | Rendered result | Locally: `git fetch && git checkout test/publications && bundle exec jekyll serve` → open `http://127.0.0.1:4000/publications.html` | Entries grouped under year headings (newest year first), authors italic venue line, DOI/Publisher/PDF links, keywords as chips, nav *Publications* link works; Assamese characters render correctly |

**Also verify once — concurrency guard**: submit two different papers back-to-back and
Run once; both PRs must exist independently and both entries must be present after both
merges (append + compare-and-swap protect this).

### If something fails

- Module red in the inspector → open its input/output; the usual suspects are the
  `<LINE BREAK>` separator (doc 02 §5.1) and boolean filter values (§5.2).
- A half-processed row (error after branch creation but before M14): fix the module,
  then either resume the incomplete execution or manually clear the row's Status and
  delete the orphan branch before re-running.
- Nothing processes: check F1 (a leftover test value in `Status`), and that the sheet
  tab is exactly `Form Responses 1`.

## Part C — Production activation (requires owner approval)

Run only after Part B passes fully. Ordered:

1. **Publish the scaffold** — open a PR `test/publications` → `master` containing
   `_data/publications.yml` (empty header), `_pages/publications.html`, the nav link,
   and `docs/publication-workflow/`. **Merge only with the owner's explicit approval.**
   The live site now shows an empty publications page — expected.
2. **Clean up test artifacts** — close any leftover test PRs and delete
   `publication/*` test branches (GitHub → Branches, or `git push origin --delete <branch>`).
   Keep the `test/publications` branch itself for future workflow testing.
3. **Re-point to production** — exactly four places:
   - Scenario 1 / M3 query `ref`: `test/publications` → `master`
   - Scenario 1 / M9 URL `git/ref/heads/…`: → `master`
   - Scenario 1 / M13 body `"base"`: → `master`
   - Scenario 2 / F1 condition `base.ref`: → `master`
4. **Activate** — turn Scheduling **ON** for both scenarios (free plan: exactly 2 active
   scenarios — no room for others). Scenario 1 clock: every 2 hours.
5. **Smoke-test production** — submit one real publication through the form, confirm the
   PR targets `master`, review and merge it (this one *is* the approval), watch the row
   reach `Merged`, and see it appear on `https://aaii-axom.github.io/publications.html`
   after the Pages rebuild (~1–2 min).
6. **Announce** — share the form link with faculty/collaborators.

### Optional hardening (any time)

- **Labels**: create a `publication` label in the repo; Scenario 1 gains one HTTP POST
  `repos/…/issues/{number}/labels` (issue labels API covers PRs) — or maintainers add it
  manually on review.
- **Reviewers**: POST `repos/…/pulls/{number}/requested_reviewers` with a chosen
  reviewer list; skip if the team prefers triage via notifications.
- **Branch protection on master**: require a PR + 1 approval before merge — aligns the
  repo itself with the workflow's review-first design.
- **PAT rotation**: fine-grained tokens expire (90 days recommended) — calendar it; the
  edit is 5 header values in Scenario 1.

## Operations quick reference

| Task | Where |
|---|---|
| Watch runs / errors | Make → scenario → *History* |
| Monthly op budget | Make → scenario → *Insights* (design budget: ~480 of 1,000 ops/month) |
| Who submitted what | Response sheet columns A–M (immutable original + timestamp) |
| Submission state machine | `Status` column: empty → `PR Created` → `Merged` (or `Invalid`/`Duplicate – needs review`) |
| Failed webhook delivery | GitHub → Settings → Webhooks → Recent deliveries → *Redeliver* |
| Recover a stuck row | Clear `Status` in the sheet → next cycle reprocesses |
