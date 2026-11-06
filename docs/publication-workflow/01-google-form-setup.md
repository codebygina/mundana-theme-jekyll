# 01 — Google Form & Response Spreadsheet Setup

Manual, one-time setup (~10 minutes). Make.com cannot create Google Forms.

## 1. Create the form

1. Go to <https://forms.google.com> → **Blank form** (＋).
2. Title: **AAII-Axom Publication Submission**.
3. Description (suggested):

> Submit a newly published research paper to be listed on the AAII-Axom website.
> A maintainer reviews every submission before it appears publicly. Fields marked
> with * are required.

## 2. Add the questions — in this exact order

Column order in the linked spreadsheet is determined by question order, and the Make
scenario maps columns **A–M** by position. Do not reorder later.

| # | Question | Type | Required | Options / validation |
|---|---|---|---|---|
| 1 | Publication title | Short answer | ✔ | — |
| 2 | Authors | Paragraph | ✔ | Help text: *Full author list, in publication order, comma-separated.* |
| 3 | Publication venue | Short answer | ✔ | Help text: *Journal or conference name.* |
| 4 | Publication type | Dropdown | ✔ | `Journal` `Conference` `Workshop` `Book Chapter` `Other` — exactly these five labels |
| 5 | Year | Short answer | ✔ | Response validation → *Number* → *Regular expression* → *Matches* → `^(19|20)[0-9]{2}$`, custom error "Enter a 4-digit year" |
| 6 | DOI | Short answer | ✖ | Help text: *Bare DOI, e.g. 10.1000/xyz123 (no URL).* |
| 7 | Publication URL | Short answer | ✖ | Publisher or proceedings page |
| 8 | PDF URL | Short answer | ✖ | Publicly accessible PDF |
| 9 | Abstract | Paragraph | ✖ | — |
| 10 | Keywords | Short answer | ✖ | Comma-separated |
| 11 | Submitted by | Short answer | ✔ | Your full name |
| 12 | Submitter email | Short answer | ✔ | Response validation → *Text* → *Email address* |

## 3. Form settings (⚙ Settings tab)

- **Collect email addresses**: *Off* (question 12 covers it — keeps the form usable by
  collaborators without Google accounts).
- **Limit to 1 response**: *Off* (same reason).
- **Allow response editing**: *On* is fine — edits re-sync to the sheet.

Optional hardening later: restrict the form to your Google Workspace organization.

## 4. Link the response spreadsheet

1. **Responses** tab → **Link to Sheets** (green spreadsheet icon) → **Create a new
   spreadsheet** → name it `AAII-Axom Publication Submission (Responses)`.
2. Open the spreadsheet. Tab name is `Form Responses 1` — keep the default.

## 5. Add tracking columns N–S

In row 1 of `Form Responses 1`, add these headers **before the first Make.com run**
(Make maps columns by header name):

| Col | Header |
|---|---|
| N | `Status` |
| O | `PR Number` |
| P | `PR URL` |
| Q | `Branch` |
| R | `Processed At` |
| S | `Notes` |

The workflow writes only to N–S; columns A–M are the untouched original submission
(timestamp included), as required.

## 6. Share

- Keep the **spreadsheet private** to administrators (it contains submitter emails).
- Share the **form** (Send → 🔗 link) with faculty/researchers who should submit.

## 7. Values Make expects (summary)

- After a test submission, row 2 will contain A–M filled and N–S empty — that empty
  `Status` is what Scenario 1 keys on. Never pre-fill `Status`.
- If a submission is edited in the Form, the Sheet row is updated in place and the
  automation may have already processed the earlier version — flag such rows manually
  in `Notes`.
