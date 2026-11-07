# 02 — Make.com Scenario 1: *Publication Submission → Pull Request*

> **Why manual**: Make's MCP *management* tools (scenario creation) require a paid
> plan, so this runbook configures every module by hand in the Make UI. Follow it
> top-to-bottom; every field value is given. Nothing here touches `master` — while
> testing, the base branch is `test/publications`.

## Scenario overview

```
M1 Watch New Rows ──F1 Status empty──▶ M2 Normalize & validate ──▶ M3 GET publications.yml (raw)
                                                                      │
                                              M4 Duplicate flags + YAML entry ──▶ M5 New file content + branch name
                                                                      │
                                    ┌─────────────────────────────────┴── Router ──┐
                              Route 1: Invalid                     Route 2: Duplicate          Route 3: Valid
                              M6 Update Row (flag)                 M7 Update Row (flag)        M9  GET base ref SHA
                                                                  M8 Gmail admin (optional)   M10 POST create branch
                                                                                              M11 GET file sha (branch)
                                                                                              M12 PUT commit entry
                                                                                              M13 POST create PR
                                                                                              M14 Update Row (PR Created)
                                                                                              M15 Gmail submitter (opt.)
```

**Module count**: 15 (2 optional) · **Operations per valid submission**: ~11 · **Polling**: every 2 h ≈ 360 ops/month.

## 1. Connections (create once)

| Connection | Where | Notes |
|---|---|---|
| Google Sheets | Add module → *Google Sheets* → Create a connection → Google OAuth | Use the account that owns the response spreadsheet. |
| Gmail | Same flow for the *Gmail* app | Only needed if you enable M8/M15. |

## 2. GitHub fine-grained PAT (least privilege)

1. GitHub → **Settings → Developer settings → Personal access tokens → Fine-grained tokens → Generate new token**.
2. **Repository access**: *Only select repositories* → `AAII-Axom/AAII-Axom.github.io`.
3. **Permissions**: `Contents: Read and write`, `Pull requests: Read and write` (`Metadata: Read` is added automatically). Nothing else.
4. **Expiration**: 90 days (calendar a renewal; rotating is a 1-line edit in 5 HTTP headers).
5. The token is used as a header `Authorization: Bearer github_pat_…` in the HTTP modules.
   ⚠️ Scenario editors in your Make team can read header values — the single-repo,
   contents+PR-only scope is the compensating control. For stricter needs, use the
   `HTTP → Make an OAuth 2.0 Request` module with a GitHub OAuth connection instead
   (same URLs/bodies).

## 3. Build the scenario

Create scenario → name it `Publication Submission → PR`.

### M1 — Google Sheets ▸ Watch New Rows *(trigger)*

| Setting | Value |
|---|---|
| Connection | your Google Sheets connection |
| Spreadsheet | `AAII-Axom Publication Submission (Responses)` |
| Sheet name | `Form Responses 1` |
| Contains headers | `Yes` |
| Limit | `10` |

**Scheduling** (clock icon): *At regular intervals* → **every 2 hours** (free-plan op budget; see README).

### F1 — Filter between M1 and M2 · label `Not yet processed`

| Condition | Operator | Value |
|---|---|---|
| `{{1.Status}}` | Text: *Equal to* | *(leave empty)* |

This is the double-PR guard: rows the scenario already processed have a Status and are skipped, even if re-fetched.

### M2 — Tools ▸ Set multiple variables · label `Normalize & validate`

Create each variable (name → value formula):

| Variable | Value |
|---|---|
| `esc_title` | `{{replace(replace(trim(1."Publication title"); "\\"; "\\\\"); "\""; "\\\"")}}` |
| `esc_authors` | `{{replace(replace(trim(1.Authors); "\\"; "\\\\"); "\""; "\\\"")}}` |
| `esc_venue` | `{{replace(replace(trim(1."Publication venue"); "\\"; "\\\\"); "\""; "\\\"")}}` |
| `esc_abstract` | `{{replace(replace(trim(1.Abstract); "\\"; "\\\\"); "\""; "\\\"")}}` |
| `esc_submitted_by` | `{{replace(replace(trim(1."Submitted by"); "\\"; "\\\\"); "\""; "\\\"")}}` |
| `type_norm` | `{{if(contains(lower(trim(1."Publication type")); "journal"); "journal"; if(contains(lower(trim(1."Publication type")); "conference"); "conference"; if(contains(lower(trim(1."Publication type")); "workshop"); "workshop"; if(contains(lower(trim(1."Publication type")); "book"); "book-chapter"; "other"))))}}` |
| `pub_year` | `{{trim(1.Year)}}` |
| `date_added` | `{{formatDate(now; "YYYY-MM-DD")}}` |
| `norm_doi` | `{{lower(trim(replace(replace(replace(replace(replace(1.DOI; "https://doi.org/"; ""); "http://doi.org/"; ""); "https://dx.doi.org/"; ""); "doi:"; ""); " "; "")))}}` |
| `norm_title` | `{{lower(trim(replace(1."Publication title"; "/[^a-zA-Z0-9]+/"; " ")))}}` |
| `first_author_l` | `{{lower(trim(get(split(1.Authors; ","); 1)))}}` |
| `slug_full` | `{{lower(replace(replace(trim(1."Publication title"); "/[^a-zA-Z0-9]+/"; "-"); "/^-+|-+$/"; ""))}}` |
| `title_json` | `{{escapeJSON(trim(1."Publication title"))}}` *(see note 3 below)* |

`issues` — paste this as one value (Make concatenates the mapped expressions; each yields
empty string or a message, so `length(issues) = 0` means valid):

```
{{if(empty(trim(1."Publication title")); "Missing publication title. "; "")}}{{if(empty(trim(1.Authors)); "Missing authors. "; "")}}{{if(empty(trim(1."Publication venue")); "Missing venue. "; "")}}{{if(empty(trim(1."Publication type")); "Missing publication type. "; "")}}{{if(not(empty(trim(1.Year))); if(match("/^(19|20)[0-9]{2}$/"; trim(1.Year)); ""; "Year is not a valid 4-digit year (1900–2099). "); "Missing year. ")}}{{if(and(empty(trim(1.DOI)); and(empty(trim(1."Publication URL")); empty(trim(1."PDF URL")))); "No identifier: provide at least one of DOI, publication URL, or PDF URL. "; "")}}
```

Validation semantics (per spec): title/authors/venue/type/year required; year must match
`(19|20)\d\d`; **at least one** of DOI / publication URL / PDF URL must exist — a missing
DOI alone never rejects a submission.

### M3 — HTTP ▸ Make a request · label `GET current publications file (raw)`

| Setting | Value |
|---|---|
| Method | `GET` |
| URL | `https://api.github.com/repos/AAII-Axom/AAII-Axom.github.io/contents/_data/publications.yml` |
| Query string | `ref` = `test/publications` *(→ `master` at go-live — spot 1/3)* |
| Headers | `Authorization: Bearer <PAT>` · `Accept: application/vnd.github.raw+json` · `X-GitHub-Api-Version: 2022-11-28` |
| Parse response | **No** (we consume `{{3.data}}` as raw text) |
| Error handler | **Ignore** (tolerates a not-yet-existing file) |

This fetch doubles as the duplicate-check source — it is read **fresh on every run**, so
entries merged minutes ago are already covered.

### M4 — Tools ▸ Set multiple variables · label `Duplicate flags + YAML entry`

| Variable | Value |
|---|---|
| `dupe_doi` | `{{if(empty(2.norm_doi); false; contains(lower(toString(3.data)); 2.norm_doi))}}` |
| `dupe_title` | `{{if(empty(2.norm_title); false; contains(lower(toString(3.data)); 2.norm_title))}}` |
| `dupe_weak` | `{{if(empty(2.first_author_l); false; if(contains(lower(toString(3.data)); 2.first_author_l); if(contains(lower(toString(3.data)); 2.pub_year); true; false); false))}}` |

`entry_yaml` — a `join()` whose separator is a **real line break** (see note 1). Empty
optional fields contribute blank array elements, which simply render as blank YAML lines:

```
{{join(array("- title: \"" + 2.esc_title + "\""; "  authors: \"" + 2.esc_authors + "\""; "  venue: \"" + 2.esc_venue + "\""; "  type: \"" + 2.type_norm + "\""; "  year: " + 2.pub_year; if(empty(trim(1.DOI)); ""; "  doi: \"" + trim(1.DOI) + "\""); if(empty(trim(1."Publication URL")); ""; "  url: \"" + trim(1."Publication URL") + "\""); if(empty(trim(1."PDF URL")); ""; "  pdf: \"" + trim(1."PDF URL") + "\""); if(empty(trim(1.Abstract)); ""; "  abstract: \"" + 2.esc_abstract + "\""); if(empty(trim(1.Keywords)); ""; "  keywords: \"" + trim(1.Keywords) + "\""); "  submitted_by: \"" + 2.esc_submitted_by + "\""; "  date_added: \"" + 2.date_added + "\""); "<LINE BREAK>")}}
```

Matching precedence matches the spec: DOI (exact, normalized) → normalized title
(substring, so it errs toward flagging) → first author + year (weak signal). All
duplicates **flag for manual review**; nothing is auto-rejected.

### M5 — Tools ▸ Set multiple variables · label `New file content + branch name`

| Variable | Value |
|---|---|
| `new_content` | `{{toString(3.data) + "<LINE BREAK>" + "<LINE BREAK>" + 4.entry_yaml}}` |
| `branch_name` | `{{"publication/" + formatDate(1.Timestamp; "YYYYMMDD-HHmm") + if(empty(2.slug_full); ""; "-" + substring(2.slug_full; 0; if(greater(length(2.slug_full); 40); 40; length(2.slug_full))))}}` |

Appending at the end is deliberate: the page sorts by year, and append can never
overwrite or reorder existing entries. The branch name embeds the submission timestamp,
so even two identical titles can never collide on a branch name.

### Router — 3 routes (order matters; set Route 1 and Route 2 filters, leave Route 3 as fallback)

**Route 1 · `Invalid`** (priority 1):

| Condition | Operator | Value |
|---|---|---|
| `{{length(2.issues)}}` | Numeric: *greater than* | `0` |

**Route 2 · `Duplicate`** (priority 2, conditions joined with **OR**):

| Condition | Operator | Value |
|---|---|---|
| `{{4.dupe_doi}}` | Equal to | `true` |
| `{{4.dupe_title}}` | Equal to | `true` |
| `{{4.dupe_weak}}` | Equal to | `true` |

**Route 3 · `Valid`** — no filter (fallback).

### Route 1 → M6 — Google Sheets ▸ Update a Row

Key: Row number = `{{1.__ROW_NUMBER__}}` · Spreadsheet/sheet as in M1.

| Column | Value |
|---|---|
| `Status` | `Invalid – needs review` |
| `Processed At` | `{{now}}` |
| `Notes` | `{{2.issues}}` |

### Route 2 → M7 — Google Sheets ▸ Update a Row

| Column | Value |
|---|---|
| `Status` | `Duplicate – needs review` |
| `Processed At` | `{{now}}` |
| `Notes` | `{{if(4.dupe_doi; "DOI already in list. "; "")}}{{if(4.dupe_title; "Similar title already in list. "; "")}}{{if(4.dupe_weak; "Same first author + year already in list. "; "")}}Verify manually, then resubmit or ignore.` |

### Route 2 → M8 — Gmail ▸ Send an email *(optional)*

To: `ADMIN_EMAIL` · Subject: `Publication submission flagged for review` · Content: map
title, submitter, reason (`{{2.issues}}{{7.Notes}}`), and a link to the spreadsheet.

### Route 3 → M9 — HTTP ▸ Make a request · `GET base branch SHA`

| Setting | Value |
|---|---|
| Method / URL | `GET https://api.github.com/repos/AAII-Axom/AAII-Axom.github.io/git/ref/heads/test/publications` *(→ `master` at go-live — spot 2/3)* |
| Headers | `Authorization: Bearer <PAT>` · `Accept: application/vnd.github+json` · `X-GitHub-Api-Version: 2022-11-28` |
| Parse response | Yes (JSON) — gives `{{9.object.sha}}` |

### Route 3 → M10 — HTTP ▸ Make a request · `POST create branch`

URL: `https://api.github.com/repos/AAII-Axom/AAII-Axom.github.io/git/refs` · same headers · Body type **Raw → JSON**:

```json
{
  "ref": "refs/heads/{{5.branch_name}}",
  "sha": "{{9.object.sha}}"
}
```

If the branch already exists (409/422 — e.g. two submissions in the same minute) the
error handler below retries the whole chain on the next cycle with a new timestamp.

### Route 3 → M11 — HTTP ▸ Make a request · `GET file sha on new branch`

| Setting | Value |
|---|---|
| Method / URL | `GET https://api.github.com/repos/AAII-Axom/AAII-Axom.github.io/contents/_data/publications.yml` |
| Query string | `ref` = `{{5.branch_name}}` |
| Headers | as M9 |
| Parse response | Yes (JSON) — gives `{{11.sha}}` |
| Error handler | **Ignore** (404 → first-ever file on a branch) |

### Route 3 → M12 — HTTP ▸ Make a request · `PUT commit entry`

URL: `https://api.github.com/repos/AAII-Axom/AAII-Axom.github.io/contents/_data/publications.yml` · headers as M9 · Body type **Raw → JSON**:

```json
{
  "message": "Add publication: {{2.title_json}} ({{2.pub_year}})",
  "content": "{{encode64(5.new_content)}}",
  "branch": "{{5.branch_name}}",
  "sha": {{if(empty(11.sha); "null"; "\"" + 11.sha + "\"")}}
}
```

The `sha` line makes the commit a *compare-and-swap* against the version read in M11 —
GitHub rejects the PUT (409) if the file changed in between, which is exactly the
protection against overwriting concurrent entries. The inline `if` emits JSON `null`
when M11 was ignored (file creation).

### Route 3 → M13 — HTTP ▸ Make a request · `POST create pull request`

URL: `https://api.github.com/repos/AAII-Axom/AAII-Axom.github.io/pulls` · headers as M9 · Body type **Raw → JSON** (newlines are written as `\n` — this is valid JSON; do **not** paste literal line breaks inside a JSON string):

```json
{
  "title": "[New Publication] {{2.title_json}} ({{2.pub_year}})",
  "head": "{{5.branch_name}}",
  "base": "test/publications",
  "body": "## New Publication Submission\n\nA new publication has been submitted through the Google Form.\n\n### Publication Details\n\n- **Title:** {{2.title_json}}\n- **Authors:** {{escapeJSON(1.Authors)}}\n- **Venue:** {{escapeJSON(1."Publication venue")}}\n- **Type:** {{2.type_norm}}\n- **Year:** {{2.pub_year}}\n- **DOI:** {{escapeJSON(trim(1.DOI))}}\n- **Paper URL:** {{escapeJSON(trim(1."Publication URL"))}}\n\n### Changes\n- Appended the publication to `_data/publications.yml` (canonical list).\n- Rendering, ordering and existing entries untouched — page sorts by year.\n\n### Submitted By\n- **Name:** {{escapeJSON(1."Submitted by")}}\n\n### Review Checklist\n- [ ] Publication details are accurate.\n- [ ] Author order and spelling are correct.\n- [ ] Publication is not already listed.\n- [ ] Formatting follows repository conventions.\n\n<sub>Submitted via the publication-submission workflow. Submitter email is stored in the response sheet, not shown here.</sub>"
}
```

*(→ `"base"` becomes `master` at go-live — spot 3/3.)* The submitter's **email is
intentionally excluded** from the public PR; reviewers find it in the response sheet,
keeping personal data off the public repository.

### Route 3 → M14 — Google Sheets ▸ Update a Row

| Column | Value |
|---|---|
| `Status` | `PR Created` |
| `PR Number` | `{{13.number}}` |
| `PR URL` | `{{13.html_url}}` |
| `Branch` | `{{5.branch_name}}` |
| `Processed At` | `{{now}}` |

### Route 3 → M15 — Gmail ▸ Send an email *(optional)*

To: `{{1."Submitter email"}}` · Subject: `Your publication submission is under review` ·
Content: thank-you + `{{13.html_url}}` (link to follow the review status).

## 4. Error handling & reliability

| Concern | Implementation |
|---|---|
| Transient GitHub errors / rate limits | On **M3, M9, M10, M12, M13** add error handler ▸ **Break**: attempts `2`, interval `60 s`. (Authenticated REST budget is 5,000 req/h — we use ~5 per submission — so Break is a safety net, not a routine path.) |
| Branch-name collision | Timestamped branch names (M5) make collisions near-impossible; if one still occurs, M10 errors, the run lands in incomplete executions, and the row's empty Status re-queues it. |
| Concurrent modification of the list | M12's `sha` compare-and-swap (see above). |
| Failed runs | Scenario settings (checkmark tab) ▸ enable **Allow storing of incomplete executions** ▸ *Sequential processing* ON. A crashed submission resumes from the failed module instead of restarting. |
| Double PRs for one submission | Three layers: Watch-Rows cursor + F1 Status-empty filter + Status written in every route. |
| Logs | Every row's `Status`/`Notes`/`Processed At` = business log; Make's *Scenario history* = technical log. |
| Credentials | OAuth connections for Google; single-repo fine-grained PAT for GitHub (see §2). |

## 5. Implementation notes (read before first run)

1. **`<LINE BREAK>` fields (M4 separator, M5):** Make cannot type `\n` as a newline in
   these value fields. Paste a *real* line break into the field (copy one from any text
   editor). After the first *Run once*, open the M4 output in the inspector and confirm
   the entry renders as multiple lines, not one line with gaps.
2. **Boolean filters** — make sure the Equal-to value is the boolean `true` (picked from
   the mapping/expression editor), not the text `"true"`.
3. **`escapeJSON()`** — available in current Make editors. If yours doesn't offer it,
   substitute `{{replace(trim(1."Publication title"); "\""; "'")}}`-style quote-to-apostrophe
   replaces for every JSON-body insertion (safe, since it removes the characters that
   break JSON strings).
4. **Google Sheets column mapping** — M6/M7/M14 map by header name (`Status`, `PR
   Number`, `PR URL`, `Branch`, `Processed At`, `Notes`). Add those headers (doc 01 §5)
   before the first scheduled run.
5. **First-run check**: set the scenario to *Scheduling OFF*, use **Run once** after a
   test submission, and walk the inspector output of every module — especially M4's
   `entry_yaml` and M5's `new_content` — before trusting a real PR. Doc 04 walks this.
