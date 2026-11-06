# 03 — Make.com Scenario 2: *Merge Tracker*

Detects when a publication PR is **actually merged**, then updates the response sheet to
`Merged`. A row is never marked merged merely because a PR was created — the status
transition fires only on GitHub's `pull_request` → `closed` + `merged: true` webhook
event.

**Design**: webhook-driven (real-time, ~1–2 ops per PR event, no polling budget spent).
A polling fallback is in §4 if webhooks are not an option.

> Together with Scenario 1 this uses the free plan's 2 active scenarios exactly — no
> headroom for a third active scenario.

## 1. Build the scenario

Create scenario → name `Publication Merge Tracker`.

### M1 — Webhooks ▸ Custom webhook *(trigger)*

1. Add module → *Webhooks → Custom webhook* → **Create a webhook** → name
   `publication-merge-tracker` → copy the generated URL
   (`https://hook.eu2.make.com/…`).
2. In GitHub: repo → **Settings → Webhooks → Add webhook**:
   - **Payload URL**: the copied webhook URL
   - **Content type**: `application/json`
   - **Which events?**: *Let me select individual events* → tick **Pull requests** only
   - **Active**: ✔
3. Back in Make, click *Redetermine data structure* (or send a test event — e.g. open
   and close any PR in the repo) so payload fields become mappable.

### F1 — Filter · label `Merged publication PR`

All conditions joined with **AND**:

| Condition | Operator | Value |
|---|---|---|
| `{{1.event}}` | Text: *Equal to* | `pull_request` |
| `{{1.action}}` | Text: *Equal to* | `closed` |
| `{{1.pull_request.merged}}` | Boolean: *Equal to* | `true` |
| `{{1.pull_request.base.ref}}` | Text: *Equal to* | `test/publications` *(→ `master` at go-live — spot 4/4)* |
| `{{1.pull_request.title}}` | Text: *Begins with* | `[New Publication]` |

The title filter means unrelated PRs merged into the base branch are ignored.

### M2 — Google Sheets ▸ Search Rows

| Setting | Value |
|---|---|
| Connection / Spreadsheet / Sheet | as in Scenario 1 |
| Search for rows where | column `PR Number` **equals** `{{1.pull_request.number}}` |

Outputs the matching submission row (the one Scenario 1 stamped with this PR number).

### M3 — Google Sheets ▸ Update a Row

Key: Spreadsheet/Sheet as above, Row number = `{{2.__ROW_NUMBER__}}`.

| Column | Value |
|---|---|
| `Status` | `Merged` |
| `Processed At` | `{{now}}` |
| `Notes` | `Merged at {{1.pull_request.merged_at}} by {{1.pull_request.merged_by.login}}` |

*(If `merged_by` isn't exposed in your payload structure, drop it — it's cosmetic.)*

### M4 — Gmail ▸ Send an email *(optional)*

To: `{{2."Submitter email"}}` · Subject: `Your publication is now listed on the AAII-Axom
website` · Content: merge link `{{1.pull_request.html_url}}` + the publications page URL
`https://aaii-axom.github.io/publications.html` (site rebuilds automatically via GitHub
Pages within a couple of minutes of the merge).

## 2. Error handling

| Concern | Implementation |
|---|---|
| PR merged while webhook down | GitHub retries failed deliveries up to 10 times over ~2 days (repo → Settings → Webhooks → Recent deliveries shows them). Additionally, if a row shows `PR Created` for more than a day after you know it merged, press *Redeliver* on the `closed` delivery. |
| No sheet row found (M2 empty) | Add an error handler ▸ *Ignore* on M2… actually M2 with zero results simply ends that route. Safe: nothing to update. |
| Duplicate deliveries | Idempotent by nature: setting `Merged` twice changes nothing. |
| Logs | `Status` + `Notes` columns carry the merge timestamp; scenario history has the payloads. |

## 3. Free-plan note

Custom webhooks are instant triggers — available on the free plan and not subject to the
15-minute scheduling floor. Ops: one trigger op per PR event the repo emits (opened /
closed / reopened…); the filter stops non-merge events before any paid module runs. At
lab-scale PR volume this is single-digit ops per month.

## 4. Fallback: polling variant (no repo webhook)

If you cannot add a webhook, replace M1 with:

- **Trigger**: *Schedule app ▸ Basic trigger* module, with the scenario's scheduling
  clock set to **every 4 hours** (≈180 ops/month).
- **M1b HTTP GET**
  `https://api.github.com/repos/AAII-Axom/AAII-Axom.github.io/pulls?state=closed&sort=updated&direction=desc&per_page=10`
  with the usual auth headers, Parse response = Yes.
- **Iterator** over the array, then the same filter conditions as F1 using
  `{{1.merged}}`, `{{1.base.ref}}`, `{{1.title}}`, `{{1.number}}` — merge detection is
  up to 4 h late instead of instant.

Everything downstream (Search Rows → Update Row → email) is identical.
