# Workflow: Creative leadership job search (daily)

First run: 2026-11-05. The full research brief is in `workflows/job-search/BRIEF.md`.
That file covers the candidate profile, filters, scoring, and output format.

## 1. Trigger
Daily. Notify Ben only when a new A+ or A role appears. Otherwise report
"no new qualifying opportunities".

## 2. Steps
1. **Discover (LinkedIn guest search).** Run
   `python3 -I workflows/job-search/li_search.py <outdir> r259200` (3 days) or `r1209600` (14 days).
   It runs about 24 title keywords on LinkedIn with Remote and United States filters, drops
   closed or non-full-time posts, and saves each posting's description, salary, Texas mentions
   and state restrictions to `<outdir>/results.json`.
   Each result carries its individual LinkedIn URL (`/jobs/view/<id>/`).
2. **Filter.** `python3 -I workflows/job-search/filter.py <outdir>/results.json`
   lists open full-time roles whose published pay ceiling is at least $125k.
3. **Dedupe** against `workflows/job-search/tracker.csv`, the brief's
   "previously identified" list, and `workflows/job-search/seen.md`.
4. **Screen by hand.** Read the full description of each survivor and confirm:
   - truly remote, with no state list that excludes Texas (a LinkedIn city label doesn't settle this)
   - salary is base pay, not OTE
   - seniority is realistic
   - creative scope, not pure UX or copy
5. **Verify on the official ATS.** Fetch the employer's posting page:
   - Lever, Greenhouse and Rippling pages render server-side.
   - Ashby: read the board HTML (`jobs.ashbyhq.com/<co>`), which embeds the
     postings as JSON; the individual posting HTML includes `descriptionHtml`.
6. **Rankings.** Check the specific award and year (Fortune/GPTW, Inc., Built In,
   Forbes, Comparably). Never assume one.
7. **Score** with the brief's weights. Add rows to `tracker.csv` and the Google Sheet
   ([Job Search Master Tracker](https://docs.google.com/spreadsheets/d/18u5Zi9IPvAW7UpZcn8u_K0jq6-_3k3pnufIvqRn8w34/edit), in the Drive account the connector uses). Write `workflows/job-search/reports/<date>.md`.

## 3. Gotchas learned
- Cloud network: the session needs the `workflow-automation-assistant` environment, which
  allows LinkedIn, Lever, Greenhouse, Ashby, Rippling and Built In. The API hosts
  (`api.lever.co`, `api.ashbyhq.com`, `boards-api.greenhouse.io`) are NOT allowed, so read the HTML pages.
- WebFetch (web-fetch subagent) failed on every job host. Use curl through Bash instead.
- Rippling (Forbes Advisor): `payRangeDetails: []` means no published salary, so the role is excluded.
- Agencies post one role under several titles (Directive: three titles, one job).
  Keep one row and note the others.
- Jobgether and other aggregators hide the employer. Mark it unverified.
- Proof publishes "total cash" ranges. Flag these, since the brief requires base pay.
- Google Sheets editor connector isn't on: the master sheet can only be created
  via Drive, not edited in place. Turn on the Sheets connector to append rows daily.

## 4. Judgment calls (Ben)
Which roles to apply to, tailoring materials, any outreach.

## 5. Never
Apply, message recruiters, or share the tracker without Ben's OK.
