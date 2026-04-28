---
name: portfolio-meeting-prep
description: Generate an interactive HTML meeting agenda and prep document from the latest portfolio dashboard and daily team audits for portfolio review meetings.
argument-hint: [duration in minutes, e.g. 30m or 45m — defaults to 30m]
allowed-tools: Read, Glob, Grep, Bash, Write, Agent
---

<!-- markdownlint-disable MD013 -->

# Portfolio Meeting Prep Skill

Generate a self-contained, interactive HTML meeting agenda that compiles data from the latest portfolio dashboard and all team audit reports into a structured, time-boxed document for portfolio review meetings.

Do not use this skill for:

- Generating or re-computing portfolio dashboards (use `portfolio-health`)
- Running individual project audits (use `ado-safe-audit` or `git_iteration_audit`)
- Sending the meeting prep via email (use `portfolio-email`)

## Authority and precedence

This skill is the authoritative source for:

- Meeting agenda structure, topic ordering, and time allocation
- HTML meeting prep template (layout, CSS, SVG charts, interactive elements)
- Discussion point generation from audit data
- Action item compilation and prioritization

This skill defers to:

- `portfolio-health` SKILL.md for portfolio scoring methodology (UPS formula, risk bands)
- `ado-safe-audit` SKILL.md for how ADO scores are computed
- `git_iteration_audit` SKILL.md for how Git scores (ICS, SGPI, HCI) are computed
- Individual workspace `CLAUDE.md` files for team metadata
- Memory files (`memory/user_*.md`) for attendee information

## Accepted inputs

### Default (30 minutes)

```text
/portfolio-meeting-prep
```

### Custom timebox

```text
/portfolio-meeting-prep 45m
/portfolio-meeting-prep 60m
```

The time budget is distributed proportionally across all agenda topics. Default is 30 minutes.

## Required workflow

### Step 1 — Determine meeting parameters

- Parse optional duration argument (default: 30 minutes)
- Read memory files to identify attendees (Ramon Aseniero — CEO, Karl Caumban — PDM)
- Determine current date and iteration context from the latest portfolio dashboard

### Step 2 — Find the latest portfolio dashboard

```text
Glob pattern: portfolio_report/PORTFOLIO_*.html
```

Select the most recent file by filename timestamp. Exclude `_SUMMARY.html`, `_TREND`, and `_MEETING_PREP` files.

### Step 3 — Find prior portfolio dashboards for trend data

Collect up to 7 most recent portfolio dashboard files to build the mean/median score trend. Extract from each:

- Portfolio Mean
- Portfolio Median
- Teams at Risk count
- Date and iteration day

### Step 4 — Find the latest audit for each team

```text
Glob patterns:
  ado_*/audit/AUDIT_*.md
  git_*/audit/AUDIT_*.md
```

For each workspace, select the most recent audit file. Extract:

- Overall / UPS score
- Risk band
- Trend (delta from prior audit)
- Key findings (top 2-3)
- Top blocker or P0 recommendation
- Any pending action items
- Team contributor names (for bus factor analysis)

### Step 5 — Check for pending todo files

```text
Glob pattern: ado_*/todo/*.md, git_*/todo/*.md
```

Reference any existing todo files in the action items section.

### Step 6 — Analyze and categorize

Group teams into tiers:

| Tier | Band | Score Range |
|------|------|-------------|
| Low Risk | Green | >= 80 |
| Moderate | Yellow | 60 - 79.9 |
| High Risk | Orange | 40 - 59.9 |
| Critical | Red | < 40 |

Identify:

- **Quick wins:** Actions with high impact and low effort (< 30 min)
- **Escalations:** Items unactioned across multiple audits
- **Structural risks:** Recurring patterns (bus factor, backlog debt, engineering gaps)
- **Decisions needed:** Items requiring PDM sign-off or direction

### Step 7 — Calculate time allocation

Distribute the meeting timebox across 7 topics. Default 30-minute allocation:

| # | Topic | Default | Purpose |
|---|-------|---------|---------|
| 1 | Portfolio Snapshot + Scorecard | 3 min | Context setting |
| 2 | Critical & High Risk Teams | 8 min | Deep dive on at-risk teams |
| 3 | Quick Wins & Escalations | 5 min | Immediate actions |
| 4 | Structural Risks | 5 min | Backlog debt, engineering gaps, bus factor |
| 5 | Decisions | 4 min | Items needing PDM sign-off |
| 6 | Action Items & Owners | 3 min | Assign P0/P1 actions |
| 7 | Wrap-up & Next Steps | 2 min | PI readiness, follow-up |

For custom durations, scale proportionally:

- 45 min: multiply each by 1.5
- 60 min: multiply each by 2.0
- Round to nearest minute; ensure total matches requested duration

Include a facilitator tip: "Topics 2-3 carry the most value. If time runs short, skip Topic 4 and capture structural risks as async follow-ups."

### Step 8 — Generate HTML

Create a self-contained HTML file using the design reference at `portfolio_report/PORTFOLIO_MEETING_PREP_20260402.html`. The HTML must include:

#### Required visual elements

1. **Header** — Dark gradient banner with meeting title, iteration info, date, attendees, duration
2. **Agenda timeline bar** — Color-coded horizontal bar showing all topics with time allocations
3. **Metric cards** — Portfolio Mean, Median, Teams at Risk with trend deltas
4. **SVG trend chart** — Line chart of mean score over available data points (up to 7). Include:
   - Green dashed line at score 80 (Low Risk threshold)
   - Color-coded data points (green for peaks, red for current if declining)
   - X-axis: dates, Y-axis: scores 50-80 range
5. **Score bar chart** — Horizontal bars for all teams, color-coded by risk band, with risk pills
6. **Risk blocks** — Bordered blocks for Critical and High Risk teams with findings
7. **Quick win cards** — Card grid with impact, effort, owner per win
8. **Structural risk grid** — 3-column grid (backlog debt, engineering gaps, bus factor)
9. **Decision checkboxes** — Interactive checkboxes (toggleable via `onclick`) with urgency pills
10. **Action item tables** — Grouped by priority (Do Today, Before Sprint Close, PI Planning)
11. **Impact comparison** — Side-by-side cards showing "Act Today" vs "No Action" outcomes
12. **Footer** — Source attribution, risk band legend with colored dots

#### HTML rules

- Self-contained: no external CDN, no `<script src>`, no `<link>` to external CSS
- Inline `<style>` block in `<head>` is acceptable (this is for browser viewing, not email)
- SVG for charts (no canvas, no chart libraries)
- Interactive checkboxes use inline `onclick` handlers only
- Print-friendly: include `@media print` styles
- Responsive: works on both desktop and tablet screens

#### Color reference

| Element | Hex |
|---------|-----|
| Low Risk / Green | `#22c55e` |
| Moderate / Yellow | `#eab308` |
| High Risk / Orange | `#f97316` |
| Critical / Red | `#ef4444` |
| Header gradient | `linear-gradient(135deg, #1e1b4b 0%, #312e81 100%)` |
| Body text | `#113069` |
| Background | `#faf8ff` |
| Card background | `#ffffff` |
| Muted text | `#6b7280` |
| ADO pill | bg `#e0f2fe`, text `#0369a1` |
| Git pill | bg `#f3e8ff`, text `#7e22ce` |
| Trend up | `#16a34a` |
| Trend down | `#dc2626` |
| Trend flat | `#9ca3af` |
| Note background | `#fffbeb` |
| Note text | `#92400e` |

#### Agenda topic colors (for timeline bar)

| Topic | Color |
|-------|-------|
| Snapshot | `#6366f1` |
| At-Risk Teams | `#ef4444` |
| Quick Wins | `#22c55e` |
| Structural Risks | `#f97316` |
| Decisions | `#8b5cf6` |
| Actions | `#0ea5e9` |
| Wrap-up | `#64748b` |

### Step 9 — Write output

Save the HTML file to:

```text
portfolio_meeting_agenda/PORTFOLIO_MEETING_AGENDA_YYYYMMDD.html
```

Where `YYYYMMDD` is today's date (e.g., `PORTFOLIO_MEETING_AGENDA_20260402.html`).

If a file with the same date already exists, append a time suffix:

```text
portfolio_meeting_agenda/PORTFOLIO_MEETING_AGENDA_YYYYMMDD_HHMM.html
```

### Step 10 — Report completion

Tell the user:

- File path of the generated HTML
- Number of teams covered
- Meeting duration
- How many action items were identified
- Any data gaps or missing audits

## Content generation guidelines

### Discussion points

- Frame for a CEO-to-PDM conversation (strategic, not tactical)
- Lead with the highest-impact items
- Flag items that have been unactioned across multiple audits (escalation candidates)
- Distinguish between systemic issues and seasonal/one-time events
- Always include the "act vs no action" impact framing

### Action items

- Every action must have: description, owner, estimated time
- Group as P0 (today), P1 (before sprint close), P2 (next PI planning)
- Quick wins (< 30 min, high impact) should be called out separately
- Reference todo files when they exist

### Scoring artifacts

- Flag scores that are artifacts of rubric limitations (e.g., zero-denominator after 100% closure)
- Distinguish between genuine delivery failures and scoring anomalies
- Note seasonal impacts (holidays, IP sprints) that suppress scores temporarily

## Output policy

- Output location: `portfolio_meeting_agenda/` at repo root
- Format: Self-contained HTML only
- Naming: `PORTFOLIO_MEETING_AGENDA_YYYYMMDD[_HHMM].html`
- Never overwrite existing files
- Do not generate Markdown, PDF, or chart image files
- Do not modify any audit reports or dashboard files

## Failure behavior

- If no portfolio dashboard exists: Tell the user to run `/portfolio-health` first
- If an individual team audit is missing: Include the team with "No recent audit" note, do not block generation
- If fewer than 3 portfolio reports exist: Skip trend chart, note insufficient data
- If all audits are older than 7 days: Warn that data may be stale

## Completion checklist

1. Latest portfolio dashboard identified and read
2. Prior dashboards read for trend data (up to 7)
3. Latest audit for each team read and extracted
4. Todo files checked for pending action items
5. Teams grouped into risk tiers
6. Quick wins, escalations, and structural risks identified
7. Time allocation calculated for requested duration
8. HTML generated with all required visual elements
9. SVG trend chart renders correctly
10. Interactive checkboxes work (onclick toggle)
11. Print styles included
12. File saved to `portfolio_meeting_agenda/` with correct naming
13. No external dependencies in HTML
14. Completion report shown to user
