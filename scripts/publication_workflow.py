#!/usr/bin/env python3
"""Publication submission automation (GitHub-native path).

Usage — invoked by .github/workflows/publication-pr.yml:
    python3 scripts/publication_workflow.py submission   # on issues(opened)
    python3 scripts/publication_workflow.py merge        # on pull_request(closed)

Everything it needs comes from the workflow event JSON (GITHUB_EVENT_PATH), the
built-in GITHUB_TOKEN (consumed by the gh CLI) and git. No external credentials
or services.
"""

import json
import os
import re
import subprocess
import sys
from datetime import date

REPO = os.environ.get("GITHUB_REPOSITORY", "AAII-Axom/AAII-Axom.github.io")
DATA_FILE = "_data/publications.yml"
FORM_MARKER = "### Publication title"  # first field header of the issue form
SITE_PAGE = "https://aaii-axom.github.io/publications.html"

# issue-form label (lowercased) -> canonical field name
ALIASES = {
    "publication title": "title",
    "authors": "authors",
    "publication venue": "venue",
    "publication type": "type",
    "year": "year",
    "doi": "doi",
    "publication url": "url",
    "pdf url": "pdf",
    "abstract": "abstract",
    "keywords": "keywords",
    "submitted by": "submitted_by",
}

TYPE_MAP = [
    ("journal", "journal"),
    ("conference", "conference"),
    ("workshop", "workshop"),
    ("book", "book-chapter"),
    ("other", "other"),
]

LABELS = {
    "pr-open": ("publication/pr-open", "0E8A16"),
    "published": ("publication/published", "1D76DB"),
    "invalid": ("publication/invalid", "D93F0B"),
    "duplicate": ("publication/duplicate", "9A6700"),
}


def sh(*args, check=True):
    """Run a command, return stdout (stripped). Raises on failure when check."""
    r = subprocess.run(list(args), capture_output=True, text=True)
    if check and r.returncode != 0:
        raise RuntimeError(
            "command failed (%d): %s\n%s" % (r.returncode, " ".join(args), r.stderr)
        )
    return r.stdout.strip()


def event():
    with open(os.environ["GITHUB_EVENT_PATH"], encoding="utf-8") as fh:
        return json.load(fh)


# ---------------------------------------------------------------- parsing

def parse_issue(body):
    """Parse an issue-form body into {field: value}.

    Issue forms render each field as '### <Label>' followed by the value
    (input values are **bolded**, textareas are raw). '_No response_' means
    the optional field was left empty.
    """
    fields = {}
    for section in re.split(r"^### ", body, flags=re.MULTILINE)[1:]:
        lines = section.splitlines()
        label = lines[0].strip().lower()
        value = "\n".join(lines[1:]).strip()
        if value.startswith("**") and value.endswith("**") and len(value) > 4:
            value = value[2:-2].strip()
        if value == "_No response_":
            value = ""
        key = ALIASES.get(label, label)
        if key not in fields:  # injected '### ' lines inside a textarea lose
            fields[key] = value
    return fields


# ----------------------------------------------------------- normalization

def normalize_type(value):
    value = value.strip().lower()
    for needle, canon in TYPE_MAP:
        if needle in value:
            return canon
    return "other"


def normalize_doi(value):
    value = re.sub(
        r"^(https?://(dx\.)?doi\.org/|doi:)", "", value.strip(), flags=re.I
    ).replace(" ", "")
    return value.lower()


def norm_text(s):
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


# ------------------------------------------------------------- validation

def validate(f):
    problems = []
    if not f.get("title"):
        problems.append("**Publication title** is required.")
    if not f.get("authors"):
        problems.append("**Authors** is required.")
    if not f.get("venue"):
        problems.append("**Publication venue** is required.")
    if not f.get("type"):
        problems.append("**Publication type** is required.")
    year = f.get("year", "").strip()
    if not year:
        problems.append("**Year** is required.")
    elif not re.fullmatch(r"(19|20)\d{2}", year):
        problems.append("**Year** must be a 4-digit year, e.g. 2026.")
    if not any(f.get(k, "").strip() for k in ("doi", "url", "pdf")):
        problems.append(
            "At least one of **DOI**, **Publication URL** or **PDF URL** is "
            "required so reviewers can verify the paper (a DOI alone is never "
            "mandatory)."
        )
    return problems


def find_duplicates(existing, f):
    """Return a human-readable reason if the publication looks already listed."""
    blob = existing.lower()
    squashed = norm_text(existing)
    doi = normalize_doi(f.get("doi", ""))
    title = norm_text(f.get("title", ""))
    first_author = f.get("authors", "").split(",")[0].strip().lower()
    year = f.get("year", "").strip()
    if doi and doi in blob:
        return "its DOI (`%s`) is already in the publication list" % doi
    if title and title in squashed:
        return (
            "a publication with the same (or very similar) title is already "
            "in the list"
        )
    if first_author and year and first_author in blob and year in blob:
        return (
            "the first author (`%s`) already has a `%s` entry — please "
            "double-check it is not the same paper" % (first_author, year)
        )
    return None


# ------------------------------------------------------------- entry build

def y(value):
    """YAML-safe double-quoted scalar (JSON strings are valid YAML)."""
    return json.dumps(str(value))


def build_entry(f, submitted_by):
    year = f["year"].strip()
    lines = [
        "- title: %s" % y(f["title"]),
        "  authors: %s" % y(f["authors"]),
        "  venue: %s" % y(f["venue"]),
        "  type: %s" % y(normalize_type(f["type"])),
        "  year: %s" % year,
    ]
    for key in ("doi", "url", "pdf"):
        value = f.get(key, "").strip()
        if key == "doi" and value:
            value = normalize_doi(value)  # store the bare DOI
        if value:
            lines.append("  %s: %s" % (key, y(value)))
    if f.get("abstract"):
        lines.append("  abstract: %s" % y(f["abstract"]))
    if f.get("keywords"):
        lines.append("  keywords: %s" % y(f["keywords"]))
    lines.append("  submitted_by: %s" % y(submitted_by))
    lines.append("  date_added: %s" % y(date.today().isoformat()))
    return "\n".join(lines)


def branch_name(number, title):
    slug = re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", title.lower()))
    slug = slug.strip("-")[:40].rstrip("-")
    return "publication/issue-%d%s" % (number, "-" + slug if slug else "")


def pr_body(f, submitted_by, number):
    def line(label, value):
        return "- **%s:** %s" % (label, value if value else "—")

    return """## New Publication Submission

A new publication has been submitted through the publication submission issue form.

### Publication Details

{title}
{authors}
{venue}
{ptype}
{year}
{doi}
{url}
{pdf}

### Changes
- Appended the publication to `_data/publications.yml` (canonical list).
- Rendering, ordering and existing entries untouched — the page sorts by year.

### Submitted By
- **Name:** {submitted_by}
- **Submission issue:** #{number}

Closes #{number}

### Review Checklist
- [ ] Publication details are accurate.
- [ ] Author order and spelling are correct.
- [ ] Publication is not already listed.
- [ ] Formatting follows repository conventions.
""".format(
        title=line("Title", f["title"]),
        authors=line("Authors", f["authors"]),
        venue=line("Venue", f["venue"]),
        ptype=line("Type", normalize_type(f["type"])),
        year=line("Year", f["year"].strip()),
        doi=line("DOI", normalize_doi(f.get("doi", ""))),
        url=line("Paper URL", f.get("url", "")),
        pdf=line("PDF", f.get("pdf", "")),
        submitted_by=submitted_by,
        number=number,
    )


# ------------------------------------------------------------ gh helpers

def ensure_labels():
    for name, color in LABELS.values():
        sh("gh", "label", "create", name, "--color", color, check=False)


# ------------------------------------------------------------------ modes

def cmd_submission(ev):
    issue = ev["issue"]
    number = issue["number"]
    body = issue.get("body") or ""
    if FORM_MARKER not in body:
        print("not a publication-submission issue; nothing to do")
        return

    ensure_labels()
    f = parse_issue(body)

    problems = validate(f)
    if problems:
        comment = (
            "### :warning: Submission needs fixes\n\n"
            "This submission could not be processed:\n\n"
            + "\n".join("- %s" % p for p in problems)
            + "\n\nPlease **open a new submission issue** with the corrections — "
            "this one is kept for reference."
        )
        sh("gh", "issue", "comment", str(number), "--body", comment)
        sh("gh", "issue", "edit", str(number), "--add-label", LABELS["invalid"][0])
        return

    f["year"] = f["year"].strip()
    submitted_by = (
        f.get("submitted_by", "").strip() or "@" + issue["user"]["login"]
    )
    base = os.environ.get("PUBLICATION_BASE_BRANCH", "test/publications")

    sh("git", "config", "user.name", "github-actions[bot]")
    sh("git", "config", "user.email",
       "41898282+github-actions[bot]@users.noreply.github.com")
    sh("git", "fetch", "--quiet", "origin", base)

    r = subprocess.run(
        ["git", "show", "FETCH_HEAD:%s" % DATA_FILE],
        capture_output=True, text=True,
    )
    existing = r.stdout if r.returncode == 0 else ""

    dup = find_duplicates(existing, f)
    if dup:
        comment = (
            "### :repeat: Possible duplicate — manual review\n\n"
            "No pull request was created: %s.\n\n"
            "A maintainer will take a look. If this is genuinely a new "
            "publication, please reply here or open a corrected submission."
            % dup
        )
        sh("gh", "issue", "comment", str(number), "--body", comment)
        sh("gh", "issue", "edit", str(number), "--add-label",
           LABELS["duplicate"][0])
        return

    branch = branch_name(number, f["title"])
    sh("git", "checkout", "--quiet", "-B", branch, "FETCH_HEAD")
    with open(DATA_FILE, "a", encoding="utf-8") as fh:
        if existing and not existing.endswith("\n"):
            fh.write("\n")
        fh.write("\n" + build_entry(f, submitted_by) + "\n")
    sh("git", "add", DATA_FILE)
    sh("git", "commit", "--quiet", "-m",
       "Add publication: %s (%s)" % (f["title"], f["year"]))
    sh("git", "push", "--quiet", "origin", branch)

    pr_url = sh(
        "gh", "pr", "create",
        "--base", base,
        "--head", branch,
        "--title", "[New Publication] %s (%s)" % (f["title"], f["year"]),
        "--body", pr_body(f, submitted_by, number),
    )
    sh("gh", "issue", "comment", str(number), "--body",
       "### :white_check_mark: Pull request created\n\n%s\n\nA maintainer "
       "will review it. You will be notified here when it is merged and the "
       "publication goes live." % pr_url)
    sh("gh", "issue", "edit", str(number), "--add-label", LABELS["pr-open"][0])


def cmd_merge(ev):
    pr = ev["pull_request"]
    if not pr.get("title", "").startswith("[New Publication]"):
        return
    body = pr.get("body") or ""
    m = re.search(r"#(\d+)", body)
    if not m:
        print("no submission issue referenced in PR body; nothing to do")
        return
    number = m.group(1)

    if pr.get("merged"):
        sh("gh", "issue", "close", number, "--comment",
           "### :tada: Published\n\nThe pull request was merged — the "
           "publication is now part of the list. The site rebuilds "
           "automatically: %s" % SITE_PAGE)
        sh("gh", "issue", "edit", number,
           "--add-label", LABELS["published"][0],
           "--remove-label", LABELS["pr-open"][0])
        # tidy up the merged head branch (harmless if already deleted)
        sh("gh", "api", "-X", "DELETE",
           "repos/%s/git/refs/heads/%s" % (REPO, pr["head"]["ref"]), check=False)
    else:
        sh("gh", "issue", "comment", number, "--body",
           "The pull request for this submission was closed without merging. "
           "The issue stays open for re-review — see the PR discussion for "
           "details.")


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    ev = event()
    if mode == "submission":
        cmd_submission(ev)
    elif mode == "merge":
        cmd_merge(ev)
    else:
        sys.exit("usage: publication_workflow.py submission|merge")


if __name__ == "__main__":
    main()
